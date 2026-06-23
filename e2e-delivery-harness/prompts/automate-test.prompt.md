---
name: automate-test
description: "automate test execution prompt for E2E delivery workflow"
type: prompt
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['prompt', 'ai-execution']
---
# Prompt: 自动化测试 (Automate Test)

## Purpose

本提示词指导AI执行自动化测试任务，按照任务规格搭建测试框架、编写测试用例、集成CI/CD流水线，确保测试覆盖率和质量达标。

### Key Objectives

- **准确理解测试范围**: 深入理解测试需求和被测系统架构，确保测试策略与目标匹配
- **高质量测试框架**: 设计可维护、可扩展的自动化测试框架，遵循最佳实践
- **充分测试覆盖**: 核心路径覆盖率≥80%，关键业务逻辑100%覆盖
- **CI/CD无缝集成**: 将自动化测试集成到持续集成流水线，实现自动触发和报告生成
- **规范交接准备**: 生成完整的Handover Context，便于运维和后续测试阶段接手

## Input Variables (变量定义)

> **AI 在执行前必须确认以下变量已填充**，如未填充则请求用户提供

| Variable | Type | Required | Default | Description | Validation |
|----------|------|----------|---------|-------------|------------|
| `project_name` | string | true | - | 项目名称 | 非空字符串 |
| `test_scope` | string | true | - | 测试范围: unit\|integration\|e2e\|performance | 枚举值之一 |
| `tech_stack` | string | true | - | 技术栈: Python/JavaScript/Java等 | 有效的技术名称 |
| `test_framework` | string | true | - | 测试框架: pytest/jest/JUnit/TestNG | 与tech_stack兼容 |
| `target_system` | string | true | - | 被测系统信息(架构、依赖、环境) | 非空字符串 |
| `coverage_target` | number | false | 80 | 覆盖率目标(百分比) | 0-100的整数 |
| `ci_platform` | string | true | - | CI平台: GitHub Actions/GitLab CI/Jenkins | 有效的CI平台名称 |
| `priority_cases` | array | false | [] | 优先测试的用例列表 | 字符串数组 |

### 示例: 变量的正确格式

```yaml
# 示例: 完整的自动化测试输入
project_name: "用户中心微服务"
test_scope: "integration"
tech_stack: "Python 3.11"
test_framework: "pytest"
target_system: |
  用户中心微服务，基于 FastAPI 框架
  外部依赖：PostgreSQL 14, Redis 7, Kafka 3.0
  部署于 Kubernetes 集群
coverage_target: 85
ci_platform: "GitHub Actions"
priority_cases:
  - "用户登录认证流程"
  - "用户注册与邮箱验证"
  - "权限控制校验"
```

## Chain of Thought (思维链)

> **AI 必须按照以下思维链逐步执行**，每完成一步后进行自我验证

```
[THINK] Step 1: 理解测试需求和被测系统
   ├─ 输入: project_name, test_scope, target_system, priority_cases
   ├─ 思考: 测试范围是否明确？被测系统的关键路径有哪些？外部依赖是什么？
   ├─ 验证: 与项目要求对照，逐条确认无遗漏和误解
   └─ 输出: 测试需求分析备忘录（范围定义、关键路径、依赖清单、风险点）
   ↓
[ANALYZE] Step 2: 分析测试框架和技术方案
   ├─ 输入: 测试需求分析, tech_stack, test_framework
   ├─ 思考: 框架选型是否合适？测试分层如何设计？数据管理策略是什么？
   ├─ 验证: 框架满足测试需求，社区支持良好，与团队技能匹配
   └─ 输出: 测试技术方案（框架结构、分层设计、数据方案、工具链）
   ↓
[DESIGN] Step 3: 设计测试用例和测试数据
   ├─ 输入: 测试技术方案, coverage_target, priority_cases
   ├─ 思考: 用例是否覆盖核心路径和边界条件？测试数据是否可重复使用？
   ├─ 验证: 用例独立无依赖，BDD/GWT风格描述，覆盖率目标可达
   └─ 输出: 测试用例设计（用例清单、数据工厂、断言策略）
   ↓
[IMPLEMENT] Step 4: 实现测试脚本和辅助模块
   ├─ 输入: 测试用例设计, tech_stack
   ├─ 思考: Page Object/Service Object封装是否合理？断言是否完整？
   ├─ 验证: 代码清晰可维护，测试可独立运行，错误信息明确
   └─ 输出: 测试脚本代码 + 辅助模块 + 测试数据 + 执行指南
   ↓
[INTEGRATE] Step 5: 集成CI/CD流水线
   ├─ 输入: 测试脚本, ci_platform
   ├─ 思考: 流水线触发条件如何配置？测试环境如何保障？报告如何生成？
   ├─ 验证: CI配置正确，流水线可成功触发，报告完整
   └─ 输出: CI流水线配置 + 测试报告配置 + 通知配置
   ↓
[VERIFY] Step 6: 验证测试质量和覆盖率
   ├─ 输入: 测试脚本, CI配置
   ├─ 执行: 执行测试套件、检查覆盖率报告、评估用例质量
   ├─ 验证: 覆盖率≥目标值，脆弱测试率≤5%，执行时间≤30min
   └─ 输出: 测试验证报告（执行结果、覆盖率、质量评估、改进建议）
```

## Error Handling (错误处理)

> **AI 在执行过程中遇到以下情况时的处理策略**

### Error Scenario 1: 环境依赖缺失

**识别信号**: 
- ImportError / ModuleNotFoundError
- 测试运行时报依赖缺失错误

**处理流程**:
```
IF 环境依赖缺失
THEN
  1. 检查 requirements.txt / package.json 依赖声明
  2. 确认依赖版本兼容性
  3. 重新安装依赖并验证
  4. IF 仍有问题 THEN 记录错误并升级
END
```

**降级方案**: 使用mock替代不可用外部依赖

**升级条件**: 核心依赖无法安装，阻塞全部测试执行

---

### Error Scenario 2: 测试数据不可用

**识别信号**: 
- AssertionError / NoSuchElementException
- 测试数据准备失败

**处理流程**:
```
IF 测试数据不可用
THEN
  1. 检查测试数据构造逻辑
  2. 确认数据准备脚本是否正确执行
  3. 尝试使用mock数据绕过外部依赖
  4. IF 仍无法解决 THEN 标记为[需修复-数据依赖]
END
```

**降级方案**: 使用mock替代真实数据，缩小测试范围

**升级条件**: 核心测试路径全部阻塞，无法验证基本功能

---

### Error Scenario 3: 测试超时

**识别信号**: 
- TimeoutException
- 测试执行时间超过预期

**处理流程**:
```
IF 测试超时
THEN
  1. 检查超时配置是否合理
  2. 检查被测系统响应时间
  3. 优化测试脚本性能（减少等待、增加并发）
  4. IF 系统性问题 THEN 记录到性能报告
END
```

**降级方案**: 延长超时时间，标记为性能关注点

**升级条件**: 所有测试超时，表明系统不可用

---

### Error Scenario 4: 间歇性失败 (Flaky Test)

**识别信号**: 
- 相同测试多次执行结果不一致
- 与环境或顺序相关的失败

**处理流程**:
```
IF 间歇性失败
THEN
  1. 分析失败模式（环境/顺序/时间敏感）
  2. 添加合理等待/轮询策略替换固定等待
  3. 修复测试依赖或竞态条件
  4. 添加重试机制（自动重试1-2次）
  5. IF 无法修复 THEN 标记为[已知Flaky]并记录
END
```

**降级方案**: 标记flaky测试，设置重试机制，持续监控

**升级条件**: Flaky测试比例>5%，影响CI流水线稳定性

## Quality Metrics (质量指标)

### Key Performance Indicators (KPIs)

| KPI ID | 指标名称 | 目标值 | 计算公式 | 验证方法 | 权重 |
|--------|----------|--------|----------|----------|------|
| KPI-001 | AUTO-COVERAGE | ≥80% | (自动化覆盖路径数/总路径数)×100% | 覆盖率报告测量 | 30% |
| KPI-002 | FLAKY-RATE | ≤5% | (间歇性失败数/总测试数)×100% | 多次执行统计 | 30% |
| KPI-003 | EXEC-TIME | ≤30min | 完整测试套件执行时间 | 定时记录 | 20% |
| KPI-004 | MAINTAIN-COST | 降低≥30% | (自动化后工时/原始手工工时)×100% | 工时对比统计 | 20% |

**综合评分计算**: 
```
Quality Score = (AUTO-COVERAGE达标?分数) × 0.30 + (100% - FLAKY-RATE) × 0.30 + (EXEC-TIME达标?分数) × 0.20 + (MAINTAIN-COST达标?分数) × 0.20
合格: ≥70分 | 优秀: ≥85分 | 卓越: ≥95分
```

## Output Format (输出格式)

> AI必须按照以下结构生成自动化测试交付物

```markdown
## Test Automation Deliverables

### 1. Summary
- **Status**: completed / partial / blocked
- **Completion**: {percentage}
- **Quality Score**: {score}/100

### 2. Acceptance Criteria Status
| AC ID | Criterion | Status | Notes |
|-------|-----------|--------|-------|
| AC-001 | {描述} | ✅ Pass / ⚠️ Partial / ❌ Fail | {说明} |

### 3. Framework Implementation
- **Framework**: {test_framework}
- **Structure**: {Page Object Model / Service Object Model}
- **Test Scope**: {test_scope}
- **Total Cases**: {N}
- **Execution Time**: {X} min

### 4. Test Results
- **Pass Rate**: {X}%
- **Coverage**: {X}% (target: {coverage_target}%)
- **Flaky Rate**: {X}% (target: ≤5%)

### 5. CI/CD Integration
- **Platform**: {ci_platform}
- **Trigger**: {on push / on pull_request / scheduled}
- **Reports**: {test-report.html, coverage.xml}

### 6. Quality Score
- **Overall Score**: {score}/100
- **Grade**: Excellent (≥95) / Good (≥85) / Satisfactory (≥70) / Needs Improvement (<70)
- **KPI Breakdown**:
  - AUTO-COVERAGE: {value}% (target: ≥80%) - {pass/fail}
  - FLAKY-RATE: {value}% (target: ≤5%) - {pass/fail}
  - EXEC-TIME: {value}min (target: ≤30min) - {pass/fail}
  - MAINTAIN-COST: {value}% reduction (target: ≥30%) - {pass/fail}
```

## Output Validation (输出验证)

> **重要**: 在提交前，必须完成以下验证步骤

### Validation Checklist

**V-001: Framework Structure (框架结构验证)**
- [ ] 测试框架结构完整（test runner + assertion library + report generator）
- [ ] Page Object / Service Object 封装合理，层次清晰
- [ ] 测试数据管理方案完善（数据工厂/隔离策略）

**V-002: Test Coverage (测试覆盖验证)**
- [ ] 核心路径覆盖率 ≥ {coverage_target}%
- [ ] 关键业务逻辑实现100%自动化覆盖
- [ ] 边界条件和异常场景已覆盖

**V-003: Test Independence (用例独立性验证)**
- [ ] 无测试间依赖，可独立执行
- [ ] 测试可并行执行，无竞态条件
- [ ] 无顺序相关的失败问题

**V-004: CI Integration (CI集成验证)**
- [ ] CI配置正确，流水线可成功触发测试执行
- [ ] 测试报告完整（包含执行结果、覆盖率、失败详情）
- [ ] 失败通知机制已配置（邮件/即时消息）

**V-005: Code Maintainability (代码可维护性验证)**
- [ ] 代码遵循编码规范，命名清晰
- [ ] 测试脚本有清晰注释和文档
- [ ] 无硬编码值，配置分离

### Validation Failure Handling

```
IF any validation check fails
THEN
  1. 识别具体失败项和严重程度
  2. 尝试修复（基于可用信息）
  3. IF 无法修复 THEN 标记为 [NEEDS REVIEW] 并附详细说明
  4. 生成验证报告（每项pass/fail状态）
  5. 高亮关键问题
  6. IF 关键问题存在 THEN 不进行交接
END
```

## Handover Context (交接上下文)

> 完成自动化测试任务后，生成以下交接信息

```yaml
handover:
  header:
    from_stage: "test-automation"
    to_stage: "verify-test"
    handover_id: "HO-{{timestamp}}-{{sequence}}"
    timestamp: "{{ISO8601}}"
    prepared_by: "{{agent.name}}"

  summary:
    status: "completed/partial/blocked"
    completion_percentage: {{0-100}}
    quality_score: {{0-100}}
    total_test_cases: {{number}}
    coverage_percentage: {{number}}
    flaky_rate: {{number}}
    execution_time_minutes: {{number}}

  artifacts:
    delivered:
      - name: "Test Framework"
        path: "tests/framework/"
        version: "1.0.0"
      - name: "Test Cases"
        path: "tests/test_cases/"
        version: "1.0.0"
      - name: "CI Configuration"
        path: ".github/workflows/test.yml"
        version: "1.0.0"
      - name: "Test Documentation"
        path: "docs/testing/"
        version: "1.0.0"

  metrics:
    auto_coverage: {{percentage}}
    flaky_rate: {{percentage}}
    exec_time_minutes: {{number}}
    maintain_cost_reduction: {{percentage}}

  decisions:
    - id: "DC-001"
      description: "Framework selection"
      rationale: "Chose {framework} for better community support"
      alternatives_considered: ["{alt1}", "{alt2}"]
      impact: "Affects team onboarding and maintenance"

  open_issues:
    blocking: []
    non_blocking:
      - id: "ISSUE-001"
        description: "{flaky test description}"
        risk_level: "low"
        planned_resolution: "Add retry mechanism in next iteration"

  risks:
    - id: "RISK-001"
      description: "Test environment stability"
      probability: "low"
      impact: "medium"
      mitigation: "CI pipeline retry and monitoring"
      contingency_plan: "Fallback to manual testing"

  quality_metrics:
    kpi_results:
      - kpi_id: "KPI-001"
        name: "AUTO-COVERAGE"
        value: 85
        target: 80
        unit: "%"
        status: "pass"
      - kpi_id: "KPI-002"
        name: "FLAKY-RATE"
        value: 3
        target: 5
        unit: "%"
        status: "pass"
      - kpi_id: "KPI-003"
        name: "EXEC-TIME"
        value: 25
        target: 30
        unit: "min"
        status: "pass"
      - kpi_id: "KPI-004"
        name: "MAINTAIN-COST"
        value: 35
        target: 30
        unit: "% reduction"
        status: "pass"
    overall_score: 88
    grade: "good"

  recommendations:
    - "Monitor flaky tests in CI pipeline"
    - "Add performance tests in next iteration"
    - "Review test coverage for edge cases"
```

## Related Assets (关联资产)

| Asset Type | Path | Description |
|------------|------|-------------|
| Scenario | `../scenarios/automate-test/SCENARIO.md` | 自动化测试场景定义 |
| Agent | `../agents/automate-test.agent.md` | 自动化测试Agent角色 |
| Instruction | `../instructions/automate-test.instructions.md` | 自动化测试技术指令 |

## Related Resources (相关资源)

- **Standards**: 
  - [Testing Guidelines](../standards/testing-guidelines.md) - 测试编写指南
  - [Code Review Checklist](../standards/code-review-checklist.md) - 代码审查检查清单
- **Templates**: 
  - [Test Case Template](../templates/test-case.template.md) - 测试用例模板
- **Evaluations**: 
  - [Test Coverage Analysis](../evaluations/test-coverage-analysis.md) - 测试覆盖率分析

## Handover Preparation (交接准备)

使用 [contexts/unified-handover-template.md](../contexts/unified-handover-template.md)。

```yaml
handover:
  header:
    from_stage: "test-automation"
    to_stage: "verify-test"
    handover_id: "HO-{ISO8601}-{sequence}"
    timestamp: "{ISO8601}"
    prepared_by: "automate-test"
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
