---
name: automate-test
description: "Detailed technical instructions for automate-test scenario execution"
applyTo: "scenarios/automate-test/**"
phase: testing
type: instruction
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['instruction', 'technical']
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


## Multi-Language Code Examples

### Python (pytest + Selenium)

```python
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Final

# Page Object Model
class LoginPage:
    """登录页面对象，封装登录相关元素操作"""
    
    URL: Final[str] = "https://example.com/login"
    
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        self._username = (By.ID, "username")
        self._password = (By.ID, "password")
        self._login_btn = (By.ID, "login-btn")
        self._error_msg = (By.CLASS_NAME, "error-message")
    
    def navigate(self) -> "LoginPage":
        self.driver.get(self.URL)
        return self
    
    def login(self, username: str, password: str) -> "HomePage":
        self.driver.find_element(*self._username).send_keys(username)
        self.driver.find_element(*self._password).send_keys(password)
        self.driver.find_element(*self._login_btn).click()
        return HomePage(self.driver)

class HomePage:
    """首页页面对象"""
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        self._welcome = (By.CLASS_NAME, "welcome-message")

# Test Fixture
@pytest.fixture(scope="class")
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# Test Case with assertions
@pytest.mark.smoke
class TestLogin:
    def test_successful_login(self, browser):
        home = LoginPage(browser).navigate().login("admin", "Pass123!")
        welcome_text = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located(home._welcome)
        ).text
        assert "Welcome" in welcome_text, \
            f"Login failed: expected 'Welcome' in '{welcome_text}'"
```

### Java (JUnit 5 + Selenium)

```java
package com.example.tests;

import org.junit.jupiter.api.*;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.support.ui.ExpectedConditions;
import java.time.Duration;

// Page Object Model
class LoginPage {
    private final WebDriver driver;
    private final By usernameInput = By.id("username");
    private final By passwordInput = By.id("password");
    private final By loginButton  = By.id("login-btn");

    public LoginPage(WebDriver driver) {
        this.driver = driver;
    }

    public LoginPage navigate() {
        driver.get("https://example.com/login");
        return this;
    }

    public HomePage login(String username, String password) {
        driver.findElement(usernameInput).sendKeys(username);
        driver.findElement(passwordInput).sendKeys(password);
        driver.findElement(loginButton).click();
        return new HomePage(driver);
    }
}

class HomePage {
    private final WebDriver driver;
    private final By welcomeMessage = By.className("welcome-message");

    public HomePage(WebDriver driver) { this.driver = driver; }

    public String getWelcomeText() {
        return new WebDriverWait(driver, Duration.ofSeconds(5))
            .until(ExpectedConditions.visibilityOfElementLocated(welcomeMessage))
            .getText();
    }
}

// Test Class
@TestInstance(TestInstance.Lifecycle.PER_CLASS)
public class LoginTest {
    private WebDriver driver;

    @BeforeAll
    void setup() {
        driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
    }

    @Test
    @DisplayName("Successful login redirects to home page")
    void testSuccessfulLogin() {
        LoginPage loginPage = new LoginPage(driver);
        HomePage homePage = loginPage.navigate().login("admin", "Pass123!");
        
        String welcomeText = homePage.getWelcomeText();
        Assertions.assertTrue(
            welcomeText.contains("Welcome"),
            "Expected welcome message, got: " + welcomeText
        );
    }

    @AfterAll
    void teardown() {
        if (driver != null) driver.quit();
    }
}
```

### Go (testify)

```go
package e2e_test

import (
    "fmt"
    "testing"
    "time"
    
    "github.com/tebeka/selenium"
    "github.com/stretchr/testify/assert"
    "github.com/stretchr/testify/suite"
)

// Page Object Model
type LoginPage struct {
    wd             selenium.WebDriver
    usernameInput  selenium.WebElement
    passwordInput  selenium.WebElement
    loginButton    selenium.WebElement
}

func NewLoginPage(wd selenium.WebDriver) *LoginPage {
    return &LoginPage{wd: wd}
}

func (p *LoginPage) Navigate() *LoginPage {
    if err := p.wd.Get("https://example.com/login"); err != nil {
        panic(fmt.Sprintf("failed to navigate: %v", err))
    }
    return p
}

func (p *LoginPage) Login(username, password string) *HomePage {
    userElem, _ := p.wd.FindElement(selenium.ByID, "username")
    userElem.SendKeys(username)
    passElem, _ := p.wd.FindElement(selenium.ByID, "password")
    passElem.SendKeys(password)
    btnElem, _ := p.wd.FindElement(selenium.ByID, "login-btn")
    btnElem.Click()
    return &HomePage{wd: p.wd}
}

type HomePage struct {
    wd selenium.WebDriver
}

// Test Suite
type LoginSuite struct {
    suite.Suite
    wd selenium.WebDriver
}

func (s *LoginSuite) SetupSuite() {
    wd, err := selenium.NewRemote(selenium.Capabilities{
        "browserName": "chrome",
    }, "")
    s.Require().NoError(err)
    s.wd = wd
}

func (s *LoginSuite) TearDownSuite() {
    s.wd.Quit()
}

func (s *LoginSuite) TestSuccessfulLogin() {
    page := NewLoginPage(s.wd).Navigate().Login("admin", "Pass123!")
    
    // Assertion with context
    welcome, err := s.wd.FindElement(selenium.ByClassName, "welcome-message")
    if s.Require().NoError(err) {
        text, _ := welcome.Text()
        assert.Contains(s.T(), text, "Welcome",
            "Login verification failed")
    }
}

func TestLoginSuite(t *testing.T) {
    suite.Run(t, new(LoginSuite))
}
```

### JavaScript (Playwright)

```javascript
// playwright.config.js
// @ts-check
const { defineConfig, devices } = require('@playwright/test');

module.exports = defineConfig({
  testDir: './tests',
  timeout: 30000,
  retries: 2,
  use: {
    baseURL: 'https://example.com',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
  },
  projects: [
    { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
    { name: 'firefox',  use: { ...devices['Desktop Firefox'] } },
  ],
});
```

```javascript
// tests/login.spec.js
import { test, expect } from '@playwright/test';

// Page Object Model
class LoginPage {
  /**
   * @param {import('@playwright/test').Page} page
   */
  constructor(page) {
    this.page = page;
    this.usernameInput = page.locator('#username');
    this.passwordInput = page.locator('#password');
    this.loginButton   = page.locator('#login-btn');
  }

  async navigate() {
    await this.page.goto('/login');
    return this;
  }

  async login(username, password) {
    await this.usernameInput.fill(username);
    await this.passwordInput.fill(password);
    await this.loginButton.click();
    return new HomePage(this.page);
  }
}

class HomePage {
  constructor(page) {
    this.page = page;
    this.welcomeMessage = page.locator('.welcome-message');
  }

  async getWelcomeText() {
    return await this.welcomeMessage.textContent();
  }
}

// Test suite
test.describe('Login Flow', () => {
  test('successful login shows welcome message', async ({ page }) => {
    const loginPage = new LoginPage(page);
    const homePage = await loginPage.navigate().login('admin', 'Pass123!');

    const welcomeText = await homePage.getWelcomeText();
    expect(welcomeText).toContain('Welcome');
  });

  test('failed login shows error', async ({ page }) => {
    const loginPage = new LoginPage(page);
    await loginPage.navigate().login('invalid', 'wrong');

    const error = page.locator('.error-message');
    await expect(error).toBeVisible();
    await expect(error).toHaveText(/Invalid credentials/i);
  });
});
```

## Best Practices

> Industry-standard best practices for automate-test execution.

1. **Practice 1**: Design test automation with maintainable page-object patterns
2. **Practice 2**: Integrate automated tests into CI/CD pipeline gates
3. **Practice 3**: Maintain test data independence and environment isolation


## Error Handling

> Common error scenarios and resolution strategies for automate-test.

### Error Scenario 1: 测试环境不稳定导致用例执行失败 (P2)

**触发条件**: 测试环境（如测试数据库、Mock服务、容器化环境）响应超时或不可用，导致自动化测试用例大面积失败（失败率 > 20%）。

**处理流程**:
```
IF 单轮测试失败率 > 20% AND 环境健康检查接口返回非200
THEN
  1. 立即停止当前测试执行流水线，标记环境为"不健康"状态
  2. 执行环境健康检查脚本：/scripts/health-check.sh，验证数据库、消息队列、容器组件的可用性
  3. 根据监测结果重启故障组件（容器重建、数据库连接池刷新、Mock服务拉起）
  4. 等待环境恢复后，触发环境验证用例集合（SmokeTestSuite）重新执行
  5. 验证通过后恢复测试流水线，记录环境故障时长和用例重跑结果
END
```

**降级方案**: 切换至备用测试环境（staging-slave），或回退至本地Docker Compose搭建的最小化测试环境运行关键用例。

**升级条件**: 环境恢复时间 > 30分钟，需要测试负责人介入评估测试计划调整；连续2次环境故障需上报基础设施团队。

### Error Scenario 2: Flaky Test治理 (P2)

**触发条件**: 稳定环境中，同一测试用例在相同代码版本下随机通过/失败（单用例偶发失败率 > 5%），且非环境问题导致。

**处理流程**:
```
IF 用例在 ≥3 次独立流水线运行中出现结果不一致
THEN
  1. 标记该用例为"疑似Flaky"，自动创建Jira Ticket记录失败频次和时间分布
  2. 收集失败日志、截图、网络请求记录（Playwright Trace / Selenium Log），分析失败根因
  3. 引入重试机制：@FlakyTest(retries=2) 注解标记，设置最大重试次数和重试间隔
  4. 定位根因：排查异步等待不足、竞态条件、测试数据冲突、外部依赖抖动
  5. 修复后运行50次重复验证确认稳定，移除Flaky标记
END
```

**降级方案**: 将Flaky用例从阻塞流水线的关键测试集中移出，归入"Flaky Test Suite"单独跟踪，允许流水线继续通过。

**升级条件**: 单用例修复时间 > 3个工作日，或累计Flaky用例数量超过测试集总量的10%，需上报测试架构师。

### Error Scenario 3: 测试数据污染 (P1)

**触发条件**: 并行测试或连续测试执行中，测试用例修改了共享数据状态（如数据库记录、缓存键值），导致后续依赖该数据的用例断言失败。

**处理流程**:
```
IF 后序用例断言失败 AND 失败数据字段与前序用例写入字段重合
THEN
  1. 隔离数据库查询，确认污染数据记录及其来源用例
  2. 立即清理污染数据：执行回滚SQL或调用数据清理API
  3. 为所有测试数据操作增加唯一标识（UUID suffix + 时间戳），确保数据隔离
  4. 重构数据管理策略：将共享数据源改为"每个用例独立Fixture + 事务回滚"模式
  5. 验证修复后并行执行20次，确保数据隔离有效
END
```

**降级方案**: 切换测试数据库至干净的快照副本，该轮测试回退至串行执行。

**升级条件**: 数据污染导致超过10个用例失败，或影响发布流水线阻塞 > 1小时，需DBA和测试Owner联合排查。


## Quality Standards

> Acceptance criteria and quality gates for automate-test deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | Automated test coverage meets team-defined targets | Automated check |
| Standard 2 | Test flakiness rate is below 5% | Automated check |
| Standard 3 | CI pipeline integration passes consistently | Automated check |
## References

- [harness-engineering.md](../standards/harness-engineering.md)
- [output-validation-checklist.md](../evaluations/output-validation-checklist.md)
- [regression-checklist.md](../evaluations/regression-checklist.md)
