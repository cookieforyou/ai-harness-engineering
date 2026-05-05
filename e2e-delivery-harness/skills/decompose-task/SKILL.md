---

name: decompose-task
description: 将架构设计拆解为可执行的任务清单，制定迭代计划和里程碑
category: planning
version: "1.1.0"
type: skill
---

# Task Decomposition Skill

## Use When

使用此技能的场景：

- 架构设计完成后，需要拆解开发任务
- 项目进度不理想，需要重新规划
- 团队规模变化，需要调整任务分配
- 需要制定详细的迭代计划

## Expected Input

### 必需输入

| 输入项 | 类型 | 描述 |
|--------|------|------|
| 架构设计文档 | 文件 | 来自系统设计阶段的输出 |
| 团队能力信息 | 文本 | 团队成员的技术能力分布 |

### 可选输入

| 输入项 | 类型 | 描述 |
|--------|------|------|
| 时间约束 | 文本 | 项目的交付时间要求 |
| 迭代策略 | 文本 | 期望的迭代周期和节奏 |
| 历史数据 | 文件 | 历史项目的工作量数据 |

## Instructions

### 步骤 1：任务识别

**目标**：从架构设计中识别需要完成的开发任务

**操作**：
1. 按组件拆解功能点
2. 识别基础设施任务
3. 识别公共模块开发任务
4. 识别集成对接任务
5. 识别测试环境任务
6. 识别文档任务

**检查点**：
- [ ] 所有功能点已拆解
- [ ] 技术任务已识别
- [ ] 任务分类清晰

### 步骤 2：任务细化

**目标**：将大任务拆分为可执行的小任务

**操作**：
1. 评估任务粒度（目标 1-3 天）
2. 拆分粒度过大的任务
3. 合并粒度过小的任务
4. 为每个任务定义验收标准
5. 标注任务类型（功能/技术债务/基础设施）

**检查点**：
- [ ] 90% 任务在 1-3 天范围
- [ ] 每个任务有验收标准
- [ ] 任务类型已标注

### 步骤 3：依赖分析

**目标**：分析任务间的依赖关系

**操作**：
1. 识别任务间的硬依赖（必须先完成）
2. 识别任务间的软依赖（建议顺序）
3. 识别可并行执行的任务
4. 绘制任务依赖图
5. 识别关键路径

**检查点**：
- [ ] 所有依赖已标注
- [ ] 无循环依赖
- [ ] 关键路径已识别

### 步骤 4：工作量估算

**目标**：评估每个任务的开发时间

**操作**：
1. 使用历史数据参考
2. 采用三点估算法（乐观、悲观、最可能）
3. 考虑学习和准备时间
4. 汇总各迭代工时
5. 预留缓冲时间（10-20%）

**检查点**：
- [ ] 每个任务有估算
- [ ] 估算有依据
- [ ] 缓冲时间已预留

### 步骤 5：优先级排序

**目标**：确定任务的执行优先级

**操作**：
1. 评估业务价值
2. 考虑技术依赖
3. 评估风险因素
4. 确定优先级（P0/P1/P2）
5. 考虑干系人期望

**检查点**：
- [ ] 所有任务有优先级
- [ ] 优先级与价值匹配
- [ ] 高优先级任务已确认

### 步骤 6：迭代规划

**目标**：将任务分配到迭代计划中

**操作**：
1. 确定迭代周期（通常 1-2 周）
2. 确定每个迭代的目标
3. 分配任务到迭代
4. 平衡迭代负载
5. 制定里程碑计划

**检查点**：
- [ ] 迭代目标明确
- [ ] 迭代负载平衡
- [ ] 里程碑已确定

### 步骤 7：资源分配

**目标**：将任务分配给团队成员

**操作**：
1. 根据技能匹配分配任务
2. 考虑团队成员负载
3. 标注任务负责人
4. 确认资源可用性

**检查点**：
- [ ] 任务已分配
- [ ] 负责人已标注
- [ ] 负载已平衡

## Expected Output

### 产出列表

1. **任务分解清单**：完整的开发任务列表
2. **任务依赖图**：任务间的依赖关系
3. **迭代计划**：各迭代的任务分配
4. **工作量评估**：工时估算汇总

### 输出格式

```markdown
## Task Decomposition Checklist

### 任务总览
...

### 任务详情
...

### 依赖关系
...

### 迭代计划
...

### 里程碑计划
...
```

## Quality Criteria

| 维度 | 标准 | 检查方法 |
|------|------|----------|
| 完整性 | 所有设计都有对应任务 | 设计映射 |
| 可执行性 | 任务粒度适中 | 粒度检查 |
| 依赖清晰 | 依赖关系明确 | 依赖检查 |
| 优先级合理 | 优先级与价值匹配 | 优先级检查 |

## Related Assets

- **Agent**: [../../agents/decompose-task.agent.md](../../agents/decompose-task.agent.md)
- **Instruction**: [../../instructions/decompose-task.instructions.md](../../instructions/decompose-task.instructions.md)
- **Prompt**: [../../prompts/decompose-task.prompt.md](../../prompts/decompose-task.prompt.md)


## Core Knowledge

> Essential knowledge domain for decompose-task execution.

### Domain Fundamentals
- [Core concept 1]
- [Core concept 2]
- [Core concept 3]

### Key Principles
1. [Principle 1]
2. [Principle 2]
3. [Principle 3]


## Best Practices

> Proven practices for decompose-task excellence.

1. **Practice 1**: [Description and rationale]
2. **Practice 2**: [Description and rationale]
3. **Practice 3**: [Description and rationale]


## Common Pitfalls

> Frequent mistakes to avoid during decompose-task execution.

### Pitfall 1: [Name]
**Risk**: [Description]
**Prevention**: [How to avoid]
**Impact**: [Consequences if not avoided]

### Pitfall 2: [Name]
**Risk**: [Description]
**Prevention**: [How to avoid]
**Impact**: [Consequences if not avoided]

### Pitfall 3: [Name]
**Risk**: [Description]
**Prevention**: [How to avoid]
**Impact**: [Consequences if not avoided]
