---
name: design-database
description: Detailed technical instructions for design-database scenario execution
type: instruction
version: "1.1.0"
stage: design-database
---

# Instructions: 数据库设计 (Design Database)

## 数据库选型规范

### 选型决策矩阵

| 场景 | 推荐数据库 | 原因 |
|------|------------|------|
| OLTP 核心业务 | MySQL/PostgreSQL | 事务支持、高并发 |
| OLAP 分析报表 | ClickHouse/Greenplum | 列式存储、压缩比高 |
| 文档存储 | MongoDB | 灵活 Schema |
| 缓存 | Redis | 内存存储、低延迟 |
| 全文搜索 | Elasticsearch | 倒排索引 |
| 时序数据 | InfluxDB/TimescaleDB | 时序优化 |

### MySQL vs PostgreSQL

| 特性 | MySQL | PostgreSQL |
|------|-------|------------|
| 事务 | 支持 | 支持 |
| 复杂查询 | 一般 | 优秀 |
| 扩展性 | 一般 | 优秀 |
| JSON 支持 | 5.7+ 支持 | 原生支持 |
| GIS 支持 | 需要插件 | 原生支持 |
| 复制 | 半同步/异步 | 同步/异步 |

## 命名规范

### 表命名

```yaml
# 表命名规范
naming_rules:
  table_name:
    pattern: "{module}_{entity}"
    example: "user_account", "order_item"
    plural: true

  column_name:
    pattern: "snake_case"
    example: "user_id", "created_at"

  index_name:
    pattern: "idx_{table}_{columns}"
    example: "idx_user_id_name"

  foreign_key:
    pattern: "fk_{table}_{ref_table}"
    example: "fk_order_user"
```

### 字段命名

```yaml
# 通用字段
common_fields:
  - name: "id"
    type: "bigint"
    pk: true

  - name: "created_at"
    type: "datetime"
    default: "CURRENT_TIMESTAMP"

  - name: "updated_at"
    type: "datetime"
    default: "ON UPDATE"

  - name: "created_by"
    type: "bigint"
    nullable: true

  - name: "deleted_at"
    type: "datetime"
    nullable: true
    description: "软删除时间"

# 业务字段示例
business_fields:
  user: ["username", "email", "mobile", "password_hash"]
  order: ["order_no", "user_id", "status", "total_amount"]
  product: ["name", "description", "price", "stock"]
```

## 范式设计规范

### 三大范式

```yaml
normalization:
  first_normal_form:
    rule: "原子性，每列不可再分"
    example: |
      # 错误
      address: "省市区详细地址"
      
      # 正确
      province: "省份"
      city: "城市"
      district: "区"
      detail: "详细地址"

  second_normal_form:
    rule: "非主键列完全依赖于主键"
    example: |
      # 错误：部分依赖
      order_item(order_id, product_id, product_name)
      
      # 正确：消除部分依赖
      order(order_id, ...)
      product(product_id, product_name, ...)
      order_item(order_id, product_id, ...)

  third_normal_form:
    rule: "非主键列之间不存在传递依赖"
    example: |
      # 错误：传递依赖
      user(id, name, department_id, department_name)
      
      # 正确：消除传递依赖
      department(id, name)
      user(id, name, department_id)
```

## 索引设计规范

### 索引类型

| 类型 | 适用场景 | 示例 |
|------|----------|------|
| 主键索引 | 唯一标识 | PRIMARY KEY |
| 唯一索引 | 唯一约束 | UNIQUE |
| 普通索引 | 查询加速 | INDEX |
| 联合索引 | 多字段查询 | INDEX(a,b,c) |
| 全文索引 | 文本搜索 | FULLTEXT |

### 联合索引设计

```yaml
# 联合索引设计原则
composite_index:
  order_matters:
    # 查询条件顺序
    query: "WHERE a=1 AND b=2 AND c=3"
    # 联合索引顺序
    index: "INDEX idx_abc (a, b, c)"
    reason: "最左前缀匹配"

  selectivity:
    high_selectivity_first:
      # 高选择性的列放前面
      index: "INDEX idx_status_user (status, user_id)"
      query: "WHERE status='active' AND user_id=123"

  covering_index:
    # 覆盖索引减少回表
    index: "INDEX idx_cover (user_id, name, email)"
    query: "SELECT name, email FROM users WHERE user_id=?"
    benefit: "无需回表查询"
```

### 索引注意事项

```sql
-- 不要在索引列上使用函数
-- 错误
SELECT * FROM orders WHERE YEAR(created_at) = 2024

-- 正确
SELECT * FROM orders WHERE created_at >= '2024-01-01' AND created_at < '2025-01-01'

-- 不要在索引列上进行计算
-- 错误
SELECT * FROM products WHERE price * 1.1 > 100

-- 正确
SELECT * FROM products WHERE price > 100 / 1.1

-- 避免前导通配符
-- 错误
SELECT * FROM users WHERE name LIKE '%张%'

-- 正确
SELECT * FROM users WHERE name LIKE '张%'
```

## 分区设计规范

### 分区类型

```yaml
partitioning:
  range_partition:
    use_case: "时间序列数据"
    example: |
      CREATE TABLE logs (
        id BIGINT,
        created_at DATETIME,
        ...
      )
      PARTITION BY RANGE (YEAR(created_at)) (
        PARTITION p2022 VALUES LESS THAN (2023),
        PARTITION p2023 VALUES LESS THAN (2024),
        PARTITION p2024 VALUES LESS THAN (2025),
        PARTITION pmax VALUES LESS THAN MAXVALUE
      )

  hash_partition:
    use_case: "均匀分布"
    example: |
      CREATE TABLE orders (
        id BIGINT,
        ...
      )
      PARTITION BY HASH(id)
      PARTITIONS 8

  list_partition:
    use_case: "枚举值"
    example: |
      CREATE TABLE products (
        id BIGINT,
        category VARCHAR(20),
        ...
      )
      PARTITION BY LIST COLUMNS(category) (
        PARTITION p_electronics VALUES IN ('electronics'),
        PARTITION p_clothing VALUES IN ('clothing'),
        PARTITION p_food VALUES IN ('food')
      )
```

## 分库分表规范

### 分片策略

```yaml
sharding:
  vertical_sharding:
    strategy: "按业务拆分"
    example: |
      # 用户库
      users_db
      # 订单库
      orders_db
      # 商品库
      products_db

  horizontal_sharding:
    strategies:
      - by_user_id:
          shard_key: "user_id"
          shard_count: 8
          algorithm: "hash(user_id) % 8"

      - by_time:
          shard_key: "created_at"
          strategy: "RANGE"
          example: "按月分表 orders_202401"

      - by_region:
          shard_key: "region_id"
          strategy: "LIST"
          example: "华东、华北、华南"
```

### 分片中间件选择

| 中间件 | 特点 | 适用场景 |
|--------|------|----------|
| ShardingSphere | 功能全面 | 通用场景 |
| MyCat | 配置简单 | MySQL |
| TiDB | 分布式原生 | NewSQL |
| Vitess | MySQL 协议兼容 | Kubernetes |

## 数据类型规范

### 数值类型

```yaml
numeric_types:
  tinyint: "TINYINT -128~127 或 0~255"
  smallint: "SMALLINT -32768~32767 或 0~65535"
  int: "INT -21亿~21亿"
  bigint: "BIGINT 适用于 ID"
  decimal: "DECIMAL(10,2) 精确小数"
  float: "FLOAT 浮点数"
  double: "DOUBLE 双精度浮点数"
```

### 字符串类型

```yaml
string_types:
  varchar:
    mysql: "VARCHAR(255) 可变长度"
    postgresql: "VARCHAR(255)"

  text:
    mysql: "TINYTEXT/TEXT/MEDIUMTEXT/LONGTEXT"
    postgresql: "TEXT"

  char:
    mysql: "CHAR(36) 固定长度 UUID"
    postgresql: "CHAR(36)"

  json:
    mysql: "JSON 类型"
    postgresql: "JSON/JSONB (推荐)"
```

### 日期时间类型

```yaml
datetime_types:
  datetime:
    mysql: "DATETIME 'YYYY-MM-DD HH:MM:SS'"
    postgresql: "TIMESTAMP"

  date: "日期 'YYYY-MM-DD'"
  time: "时间 'HH:MM:SS'"
  timestamp: "时间戳（带时区）"
```

## 约束设计规范

```sql
-- 主键约束
ALTER TABLE users ADD PRIMARY KEY (id);

-- 唯一约束
ALTER TABLE users ADD UNIQUE (email);
ALTER TABLE users ADD UNIQUE (uk_username, domain);

-- 外键约束
ALTER TABLE orders ADD CONSTRAINT fk_order_user
  FOREIGN KEY (user_id) REFERENCES users(id)
  ON DELETE CASCADE
  ON UPDATE CASCADE;

-- 检查约束
ALTER TABLE products ADD CONSTRAINT chk_price
  CHECK (price >= 0);

-- 默认值
ALTER TABLE users MODIFY COLUMN status TINYINT DEFAULT 1;

-- 非空约束
ALTER TABLE users MODIFY COLUMN username VARCHAR(50) NOT NULL;
```


## Overview

> High-level description of the design-database execution process.
>
> This instruction defines the technical approach, key activities, and success criteria for the design-database scenario.


## Technical Specifications

> Detailed technical requirements and implementation guidelines for design-database.

### Required Tools
- [List required tools and frameworks]

### Environment Requirements
- [List environment prerequisites]

### Configuration Parameters
- [List key configuration parameters]


## Best Practices

> Industry-standard best practices for design-database execution.

1. **Practice 1**: [Description]
2. **Practice 2**: [Description]
3. **Practice 3**: [Description]


## Error Handling

> Common error scenarios and resolution strategies for design-database.

### Error Category 1
**Symptom**: [Description]
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]

### Error Category 2
**Symptom**: [Description]
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]


## Quality Standards

> Acceptance criteria and quality gates for design-database deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | [Description] | [How to verify] |
| Standard 2 | [Description] | [How to verify] |
| Standard 3 | [Description] | [How to verify] |
