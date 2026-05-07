---
name: integrate-monitor
version: 1.1.0
stage: integrate-monitor
description: Integrate Monitor scenario for the E2E delivery lifecycle
author: AI Harness Engineering Team
type: scenario
---

# Scenario: 监控集成 (Integrate Monitor)

## Overview

监控集成是系统可观测性的核心，负责指标采集、日志收集、链路追踪的统一集成。

## Core Decision Points

| 阶段 | 决策点 | 输出 |
|------|--------|------|
| 监控规划 | Metric Selection | 监控指标 |
| 埋点实施 | Instrumentation | 埋点代码 |
| 告警配置 | Alert Configuration | 告警规则 |
| 可视化 | Dashboard Design | 监控面板 |

## Execution Flow

```python
class MonitoringIntegration:
    """监控集成流程"""

    def execute(self, system_context, monitoring_requirements):
        """
        1. 监控规划 (30分钟)
        2. 指标埋点 (60分钟)
        3. 告警配置 (30分钟)
        4. 面板搭建 (30分钟)
        """
        # Step 1: 监控规划
        monitoring_plan = self.plan_monitoring(
            system_context, monitoring_requirements
        )

        # Step 2: 指标埋点
        instrumented_code = self.instrument_code(monitoring_plan)

        # Step 3: 告警配置
        alert_rules = self.configure_alerts(monitoring_plan)

        # Step 4: 面板搭建
        dashboards = self.build_dashboards(monitoring_plan)

        return MonitoringPackage(
            monitoring_plan, instrumented_code, alert_rules, dashboards
        )

    def plan_monitoring(self, context, requirements):
        """监控规划"""
        # 1. 识别关键指标 (RED/USE 方法)
        # 2. 定义指标层次
        # 3. 规划采集频率
        pass

    def instrument_code(self, plan):
        """指标埋点"""
        # 1. 集成 SDK
        # 2. 添加埋点
        # 3. 配置导出
        pass
```

## Decision Checkpoints

- [ ] **指标完整性**: 核心指标是否覆盖？
- [ ] **采集开销**: 监控采集对性能的影响是否可接受？
- [ ] **告警有效性**: 告警规则是否能及时发现问题？
- [ ] **可视化可用性**: 面板是否便于日常巡检和故障排查？

## Error Handling

| 场景 | 处理方式 |
|------|----------|
| 指标丢失 | 启用本地缓冲，降级重试 |
| 告警风暴 | 启用告警聚合和静默规则 |
| 数据延迟 | 配置数据刷新频率 |

## Handover Standards

### 监控集成完成标准

```
✅ 核心指标已埋点并可采集
✅ 告警规则已配置并测试
✅ 监控面板已搭建
✅ 文档已更新
```

### 交付物

1. **监控架构**: 监控组件和拓扑图
2. **埋点代码**: 指标采集代码
3. **告警规则**: 告警配置
4. **监控面板**: Dashboard 配置

## Associated Assets

| 类型 | 路径 |
|------|------|
| SCENARIO | `scenarios/integrate-monitor/SCENARIO.md` |
| PROMPT | `prompts/integrate-monitor.prompt.md` |
| INSTRUCTIONS | `instructions/integrate-monitor.instructions.md` |
| AGENT | `agents/integrate-monitor.agent.md` |
| SKILL | `skills/integrate-monitor/SKILL.md` |


## Purpose

> Define the objectives and scope of the integrate-monitor scenario.
>
> This scenario ensures systematic execution of integrate-monitor activities with clear decision checkpoints and handover criteria.


## Prerequisites

- [ ] Prerequisite 1: Monitoring tool stack is selected and provisioned
- [ ] Prerequisite 2: Application instrumentation points are identified
- [ ] Prerequisite 3: Notification channels are configured and tested


## Primary Assets

| Asset Type | Path | Description |
|------------|------|-------------|
| Scenario | `scenarios/integrate-monitor/SCENARIO.md` | This scenario definition |
| Prompt | `prompts/integrate-monitor.prompt.md` | Execution prompt |
| Instructions | `instructions/integrate-monitor.instructions.md` | Technical instructions |
| Agent | `agents/integrate-monitor.agent.md` | Responsible agent |
| Skill | `skills/integrate-monitor/SKILL.md` | Domain skill |


## Chain of Thought

1. Understand the context and requirements for integrate-monitor
2. Analyze dependencies and constraints
3. Execute core activities systematically
4. Validate outputs against acceptance criteria
5. Document decisions and handover state


## Decision Checkpoints

| Checkpoint | Question | Decision Options |
|------------|----------|-----------------|

## Quality Metrics

> Quality metrics for measuring scenario execution success.

| KPI | Target | Description |
|-----|--------|-------------|
| `METRIC-COVERAGE` | ≥90% | 指标覆盖率：关键组件有监控指标 |
| `INSTRUMENT-OVERHEAD` | ≤5% | 埋点开销：性能影响≤5% |
| `DASHBOARD-UTIL` | ≥70% | 面板利用率：面板被查看频率 |

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识

## Handover Criteria

- [ ] Criterion 1: All critical components have active monitoring
- [ ] Criterion 2: Alerting rules are validated with test scenarios
- [ ] Criterion 3: Dashboards are deployed and accessible to stakeholders
