---
name: analyze-requirement
description: "业务需求分析提示词，用于将原始需求转换为结构化的需求规格说明书"
type: execution
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['prompt', 'ai-execution']
---
# Analyze Requirement

> **版本**: 1.1.0 | **适用阶段**: 需求分析 | **预计工时**: 2-4小时

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




> AI 在执行前必须确认以下变量已填充

| 变量名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|------|
| `project_name` | string | 是 | 项目名称 | "电商订单系统" |
| `raw_requirements` | string | 是 | 原始需求描述 | "用户希望能够..." |
| `stakeholders` | string[] | 否 | 已知干系人 | ["产品经理", "技术负责人"] |
| `constraints` | string[] | 否 | 已知约束 | ["必须在3个月内完成"] |
| `business_background` | string | 否 | 业务背景 | "公司计划拓展新市场" |

## Chain of Thought

```
1. [THINK] 理解业务目标 → 业务目标是否清晰可衡量？
2. [THINK] 识别干系人 → 是否有遗漏的干系人？
3. [THINK] 梳理业务流程 → 流程边界是否清晰？
4. [THINK] 定义功能需求 → 验收标准是否可测试？
5. [THINK] 识别非功能需求 → 是否覆盖性能/安全/可用性？
6. [VALIDATE] 验证输出 → 输出是否符合质量标准？
7. [OUTPUT] 生成交付物 → 需求规格说明书
```

## Error Handling

> AI 在执行过程中遇到以下情况时的处理策略

### 情况 1：需求模糊不清

```
IF 原始需求描述不完整或含糊
THEN
  1. 列出所有可能的理解方式
  2. 为每种理解方式生成假设
  3. 在输出中标注需要确认的问题
  4. 使用 [需要确认] 标签标记
END
```

### 情况 2：干系人信息不足

```
IF 无法识别完整的干系人
THEN
  1. 列出已识别的干系人
  2. 识别可能遗漏的角色类型（决策者、使用者、受影响者）
  3. 在输出中建议需要联系的干系人
END
```

### 情况 3：需求之间冲突

```
IF 发现需求之间存在矛盾
THEN
  1. 列出冲突的需求对
  2. 分析冲突的根本原因
  3. 提出解决建议
  4. 标记为 [冲突待解决]
END
```

### 情况 4：约束不明确

```
IF 约束条件缺失或模糊
THEN
  1. 列出合理的默认假设
  2. 在输出中标注 [基于假设]
  3. 建议在评审时确认
END
```

## Task Steps

### 步骤 1：理解业务目标

**任务**：
- 识别需求背后的业务触发点
- 明确期望达成的业务目标
- 理解需求解决的问题或抓住的机会

**产出**：业务目标清单（3-5 条核心目标）

### 步骤 2：识别干系人

**任务**：
- 识别所有相关干系人
- 了解各干系人的诉求和期望
- 评估干系人的影响力和优先级

**产出**：干系人分析表

### 步骤 3：梳理业务流程

**任务**：
- 识别主要业务流程
- 描述流程的输入、处理、输出
- 标注关键决策点和异常处理

**产出**：业务流程描述

### 步骤 4：定义功能需求

**任务**：
- 使用 "As a [角色]，I want [功能]，so that [价值]" 格式
- 为每个需求定义验收标准
- 标注需求的优先级

**产出**：功能需求清单

### 步骤 5：识别非功能需求

**任务**：
- 识别性能需求（响应时间、吞吐量）
- 识别安全需求（认证、授权、数据保护）
- 识别可用性需求（可用率、恢复时间）
- 识别其他质量属性需求

**产出**：非功能需求清单

### 步骤 6：整理约束与假设

**任务**：
- 整理已知的技术和业务约束
- 列出当前做出的假设
- 识别未解决的问题

**产出**：约束与假设清单



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
## Requirement Analysis Deliverables

### Summary
- Status: [completed | partial | blocked]
- Completion: [percentage]

### Key Outputs
1. **Requirements Specification**: Structured functional and non-functional requirements with acceptance criteria
2. **Stakeholder Analysis**: Impact and interest matrix for all identified stakeholders
3. **Use Case Model**: System use cases and business process descriptions
4. **Traceability Matrix**: Mapping from business objectives to requirements
5. **Constraints & Assumptions**: Documented limitations and assumptions

### Validation Checklist
- [ ] All requirements have unambiguous acceptance criteria
- [ ] Stakeholder sign-off is obtained for scope baseline
- [ ] Traceability matrix covers all business objectives
- [ ] No conflicting or duplicate requirements remain

### Next Steps
- [ ] Review requirements with stakeholders
- [ ] Proceed to system design phase
```


## 1. Document Information
- 项目名称：
- 版本：1.0
- 日期：[当前日期]
- 状态：草稿

## 2. Business Background & Goals

### 2.1 业务背景
[描述业务背景]

### 2.2 业务目标
| 目标 | 描述 | 优先级 |
|------|------|--------|
| 目标1 | 描述 | 高 |
| 目标2 | 描述 | 中 |

## 3. Stakeholder Analysis

### 3.1 干系人列表
| 干系人 | 角色 | 诉求 | 优先级 |
|--------|------|------|--------|
| 干系人1 | 决策者 | 诉求描述 | 高 |

### 3.2 沟通计划
[与各干系人的沟通计划]

## 4. Functional Requirements

### 4.1 需求总览
| ID | 需求名称 | 优先级 | 状态 |
|----|----------|--------|------|
| FR-001 | 需求名称 | P0 | 新增 |

### 4.2 需求详情

#### FR-001: [需求名称]
- **角色**: [As a...]
- **功能**: [I want...]
- **价值**: [so that...]
- **验收标准**:
  1. [标准1]
  2. [标准2]
  3. [标准3]
- **依赖关系**: [如有]

## 5. Non-Functional Requirements

### 5.1 性能需求
| 指标 | 要求 | 说明 |
|------|------|------|
| 响应时间 | < Xms | 在正常负载下 |

### 5.2 安全需求
| 需求 | 要求 | 说明 |
|------|------|------|
| 认证 | 支持X方式认证 | - |

### 5.3 可用性需求
| 指标 | 要求 | 说明 |
|------|------|------|
| 可用率 | 99.9% | - |

## 6. Business Processes

### 6.1 流程A
**流程描述**: [描述]
**参与者**: [参与者列表]
**输入**: [输入]
**输出**: [输出]

**流程步骤**:
1. [步骤1]
2. [步骤2]
3. [步骤3]

**决策点**:
- [决策点1描述] → [不同分支的处理]

**异常处理**:
- [异常1]: [处理方式]
- [异常2]: [处理方式]

## 7. Acceptance Criteria

| 需求ID | 验收标准 | 测试方法 |
|--------|----------|----------|
| FR-001 | 标准1 | 方法 |

## 8. Constraints & Assumptions

### 8.1 约束条件
- [约束1]
- [约束2]

### 8.2 假设
- [假设1]
- [假设2]

### 8.3 未解决问题
- [问题1] - 待确认
- [问题2] - 待确认

## Output Validation

> **重要**: 在生成最终输出前，必须完成以下验证步骤

### 验证清单

```markdown
## Self-Validation Report

### V-001: 完整性检查
- [ ] 所有章节都已填充
- [ ] 业务背景描述清晰
- [ ] 业务目标可衡量
- [ ] 干系人覆盖完整

### V-002: 一致性检查
- [ ] 功能需求与业务目标一致
- [ ] 验收标准与功能需求匹配
- [ ] 约束条件被满足
- [ ] 无矛盾的需求描述

### V-003: 可测试性检查
- [ ] 每个功能需求有验收标准
- [ ] 验收标准可被测试
- [ ] 验收标准足够具体

### V-004: 清晰度检查
- [ ] 术语使用一致
- [ ] 无歧义的描述
- [ ] 业务流程无遗漏

### V-005: 可追溯性检查
- [ ] 需求可追溯到业务目标
- [ ] 验收标准可追溯到需求
- [ ] 未解决问题已记录

### 验证结果
- 验证通过: [是/否]
- 未通过的检查项: [列出]
- 需要确认的问题: [列出]
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



## Handover 准备

在完成验证后，生成以下交接信息：

```yaml
handoff_to_system_design:
  deliverable: "需求规格说明书"
  version: "1.0"
  status: "草稿/待评审/已评审"

  summary:
    total_requirements: N       # 功能需求总数
    total_stakeholders: N       # 干系人总数
    critical_requirements: N     # P0 需求数
    high_requirements: N        # P1 需求数

  open_issues:
    count: N
    blocking: [列表]           # 阻塞性问题
    non_blocking: [列表]       # 非阻塞性问题

  risks:
    - risk: "风险描述"
      impact: "影响"
      mitigation: "缓解措施"

  recommendations:
    - "建议"
```

## 9. Appendix

### 9.1 术语表
| 术语 | 定义 |
|------|------|
| 术语1 | 定义 |

### 9.2 参考文档
- [文档1链接]
- [文档2链接]
```

## Constraints

1. **语言**：输出使用中文
2. **格式**：严格遵循上述输出格式
3. **完整性**：所有章节必须填写，不可留空
4. **可验证性**：每个功能需求必须有明确的验收标准
5. **优先级**：需求必须标注优先级（P0/P1/P2）

## Quality Requirements

| 要求 | 说明 |
|------|------|
| 业务目标清晰 | 每个需求都能追溯到业务目标 |
| 干系人覆盖 | 关键干系人的诉求都有体现 |
| 验收标准明确 | 每个需求都有可测试的验收标准 |
| 无歧义 | 用词准确，逻辑清晰 |

## Examples

### Example

**输入**：
```
业务希望增加一个用户积分功能，用户消费可以获得积分，积分可以兑换礼品。
```

**期望输出**：
```
需求规格说明书（完整填写所有章节）
```

## Tone and Style

- 专业、严谨的表达
- 结构清晰、层次分明
- 重点内容加粗标注
- 使用表格呈现结构化数据

## Task Description

> Describe the specific task for the analyze-requirement scenario execution.
> AI must understand the context, objectives, and success criteria before proceeding.

## Execution Flow

> Step-by-step execution sequence for analyze-requirement

### Phase 1: Analysis
- Understand requirements and context
- Identify constraints and dependencies

### Phase 2: Execution
- Perform core analyze-requirement activities
- Apply best practices and standards

### Phase 3: Validation
- Verify outputs against acceptance criteria
- Ensure completeness and quality
