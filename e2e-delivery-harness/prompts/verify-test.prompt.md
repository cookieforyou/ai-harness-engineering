---
name: verify-test
description: "测试验证提示词，用于设计测试用例并执行测试验证"
type: execution
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['prompt', 'ai-execution']
---
# Verify and Test

> **版本**: 1.1.0 | **适用阶段**: 测试验证 | **预计工时**: 根据测试范围

## Input Variables

## Chain of Thought (思维链)

> **AI 必须按照以下思维链逐步执行**，每完成一步后进行自我验证

```
Step 1: [THINK] 理解测试范围和目标
   ├─ 输入: requirements_spec, test_scope
   ├─ 思考: 需要测试哪些功能？验收标准是什么？
   ├─ 验证: 与需求规格对照，确认覆盖所有验收标准
   └─ 输出: 测试范围定义
   ↓
Step 2: [ANALYZE] 分析测试策略和方法
   ├─ 输入: 测试范围定义, design_documents
   ├─ 思考: 采用什么测试方法？需要哪些测试类型？
   ├─ 验证: 测试策略能发现主要缺陷
   └─ 输出: 测试策略文档
   ↓
Step 3: [DESIGN] 设计测试用例和测试数据
   ├─ 输入: 测试策略文档
   ├─ 思考: 测试用例是否覆盖所有场景？边界条件呢？
   ├─ 验证: 正向、反向、边界全覆盖
   └─ 输出: 测试用例集 + 测试数据
   ↓
Step 4: [IMPLEMENT] 准备测试环境和执行测试
   ├─ 输入: 测试用例集, test_environment
   ├─ 思考: 环境是否就绪？测试数据是否充分？
   ├─ 验证: 环境配置正确，数据准备完成
   └─ 输出: 测试执行结果
   ↓
Step 5: [VERIFY] 分析测试结果和缺陷管理
   ├─ 输入: 测试执行结果
   ├─ 执行: 缺陷识别、分类、报告
   ├─ 验证: 缺陷描述清晰可复现
   └─ 输出: 缺陷报告 + 测试报告
   ↓
Step 6: [HANDOVER] 准备交接给部署或返工阶段
   ├─ 生成: Handover Context
   ├─ 更新: Global Context (质量状态)
   └─ 通知: Deploy Release Agent 或 Implement Feature Agent
```




| 变量名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|------|
| `features_to_test` | string[] | 是 | 待测功能列表 | ["用户登录", "订单创建"] |
| `test_environment` | string | 是 | 测试环境 | "https://test.example.com" |
| `test_credentials` | string | 否 | 测试账号 | (用户名/密码) |
| `coverage_target` | string | 否 | 覆盖率目标 | "80%" |
| `regression_scope` | string[] | 否 | 回归测试范围 | ["登录模块"] |

## Chain of Thought

```
1. [THINK] 分析测试范围 → 哪些功能需要测试？
2. [THINK] 设计测试策略 → 黑盒/白盒/灰盒？
3. [THINK] 编写测试用例 → 覆盖正常/异常/边界？
4. [THINK] 执行测试 → 用例是否通过？
5. [THINK] 跟踪缺陷 → 缺陷是否已修复？
6. [VALIDATE] 评估测试充分性 → 覆盖率是否达标？
7. [OUTPUT] 生成测试报告
```

## Error Handling

### 情况 1：测试环境不可用

```
IF 测试环境无法访问
THEN
  1. 检查环境状态
  2. 联系运维人员
  3. 记录问题
  4. 标记为 [环境阻塞]
END
```

### 情况 2：发现严重缺陷

```
IF 发现严重缺陷（P0/P1）
THEN
  1. 立即记录缺陷
  2. 通知开发负责人
  3. 暂停相关测试
  4. 等待修复后重新测试
END
```

### 情况 3：测试用例失败

```
IF 测试用例执行失败
THEN
  1. 确认测试环境正确
  2. 验证测试数据正确
  3. 确认为代码问题还是测试问题
  4. 记录并创建缺陷
END
```

## Task Steps

### 步骤 1：测试计划

**任务**：
- 确定测试范围和重点
- 选择测试方法
- 规划测试资源
- 制定测试时间表

**产出**：测试计划

### 步骤 2：用例设计

**任务**：
- 设计正常路径用例
- 设计异常路径用例
- 设计边界条件用例
- 设计性能测试用例（如需要）

**产出**：测试用例集

### 步骤 3：环境准备

**任务**：
- 搭建测试环境
- 准备测试数据
- 配置测试工具
- 验证环境就绪

**产出**：就绪的测试环境

### 步骤 4：测试执行

**任务**：
- 执行测试用例
- 记录测试结果
- 记录发现的缺陷
- 更新执行状态

**产出**：测试执行记录

### 步骤 5：缺陷管理

**任务**：
- 提交缺陷报告
- 跟踪缺陷状态
- 验证缺陷修复
- 分析缺陷分布

**产出**：缺陷报告

### 步骤 6：测试报告

**任务**：
- 汇总测试结果
- 评估测试覆盖
- 分析遗留风险
- 给出测试结论

**产出**：测试报告



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
## Test Verification Deliverables

### Summary
- Status: [completed | partial | blocked]
- Completion: [percentage]

### Key Outputs
1. **Test Execution Report**: Pass/fail statistics with evidence
2. **Defect Reports**: Discovered issues with reproduction steps
3. **Coverage Report**: Requirement-to-test traceability matrix
4. **Quality Assessment**: Go/no-go recommendation with rationale
5. **Test Log**: Detailed execution log with timestamps

### Validation Checklist
- [ ] Test pass rate is 90% or higher
- [ ] Requirement traceability coverage is 100%
- [ ] Defect detection rate is 95% or higher
- [ ] All critical defects are documented and triaged

### Next Steps
- [ ] Triage defects with product owner
- [ ] Proceed to release decision
```


## 1. 测试概要

### 1.1 基本信息
| 项目 | 内容 |
|------|------|
| 项目名称 | - |
| 测试阶段 | 功能测试 |
| 测试时间 | 日期 |
| 测试人员 | - |
| 测试环境 | - |

### 1.2 测试范围
- 测试功能：X 项
- 设计用例：X 个
- 执行用例：X 个
- 通过用例：X 个

### 1.3 测试结论
[结论：测试通过/测试不通过]

## 2. 测试结果

### 2.1 测试用例执行情况
| 功能模块 | 用例数 | 通过 | 失败 | 阻塞 | 通过率 |
|----------|--------|------|------|------|--------|
| 模块A | 10 | 9 | 1 | 0 | 90% |

### 2.2 测试结果汇总
| 结果 | 数量 | 占比 |
|------|------|------|
| 通过 | X | XX% |
| 失败 | X | XX% |
| 阻塞 | X | XX% |

## 3. 缺陷统计

### 3.1 缺陷汇总
| 状态 | 数量 |
|------|------|
| 新增 | X |
| 已修复 | X |
| 待验证 | X |
| 遗留 | X |

### 3.2 缺陷分布
| 严重程度 | 数量 | 已修复 | 遗留 |
|----------|------|--------|------|
| 致命 | X | X | X |
| 严重 | X | X | X |
| 中等 | X | X | X |
| 轻微 | X | X | X |

### 3.3 遗留缺陷
| ID | 描述 | 严重程度 | 影响 | 解决方案 | 负责人 |
|----|------|----------|------|----------|--------|
| D001 | 描述 | 中等 | 有限 | 后续修复 | - |

## 4. 测试用例详情

### 4.1 功能模块A

#### TC001: [用例名称]
- **优先级**: P0
- **前置条件**: [条件]
- **测试步骤**:
  1. [步骤1]
  2. [步骤2]
  3. [步骤3]
- **预期结果**: [结果]
- **执行结果**: 通过/失败
- **实际结果**: [如有]
- **缺陷ID**: [如有]

#### TC002: [用例名称]
...

## 5. 风险评估

### 5.1 遗留风险
| 风险 | 影响 | 可能性 | 应对措施 |
|------|------|--------|----------|
| 风险1 | 高 | 中 | 措施 |

### 5.2 测试充分性
- 功能覆盖率：XX%
- 代码覆盖率：XX%

## 6. 测试结论与建议

### 6.1 测试结论
[基于测试结果的综合结论]

### 6.2 发布建议
- [建议1]
- [建议2]

### 6.3 后续工作
- [工作1]
- [工作2]

## Output Validation

> **重要**: 在生成最终输出前，必须完成以下验证步骤

### 验证清单

```markdown
## Self-Validation Report

### V-001: 测试用例完整性
- [ ] 核心功能用例覆盖率 100%
- [ ] 边界条件用例已覆盖
- [ ] 异常场景用例已覆盖
- [ ] 回归测试范围已定义

### V-002: 测试用例质量
- [ ] 每个用例有明确的验收标准
- [ ] 测试步骤清晰可执行
- [ ] 预期结果明确可验证
- [ ] 优先级设置合理

### V-003: 测试环境一致性
- [ ] 测试环境配置已记录
- [ ] 测试数据已准备
- [ ] 与生产环境差异已标注

### V-004: 缺陷报告规范性
- [ ] 缺陷描述清晰可复现
- [ ] 缺陷步骤完整
- [ ] 缺陷等级设置合理
- [ ] 缺陷可追溯到用例

### 验证结果
- 验证通过: [是/否]
- 未通过的检查项: [列出]
```

### 验证失败时的处理

```
IF 验证未通过
THEN
  1. 识别未通过的验证项
  2. 补充缺失的测试用例
  3. 修正不规范的缺陷报告
  4. 重新执行验证
END
```

## Appendix

### A. 测试环境
- 环境：测试环境
- 配置：[配置信息]

### B. 测试数据
- 数据量：X 条
- 数据来源：[来源]
```

## Constraints

1. **语言**：输出使用中文
2. **覆盖**：测试用例需覆盖核心功能
3. **准确**：测试结果必须准确记录
4. **规范**：缺陷报告必须规范完整
5. **可追溯**：缺陷必须可跟踪

## Quality Requirements

| 要求 | 说明 |
|------|------|
| 覆盖完整 | 核心功能都有测试 |
| 结果准确 | 测试结果准确无误 |
| 缺陷清晰 | 缺陷描述清晰可复现 |
| 报告完整 | 报告包含所有必要信息 |



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
handoff_to_deployment:
  deliverable: "测试报告"
  version: "1.0"
  status: "通过/有条件通过/未通过"

  summary:
    total_testcases: N           # 总测试用例数
    passed: N                    # 通过数
    failed: N                    # 失败数
    blocked: N                   # 阻塞数
    pass_rate: percentage        # 通过率

  by_module:
    module_a:
      testcases: N
      passed: N
      failed: N
      pass_rate: percentage

  critical_defects:
    count: N
    open: N
    resolved: N
    blocking_deployment: boolean

  coverage:
    statement: percentage
    branch: percentage
    function: percentage

  recommendations:
    - "建议"

  open_issues:
    count: N
    blocking: [列表]              # 阻塞性问题
    non_blocking: [列表]         # 非阻塞性问题

  sign_off:
    tester: string
    reviewer: string
    date: datetime
```

## Task Description

> Describe the specific task for the verify-test scenario execution.
> AI must understand the context, objectives, and success criteria before proceeding.

## Execution Flow

> Step-by-step execution sequence for verify-test

### Phase 1: Analysis
- Understand requirements and context
- Identify constraints and dependencies

### Phase 2: Execution
- Perform core verify-test activities
- Apply best practices and standards

### Phase 3: Validation
- Verify outputs against acceptance criteria
- Ensure completeness and quality
