---
name: implement-feature
description: "功能实现提示词，用于完成具体的代码开发任务"
type: prompt
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: [prompt, development, coding]
---
# Implement Feature Prompt

## Purpose

本提示词指导AI执行功能实现任务，按照任务规格完成高质量的代码开发、单元测试和文档更新，确保代码符合团队规范和最佳实践。

### Key Objectives

- **准确理解需求**: 深入理解任务规格和验收标准，确保实现符合预期
- **高质量代码实现**: 遵循编码规范和SOLID原则，编写清晰、可维护的代码
- **充分测试覆盖**: 编写全面的单元测试，核心逻辑100%覆盖，整体≥80%
- **完整文档同步**: 及时更新API文档、代码注释和变更记录
- **规范交接准备**: 生成完整的Handover Context，便于测试验证阶段顺利接手

## Input Variables (变量定义)

> **AI 在执行前必须确认以下变量已填充**，如未填充则请求用户提供

| Variable | Type | Required | Default | Description | Validation |
|----------|------|----------|---------|-------------|------------|
| `task_id` | string | true | - | 任务唯一标识符 | 非空字符串，格式：TASK-XXX |
| `task_name` | string | true | - | 任务名称 | 非空字符串，长度5-100字符 |
| `acceptance_criteria` | array | true | - | 验收标准列表 | 至少1个标准，每个标准符合SMART原则 |
| `tech_stack` | array | true | - | 技术栈列表 | 有效的技术名称（Java/Python/JavaScript等） |
| `task_spec` | markdown | true | - | 详细任务规格说明 | 长度 > 100字符，包含用户故事和AC |
| `design_reference` | string | false | "" | 相关设计文档链接或内容 | 有效的文件路径或URL |
| `codebase_context` | string | false | "" | 代码库上下文信息 | 相关模块、依赖、现有代码说明 |
| `coding_standards` | string | false | "team_default" | 编码规范文档 | 有效的规范文档路径或内容 |
| `test_requirements` | object | false | {coverage: 80} | 测试要求 | 包含覆盖率目标和测试类型 |

### Test Requirements Structure Definition

```yaml
test_requirements:
  coverage_target: number      # 覆盖率目标（百分比），默认80
  test_types: array            # 测试类型列表
    - unit                     # 单元测试（必需）
    - integration              # 集成测试（可选）
    - e2e                      # 端到端测试（可选）
  critical_logic_coverage: number  # 核心逻辑覆盖率目标，默认100
  performance_testing: boolean     # 是否需要性能测试，默认false
```

### 示例: 变量的正确格式

```yaml
# 示例: 完整的功能实现输入
task_id: "TASK-001"
task_name: "用户登录功能实现"

acceptance_criteria:
  - "用户可以使用邮箱和密码登录系统"
  - "登录成功后返回JWT token，有效期24小时"
  - "连续5次登录失败后锁定账户30分钟"
  - "响应时间在正常负载下 < 500ms"

tech_stack:
  - "Java 17"
  - "Spring Boot 3.0"
  - "Spring Security"
  - "JWT (io.jsonwebtoken)"
  - "JUnit 5"
  - "Mockito"

task_spec: |
  ## User Story
  As a 注册用户
  I want 能够通过邮箱和密码登录系统
  So that 我可以访问我的个人账户和功能
  
  ## Technical Requirements
  - 使用BCrypt加密存储密码
  - 实现JWT token生成和验证
  - 添加登录失败次数限制和账户锁定机制
  - 记录登录日志（成功/失败）
  
  ## API Endpoint
  POST /api/v1/auth/login
  Request Body: { email: string, password: string }
  Response: { token: string, expires_in: number, user: UserInfo }

design_reference: "docs/design/authentication-design.md"

codebase_context: |
  - 现有用户模块位于 src/main/java/com/example/user/
  - 已有User实体类和UserRepository
  - Spring Security已配置，需要添加自定义AuthenticationProvider
  - 使用Redis存储登录失败次数和账户锁定状态

coding_standards: "docs/coding-standards.md"

test_requirements:
  coverage_target: 85
  test_types:
    - unit
    - integration
  critical_logic_coverage: 100
  performance_testing: false
```

## Chain of Thought (思维链)

> **AI 必须按照以下思维链逐步执行**，每完成一步后进行自我验证

```
[THINK] Step 1: 理解任务需求和验收标准
   ├─ 输入: task_spec, acceptance_criteria, design_reference
   ├─ 思考: 需求是否清晰？验收标准是否符合SMART原则？是否有歧义？
   ├─ 验证: 与任务规格对照，逐条确认无遗漏和误解
   └─ 输出: 任务理解备忘录（包含需求摘要、关键点、疑问清单）
   ↓
[ANALYZE] Step 2: 分析技术方案和依赖关系
   ├─ 输入: 任务理解备忘录, codebase_context, tech_stack
   ├─ 思考: 实现方案是否符合架构设计？是否有技术风险？依赖是否明确？
   ├─ 验证: 参考系统设计文档，确认技术选型合理，识别所有外部依赖
   └─ 输出: 技术实现方案（包含类图、时序图、依赖清单、风险评估）
   ↓
[DESIGN] Step 3: 设计代码结构和接口
   ├─ 输入: 技术实现方案, coding_standards
   ├─ 思考: 类/函数结构如何设计？接口契约是什么？是否符合SOLID原则？
   ├─ 验证: 代码结构清晰，职责单一，接口定义明确，无循环依赖
   └─ 输出: 代码结构设计（包含类图、接口定义、关键算法伪代码）
   ↓
[IMPLEMENT] Step 4: 编写代码和单元测试
   ├─ 输入: 代码结构设计, acceptance_criteria
   ├─ 思考: 代码是否规范？命名是否清晰？测试是否覆盖核心逻辑和边界条件？
   ├─ 验证: 遵循编码规范，测试覆盖率≥80%，核心逻辑100%覆盖
   └─ 输出: 源代码 + 单元测试代码 + 初步测试报告
   ↓
[VERIFY] Step 5: 自检代码质量和测试覆盖
   ├─ 输入: 源代码, 单元测试代码
   ├─ 执行: 代码规范检查（lint）、静态分析、单元测试执行、安全扫描
   ├─ 验证: 无规范违规，圈复杂度≤15，测试全部通过，无高危漏洞
   └─ 输出: 自检报告 + 测试报告 + 覆盖率报告 + 静态分析报告
   ↓
[HANDOVER] Step 6: 准备交接给测试验证阶段
   ├─ 生成: Handover Context（含代码统计、质量指标、开放问题、风险）
   ├─ 更新: Global Context（代码库状态、分支信息、CI/CD状态）
   ├─ 创建: Pull Request（如适用）
   └─ 通知: Verify Test Agent（提交代码审查请求）
```

## Error Handling (错误处理)

> **AI 在执行过程中遇到以下情况时的处理策略**

### Error Scenario 1: 验收标准不清晰

**识别信号**: 
- 验收标准存在模糊表述（如"用户友好"、"高性能"、"快速响应"）
- 缺少量化指标或阈值
- 多个理解方式都合理，无法确定唯一实现方案

**处理流程**:
```
IF 验收标准模糊或有歧义
THEN
  1. 列出所有可能的理解方式（至少2种）
  2. 选择最合理的理解（基于行业标准和最佳实践）
  3. 在代码注释中明确说明假设条件和选择理由
  4. 标记为 [需确认-验收标准] 并在输出中突出显示
  5. IF 影响核心功能实现 THEN 升级到产品经理或Tech Lead确认
  6. 记录决策依据和潜在风险
END
```

**降级方案**: 基于行业标准做出合理假设，明确标注待确认，承诺在评审时重点讨论

**升级条件**: 影响核心功能实现、存在重大理解分歧、或假设可能导致架构变更

---

### Error Scenario 2: 技术难点阻塞

**识别信号**: 
- 多次尝试（≥3次）仍无法解决的技术问题
- 缺少必要的技术知识或工具权限
- 第三方依赖存在兼容性问题或版本冲突
- 性能指标无法达到要求

**处理流程**:
```
IF 遇到无法解决的技术问题
THEN
  1. 分析问题的根本原因（使用5 Whys方法）
  2. 搜索官方文档、社区资源、Stack Overflow寻找解决方案
  3. 尝试替代方案（最多3种不同approach）
  4. 评估每种方案的优缺点和可行性
  5. IF 仍无法解决 THEN 
       a. 记录详细的问题描述、错误信息、尝试过程和失败原因
       b. 升级到技术负责人或架构师
       c. 标记任务为 [阻塞-技术难点]
       d. 提出临时解决方案或简化版本（如可行）
     END
  6. 更新技术债务记录和风险清单
END
```

**降级方案**: 实现简化版本或临时方案，明确标注技术债务和限制条件，承诺后续迭代完善

**升级条件**: 
- P0: 完全阻塞任务进展，超过2小时未解决，无临时方案
- P1: 影响核心功能，但有临时方案可继续其他工作

---

### Error Scenario 3: 设计与实现不匹配

**识别信号**: 
- 实现过程中发现设计文档存在缺陷或不可行
- 设计方案在实际编码中发现性能瓶颈或技术限制
- 发现更好的实现方式或更优的设计模式
- 需求变更导致原设计不再适用

**处理流程**:
```
IF 发现设计与实现不匹配
THEN
  1. 分析差异的具体内容、原因和影响范围
  2. 判断是设计问题（设计不合理）还是实现问题（实现偏差）
  3. 评估修改设计的成本 vs 调整实现的成本
  4. 评估对其它模块的影响（blast radius分析）
  5. IF 需要修改设计 THEN
       a. 联系系统设计师讨论，提供改进建议和数据支持
       b. 提出至少2个备选方案及权衡分析
       c. 等待设计确认后再继续实现
       d. 更新设计文档并记录变更原因
     ELSE
       a. 调整实现方案以符合设计
       b. 记录偏离设计的原因和权衡考虑
       c. 在代码注释中说明特殊情况
     END
  6. 更新变更记录和技术决策日志
END
```

**降级方案**: 记录设计偏差，在代码注释中详细说明原因和权衡考虑，承诺后续与设计团队对齐

**升级条件**: 需要修改架构设计、影响多个模块、或涉及核心技术选型变更

---

### Error Scenario 4: 测试覆盖率不达标

**识别信号**: 
- 单元测试覆盖率 <80%（团队标准为80%）
- 关键业务逻辑路径未覆盖
- 边界条件和异常场景缺失测试
- Mock对象使用过多，真实逻辑测试不足

**处理流程**:
```
IF 测试覆盖率不达标
THEN
  1. 识别未覆盖的代码路径和分支（使用覆盖率报告工具）
  2. 分析未覆盖原因：难以测试/时间不足/设计问题
  3. 补充缺失的测试用例，优先覆盖核心业务逻辑
  4. 对于难以测试的代码，考虑重构以提高可测试性
  5. IF 仍无法达到目标 THEN
       a. 记录未覆盖区域、代码行号和原因
       b. 评估未覆盖区域的风险等级（高/中/低）
       c. 制定后续完善计划和责任人
       d. 标记为 [部分覆盖-需后续完善]
       e. 在输出中明确说明
     END
  6. 确保核心业务逻辑测试覆盖率100%
END
```

**降级方案**: 记录未覆盖区域和风险，承诺在下个迭代或专门的技术债务迭代中完善，获得Tech Lead批准

**升级条件**: 核心业务逻辑测试覆盖率 <60%，或高风险区域未覆盖

## Output Format (输出格式)

> AI必须按照以下结构生成功能实现交付物

```markdown
# Feature Implementation Deliverables

## 1. Task Information
- **Task ID**: {task_id}
- **Task Name**: {task_name}
- **Developer**: {agent_name}
- **Completion Date**: {current_date}
- **Status**: Completed/Partial/Blocked

## 2. Implementation Summary

### 2.1 Acceptance Criteria Status
| AC ID | Acceptance Criteria | Status | Notes |
|-------|---------------------|--------|-------|
| AC-001 | {criteria description} | ✅ Pass / ⚠️ Partial / ❌ Fail | {explanation} |
| AC-002 | {criteria description} | ✅ Pass / ⚠️ Partial / ❌ Fail | {explanation} |

### 2.2 Work Effort
- **Planned Effort**: {X} person-days
- **Actual Effort**: {Y} person-days
- **Variance**: {Z}% (positive = over budget, negative = under budget)

## 3. Code Changes

### 3.1 New Files
| File Path | Description | Lines |
|-----------|-------------|-------|
| src/{path}/{file}.java | {description} | {N} |

### 3.2 Modified Files
| File Path | Changes Description | Lines Added/Deleted |
|-----------|---------------------|---------------------|
| src/{path}/{file}.java | {description} | +{N}/-{M} |

### 3.3 Deleted Files
| File Path | Reason |
|-----------|--------|
| - | - |

### 3.4 Code Statistics
- **Total Lines Added**: {N}
- **Total Lines Modified**: {M}
- **Total Lines Deleted**: {K}
- **Files Changed**: {count}
- **Commits Count**: {count}

## 4. Test Results

### 4.1 Unit Test Summary
- **Total Test Cases**: {N}
- **Passed**: {N}
- **Failed**: {0}
- **Skipped**: {0}
- **Execution Time**: {X}s

### 4.2 Coverage Report
- **Overall Coverage**: {X}% (target: 80%)
- **Critical Logic Coverage**: {Y}% (target: 100%)
- **Line Coverage**: {X}%
- **Branch Coverage**: {Y}%
- **Function Coverage**: {Z}%

### 4.3 Uncovered Areas (if any)
| Code Path | Coverage % | Risk Level | Remediation Plan |
|-----------|------------|------------|------------------|
| {path/to/code} | {X}% | Low/Medium/High | {plan} |

## 5. Code Quality Metrics

### 5.1 Static Analysis Results
- **Lint Errors**: {0} (target: 0)
- **Lint Warnings**: {N} (target: <10)
- **Sonar Issues**: {N} (target: 0 critical/major)
- **Cyclomatic Complexity**: Avg {X}, Max {Y} (target: ≤15)

### 5.2 Security Scan
- **High Vulnerabilities**: {0} (target: 0)
- **Medium Vulnerabilities**: {N}
- **Low Vulnerabilities**: {M}

## 6. Design Decisions

### 6.1 Key Decisions
| Decision ID | Description | Rationale | Alternatives Considered |
|-------------|-------------|-----------|-------------------------|
| DC-001 | {decision} | {rationale} | [Option A, Option B] |

### 6.2 Deviations from Design
| Design Element | Planned | Implemented | Reason for Deviation |
|----------------|---------|-------------|----------------------|
| {element} | {planned} | {actual} | {reason} |

## 7. Documentation Updates

### 7.1 Updated Documents
- [ ] API Documentation (docs/api-spec.md) - Version {version}
- [ ] README.md - Section {section} updated
- [ ] CHANGELOG.md - Entry added for this feature
- [ ] Code Comments - Added to {N} files

### 7.2 API Changes (if applicable)
```yaml
endpoint: POST /api/v1/{resource}
request_body:
  {field}: {type} - {description}
response:
  {field}: {type} - {description}
example:
  request: {...}
  response: {...}
```

## 8. Open Issues & Risks

### 8.1 Open Issues
| Issue ID | Description | Severity | Planned Resolution | Owner | Target Date |
|----------|-------------|----------|--------------------|-------|-------------|
| ISSUE-001 | {description} | Low/Medium/High | {plan} | {owner} | {date} |

### 8.2 Risks
| Risk ID | Description | Probability | Impact | Mitigation |
|---------|-------------|-------------|--------|--------------|
| RISK-001 | {description} | Low/Medium/High | Low/Medium/High | {mitigation} |

## 9. Recommendations for Testing

1. **Focus Areas**: 
   - {area 1}: {reason}
   - {area 2}: {reason}

2. **Test Scenarios**:
   - Scenario 1: {description}
   - Scenario 2: {description}

3. **Integration Points**:
   - Module A: {interaction description}
   - Module B: {interaction description}

## 10. Quality Score

- **Overall Score**: {score}/100
- **Grade**: Excellent (≥95) / Good (≥85) / Satisfactory (≥70) / Needs Improvement (<70)
- **KPI Breakdown**:
  - CODE-COVERAGE: {value}% (target: 80%) - {pass/fail}
  - BUG-DENSITY: {value}/KLOC (target: ≤0.5) - {pass/fail}
  - CYCLOMATIC: {value} (target: ≤15) - {pass/fail}
  - REVIEW-PASS: {value}% (target: 100%) - {pass/fail}
```

## Output Validation (输出验证)

> **重要**: 在提交代码前，必须完成以下验证步骤

### Validation Checklist

**V-001: Functional Validation (功能验证)**
- [ ] All acceptance criteria are implemented and verified
- [ ] Feature logic is correct and matches requirements
- [ ] Exception handling covers all error scenarios
- [ ] Edge cases are handled properly
- [ ] Manual testing passed (if applicable)

**V-002: Code Quality Validation (代码质量验证)**
- [ ] Code follows team coding standards (lint check passed)
- [ ] Naming is clear and meaningful (variables, functions, classes)
- [ ] Functions are appropriately sized (<50 lines recommended)
- [ ] No hard-coded values (use constants or configuration)
- [ ] DRY principle applied (no duplicate code)
- [ ] SOLID principles followed

**V-003: Security Validation (安全验证)**
- [ ] No SQL injection vulnerabilities (use parameterized queries)
- [ ] No XSS risks (sanitize user input)
- [ ] Sensitive data is encrypted (passwords, tokens, PII)
- [ ] Authentication and authorization are correctly implemented
- [ ] Input validation is in place for all user inputs
- [ ] Security scan shows no high-severity vulnerabilities

**V-004: Test Validation (测试验证)**
- [ ] All unit tests pass (0 failures)
- [ ] Test coverage meets target (≥80% overall, 100% critical logic)
- [ ] Boundary conditions are covered
- [ ] Exception paths are tested
- [ ] Tests are repeatable and deterministic
- [ ] Mock objects used appropriately (not over-mocked)

**V-005: Documentation Validation (文档验证)**
- [ ] Code comments are clear and complete
- [ ] API documentation is updated (if API changed)
- [ ] README is updated (if needed)
- [ ] CHANGELOG entry is added
- [ ] Architectural decisions are documented

**V-006: Performance Validation (性能验证)**
- [ ] Response time meets requirements
- [ ] Memory usage is acceptable
- [ ] No obvious performance bottlenecks (N+1 queries, inefficient algorithms)
- [ ] Caching is used appropriately (if applicable)
- [ ] Database queries are optimized (indexes, query plans)

### Validation Failure Handling

```
IF any validation check fails
THEN
  1. Identify specific failed items and severity
  2. Attempt to fix based on available information
  3. IF cannot fix THEN mark as [NEEDS REVIEW] with detailed explanation
  4. Generate validation report with pass/fail status for each check
  5. Highlight critical issues requiring immediate attention
  6. Provide recommendations for improvement
  7. IF critical issues exist THEN do not proceed to handover
END
```

## Handover Context (交接上下文)

> 完成功能实现后，生成以下交接信息给测试验证阶段

```yaml
handover:
  header:
    from_stage: "development"
    to_stage: "testing"
    handover_id: "HO-{{timestamp}}-{{sequence}}"
    timestamp: "{{ISO8601}}"
    prepared_by: "{{agent.name}}"
    
  summary:
    status: "completed/partial/blocked"
    completion_percentage: {{0-100}}
    quality_score: {{0-100}}
    total_lines_added: {{number}}
    total_lines_modified: {{number}}
    total_lines_deleted: {{number}}
    files_changed: {{number}}
    commits_count: {{number}}
    
  artifacts:
    delivered:
      - name: "Feature Implementation"
        path: "src/{feature_path}/"
        version: "1.0.0"
        checksum: "{{SHA256}}"
        files_count: {{number}}
      - name: "Unit Tests"
        path: "tests/{test_path}/"
        version: "1.0.0"
        checksum: "{{SHA256}}"
        test_cases_count: {{number}}
      - name: "Test Report"
        path: "reports/test-report.html"
        version: "1.0.0"
      - name: "Coverage Report"
        path: "reports/coverage/index.html"
        version: "1.0.0"
      - name: "API Documentation"
        path: "docs/api-spec.md"
        version: "1.0.0"
        
  metrics:
    code_coverage: {{percentage}}%
    critical_logic_coverage: {{percentage}}%
    cyclomatic_complexity_avg: {{number}}
    lint_errors: {{number}}
    sonar_issues: {{number}}
    security_vulnerabilities: {{number}}
    
  decisions:
    - id: "DC-001"
      description: "Technical approach selection"
      rationale: "Chose approach A because of better performance (30% faster)"
      alternatives_considered: ["Approach B (simpler but slower)", "Approach C (complex but scalable)"]
      impact: "Affects performance of modules X and Y"
      
  open_issues:
    blocking: []
    non_blocking:
      - id: "ISSUE-001"
        description: "Edge case X has insufficient test coverage (60%)"
        risk_level: "low"
        planned_resolution: "Add boundary test cases in next iteration"
        owner: "Developer"
        target_date: "{{date}}"
        
  risks:
    - id: "RISK-001"
      description: "New feature depends on third-party library v2.0.0 which may have unknown bugs"
      probability: "low"
      impact: "medium"
      mitigation: "Verified compatibility in test environment, monitoring production logs"
      contingency_plan: "Ready to rollback to stable version v1.9.0"
      
  recommendations:
    - "Focus testing on boundary conditions and exception scenarios (see ISSUE-001)"
    - "Pay attention to performance-sensitive areas (functions X and Y have higher complexity)"
    - "Verify integration with existing functionality, especially module Z compatibility"
    - "Consider load testing to validate third-party library stability"
    
  next_steps_for_testing:
    - "Execute integration tests to verify interactions with modules A/B/C"
    - "Perform end-to-end testing covering complete user journeys"
    - "Run performance tests to validate response time and throughput metrics"
    - "Conduct security testing, especially input validation and access control"
    
  quality_metrics:
    kpi_results:
      - kpi_id: "KPI-001"
        name: "CODE-COVERAGE"
        value: 85
        target: 80
        status: "pass"
        critical_logic_coverage: 100
      - kpi_id: "KPI-002"
        name: "BUG-DENSITY"
        value: 0.3
        target: 0.5
        unit: "defects/KLOC"
        status: "pass"
      - kpi_id: "KPI-003"
        name: "CYCLOMATIC"
        value: 12
        target: 15
        max_function_complexity: 18
        status: "pass"
      - kpi_id: "KPI-004"
        name: "REVIEW-PASS"
        value: 100
        target: 100
        review_rounds: 1
        status: "pass"
    overall_score: 92
    grade: "excellent"
```

## Related Assets (关联资产)

| Asset Type | Path | Description |
|------------|------|-------------|
| Scenario | `../scenarios/implement-feature/SCENARIO.md` | 功能实现场景定义 |
| Agent | `../agents/implement-feature.agent.md` | 功能实现Agent角色 |
| Skill | `../skills/implement-feature/SKILL.md` | 功能实现技能包 |
| Instruction | `../instructions/implement-feature.instructions.md` | 功能实现技术指令 |

## Related Resources (相关资源)

- **Standards**: 
  - [Coding Standards](../standards/coding-standards.md) - 团队编码规范
  - [Testing Guidelines](../standards/testing-guidelines.md) - 测试编写指南
  - [Git Workflow](../standards/git-workflow.md) - Git分支管理和提交规范
  - [Code Review Checklist](../standards/code-review-checklist.md) - 代码审查检查清单
- **Templates**: 
  - [Pull Request Template](../templates/pull-request.template.md) - PR模板
  - [Commit Message Convention](../templates/commit-message-convention.md) - Commit消息规范
  - [API Documentation Template](../templates/api-doc.template.md) - API文档模板
- **Evaluations**: 
  - [Code Quality Checklist](../evaluations/code-quality-checklist.md) - 代码质量检查清单
  - [Test Coverage Analysis](../evaluations/test-coverage-analysis.md) - 测试覆盖率分析
  - [Static Code Analysis Report](../evaluations/static-code-analysis.md) - 静态代码分析报告

## Handover Preparation (交接准备)

使用 [contexts/unified-handover-template.md](../contexts/unified-handover-template.md)。

```yaml
handover:
  header:
    from_stage: "development"
    to_stage: "testing"
    handover_id: "HO-{ISO8601}-{sequence}"
    timestamp: "{ISO8601}"
    prepared_by: "implement-feature"
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
