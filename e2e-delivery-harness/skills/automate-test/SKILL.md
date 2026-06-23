---
name: automate-test
description: "Domain skill for automate-test execution"
category: testing
type: skill
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
language: "zh-CN"
tags: ['skill', 'knowledge']
---
# Skill: 自动化测试 (Test Automation)

## Overview

本 Skill 定义了自动化测试的核心知识体系。

## Core Knowledge

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

## Best Practices

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

## Toolchain

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

## Associated Assets

- **Scenario**: `../../scenarios/automate-test/SCENARIO.md`
- **Instruction**: `../../instructions/automate-test.instructions.md`
- **Prompt**: `../../prompts/automate-test.prompt.md`
- **Agent**: `../../agents/automate-test.agent.md`


## Core Knowledge

> Essential knowledge domain for automate-test execution.

### Domain Fundamentals
- **Test Pyramid (测试金字塔)**: 分层自动化策略，自底向上包含单元测试、集成测试和E2E测试。底层测试数量多、速度快、成本低；顶层测试数量少、速度慢、成本高。遵循金字塔比例可最大化投资回报率。
- **Page Object Model**: 将页面元素和操作封装为独立对象类，实现测试逻辑与页面细节分离。减少UI变更时的测试维护成本，提高代码复用性和可读性。
- **Test Data Management**: 管理测试数据的策略和方法体系，包括数据生成、数据隔离和数据清理。确保测试的可重复性和独立性，避免测试之间的数据污染。

### Key Principles
1. **FIRST原则**: Fast（快速运行）、Independent（独立无依赖）、Repeatable（可重复执行）、Self-validating（自动验证结果）、Timely（及时编写）。遵循FIRST原则确保测试套件的健康和效率。
2. **覆盖率驱动**: 以代码覆盖率和功能覆盖率为导向进行测试设计。关注关键路径和边界条件，优先覆盖高风险区域，而非盲目追求行覆盖率的数字指标。
3. **可维护性优先**: 测试代码与生产代码同等对待，注重可读性、模块化和重构能力。测试应当易于理解和修改，避免过度耦合于实现细节。


## Best Practices

> Proven practices for automate-test excellence.

1. **Arrange-Act-Assert (AAA) 模式**: 将每个测试用例结构化为三个清晰阶段——准备(Arrange)测试前置条件、执行(Act)被测操作、验证(Assert)预期结果。这种结构化模式提高了测试的可读性和一致性，使失败时能快速定位问题阶段。

2. **测试数据工厂模式**: 使用工厂类动态生成测试数据，替代硬编码或Fixture方式的固定数据集。工厂模式通过参数化构建方法，按需生成不同场景下的测试数据，减少重复代码，提高数据准备的灵活性和维护性。

3. **Flaky Test 治理机制**: 建立不稳定的Flaky测试治理流程，包括自动识别、分类标记、隔离处理和逐步修复。Flaky测试会严重损害团队对测试套件的信任，必须及时发现并修复或剔除，避免持续集成管道的可靠性下降。

## Anti-patterns (反模式)

> 与 Common Pitfalls 同义，执行时合并检查。

## Common Pitfalls

> Frequent mistakes to avoid during automate-test execution.

### Pitfall 1: 过度Mock导致假绿色
**Risk**: 过度使用Mock框架隔离外部依赖，使得测试覆盖的是模拟行为而非真实逻辑。Mock的不当配置可能掩盖集成问题，导致测试全部通过但在生产环境中故障。
**Prevention**: 遵循"真实优先"原则——尽可能使用真实实例或轻量级替代方案(如内存数据库)，仅在不可避免时使用Mock。为Mock行为设置验证断言，确保被Mock的行为与实际接口一致。
**Impact**: 交付的代码在集成环境中出现大量未预见的故障，降低发布信心；测试套件逐渐失去守护质量的价值。

### Pitfall 2: UI测试不稳定 (Flaky)
**Risk**: UI自动化测试因网络延迟、渲染时间、动画过渡等不确定因素而间歇性失败。频繁的假阳性结果导致团队对测试结果失去信任，开始忽视失败测试。
**Prevention**: 优先使用显式等待(如WebDriverWait)而非固定sleep；将高频验证下移到集成测试或单元测试层；对脆弱的UI测试添加重试机制和详细截图捕获以便调试。
**Impact**: 假阳性时间消耗显著增加，开发者和QA被迫花费大量时间排查环境问题而非真正的代码缺陷。

### Pitfall 3: 测试间隐式依赖
**Risk**: 测试用例之间存在共享状态或执行顺序依赖，例如：TestCase B依赖TestCase A创建的数据。这种隐式耦合破坏了独立性，导致单独运行或随机排序时测试失败。
**Prevention**: 每个测试用例独立设置(setUp)和清理(tearDown)自己的数据和状态；使用事务回滚或测试容器保证数据隔离；CI中采用随机执行顺序暴露依赖问题。
**Impact**: 测试套件脆弱且不可预测，定位失败根因困难，团队无法快速判断是代码变更还是测试自身的问题。
