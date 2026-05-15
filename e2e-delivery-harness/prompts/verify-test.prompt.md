---
name: verify-test
description: "测试验证提示词，用于设计测试用例并执行测试验证"
type: prompt
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: [prompt, testing, quality]
---
# Verify Test Prompt

## Purpose

本提示词指导AI执行测试验证任务，设计全面的测试用例，执行系统化的测试流程，发现并跟踪缺陷，提供客观的质量评估和发布建议，确保软件交付质量。

### Key Objectives

- **全面覆盖测试**: 确保所有功能需求和非功能需求都有对应的测试用例（正向、反向、边界）
- **系统化测试执行**: 按优先级执行测试用例，记录详细结果和证据（截图、日志）
- **缺陷管理**: 准确识别、分类和报告缺陷，确保描述清晰可复现
- **质量评估**: 基于KPIs计算质量评分，提供客观的发布建议
- **完整交接准备**: 生成Handover Context，便于部署或返工阶段顺利接手

## Input Variables

| Variable | Type | Required | Description | Validation |
|----------|------|----------|-------------|------------|
| `test_scope` | string | true | 测试范围描述，明确测试边界和重点 | 非空字符串，包含功能模块列表 |
| `requirements_spec` | markdown | true | 需求规格说明书，包含验收标准 | 必须有明确的Given-When-Then格式验收标准 |
| `test_environment` | object | true | 测试环境配置信息 | 包含URL、账号、依赖服务状态 |
| `design_documents` | array | false | 相关设计文档路径列表 | 用于理解实现细节和技术约束 |
| `test_data` | object | false | 测试数据集或数据生成方案 | 结构化数据，覆盖正常/异常/边界场景 |
| `previous_test_results` | array | false | 历史测试结果（回归测试用） | 包含用例ID、状态、缺陷ID |
| `automation_scripts` | array | false | 可用的自动化测试脚本列表 | 脚本路径和执行说明 |
| `coverage_target` | number | false | 代码覆盖率目标值（默认85%） | 范围：0-100，推荐≥85 |

## Chain of Thought (思维链)

> **AI 必须按照以下思维链逐步执行**，每完成一步后进行自我验证

```
[THINK] Step 1: 理解测试范围和目标
   ├─ 输入: requirements_spec, test_scope
   ├─ 思考: 需要测试哪些功能？验收标准是什么？测试重点在哪里？
   ├─ 验证: 与需求规格对照，确认覆盖所有验收标准
   └─ 输出: 测试范围定义（含核心功能、边界场景、异常处理清单）
   ↓
[ANALYZE] Step 2: 分析测试策略和方法
   ├─ 输入: 测试范围定义, design_documents
   ├─ 思考: 采用什么测试方法（黑盒/白盒/灰盒）？需要哪些测试类型？
   ├─ 验证: 测试策略能有效发现主要缺陷，平衡覆盖率和效率
   └─ 输出: 测试策略文档（含测试类型、方法选择、资源安排）
   ↓
[DESIGN] Step 3: 设计测试用例和测试数据
   ├─ 输入: 测试策略文档, requirements_spec
   ├─ 思考: 测试用例是否覆盖所有场景？正向、反向、边界条件呢？
   ├─ 验证: 每个验收标准至少有3个测试用例（正常、异常、边界）
   └─ 输出: 测试用例集（含前置条件、步骤、预期结果、优先级）
   ↓
[IMPLEMENT] Step 4: 准备测试环境和执行测试
   ├─ 输入: 测试用例集, test_environment, test_data
   ├─ 思考: 环境是否就绪？测试数据是否充分？自动化脚本可用吗？
   ├─ 验证: 环境配置正确，数据准备完成，工具链正常工作
   └─ 输出: 测试执行结果（含通过/失败/阻塞状态、截图、日志）
   ↓
[VERIFY] Step 5: 分析测试结果和缺陷管理
   ├─ 输入: 测试执行结果
   ├─ 执行: 缺陷识别、分类（P0-P3）、优先级评定、报告编写
   ├─ 验证: 缺陷描述清晰可复现，包含步骤、预期、实际、截图
   └─ 输出: 缺陷报告 + 测试执行统计（通过率、覆盖率）
   ↓
[HANDOVER] Step 6: 准备交接给部署或返工阶段
   ├─ 生成: Handover Context（含测试统计、缺陷清单、质量评分、发布建议）
   ├─ 更新: Global Context（质量状态、遗留风险、监控建议）
   └─ 通知: Deploy Release Agent（如通过）或 Implement Feature Agent（如有阻塞缺陷）
```

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
       c. 标记受影响的测试用例为 [阻塞-环境问题]
       d. 升级到项目负责人，说明影响范围和预计延迟
     END
  5. 记录环境问题的详细信息和已尝试的解决方案
  6. 评估对测试进度的影响，调整测试计划
END
```

**降级方案**: 使用Mock或Stub替代不可用的外部服务，标注测试局限性和潜在风险

**升级条件**: P0: 完全无法进行测试，超过1小时未恢复；P1: 部分功能无法测试但有替代方案

---

### Error Scenario 2: 测试数据不足

**识别信号**: 
- 缺少必要的测试数据（特定状态、边界值、异常数据）
- 现有数据无法覆盖特定场景（如特殊用户角色、历史数据）
- 数据质量不符合要求（脏数据、不完整、不一致）

**处理流程**:
```
IF 缺少必要的测试数据
THEN
  1. 明确数据需求（字段、范围、数量、分布、特殊条件）
  2. 请求数据准备团队或使用数据生成工具创建数据
  3. 检查是否有可用的脱敏生产数据（需符合隐私政策）
  4. IF 无法获取真实数据 THEN
       a. 创建模拟数据（Mock Data），覆盖关键场景
       b. 使用数据生成工具（如Faker、Mockaroo）生成测试数据
       c. 标注数据限制和对测试结论的影响
     END
  5. 验证测试数据的完整性和一致性
  6. 评估数据不足对测试充分性的影响，记录风险
END
```

**降级方案**: 使用模拟数据，明确标注测试局限性，承诺在获得真实数据后进行补充测试

**升级条件**: 核心功能测试因数据问题无法进行，且无合适的模拟数据方案

---

### Error Scenario 3: 缺陷争议

**识别信号**: 
- 开发人员认为不是缺陷（"按设计实现"、"需求未明确"）
- 产品经理认为符合预期行为
- 团队成员对验收标准理解不一致

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
     END
  6. 将争议案例加入团队知识库，避免类似问题
END
```

**降级方案**: 暂时标记为"待确认"，继续测试其他功能，避免阻塞整体进度

**升级条件**: 超过1轮讨论仍无法达成共识，或缺陷影响核心功能发布

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
- [ ] 优先级设置合理（P0-P3）

### V-003: 测试环境一致性
- [ ] 测试环境配置已记录
- [ ] 测试数据已准备
- [ ] 与生产环境差异已标注

### V-004: 缺陷报告规范性
- [ ] 缺陷描述清晰可复现
- [ ] 缺陷步骤完整（至少3步）
- [ ] 缺陷等级设置合理
- [ ] 缺陷可追溯到用例

### V-005: 质量指标达标
- [ ] TEST-PASS-RATE ≥90%
- [ ] REQ-TRACE = 100%
- [ ] TEST-COVERAGE ≥85%
- [ ] 质量评分 ≥70分

### 验证结果
- 验证通过: [是/否]
- 未通过的检查项: [列出]
- 补救措施: [如有]
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

## Output Format

```markdown
## Test Verification Deliverables

### Summary
- Status: [passed/failed/partial/conditional_pass]
- Completion: [percentage]%
- Quality Score: [score]/100

### Key Outputs
1. **Test Execution Report**: Pass/fail statistics with evidence
   - Total Test Cases: {number}
   - Passed: {number} ({percentage}%)
   - Failed: {number} ({percentage}%)
   - Blocked: {number} ({percentage}%)
   - Skipped: {number} ({percentage}%)

2. **Defect Reports**: Discovered issues with reproduction steps
   - Total Defects: {number}
   - P0 (Critical): {number}
   - P1 (Major): {number}
   - P2 (Minor): {number}
   - P3 (Trivial): {number}
   - Open Defects: {number}
   - Resolved Defects: {number}

3. **Coverage Report**: Requirement-to-test traceability matrix
   - Requirements Covered: {number}/{total} (100%)
   - Code Coverage: {percentage}% (target: 85%)
   - Branch Coverage: {percentage}%
   - Function Coverage: {percentage}%

4. **Quality Assessment**: Go/no-go recommendation with rationale
   - Overall Grade: [excellent/good/fair/poor]
   - Recommendation: [approved_for_release/approved_with_conditions/not_recommended]
   - Conditions: [list if applicable]

5. **Test Log**: Detailed execution log with timestamps
   - Environment: {URL, version, config}
   - Test Data: {description, source}
   - Execution Time: {start_time} to {end_time}
   - Tester: {agent.name}

### Validation Checklist
- [ ] Test pass rate is 90% or higher
- [ ] Requirement traceability coverage is 100%
- [ ] Code coverage is 85% or higher
- [ ] All critical defects are documented and triaged
- [ ] Handover Context is complete

### Next Steps
- [ ] Triage defects with product owner
- [ ] Fix P0/P1 defects (if any)
- [ ] Execute regression tests after fixes
- [ ] Proceed to release decision
```

## Handover Context Template

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
| Scenario | `../../scenarios/verify-test/SCENARIO.md` | 测试验证场景定义 |
| Agent | `../../agents/verify-test.agent.md` | 测试验证Agent角色定义 |
| Skill | `../../skills/verify-test/SKILL.md` | 测试验证技能包 |
| Instruction | `../../instructions/verify-test.instructions.md` | 测试验证技术指令 |

## Related Resources (相关资源)

- **Standards**: 
  - [Testing Best Practices](../standards/testing-best-practices.md) - 测试最佳实践指南
  - [Defect Classification](../standards/defect-classification.md) - 缺陷分类和优先级标准
  - [Test Coverage Guidelines](../standards/test-coverage-guidelines.md) - 测试覆盖率指南
- **Templates**: 
  - [Test Case Template](../templates/test-case.template.md) - 测试用例模板
  - [Defect Report Template](../templates/defect-report.template.md) - 缺陷报告模板
  - [Test Report Template](../templates/test-report.template.md) - 测试报告模板
- **Evaluations**: 
  - [Test Quality Checklist](../evaluations/test-quality-checklist.md) - 测试质量检查清单
  - [Coverage Analysis](../evaluations/coverage-analysis.md) - 覆盖率分析指南
