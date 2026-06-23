---
name: normalization-guidelines
description: "数据库范式化指南标准，定义 1NF/2NF/3NF/BCNF/4NF 的形式化定义、实例分析和反范式化(Denormalization)的使用场景与权衡"
type: standard
version: "1.1.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-23
status: active
tags: ['standard', 'database', 'normalization', 'denormalization', 'data-modeling']
---

# 数据库范式化指南标准

## Overview

**Purpose**: 提供标准化的数据库范式化指南，确保数据完整性、减少冗余，并优化查询性能。本指南为项目内所有关系型数据库表结构设计提供统一规范，涵盖从第一范式（1NF）到第四范式（4NF）及反范式化的完整决策框架。

**Scope**: 适用于本项目所有关系型数据库的 Schema 设计，包括核心业务表、日志表、配置表及中间表。对于 NoSQL 存储，建议参考其模式设计原则，但仍鼓励遵循本指南中关于数据一致性的核心思想。

**Audience**: 数据架构师 (Data Architects)、后端开发工程师 (Backend Developers)、数据库管理员 (DBAs) 和任何参与数据模型设计的团队成员。

> 本文件为 E2E Delivery Harness 引用标准。审查基准见 [harness-engineering.md](harness-engineering.md)。

---

## Core Content

### 1NF - 第一范式 (First Normal Form)

**定义**: 表中的每个列包含原子（不可再分）的值；每一行唯一可标识；每一列的值属于同一数据类型。

**违反示例**:
- 多值列：`phone_numbers: "13800138000,13900139000"` —— 单个列存储了多个电话号码。
- 重复组：`phone1, phone2, phone3` —— 用多个列来存储同一类数据。
- 非原子数据：`address: "北京市朝阳区建国路88号,100022,北京"` —— 地址和邮编混在同一个字段。

**解决方案**:
- 多值列 → 拆分为多行，或使用独立的关联表。
- 重复组 → 创建子表，每行存储一个值。

**示例**:
- 违反 1NF：`user(id, name, phones: "138xxxx,139xxxx")`
- 符合 1NF：`user(id, name)` + `user_phone(user_id, phone_number)`，每个电话号码占一行。

---

### 2NF - 第二范式 (Second Normal Form)

**定义**: 满足 1NF + 每个非键列完全函数依赖于整个主键（不存在**部分依赖**）。

**适用场景**: 仅适用于复合主键（Composite Primary Key）的表。单列主键天然满足 2NF。

**违反示例**: 表 `order_item` 的主键为 `(order_id, product_id)`，但 `product_name` 仅依赖于 `product_id`，而不是依赖完整的联合主键。

**解决方案**: 按部分键依赖拆分为独立表。

**示例**:
- 违反 2NF：`order_item(order_id, product_id, product_name, quantity)` —— `product_name` 只依赖 `product_id`。
- 符合 2NF：`product(product_id, product_name)` + `order_item(order_id, product_id, quantity)`。

---

### 3NF - 第三范式 (Third Normal Form)

**定义**: 满足 2NF + 每个非键列不存在对主键的**传递依赖**（即不存在 A → B → C 的依赖链，其中 B 不是候选键）。

**违反示例**: `employee(emp_id, dept_id, dept_name)` 中，`dept_name` 依赖于 `dept_id`，而 `dept_id` 不是主键。

**解决方案**: 将传递依赖的列迁移到独立的表中。

**示例**:
- 违反 3NF：`order(order_id, customer_id, customer_name, customer_address)`
- 符合 3NF：`order(order_id, customer_id)` + `customer(customer_id, name, address)`

---

### BCNF - 鲍依斯-科得范式 (Boyce-Codd Normal Form)

**定义**: 满足 3NF + **每个决定因子（determinant）都是候选键**。BCNF 是 3NF 的强化版本，解决了 3NF 未能覆盖的某些特殊依赖情形。

**违反示例**: 当非键属性决定了复合键的一部分时。考虑表 `student_course(student_id, course_id, instructor)`，假设每个课程只有一位讲师 (`instructor → course_id`)，但 instructor 不是超键（superkey），即同一个讲师可以教授多个课程。

**解决方案**: 将决定因子拆分为独立表。

**示例**:
- 违反 BCNF：`student_course(student_id, course_id, instructor)`，其中 `instructor → course_id`。
- 符合 BCNF：`course_instructor(course_id, instructor)` + `student_enrollment(student_id, course_id)`。

---

### 4NF - 第四范式 (Fourth Normal Form)

**定义**: 满足 BCNF + 不存在非平凡的多值依赖（Multi-Valued Dependency, MVD）且该 MVD 不是函数依赖。

**违反示例**: 表中独立存储了关于同一个实体的多个多值事实。例如 `employee_skill_language(emp_id, skill, language)` 中，技能和语言是相互独立的——一个员工拥有的技能并不依赖于其掌握的语言。

**解决方案**: 将每个独立的多值属性拆分为单独的表。

**示例**:
- 违反 4NF：`employee_skill_language(emp_id, skill, language)` —— 造成大量笛卡尔积式的冗余行。
- 符合 4NF：`employee_skill(emp_id, skill)` + `employee_language(emp_id, language)`。

---

### 反范式化 (Denormalization) 场景与权衡

**何时应考虑反范式化**:
- **读密集型工作负载**：面对高并发读取、低延迟查询的场景，适当反范式化可以减少 JOIN 次数。
- **报表与分析**：数据仓库 / OLAP 场景常采用星型或雪花型模式，通过预聚合和冗余来提升分析效率。
- **高 JOIN 开销场景**：当 JOIN 操作成为性能瓶颈且优化索引无法解决时。
- **缓存层替代**：在不适合引入 Redis / Memcached 等外部缓存时，通过字段冗余达到类似效果。
- **微服务数据隔离**：服务切分后，各服务持有自己的数据副本以避免跨服务 JOIN。

**权衡分析**:

| 方面 | 范式化 (Normalized) | 反范式化 (Denormalized) |
|------|---------------------|------------------------|
| 读性能 | 较低（多表 JOIN） | 较高（单表或少量表） |
| 写性能 | 较高（无冗余更新） | 较低（需维护冗余一致性） |
| 数据冗余 | 无 | 有 |
| 存储成本 | 较低 | 较高 |
| 更新异常风险 | 低 | 高（需应用层保证） |
| 数据一致性 | 天然保证 | 需要额外机制 |

**常见反范式化模式**:
1. **预计算聚合** (Summary Tables)：提前计算并存储 COUNT / SUM / AVG 等聚合结果。
2. **物化视图** (Materialized Views)：数据库原生支持的预计算视图，自动或定时刷新。
3. **字段冗余**：在 `order` 表中直接存储 `customer_name`，可减少 80% 的 JOIN 查询，避免每次读取时 JOIN `customer` 表。
4. **JSON / JSONB 列**：在关系型数据库中嵌入半结构化数据（如 PostgreSQL 的 JSONB），适用于属性不固定的场景。

**黄金法则**: 以范式化设计为起点，90% 以上的新表应从 3NF 开始设计，在明确测量到性能瓶颈后有意图地进行反范式化。**每个反范式化决策必须有文档化的理由和可量化的收益预期，预期收益需 ≥30% 查询性能提升**，并在代码评审中标注。

---

### 实用范式检查清单

在设计或评审表结构时，逐项检查以确保满足目标范式等级：

1. **所有列是否都是原子的？** —— 不存在逗号分隔的多值、JSON 字符串（不适用于半结构化设计）或重复组。(1NF)
2. **是否有清晰的主键定义？** —— 每行可唯一标识；首选自增 ID、UUID 或业务自然键。(1NF)
3. **所有非键列是否完全依赖于完整主键？** —— 尤其注意复合主键表是否存在部分依赖。(2NF)
4. **是否存在传递依赖？** —— 检查 A → B → C 的依赖链（B 不是候选键）。(3NF)
5. **每个决定因子是否都是候选键？** —— 非键属性是否决定了键的一部分。(BCNF)
6. **独立的多值事实是否已分离？** —— 检查表中是否存在多个相互独立的 1:N 关系。(4NF)
7. **反范式化字段是否可控？** —— 是否有应用层逻辑、触发器或物化视图来保证数据一致性？

---

## Examples

### 反范式化结构（Before）

```sql
-- 一张大表包含所有信息 —— 违反 3NF
CREATE TABLE orders (
    order_id      BIGINT PRIMARY KEY,
    order_date    TIMESTAMP NOT NULL,
    customer_id   BIGINT NOT NULL,
    customer_name VARCHAR(100) NOT NULL,   -- 冗余：传递依赖
    customer_addr VARCHAR(200) NOT NULL,   -- 冗余：传递依赖
    product_id    BIGINT NOT NULL,
    product_name  VARCHAR(100) NOT NULL,   -- 冗余：部分依赖（在复合键场景下）
    product_price DECIMAL(10,2) NOT NULL,  -- 冗余
    quantity      INT NOT NULL,
    -- 同一订单多个商品时，客户和产品信息大面积重复
);
```

**更新异常举例**:
- 客户地址变更需更新所有关联的 `orders` 行，遗漏则产生数据不一致。
- 产品价格更新需扫描全部历史订单，且历史价格会被覆盖。
- 插入订单时需重复录入大量客户和产品信息。

### 范式化结构（After - 3NF）

```sql
-- 客户表
CREATE TABLE customers (
    customer_id   BIGINT PRIMARY KEY,
    name          VARCHAR(100) NOT NULL,
    address       VARCHAR(200) NOT NULL,
    created_at    TIMESTAMP DEFAULT NOW()
);

-- 产品表
CREATE TABLE products (
    product_id    BIGINT PRIMARY KEY,
    name          VARCHAR(100) NOT NULL,
    price         DECIMAL(10,2) NOT NULL,
    category      VARCHAR(50)
);

-- 订单表
CREATE TABLE orders (
    order_id      BIGINT PRIMARY KEY,
    customer_id   BIGINT NOT NULL REFERENCES customers(customer_id),
    order_date    TIMESTAMP NOT NULL DEFAULT NOW(),
    status        VARCHAR(20) NOT NULL DEFAULT 'pending'
);

-- 订单明细表
CREATE TABLE order_items (
    order_id      BIGINT NOT NULL REFERENCES orders(order_id),
    product_id    BIGINT NOT NULL REFERENCES products(product_id),
    quantity      INT NOT NULL,
    unit_price    DECIMAL(10,2) NOT NULL,  -- 快照价格，防止产品表价格变更影响历史订单
    PRIMARY KEY (order_id, product_id)
);
```

### 对比总结

| 维度 | 反范式化 (Before) | 范式化 (After) |
|------|-------------------|----------------|
| 查询一个订单的客户和产品信息 | 1 次单表查询 | 1~3 次 JOIN 查询 |
| 更新客户地址 | 更新 N 行（可能遗漏） | 更新 1 行 |
| 更新产品价格（保持历史不变） | 不可能（会覆盖历史） | 通过 `unit_price` 快照支持 |
| 插入新订单 | 必须知道客户和产品完整信息 | 仅需 ID 引用 |
| 数据一致性保障 | 依赖应用层逻辑 | 外键约束 + 单一数据源 |

---

## Compliance Checklist

使用以下检查项对数据库 Schema 进行合规审查：

**建议**: 对于 OLTP 系统，90% 以上的表应满足 3NF 要求。

- [ ] 所有表是否至少满足 3NF？（业务需求明确允许反范式化的除外）
- [ ] 是否有列包含多值或重复组？（违反 1NF）
- [ ] 复合主键表中是否有部分依赖？（违反 2NF）
- [ ] 是否有传递依赖（A→B→C）？（违反 3NF）
- [ ] BCNF 检查：非键列是否决定了候选键的一部分？
- [ ] 反范式化是否有文档记录的 rationale 和可量化的性能收益？
- [ ] 核心业务表（订单、账户、支付、用户）是否保持 3NF 以上？设计合规率应 ≥95%
- [ ] 反范式化字段的更新频率是否可控？建议不超过总写入量的 5%，更新成功率应 ≥99.9%
- [ ] 反范式化字段是否通过应用层逻辑、触发器或物化视图保证一致性？

---

## 相关资产

- [database-naming-convention.md](../standards/database-naming-convention.md)
- [harness-engineering.md](../harness-engineering.md)
- [asset-model.md](../standards/asset-model.md)
- [authoring-checklist.md](../standards/authoring-checklist.md)
- [output-quality-rubric.md](../standards/output-quality-rubric.md)

---

*本标准的维护者应至少每季度复审一次，确保与业务发展和技术演进保持同步。任何修改需经架构评审委员会 (ARC) 审批。*
