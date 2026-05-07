---
name: implement-feature
description: "功能实现提示词，用于完成具体的代码开发任务"
type: execution
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['prompt', 'ai-execution']
---
# Implement Feature

> **版本**: 1.1.0 | **适用阶段**: 开发实现 | **预计工时**: 1-3天/任务

## Input Variables

## Chain of Thought (思维链)

> **AI 必须按照以下思维链逐步执行**，每完成一步后进行自我验证

```
Step 1: [THINK] 理解任务需求和验收标准
   ├─ 输入: task_spec, acceptance_criteria
   ├─ 思考: 需求是否清晰？验收标准是否可测量？
   ├─ 验证: 与需求规格对照，确认无歧义
   └─ 输出: 任务理解备忘录
   ↓
Step 2: [ANALYZE] 分析技术方案和依赖关系
   ├─ 输入: 任务理解备忘录, design_reference
   ├─ 思考: 实现方案是否合理？是否有技术风险？
   ├─ 验证: 符合架构设计，依赖已明确
   └─ 输出: 技术实现方案
   ↓
Step 3: [DESIGN] 设计代码结构和接口
   ├─ 输入: 技术实现方案
   ├─ 思考: 类/函数结构如何设计？接口契约是什么？
   ├─ 验证: 符合SOLID原则，接口清晰
   └─ 输出: 代码结构设计
   ↓
Step 4: [IMPLEMENT] 编写代码和单元测试
   ├─ 输入: 代码结构设计
   ├─ 思考: 代码是否规范？测试是否充分？
   ├─ 验证: 遵循编码规范，测试覆盖核心逻辑
   └─ 输出: 源代码 + 单元测试
   ↓
Step 5: [VERIFY] 自检代码质量和测试覆盖
   ├─ 输入: 源代码, 单元测试
   ├─ 执行: 代码规范检查, 单元测试执行
   ├─ 验证: 无规范违规，测试全部通过
   └─ 输出: 自检报告 + 测试报告
   ↓
Step 6: [HANDOVER] 准备交接给测试验证阶段
   ├─ 生成: Handover Context
   ├─ 更新: Global Context (代码库状态)
   └─ 通知: Verify Test Agent
```




| 变量名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|------|
| `task_id` | string | 是 | 任务ID | "T001" |
| `task_name` | string | 是 | 任务名称 | "用户登录功能" |
| `module` | string | 是 | 所属模块 | "user-service" |
| `priority` | string | 是 | 优先级 | "P0" |
| `acceptance_criteria` | string[] | 是 | 验收标准 | ["支持JWT认证"] |
| `tech_stack` | string[] | 是 | 技术栈 | ["Java", "Spring Boot"] |
| `existing_code` | string | 否 | 现有代码 | (代码路径) |

## Chain of Thought

```
1. [THINK] 理解任务 → 验收标准是否清晰？
2. [THINK] 分析实现方案 → 技术选型是否合理？
3. [THINK] 编写代码 → 是否遵循编码规范？
4. [THINK] 编写测试 → 边界条件是否覆盖？
5. [THINK] 自检代码 → 是否有安全漏洞？
6. [VALIDATE] 验证实现 → 是否满足所有验收标准？
7. [OUTPUT] 生成交付物
```

## Error Handling

### 情况 1：验收标准不清晰

```
IF 验收标准模糊或有歧义
THEN
  1. 列出所有可能的理解
  2. 选择最合理的理解
  3. 在代码注释中说明假设
  4. 标记为 [需确认]
END
```

### 情况 2：实现遇到技术难点

```
IF 遇到无法解决的技术问题
THEN
  1. 分析问题的根本原因
  2. 尝试替代方案
  3. 如仍无法解决，向上升级（联系技术负责人）
  4. 记录问题和尝试的解决方案
END
```

### 情况 3：发现设计问题

```
IF 发现设计与实现不匹配
THEN
  1. 分析差异的影响
  2. 判断是设计问题还是实现问题
  3. 与设计文档对比
  4. 如需修改设计，联系系统设计师
END
```

```

## Task Steps

### 步骤 1：任务理解

**任务**：
- 理解业务需求
- 理解技术要求
- 确认验收标准
- 识别实现难点

**产出**：任务理解备忘录

### 步骤 2：技术方案

**任务**：
- 设计代码结构
- 定义接口和类
- 考虑异常处理
- 编写伪代码（如需要）

**产出**：技术实现方案

### 步骤 3：编码实现

**任务**：
- 按照规范编写代码
- 添加必要的注释
- 确保代码规范
- 保持代码简洁

**产出**：源代码

### 步骤 4：单元测试

**任务**：
- 编写测试用例
- 覆盖正常路径
- 覆盖异常路径
- 执行测试验证

**产出**：测试代码和测试报告

### 步骤 5：代码审查

**任务**：
- 自检代码
- 准备审查材料
- 响应审查意见
- 获得审查通过

**产出**：审查通过的代码

### 步骤 6：文档更新

**任务**：
- 更新接口文档
- 更新代码注释
- 更新变更记录

**产出**：更新后的文档



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
## Feature Implementation Deliverables

### Summary
- Status: [completed | partial | blocked]
- Completion: [percentage]

### Key Outputs
1. **Source Code**: Implemented feature with comments and documentation
2. **Unit Tests**: Test code with coverage report
3. **Integration Tests**: Integration test code (if applicable)
4. **Code Documentation**: Module/function-level documentation
5. **Implementation Notes**: Key decisions and considerations

### Validation Checklist
- [ ] Code coverage meets or exceeds 80%
- [ ] Code review passes with no critical findings
- [ ] Feature is demonstrable and meets acceptance criteria
- [ ] No regression in existing functionality

### Next Steps
- [ ] Submit for code review
- [ ] Merge to main branch after approval
```


## 1. 任务信息
- 任务ID：T001
- 任务名称：[名称]
- 执行人：[姓名]
- 完成时间：[日期]

## 2. 实现摘要

### 2.1 完成情况
| 验收标准 | 完成状态 | 说明 |
|----------|----------|------|
| 标准1 | ✅ 完成 | - |
| 标准2 | ✅ 完成 | - |
| 标准3 | ✅ 完成 | - |

### 2.2 工作量
- 计划工时：2 人天
- 实际工时：1.5 人天
- 偏差：-25%

## 3. 代码变更

### 3.1 新增文件
| 文件 | 说明 |
|------|------|
| src/xxx.ts | 新增功能实现 |

### 3.2 修改文件
| 文件 | 说明 |
|------|------|
| src/yyy.ts | 修改功能实现 |

### 3.3 删除文件
| 文件 | 说明 |
|------|------|
| - | - |

### 3.4 代码统计
- 新增代码：XXX 行
- 修改代码：XXX 行
- 删除代码：XXX 行

## 4. 测试结果

### 4.1 测试用例
| 用例ID | 描述 | 结果 |
|--------|------|------|
| TC001 | 测试描述 | 通过 |

### 4.2 测试覆盖
- 覆盖率：XX%
- 通过率：100%

## 5. 遗留问题

| 问题 | 影响 | 解决方案 | 状态 |
|------|------|----------|------|
| 问题1 | 低 | 后续优化 | 待处理 |

## 6. 后续建议

- [建议1]
- [建议2]
```

## Output Validation

> **重要**: 在提交代码前，必须完成以下验证步骤

### 验证清单

```markdown
## Self-Validation Report

### V-001: 功能验证
- [ ] 所有验收标准都已实现
- [ ] 功能逻辑正确
- [ ] 异常情况已处理

### V-002: 代码质量验证
- [ ] 代码遵循编码规范
- [ ] 命名清晰有意义
- [ ] 函数长度适中
- [ ] 无硬编码值

### V-003: 安全验证
- [ ] 无 SQL 注入风险
- [ ] 无 XSS 风险
- [ ] 敏感数据已加密
- [ ] 权限控制正确

### V-004: 测试验证
- [ ] 单元测试通过
- [ ] 测试覆盖核心逻辑
- [ ] 边界条件已覆盖
- [ ] 测试可重复执行

### V-005: 文档验证
- [ ] 代码注释清晰
- [ ] API 文档已更新
- [ ] README 已更新（如需要）

### 验证结果
- 验证通过: [是/否]
- 未通过的检查项: [列出]
```

### 验证失败时的处理

```
IF 验证未通过
THEN
  1. 修复问题
  2. 重新运行测试
  3. 再次验证
  4. 如无法解决，联系团队负责人
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

```yaml
handoff_to_testing:
  deliverable: "代码实现"
  task_id: "{{task_id}}"
  version: "1.0"

  summary:
    files_changed: N
    lines_added: N
    lines_deleted: N
    test_coverage: "XX%"

  test_results:
    unit_tests_passed: [是/否]
    coverage_meet_target: [是/否]

  open_issues:
    - issue: "问题描述"
      severity: "high/medium/low"
```

## Constraints

1. **语言**：输出使用中文
2. **规范**：遵循团队代码规范
3. **测试**：核心逻辑必须有测试覆盖
4. **文档**：代码变更必须更新相关文档
5. **可追溯**：变更必须可追溯

## Quality Requirements

| 要求 | 说明 |
|------|------|
| 功能正确 | 实现符合需求 |
| 代码规范 | 遵循编码规范 |
| 测试通过 | 单元测试全部通过 |
| 文档同步 | 相关文档已更新 |

## Task Description

> Describe the specific task for the implement-feature scenario execution.
> AI must understand the context, objectives, and success criteria before proceeding.

## Execution Flow

> Step-by-step execution sequence for implement-feature

### Phase 1: Analysis
- Understand requirements and context
- Identify constraints and dependencies

### Phase 2: Execution
- Perform core implement-feature activities
- Apply best practices and standards

### Phase 3: Validation
- Verify outputs against acceptance criteria
- Ensure completeness and quality
