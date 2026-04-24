# {scenario-name} Scenario

## Purpose

{场景目标描述}

## Chain of Thought (思维链)

> AI 执行时的思维引导，帮助逐步完成 {场景名称} 工作

### Think-Aloud Protocol

```
THINK: 步骤1
   ↓
THINK: 步骤2
   ↓
THINK: 步骤3
   ↓
THINK: 步骤4
   ↓
THINK: 验证和输出
```

### Step-by-Step Reasoning

**Step 1: {子步骤1}**
- 问：{自问1}？
- 验证：{验证方式}
- 检查：{检查点}

**Step 2: {子步骤2}**
- 问：{自问1}？
- 验证：{验证方式}
- 检查：{检查点}

**Step 3: {子步骤3}**
- 问：{自问1}？
- 验证：{验证方式}
- 检查：{检查点}

## Primary Assets

### Agent
- **Agent**: [../../agents/{agent-file}.agent.md](../../agents/{agent-file}.agent.md)

### Instruction
- **Instruction**: [../../instructions/{instruction-file}.instructions.md](../../instructions/{instruction-file}.instructions.md)

### Prompt
- **Prompt**: [../../prompts/{prompt-file}.prompt.md](../../prompts/{prompt-file}.prompt.md)

### Skills
- **Skill**: [../../skills/{skill-dir}/SKILL.md](../../skills/{skill-dir}/SKILL.md)

## Error Handling (错误处理)

> 遇到以下情况时的处理策略

### EH-1: {错误情况1}

- **识别信号**：{信号描述}
- **处理方式**：
  1. {处理步骤1}
  2. {处理步骤2}
  3. {处理步骤3}
- **升级条件**：{升级条件}

### EH-2: {错误情况2}

- **识别信号**：{信号描述}
- **处理方式**：
  1. {处理步骤1}
  2. {处理步骤2}
  3. {处理步骤3}
- **升级条件**：{升级条件}

## Expected Output

### 产出清单

1. **{产出1}**：{说明}
2. **{产出2}**：{说明}

### 输出格式

```markdown
## {产出标题}

### 1. 文档信息
...
```

## Prerequisites

### 必需前置条件

1. {前置条件1}
2. {前置条件2}
3. {前置条件3}

### 可选前置条件

1. {可选条件1}
2. {可选条件2}

## Quality Gates

### 阶段准入

- [ ] {准入条件1}
- [ ] {准入条件2}
- [ ] {准入条件3}

### 阶段准出

- [ ] {准出条件1}
- [ ] {准出条件2}
- [ ] {准出条件3}

## Decision Checkpoints (决策检查点)

> AI 执行过程中必须停下来等待人工决策的关键节点

| 检查点 | 触发条件 | 等待决策 | 下一步 |
|--------|----------|----------|--------|
| **DC-1: {检查点1}** | {触发条件} | {决策内容} | 继续或修正 |
| **DC-2: {检查点2}** | {触发条件} | {决策内容} | 继续或修正 |

### 决策检查点执行规范

```
执行流程:
1. 到达检查点 → 暂停执行
2. 生成决策材料 → 总结要点
3. 等待反馈 → 标注 [待确认]
4. 获取决策 → 继续或修正
5. 记录决策 → 归档到输出文档
```

## Handover Criteria (交接标准)

> 进入下一阶段前必须满足的条件

| 条件项 | 状态 | 说明 |
|--------|------|------|
| {交付物1} | ☐ | {完成标准} |
| {交付物2} | ☐ | {完成标准} |
| {交付物3} | ☐ | {完成标准} |

### 交接检查清单

- [ ] 产出文档完整
- [ ] 评审已通过
- [ ] 遗留问题已记录
- [ ] 下一阶段已知晓

## Workflow

```
1. 启动 → {步骤1}
2. {阶段2} → {步骤2}
3. {阶段3} → {步骤3}
4. {阶段4} → {步骤4}
5. 完成 → 输出交付物
```

## Related Scenarios

- **Next**: [../{next-scenario}/SCENARIO.md](../{next-scenario}/SCENARIO.md) - {下一场景}
- **Previous**: [../{prev-scenario}/SCENARIO.md](../{prev-scenario}/SCENARIO.md) - {上一场景}

## Metrics

| 指标 | 目标 | 测量方法 |
|------|------|----------|
| {指标1} | {目标值} | {测量方法} |
| {指标2} | {目标值} | {测量方法} |
| {指标3} | {目标值} | {测量方法} |
