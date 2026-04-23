# Deployment Scenario

## Purpose

规划并执行应用的部署发布，确保部署安全、可回滚，并完成验证。

## Chain of Thought (思维链)

> AI 执行时的思维引导，帮助逐步完成部署发布工作

### Think-Aloud Protocol

```
THINK: 确认部署准备就绪
   ↓
THINK: 制定部署计划
   ↓
THINK: 执行部署步骤
   ↓
THINK: 验证部署结果
   ↓
THINK: 监控系统状态
   ↓
THINK: 归档部署记录
```

### Step-by-Step Reasoning

**Step 1: 部署就绪检查**
- 问：所有准备工作都完成了吗？
- 验证：测试通过、环境就绪、回滚方案
- 检查：部署窗口是否合适

**Step 2: 计划制定**
- 问：部署步骤是否清晰？
- 验证：每个步骤的前置条件和验证点
- 检查：回滚触发条件是否明确

**Step 3: 部署执行**
- 问：部署过程是否按计划执行？
- 验证：每个步骤的结果
- 检查：是否有异常需要处理

**Step 4: 验证检查**
- 问：部署后的验证都通过了吗？
- 验证：功能验证、性能验证
- 检查：监控系统是否正常

**Step 5: 记录归档**
- 问：部署记录是否完整？
- 验证：配置变更、性能数据
- 检查：是否更新了运维文档

## Primary Assets

### Agent

- **Agent**: [../../agents/devops-engineer.agent.md](../../agents/devops-engineer.agent.md)

### Instruction

- **Instruction**: [../../instructions/deployment-release.instructions.md](../../instructions/deployment-release.instructions.md)

### Prompt

- **Prompt**: [../../prompts/deploy-release.prompt.md](../../prompts/deploy-release.prompt.md)

### Skills

- **Skill**: [../../skills/deployment/SKILL.md](../../skills/deployment/SKILL.md)

## Error Handling (错误处理)

### EH-1: 部署验证失败

- **识别信号**：部署后验证检查不通过
- **处理方式**：
  1. 检查部署日志
  2. 回滚到上一版本
  3. 分析失败原因
  4. 修复后重新部署
- **升级条件**：无法快速恢复

### EH-2: 配置问题

- **识别信号**：配置错误导致功能异常
- **处理方式**：
  1. 检查配置文件
  2. 验证配置值
  3. 更新配置
  4. 重新验证
- **升级条件**：影响核心功能

### EH-3: 回滚触发

- **识别信号**：满足回滚条件
- **处理方式**：
  1. 执行回滚操作
  2. 验证回滚成功
  3. 通知相关方
  4. 记录回滚原因
- **升级条件**：发布延迟

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
