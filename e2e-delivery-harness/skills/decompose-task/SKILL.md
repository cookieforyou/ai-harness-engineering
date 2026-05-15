---
name: decompose-task
description: "任务拆分技能包，提供任务分解、估算、依赖分析的专业知识和最佳实践"
type: skill
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: [skill, knowledge, planning]
---
# Task Decomposition Skill

## Skill Overview

本技能包提供任务拆分的专业知识、最佳实践和常见陷阱，指导AI高质量地完成从架构设计到任务清单的转换。

### Core Competencies

- **INVEST原则应用**: 确保任务独立、可协商、有价值、可估算、小、可测试
- **工作量估算**: 基于历史数据和团队能力进行准确估算
- **依赖分析**: 识别任务间的技术依赖和执行顺序
- **迭代规划**: 制定合理的Sprint计划和里程碑
- **风险管理**: 识别潜在风险并制定应对策略

## Use When

使用此技能的场景：

- 架构设计完成后，需要将架构设计转换为可执行任务
- Sprint规划前，需要制定详细的迭代计划
- 需求变更时，需要重新评估和调整任务分解
- 团队规模变化，需要重新分配任务和调整计划

## Instructions

### 步骤 1：架构分析与任务识别

**目标**: 理解架构设计，识别所有开发任务

**操作方法**:
1. **阅读架构设计文档**
   - 提取核心模块列表
   - 识别技术栈和框架
   - 理解模块间依赖关系

2. **按维度识别任务**
   - **前端任务**: UI组件开发、页面集成、状态管理
   - **后端任务**: API开发、业务逻辑实现、数据访问层
   - **数据库任务**: Schema设计、索引优化、数据迁移
   - **测试任务**: 单元测试、集成测试、端到端测试
   - **DevOps任务**: CI/CD配置、部署脚本、监控告警

3. **建立需求-任务映射**
   - 为每个功能需求创建对应的任务
   - 为非功能性需求创建专门任务
   - 确保100%需求覆盖

**检查点**:
- [ ] 所有功能模块已识别
- [ ] 任务覆盖前端、后端、数据库、测试、DevOps
- [ ] 需求-任务映射表100%覆盖

---

### 步骤 2：任务细化与粒度调整

**目标**: 确保任务粒度符合INVEST原则

**操作方法**:
1. **应用INVEST原则**
   - **Independent（独立）**: 任务可以独立开发和测试
   - **Negotiable（可协商）**: 任务细节可以与团队讨论
   - **Valuable（有价值）**: 任务对业务或技术有明确价值
   - **Estimable（可估算）**: 团队可以估算工作量
   - **Small（小）**: 任务可以在1-3天内完成
   - **Testable（可测试）**: 任务有明确的验收标准

2. **拆分过大的任务（>5天）**
   - 按功能子模块拆分
   - 按技术层次拆分（API、Service、DAO）
   - 按CRUD操作拆分（Create、Read、Update、Delete）

3. **合并过小的任务（<0.5天）**
   - 合并相关的CRUD操作
   - 合并同一模块的小任务
   - 减少上下文切换成本

4. **验证粒度合适性**
   - 90%任务在1-3天范围内
   - 无>5天的超大任务
   - 无<0.5天的超小任务

**检查点**:
- [ ] 90%任务符合INVEST原则
- [ ] 任务粒度在1-3天范围内
- [ ] 无过大或过小的任务

---

### 步骤 3：依赖分析与关键路径识别

**目标**: 识别任务间依赖关系，绘制依赖图

**操作方法**:
1. **识别依赖类型**
   - **技术依赖**: 任务B需要任务A的输出（如API需要先于前端开发）
   - **资源依赖**: 多个任务需要同一人员或设备
   - **逻辑依赖**: 任务B的逻辑依赖于任务A的决策

2. **绘制依赖图（DAG）**
   - 使用有向无环图（Directed Acyclic Graph）
   - 节点表示任务，边表示依赖关系
   - 确保无循环依赖

3. **识别关键路径**
   - 找出最长路径（决定项目总工期）
   - 标注关键路径上的任务
   - 优先保障关键路径任务的资源

4. **优化依赖关系**
   - 最小化串行依赖，最大化并行可能性
   - 引入抽象层打破紧耦合
   - 提前开发共享组件

**检查点**:
- [ ] 所有任务依赖已标注
- [ ] 无循环依赖
- [ ] 关键路径已识别
- [ ] 依赖图可视化

---

### 步骤 4：工作量估算

**目标**: 基于历史数据和团队能力进行准确估算

**操作方法**:
1. **选择估算方法**
   - **故事点（Story Points）**: 相对复杂度估算（适合敏捷团队）
   - **人天（Person-Days）**: 绝对时间估算（适合传统项目）
   - **T-shirt尺寸**: 粗略估算（S/M/L/XL，适合早期阶段）

2. **参考历史数据**
   - 查找类似任务的 historical data
   - 计算平均估算准确率
   - 调整当前估算基准

3. **考虑影响因素**
   - **复杂度**: 技术难度、业务逻辑复杂度
   - **不确定性**: 新技术、外部依赖、需求模糊
   - **团队能力**: 技能匹配度、经验水平
   - **风险缓冲**: 高风险任务增加10-20%缓冲

4. **验证估算合理性**
   - 对比类似任务的历史估算
   - 团队评审估算结果（Planning Poker）
   - 确保估算偏差在±20%以内

**检查点**:
- [ ] 所有任务有工作量估算
- [ ] 估算有依据支撑
- [ ] 考虑了风险缓冲
- [ ] 估算偏差在±20%以内

---

### 步骤 5：优先级排序

**目标**: 基于业务价值、技术风险、依赖关系确定优先级

**操作方法**:
1. **优先级分级**
   - **P0（紧急重要）**: 核心功能、阻塞其他任务、高业务价值
   - **P1（重要不紧急）**: 重要功能、但可延后、中等业务价值
   - **P2（紧急不重要）**: 次要功能、但有时间窗口、低业务价值
   - **P3（其他）**: 锦上添花、可最后做、极低业务价值

2. **评估维度**
   - **业务价值**: 对用户和业务的影响程度
   - **技术风险**: 不确定性和失败概率
   - **依赖关系**: 是否阻塞其他任务
   - **学习曲线**: 是否需要新技术学习

3. **排序策略**
   - P0任务优先安排在早期Sprint
   - 高风险任务提前做，降低不确定性
   - 考虑依赖关系，前置任务优先
   - 平衡短期交付和长期价值

**检查点**:
- [ ] 所有任务有优先级标注
- [ ] P0任务占比合理（20-30%）
- [ ] 优先级与业务价值匹配
- [ ] 高风险任务已提前安排

---

### 步骤 6：迭代规划与Sprint安排

**目标**: 将任务分配到Sprint，制定迭代计划

**操作方法**:
1. **计算团队产能**
   ```
   每Sprint产能 = 开发人员数 × 每日有效工时 × Sprint天数
   例如：3人 × 7小时 × 10天 = 210小时 = 26.25人天
   ```

2. **分配任务到Sprint**
   - 优先安排P0任务
   - 考虑依赖关系，前置任务先安排
   - 负载均衡，避免单点过载
   - Sprint计划不超过产能的90%

3. **定义Sprint Goal**
   - 每个Sprint有明确的目标
   - 目标聚焦于可交付的功能
   - 目标可量化、可验证

4. **预留缓冲时间**
   - 预留10%产能作为缓冲
   - 用于处理突发问题和风险
   - 提高计划的可预测性

**检查点**:
- [ ] Sprint计划不超过产能90%
- [ ] 每个Sprint有明确目标
- [ ] 负载均衡，无单点过载
- [ ] 预留10%缓冲时间

---

### 步骤 7：风险管理与应对策略

**目标**: 识别潜在风险并制定应对措施

**操作方法**:
1. **风险识别**
   - **技术风险**: 新技术不确定性、性能瓶颈
   - **资源风险**: 人员变动、技能缺口
   - **依赖风险**: 第三方服务延迟、外部依赖不可用
   - **需求风险**: 需求变更、范围蔓延

2. **风险评估**
   - **概率**: 高/中/低
   - **影响**: 高/中/低
   - **风险等级**: 概率 × 影响

3. **应对策略**
   - **规避**: 改变计划以消除风险
   - **转移**: 将风险转嫁给第三方
   - **缓解**: 降低风险概率或影响
   - **接受**: 接受风险并准备应急计划

4. **风险监控**
   - 定期审查风险状态
   - 更新风险登记册
   - 触发应急预案

**检查点**:
- [ ] Top 5风险已识别
- [ ] 每个风险有应对策略
- [ ] 高风险任务已提前安排
- [ ] 风险监控机制已建立

## Core Knowledge

### INVEST Principle

**Independent**:
- Tasks can be developed and tested independently
- Minimal dependencies on other tasks
- Enables parallel development

**Negotiable**:
- Task details are open for discussion
- Not overly prescriptive
- Allows team input and refinement

**Valuable**:
- Delivers clear business or technical value
- Aligns with project goals
- Stakeholders understand the benefit

**Estimable**:
- Team can estimate effort with confidence
- Clear scope and requirements
- Known technology and approach

**Small**:
- Completable within 1-3 days
- Reduces uncertainty
- Enables frequent feedback

**Testable**:
- Has clear acceptance criteria
- Can be verified objectively
- Supports definition of done (DoD)

### Estimation Techniques

**Story Points**:
- Relative complexity estimation
- Uses Fibonacci sequence (1, 2, 3, 5, 8, 13)
- Accounts for complexity, uncertainty, effort

**Person-Days**:
- Absolute time estimation
- Based on historical data
- More precise but less flexible

**Planning Poker**:
- Collaborative estimation technique
- Team members vote independently
- Discuss differences and reach consensus

### Dependency Types

**Technical Dependencies**:
- Task B requires output from Task A
- Example: API must be built before frontend integration

**Resource Dependencies**:
- Multiple tasks need same person or equipment
- Example: Two tasks require same senior developer

**Logical Dependencies**:
- Task B's logic depends on Task A's decision
- Example: Database schema must be finalized before ORM mapping

## Best Practices

### 1. Follow INVEST Principles Rigorously

**Practice Description**: Ensure every task meets all six INVEST criteria.

**Rationale**: INVEST-compliant tasks are easier to estimate, track, and complete.

**How to Apply**:
- Review each task against INVEST checklist
- Split tasks that fail any criterion
- Merge tasks that are too small
- Validate with team during refinement sessions

---

### 2. Use Historical Data for Estimation

**Practice Description**: Base estimates on actual data from similar past tasks.

**Rationale**: Historical data provides objective baseline and improves accuracy.

**How to Apply**:
- Maintain estimation database
- Track actual vs. estimated effort
- Calculate estimation accuracy rate
- Adjust future estimates based on trends

---

### 3. Identify Critical Path Early

**Practice Description**: Find the longest path through the dependency graph.

**Rationale**: Critical path determines minimum project duration; delays here impact entire timeline.

**How to Apply**:
- Draw dependency graph (DAG)
- Calculate path lengths
- Mark critical path tasks
- Prioritize resources for critical path

---

### 4. Reserve Buffer Time

**Practice Description**: Allocate 10% capacity as buffer for unexpected issues.

**Rationale**: Improves plan reliability and reduces stress from unforeseen problems.

**How to Apply**:
- Plan sprints at 90% capacity
- Use buffer for bug fixes, emergencies, learning
- Track buffer utilization
- Adjust future plans based on buffer usage

---

### 5. Conduct Regular Estimation Reviews

**Practice Description**: Compare actual effort vs. estimates after each sprint.

**Rationale**: Continuous improvement of estimation accuracy through feedback loop.

**How to Apply**:
- Record actual effort spent
- Calculate estimation variance
- Identify patterns (over/under estimation)
- Adjust estimation approach accordingly

---

### 6. Break Down by Technical Layers

**Practice Description**: Split large features into frontend, backend, database, and test tasks.

**Rationale**: Enables parallel work by specialists and clearer responsibility assignment.

**How to Apply**:
- For each feature, create:
  - Frontend task (UI components, integration)
  - Backend task (API, business logic)
  - Database task (schema, migrations)
  - Test task (unit, integration tests)
- Define clear interfaces between layers

## Common Pitfalls

### Pitfall 1: Overly Large Tasks

**Risk**: Tasks >5 days are hard to estimate accurately and track progress.

**Prevention**:
- Enforce maximum task size (5 days)
- Split by sub-features or technical layers
- Use subtasks for complex items

**Impact**: Poor estimation accuracy, delayed feedback, difficulty tracking progress

---

### Pitfall 2: Ignoring Dependencies

**Risk**: Unidentified dependencies cause blockers and delays during execution.

**Prevention**:
- Systematically analyze all task relationships
- Draw dependency graph
- Review with team to catch missed dependencies
- Update graph as new dependencies emerge

**Impact**: Blocked tasks, idle resources, schedule delays

---

### Pitfall 3: Optimistic Estimation

**Risk**: Underestimating complexity leads to missed deadlines and team burnout.

**Prevention**:
- Use historical data as baseline
- Include risk buffer (10-20%)
- Account for learning curve
- Get team consensus (Planning Poker)

**Impact**: Missed deadlines, quality compromises, team stress

---

### Pitfall 4: Unclear Acceptance Criteria

**Risk**: Ambiguous task definitions lead to rework and disputes.

**Prevention**:
- Define clear, testable acceptance criteria
- Use Given-When-Then format
- Review criteria with stakeholders
- Ensure criteria are measurable

**Impact**: Rework, scope creep, stakeholder dissatisfaction

## Related Assets

- **Scenario**: [../scenarios/decompose-task/SCENARIO.md](../scenarios/decompose-task/SCENARIO.md)
- **Agent**: [../agents/decompose-task.agent.md](../agents/decompose-task.agent.md)
- **Prompt**: [../prompts/decompose-task.prompt.md](../prompts/decompose-task.prompt.md)
- **Instruction**: [../instructions/decompose-task.instructions.md](../instructions/decompose-task.instructions.md)
