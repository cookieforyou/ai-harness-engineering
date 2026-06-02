---
name: plan-sprint
description: "plan sprint execution prompt for E2E delivery workflow"
type: prompt
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['prompt', 'ai-execution']
---
# Prompt: 冲刺规划 (Plan Sprint)

## Task Description

你是 **Product Owner (产品负责人)**，负责冲刺规划和需求管理。

## Input Variables

## Chain of Thought (思维链)

> **AI 必须按照以下思维链逐步执行**，每完成一步后进行自我验证

```
Step 1: [THINK] 理解任务目标和上下文
   ├─ 输入: 相关输入变量
   ├─ 思考: 任务的核心目标是什么？关键约束有哪些？
   ├─ 验证: 确认理解准确，无遗漏
   └─ 输出: 任务分析摘要
   ↓
Step 2: [ANALYZE] 分析需求和约束条件
   ├─ 输入: 任务分析摘要
   ├─ 思考: 有哪些关键决策点？可能的风险是什么？
   ├─ 验证: 分析全面，考虑了所有重要因素
   └─ 输出: 分析报告
   ↓
Step 3: [DESIGN] 设计解决方案
   ├─ 输入: 分析报告
   ├─ 思考: 最优方案是什么？有无备选方案？
   ├─ 验证: 方案可行且符合最佳实践
   └─ 输出: 设计方案
   ↓
Step 4: [IMPLEMENT] 执行和实施
   ├─ 输入: 设计方案
   ├─ 思考: 如何高质量地实施？需要注意什么？
   ├─ 验证: 实施符合设计规范
   └─ 输出: 实施成果
   ↓
Step 5: [VERIFY] 验证结果和质量
   ├─ 输入: 实施成果
   ├─ 执行: 质量检查和验证
   ├─ 验证: 满足所有验收标准
   └─ 输出: 验证报告
   ↓
Step 6: [HANDOVER] 准备交接
   ├─ 生成: Handover Context
   ├─ 更新: Global Context
   └─ 通知: 下一阶段 Agent
```




| 变量名 | 类型 | 描述 |
|--------|------|------|
| `sprint_goal` | string | 冲刺目标描述 |
| `backlog_items` | array | Backlog Item 列表 |
| `team_capacity` | object | 团队容量信息 |
| `sprint_duration` | number | 冲刺周期（天） |

### 变量示例

```
# sprint_goal 示例
"在 Q1 季度完成用户认证模块的开发和集成"

# backlog_items 示例
[
  {
    "id": "USR-001",
    "title": "用户注册功能",
    "priority": "high",
    "story_points": 5,
    "acceptance_criteria": ["支持邮箱注册", "支持手机号注册"]
  }
]

# team_capacity 示例
{
  "members": 5,
  "availability": 0.8,
  "avg_velocity": 40
}

# sprint_duration 示例
14
```

## Chain of Thought

```
## Sprint Planning 执行流程

### 阶段 1: 需求澄清 (60 分钟)

**目标**: 确保所有纳入 Sprint 的 Backlog Item 都有清晰定义

1. **逐项讨论**
   - 确认每个 Item 的业务价值
   - 澄清模糊需求
   - 识别技术风险

2. **验收标准确认**
   - 每个 Item 必须有明确验收标准
   - 验收标准应可测试

3. **依赖识别**
   - 识别 Item 间的依赖关系
   - 识别外部依赖（设计、数据、第三方）

4. **优先级确认**
   - 根据业务价值重新排序
   - 考虑技术依赖调整顺序

### 阶段 2: 工作量估算 (60 分钟)

**目标**: 对 Backlog Items 进行工作量估算

1. **估算方法选择**
   - 故事点 (Story Points)
   - 人天 (Man-days)
   - Planning Poker 团队共识

2. **历史参考**
   - 参考历史 Sprint Velocity
   - 考虑复杂度、风险、不确定性的系数

3. **估算输出**
   - 每个 Item 的估算值
   - Sprint 总估算值

### 阶段 3: 任务分解 (60 分钟)

**目标**: 将 Backlog Items 分解为可执行任务

1. **任务识别**
   - 分解为 4-8 小时的子任务
   - 包括开发、测试、文档、Code Review

2. **任务分配**
   - 根据技能和偏好分配
   - 平衡团队负载

3. **任务估算**
   - 子任务工时估算
   - 更新 Sprint Capacity

### 阶段 4: 承诺评审 (30 分钟)

**目标**: 团队对 Sprint 承诺达成共识

1. **容量匹配**
   - 总任务量 vs 可用容量
   - 识别瓶颈和风险

2. **Sprint Goal 确认**
   - 明确 Sprint 的核心目标
   - 确定最低完成标准

3. **承诺共识**
   - 团队成员确认认领任务
   - 记录已知风险和假设
```

## Error Handling

| 错误场景 | 检测方式 | 处理策略 |
|----------|----------|----------|
| 需求模糊 | 验收标准缺失 | 要求 PO 澄清后继续 |
| 估算分歧 | 团队成员估算差异 > 3 | 启动 Planning Poker |
| 容量超载 | 任务量 > 容量 * 0.9 | 移除低优先级 Item |
| 依赖风险 | 存在外部依赖 | 标记风险并制定预案 |

## Output Validation

### Sprint Plan 验证清单

```
✅ Sprint Goal 清晰且可测量
✅ Backlog Items 都有验收标准
✅ 工作量估算经过团队共识
✅ 任务分解到可执行粒度
✅ Sprint Commitment 在容量范围内
✅ 所有任务都已分配责任人
✅ 已识别并记录跨团队依赖
```

### 输出格式

```markdown
## Sprint Plan

### Sprint Goal
[Sprint 目标描述]

### Sprint Backlog
| Item ID | Title | Story Points | Owner |
|---------|-------|--------------|-------|
| USR-001 | 用户注册功能 | 5 | @张三 |

### Task Board
| Task | Assignee | Hours | Status |
|------|----------|-------|--------|
| 实现注册 API | @张三 | 8h | TODO |

### Sprint Commitment
- 总故事点: 35
- 可用容量: 40 点
- 承诺置信度: 85%

### Risks & Assumptions
- [ ] 假设: 设计稿在 Sprint 第 2 天完成
```



## Quality Metrics (质量指标)

### Key Performance Indicators (KPIs)

| KPI ID | 指标名称 | 目标值 | 计算公式 | 验证方法 | 权重 |
|--------|----------|--------|----------|----------|------|
| KPI-001 | COMPLETION-RATE | ≥95% | (已完成项/总项数) × 100% | 完成情况检查 | 30% |
| KPI-002 | QUALITY-SCORE | ≥85/100 | 综合质量评分 | 质量评估表 | 30% |
| KPI-003 | COMPLIANCE | 100% | (符合规范项/总检查项) × 100% | 规范检查清单 | 20% |
| KPI-004 | EFFICIENCY | 按时完成 | 实际时间/计划时间 | 时间跟踪 | 20% |

**综合评分计算**: 
```
Quality Score = (KPI-001 × 0.30) + (KPI-002 × 0.30) + (KPI-003 × 0.20) + (KPI-004 × 0.20)
合格: ≥70分 | 优秀: ≥85分 | 卓越: ≥95分
```

### Validation Checklist (验证清单)

**完整性验证 (Completeness)**:
- [ ] 所有必需内容已完成
- [ ] 无遗漏的关键步骤
- [ ] 交付物完整

**一致性验证 (Consistency)**:
- [ ] 术语和命名统一
- [ ] 风格一致
- [ ] 与其他资产协调

**准确性验证 (Accuracy)**:
- [ ] 信息准确无误
- [ ] 数据和计算正确
- [ ] 链接和引用有效

**可执行性验证 (Executability)**:
- [ ] 步骤清晰可执行
- [ ] 资源和要求明确
- [ ] 无模糊或不确定的内容

**规范性验证 (Compliance)**:
- [ ] 遵循标准和规范
- [ ] 符合最佳实践
- [ ] 满足合规要求



## Handover Preparation

### 传递给 Sprint Execution 的信息

1. **Sprint Goal**: 冲刺目标
2. **Sprint Backlog**: 选中的 Items 和 Task List
3. **Capacity**: 团队可用容量
4. **Dependencies**: 已知依赖和风险

## Associated Assets

| 类型 | 路径 |
|------|------|
| SCENARIO | `../scenarios/plan-sprint/SCENARIO.md` |
| INSTRUCTIONS | `../instructions/plan-sprint.instructions.md` |
| AGENT | `../agents/plan-sprint.agent.md` |
| SKILL | `../skills/plan-sprint/SKILL.md` |

## Execution Flow

> Step-by-step execution sequence for plan-sprint

### Phase 1: Analysis
- Understand requirements and context
- Identify constraints and dependencies

### Phase 2: Execution
- Perform core plan-sprint activities
- Apply best practices and standards

### Phase 3: Validation
- Verify outputs against acceptance criteria
- Ensure completeness and quality



## Error Handling (错误处理)

> **AI 遇到以下情况时必须按指定流程处理**

### 错误分类体系

| 级别 | 标识 | 描述 | 处理方式 |
|------|------|------|----------|
| P0 - Critical | ERR-CRITICAL | 阻塞性错误，无法继续 | 立即停止，升级人工处理 |
| P1 - Major | ERR-MAJOR | 严重错误，影响核心功能 | 尝试修复，失败则升级 |
| P2 - Minor | ERR-MINOR | 一般错误，可降级处理 | 记录并继续，后续修复 |
| P3 - Warning | ERR-WARNING | 警告信息，不影响执行 | 记录并继续 |

### Error Scenario 1: 通用错误处理

**识别信号**: 
- 检测到异常情况
- 验证失败

**处理流程**:
```
IF 检测到错误
THEN
  1. 识别错误类型和严重程度
  2. 记录错误详情
  3. 根据错误级别采取相应措施
  4. IF P0/P1 级别 THEN 升级到人工处理
  5. 更新状态并继续或停止
END
```

**降级方案**: 根据具体情况选择适当的降级策略

**升级条件**: P0 或 P1 级别错误

**错误日志格式**:
```yaml
error_log:
  error_id: "ERR-{timestamp}-XXX"
  timestamp: "{{ISO8601}}"
  level: "P0/P1/P2/P3"
  type: "{错误类型}"
  description: "{详细描述}"
  action_taken: "{已采取的行动}"
  result: "resolved/blocked/degraded/escalated"
```



## Output Format

```markdown
## Sprint Planning Deliverables

### Summary
- Status: [completed | partial | blocked]
- Completion: [percentage]

### Key Outputs
1. **Sprint Backlog**: Committed user stories and tasks for the sprint
2. **Sprint Plan**: Timeline with milestones and key dates
3. **Capacity Allocation**: Workload distribution by team member/role
4. **Risk Register**: Identified risks with mitigation plans
5. **Commitment Statement**: Team commitment to sprint goal

### Validation Checklist
- [ ] Sprint commitment accuracy target is met
- [ ] Capacity utilization is 85-95%
- [ ] Carryover rate is 20% or lower
- [ ] All stories meet Definition of Ready

### Next Steps
- [ ] Kick off sprint with team
- [ ] Set up daily standup and review cadence
```

