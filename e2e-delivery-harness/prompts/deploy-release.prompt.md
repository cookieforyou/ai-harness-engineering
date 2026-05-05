---
name: deploy-release
description: 部署发布提示词，用于规划和执行应用部署
type: deployment
version: "1.1.0"
stage: deployment
---

# Deploy and Release

> **版本**: 1.1.0 | **适用阶段**: 部署发布 | **预计工时**: 1-3小时

## Input Variables

> AI 在执行前必须确认以下变量已填充

| 变量名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|------|
| `project_name` | string | 是 | 项目名称 | "电商订单系统" |
| `version` | string | 是 | 部署版本 | "v1.0.0" |
| `deploy_package` | string | 是 | 部署包路径 | "/builds/app.tar" |
| `target_env` | enum | 是 | 目标环境 | DEV/STAGING/PROD |
| `cluster_info` | object | 否 | 集群信息 | 见 ClusterInfo 结构 |
| `test_report` | string | 是 | 测试报告路径 | "test-report.md" |
| `rollback_version` | string | 是 | 回滚目标版本 | "v0.9.0" |
| `deployment_window` | datetime | 是 | 部署时间窗口 | "2024-01-15 02:00" |
| `deployment_team` | string[] | 是 | 部署团队 | ["工程师A", "工程师B"] |

### ClusterInfo 结构

```typescript
interface ClusterInfo {
  cluster_name: string;         // 集群名称
  namespace: string;           // 命名空间
  replicas: number;           // 副本数
  autoscaling: boolean;       // 是否启用自动扩缩容
}
```

## Chain of Thought

```
1. [THINK] 环境检查 → 目标环境是否就绪？
2. [THINK] 包验证 → 部署包是否完整有效？
3. [THINK] 策略选择 → 采用何种部署策略？
4. [THINK] 回滚准备 → 回滚方案是否可行？
5. [THINK] 分批规划 → 分批数量和间隔？
6. [EXECUTE] 执行部署 → 按计划执行
7. [VALIDATE] 验证确认 → 部署后验证
8. [MONITOR] 持续监控 → 确保稳定
```

## Error Handling

### 情况 1：部署包校验失败

```
IF 部署包 MD5 或签名校验失败
THEN
  1. 标记部署为失败
  2. 停止后续操作
  3. 建议重新构建或获取包
  4. 升级为 CRITICAL
END
```

### 情况 2：健康检查超时

```
IF 健康检查持续失败
THEN
  1. 检查服务日志
  2. 验证配置是否正确
  3. 检查资源是否充足
  4. 超过阈值时触发回滚
END
```

### 情况 3：部分批次失败

```
IF 中间批次部署失败
THEN
  1. 停止后续批次
  2. 评估已部署实例状态
  3. 决定是继续还是回滚
  4. 记录失败原因
END
```

### 情况 4：回滚失败

```
IF 回滚操作失败
THEN
  1. 立即升级为 CRITICAL
  2. 通知值班负责人
  3. 准备紧急响应
  4. 准备手动回滚方案
END
```

### 情况 5：资源不足

```
IF 部署时发现资源不足
THEN
  1. 评估可用资源
  2. 调整副本数或资源配置
  3. 重新尝试部署
  4. 记录资源配置变更
END
```

## Objective

规划并执行应用的部署发布，确保部署安全、可回滚，并完成验证。

## Context

你是一名 DevOps 工程师，正在负责应用的部署发布工作。你的目标是确保部署过程安全可靠，系统平稳上线。

## Input Format

```markdown
## Deployment Information

### 待发布内容
- 版本：v1.0.0
- 部署包：[包路径]
- 变更清单：[变更列表]

### 目标环境
- 环境：生产环境
- 集群：[集群信息]
- 配置：[配置信息]

### 测试通过信息
- 测试报告：[报告路径]
- 测试结论：通过
- 遗留问题：[问题列表]

### Rollback Plan
- 回滚版本：[版本]
- 回滚步骤：[步骤]
```

## Task Steps

### 步骤 1：部署规划

**任务**：
- 制定部署策略
- 确定部署时间
- 分配部署角色
- 准备回滚方案

**产出**：部署计划

### 步骤 2：环境准备

**任务**：
- 验证环境可用
- 准备环境配置
- 执行数据备份
- 验证备份成功

**产出**：就绪的部署环境

### 步骤 3：部署执行

**任务**：
- 执行部署前检查
- 按计划执行部署
- 记录部署过程
- 监控部署状态

**产出**：部署执行记录

### 步骤 4：验证检查

**任务**：
- 功能验证
- 健康检查
- 数据验证
- 性能检查

**产出**：验证报告

### 步骤 5：监控跟踪

**任务**：
- 持续监控状态
- 关注告警
- 定期报告状态
- 处理异常

**产出**：状态报告

### 步骤 6：文档归档

**任务**：
- 整理部署文档
- 归档部署记录
- 更新配置文档
- 总结经验教训

**产出**：归档文档

## Output Format

```markdown
# 部署报告

## 1. 部署信息

### 1.1 基本信息
| 项目 | 内容 |
|------|------|
| 项目名称 | - |
| 版本 | v1.0.0 |
| 部署时间 | 日期时间 |
| 部署环境 | 生产环境 |
| 部署方式 | 滚动更新 |
| 部署人员 | - |

### 1.2 部署内容
| 类型 | 名称 | 版本/变更 |
|------|------|-----------|
| 服务 | 服务A | v1.0.0 |
| 配置 | 配置A | 更新 |

## 2. Deployment Plan

### 2.1 部署策略
- 部署方式：滚动更新
- 批次：3 批次
- 每批间隔：10 分钟

### 2.2 部署步骤
| 步骤 | 操作 | 验证 | 负责人 |
|------|------|------|--------|
| 1 | 预检查 | 状态检查 | - |
| 2 | 执行部署 | 服务启动 | - |
| 3 | 健康检查 | 健康端点 | - |
| 4 | 功能验证 | 核心功能 | - |

### 2.3 回滚方案
- 回滚触发条件：
  - 健康检查失败
  - 核心功能异常
  - 错误率超过阈值
- 回滚步骤：
  1. 停止当前版本
  2. 启动上一版本
  3. 验证回滚成功
- 回滚预计时间：15 分钟

## 3. Deployment Execution

### 3.1 执行记录
| 时间 | 步骤 | 操作 | 结果 | 操作人 |
|------|------|------|------|--------|
| 10:00 | 1 | 预检查 | 通过 | - |
| 10:05 | 2 | 执行部署 | 成功 | - |
| 10:08 | 3 | 健康检查 | 通过 | - |
| 10:15 | 4 | 功能验证 | 通过 | - |

### 3.2 执行日志
```
[关键日志记录]
```

### 3.3 异常处理
| 时间 | 异常 | 处理 | 结果 |
|------|------|------|------|
| - | - | - | - |

## 4. Validation Results

### 4.1 部署后检查
| 检查项 | 检查方法 | 结果 | 说明 |
|--------|----------|------|------|
| 服务状态 | 健康检查 | 通过 | - |
| 核心功能 | 功能测试 | 通过 | - |
| 日志正常 | 日志检查 | 通过 | 无异常 |
| 监控正常 | 指标检查 | 通过 | - |

### 4.2 业务验证
| 业务 | 验证结果 | 说明 |
|------|----------|------|
| 业务A | 通过 | - |

## 5. Monitoring Status

### 5.1 关键指标
| 指标 | 值 | 状态 |
|------|------|------|
| CPU使用率 | XX% | 正常 |
| 内存使用率 | XX% | 正常 |
| 接口响应时间 | XXms | 正常 |
| 错误率 | X% | 正常 |

### 5.2 告警情况
- 告警数量：0
- 状态：正常

## 6. Conclusion

### 6.1 部署结论
**状态**：部署成功

### 6.2 遗留事项
| 事项 | 影响 | 负责人 | 完成时间 |
|------|------|--------|----------|
| - | - | - | - |

### 6.3 后续监控
- 监控时间：[持续时间]
- 关注重点：[重点]
- 负责人：[姓名]

## 7. Appendix

### 7.1 变更记录
| 变更类型 | 变更内容 | 影响 |
|----------|----------|------|
| 新增 | 功能A | - |

### 7.2 相关文档
- 部署计划：[链接]
- 测试报告：[链接]
- 回滚脚本：[链接]
```

## Output Validation

> **重要**: 在生成最终输出前，必须完成以下验证步骤

### 验证清单

```markdown
## Self-Validation Report

### V-001: 部署前检查
- [ ] 部署包校验通过
- [ ] 目标环境就绪
- [ ] 回滚方案可用
- [ ] 部署团队就位

### V-002: 部署过程检查
- [ ] 每批部署执行记录完整
- [ ] 健康检查全部通过
- [ ] 异常情况已记录
- [ ] 回滚触发条件正确

### V-003: 部署后检查
- [ ] 所有副本运行正常
- [ ] 健康检查 100% 通过
- [ ] 核心功能验证通过
- [ ] 监控指标正常

### V-004: 验证完成标准
- [ ] 服务状态: Healthy
- [ ] 错误率: < 0.1%
- [ ] 响应时间: < SLA
- [ ] 无新增告警

### 验证结果
- 验证通过: [是/否]
- 未通过的检查项: [列出]
```

### 验证失败时的处理

```
IF 验证未通过
THEN
  1. 识别未通过的验证项
  2. 评估是否可以自动恢复
  3. 超过阈值时执行回滚
  4. 记录失败原因和恢复过程
END
```

## Handover 准备

在完成验证后，生成以下交接信息：

```yaml
handoff_to_monitoring:
  deliverable: "部署报告"
  version: "1.0"
  status: "成功/失败/部分成功"

  summary:
    deployment_time: datetime      # 部署完成时间
    duration: minutes            # 总耗时
    batches: N                    # 批次数
    instances_total: N           # 总实例数

  health_status:
    checks_passed: boolean
    error_rate: percentage
    avg_response_time: ms

  monitoring:
    watch_duration: hours        # 监控观察时长
    alert_threshold: string       # 告警阈值
    contact: string              # 联系人

  rollback_available: boolean
  rollback_version: string

  recommendations:
    - "建议"
```

## Constraints

1. **语言**：输出使用中文
2. **安全**：必须可回滚
3. **验证**：必须完整验证
4. **记录**：必须记录完整
5. **通知**：必须通知相关方

## Quality Requirements

| 要求 | 说明 |
|------|------|
| 可回滚 | 有完整的回滚方案 |
| 验证完整 | 核心功能都有验证 |
| 记录完整 | 部署过程有记录 |
| 监控就绪 | 监控系统已配置 |

## Task Description

> Describe the specific task for the deploy-release scenario execution.
> AI must understand the context, objectives, and success criteria before proceeding.

## Execution Flow

> Step-by-step execution sequence for deploy-release

### Phase 1: Analysis
- Understand requirements and context
- Identify constraints and dependencies

### Phase 2: Execution
- Perform core deploy-release activities
- Apply best practices and standards

### Phase 3: Validation
- Verify outputs against acceptance criteria
- Ensure completeness and quality
