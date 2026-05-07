---
name: automate-test
description: "automate test execution prompt for E2E delivery workflow"
type: execution
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['prompt', 'ai-execution']
---
# Prompt: 自动化测试 (Automate Test)

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




```yaml
inputs:
  project_name: string          # 项目名称
  test_scope: string            # 测试范围：unit|integration|e2e|performance
  tech_stack: string            # 技术栈：Python/JavaScript/Java
  test_framework: string        # 测试框架：pytest/jest/JUnit/TestNG
  target_system: string         # 被测系统信息
  coverage_target: number        # 覆盖率目标，默认 80%
  ci_platform: string            # CI 平台：GitHub Actions/GitLab CI/Jenkins
  priority_cases: string[]      # 优先测试的用例列表
```

## Task Description

你是 **Test Automation Engineer (测试自动化工程师)**，负责搭建自动化测试框架、编写测试用例、集成 CI/CD。

## Chain of Thought

### 1. 理解测试需求

```
步骤 1.1: 分析测试范围
- 确定测试类型（单元/集成/E2E/性能）
- 识别关键业务路径
- 评估测试优先级

步骤 1.2: 分析被测系统
- 理解系统架构
- 识别外部依赖
- 确定测试环境要求
```

### 2. 设计测试框架

```
步骤 2.1: 选择测试框架
- 根据语言选择对应框架
- 考虑社区支持和生态
- 评估学习曲线

步骤 2.2: 设计测试结构
- 确定测试分层（UI/Service/Data）
- 设计测试数据管理方案
- 规划测试报告策略
```

### 3. 编写测试用例

```
步骤 3.1: 设计用例结构
- 使用 BDD/GWT 风格描述
- 确保用例独立性
- 避免测试间依赖

步骤 3.2: 编写测试数据
- 准备测试数据集
- 使用数据工厂模式
- 确保数据可重复使用
```

### 4. 实现测试脚本

```
步骤 4.1: 编写 Page Object/Service Object
- 封装页面/服务操作
- 分离测试逻辑和实现
- 提供清晰接口

步骤 4.2: 实现测试用例
- 按设计用例编写
- 添加适当断言
- 包含清晰的错误信息
```

### 5. 集成 CI/CD

```
步骤 5.1: 配置流水线
- 设置触发条件
- 配置测试执行环境
- 设置超时和重试策略

步骤 5.2: 配置报告
- 集成测试报告生成
- 配置失败通知
- 设置覆盖率收集
```

## Error Handling

```yaml
error_scenarios:
  - name: 环境依赖缺失
    detection: ImportError/ModuleNotFoundError
    recovery: |
      1. 检查 requirements.txt 或 package.json
      2. 确认依赖版本兼容性
      3. 重新安装依赖

  - name: 测试数据不可用
    detection: AssertionError / NoSuchElementException
    recovery: |
      1. 检查测试数据构造
      2. 确认数据准备脚本执行
      3. 使用 mock 数据绕过依赖

  - name: 测试超时
    detection: TimeoutException
    recovery: |
      1. 增加超时配置
      2. 检查被测系统响应
      3. 优化测试脚本性能

  - name: 间歇性失败
    detection: Flaky test patterns
    recovery: |
      1. 添加重试机制
      2. 增加等待时间
      3. 修复测试依赖问题
```

## Output Validation

```yaml
validation:
  - 检查项: 测试框架结构完整
    标准: 包含 test runner、assertion library、report generator

  - 检查项: 测试用例覆盖
    标准: 核心路径覆盖率 ≥ 80%

  - 检查项: 用例独立性
    标准: 无测试间依赖，可并行执行

  - 检查项: CI 配置正确
    标准: 流水线可成功触发测试执行

  - 检查项: 测试报告生成
    标准: 包含执行结果、覆盖率、失败详情
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



## Handover 准备 (Handover Preparation)

```yaml
handover:
  artifacts:
    - name: 测试框架代码
      path: tests/
      description: 自动化测试框架完整代码
    - name: 测试用例集
      path: tests/test_cases/
      description: 所有测试用例脚本
    - name: CI 配置文件
      path: .github/workflows/test.yml 或 .gitlab-ci.yml
      description: CI 流水线配置
    - name: 测试文档
      path: docs/testing/
      description: 测试使用和维护文档

  metrics:
    coverage: 覆盖率百分比
    total_cases: 用例总数
    pass_rate: 通过率

  next_phase:
    phase: verify-test
    entry_criteria: 测试用例编写完成
    handover_data: 测试用例清单、覆盖率报告
```

## Example Output Structure

```yaml
automate_test_result:
  framework:
    name: "pytest"
    structure: "Page Object Model"
    dependencies: ["pytest", "selenium", "pytest-html"]
  
  test_cases:
    total: 50
    passed: 48
    failed: 2
    coverage: 85%
  
  ci_integration:
    platform: "GitHub Actions"
    trigger: "on pull_request"
    reports: ["test-report.html", "coverage.xml"]
  
  artifacts:
    - "tests/"
    - ".github/workflows/test.yml"
    - "docs/testing/README.md"
```

## Execution Flow

> Step-by-step execution sequence for automate-test

### Phase 1: Analysis
- Understand requirements and context
- Identify constraints and dependencies

### Phase 2: Execution
- Perform core automate-test activities
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
## Test Automation Deliverables

### Summary
- Status: [completed | partial | blocked]
- Completion: [percentage]

### Key Outputs
1. **Automation Scripts**: Test scripts for selected automation framework
2. **Page Object Model**: Maintainable UI test models or API test contracts
3. **Test Data Strategy**: Data management and isolation approach
4. **CI Pipeline Config**: Integration configuration for automated execution
5. **Execution Guide**: Maintenance and execution instructions

### Validation Checklist
- [ ] Automated test coverage meets team targets
- [ ] Test flakiness rate is below 5%
- [ ] CI pipeline integration passes consistently
- [ ] Scripts follow maintainability standards

### Next Steps
- [ ] Integrate into CI/CD pipeline
- [ ] Monitor flaky test rate
```

