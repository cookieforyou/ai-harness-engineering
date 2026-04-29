# Skill: 数据库设计 (Database Design)

## 概述

本 Skill 定义了数据库设计的核心知识体系。

## 核心知识

### 数据建模方法

#### ER 模型

```python
class Entity:
    """实体"""

    def __init__(self, name, attributes, primary_key):
        self.name = name
        self.attributes = attributes
        self.primary_key = primary_key

    def get_columns(self):
        return [
            Column(name, type, nullable)
            for name, type, nullable in self.attributes
        ]


class Relationship:
    """关系"""

    def __init__(self, from_entity, to_entity, cardinality):
        self.from_entity = from_entity
        self.to_entity = to_entity
        # cardinality: "1:1", "1:N", "N:M"
        self.cardinality = cardinality

    def resolve(self):
        """转换为物理模型"""
        if self.cardinality == "N:M":
            # 多对多需要中间表
            return self._create_junction_table()
        elif self.cardinality == "1:N":
            # 一对多添加外键
            return self._add_foreign_key()
        else:
            # 一对一可以合并或外键
            return self._add_foreign_key()
```

### 分布式 ID 生成

```python
class IDGenerator:
    """分布式 ID 生成器"""

    # Snowflake 算法
    def snowflake(self, worker_id=1, datacenter_id=1):
        """
        Snowflake ID 结构:
        - 1 bit: 符号位
        - 41 bits: 时间戳
        - 10 bits: 工作机器 ID
        - 12 bits: 序列号
        """
        timestamp = self._current_timestamp()
        sequence = self._next_sequence()

        return (
            (timestamp - self.EPOCH) << 22 |
            datacenter_id << 17 |
            worker_id << 12 |
            sequence
        )

    # UUID 算法
    def uuid_v1(self):
        """时间序列 UUID"""
        import uuid
        return uuid.uuid1()

    def uuid_v4(self):
        """随机 UUID"""
        import uuid
        return uuid.uuid4()


class ShardingStrategy:
    """分片策略"""

    def hash_sharding(self, user_id, shard_count=8):
        """哈希分片"""
        return user_id % shard_count

    def range_sharding(self, created_at, ranges):
        """范围分片"""
        for range_name, (start, end) in ranges.items():
            if start <= created_at < end:
                return range_name
        return "default"
```

### SQL 优化

```python
class SQLOptimizer:
    """SQL 优化器"""

    def analyze_query(self, sql):
        """分析查询"""
        # 使用 EXPLAIN 分析执行计划
        explain_plan = self.db.execute(f"EXPLAIN {sql}")

        # 检查问题
        issues = []

        if "ALL" in explain_plan.type:
            issues.append("全表扫描")

        if explain_plan.rows > 10000:
            issues.append("扫描行数过多")

        if explain_plan.extra and "Using filesort" in explain_plan.extra:
            issues.append("文件排序")

        if explain_plan.extra and "Using temporary" in explain_plan.extra:
            issues.append("临时表")

        return issues

    def optimize(self, sql):
        """优化 SQL"""
        issues = self.analyze_query(sql)

        for issue in issues:
            if issue == "全表扫描":
                return self._add_index(sql)
            elif issue == "扫描行数过多":
                return self._limit_query(sql)
            elif issue == "文件排序":
                return self._avoid_sort(sql)

        return sql
```

### 数据库调优参数

```yaml
# MySQL 调优参数
mysql_tuning:
  innodb_buffer_pool_size: "设置为你可用内存的 70-80%"
  innodb_log_file_size: "256M - 1G"
  innodb_flush_log_at_trx_commit: "1 (安全) / 2 (性能)"
  max_connections: "根据业务需求设置"
  slow_query_log: "开启"
  long_query_time: "1 秒"

# PostgreSQL 调优参数
postgres_tuning:
  shared_buffers: "设置为你可用内存的 25%"
  effective_cache_size: "设置为你可用内存的 75%"
  maintenance_work_mem: "1-4 GB"
  max_connections: "根据业务需求设置"
  work_mem: "根据查询复杂度设置"
```

## 最佳实践

### 表设计原则

1. **适度冗余**
   - 读多写少场景可适当冗余
   - 注意数据一致性维护

2. **避免宽表**
   - 单表字段不宜过多
   - 控制在 50 个字段以内

3. **冷热分离**
   - 热点数据放高速存储
   - 历史数据归档到冷存储

4. **时间分区**
   - 按时间分区的表定期归档
   - 控制单分区数据量

### 索引设计原则

1. **不要滥用索引**
   - 每个索引占用磁盘空间
   - DML 操作需要维护索引

2. **遵循最左前缀**
   - 联合索引 (a, b, c) 可加速 (a), (a, b), (a, b, c) 查询

3. **覆盖索引优先**
   - SELECT 的字段都在索引中
   - 避免回表查询

## 工具链

### 数据库设计工具

| 工具 | 用途 |
|------|------|
| PowerDesigner | ER 建模 |
| Navicat | 数据库管理 |
| DBeaver | 数据库客户端 |
| dbdiagram.io | 在线 ER 图 |

### 数据库管理工具

| 工具 | 用途 |
|------|------|
| pt-online-schema-change | 在线表结构变更 |
| gh-ost | GitHub 在线Schema变更 |
| mysqldumpslow | 慢查询分析 |
| pt-query-digest | 查询分析 |

## 关联资产

- **Scenario**: `../../scenarios/design-database/SCENARIO.md`
- **Instruction**: `../../instructions/design-database.instructions.md`
- **Prompt**: `../../prompts/design-database.prompt.md`
- **Agent**: `../../agents/database-architect.agent.md`
