# Skill: 自动化测试 (Test Automation)

## 概述

本 Skill 定义了自动化测试的核心知识体系。

## 核心知识

### 测试金字塔

```
         ┌─────────┐
         │   E2E   │  少量、关键路径
         ├─────────┤
         │ 集成测试│  API、数据层
         ├─────────┤
         │ 单元测试│  大量、快速
         └─────────┘
```

### 测试设计模式

#### Page Object Model

```python
class PageObject:
    """页面对象基类"""
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find_element(locator).click()

    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
```

#### Factory Pattern

```python
class UserFactory:
    @staticmethod
    def create_user(**kwargs):
        return {
            "username": kwargs.get("username", f"user_{uuid4()}"),
            "email": kwargs.get("email", f"test_{uuid4()}@example.com"),
            **kwargs
        }
```

### 测试数据策略

| 策略 | 特点 | 适用场景 |
|------|------|----------|
| Hardcoded | 简单、固定 | 不变数据 |
| Fixture | 可复用 | 多个测试共享 |
| Factory | 动态生成 | 需要唯一数据 |
| Faker | 随机生成 | 大批量数据 |

## 最佳实践

### 测试用例设计

1. **单一职责**：每个用例只验证一个点
2. **独立性**：用例间无依赖
3. **可重复**：可多次执行，结果一致
4. **清晰命名**：用例名描述测试意图

### 断言策略

```python
# 好的断言
assert response.status_code == 200
assert response.json()["user_id"] == expected_id
assert len(items) == expected_count

# 不好的断言
assert response  # 太模糊
assert response.json()["code"] == 0 and response.json()["data"]["valid"] == True
```

### 等待策略

```python
# 显式等待（推荐）
from selenium.webdriver.support.ui import WebDriverWait
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "element_id"))
)

# 避免使用
time.sleep(5)  # 不推荐
```

## 工具链

### Python 生态

| 工具 | 用途 |
|------|------|
| pytest | 测试运行器 |
| pytest-cov | 覆盖率 |
| pytest-html | HTML 报告 |
| factory_boy | 测试数据工厂 |
| faker | 假数据生成 |
| requests | HTTP 客户端 |
| selenium | Web 自动化 |
| playwright | 现代 Web 测试 |

### JavaScript 生态

| 工具 | 用途 |
|------|------|
| Jest | 测试运行器 |
| Mocha | 测试框架 |
| Chai | 断言库 |
| Supertest | HTTP 测试 |
| Cypress | E2E 测试 |
| Playwright | E2E 测试 |

## 关联资产

- **Scenario**: `../../scenarios/automate-test/SCENARIO.md`
- **Instruction**: `../../instructions/automate-test.instructions.md`
- **Prompt**: `../../prompts/automate-test.prompt.md`
- **Agent**: `../../agents/test-automation-engineer.agent.md`


## Core Knowledge

> Essential knowledge domain for automate-test execution.

### Domain Fundamentals
- [Core concept 1]
- [Core concept 2]
- [Core concept 3]

### Key Principles
1. [Principle 1]
2. [Principle 2]
3. [Principle 3]


## Best Practices

> Proven practices for automate-test excellence.

1. **Practice 1**: [Description and rationale]
2. **Practice 2**: [Description and rationale]
3. **Practice 3**: [Description and rationale]


## Common Pitfalls

> Frequent mistakes to avoid during automate-test execution.

### Pitfall 1: [Name]
**Risk**: [Description]
**Prevention**: [How to avoid]
**Impact**: [Consequences if not avoided]

### Pitfall 2: [Name]
**Risk**: [Description]
**Prevention**: [How to avoid]
**Impact**: [Consequences if not avoided]

### Pitfall 3: [Name]
**Risk**: [Description]
**Prevention**: [How to avoid]
**Impact**: [Consequences if not avoided]
