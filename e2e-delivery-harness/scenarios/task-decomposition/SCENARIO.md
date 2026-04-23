# Task Decomposition Scenario

## Purpose

将架构设计拆解为可执行的任务清单，制定迭代计划和里程碑。

## Chain of Thought (思维链)

> AI 执行时的思维引导，帮助逐步完成任务分解工作

### Think-Aloud Protocol

```
THINK: 理解设计范围和边界
   ↓
THINK: 识别任务和依赖
   ↓
THINK: 估算工作量和优先级
   ↓
THINK: 规划迭代和里程碑
   ↓
THINK: 验证计划的可行性
   ↓
THINK: 识别风险任务和缓冲
```

### Step-by-Step Reasoning

**Step 1: 范围确认**
- 问：设计文档中的所有内容都需要实现吗？
- 验证：是否有 MVP 定义
- 检查：哪些是必须项，哪些是可选项

**Step 2: 任务识别**
- 问：每个功能点可以分解成哪些任务？
- 验证：任务粒度是否适中（1-3天）
- 检查：是否有被遗漏的任务

**Step 3: 依赖分析**
- 问：任务之间有什么依赖关系？
- 验证：依赖链是否合理
- 检查：是否可以并行开发

**Step 4: 工作量估算**
- 问：每个任务需要多少工作量？
- 验证：估算是否有历史数据支撑
- 检查：估算偏差是否可接受

**Step 5: 迭代规划**
- 问：如何划分迭代？
- 验证：每个迭代是否有清晰目标
- 检查：里程碑是否可达成

## Primary Assets

### Agent

- **Agent**: [../../agents/task-decomposer.agent.md](../../agents/task-decomposer.agent.md)

### Instruction

- **Instruction**: [../../instructions/task-decomposition.instructions.md](../../instructions/task-decomposition.instructions.md)

### Prompt

- **Prompt**: [../../prompts/decompose-task.prompt.md](../../prompts/decompose-task.prompt.md)

### Skills

- **Skill**: [../../skills/task-decomposition/SKILL.md](../../skills/task-decomposition/SKILL.md)

## Expected Output

### 产出清单

1. **任务分解清单**：完整的开发任务列表
2. **任务依赖图**：任务间的依赖关系
3. **迭代计划**：各迭代的任务分配
4. **工作量评估**：工时估算汇总

### 输出格式

```markdown
## 任务分解清单

### 1. 文档信息
...

### 2. 任务清单
...

### 3. 依赖关系
...

### 4. 迭代计划
...

### 5. 里程碑计划
...

### 6. 资源配置
...

### 7. 风险与应对
...
```

## Prerequisites

### 必需前置条件

1. 架构设计文档已确认
2. 团队能力信息已了解
3. 交付时间要求已明确

### 可选前置条件

1. 历史项目工作量数据
2. 团队成员技能档案
3. 迭代策略定义

## Quality Gates

### 阶段准入

- [ ] 架构设计文档已确认
- [ ] 团队能力已评估
- [ ] 时间约束已明确

### 阶段准出

- [ ] 任务分解清单完成
- [ ] 任务粒度适中（1-3天）
- [ ] 依赖关系清晰
- [ ] 迭代计划可行

## Workflow

```
1. 启动 → 理解架构设计
2. 任务识别 → 识别开发任务
3. 任务细化 → 拆分任务粒度
4. 依赖分析 → 分析任务依赖
5. 估算排序 → 评估和排序
6. 迭代规划 → 制定迭代计划
7. 完成 → 输出任务分解清单
```

## Related Scenarios

- **Next**: [../development/SCENARIO.md](../development/SCENARIO.md) - 开发实现
- **Previous**: [../system-design/SCENARIO.md](../system-design/SCENARIO.md) - 系统设计

## Metrics

| 指标 | 目标 | 测量方法 |
|------|------|----------|
| 任务粒度 | 90% 在 1-3 天 | 粒度统计 |
| 依赖标注率 | 100% | 依赖检查 |
| 估算偏差 | < 20% | 实际对比 |
| 计划达成率 | > 80% | 里程碑对比 |
