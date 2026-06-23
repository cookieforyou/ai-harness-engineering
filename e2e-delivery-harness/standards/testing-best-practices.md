---
name: testing-best-practices
description: "测试最佳实践标准，定义测试金字塔分层指南(Unit/Integration/E2E)、FIRST原则、TDD/BDD方法论及常见测试反模式"
type: standard
version: "1.1.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-23
status: active
tags: ['standard', 'testing', 'best-practices', 'tdd', 'bdd', 'quality']
---

# 测试最佳实践标准

## Overview

**Purpose**: 定义所有项目代码库统一的测试方法论标准，确保测试质量、可维护性和可重复性。

**Scope**: 适用于单元测试 (Unit)、集成测试 (Integration)、端到端测试 (E2E) 和验收测试 (Acceptance)。

**Audience**: 所有开发工程师和 QA 工程师，要求在编写和审查测试时遵循本标准。

---

## Core Content

### 测试金字塔 (Test Pyramid)

```
           /\
          /  \         E2E Tests (5-10%)
         /    \
        /      \       Integration Tests (15-25%)
       /________\
      /          \     Unit Tests (70-80%)
     /____________\
```

| 层级 | 占比 | 特征 | 约束 |
|------|------|------|------|
| Unit | 70-80% | 毫秒级，内存执行，隔离 | 无 DB/网络/文件系统 |
| Integration | 15-25% | 秒级，组件交互 | Test Container，API 契约 |
| E2E | 5-10% | 分钟级，全系统 | 仅关键用户旅程 |

**指导**: 从单元测试构建；边界处加集成测试；关键路径加 E2E。避免低层覆盖不足时写高层测试。

---

### FIRST 原则

| 字母 | 含义 | 原则 | 检查问题 |
|------|------|------|---------|
| F | Fast 快速 | 测试应快速执行（ms级） | 单个测试 < 100ms？ |
| I | Isolated 隔离 | 测试间无依赖，可独立运行 | 随机顺序执行是否通过？ |
| R | Repeatable 可重复 | 任何环境结果一致 | CI 和本地结果是否一致？ |
| S | Self-validating 自验证 | 自动判定 pass/fail | 是否需要人工检查结果？ |
| T | Timely 及时 | 测试先于代码编写 | TDD: 红-绿-重构流程？ |

**关键约束**: Fast — 慢测试降级或标记 `slow`；Isolated — 禁止共享状态，独立 setup/teardown；Repeatable — Mock 时间/随机数，避免外部服务依赖；Self-validating — 每个测试至少一个断言，禁止人工核查；Timely — 无失败测试不得编写生产代码。

---

### TDD (Test-Driven Development)

**Cycle**: Red (写失败测试) → Green (最简实现使其通过) → Refactor (改进设计)

**Benefits**: 100% 覆盖、清晰 API 设计、回归安全网、可执行文档。

**适用场景**: 新功能、Bug 修复（先写复现测试）、复杂业务逻辑、核心库代码。

**不适用场景**: UI 原型、探索性编码、概念验证、一次性脚本。

**规则**: 没有失败测试，禁止编写生产代码。例外需在代码评审中说明。

---

### BDD (Behavior-Driven Development)

**格式**: Given-When-Then (Gherkin 语法)

```gherkin
Feature: User Login
  Scenario: Successful login with valid credentials
    Given the user has a valid account
    When the user enters correct username and password
    Then the user should be redirected to the dashboard
```

**工具**: Cucumber, SpecFlow, Behave, Jest-Cucumber, Godog.

**BDD vs TDD**: BDD 关注业务行为和验收标准，测试可被非技术人员理解；TDD 关注代码正确性和设计。两者互补 — TDD 驱动内部设计，BDD 驱动外部行为。

**规则**: Given 描述前置状态；When 描述操作；Then 描述结果。避免在场景中使用技术细节。

---

### 测试命名规范

```
- 单元测试:   {MethodName}_{Scenario}_{ExpectedResult}
  示例: `withdraw_insufficientBalance_throwsException`
- 集成测试:   {Component}_{Action}_{Outcome}
  示例: `OrderService_createOrder_persistsCorrectly`
- E2E 测试:   {Feature}_{Scenario}_{Status}
  示例: `UserLogin_ValidCredentials_RedirectsToDashboard`
```

**规则**: snake_case，三要素（对象_场景_期望）。测试文件 `{source}.test.{ext}` 或 `{source}.spec.{ext}`（项目统一）。测试类名 `{Class}Test`。禁止 `test1`、`testFunctionality` 等模糊命名。

---

### 测试反模式 (Anti-patterns)

| 反模式 | 表现 | 后果 | 正确做法 |
|--------|------|------|---------|
| 测试间依赖 | 测试 B 依赖测试 A 结果 | 随机失败、无法单独运行 | 独立 setup/teardown |
| Flaky 测试 | 同样代码有时 Fail | 失去信任 | 标记 flaky + 跟踪 Issue，5日修复或移除 |
| 过度 Mock | Mock 所有依赖包括简单对象 | 不验证真实行为 | 集成测交互，单元测只 Mock 外部 I/O |
| 测试国王 | 单测试类 1000+ 行 | 难以维护 | 按方法/场景拆分，>300行即拆分 |
| 无断言测试 | 无 assert 执行代码 | 永不 Fail，无价值 | 每测试至少一个断言 |
| 条件逻辑 | 含 if/for/try-catch | 测试自身有 Bug | 仅有 Arrange-Act-Assert |
| 测试实现 | 测内部细节而非公共 API | 重构时大量 Fail | 测公共接口和可观测行为 |

---

### Mock vs Stub vs Spy 选择指南

| 类型 | 用途 | 何时使用 |
|------|------|---------|
| Mock | 验证交互行为（调用次数、参数） | 验证外部通信时 |
| Stub | 提供预设返回值 | 需要控制依赖响应时 |
| Spy | 真实对象 + 选择性拦截 | 大部分真实 + 局部 Mock |
| Dummy | 仅占位，不使用 | 填充构造函数参数 |
| Fake | 轻量级替代（如 in-memory DB） | 真实实现太慢或有副作用 |

**决策流程**: 验证交互→Mock；控制返回→Stub；真实+拦截→Spy；填充参数→Dummy；轻量替代→Fake。

**断言最佳实践**: 先写断言再写代码 (TDD)；使用领域特定断言如 `assertThat(order.getTotal()).isEqualTo(100)`；一个测试一个行为场景；失败信息应包含期望值和实际值。

---

## Examples

### 好的测试 (Good Practice)

```java
@DisplayName("OrderService - calculateTotal")
class OrderServiceTest {
    private OrderService orderService;
    private ProductRepository productRepository;

    @BeforeEach
    void setUp() {
        productRepository = mock(ProductRepository.class);
        orderService = new OrderService(productRepository);
    }

    @Test
    @DisplayName("with discount coupon returns discounted amount")
    void calculateTotal_withDiscount_returnsDiscountedAmount() {
        Product product = new Product("P001", "Laptop", 1000.00);
        Order order = new Order().addItem(product, 1)
            .applyCoupon(new Coupon("SAVE10", 10.0));
        when(productRepository.findById("P001")).thenReturn(Optional.of(product));

        double total = orderService.calculateTotal(order);

        assertThat(total).isEqualTo(900.00);
    }
}
```

**特征**: FIRST 完整遵循，命名含三要素，单一断言，独立隔离。

### 差的测试 (Bad Practice)

```java
public class OrderTest {
    private static Order order = new Order();  // 共享状态
    private static int counter;

    @Test public void test1() { counter++; }  // 无断言
    @Test public void test2() {               // 依赖 test1 顺序
        double total = order.calculateTotal();
        try { assertThat(total).isEqualTo(1000.00); }
        catch (Exception e) { }  // 吞异常 + 条件逻辑
    }
}
```

**问题**: 共享静态状态、依赖执行顺序、无断言、吞没异常、条件逻辑。

---

## Compliance Checklist

- [ ] 测试是否遵循金字塔比例（Unit 70-80% / Integration 15-25% / E2E 5-10%）？
- [ ] 每个测试是否满足 FIRST 原则？
- [ ] 测试命名是否包含 {方法}_{场景}_{期望结果} 三要素？
- [ ] 测试是否无相互依赖、可独立运行？
- [ ] 是否存在无断言或条件逻辑的测试？
- [ ] Mock 使用是否适度（只 Mock 外部 I/O，不过度 Mock）？
- [ ] 是否遵循 TDD/BDD 方法论的适用场景？
- [ ] Flaky 测试是否被标记并跟踪处理？

---

## Related Standards

- [test-coverage-guidelines.md](test-coverage-guidelines.md)
- [test-data-management.md](test-data-management.md)
- [harness-engineering.md](harness-engineering.md)
- [authoring-checklist.md](authoring-checklist.md)
