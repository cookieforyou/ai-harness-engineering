---
name: verify-test
description: "测试验证场景，负责设计测试用例、执行测试并报告缺陷"
version: "1.2.0"
type: scenario
category: quality
stage: test-verification
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: [testing, quality, validation, verification]
---
# Verify Test - Testing Scenario

## Purpose

设计并执行全面的测试用例，验证功能实现是否满足需求和验收标准，发现并跟踪缺陷，提供客观的质量评估和发布建议，确保软件交付质量。

### Business Value

- **保证产品质量**: 通过系统化测试发现潜在缺陷，避免生产环境故障和用户投诉
- **降低修复成本**: 早期发现缺陷，修复成本远低于生产环境问题（10-100倍差异）
- **提升用户满意度**: 充分的功能和性能测试确保用户体验流畅，减少负面反馈
- **支持决策制定**: 客观的质量评估和风险分析为发布决策提供数据支持
- **建立质量基线**: 完整的测试记录和覆盖率数据便于后续回归测试和质量趋势分析

## Chain of Thought

> AI 执行时的思维引导，帮助逐步完成测试验证工作

### Think-Aloud Protocol (强制遵循)

```
[THINK] Step 1: 理解测试范围和目标
   ├─ 问：需要测试哪些功能？验收标准是什么？测试重点在哪里？
   ├─ 验证：与需求规格说明书逐条对照，确认覆盖所有验收标准
   └─ 检查：识别核心功能、边界场景、异常处理、性能要求
   ↓
[ANALYZE] Step 2: 分析测试策略和方法
   ├─ 问：采用什么测试方法（黑盒/白盒/灰盒）？需要哪些测试类型？
   ├─ 验证：测试策略能有效发现主要缺陷，平衡覆盖率和效率
   └─ 检查：功能测试、边界测试、异常测试、性能测试、安全测试
   ↓
[DESIGN] Step 3: 设计测试用例和测试数据
   ├─ 问：测试用例是否覆盖所有场景？正向、反向、边界条件呢？
   ├─ 验证：每个验收标准至少有3个测试用例（正常、异常、边界）
   └─ 检查：测试数据充分且多样化，覆盖各种输入组合
   ↓
[IMPLEMENT] Step 4: 准备测试环境和执行测试
   ├─ 问：测试环境是否就绪？测试数据是否充分？自动化脚本可用吗？
   ├─ 验证：环境配置正确，数据准备完成，工具链正常工作
   └─ 检查：按优先级执行测试用例，记录详细结果和截图
   ↓
[VERIFY] Step 5: 分析测试结果和缺陷管理
   ├─ 执行：缺陷识别、分类、优先级评定、报告编写
   ├─ 验证：缺陷描述清晰可复现，包含步骤、预期、实际、截图
   └─ 检查：缺陷跟踪状态准确，回归测试计划明确
   ↓
[HANDOVER] Step 6: 准备交接给部署或返工阶段
   ├─ 生成：Handover Context（含测试统计、缺陷清单、质量评分、发布建议）
   ├─ 更新：Global Context（质量状态、遗留风险、监控建议）
   └─ 通知：Deploy Release Agent（如通过）或 Implement Feature Agent（如有阻塞缺陷）
```

## Decision Checkpoints

| ID | 决策点 | 触发条件 | 决策选项 | 选择标准 | 记录位置 |
|----|--------|----------|----------|----------|----------|
| DC-001 | 测试范围界定 | 开始测试设计前 | 全量测试/回归测试/冒烟测试/探索性测试 | 变更范围、风险评估、时间约束 | 测试计划 |
| DC-002 | 测试方法选择 | 测试策略制定时 | 手动测试/自动化测试/混合测试 | 成本效益、复用频率、稳定性要求 | 测试策略文档 |
| DC-003 | 缺陷优先级判定 | 发现缺陷时 | P0(阻塞)/P1(严重)/P2(一般)/P3(轻微) | 影响范围、严重程度、业务价值、用户影响 | 缺陷报告 |
| DC-004 | 测试充分性判断 | 测试执行中 | 继续测试/停止测试 | 覆盖率达标、边际收益递减、时间约束 | 测试报告 |
| DC-005 | 争议缺陷处理 | 开发不认可缺陷时 | 维持/关闭/延期/需进一步调查 | 是否符合需求和验收标准、用户影响 | 缺陷跟踪系统 |
| DC-006 | 回归测试范围 | 缺陷修复后 | 全量回归/部分回归/选择性回归 | 修改影响范围、风险等级、变更复杂度 | 回归测试计划 |

## Error Handling (错误处理)

> **AI 遇到以下情况时必须按指定流程处理**

### Error Scenario 1: 测试环境问题

**识别信号**: 
- 测试环境无法访问或启动失败
- 依赖服务不可用（数据库、API、第三方服务）
- 测试数据损坏或缺失
- 环境配置错误导致测试无法执行

**处理流程**:
```
IF 测试环境无法正常工作
THEN
  1. 诊断具体问题（网络连通性、服务状态、配置检查、日志分析）
  2. 尝试重启服务或重新配置环境
  3. 检查依赖服务状态（数据库、缓存、消息队列等）
  4. IF 15分钟内无法解决 THEN
       a. 联系运维团队或环境负责人
       b. 尝试使用备用环境（如存在）
       c. 如无可用的备用环境，标记受影响的测试用例为 [阻塞-环境问题]
       d. 升级到项目负责人，说明影响范围和预计延迟
     END
  5. 记录环境问题的详细信息和已尝试的解决方案
  6. 评估对测试进度的影响，调整测试计划
END
```

**降级方案**: 使用Mock或Stub替代不可用的外部服务，标注测试局限性和潜在风险

**升级条件**: 
- P0: 完全无法进行测试，超过1小时未恢复，无替代方案
- P1: 部分功能无法测试，但有替代方案（Mock/Stub），测试覆盖率受影响

**错误日志格式**:
```yaml
error_log:
  error_id: "ERR-{timestamp}-001"
  timestamp: "{{ISO8601}}"
  level: "P0/P1"
  type: "test_environment_issue"
  description: "测试环境问题：{详细描述，包括错误信息、日志片段}"
  affected_services: ["service_1", "service_2"]
  affected_tests: ["TC-001", "TC-002", ...]
  troubleshooting_steps:
    - step_1: "{操作1} - 结果"
    - step_2: "{操作2} - 结果"
  action_taken: "{已采取的行动，如联系运维、切换环境等}"
  result: "resolved/blocked/degraded"
  estimated_delay: "{预计延迟时间}"
  workaround_available: true/false
  workaround_description: "{临时方案描述，如使用Mock}"
```

---

### Error Scenario 2: 测试数据不足

**识别信号**: 
- 缺少必要的测试数据（特定状态、边界值、异常数据）
- 现有数据无法覆盖特定场景（如特殊用户角色、历史数据）
- 数据质量不符合要求（脏数据、不完整、不一致）
- 数据量不足以进行性能测试

**处理流程**:
```
IF 缺少必要的测试数据
THEN
  1. 明确数据需求（字段、范围、数量、分布、特殊条件）
  2. 请求数据准备团队或使用数据生成工具创建数据
  3. 检查是否有可用的数据脱敏的生产数据（需符合隐私政策）
  4. IF 无法获取真实数据 THEN
       a. 创建模拟数据（Mock Data），覆盖关键场景
       b. 使用数据生成工具（如Faker、Mockaroo）生成测试数据
       c. 标注数据限制和对测试结论的影响
       d. 评估是否需要补充真实数据测试
     END
  5. 验证测试数据的完整性和一致性
  6. 评估数据不足对测试充分性的影响，记录风险
END
```

**降级方案**: 使用模拟数据，明确标注测试局限性，承诺在获得真实数据后进行补充测试

**升级条件**: 核心功能测试因数据问题无法进行，且无合适的模拟数据方案

**错误日志格式**:
```yaml
error_log:
  error_id: "ERR-{timestamp}-002"
  timestamp: "{{ISO8601}}"
  level: "P1/P2"
  type: "insufficient_test_data"
  description: "测试数据不足：{详细描述缺少的数据类型和场景}"
  data_requirements:
    - requirement_1: "{数据需求1}"
    - requirement_2: "{数据需求2}"
  available_data: "{当前可用数据描述}"
  gap_analysis: "{数据缺口分析}"
  action_taken: "{已采取的行动，如请求数据、生成Mock数据等}"
  result: "resolved/partial/blocked"
  workaround_available: true/false
  workaround_description: "{临时方案描述}"
  impact_on_testing: "{对测试的影响评估}"
```

---

### Error Scenario 3: 缺陷争议

**识别信号**: 
- 开发人员认为不是缺陷（"按设计实现"、"需求未明确"）
- 产品经理认为符合预期行为
- 团队成员对验收标准理解不一致
- 缺陷优先级评定存在分歧

**处理流程**:
```
IF 发现缺陷存在争议
THEN
  1. 引用需求规格说明书和验收标准作为依据
  2. 提供缺陷的详细复现步骤和影响分析
  3. 组织讨论会议（测试、开发、产品三方参与）
  4. 澄清验收标准的真实意图和业务背景
  5. IF 仍无法达成共识 THEN
       a. 升级到产品经理或技术负责人裁决
       b. 记录讨论过程、各方观点和论据
       c. 等待最终决定，期间标记为 [待确认]
     ELSE
       a. 根据共识更新缺陷状态（保持/关闭/调整优先级）
       b. 如需，更新验收标准文档以消除歧义
       c. 记录决策理由供后续参考
     END
  6. 将争议案例加入团队知识库，避免类似问题
END
```

**降级方案**: 暂时标记为"待确认"，继续测试其他功能，避免阻塞整体进度

**升级条件**: 超过1轮讨论仍无法达成共识，或缺陷影响核心功能发布

**错误日志格式**:
```yaml
error_log:
  error_id: "ERR-{timestamp}-003"
  timestamp: "{{ISO8601}}"
  level: "P2"
  type: "defect_dispute"
  defect_id: "DEFECT-XXX"
  description: "缺陷争议：{争议焦点描述}"
  viewpoints:
    tester: "{测试方观点}"
    developer: "{开发方观点}"
    product_owner: "{产品方观点（如有）}"
  evidence:
    - requirement_reference: "{相关需求条款}"
    - acceptance_criteria: "{相关验收标准}"
    - user_impact: "{用户影响分析}"
  discussion_summary: "{讨论要点总结}"
  action_taken: "已组织讨论/已升级裁决"
  result: "resolved/pending/escalated"
  final_decision: "{最终决定（如已有）}"
  decision_rationale: "{决策理由}"
```

---

### Error Scenario 4: 测试时间不足

**识别信号**: 
- 剩余时间不足以完成所有计划的测试用例
- 临近发布截止时间，测试进度滞后
- 发现大量缺陷需要回归测试，时间压力增大
- 测试环境不稳定导致执行效率降低

**处理流程**:
```
IF 测试时间不足
THEN
  1. 重新评估测试用例优先级（P0核心/P1重要/P2一般/P3可选）
  2. 优先执行P0（关键路径、核心功能）测试用例
  3. 基于风险评估选择性地跳过或简化P2/P3测试
  4. IF 时间仍然不足 THEN
       a. 与项目经理沟通，评估调整发布计划或增加测试资源
       b. 采用基于风险的测试策略（Risk-Based Testing）
       c. 明确标注未测试区域、覆盖缺口和潜在风险
       d. 提出分阶段发布建议（先发布核心功能）
     END
  5. 记录时间限制对测试充分性的影响
  6. 在测试报告中明确说明测试局限性和残留风险
  7. 制定后续补充测试计划（下个迭代或专门测试周期）
END
```

**降级方案**: 基于风险的测试策略，优先保证核心功能和高风险区域的质量，接受一定的测试覆盖率妥协

**升级条件**: 关键路径（P0）测试无法完成，或高危区域未测试

**错误日志格式**:
```yaml
error_log:
  error_id: "ERR-{timestamp}-004"
  timestamp: "{{ISO8601}}"
  level: "P2"
  type: "insufficient_test_time"
  description: "测试时间不足：{详细描述时间约束和影响}"
  planned_test_cases: {number}
  executed_test_cases: {number}
  skipped_test_cases: {number}
  coverage_gap:
    functional_areas: ["未测试功能模块列表"]
    risk_level: "high/medium/low"
  action_taken: "已调整测试优先级/已申请延期/已采用风险基测试"
  result: "partial_completion"
  residual_risks:
    - risk_1: "{风险1描述} - 可能性: {高/中/低} - 影响: {高/中/低}"
    - risk_2: "{风险2描述} - 可能性: {高/中/低} - 影响: {高/中/低}"
  remediation_plan:
    owner: "{责任人}"
    target_date: "{补充测试目标日期}"
    approach: "{补充测试方案}"
  release_recommendation: "approved_with_risks/conditional_approval/not_recommended"
```

## Quality Metrics

### Key Performance Indicators (KPIs)

| KPI ID | 指标名称 | 目标值 | 计算公式 | 验证方法 | 权重 |
|--------|----------|--------|----------|----------|------|
| KPI-001 | TEST-PASS-RATE | ≥90% | (通过测试数/总测试数) × 100% | 测试执行报告统计 | 30% |
| KPI-002 | DEFECT-DETECTION | ≥95% | (发现的缺陷数/实际缺陷总数估算) × 100% | 事后回顾分析、生产问题回溯 | 25% |
| KPI-003 | REQ-TRACE | 100% | (有测试覆盖的需求数/总需求数) × 100% | 需求-测试映射表检查 | 25% |
| KPI-004 | TEST-COVERAGE | ≥85% | (被测试覆盖的代码行数/总代码行数) × 100% | 代码覆盖率工具（JaCoCo/Istanbul等） | 20% |

**综合评分计算**: 
```
Quality Score = (KPI-001 × 0.30) + (KPI-002 × 0.25) + (KPI-003 × 0.25) + (KPI-004 × 0.20)
合格: ≥70分 | 优秀: ≥85分 | 卓越: ≥95分
```

**KPI详细说明**:
- **TEST-PASS-RATE**: 反映代码质量和测试用例设计的合理性，过低可能表示代码质量问题或测试用例过于严格
- **DEFECT-DETECTION**: 衡量测试有效性，通过生产环境问题回溯评估漏测率
- **REQ-TRACE**: 确保所有需求都有对应的测试验证，避免遗漏
- **TEST-COVERAGE**: 代码级覆盖率，补充功能测试的不足，发现未测试的代码路径

### Validation Checklist (验证清单)

**完整性验证 (Completeness)**:
- [ ] 所有功能需求都有对应测试用例（正向、反向、边界）
- [ ] 所有非功能需求都已验证（性能、安全、可用性）
- [ ] 边界条件和异常场景已充分覆盖
- [ ] 测试数据充分且多样化，覆盖各种输入组合
- [ ] 测试报告包含所有必需信息（执行统计、缺陷清单、质量评估）
- [ ] 需求-测试追溯矩阵完整，无遗漏

**一致性验证 (Consistency)**:
- [ ] 测试用例与需求规格和验收标准一致
- [ ] 测试结果与预期行为对比明确，无歧义
- [ ] 缺陷描述标准化，包含复现步骤、预期结果、实际结果
- [ ] 术语使用统一，符合项目词汇表
- [ ] 缺陷优先级评定标准一致，无主观偏差

**准确性验证 (Accuracy)**:
- [ ] 测试结果准确无误，无假阳性或假阴性
- [ ] 缺陷定位精确，包含足够的调试信息（日志、截图、堆栈跟踪）
- [ ] 测试数据统计正确，通过率、覆盖率计算无误
- [ ] 缺陷严重程度评定合理，符合影响评估标准
- [ ] 测试环境配置记录准确，便于问题复现

**可执行性验证 (Executability)**:
- [ ] 测试用例可重复执行，结果确定（无flaky tests）
- [ ] 测试环境稳定可靠，无明显波动
- [ ] 自动化测试脚本运行正常，无间歇性失败
- [ ] 测试数据可重置，支持多次执行
- [ ] 测试步骤清晰，其他测试人员可按步骤复现

**规范性验证 (Compliance)**:
- [ ] 遵循测试规范和流程（测试计划→用例设计→执行→报告）
- [ ] 缺陷报告格式标准，包含所有必需字段
- [ ] 测试文档完整归档，便于后续查阅和审计
- [ ] 符合行业测试标准（如ISTQB最佳实践）
- [ ] 测试数据和结果符合隐私和合规要求（GDPR等）

## Handover Criteria

### 准出条件

```
✅ 测试用例设计完成并通过评审（覆盖率≥90%）
✅ 测试环境已验证可用，依赖服务正常
✅ 计划的测试用例已全部执行（执行率≥95%）
✅ 发现的缺陷已记录、分类并评定优先级
✅ P0/P1缺陷已修复并通过回归测试
✅ 测试报告已编写完成，包含质量评估和发布建议
✅ 需求-测试追溯矩阵完整（100%覆盖）
✅ 代码覆盖率达标（≥85%）
✅ Handover Context 已生成，所有必需字段完整
✅ 质量评分 ≥70分（基于KPIs计算）
```

### 交付物清单

| 交付物 | 格式 | 位置 | 版本 | 说明 |
|--------|------|------|------|------|
| 测试用例集 | Excel/TestLink/Markdown | docs/test-cases.xlsx | v1.0.0 | 完整测试用例，含前置条件、步骤、预期结果 |
| 测试执行报告 | HTML/PDF | reports/test-execution-report.html | - | 执行结果汇总，含通过率、失败用例详情 |
| 缺陷报告 | JIRA导出/Excel | defects/defect-list.xlsx | - | 缺陷清单，含状态、优先级、修复情况 |
| 代码覆盖率报告 | HTML | reports/coverage/index.html | - | 详细的代码覆盖率分析 |
| 测试总结报告 | Markdown | docs/test-summary.md | v1.0.0 | 质量评估、风险分析、发布建议 |
| 需求-测试追溯矩阵 | Excel/Markdown | docs/traceability-matrix.xlsx | v1.0.0 | 需求到测试用例的映射关系 |
| 自动化测试脚本 | Code repository | tests/automation/ | - | 可重复执行的自动化测试脚本 |

### Handover Context Template

```yaml
handover:
  header:
    from_stage: "testing"
    to_stage: "deployment" or "development"
    handover_id: "HO-{{timestamp}}-{{sequence}}"
    timestamp: "{{ISO8601}}"
    prepared_by: "{{agent.name}}"
    
  summary:
    status: "passed/failed/partial/conditional_pass"
    completion_percentage: {{0-100}}
    quality_score: {{0-100}}
    total_test_cases: {{number}}
    passed: {{number}}
    failed: {{number}}
    blocked: {{number}}
    skipped: {{number}}
    pass_rate: {{percentage}}%
    execution_rate: {{percentage}}%
    
  artifacts:
    delivered:
      - name: "Test Cases"
        path: "docs/test-cases.xlsx"
        version: "1.0.0"
        checksum: "{{SHA256}}"
        test_case_count: {{number}}
      - name: "Test Execution Report"
        path: "reports/test-execution-report.html"
        version: "1.0.0"
      - name: "Defect List"
        path: "defects/defect-list.xlsx"
        version: "1.0.0"
        defect_count: {{number}}
      - name: "Test Summary Report"
        path: "docs/test-summary.md"
        version: "1.0.0"
      - name: "Coverage Report"
        path: "reports/coverage/index.html"
        version: "1.0.0"
      - name: "Traceability Matrix"
        path: "docs/traceability-matrix.xlsx"
        version: "1.0.0"
      
  decisions:
    - id: "DC-003"
      description: "缺陷优先级判定"
      rationale: "基于影响范围、严重程度、业务价值评定P0-P3"
      criteria_used: "P0: 阻塞核心功能; P1: 严重影响用户体验; P2: 一般功能问题; P3: 轻微UI/文案问题"
      
  open_issues:
    blocking:
      - id: "DEFECT-001"
        description: "核心功能X存在严重缺陷，导致系统崩溃"
        severity: "P0"
        status: "open"
        impact: "阻塞发布，必须修复"
        assigned_to: "{{developer_name}}"
    non_blocking:
      - id: "DEFECT-002"
        description: "UI显示小问题，不影响功能"
        severity: "P3"
        status: "accepted"
        impact: "可延期修复，不影响发布"
        planned_fix: "下个迭代"
        
  risks:
    - id: "RISK-001"
      description: "部分边缘场景未充分测试（时间限制）"
      probability: "low"
      impact: "medium"
      affected_areas: ["功能A的边缘情况", "功能B的并发场景"]
      mitigation: "生产环境密切监控，承诺下个迭代补充测试"
      contingency_plan: "如出现问题，立即回滚并修复"
      
  recommendations:
    - "建议先修复P0和P1级别缺陷再发布"
    - "重点关注性能测试中发现的瓶颈（API X响应时间超标）"
    - "建议在灰度发布阶段重点监控X功能的用户反馈"
    - "建议在下个迭代补充边缘场景测试（见RISK-001）"
    - "建议加强自动化测试覆盖，减少手动测试工作量"
    
  quality_metrics:
    kpi_results:
      - kpi_id: "KPI-001"
        name: "TEST-PASS-RATE"
        value: 92
        target: 90
        unit: "%"
        status: "pass"
      - kpi_id: "KPI-002"
        name: "DEFECT-DETECTION"
        value: 96
        target: 95
        unit: "%"
        status: "pass"
        estimation_method: "基于历史数据和同行评审"
      - kpi_id: "KPI-003"
        name: "REQ-TRACE"
        value: 100
        target: 100
        unit: "%"
        status: "pass"
      - kpi_id: "KPI-004"
        name: "TEST-COVERAGE"
        value: 87
        target: 85
        unit: "%"
        status: "pass"
        breakdown:
          line_coverage: 87%
          branch_coverage: 82%
          function_coverage: 91%
    overall_score: 93
    grade: "excellent"
    recommendation: "approved_for_release_with_conditions"
    conditions:
      - "修复所有P0/P1缺陷"
      - "监控生产环境X功能的表现"
      - "下个迭代补充边缘场景测试"
      
  next_steps:
    if_passed:
      - "准备部署包和发布说明"
      - "执行预发布环境验证"
      - "安排灰度发布计划"
      - "设置生产环境监控告警"
    if_failed:
      - "开发团队修复P0/P1缺陷"
      - "执行回归测试验证修复"
      - "重新评估发布计划和时间表"
      - "必要时调整需求范围或延期发布"
```

## Related Assets (关联资产)

| Asset Type | Path | Description |
|------------|------|-------------|
| Agent | `../../agents/verify-test.agent.md` | 测试验证Agent角色定义 |
| Prompt | `../../prompts/verify-test.prompt.md` | 测试验证提示词模板 |
| Skill | `../../skills/verify-test/SKILL.md` | 测试验证技能包 |
| Instruction | `../../instructions/verify-test.instructions.md` | 测试验证技术指令 |

## Related Resources (相关资源)

- **Standards**: 
  - [Testing Best Practices](../../standards/testing-best-practices.md) - 测试最佳实践指南
  - [Defect Classification](../../standards/defect-classification.md) - 缺陷分类和优先级标准
  - [Test Coverage Guidelines](../../standards/test-coverage-guidelines.md) - 测试覆盖率指南
  - [Test Data Management](../../standards/test-data-management.md) - 测试数据管理规范
- **Templates**: 
  - [Test Case Template](../../templates/test-case.template.md) - 测试用例模板
  - [Defect Report Template](../../templates/defect-report.template.md) - 缺陷报告模板
  - [Test Plan Template](../../templates/test-plan.template.md) - 测试计划模板
  - [Test Report Template](../../templates/test-report.template.md) - 测试报告模板
- **Evaluations**: 
  - [Test Quality Checklist](../../evaluations/test-quality-checklist.md) - 测试质量检查清单
  - [Defect Analysis Report](../../evaluations/defect-analysis.md) - 缺陷分析报告模板
  - [Coverage Analysis](../../evaluations/coverage-analysis.md) - 覆盖率分析指南

## Prerequisites

### 必需前置条件

1. ✅ 功能开发已完成 (implement-feature 场景输出)
2. ✅ 测试环境已部署并验证可用
3. ✅ 测试数据已准备（或Mock方案就绪）
4. ✅ 需求规格和验收标准明确
5. ✅ 测试工具和框架已就绪
6. ✅ 代码已合并到测试分支

### 期望输入

| Input Variable | Type | Required | Default | Description | Validation |
|----------------|------|----------|---------|-------------|------------|
| `test_scope` | string | true | - | 测试范围描述 | 非空字符串，明确测试边界 |
| `requirements_spec` | markdown | true | - | 需求规格说明书 | 包含完整的验收标准 |
| `test_environment` | object | true | - | 测试环境信息 | URL、账号、配置、依赖服务状态 |
| `design_documents` | array | false | [] | 相关设计文档 | 文件路径列表，用于理解实现细节 |
| `test_data` | object | false | {} | 测试数据集 | 结构化数据，或数据生成方案 |
| `previous_test_results` | array | false | [] | 历史测试结果 | 用于回归测试对比 |
| `automation_scripts` | array | false | [] | 自动化测试脚本 | 可用的自动化测试集合 |
