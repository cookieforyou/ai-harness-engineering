---
name: query-performance-benchmark
type: evaluation
version: "1.1.0"
status: active
updated: 2026-06-23
description: >
  查询性能基准评估，基于SQL响应时间分级(S≤10ms/A≤100ms/B≤1s/C>1s)、
  EXPLAIN计划审查和索引命中率分析。提供慢查询阈值、优化建议模板
  和索引设计最佳实践，保障数据库查询性能持续符合SLA要求。
---

# 查询性能基准评估 (Query Performance Benchmark Evaluation)

## Overview

查询性能基准评估用于系统化地评估和优化数据库查询性能，通过响应时间分级、执行计划审查和索引使用分析，识别慢查询并提供优化建议。适用于数据库查询的性能基线建立、代码审查和线上问题排查。

### 适用场景

- 代码审查阶段的 SQL 查询性能预检
- 线上慢查询的根因分析和优化
- 数据库 Schema 变更前的性能影响评估
- 新服务上线前的数据库查询性能基线建立

---

## Evaluation Criteria

| 维度 | 权重 | 目标值 | 测量方法 |
|------|------|--------|----------|
| 响应时间分级 (Latency Grade) | 35% | S级 ≥ 80%, C级 < 1% | 慢查询日志/APM 响应时间分布 |
| EXPLAIN 计划审查 | 25% | ALL/Index Merge 扫描 < 5% | EXPLAIN ANALYZE 执行计划分析 |
| 索引命中率 (Index Hit) | 25% | 命中率 ≥ 99% | PG pg_stat_user_tables / MySQL 索引统计 |
| 慢查询治理 (Slow Query) | 15% | 慢查询数 ≤ 5条/天 | 慢查询日志聚合 |

### 响应时间分级标准

| 等级 | 响应时间 | 占比目标 | 治理策略 |
|------|----------|----------|----------|
| S (Fast) | ≤ 10ms | ≥ 80% | 无需关注，维持即可 |
| A (Acceptable) | 10ms - 100ms | ≤ 18% | Code Review 关注，必要时优化 |
| B (Degraded) | 100ms - 1s | ≤ 2% | 必须分析原因并制定优化计划 |
| C (Critical) | > 1s | < 1% | 立即创建慢查询优化任务 |

---

## Scoring Formula

```
响应时间得分 = (S级占比 × 100 + A级占比 × 70 + B级占比 × 30 + C级占比 × 0) / 100
  若 S级 ≥ 80% 且 C级 < 1% 则加 10 分

EXPLAIN得分 = max(0, 100 - ALL扫描占比 × 500)   // 全表扫描每1%扣5分
索引得分 = 索引命中率 × 100
慢查询得分 = max(0, 100 - 日均慢查询数 × 5)     // 每条慢查询扣5分

总分 = 响应时间得分 × 35% + EXPLAIN得分 × 25% + 索引得分 × 25% + 慢查询得分 × 15%
```

### 等级划分

| 等级 | 分数范围 | 判定 |
|------|----------|------|
| S (Excellent) | ≥ 90 | 查询性能优秀，无治理需求 |
| A (Good) | 80-89 | 少量优化空间，纳入定期维护 |
| B (Fair) | 70-79 | 存在明显性能问题，需专项治理 |
| F (Failed) | < 70 | 查询性能严重不达标，禁止上线 |

---

## Checklist

### 1. 响应时间分布检查 (5项)

- [ ] **QPB-LAT-001**: S 级查询（≤ 10ms）占总查询量的 ≥ 80%
- [ ] **QPB-LAT-002**: C 级查询（> 1s）占总查询量的 < 1%，无 10s+ 查询
- [ ] **QPB-LAT-003**: 慢查询日志已开启（MySQL slow_query_log / PG log_min_duration_statement = 1s）
- [ ] **QPB-LAT-004**: 周级慢查询趋势稳定或下降，无突发增长
- [ ] **QPB-LAT-005**: 前 N（N ≤ 3）个耗时最高的查询已有优化计划

### 2. EXPLAIN 计划审查 (6项)

- [ ] **QPB-EXP-001**: 查询执行计划无 `ALL`（全表扫描），或仅限小表（< 1000 行）
- [ ] **QPB-EXP-002**: 查询行估计值与实际行数偏差 ≤ 5 倍（统计信息准确性）
- [ ] **QPB-EXP-003**: `Extra` 列无 `Using filesort` 或 `Using temporary`（MySQL），或 Sort Method 未使用磁盘（PG）
- [ ] **QPB-EXP-004**: JOIN 操作使用 `Nested Loop` 或 `Hash Join`，无 `Block Nested Loop`（BNL）
- [ ] **QPB-EXP-005**: 使用 `EXPLAIN ANALYZE` 而非 `EXPLAIN`（获得实际执行时间），对线上只使用 `EXPLAIN`
- [ ] **QPB-EXP-006**: WHERE 条件列和 JOIN 列的数据类型一致，避免隐式类型转换

### 3. 索引命中率检查 (6项)

- [ ] **QPB-IDX-001**: 索引命中率 ≥ 99%（MySQL: `rows_examined / rows_sent` ≤ 3）
- [ ] **QPB-IDX-002**: 复合索引遵循最左前缀原则，查询条件覆盖索引前导列
- [ ] **QPB-IDX-003**: 无冗余索引（相同前导列的索引数 ≤ 2 个），定期清理未使用索引
- [ ] **QPB-IDX-004**: 索引覆盖查询列（Covering Index），避免回表查询
- [ ] **QPB-IDX-005**: 表的数据量 > 10 万行时全表扫描查询创建了对应的索引
- [ ] **QPB-IDX-006**: 索引维护计划（重建/整理）已配置，碎片率 ≤ 30%

### 4. 慢查询治理检查 (5项)

- [ ] **QPB-SQL-001**: 慢查询日志中每天的慢查询数 ≤ 5 条
- [ ] **QPB-SQL-002**: 每条慢查询有根因分析标签（N+1/缺少索引/数据量增长/锁争用）
- [ ] **QPB-SQL-003**: 慢查询优化后有验证步骤（重新 EXPLAIN + 再测试）
- [ ] **QPB-SQL-004**: ORM 生成的 SQL 与慢查询日志对齐（ORM 配置中启用 SQL 日志）
- [ ] **QPB-SQL-005**: 慢查询 Task/Bug 有负责人和预期完成日期，P0 慢查询 3 天内修复

---

## 优化建议模板

```sql
-- 优化前
SELECT * FROM orders WHERE status = 'PENDING' AND created_at > NOW() - INTERVAL 30 DAY;

-- EXPLAIN 分析: 全表扫描 (ALL), 预计扫描 500K 行
-- 优化建议:
-- 1. 添加复合索引: CREATE INDEX idx_orders_status_created ON orders(status, created_at);
-- 2. 避免 SELECT *，只选取必要列
-- 3. 若条件值分布不均匀，考虑使用覆盖索引

-- 优化后
SELECT id, user_id, amount, status FROM orders
WHERE status = 'PENDING' AND created_at > NOW() - INTERVAL 30 DAY;
```

---

## Report Template

```markdown
# 查询性能基准评估报告

## 概要

| 项目 | 值 |
|------|-----|
| 评估对象 | [数据库实例/数据源] |
| 评估日期 | YYYY-MM-DD |
| 数据库类型 | [MySQL 8.0 / PostgreSQL 15 / ...] |
| 总查询量 (日均) | [N] |
| 综合评分 | [XX.X] 分 / 100 |
| 等级判定 | [S/A/B/F] |

## 响应时间分布

| 等级 | 响应时间范围 | 占比 | 目标 | 达标 |
|------|-------------|------|------|------|
| S | ≤ 10ms | XX.X% | ≥ 80% | Y/N |
| A | 10ms - 100ms | XX.X% | ≤ 18% | Y/N |
| B | 100ms - 1s | XX.X% | ≤ 2% | Y/N |
| C | > 1s | XX.X% | < 1% | Y/N |

## Top 5 慢查询

| 排名 | 查询指纹 | 平均耗时 | 次数/天 | 扫描行数 | 根因 | 优化建议 |
|------|----------|----------|---------|----------|------|----------|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |

## 索引分析

| 指标 | 实际值 | 目标值 | 达标 |
|------|--------|--------|------|
| 索引命中率 | XX.X% | ≥ 99% | Y/N |
| 未使用索引数 | N | ≤ 2 | Y/N |
| 冗余索引数 | N | ≤ 2 | Y/N |
| 碎片率 | XX% | ≤ 30% | Y/N |

## 改进跟踪

| # | 查询 | 问题 | 优先级 | 责任人 | 计划完成 | 状态 |
|---|------|------|--------|--------|----------|------|
| 1 | | | | | | |

---

## Revision History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | YYYY-MM-DD | Initial report | 评估团队 |
```

---

## 相关评估

- [performance-baseline.md](../evaluations/performance-baseline.md)
- [response-time-analysis.md](../evaluations/response-time-analysis.md)
- [schema-review-checklist.md](../evaluations/schema-review-checklist.md)
- [slo-compliance.md](../evaluations/slo-compliance.md)
