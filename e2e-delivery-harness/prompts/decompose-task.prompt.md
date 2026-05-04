---
name: decompose-task
description: 任务分解提示词，用于将架构设计拆解为可执行的任务清单
type: planning
version: "1.1.0"
stage: task-decomposition
---

# Decompose Task

> **版本**: 1.1.0 | **适用阶段**: 任务分解 | **预计工时**: 1-2小时

## Input Variables

> AI 在执行前必须确认以下变量已填充

| 变量名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|------|
| `project_name` | string | 是 | 项目名称 | "电商订单系统" |
| `architecture_design` | string | 是 | 架构设计文档路径 | "design.md" |
| `team_capacity` | object | 是 | 团队产能配置 | 见 TeamCapacity 结构 |
| `sprint_duration` | number | 是 | Sprint 周期(天) | 14 |
| `team_members` | string[] | 是 | 团队成员列表 | ["开发A", "开发B"] |
| `available_skills` | string[] | 否 | 可用技能 | ["React", "Python"] |
| `risk_tolerance` | enum | 否 | 风险承受能力 | LOW/MEDIUM/HIGH |

### TeamCapacity 结构

```typescript
interface TeamCapacity {
  developers: number;          // 开发人员数量
  qa_engineers: number;        // QA 人员数量
  devops: number;             // DevOps 人员数量
  working_hours_per_day: number; // 每日有效工时
  capacity_per_sprint: number; // 每 Sprint 可用工时
}
```

## Chain of Thought

```
1. [THINK] 理解架构 → 模块边界和技术选型是否清晰？
2. [THINK] 任务识别 → 所有功能模块都有对应任务？
3. [THINK] 任务细化 → 任务粒度是否适中(1-3天)？
4. [THINK] 依赖分析 → 依赖关系是否完整无遗漏？
5. [THINK] 估算排序 → 估算是否考虑了风险？
6. [VALIDATE] 验证输出 → 任务清单是否完整可执行？
7. [OUTPUT] 生成交付物 → 任务清单 + Sprint 计划
```

## Error Handling

### 情况 1：架构设计信息不足

```
IF 架构设计文档缺少关键信息
THEN
  1. 识别缺失的信息项
  2. 基于常见架构模式进行合理假设
  3. 在输出中标注 [基于假设] 的部分
  4. 列出需要补充确认的问题
END
```

### 情况 2：任务粒度不均

```
IF 任务粒度差异过大
THEN
  1. 识别粒度过大的任务 (> 5天)
  2. 拆分为子任务
  3. 识别粒度过小的任务 (< 0.5天)
  4. 合并为组合任务
END
```

### 情况 3：资源不足冲突

```
IF 任务需求超出团队产能
THEN
  1. 计算产能缺口
  2. 识别可推迟的任务
  3. 建议调整 Sprint 范围
  4. 标记为 [需要决策] 的事项
END
```

### 情况 4：循环依赖

```
IF 存在循环依赖
THEN
  1. 识别参与循环的任务
  2. 引入抽象层打破循环
  3. 或标记需要并行开发的窗口
  4. 制定临时方案
END
```

## Input Format

```markdown
## Architecture Design Document

### 模块划分
[模块列表及职责]

### 接口设计
[接口列表]

### 数据设计
[数据模型]

### 部署方案
[部署架构]

### 技术选型
[技术栈]

### 实施计划
[里程碑计划]
```

## Task Steps

### 步骤 1：任务识别

**任务**：
- 从模块划分中识别开发任务
- 识别基础设施任务
- 识别公共模块任务
- 识别集成任务
- 识别测试任务

**产出**：初步任务清单

### 步骤 2：任务细化

**任务**：
- 将大任务拆分为小任务
- 确保粒度适中（1-3天）
- 为每个任务定义验收标准
- 标注任务类型

**产出**：细化后的任务清单

### 步骤 3：依赖分析

**任务**：
- 分析任务间的依赖关系
- 绘制依赖图
- 识别可并行任务
- 识别关键路径

**产出**：任务依赖图

### 步骤 4：估算与排序

**任务**：
- 估算每个任务的工时
- 确定任务优先级
- 考虑资源约束
- 制定初步计划

**产出**：带估算的任务清单

### 步骤 5：迭代规划

**任务**：
- 划分迭代周期
- 分配任务到迭代
- 平衡迭代负载
- 制定里程碑

**产出**：迭代计划

## Output Format

```markdown
# 任务分解清单

## 1. Document Information
- 项目名称：
- 版本：1.0
- 日期：[当前日期]
- 总任务数：X
- 总工时：X 人天

## 2. Task List

### 2.1 任务总览
| ID | 任务名称 | 模块 | 类型 | 优先级 | 估算(人天) | 负责人 | 依赖 |
|----|----------|------|------|--------|------------|--------|------|
| T001 | 任务名称 | 模块A | 功能 | P0 | 2 | - | - |

### 2.2 任务详情

#### T001: [任务名称]
- **模块**: [所属模块]
- **类型**: [功能/技术债务/基础设施/测试]
- **优先级**: [P0/P1/P2]
- **估算**: [X] 人天
- **依赖任务**: [Txxx]
- **验收标准**:
  1. [标准1]
  2. [标准2]
- **技术要点**:
  - [要点1]
  - [要点2]

#### T002: [任务名称]
...

## 3. Dependencies

### 3.1 依赖图
```
[TODO: 绘制依赖关系图]
```

### 3.2 关键路径
- 路径：[T001] → [T005] → [T010] → [T015]
- 总工期：X 天

### 3.3 可并行任务
| 组 | 任务 | 说明 |
|----|------|------|
| 组1 | T001, T002 | 可并行开发 |

## 4. Iteration Plan

### 4.1 迭代总览
| 迭代 | 时间 | 任务数 | 工时 | 目标 |
|------|------|--------|------|------|
| Sprint 1 | Week 1-2 | X | X | 完成基础设施 |
| Sprint 2 | Week 3-4 | X | X | 完成核心功能 |

### 4.2 Sprint 1: [迭代名称]
**时间**: [开始日期] - [结束日期]
**目标**: [迭代目标]

**任务列表**:
| ID | 任务名称 | 估算 | 验收标准 |
|----|----------|------|----------|
| T001 | 任务1 | 2天 | 标准 |

**完成标准**:
- [完成条件1]
- [完成条件2]

### 4.3 Sprint 2: [迭代名称]
...

## 5. Milestone Plan

| 里程碑 | 计划日期 | 交付物 | 状态 |
|--------|----------|--------|------|
| M1: 架构完成 | Week 1 | 架构设计 | 待开始 |
| M2: 功能完成 | Week 4 | 可运行系统 | 待开始 |

## 6. Resource Allocation

### 6.1 团队能力
| 角色 | 人数 | 技能 | 备注 |
|------|------|------|------|
| 前端开发 | 2 | Vue3 | - |

### 6.2 容量规划
| 迭代 | 可用工时 | 计划工时 | 缓冲 |
|------|----------|----------|------|
| Sprint 1 | 20 | 18 | 10% |

## 7. Risks & Mitigation

| 风险 | 影响 | 概率 | 应对 |
|------|------|------|------|
| 风险1 | 高 | 中 | 措施 |

## 8. Open Items

| 事项 | 影响 | 待确认人 | 截止日期 |
|------|------|----------|----------|
| 事项1 | 中 | 负责人 | 日期 |
```

## Output Validation

> **重要**: 在生成最终输出前，必须完成以下验证步骤

### 验证清单

```markdown
## Self-Validation Report

### V-001: 完整性检查
- [ ] 所有模块都有对应任务
- [ ] 基础设施任务已覆盖
- [ ] 公共模块任务已识别
- [ ] 集成测试任务已规划

### V-002: 粒度检查
- [ ] 90% 任务在 1-3 天范围内
- [ ] 没有超过 5 天的任务（需要拆分）
- [ ] 没有小于 0.5 天的任务（需要合并）

### V-003: 依赖检查
- [ ] 所有依赖关系已标注
- [ ] 没有循环依赖
- [ ] 关键路径已识别
- [ ] 可并行任务已分组

### V-004: 估算检查
- [ ] 每个任务都有估算
- [ ] 估算考虑了风险缓冲
- [ ] 迭代容量平衡合理

### V-005: 可追溯性检查
- [ ] 任务可追溯到模块设计
- [ ] 任务可追溯到技术选型
- [ ] 里程碑与业务目标对齐

### 验证结果
- 验证通过: [是/否]
- 未通过的检查项: [列出]
```

### 验证失败时的处理

```
IF 验证未通过
THEN
  1. 识别未通过的验证项
  2. 修正相应内容
  3. 重新执行验证
  4. 记录仍存在的问题
END
```

## Handover 准备

在完成验证后，生成以下交接信息：

```yaml
handoff_to_development:
  deliverable: "任务分解清单"
  version: "1.0"
  status: "草稿/待评审/已评审"

  summary:
    total_tasks: N           # 任务总数
    total_effort: N           # 总工时(人天)
    sprint_count: N           # Sprint 数量
    critical_path_duration: N # 关键路径工期

  by_priority:
    p0: N                     # P0 任务数
    p1: N                     # P1 任务数
    p2: N                     # P2 任务数

  open_issues:
    count: N
    blocking: [列表]          # 阻塞性问题
    non_blocking: [列表]      # 非阻塞性问题

  recommendations:
    - "建议"
```

## Constraints

1. **语言**：输出使用中文
2. **粒度**：任务粒度控制在 1-3 天
3. **完整性**：所有设计点都有对应任务
4. **可执行**：每个任务有明确验收标准
5. **可追溯**：任务可追溯到需求和设计

## Quality Requirements

| 要求 | 说明 |
|------|------|
| 粒度适中 | 90% 任务在 1-3 天范围 |
| 依赖清晰 | 所有依赖已标注 |
| 优先级合理 | 优先级与价值匹配 |
| 计划可行 | 在资源和时间约束内可行 |

## Task Description

> Describe the specific task for the decompose-task scenario execution.
> AI must understand the context, objectives, and success criteria before proceeding.

## Execution Flow

> Step-by-step execution sequence for decompose-task

### Phase 1: Analysis
- Understand requirements and context
- Identify constraints and dependencies

### Phase 2: Execution
- Perform core decompose-task activities
- Apply best practices and standards

### Phase 3: Validation
- Verify outputs against acceptance criteria
- Ensure completeness and quality
