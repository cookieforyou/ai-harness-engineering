---
name: decompose-task
description: "任务拆分场景，负责将需求分解为可执行、可跟踪、可度量的技术任务"
version: "1.2.0"
type: scenario
category: planning
stage: task-decomposition
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: [planning, decomposition, tasks]
---
# Decompose Task Scenario

## Purpose

将需求规格说明书和技术设计方案分解为可执行、可跟踪、可度量的技术任务，为开发团队提供清晰的工作项清单，确保开发过程的可控性和可预测性。

### Business Value

- **降低认知负荷**: 将复杂需求拆解为小颗粒度任务，减少开发人员的理解成本
- **提升可预测性**: 通过任务估算和依赖分析提高计划准确性和交付可靠性
- **增强可追溯性**: 建立需求-任务-代码的完整追溯链，便于问题定位和进度跟踪
- **优化资源配置**: 基于任务优先级和技能匹配合理分配人力，最大化团队效率

## Chain of Thought (思维链)

### Think-Aloud Protocol (强制遵循)

```
[THINK] Step 1: 理解需求范围和边界
   ├─ 问：需求的业务范围和技术边界是什么？核心功能有哪些？
   ├─ 验证：与需求规格说明书逐条对照，确认理解一致
   └─ 检查：识别所有功能模块、API接口、数据模型、用户交互点
   ↓
[ANALYZE] Step 2: 识别技术任务和依赖
   ├─ 问：实现每个功能需要哪些技术工作？涉及哪些技术栈和组件？
   ├─ 验证：覆盖前端、后端、数据库、测试、部署等全维度
   └─ 检查：识别任务间的依赖关系和并行可能性
   ↓
[DESIGN] Step 3: 设计任务结构和粒度
   ├─ 问：任务粒度是否合适（1-3天工作量）？是否符合INVEST原则？
   ├─ 验证：90%任务在1-3天范围内，符合独立、可估算、可测试要求
   └─ 检查：任务之间有清晰的接口和交付物定义
   ↓
[EVALUATE] Step 4: 估算工作量和优先级
   ├─ 问：每个任务的复杂度、风险和工作量是多少？优先级如何排序？
   ├─ 验证：参考历史数据和团队能力，使用故事点或人天估算
   └─ 检查：考虑学习曲线、技术风险、依赖等待时间
   ↓
[DOCUMENT] Step 5: 输出任务清单和迭代计划
   ├─ 生成任务清单（含ID、名称、描述、验收标准、估算、优先级）
   ├─ 绘制任务依赖图，识别关键路径
   └─ 制定Sprint计划和里程碑安排
   ↓
[VALIDATE] Step 6: 评审确认并准备交接
   ├─ 组织任务评审会议，收集团队反馈
   ├─ 根据反馈调整任务分解和估算
   └─ 获得Tech Lead签字确认，准备交接给开发阶段
```

## Decision Checkpoints (决策检查点)

| ID | 决策点 | 触发条件 | 决策选项 | 选择标准 | 记录位置 |
|----|--------|----------|----------|----------|----------|
| DC-001 | 任务粒度确定 | 任务拆分时 | 粗粒度(>5天) / 中粒度(2-5天) / 细粒度(<2天) | 符合INVEST原则，1-3天为佳 | 任务清单 |
| DC-002 | 优先级排序 | 任务列表完成后 | P0(紧急重要) / P1(重要不紧急) / P2(紧急不重要) / P3(其他) | 业务价值、依赖关系、风险程度 | 任务清单 |
| DC-003 | 估算方法选择 | 开始估算前 | 故事点 / 人天 / T-shirt尺寸 | 团队习惯、项目阶段、精度要求 | 估算说明文档 |
| DC-004 | 依赖处理方式 | 发现复杂依赖时 | 串行执行 / 并行执行+协调 / 重构解耦 | 时间约束、团队能力、长期收益 | 依赖分析文档 |
| DC-005 | 风险缓冲设置 | 高风险任务识别后 | 无缓冲 / 10%缓冲 / 20%缓冲 / 单独风险任务 | 风险概率和影响程度 | 风险管理计划 |

## Error Handling (错误处理)

> **AI 在执行过程中遇到以下情况时的处理策略**

### Error Scenario 1: 任务粒度不当

**识别信号**: 
- 任务估算工作量 >5天（过粗）或 <0.5天（过细）
- 90%任务不在1-3天范围内
- 任务描述模糊，无法明确验收标准

**处理流程**:
```
IF 检测到任务粒度不当
THEN
  1. 识别粒度过大的任务 (>5天)
  2. 拆分为子任务，确保每个子任务符合INVEST原则
  3. 识别粒度过小的任务 (<0.5天)
  4. 合并相关任务，减少上下文切换成本
  5. 验证新粒度是否合适（1-3天工作量为佳）
  6. 更新任务清单和依赖关系
END
```

**降级方案**: 如无法确定合适粒度，标记为"待细化"并升级到Tech Lead确认

**升级条件**: 经过2次调整后仍无法确定合适粒度，需要Tech Lead介入评审

---

### Error Scenario 2: 依赖关系不清晰

**识别信号**: 
- 任务间依赖关系不明确或缺失
- 存在循环依赖（A依赖B，B依赖A）
- 关键路径上的任务缺乏前置任务

**处理流程**:
```
IF 检测到依赖关系不清晰
THEN
  1. 梳理所有任务间的依赖关系
  2. 绘制任务依赖图（有向无环图DAG）
  3. 识别循环依赖并打破（引入抽象层或并行开发）
  4. 识别关键路径和阻塞点
  5. 调整任务顺序，最小化串行依赖
  6. 更新依赖图和关键路径分析
END
```

**降级方案**: 暂时接受当前依赖关系，但标记为"待优化"，在后续迭代中重构

**升级条件**: 存在无法打破的循环依赖或关键路径过长影响交付，需要架构师介入

---

### Error Scenario 3: 资源不足冲突

**识别信号**: 
- 任务总工时超出团队产能 >20%
- 关键路径上的任务缺乏所需技能的成员
- 多个高优先级任务需要同一资源

**处理流程**:
```
IF 检测到资源不足冲突
THEN
  1. 计算任务总工时和团队产能
  2. IF 超出产能 >20% THEN 调整Sprint范围或增加资源
  3. 识别技能缺口，安排培训或外部支持
  4. 重新分配任务，平衡负载
  5. 调整优先级，确保关键任务优先
  6. 更新迭代计划和资源分配方案
END
```

**降级方案**: 降低非核心任务的优先级，延后到后续Sprint

**升级条件**: 资源缺口超过30%且无法通过调整解决，需要项目经理和管理层决策

## Quality Metrics (质量指标)

### Key Performance Indicators (KPIs)

| KPI ID | 指标名称 | 目标值 | 计算公式 | 验证方法 | 权重 |
|--------|----------|--------|----------|----------|------|
| KPI-001 | TASK-COVERAGE | 100% | (已分解需求数/总需求数) × 100% | 需求-任务映射表检查 | 25% |
| KPI-002 | GRANULARITY-SUITABILITY | ≥90% | (符合INVEST原则的任务数/总任务数) × 100% | 任务清单抽样审查 | 20% |
| KPI-003 | DEPENDENCY-COMPLETENESS | 100% | (已识别依赖数/实际依赖数) × 100% | 依赖图完整性检查 | 20% |
| KPI-004 | ESTIMATION-ACCURACY | ±20% | 1 - \|(实际工时-估算工时)/估算工时\| | 历史数据对比分析 | 20% |
| KPI-005 | CLARITY-SCORE | ≥85/100 | 任务描述清晰度评分（DoR检查） | 团队反馈和审查 | 15% |

**综合评分计算**: 
```
Quality Score = (KPI-001 × 0.25) + (KPI-002 × 0.20) + (KPI-003 × 0.20) + (KPI-004 × 0.20) + (KPI-005 × 0.15)
合格: ≥70分 | 优秀: ≥85分 | 卓越: ≥95分
```

### Validation Checklist (验证清单)

**完整性验证 (Completeness)**:
- [ ] 所有功能需求都有对应的任务分解
- [ ] 非功能性需求（性能、安全、可用性）有专门任务
- [ ] 基础设施和DevOps任务已包含
- [ ] 测试任务覆盖单元测试、集成测试、端到端测试

**一致性验证 (Consistency)**:
- [ ] 任务命名规范统一（动词+名词格式）
- [ ] 术语和缩写在整个任务清单中保持一致
- [ ] 任务ID唯一且连续
- [ ] 与其他相关文档（需求规格、架构设计）协调一致

**可行性验证 (Feasibility)**:
- [ ] 任务估算在团队能力范围内
- [ ] Sprint计划不超过团队产能的90%
- [ ] 依赖关系合理，无循环依赖
- [ ] 关键路径时长可接受

**规范性验证 (Compliance)**:
- [ ] 遵循INVEST原则（独立、可协商、有价值、可估算、小、可测试）
- [ ] 每个任务有明确的验收标准（DoD）
- [ ] 任务描述清晰，无歧义
- [ ] 优先级标注合理（P0-P3）


## Handover Criteria

```
✅ 所有必需交付物已生成并通过 Output Validation
✅ 质量评分达到合格标准（≥70 分）
✅ 决策点 DC-* 已记录 rationale
✅ 开放问题与风险已写入 Handover
✅ Handover Context YAML 已生成
```

### Handover Context Template

```yaml
handover:
  header:
    from_stage: "task-decomposition"
    to_stage: "development"
    handover_id: "HO-{timestamp}-{sequence}"
    timestamp: "{ISO8601}"
    prepared_by: "decompose-task"
  summary:
    status: completed|partial|blocked
    quality_score: {0-100}
  artifacts:
    delivered: []
  decisions: []
  open_issues:
    blocking: []
    non_blocking: []
  risks: []
  quality_metrics:
    kpi_results: []
  recommendations: []
```

## Related Assets (关联资产)

| Asset Type | Path | Description |
|------------|------|-------------|
| Agent | `../../agents/decompose-task.agent.md` | 任务拆分Agent角色定义 |
| Prompt | `../../prompts/decompose-task.prompt.md` | 任务拆分提示词模板 |
| Skill | `../../skills/decompose-task/SKILL.md` | 任务拆分技能包 |
| Instruction | `../../instructions/decompose-task.instructions.md` | 任务拆分技术指令 |

## Related Resources (相关资源)

- **Standards**: 
  - [INVEST Principle](../../standards/invest-principle.md) - INVEST原则详解
  - [Task Naming Convention](../../standards/task-naming-convention.md) - 任务命名规范
- **Templates**: 
  - [Task List Template](../../templates/task-list.template.md) - 任务清单模板
  - [Dependency Graph Template](../../templates/dependency-graph.template.md) - 依赖图模板
- **Evaluations**: 
  - [Task Quality Checklist](../../evaluations/task-quality-checklist.md) - 任务质量检查清单
  - [Estimation Accuracy Review](../../evaluations/estimation-accuracy-review.md) - 估算准确性回顾
