---
name: data-dictionary
type: deliverable-template
version: "1.0.0"
status: active
---

# 数据字典 模板

> 复制本模板到 `docs/` 对应路径，由 Agent 按 [standards/harness-engineering.md](../standards/harness-engineering.md) 填充。

## 元数据

- 项目: {project_name}
- 版本: {version}
- 作者: {author}
- 日期: {ISO8601}

## 正文

## 数据存储概览

- **数据库类型**: {MySQL / PostgreSQL / MongoDB / Redis / Elasticsearch}
- **数据库名称**: {database_name}
- **字符集**: {charset} (如: utf8mb4)
- **备份策略**: {备份方案描述}

## 实体关系总览

```
{ER图简述或引用, 描述主要实体间的关系}
```

## 数据表/集合清单

### {表名/集合名}

**描述**: {表/集合的业务含义}

**常规属性**:
- 存储引擎: {InnoDB / MongoDB / ...}
- 行数预估: {estimated_row_count}
- 数据量预估: {estimated_data_size}
- 分片策略: {sharding_strategy}

**字段定义**:

| 字段名 | 类型 | 长度 | 约束 | 必填 | 默认值 | 描述 |
|--------|------|------|------|------|--------|------|
| id | BIGINT | 20 | PRIMARY KEY, AUTO_INCREMENT | Y | - | 主键ID |
| {field_name} | {type} | {length} | {constraints} | Y/N | {default} | {description} |

**索引**:

| 索引名 | 字段 | 类型 | 唯一 | 描述 |
|--------|------|------|------|------|
| idx_{field} | {field} | BTREE | Y/N | {description} |

**关联关系**:

| 关联表 | 关联字段 | 关系类型 | 级联策略 |
|--------|----------|----------|----------|
| {related_table} | {field} -> {related_field} | 1:1 / 1:N / M:N | CASCADE/SET NULL/RESTRICT |

**示例数据**:

```json
{
  "id": 1,
  "field_name": "示例值"
}
```

### {表名/集合名}

**描述**: {表/集合的业务含义}

**字段定义**:

| 字段名 | 类型 | 长度 | 约束 | 必填 | 默认值 | 描述 |
|--------|------|------|------|------|--------|------|
| {field_name} | {type} | {length} | {constraints} | Y/N | {default} | {description} |

**索引**:

| 索引名 | 字段 | 类型 | 唯一 | 描述 |
|--------|------|------|------|------|
| {index_name} | {field} | BTREE | Y/N | {description} |

**关联关系**:

| 关联表 | 关联字段 | 关系类型 | 级联策略 |
|--------|----------|----------|----------|
| {related_table} | {field} -> {related_field} | 1:1 / 1:N / M:N | CASCADE/SET NULL/RESTRICT |

## 重要查询模式

| 查询模式 | 涉及表 | SQL/操作示例 | 执行频率 | 优化建议 |
|----------|--------|--------------|----------|----------|
| {query_pattern} | {tables} | {sql_example} | {frequency} | {optimization} |

## 数据归档策略

- **归档周期**: {archive_cycle}
- **归档方式**: {archive_method}
- **清理策略**: {cleanup_strategy}

## 修订历史

| 版本 | 日期 | 作者 | 变更内容 | 评审人 |
|------|------|------|----------|--------|
| v1.0 | {ISO8601} | {author} | 初稿 | {reviewer} |

## 验证

- [ ] 已通过 [evaluations/output-validation-checklist.md](../evaluations/output-validation-checklist.md)
