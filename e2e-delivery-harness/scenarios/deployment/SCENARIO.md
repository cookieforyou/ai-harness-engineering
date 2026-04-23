# Deployment Scenario

## Purpose

规划并执行应用的部署发布，确保部署安全、可回滚，并完成验证。

## Primary Assets

### Agent

- **Agent**: [../../agents/devops-engineer.agent.md](../../agents/devops-engineer.agent.md)

### Instruction

- **Instruction**: [../../instructions/deployment-release.instructions.md](../../instructions/deployment-release.instructions.md)

### Prompt

- **Prompt**: [../../prompts/deploy-release.prompt.md](../../prompts/deploy-release.prompt.md)

### Skills

- **Skill**: [../../skills/deployment/SKILL.md](../../skills/deployment/SKILL.md)

## Expected Output

### 产出清单

1. **部署计划**：详细的部署步骤和时间表
2. **回滚方案**：回滚操作步骤和条件
3. **部署检查清单**：部署后的验证检查项
4. **部署报告**：部署执行记录和结果

### 输出格式

```markdown
## 部署报告

### 1. 部署信息
...

### 2. 部署计划
...

### 3. 回滚方案
...

### 4. 部署执行
...

### 5. 验证结果
...

### 6. 监控状态
...

### 7. 结论
...
```

## Prerequisites

### 必需前置条件

1. 测试已通过
2. 部署包已准备
3. 目标环境已就绪

### 可选前置条件

1. 回滚脚本已准备
2. 配置变更清单
3. 监控告警已配置

## Quality Gates

### 阶段准入

- [ ] 测试通过报告已签发
- [ ] 部署包已验证
- [ ] 目标环境已就绪

### 阶段准出

- [ ] 部署执行成功
- [ ] 验证检查通过
- [ ] 监控系统正常
- [ ] 部署报告已归档

## Workflow

```
1. 启动 → 准备部署
2. 规划 → 制定部署计划
3. 环境准备 → 准备目标环境
4. 部署执行 → 按计划部署
5. 验证检查 → 验证部署结果
6. 监控跟踪 → 监控运行状态
7. 文档归档 → 归档部署记录
8. 完成 → 输出部署报告
```

## Related Scenarios

- **Next**: [../monitoring/SCENARIO.md](../monitoring/SCENARIO.md) - 监控运维
- **Previous**: [../testing/SCENARIO.md](../testing/SCENARIO.md) - 测试验证

## Metrics

| 指标 | 目标 | 测量方法 |
|------|------|----------|
| 部署成功率 | 100% | 部署记录 |
| 回滚准备率 | 100% | 回滚方案 |
| 验证通过率 | 100% | 验证清单 |
| 部署时间 | 按计划 | 时间统计 |
