---
name: automate-test
description: Detailed technical instructions for automate-test scenario execution
type: instruction
version: "1.1.0"
stage: automate-test
---

# Instructions: 自动化测试 (Automate Test)

## Test Framework Selection

### Python 技术栈

| 类型 | 推荐框架 | 说明 |
|------|----------|------|
| 单元测试 | pytest | 生态丰富、插件完善 |
| Web 自动化 | Selenium/Playwright | 支持多浏览器 |
| API 测试 | requests + pytest | 轻量级 |
| 性能测试 | locust | Python 原生 |

### JavaScript 技术栈

| 类型 | 推荐框架 | 说明 |
|------|----------|------|
| 单元测试 | Jest | Facebook 维护 |
| E2E 测试 | Playwright/Cypress | 现代浏览器支持 |
| API 测试 | Supertest | Node.js 原生 |

### Java 技术栈

| 类型 | 推荐框架 | 说明 |
|------|----------|------|
| 单元测试 | JUnit 5 | Java 标准 |
| 集成测试 | TestNG | 高级特性 |
| E2E 测试 | Selenium | Web 测试 |

## Test Layering Standards

### 分层结构

```
tests/
├── unit/                    # 单元测试
│   ├── test_services/
│   └── test_utils/
├── integration/             # 集成测试
│   ├── test_api/
│   └── test_db/
├── e2e/                     # 端到端测试
│   ├── pages/               # Page Objects
│   └── test_cases/
└── performance/             # 性能测试
    └── scenarios/
```

### Page Object 模型规范

```python
# 正确示例
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login")

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        return HomePage(self.driver)

# 错误示例 - 直接在测试中操作元素
def test_login():
    driver.find_element(By.ID, "username").send_keys("user")  # 不推荐
```

## Test Data Management

### 测试数据策略

| 策略 | 适用场景 | 实现方式 |
|------|----------|----------|
| Fixture | 固定测试数据 | pytest fixtures |
| Factory | 动态测试数据 | Factory Boy/Faker |
| Mock | 外部依赖 | unittest.mock |
| Shared | 跨测试共享 | conftest.py |

### 数据清理规范

- 每个测试用例执行后清理数据
- 使用 try-finally 确保清理执行
- 并行测试使用唯一数据标识

## Assertion Standards

### 断言命名

```python
# 推荐使用自定义断言
assert_response_status(response, 200)
assert_user_exists(user_id)
assert_payment_processed(order_id)

# 避免直接断言
assert response.status_code == 200  # 不推荐
assert user is not None
```

### 断言消息

```python
# 包含上下文信息
assert actual == expected, f"Expected {expected}, got {actual}, request_id={request_id}"

# 使用自定义错误消息
assert_valid_response(response, "Login API failed")
```

## CI/CD 集成规范

### GitHub Actions 配置

```yaml
name: Test Suite

on: [pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest tests/ --html=report.html
      - name: Upload report
        uses: actions/upload-artifact@v3
        with:
          name: test-report
          path: report.html
```

### 测试执行策略

| 场景 | 触发时机 | 执行范围 |
|------|----------|----------|
| PR 创建 | 每次 | 全量测试 |
| PR 修改 | 每次 | 全量测试 |
| 定时任务 | 每日 | 全量测试 |
| 发布前 | 手动 | 全量 + 回归 |

## Coverage Requirements

| 级别 | 要求 | 说明 |
|------|------|------|
| 单元测试 | ≥ 80% | 核心业务逻辑 |
| 集成测试 | ≥ 60% | API 和数据层 |
| E2E 测试 | ≥ 40% | 关键用户路径 |

## Maintenance Standards

### 用例维护

- 新功能必须同步新增测试用例
- 用例变更需要更新文档
- 废弃用例及时清理

### 失败用例处理

1. 分析失败原因
2. 修复或标记为 known issue
3. 添加跟踪 ticket
4. 设置合理的重试策略


## Overview

> High-level description of the automate-test execution process.
>
> This instruction defines the technical approach, key activities, and success criteria for the automate-test scenario.


## Technical Specifications

> Detailed technical requirements and implementation guidelines for automate-test.

### Required Tools
- [List required tools and frameworks]

### Environment Requirements
- [List environment prerequisites]

### Configuration Parameters
- [List key configuration parameters]


## Best Practices

> Industry-standard best practices for automate-test execution.

1. **Practice 1**: Design test automation with maintainable page-object patterns
2. **Practice 2**: Integrate automated tests into CI/CD pipeline gates
3. **Practice 3**: Maintain test data independence and environment isolation


## Error Handling

> Common error scenarios and resolution strategies for automate-test.

### Error Category 1
**Symptom**: Automated tests are flaky or unreliable
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]

### Error Category 2
**Symptom**: Test execution time exceeds acceptable thresholds
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]


## Quality Standards

> Acceptance criteria and quality gates for automate-test deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | Automated test coverage meets team-defined targets | Automated check |
| Standard 2 | Test flakiness rate is below 5% | Automated check |
| Standard 3 | CI pipeline integration passes consistently | Automated check |
