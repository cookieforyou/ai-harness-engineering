---
name: monitor-operate
description: 监控运维提示词，用于配置监控和执行日常运维工作
type: operations
version: "1.1.0"
stage: monitoring
---

# Monitor and Operate

> **版本**: 1.1.0 | **适用阶段**: 监控运维 | **预计工时**: 持续

## Input Variables

> AI 在执行前必须确认以下变量已填充

| 变量名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|------|
| `project_name` | string | 是 | 项目名称 | "电商订单系统" |
| `architecture` | string | 是 | 系统架构描述 | "微服务架构" |
| `components` | string[] | 是 | 关键组件列表 | ["API", "DB", "Cache"] |
| `deployment_version` | string | 是 | 当前部署版本 | "v1.0.0" |
| `slo_targets` | object | 是 | SLO 目标 | 见 SLO Targets 结构 |
| `alert_channels` | string[] | 是 | 告警渠道 | ["钉钉", "邮件"] |
| `runbook_links` | string[] | 否 | 运维手册链接 | ["runbook.md"] |
| `oncall_schedule` | object | 否 | 值班安排 | 见 OnCall 结构 |

### SLO Targets 结构

```typescript
interface SLOTargets {
  availability: number;          // 可用性目标 (如 99.9%)
  latency_p50: number;           // 延迟 P50 目标 (ms)
  latency_p99: number;           // 延迟 P99 目标 (ms)
  error_rate: number;           // 错误率目标 (%)
  recovery_time: number;        // 恢复时间目标 (分钟)
}
```

### OnCall 结构

```typescript
interface OnCall {
  primary: string;               // 主值班
  secondary: string;            // 备值班
  rotation: string;             // 轮换规则
  escalation_policy: string[];  // 升级策略
}
```

## Chain of Thought

```
1. [THINK] 理解架构 → 关键组件和依赖是否清晰？
2. [THINK] 设计指标 → 黄金指标是否覆盖？
3. [THINK] 配置告警 → 阈值和渠道是否合理？
4. [THINK] 准备 Runbook → 常见问题是否覆盖？
5. [EXECUTE] 配置监控 → 按计划配置
6. [VALIDATE] 验证生效 → 监控数据是否正常
7. [OUTPUT] 生成报告 → 监控配置报告
```

## Error Handling

### 情况 1：监控数据缺失

```
IF 关键指标无数据
THEN
  1. 检查采集 Agent 状态
  2. 检查网络连通性
  3. 验证指标定义
  4. 标记为 [数据缺失] 并通知
END
```

### 情况 2：告警风暴

```
IF 告警数量异常激增
THEN
  1. 识别触发告警
  2. 评估是否为级联效应
  3. 暂时抑制非关键告警
  4. 优先处理根因
END
```

### 情况 3：SLO 即将违反

```
IF SLO 趋势显示即将违反目标
THEN
  1. 立即升级告警
  2. 启动应急响应流程
  3. 通知相关团队
  4. 准备事后复盘
END
```

### 情况 4：组件告警无法定位

```
IF 告警无法定位到具体问题
THEN
  1. 扩大排查范围
  2. 检查依赖组件
  3. 逐层排查
  4. 标记为 [调查中]
END
```

## Objective

配置监控系统，执行日常运维，发现并处理问题，持续优化运维效率。

## Context

你是一名 SRE 工程师，正在负责系统的监控运维工作。你的目标是保障系统稳定运行，及时发现和处理问题。

## Input Format

```markdown
## System Information

### 系统概况
- 系统名称：[名称]
- 架构：[架构描述]
- 部署环境：[环境]
- 关键组件：[组件列表]

### Deployment Information
- 部署版本：v1.0.0
- 部署时间：[时间]
- 配置变更：[变更列表]

### 历史问题
- 问题1：[描述]
- 问题2：[描述]

### 监控需求
- 监控级别：[基础/标准/高级]
- 告警渠道：[渠道]
```

## Task Steps

### 步骤 1：监控配置

**任务**：
- 设计监控指标体系
- 配置基础监控
- 配置应用监控
- 配置业务监控
- 设置告警规则

**产出**：监控配置文档

### 步骤 2：日常巡检

**任务**：
- 检查系统健康状态
- 检查资源使用情况
- 检查业务指标
- 检查告警情况
- 记录巡检结果

**产出**：巡检报告

### 步骤 3：告警处理

**任务**：
- 响应告警通知
- 评估告警级别
- 执行处理措施
- 验证处理效果
- 更新告警记录

**产出**：告警处理记录

### 步骤 4：故障排查

**任务**：
- 确认故障现象
- 收集故障信息
- 分析故障原因
- 执行修复措施
- 验证修复效果
- 编写故障报告

**产出**：故障报告

### 步骤 5：容量管理

**任务**：
- 分析容量使用
- 评估容量趋势
- 制定扩容计划
- 执行优化措施

**产出**：容量报告

### 步骤 6：运维优化

**任务**：
- 分析运维数据
- 识别优化机会
- 实施优化措施
- 更新运维文档

**产出**：优化建议

## Output Format

```markdown
## Monitoring & Operations Deliverables

### Summary
- Status: [completed | partial | blocked]
- Completion: [percentage]

### Key Outputs
1. **Monitoring Configuration**: Collection and alerting rule configs
2. **Dashboard Definitions**: Pre-built dashboard JSON/markdown
3. **Runbook Library**: Operational procedures for common scenarios
4. **SLO Dashboard**: Service level objective tracking and reporting
5. **Alert Routing**: Escalation path and notification channel setup

### Validation Checklist
- [ ] MTTD is 5 minutes or less
- [ ] Alert noise rate is 20% or lower
- [ ] SLO compliance is 99.5% or higher
- [ ] Runbooks cover 90% of alert types

### Next Steps
- [ ] Train operations team on new monitoring
- [ ] Schedule monthly SLO review
```


## 1. 报告概要

### 1.1 监控概览
| 项目 | 状态 |
|------|------|
| 系统状态 | 正常 |
| 监控指标 | 正常 |
| 告警情况 | 无 |
| 故障情况 | 无 |

### 1.2 运维统计
| 类型 | 数量 | 处理时效 |
|------|------|----------|
| 巡检 | 1次 | - |
| 告警 | 0个 | - |
| 故障 | 0个 | - |

## 2. 监控配置

### 2.1 监控指标体系

#### 基础监控
| 指标 | 采集方式 | 阈值 | 告警级别 |
|------|----------|------|----------|
| CPU使用率 | Agent | >80% | 警告 |
| 内存使用率 | Agent | >85% | 警告 |
| 磁盘使用率 | Agent | >90% | 警告 |

#### 应用监控
| 指标 | 采集方式 | 阈值 | 告警级别 |
|------|----------|------|----------|
| 接口响应时间 | APM | >500ms | 警告 |
| 接口错误率 | APM | >1% | 警告 |

#### 业务监控
| 指标 | 采集方式 | 阈值 | 告警级别 |
|------|----------|------|----------|
| 订单量 | 日志 | 偏离>20% | 警告 |
| 转化率 | 日志 | 偏离>15% | 警告 |

### 2.2 告警规则
| 告警名称 | 条件 | 级别 | 通知方式 |
|----------|------|------|----------|
| 服务不可用 | 可用率<99% | P0 | 电话+短信 |
| 响应超时 | 响应时间>1s | P1 | 短信 |
| 错误率升高 | 错误率>5% | P1 | 短信 |

### 2.3 监控视图
| 视图名称 | 内容 | 刷新频率 |
|----------|------|----------|
| 系统总览 | 整体状态 | 30秒 |
| 服务详情 | 各服务状态 | 30秒 |
| 业务指标 | 业务数据 | 1分钟 |

## 3. 巡检报告

### 3.1 巡检记录
| 巡检时间 | 巡检人 | 巡检结果 |
|----------|--------|----------|
| 日期 | - | 正常 |

### 3.2 系统状态
| 组件 | 状态 | CPU | 内存 | 磁盘 |
|------|------|-----|------|------|
| 服务A | 正常 | 60% | 70% | 50% |
| 服务B | 正常 | 55% | 65% | 45% |

### 3.3 业务状态
| 指标 | 当前值 | 正常范围 | 状态 |
|------|--------|----------|------|
| 日活用户 | 10000 | 8000-15000 | 正常 |
| 接口QPS | 500 | 300-800 | 正常 |

## 4. 告警记录

### 4.1 告警汇总
| 告警时间 | 告警内容 | 级别 | 处理时间 | 状态 |
|----------|----------|------|-----------|------|
| - | - | - | - | - |

### 4.2 告警详情（最近告警）
| 字段 | 内容 |
|------|------|
| 告警ID | - |
| 告警时间 | - |
| 告警内容 | - |
| 告警级别 | - |
| 处理措施 | - |
| 处理结果 | - |

## 5. 故障记录

### 5.1 故障汇总
| 故障时间 | 故障描述 | 级别 | 持续时间 | 状态 |
|----------|----------|------|----------|------|
| - | - | - | - | - |

### 5.2 故障详情（最近故障）
| 字段 | 内容 |
|------|------|
| 故障ID | - |
| 故障时间 | - |
| 故障描述 | - |
| 故障级别 | - |
| 影响范围 | - |
| 故障原因 | - |
| 处理过程 | - |
| 改进措施 | - |

## 6. 容量评估

### 6.1 当前容量
| 资源 | 使用率 | 容量 | 说明 |
|------|--------|------|------|
| CPU | 60% | 80% | 有扩容空间 |
| 内存 | 70% | 85% | 有扩容空间 |
| 存储 | 50% | 90% | 有扩容空间 |

### 6.2 容量趋势
[容量趋势分析]

### 6.3 扩容建议
| 建议 | 理由 | 优先级 |
|------|------|--------|
| - | - | - |

## 7. 运维优化

### 7.1 优化建议
| 建议 | 预期收益 | 实施难度 | 优先级 |
|------|----------|----------|--------|
| - | - | - | - |

### 7.2 实施计划
[已实施的优化措施]

## 8. 联系方式

| 角色 | 姓名 | 电话 | 邮箱 |
|------|------|------|------|
| 运维负责人 | - | - | - |
| 开发负责人 | - | - | - |

## 9. Appendix

### 9.1 运维手册
- 日常操作：[链接]
- 故障处理：[链接]
- 变更流程：[链接]

### 9.2 应急预案
- P0故障：[链接]
- P1故障：[链接]
- P2故障：[链接]
```

## Output Validation

> **重要**: 在生成最终输出前，必须完成以下验证步骤

### 验证清单

```markdown
## Self-Validation Report

### V-001: 监控覆盖检查
- [ ] 黄金指标全部覆盖 (Latency, Traffic, Errors, Saturation)
- [ ] 基础设施监控完整
- [ ] 应用层监控完整
- [ ] 业务指标监控完整

### V-002: 告警配置检查
- [ ] 告警阈值合理
- [ ] 告警级别设置正确
- [ ] 告警渠道畅通
- [ ] 升级机制有效

### V-003: 巡检记录检查
- [ ] 巡检周期符合要求
- [ ] 巡检项目完整
- [ ] 异常记录详细
- [ ] 处理记录完整

### V-004: SLO 合规检查
- [ ] SLO 目标可达
- [ ] 当前 Error Budget 充足
- [ ] 趋势分析准确

### 验证结果
- 验证通过: [是/否]
- 未通过的检查项: [列出]
```

### 验证失败时的处理

```
IF 验证未通过
THEN
  1. 识别未通过的验证项
  2. 补充缺失的监控配置
  3. 修正告警配置
  4. 重新执行验证
END
```

## Handover 准备

在完成验证后，生成以下交接信息：

```yaml
handoff_to_next_shift:
  deliverable: "运维报告"
  period: "YYYY-MM-DD HH:MM - YYYY-MM-DD HH:MM"
  status: "正常/关注/告警"

  summary:
    incidents_count: N              # 故障数
    alerts_count: N                # 告警数
    slo_status: "MET/BREACHED"     # SLO 状态
    error_budget_remaining: %       # 剩余 Error Budget

  critical_items:
    - item: "需要关注的事项"
      action: "建议行动"
      owner: "负责人"

  oncall_info:
    current_shift: string
    next_shift: string
    escalation_contact: string

  recommendations:
    - "优化建议"
```

## Constraints

1. **语言**：输出使用中文
2. **及时性**：告警需及时响应
3. **完整性**：监控需覆盖核心指标
4. **可追溯**：所有操作需有记录
5. **持续改进**：需持续优化运维效率

## Quality Requirements

| 要求 | 说明 |
|------|------|
| 监控完善 | 核心指标都有监控 |
| 告警有效 | 告警阈值合理有效 |
| 响应及时 | 告警及时响应处理 |
| 文档完善 | 运维文档完整更新 |

## Task Description

> Describe the specific task for the monitor-operate scenario execution.
> AI must understand the context, objectives, and success criteria before proceeding.

## Execution Flow

> Step-by-step execution sequence for monitor-operate

### Phase 1: Analysis
- Understand requirements and context
- Identify constraints and dependencies

### Phase 2: Execution
- Perform core monitor-operate activities
- Apply best practices and standards

### Phase 3: Validation
- Verify outputs against acceptance criteria
- Ensure completeness and quality
