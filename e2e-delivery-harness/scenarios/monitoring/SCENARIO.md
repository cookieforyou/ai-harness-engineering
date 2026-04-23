# Monitoring Scenario

## Purpose

配置监控系统，执行日常巡检，处理告警和故障，保障系统稳定运行。

## Primary Assets

### Agent

- **Agent**: [../../agents/sre-monitor.agent.md](../../agents/sre-monitor.agent.md)

### Instruction

- **Instruction**: [../../instructions/monitoring-operations.instructions.md](../../instructions/monitoring-operations.instructions.md)

### Prompt

- **Prompt**: [../../prompts/monitor-operate.prompt.md](../../prompts/monitor-operate.prompt.md)

### Skills

- **Skill**: [../../skills/monitoring/SKILL.md](../../skills/monitoring/SKILL.md)

## Expected Output

### 产出清单

1. **监控方案**：监控指标和告警规则
2. **运维手册**：日常运维操作指南
3. **应急预案**：故障处理流程和预案
4. **巡检报告**：周期巡检结果

### 输出格式

```markdown
## 运维报告

### 1. 监控概览
...

### 2. 监控配置
...

### 3. 巡检记录
...

### 4. 告警记录
...

### 5. 故障记录
...

### 6. 容量评估
...

### 7. 优化建议
...
```

## Prerequisites

### 必需前置条件

1. 应用已部署上线
2. 系统架构已确认
3. 监控系统可用

### 可选前置条件

1. 历史监控数据
2. 历史故障记录
3. 业务监控需求

## Quality Gates

### 阶段准入

- [ ] 部署已完成
- [ ] 监控系统已部署
- [ ] 告警渠道已配置

### 阶段准出

- [ ] 监控配置完成
- [ ] 运维手册完成
- [ ] 应急预案完成
- [ ] 巡检报告已输出

## Workflow

```
1. 启动 → 了解系统情况
2. 监控设计 → 设计监控方案
3. 配置实施 → 配置监控系统
4. 日常巡检 → 执行巡检
5. 告警处理 → 处理告警
6. 故障处理 → 排查故障
7. 容量管理 → 评估容量
8. 运维优化 → 持续改进
9. 完成 → 输出运维报告
```

## Related Scenarios

- **Next**: - (持续运维)
- **Previous**: [../deployment/SCENARIO.md](../deployment/SCENARIO.md) - 部署发布

## Metrics

| 指标 | 目标 | 测量方法 |
|------|------|----------|
| 系统可用率 | > 99.9% | 可用率统计 |
| 告警响应时间 | < 5 分钟 | 响应记录 |
| 故障恢复时间 | < 30 分钟 | 恢复记录 |
| 巡检完成率 | 100% | 巡检记录 |
