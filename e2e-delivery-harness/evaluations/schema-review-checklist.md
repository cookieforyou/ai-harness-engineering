---
name: schema-review-checklist
type: evaluation
version: "1.1.0"
status: active
updated: 2026-06-23
description: >
  Schema审查清单，从命名规范、数据类型合理性、索引设计、约束完整性、
  性能考量和安全合规(GDPR列标识)六大维度评估数据库schema设计质量。
  适用于新增表/字段的DDL审查、数据库重构评审和数据模型规范一致性检查。
---

# Schema 审查清单 (Schema Review Checklist)

## Overview

Schema 审查清单用于系统化审查数据库 Schema 设计质量，确保新增或变更的数据库对象（表、索引、约束、视图）符合组织的数据管理规范和最佳实践。本评估覆盖命名规范、数据类型、索引、约束、性能和安全合规六个维度，适用于 DDL 合入前的强制审查环节。

### 适用场景

- 新增数据库表的 DDL 代码审查
- 已有表结构变更的 DDL 评审
- 数据库重构/迁移方案的预审
- 数据模型与 ORM 实体的一致性检查

---

## Evaluation Criteria

| 维度 | 权重 | 目标值 | 测量方法 |
|------|------|--------|----------|
| 命名规范 | 15% | 100% 合规 | 正则匹配命名规则 + Code Review |
| 数据类型合理性 | 20% | 无不合理类型 | 逐字段审查 + 数据字典比对 |
| 索引设计审查 | 25% | 索引冗余率 ≤ 10% | 索引覆盖度分析 + 冗余检测 |
| 约束完整性 | 20% | 约束覆盖率 ≥ 95% | 必填/唯一/外键/检查约束完整性检查 |
| 性能考量 | 10% | 无全表扫描风险 | 数据量预估 + 查询模式分析 |
| 安全合规 | 10% | 100% 合规 | PII/GDPR 数据列标识 + 加密审计 |

---

## Scoring Formula

```
命名得分     = 合规列数 / 总列数 × 100
类型得分     = 合理类型列数 / 总列数 × 100
索引得分     = max(0, 100 - 冗余索引率 × 200)
约束得分     = 约束覆盖率 × 100
性能得分     = 预估查询无量级问题 → 100, 有风险 → 50, 严重 → 0
安全得分     = 合规标记完成率 × 100

总分 = 命名得分 × 15% + 类型得分 × 20% + 索引得分 × 25% + 约束得分 × 20% + 性能得分 × 10% + 安全得分 × 10%
```

### 等级划分

| 等级 | 分数范围 | 判定 |
|------|----------|------|
| S (Excellent) | ≥ 90 | Schema 设计规范，可直接部署 |
| A (Good) | 80-89 | 少量优化建议，修复后部署 |
| B (Fair) | 70-79 | 存在明显问题，需返工后重审 |
| F (Failed) | < 70 | 设计严重不合规，禁止部署 |

---

## Checklist

### 1. 命名规范检查 (6项)

- [ ] **SCR-NAM-001**: 表名使用业务领域名词（单数或复数统一），长度 ≤ 30 字符
- [ ] **SCR-NAM-002**: 字段名使用 snake_case（MySQL/PG）或 camelCase（MongoDB），无大小写混用
- [ ] **SCR-NAM-003**: 索引命名遵循约定：`idx_表名_字段名` / `uq_表名_字段名` / `pk_表名`
- [ ] **SCR-NAM-004**: 外键命名包含来源表和目标表名：`fk_源表_目标表`
- [ ] **SCR-NAM-005**: 不使用数据库保留字作为表名或字段名（通过保留字列表校验）
- [ ] **SCR-NAM-006**: 布尔类型字段以 `is_` / `has_` / `can_` 前缀开头

### 2. 数据类型合理性检查 (6项)

- [ ] **SCR-DTP-001**: 数值类型使用精确类型：金额用 `DECIMAL(18,2)` 而非 `FLOAT/DOUBLE`
- [ ] **SCR-DTP-002**: 字符串类型长度有上限（非一律 `VARCHAR(255)`），长文本用 `TEXT/CLOB`
- [ ] **SCR-DTP-003**: 时间类型使用 `TIMESTAMP WITH TIME ZONE`，统一存储 UTC
- [ ] **SCR-DTP-004**: 枚举字段考虑使用 ENUM/TINYINT 或关联字典表，而非 VARCHAR 自由输入
- [ ] **SCR-DTP-005**: 主键类型使用 `BIGINT`/`UUID`，不使用自增 INT（考虑未来数据量扩展）
- [ ] **SCR-DTP-006**: 可选字段（可为 NULL）有业务含义明确的默认值或 NULL 语义文档

### 3. 索引设计审查 (6项)

- [ ] **SCR-IDX-001**: 查询 WHERE 条件中的核心字段有对应索引，无遗漏（基于 EXPLAIN 验证）
- [ ] **SCR-IDX-002**: 复合索引顺序遵循选择性从高到低（cardinality DESC）
- [ ] **SCR-IDX-003**: 索引冗余率 ≤ 10%，无完全重复或前导列相同导致索引覆盖的情况
- [ ] **SCR-IDX-004**: 外键字段有索引，避免外键关联时的全表扫描
- [ ] **SCR-IDX-005**: 唯一约束通过唯一索引实现（`UNIQUE`），区分业务唯一键与代理主键
- [ ] **SCR-IDX-006**: 索引总数控制在合理范围（单表 < 8 个索引，OLTP 建议 5 个以内）

### 4. 约束完整性检查 (5项)

- [ ] **SCR-CON-001**: 全部主键约束已定义（`PRIMARY KEY`），无缺少主键的表
- [ ] **SCR-CON-002**: 业务上必有值的字段标记 `NOT NULL`，无遗漏必填字段
- [ ] **SCR-CON-003**: 业务上唯一的值有 `UNIQUE` 约束，不依赖应用程序逻辑保证唯一性
- [ ] **SCR-CON-004**: 外键约束已定义（`REFERENCES`），或文档化说明为什么未使用外键（性能/分片原因）
- [ ] **SCR-CON-005**: `CHECK` 约束用于业务规则验证（如 `status IN ('ACTIVE', 'INACTIVE')`）

### 5. 性能考量检查 (5项)

- [ ] **SCR-PRF-001**: 预估单表数据量 ≤ 5000 万行（考虑分表策略），有数据量增长估算
- [ ] **SCR-PRF-002**: 预写查询模式分析文档，高频查询的 WHERE/JOIN/ORDER BY 有索引支持
- [ ] **SCR-PRF-003**: 大字段（TEXT/BLOB/JSON）独立存储或使用分表，不混入高频查询的主表
- [ ] **SCR-PRF-004**: JOIN 操作关联的字段类型一致（避免隐式类型转换导致索引失效）
- [ ] **SCR-PRF-005**: 数据归档/清理策略已定义（软删除/分区/定期归档）

### 6. 安全合规检查 (5项)

- [ ] **SCR-SEC-001**: PII（个人可识别信息）列已标识 `[PII]` 标签，遵循最小化存储原则
- [ ] **SCR-SEC-002**: GDPR/CCPA 合规列（如 `consent_flags`、`data_retention_date`）已定义
- [ ] **SCR-SEC-003**: 敏感字段（密码/Token/密钥）不存储明文，使用加密/Hash 存储
- [ ] **SCR-SEC-004**: 数据访问权限按业务角色划分，无跨 Schema 的默认公共访问
- [ ] **SCR-SEC-005**: 审计日志列（`created_at`、`created_by`、`updated_at`、`updated_by`）已添加

---

## Report Template

```markdown
# Schema 审查报告

## 概要

| 项目 | 值 |
|------|-----|
| 审查对象 | [数据库.表名] |
| 审查日期 | YYYY-MM-DD |
| DDL 版本 | [Git Commit SHA] |
| 表/变更类型 | [新增表/字段变更/索引变更] |
| 综合评分 | [XX.X] 分 / 100 |
| 等级判定 | [S/A/B/F] |

## 六维度评分

| 维度 | 得分 | 权重 | 加权得分 |
|------|------|------|----------|
| 命名规范 | XX/100 | 15% | XX.X |
| 数据类型合理性 | XX/100 | 20% | XX.X |
| 索引设计审查 | XX/100 | 25% | XX.X |
| 约束完整性 | XX/100 | 20% | XX.X |
| 性能考量 | XX/100 | 10% | XX.X |
| 安全合规 | XX/100 | 10% | XX.X |
| **总分** | | **100%** | **XX.X** |

## 未通过项明细

| 检查项 | 字段/对象 | 问题描述 | 严重等级 | 修复建议 |
|--------|-----------|----------|----------|----------|
| | | | | |

## 索引分析

| 索引名 | 类型 | 冗余? | 说明 |
|--------|------|-------|------|
| | | Y/N | |

## Schema 变更 SQL

```sql
-- 最终审查通过的 DDL:
CREATE TABLE ...
```

## 改进建议

1. [建议一]
2. [建议二]

---

## Revision History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | YYYY-MM-DD | Initial review | 评估团队 |
```

---

## 相关评估

- [query-performance-benchmark.md](../evaluations/query-performance-benchmark.md)
- [common-error-patterns.md](../evaluations/common-error-patterns.md)
- [code-quality-checklist.md](../evaluations/code-quality-checklist.md)
- [design-quality-assessment.md](../evaluations/design-quality-assessment.md)
