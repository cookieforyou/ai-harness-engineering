# Pipeline: 故障响应流程 (Incident Response Pipeline)

## 概述

本文档定义了从故障检测到恢复完成的全流程规范，用于指导 AI Agent 执行标准化故障响应。

## 流程阶段

```
┌─────────────────────────────────────────────────────────────────┐
│  Phase 1: 检测与分级                                             │
│  Detection & Triage                                             │
│  ├── 1.1 告警接收                                                │
│  ├── 1.2 初步评估                                                │
│  ├── 1.3 严重等级判定                                            │
│  └── 1.4 故障通告                                                │
└────────────────────────────┬────────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────────┐
│  Phase 2: 响应与缓解                                             │
│  Response & Mitigation                                          │
│  ├── 2.1 问题定位                                                │
│  ├── 2.2 应急响应                                                │
│  ├── 2.3 缓解措施                                                │
│  └── 2.4 效果验证                                                │
└────────────────────────────┬────────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────────┐
│  Phase 3: 恢复与闭环                                             │
│  Recovery & Resolution                                          │
│  ├── 3.1 完全恢复                                                │
│  ├── 3.2 服务验证                                                │
│  ├── 3.3 用户通知                                                │
│  └── 3.4 故障关闭                                                │
└────────────────────────────┬────────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────────┐
│  Phase 4: 复盘与改进                                             │
│  Post-mortem & Improvement                                      │
│  ├── 4.1 数据收集                                                │
│  ├── 4.2 根因分析                                                │
│  ├── 4.3 复盘会议                                                │
│  └── 4.4 改进跟踪                                                │
└─────────────────────────────────────────────────────────────────┘
```

## 阶段详细定义

### Phase 1: 检测与分级

#### 1.1 告警接收

**输入**
- 监控告警 / 用户报告 / 第三方通知

**执行步骤**
1. 接收告警信息
2. 记录告警时间
3. 提取告警内容
4. 初步判断告警类型

**输出**
```yaml
alert_info:
  alert_id: string
  alert_time: datetime
  alert_source: "monitor" | "user" | "third_party"
  alert_content: string
  alert_type: string
```

#### 1.2 初步评估

**执行步骤**
1. 确认告警是否真实
2. 检查相关监控数据
3. 评估影响范围
4. 判断是否需要升级

**决策树**
```
告警是否为真?
├── 是 → 影响范围?
│        ├── 核心服务 → SEV1
│        ├── 非核心服务 → 评估持续时间
│        └── 单用户 → SEV4
└── 否 → 误报/噪音处理
```

#### 1.3 严重等级判定

| 等级 | 定义 | 影响 | 响应时间 |
|------|------|------|----------|
| SEV1 | 核心服务不可用 | 大规模用户受影响 | 5 分钟 |
| SEV2 | 非核心服务不可用 | 部分功能受损 | 15 分钟 |
| SEV3 | 服务降级 | 用户体验受影响 | 30 分钟 |
| SEV4 | 轻微异常 | 极少数用户 | 2 小时 |

#### 1.4 故障通告

**通告对象**
```yaml
notification_matrix:
  SEV1:
    - 技术 VP
    - 运维负责人
    - 服务负责人
    - 客服负责人
  SEV2:
    - 运维负责人
    - 服务负责人
  SEV3:
    - 服务负责人
  SEV4:
    - 值班工程师
```

---

### Phase 2: 响应与缓解

#### 2.1 问题定位

**执行步骤**
1. 收集相关信息
   - 最近变更记录
   - 监控指标趋势
   - 日志分析
   - 告警历史

2. 缩小排查范围
   - 网络层
   - 应用层
   - 数据层
   - 第三方依赖

3. 定位问题根因
   - 使用诊断命令
   - 分析调用链路
   - 检查资源状态

**常用诊断命令**
```bash
# 查看服务状态
kubectl get pods -n production
kubectl describe pod <pod-name> -n production

# 查看日志
kubectl logs <pod-name> -n production --tail=100
kubectl logs <pod-name> -n production --since=10m

# 查看资源
kubectl top pods -n production
kubectl top nodes

# 查看网络
kubectl exec -it <pod-name> -n production -- curl {{health_check_endpoint}}
netstat -an | grep LISTEN

# 查看数据库
psql -h <host> -U <user> -c "SELECT * FROM pg_stat_activity;"
mysql -h <host> -u <user> -p -e "SHOW PROCESSLIST;"
```

#### 2.2 应急响应

**通用应急响应矩阵**

| 问题类型 | 第一响应 | 备用方案 |
|----------|----------|----------|
| 服务 OOM | 重启 Pod | 增加资源限制 |
| 数据库连接耗尽 | 清理连接 | 增加连接池 |
| 流量激增 | 限流降级 | 扩容 |
| 依赖超时 | 超时配置调优 | 熔断降级 |
| 配置错误 | 回滚配置 | 使用备份配置 |

#### 2.3 缓解措施

**执行约束**
- 优先保证核心功能
- 最小化对用户的影响
- 确保有回滚方案
- 记录所有操作

**记录模板**
```yaml
mitigation_action:
  timestamp: datetime
  action: string
  executed_by: string
  expected_result: string
  actual_result: string
  success: boolean
```

#### 2.4 效果验证

**验证检查项**
- [ ] 服务健康检查通过
- [ ] 核心功能可用
- [ ] 监控指标恢复正常
- [ ] 无新增告警
- [ ] 用户反馈正常

---

### Phase 3: 恢复与闭环

#### 3.1 完全恢复

**执行步骤**
1. 确认服务完全恢复
2. 验证数据完整性
3. 检查备份状态
4. 更新服务状态

#### 3.2 服务验证

**验证清单**
- [ ] 健康检查 100% 通过
- [ ] 响应时间在 SLA 内
- [ ] 错误率 < 0.1%
- [ ] 资源使用正常
- [ ] 上下游依赖正常

#### 3.3 用户通知

**通知模板**
```markdown
## 服务状态更新

尊敬的用户：

[服务名称] 已于 [恢复时间] 恢复正常服务。

故障持续时间：[时长]
影响范围：[影响描述]

我们对此次故障给您带来的不便深表歉意。如有疑问，请联系我们的客服团队。

感谢您的理解与支持。
```

#### 3.4 故障关闭

**关闭条件**
- 服务完全恢复
- 影响用户已通知
- 复盘会议已安排
- 改进措施已记录

---

### Phase 4: 复盘与改进

#### 4.1 数据收集

**收集清单**
- 监控截图
- 日志文件
- 告警记录
- 操作记录
- 用户反馈
- 时间线文档

#### 4.2 根因分析

**分析方法**
- 5 Whys
- Fishbone 图
- Fault Tree Analysis
- Event Sequence Diagram

#### 4.3 复盘会议

**参与人员**
- 故障响应团队
- 相关开发团队
- SRE/运维团队
- 产品经理
- 技术负责人

**议程**
1. 故障概述 (5 min)
2. 时间线回顾 (10 min)
3. 根因分析 (15 min)
4. 影响评估 (5 min)
5. 改进讨论 (20 min)
6. 行动项确认 (5 min)

#### 4.4 改进跟踪

**改进措施模板**
```yaml
action_item:
  id: string
  description: string
  type: "PREVENTIVE" | "DETECTIVE" | "CORRECTIVE"
  priority: "P0" | "P1" | "P2"
  owner: string
  due_date: datetime
  status: "OPEN" | "IN_PROGRESS" | "COMPLETED"
  verification_method: string
```

---

## 数据传递规范

### 阶段间数据

| 传递方向 | 传递数据 |
|----------|----------|
| Phase 1 → Phase 2 | 故障 ID、严重等级、初步影响评估 |
| Phase 2 → Phase 3 | 根因、已执行的缓解措施、恢复状态 |
| Phase 3 → Phase 4 | 完整时间线、统计数据、用户反馈 |
| Phase 4 → (循环) | 改进措施、更新到知识库 |

### 上下文模板

```markdown
## 故障上下文

### 基础信息
- 故障ID: {incident_id}
- 严重等级: {severity}
- 开始时间: {start_time}
- 恢复时间: {end_time}
- 持续时长: {duration}

### 影响范围
- 受影响服务: {affected_services}
- 受影响用户: {user_count}
- 业务损失: {business_loss}

### 根因
- 直接原因: {direct_cause}
- 根本原因: {root_cause}

### 改进措施
- 待执行: {pending_actions}
- 执行中: {in_progress_actions}
- 已完成: {completed_actions}
```

---

## Associated Assets

| 资产类型 | 文件路径 |
|----------|----------|
| Scenario | `scenarios/review-incident/SCENARIO.md` |
| Prompt | `prompts/review-incident.prompt.md` |
| Instruction | `instructions/review-incident.instructions.md` |
| Agent | `agents/review-incident.agent.md` |
| Skill | `skills/review-incident/SKILL.md` |

---

## Appendix

### 常用工具/命令参考

**监控查询**
```bash
# Prometheus 查询
promql: http_requests_total{service="xxx", status=~"5.."}

# 日志查询
kubectl logs -n production -l app=xxx --since=30m | grep ERROR

# 指标查询
kubectl top pods -n production
```

**故障诊断检查清单**
- [ ] 网络连通性
- [ ] DNS 解析
- [ ] 磁盘空间
- [ ] 内存使用
- [ ] CPU 使用
- [ ] 进程状态
- [ ] 端口监听
- [ ] 防火墙规则
- [ ] 证书有效期
- [ ] 连接池状态
