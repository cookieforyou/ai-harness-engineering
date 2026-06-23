---
name: rollback-procedures
description: "回滚流程标准，定义数据库、应用、配置和基础设施的分步回滚操作流程与验证清单"
type: standard
version: "2.0.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-23
status: active
language: "zh-CN"
tags: ['standard', 'rollback', 'recovery', 'database', 'disaster-recovery']
---

# 回滚流程

> 本规范提供 E2E Delivery Harness 中各组件类型的分步回滚操作流程。决策标准见 [rollback-strategy.md](../standards/rollback-strategy.md)。审查基准见 [harness-engineering.md](../harness-engineering.md)。

## 1. 通用回滚流程

所有回滚操作遵循以下通用步骤，后续各节按组件类型提供细化流程：

```
Phase 1: 确认回滚
  ├── 确认回滚条件满足（参考 rollback-strategy.md 决策矩阵）
  ├── 通知相关干系人（通道: P0/P1 电话 + Slack, P2 仅 Slack）
  └── 禁用功能开关（如有）以避免新流量进入

Phase 2: 执行回滚
  ├── 按组件类型执行对应流程（详见以下各节）
  ├── 监控恢复进度（仪表盘 + 日志）
  └── 记录操作时间戳与执行人

Phase 3: 验证回滚
  ├── 健康检查端点确认（liveness + readiness + business health）
  ├── 核心业务流程冒烟测试（自动化 + 手工）
  ├── 监控指标回归基线（错误率、延迟、吞吐量）
  └── 数据库数据完整性检查（如涉及数据回滚）

Phase 4: 事后处理
  ├── 更新 incident 时间线与状态
  ├── 标记原版本、记录失败根因
  ├── 创建跟踪 issue 用于复盘 (postmortem)
  └── 复盘会安排在 T+72 小时内
```

## 2. 数据库回滚流程

### 2.1 原理

数据库回滚分为 **Schema 回滚** 和 **数据回滚**，两者可以独立执行。

### 2.2 Schema 回滚

```
1. 确认当前 schema 版本号
2. 执行回滚迁移脚本:
   ┌────────────────────────────────────────────┐
   │ # Flyway 示例                              │
   │ flyway undo -url=jdbc:postgresql://...     │
   │                                             │
   │ # Alembic 示例                             │
   │ alembic downgrade -1                       │
   │                                             │
   │ # 手动 SQL 示例                            │
   │ ALTER TABLE orders DROP COLUMN IF EXISTS   │
   │   discount_code;                           │
   └────────────────────────────────────────────┘
3. 验证 schema 版本已恢复:
   ┌────────────────────────────────────────────┐
   │ flyway info                                │
   │ Current version: 1.0.15                    │
   │ → 确认回退到期望版本                         │
   └────────────────────────────────────────────┘
4. 运行集成测试验证数据库兼容性
5. 确认业务查询正常
```

**注意事项**:
- 禁止 DROP COLUMN 后马上回滚 — 如果数据已删除则无法恢复
- 回滚 migration 前确认没有新写入依赖新 schema
- 回滚脚本必须与正向 migration 同时提交（同一 PR）

### 2.3 数据回滚

```
1. 确认数据损坏范围与影响时间窗口
2. 选择恢复策略:
   ├── 事务级: 从 WAL 日志回放 (Point-in-Time Recovery)
   ├── 表级: 从最近备份恢复该表
   ├── 实例级: 切换只读副本为主库
   └── 应用级: 执行补偿事务 (Compensating Transaction)
3. 执行恢复操作
4. 验证数据一致性（行数校验、checksum、业务规则验证）
5. 通知受影响的上游服务清除本地缓存
```

### 2.4 数据库回滚前置条件

- [ ] 每个迁移脚本都有对应的回滚脚本（向上 + 向下）
- [ ] 数据库快照在迁移前自动执行（staging/production）
- [ ] 只读副本可用于时间点恢复 (PITR)
- [ ] 迁移脚本遵循幂等性（可多次执行）

## 3. 应用回滚流程

### 3.1 无状态服务（蓝绿部署）

```
1. 确认当前活跃版本与备用版本:
   ┌────────────────────────────────────────────┐
   │ k8s: kubectl get deployments               │
   │      → 确认 LKG 版本的 image tag           │
   │                                             │
   │ AWS: 查看 Beanstalk 版本标签               │
   └────────────────────────────────────────────┘
2. 执行蓝绿切换:
   ┌────────────────────────────────────────────┐
   │ # 负载均衡器切换（AWS ALB）                │
   │ aws elbv2 modify-listener \               │
   │   --listener-arn ...                       │
   │   --default-actions '...' reverse          │
   │                                             │
   │ # Kubernetes                              │
   │ kubectl rollout undo deployment/web        │
   │   --to-revision=<LKG_REVISION>              │
   └────────────────────────────────────────────┘
3. 验证健康检查 (参见 health-check-guidelines.md)
4. 确认监控指标回归正常
5. 记录回滚版本号与时间
```

### 3.2 有状态服务（滚动回滚）

```
1. 暂停消息消费（如有消息队列）
2. 暂停调度新请求（从服务发现摘除）
3. 逐实例或逐批次回滚:
   ├── 分批回滚 (batch size = 2, 间隔 30s)
   ├── 每批验证基础健康
   └── 异常批次暂停回滚流程
4. 验证全部实例恢复正常
5. 恢复服务发现注册
6. 恢复消息消费
```

**注意**: 有状态服务回滚涉及数据兼容性，必须在回滚前确认数据模型向后兼容。

### 3.3 前端应用（SPA/SSR）

```
1. 确认 CDN 缓存策略
2. 重新部署前一个版本的构建包
3. 清除 CDN 缓存:
   ┌────────────────────────────────────────────┐
   │ # CloudFront 缓存清除                      │
   │ aws cloudfront create-invalidation \       │
   │   --distribution-id <ID> \                │
   │   --paths "/*"                             │
   └────────────────────────────────────────────┘
4. 确认新版 JS/CSS 文件已回退
5. 浏览器硬刷新验证（或使用 service worker 控制）
```

## 4. 配置回滚流程

### 4.1 外部配置中心

```
1. 登录配置中心（Apollo/Nacos/Consul/Spring Cloud Config）
2. 查看配置变更历史，确认上一个稳定版本
3. 执行配置版本回退（一键回滚到前一个版本）
4. 通知服务刷新配置（热加载或触发重启）
5. 验证配置生效:
   ┌────────────────────────────────────────────┐
   │ curl /actuator/health                      │
   │ curl /actuator/env | grep <配置项>          │
   └────────────────────────────────────────────┘
```

### 4.2 环境变量 / 本地配置文件

```
1. 从制品库取回上一个版本的配置备份
2. 使用配置管理工具 (Ansible/Helm/Terraform) 应用配置
3. 重启受影响服务实例
4. 验证配置正确加载
```

## 5. 基础设施回滚流程

### 5.1 Infrastructure as Code (Terraform)

```
1. 定位上一个稳定的 state 版本:
   ┌────────────────────────────────────────────┐
   │ terraform state list | grep <受影响的资源>   │
   │ terraform state show <资源>                │
   │ terraform plan -refresh-only               │
   └────────────────────────────────────────────┘
2. 回滚到指定版本:
   ┌────────────────────────────────────────────┐
   │ terraform workspace select production      │
   │ terraform apply -auto-approve              │
   │   -state=<上一版本 state 文件>               │
   └────────────────────────────────────────────┘
3. 验证基础设施状态:
   ┌────────────────────────────────────────────┐
   │ terraform plan -detailed-exitcode          │
   │ → 确认无 diff (已回滚到期望状态)              │
   └────────────────────────────────────────────┘
```

### 5.2 Kubernetes 清单

```
kubectl rollout undo deployment/<name>
kubectl rollout status deployment/<name>
```

## 6. 回滚失败处理

回滚操作本身也可能失败。以下是对策：

| 失败场景 | 原因 | 行动 |
|----------|------|------|
| 数据库回滚迁移失败 | 迁移脚本有 bug 或冲突 | 手动执行修复 SQL，联系 DBA |
| 容器镜像不在制品库 | 制品保留策略已删除旧版本 | 从备份存储重新推送，或重新构建目标版本的镜像 |
| 配置回滚后服务无法启动 | 配置依赖了新功能代码 | 同时回滚代码 + 配置，检查版本兼容性矩阵 |
| 蓝绿切换负载均衡器失败 | 备用环境未就绪 | 手动调整 DNS/路由指向备用集群 |
| 数据回档后仍有不一致 | 回档窗口设置不正确 | 执行更精细的 PITR，准备数据核对脚本 |

## 7. 回滚后验证清单

以下步骤在回滚完成后必须执行：

- [ ] 所有健康检查端点返回 200 (liveness + readiness + business health)
- [ ] 核心 API 返回预期结果（自动化测试通过）
- [ ] 业务指标（订单量、转化率）恢复到基线水平
- [ ] 错误率恢复到回滚前水平（比基线差值 < 1%）
- [ ] 日志中无持续 ERROR 级别日志
- [ ] 数据一致性校验通过（行数对比、checksum）
- [ ] 告警已恢复（Alert Fatigue 除外）
- [ ] 回滚操作已记录到变更管理系统

## 相关资产

- [asset-model.md](../standards/asset-model.md)
- [authoring-checklist.md](../standards/authoring-checklist.md)
- [rollback-strategy.md](../standards/rollback-strategy.md)
- [deployment-best-practices.md](../standards/deployment-best-practices.md)
- [health-check-guidelines.md](../standards/health-check-guidelines.md)
