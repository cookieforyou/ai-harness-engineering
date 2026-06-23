---
name: test-data-management
description: "测试数据管理标准，定义测试数据隔离策略、数据工厂模式、数据脱敏规范(GDPR合规)、测试数据生命周期及生产数据引用的合规要求"
type: standard
version: "1.1.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-23
status: active
tags: ['standard', 'testing', 'test-data', 'data-management', 'gdpr', 'compliance']
---

# 测试数据管理标准

## Overview

**Purpose**: 标准化所有测试阶段中测试数据的创建、管理、共享和销毁流程，确保测试的独立性、可重复性和合规性。

**Scope**: 覆盖单元测试、集成测试、E2E测试、性能测试和手动测试中的测试数据使用。

**Audience**: 全体开发人员、QA工程师、数据工程师及涉及测试数据管理的相关人员。

## 测试数据隔离策略

**原则**: 每个测试必须拥有独立的数据，测试之间不得共享可变状态。共享状态是导致非确定性测试失败（flaky test）的首要原因。

**隔离级别**:

| 级别 | 说明 | 适用场景 | 性能影响 |
|------|------|---------|---------|
| L1 | 每测试用例独立创建/销毁 (setUp / tearDown) | Unit test | 低 |
| L2 | 每组测试共享 (setUpClass / beforeAll) | Integration test | 中 |
| L3 | 整个套件共享只读数据 | E2E / Performance | 高 |
| L4 | 外部共享数据集（版本控制 + 不可变快照） | Manual / Staging | N/A |

- **并行测试**: 使用 L1 隔离级别或唯一数据分区策略（如测试ID前缀 + 运行实例标识），防止并行执行时的数据竞争。
- **共享只读数据 (L3)**: 任何测试不得修改 L3 数据。如需修改，必须在测试本地创建副本。
- **外部数据集 (L4)**: 版本控制管理，每次变更需评审并更新版本号。

## 数据工厂模式 (Test Data Factory / Builder Pattern)

所有测试数据应通过工厂函数生成，禁止在测试代码中硬编码数据值。

```python
class UserFactory:
    @staticmethod
    def create(**overrides):
        defaults = {
            "username": f"test_user_{uuid4().hex[:8]}",
            "email": f"test_{uuid4().hex[:8]}@example.com",
            "is_active": True,
            "role": "viewer"
        }
        defaults.update(overrides)
        return User(**defaults)
```

**模式演进**: Factory (简单工厂) → Builder (构建器，支持链式调用) → Fixture (预置固定场景)

**优势**:
- UUID 保证数据唯一性，避免并行测试冲突
- 显式覆盖 (overrides) 便于构造边界条件和异常场景
- 默认值覆盖 80% 的常规测试场景，减少样板代码

**编写指南**:
- 始终为每个实体定义独立的 Factory 类
- 唯一标识符（用户名、邮箱、ID）必须使用 UUID 或时间戳生成
- 禁止在 Factory 外部硬编码测试数据值
- 复杂关联实体（如"用户 + 订单 + 支付记录"）使用 Builder 模式组装

## 数据脱敏规范 (GDPR 合规)

生产数据用于测试时，**必须**经过匿名化或去标识化处理。禁止将原始生产数据直接复制到测试环境。

**脱敏规则**:

| 数据类型 | 脱敏规则 | 示例 |
|----------|---------|------|
| 姓名 | 替换为随机生成名称 | "张三" → "test_user_{uuid}" |
| 手机号 | 保留前3位，替换后6位 | 138****0000 |
| 邮箱 | 替换域名 + 随机前缀 | user@company.com → test_{uuid}@test.com |
| 身份证 | 完全脱敏，替换为虚拟ID | 110101199001011234 → TID-{uuid} |
| 地址 | 保留城市级别，替换详细地址 | 只保留"北京市" |
| 密码/凭证 | 永远不能使用真实凭证 | 统一替换为 test-cred-{env} |

**推荐工具**:
- Python: [Faker](https://github.com/joke2k/faker)
- Java: [Java Faker](https://github.com/DiUS/java-faker)
- Ruby: [faker-ruby](https://github.com/faker-ruby/faker)
- Node.js: [@faker-js/faker](https://fakerjs.dev/)

**禁止行为**:
- 将生产数据库直接复制到测试环境而不经过脱敏管道
- 在本地开发环境中加载生产数据
- 将生产数据提交到版本控制系统

**审计要求**: 所有测试数据来源和脱敏方案必须在 `test-data-sources.md` 中记录，定期审计检查。

## 测试数据生命周期

测试数据从创建到销毁的完整管理流程：

- **创建 (Create)**:
  - 单元测试: Factory 生成，测试函数内创建
  - 集成测试: Factory 或受版本控制的 seed 数据
  - E2E/性能测试: 脱敏后的生产快照或专用 seed 数据集

- **使用 (Use)**:
  - 每次测试运行分配独立数据集，运行时跟踪数据使用
  - 并行测试通过数据分区标记实现隔离

- **清理 (Cleanup)**:
  - 单元测试: 自动回收（内存数据库或事务回滚）
  - 集成/E2E 测试: 在 `afterEach` / `@AfterEach` 中显式清理
  - 共享环境（Staging）: 每日定时清理任务
  - 数据库重新播种: 每周对 staging 数据做全量重置

- **保留 (Retention)**:
  - 测试产出物（日志、截图）: 保留 30 天
  - 测试数据: 7 天后自动删除，除非标记为可复现缺陷所需

- **隔离 (Quarantine)**:
  - Flaky 测试相关的数据标记为待审查状态
  - 隔离数据在 14 天内不会被自动清理
  - 审查完成后决定保留或删除

## 生产数据引用的合规要求

生产数据仅在满足以下所有条件时可用于测试：

1. **书面批准**: 获得数据保护官 (DPO) 的明确书面批准
2. **自动脱敏管道**: 数据摄取前通过自动脱敏/匿名化管道处理
3. **隔离存储**: 脱敏后的数据存储在独立的数据库或命名空间中
4. **访问审计**: 所有访问操作记录日志，支持审计追踪
5. **有限保留**: 数据保留最多 30 天，到期自动清除

**红线规则**:
- 永远不要将生产数据用于本地开发
- 永远不要将生产数据提交到版本控制
- 生产数据快照必须在提取前完成脱敏，不得在提取后脱敏
- 违反上述规则的代码提交将被 CI 流水线拦截并触发告警

## 测试数据目录结构

所有测试数据文件应按照以下目录结构组织：

```
tests/
  data/
    seeds/          -- 种子数据文件 (JSON/YAML)
    fixtures/       -- 序列化测试夹具 (pickle/json)
    factories/      -- 数据工厂定义代码
    masked/         -- 脱敏后的生产数据快照
```

- `seeds/`: 版本控制的静态数据集，用于集成测试和 staging 环境初始化
- `fixtures/`: 可序列化的测试夹具数据，用于加速测试集启动
- `factories/`: 工厂类和构建器模式的实现
- `masked/`: 经过脱敏管道处理的生产数据快照（带时间戳）

## Examples

**推荐做法（Good）**:

```python
# Good: 工厂模式 + 唯一数据 + 显式清理
class TestOrder:
    def setup_method(self):
        self.order = OrderFactory.create(status="pending")
    def teardown_method(self):
        self.order.delete()
    def test_cancel_order(self):
        self.order.cancel()
        assert self.order.status == "cancelled"
```

**不推荐做法（Bad）**:

```python
# Bad: 硬编码数据 + 共享可变状态
class TestOrder:
    # 硬编码数据，无法并行运行
    order_id = 1001      # 与其他测试冲突
    username = "admin"   # 与真实用户混淆
    email = "admin@test.com"  # 无唯一性保证

    # 共享 Order 对象，测试间影响
    order = Order(id=1001, user="admin", status="pending")

    def test_cancel_order(self):
        self.order.cancel()
        assert Order.query.get(1001).status == "cancelled"
        # 问题：修改了共享状态，影响其他测试
```

**生产数据处理示例**:

```
# Good: 提取前脱敏
production_db → masking_pipeline (Faker) → masked_snapshot → test_staging_db

# Bad: 提取后脱敏（存在泄露风险）
production_db → raw_snapshot (泄露风险) → masking_pipeline → test_staging_db ❌
```

## Compliance Checklist

```
- [ ] 每个测试用例是否使用独立数据或正确隔离？
- [ ] 测试数据是否通过 Factory/Builder 模式生成，而非硬编码？
- [ ] 生产数据引用是否经过脱敏处理？
- [ ] 个人身份信息(PII)是否严格按照脱敏规则处理？
- [ ] 测试数据是否在测试完成后被正确清理？
- [ ] 是否有保留超过 7 天的测试数据需要审查？
- [ ] 生产数据是否未提交到版本控制？
- [ ] 测试数据来源和脱敏方案是否已文档化？
```

## Related Standards

- [testing-best-practices.md](testing-best-practices.md)
- [test-coverage-guidelines.md](test-coverage-guidelines.md)
- [error-classification.md](error-classification.md)
- [harness-engineering.md](harness-engineering.md)
