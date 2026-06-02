---
name: design-database
description: "数据库设计场景，负责设计数据库架构、表结构、索引策略、分库分表方案等"
version: "1.2.0"
type: scenario
category: design
stage: database-design
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: [design, database, schema]
---
# Design Database Scenario

## Purpose

设计数据库架构，包括概念模型、逻辑模型、物理模型，以及表结构设计、索引设计、分库分表策略等，为数据存储和访问提供高效、可靠的基础设施。

### Business Value

- **数据一致性保障**: 通过规范化设计和约束机制确保数据完整性和一致性
- **查询性能优化**: 合理的索引设计和表结构优化提升查询效率
- **可扩展性设计**: 分库分表策略支持数据量增长，避免单点瓶颈
- **运维成本降低**: 标准化的Schema设计和文档化减少维护复杂度

## Chain of Thought (思维链)

### Think-Aloud Protocol (强制遵循)

```
[THINK] Step 1: 理解业务需求和数据特征
   ├─ 问：核心业务实体有哪些？数据访问模式是什么（OLTP/OLAP）？
   ├─ 验证：与领域模型对照，确认实体边界清晰
   └─ 检查：识别数据量级、增长趋势、读写比例
   ↓
[ANALYZE] Step 2: 分析数据需求和约束
   ├─ 问：一致性要求是强一致还是最终一致？可用性SLA是多少？
   ├─ 验证：评估数据类型选择、字符集、时区处理
   └─ 检查：识别合规要求（GDPR、PII）、安全约束
   ↓
[DESIGN] Step 3: 设计概念模型和逻辑模型
   ├─ 问：实体间关系如何建模？是否需要反范式化优化？
   ├─ 验证：ER图完整性检查，确保无遗漏实体或关系
   └─ 检查：达到第三范式（3NF），主键和外键定义清晰
   ↓
[EVALUATE] Step 4: 设计物理模型和优化策略
   ├─ 问：索引策略是否覆盖高频查询？是否需要分区或分片？
   ├─ 验证：执行计划分析，检查全表扫描风险
   └─ 检查：索引数量合理（≤5个/表），避免过度索引
   ↓
[DOCUMENT] Step 5: 输出数据库设计文档
   ├─ 生成ER图（概念模型、逻辑模型）
   ├─ 编写DDL脚本（CREATE TABLE语句）
   └─ 编写数据字典（表结构、字段说明、约束）
   ↓
[VALIDATE] Step 6: 评审确认并准备交接
   ├─ 组织数据库设计评审会议，收集反馈
   ├─ 根据反馈修订设计方案
   └─ 获得DBA签字确认，准备交接给开发阶段
```

## Decision Checkpoints (决策检查点)

| ID | 决策点 | 触发条件 | 决策选项 | 选择标准 | 记录位置 |
|----|--------|----------|----------|----------|----------|
| DC-001 | 数据库类型选择 | 分析数据特征后 | 关系型(MySQL/PG)/NoSQL(Mongo/Cassandra)/分布式(TiDB) | 基于数据结构化程度、事务需求、扩展性要求综合评估 | 技术选型文档 |
| DC-002 | 主键策略 | 设计每张表时 | 自然主键/代理主键(Auto Increment)/分布式ID(Snowflake/UUID) | 基于是否分布式、是否需要全局唯一、插入性能决定 | 表结构设计文档 |
| DC-003 | 索引策略 | 分析查询模式后 | B-Tree索引/哈希索引/全文索引/联合索引 | 基于查询条件分布、选择性、排序需求决定 | 索引设计文档 |
| DC-004 | 分库分表策略 | 预估数据量超过阈值 | 垂直拆分(按业务域)/水平拆分(按范围/哈希)/不分 | 单表>1000万行或单库>500GB时考虑分片 | 分库分表方案 |
| DC-005 | 一致性级别 | 设计跨表操作时 | 强一致性(事务)/最终一致性(异步补偿)/因果一致性 | 基于业务容忍度、性能要求、实现复杂度权衡 | ADR文档 |

## Error Handling (错误处理)

> **AI 在执行过程中遇到以下情况时的处理策略**

### Error Scenario 1: 数据不一致问题

**识别信号**: 
- 外键约束冲突或违反
- 重复数据出现
- 脏读、不可重复读、幻读现象

**处理流程**:
```
IF 检测到数据不一致
THEN
  1. 分析不一致的根本原因（并发写入、事务隔离级别、应用层逻辑错误）
  2. IF 并发问题 THEN 调整事务隔离级别或使用乐观锁/悲观锁
  3. IF 应用层错误 THEN 修复业务逻辑，添加数据校验
  4. 执行数据清洗，修复已存在的不一致数据
  5. 添加约束和触发器，防止未来出现类似问题
  6. 更新设计规范文档
END
```

**降级方案**: 暂时接受轻微不一致，通过定时任务进行数据对账和修复

**升级条件**: 经过2次调整后仍然存在严重数据不一致，需要DBA介入进行架构级调整

---

### Error Scenario 2: 查询性能不达标

**识别信号**: 
- 慢查询日志中出现大量超时查询（>1秒）
- EXPLAIN显示全表扫描或临时表
- CPU或IO使用率持续高负载

**处理流程**:
```
IF 检测到查询性能不达标
THEN
  1. 使用EXPLAIN分析慢查询的执行计划
  2. 识别性能瓶颈：全表扫描、未使用索引、JOIN过多、子查询嵌套
  3. IF 缺少索引 THEN 添加合适的索引（优先联合索引）
  4. IF SQL复杂 THEN 重构SQL，减少JOIN或拆分为多次查询
  5. IF 数据量大 THEN 考虑分区、分片或引入缓存层
  6. 重新测试查询性能，验证优化效果
  7. 更新索引设计文档
END
```

**降级方案**: 对非核心查询降低性能要求，或引入读写分离减轻主库压力

**升级条件**: 经过多轮优化仍无法满足P99延迟目标，需要重新评估架构设计（如引入搜索引擎、列式存储）

---

### Error Scenario 3: 容量预估不足导致扩容困难

**识别信号**: 
- 磁盘使用率超过80%
- 单表行数超过1000万，性能明显下降
- 备份时间过长影响业务

**处理流程**:
```
IF 检测到容量预警
THEN
  1. 评估当前数据量和增长速度
  2. IF 单表过大 THEN 实施水平分表（按时间范围或哈希）
  3. IF 单库过大 THEN 实施垂直分库（按业务域）或水平分库
  4. 制定数据归档策略，将冷数据迁移到廉价存储
  5. 执行在线迁移，确保业务不中断
  6. 更新容量规划文档
END
```

**降级方案**: 临时增加存储空间，同时启动分库分表方案设计

**升级条件**: 无法在线扩容，需要停机维护，需协调业务窗口期

## Quality Metrics (质量指标)

### Key Performance Indicators (KPIs)

| KPI ID | 指标名称 | 目标值 | 计算公式 | 验证方法 | 权重 |
|--------|----------|--------|----------|----------|------|
| KPI-001 | NORMALIZATION | 3NF | 所有表达到第三范式 | Schema审查 | 20% |
| KPI-002 | INDEX-COVERAGE | ≥90% | (有索引的高频查询数/总高频查询数) × 100% | 查询模式分析 | 25% |
| KPI-003 | SCHEMA-DOCS | 100% | (有注释的字段数/总字段数) × 100% | 数据字典检查 | 20% |
| KPI-004 | QUERY-PERF | P99<500ms | 99%查询响应时间<500ms | 性能基准测试 | 20% |
| KPI-005 | CONSTRAINT-INTEGRITY | 100% | (有约束的表数/总表数) × 100% | 约束检查清单 | 15% |

**综合评分计算**: 
```
Quality Score = (KPI-001 × 0.20) + (KPI-002 × 0.25) + (KPI-003 × 0.20) + (KPI-004 × 0.20) + (KPI-005 × 0.15)
合格: ≥70分 | 优秀: ≥85分 | 卓越: ≥95分
```

### Validation Checklist (验证清单)

**完整性验证 (Completeness)**:
- [ ] ER图包含所有核心实体和关系
- [ ] DDL脚本可执行，无语法错误
- [ ] 数据字典覆盖所有表和字段
- [ ] 索引设计文档完整

**一致性验证 (Consistency)**:
- [ ] 命名规范统一（表名、字段名、索引名）
- [ ] 数据类型选择一致（如时间统一用DATETIME）
- [ ] 外键引用关系正确，无循环依赖

**准确性验证 (Accuracy)**:
- [ ] 主键唯一且非空
- [ ] 外键引用存在的表和字段
- [ ] 默认值和约束符合业务逻辑
- [ ] 字符集和排序规则正确

**性能验证 (Performance)**:
- [ ] 高频查询有索引覆盖
- [ ] 无N+1查询问题
- [ ] JOIN表数量合理（≤5个）
- [ ] 大字段（TEXT/BLOB）单独存储

**规范性验证 (Compliance)**:
- [ ] 遵循数据库设计规范（如不使用保留字）
- [ ] 敏感字段加密存储
- [ ] 符合GDPR等合规要求
- [ ] 审计字段齐全（created_at, updated_at, deleted_at）


## Handover Criteria

```
✅ 所有必需交付物已生成并通过 Output Validation
✅ 质量评分达到合格标准（≥70 分）
✅ 决策点 DC-* 已记录 rationale
✅ 开放问题与风险已写入 Handover
✅ Handover Context YAML 已生成
```

### Handover Context Template

```yaml
handover:
  header:
    from_stage: "system-design"
    to_stage: "implement-feature"
    handover_id: "HO-{timestamp}-{sequence}"
    timestamp: "{ISO8601}"
    prepared_by: "design-database"
  summary:
    status: completed|partial|blocked
    quality_score: {0-100}
  artifacts:
    delivered: []
  decisions: []
  open_issues:
    blocking: []
    non_blocking: []
  risks: []
  quality_metrics:
    kpi_results: []
  recommendations: []
```

## Related Assets (关联资产)

| Asset Type | Path | Description |
|------------|------|-------------|
| Agent | `../../agents/design-database.agent.md` | 数据库设计Agent角色定义 |
| Prompt | `../../prompts/design-database.prompt.md` | 数据库设计提示词模板 |
| Skill | `../../skills/design-database/SKILL.md` | 数据库设计技能包 |
| Instruction | `../../instructions/design-database.instructions.md` | 数据库设计技术指令 |

## Related Resources (相关资源)

- **Standards**: 
  - [Database Naming Convention](../../standards/database-naming-convention.md) - 数据库命名规范
  - [Normalization Guidelines](../../standards/normalization-guidelines.md) - 数据库规范化指南
- **Templates**: 
  - [ER Diagram Template](../../templates/er-diagram.template.md) - ER图模板
  - [Data Dictionary Template](../../templates/data-dictionary.template.md) - 数据字典模板
- **Evaluations**: 
  - [Schema Review Checklist](../../evaluations/schema-review-checklist.md) - Schema评审检查清单
  - [Query Performance Benchmark](../../evaluations/query-performance-benchmark.md) - 查询性能基准测试
