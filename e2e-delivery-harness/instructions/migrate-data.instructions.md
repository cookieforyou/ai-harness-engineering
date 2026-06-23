---
name: migrate-data
description: "Detailed technical instructions for migrate-data scenario execution"
applyTo: "scenarios/migrate-data/**"
phase: operations
type: instruction
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-23
status: active
language: "zh-CN"
tags: ['instruction', 'technical']
---
# Instruction: 数据迁移技术规范

## Overview

This instruction defines the technical standards and execution procedures for data migration projects within the E2E delivery lifecycle. It covers migration strategy selection (big-bang vs. incremental vs. synchronization), ETL pipeline design, data quality validation techniques, zero-downtime migration patterns, and rollback strategies. The instruction ensures data integrity is preserved throughout migration, downstream consumers are properly notified and validated, and business continuity is maintained. Key focus areas include consistency checks, reconciliation procedures, and performance optimization for large-scale data movements.

## Migration Strategy Comparison

| 策略 | 描述 | 优点 | 缺点 | 适用场景 | 停机时间 | 复杂度 |
|------|------|------|------|----------|----------|--------|
| **BIG_BANG** | 一次性全量迁移所有数据 | 实施简单、速度快 | 停机时间长、风险集中 | 小数据量（<100GB）、允许停机窗口 | 高 | 低 |
| **PARALLEL** | 新旧系统并行运行，双写同步 | 风险低、可随时回滚 | 成本高、需双写逻辑 | 关键业务系统、需零风险 | 低（近零） | 高 |
| **PHASE** | 分阶段迁移，按表或按业务域分批 | 灵活可控、风险分散 | 周期长、数据一致性难保证 | 大数据量（>100GB）、复杂迁移 | 中 | 中 |
| **CDC** | 使用变更数据捕获持续同步 | 近乎零停机、实时性高 | 需CDC工具、运维复杂 | 需持续同步、零停机要求 | 极低 | 高 |

### 迁移策略选择矩阵

```
数据量 \ 停机容忍度 | 允许停机  | 受限停机  | 零停机
-------------------|-----------|-----------|--------
< 100GB            | BIG_BANG  | BIG_BANG  | CDC
100GB ~ 1TB        | PHASE     | PHASE     | CDC
> 1TB              | PHASE     | CDC       | CDC
```

## Concrete CLI Commands

### MySQL Migration

```bash
# 全量导出
mysqldump -h source_host -u user -p --single-transaction --routines --triggers \
  --quick --max-allowed-packet=1G db_name > db_dump.sql

# 分批导出（大表使用 WHERE 分片）
mysqldump -h source_host -u user -p --single-transaction --where="id BETWEEN 1 AND 1000000" \
  db_name orders > orders_part1.sql

# 导入目标库
mysql -h target_host -u user -p db_name < db_dump.sql

# 禁用外键检查加速导入
mysql -h target_host -u user -p -e "SET FOREIGN_KEY_CHECKS=0; SET UNIQUE_CHECKS=0;" db_name

# 行数校验
mysql -h source_host -u user -p -e "SELECT table_name, table_rows FROM information_schema.tables WHERE table_schema='db_name'"
mysql -h target_host -u user -p -e "SELECT table_name, table_rows FROM information_schema.tables WHERE table_schema='db_name'"

# 校验和计算
mysql -h source_host -u user -p -e "SELECT SUM(CRC32(CONCAT_WS(',', id, name, email, created_at))) AS checksum FROM users"
mysql -h target_host -u user -p -e "SELECT SUM(CRC32(CONCAT_WS(',', id, name, email, created_at))) AS checksum FROM users"
```

### PostgreSQL Migration

```bash
# 全量导出
pg_dump -h source_host -U user -d db_name --format=custom --compress=9 > db_dump.dump

# 大数据量表分批导出
pg_dump -h source_host -U user -d db_name --table=orders --exclude-table-data='!orders_*' \
  --rows-per-insert=10000 > orders.sql

# 导入目标库
pg_restore -h target_host -U user -d db_name --jobs=4 db_dump.dump

# 或使用 COPY 命令加速
psql -h target_host -U user -d db_name -c "\COPY source_table FROM 'export.csv' WITH CSV"

# 行数校验
psql -h source_host -U user -d db_name -c "SELECT relname, n_live_tup FROM pg_stat_user_tables ORDER BY relname;"
psql -h target_host -U user -d db_name -c "SELECT relname, n_live_tup FROM pg_stat_user_tables ORDER BY relname;"

# 校验和计算
psql -h source_host -U user -d db_name -c "SELECT sum(('x' || substr(md5(concat_ws(',', id::text, name, email, created_at::text)), 1, 8))::bit(32)::bigint) AS checksum FROM users"
```

### MongoDB Migration

```bash
# 全量导出
mongodump --host source_host --port 27017 --db db_name --out ./dump_dir

# 集合级导出（含查询过滤）
mongodump --host source_host --port 27017 --db db_name --collection orders \
  --query '{"created_at": {"$gte": ISODate("2024-01-01")}}' --out ./dump_dir

# 导入目标库
mongorestore --host target_host --port 27017 --db db_name --drop ./dump_dir/db_name

# 行数校验
mongosh --host source_host --quiet --eval "db.getSiblingDB('db_name').getCollectionNames().forEach(c => {print(c + ': ' + db[c].countDocuments())})"
mongosh --host target_host --quiet --eval "db.getSiblingDB('db_name').getCollectionNames().forEach(c => {print(c + ': ' + db[c].countDocuments())})"

# 使用 mongoexport/mongoimport 迁移特定集合
mongoexport --host source_host --db db_name --collection users --type csv --fields _id,name,email --out users.csv
mongoimport --host target_host --db db_name --collection users --type csv --fields _id,name,email --file users.csv
```

### Redis Migration

```bash
# 使用 redis-cli 迁移
redis-cli -h source_host -p 6379 --scan --pattern '*' | while read key; do
  redis-cli -h source_host -p 6379 DUMP "$key" | head -c -1 | \
    redis-cli -h target_host -p 6379 RESTORE "$key" 0 REPLACE
done

# 使用 redis-dump 工具（大数据量推荐）
pip install redis-dump
redis-dump -u redis://source_host:6379 -d 0 > dump.json
redis-load -u redis://target_host:6379 -d 0 < dump.json

# 使用 RDB 文件迁移（最佳方式）
# 1. 在源 Redis 执行 BGSAVE 生成 dump.rdb
redis-cli -h source_host BGSAVE
# 2. 将 dump.rdb 复制到目标 Redis 服务器
# 3. 重启目标 Redis 加载新 RDB
```

### Dump/Restore 性能对比

| 数据库 | 导出速度 | 导入速度 | 最佳实践 |
|--------|----------|----------|----------|
| MySQL | ~100MB/s | ~50MB/s | 使用 --quick 和 --max-allowed-packet |
| PostgreSQL | ~150MB/s | ~80MB/s | 使用 --jobs=N 并行恢复 |
| MongoDB | ~80MB/s | ~60MB/s | 使用 --numParallelCollections=4 |
| Redis | ~200MB/s | ~100MB/s | 使用 RDB 文件传输 |

## ETL Pipeline Design Patterns

### 模式 1: Extract-Load-Transform (ELT)

```
源数据库 → 全量导出 → 原始数据加载到目标 → SQL转换 → 校验
```

**适用场景**: 目标系统处理能力强，数据转换逻辑简单
**优点**: 加载速度快，转换灵活
**缺点**: 目标系统需大量临时存储

### 模式 2: Extract-Transform-Load (ETL)

```
源数据库 → 数据抽取 → 中间层转换 → 加载到目标 → 校验
```

**适用场景**: 复杂数据转换、清洗需求
**优点**: 目标系统负载低，转换逻辑可控
**缺点**: 需要中间存储，整体速度较慢

### 模式 3: Change Data Capture (CDC)

```
源数据库 → Binlog/WAL → 解析器 → 转换 → 写入目标 → 校验
```

**适用场景**: 零停机迁移、持续同步
**常用工具**: Debezium + Kafka、Canal、Maxwell、AWS DMS
**优点**: 实时同步，不影响源系统
**缺点**: 运维复杂，需额外基础设施

### ETL 流水线配置示例

```yaml
etl_pipeline:
  source:
    type: mysql
    connection: "mysql://user:pass@source_host:3306/db_name"
    tables:
      - users
      - orders
    extract_mode: "incremental"   # full / incremental / cdc
    batch_size: 5000
    parallelism: 4

  transform:
    - type: column_mapping
      rules:
        - source: "created_at"
          target: "create_time"
          transform: "STRING_TO_DATE"
        - source: "email"
          target: "email"
          transform: "LOWER_TRIM"

    - type: data_clean
      rules:
        - remove_nulls: ["phone", "address"]
        - default_values:
            status: "active"

  target:
    type: tidb
    connection: "mysql://user:pass@target_host:4000/db_name"
    batch_insert_size: 2000
    pre_sql:
      - "SET FOREIGN_KEY_CHECKS = 0"
      - "SET UNIQUE_CHECKS = 0"
    post_sql:
      - "SET FOREIGN_KEY_CHECKS = 1"
      - "SET UNIQUE_CHECKS = 1"
      - "ANALYZE TABLE users, orders"

  error_handling:
    max_retries: 3
    retry_delay_seconds: 10
    error_log: "./etl_errors.log"
    on_error: "skip_and_log"     # skip_and_log / stop / retry

  scheduling:
    mode: "once"                 # once / cron / continuous
    start_time: "2024-01-15T02:00:00Z"
    timeout_minutes: 240
```

## Data Validation Methods

### 方法 1: 行数校验（Row Count）

```sql
-- 逐表对比行数
SELECT 'users' AS table_name, COUNT(*) AS source_count FROM source_db.users
UNION ALL
SELECT 'users', COUNT(*) AS target_count FROM target_db.users;

-- 批量校验（生成比较语句）
SELECT CONCAT(
  'SELECT "', table_name, '" AS tbl, ',
  '(SELECT COUNT(*) FROM source_db.', table_name, ') AS src, ',
  '(SELECT COUNT(*) FROM target_db.', table_name, ') AS tgt, ',
  'CASE WHEN (SELECT COUNT(*) FROM source_db.', table_name, ') = (SELECT COUNT(*) FROM target_db.', table_name, ') ',
  'THEN "PASS" ELSE "FAIL" END AS result'
) FROM information_schema.tables WHERE table_schema = 'source_db';
```

### 方法 2: 校验和校验（Checksum）

```sql
-- MySQL 校验和方法
SELECT 'users' AS table_name,
  SUM(CRC32(CONCAT_WS('|', id, name, email, created_at))) AS source_checksum
FROM source_db.users;

-- PostgreSQL 校验和方法
SELECT 'users' AS table_name,
  SUM(('x' || SUBSTRING(MD5(CONCAT_WS('|', id::TEXT, name, email, created_at::TEXT)), 1, 8))::BIT(32)::BIGINT) AS checksum
FROM source_db.users;

-- 分片校验和（大表分片计算）
SELECT CONCAT('users_shard_', FLOOR(id / 1000000)) AS shard,
  COUNT(*) AS row_count,
  SUM(CRC32(CONCAT_WS('|', id, name))) AS checksum
FROM users
GROUP BY FLOOR(id / 1000000);
```

### 方法 3: 抽样校验（Sampling）

```sql
-- 随机抽样 1000 条逐字段对比
WITH source_sample AS (
  SELECT * FROM source_db.users ORDER BY RAND() LIMIT 1000
),
target_sample AS (
  SELECT * FROM target_db.users ORDER BY RAND() LIMIT 1000
)
SELECT s.id,
  s.name AS src_name, t.name AS tgt_name,
  s.email AS src_email, t.email AS tgt_email,
  CASE WHEN s.name = t.name AND s.email = t.email THEN 'MATCH' ELSE 'MISMATCH' END AS status
FROM source_sample s
JOIN target_sample t ON s.id = t.id;

-- 边界值抽样（取最大最小值附近的数据）
SELECT * FROM users WHERE id IN (
  SELECT MIN(id) FROM users
  UNION ALL SELECT MAX(id) FROM users
  UNION ALL SELECT id FROM users ORDER BY id LIMIT 100
  UNION ALL SELECT id FROM users ORDER BY id DESC LIMIT 100
) ORDER BY id;
```

### 方法 4: 业务规则校验（Business Rule）

```sql
-- 参照完整性校验
SELECT 'orders(foreign_key: user_id)' AS check_name,
  COUNT(*) AS orphan_records
FROM target_db.orders o
LEFT JOIN target_db.users u ON o.user_id = u.id
WHERE u.id IS NULL;

-- 数据范围校验
SELECT 'orders(amount)' AS check_name,
  COUNT(*) AS out_of_range,
  MIN(amount), MAX(amount)
FROM target_db.orders
WHERE amount < 0 OR amount > 1000000;

-- 业务逻辑校验
SELECT 'users(create_time)' AS check_name,
  COUNT(*) AS future_dates
FROM target_db.users
WHERE created_at > NOW();

-- 唯一性校验
SELECT 'users(email)' AS check_name,
  COUNT(*) AS duplicate_count,
  email, COUNT(*) AS cnt
FROM target_db.users
GROUP BY email
HAVING COUNT(*) > 1;
```

### 校验级别选择指南

| 数据重要性 | 行数校验 | 校验和 | 抽样校验 | 业务规则 | 建议策略 |
|-----------|----------|--------|----------|----------|----------|
| 核心交易 | 100% | 100% | 100% | 100% | 全量四维校验 |
| 用户信息 | 100% | 100% | 10% | 100% | 行数+校验和+业务规则 |
| 配置数据 | 100% | - | 100% | 100% | 行数+全量抽样+业务规则 |
| 历史归档 | 100% | - | 1% | - | 仅行数校验 |

### 自动化校验脚本（Python）

```python
#!/usr/bin/env python3
"""数据一致性自动校验工具"""

import hashlib
import json
import time
from typing import Dict, List, Tuple
import pymysql
import psycopg2


class DataValidator:
    """跨数据库数据校验器"""

    def __init__(self, source_config: dict, target_config: dict):
        self.source_config = source_config
        self.target_config = target_config
        self.source_conn = None
        self.target_conn = None

    def connect(self):
        """建立数据库连接"""
        if self.source_config['type'] == 'mysql':
            self.source_conn = pymysql.connect(**self.source_config['params'])
        elif self.source_config['type'] == 'postgresql':
            self.source_conn = psycopg2.connect(**self.source_config['params'])

        if self.target_config['type'] == 'mysql':
            self.target_conn = pymysql.connect(**self.target_config['params'])
        elif self.target_config['type'] == 'postgresql':
            self.target_conn = psycopg2.connect(**self.target_config['params'])

    def close(self):
        if self.source_conn:
            self.source_conn.close()
        if self.target_conn:
            self.target_conn.close()

    def validate_row_count(self, table: str) -> Tuple[bool, int, int]:
        """行数校验"""
        with self.source_conn.cursor() as cur:
            cur.execute(f"SELECT COUNT(*) FROM {table}")
            source_count = cur.fetchone()[0]
        with self.target_conn.cursor() as cur:
            cur.execute(f"SELECT COUNT(*) FROM {table}")
            target_count = cur.fetchone()[0]
        return source_count == target_count, source_count, target_count

    def validate_checksum(self, table: str, columns: List[str]) -> Tuple[bool, str, str]:
        """校验和校验"""
        concat_expr = "CONCAT_WS('|', " + ", ".join(columns) + ")"
        checksum_expr = f"SUM(CRC32({concat_expr}))"

        with self.source_conn.cursor() as cur:
            cur.execute(f"SELECT {checksum_expr} FROM {table}")
            source_checksum = str(cur.fetchone()[0] or 0)

        with self.target_conn.cursor() as cur:
            cur.execute(f"SELECT {checksum_expr} FROM {table}")
            target_checksum = str(cur.fetchone()[0] or 0)

        return source_checksum == target_checksum, source_checksum, target_checksum

    def validate_sampling(self, table: str, columns: List[str], sample_size: int = 100) -> Dict:
        """抽样校验"""
        results = {'matched': 0, 'mismatched': 0, 'missing_in_target': 0, 'missing_in_source': 0, 'details': []}

        with self.source_conn.cursor() as cur:
            cur.execute(f"SELECT * FROM {table} ORDER BY RAND() LIMIT {sample_size}")
            source_rows = {row[0]: row for row in cur.fetchall()}

        with self.target_conn.cursor() as cur:
            for pk in source_rows.keys():
                cur.execute(f"SELECT * FROM {table} WHERE id = {pk}")
                target_row = cur.fetchone()
                if target_row:
                    if source_rows[pk] == target_row:
                        results['matched'] += 1
                    else:
                        results['mismatched'] += 1
                        results['details'].append({
                            'pk': pk,
                            'source': dict(zip(columns, source_rows[pk])),
                            'target': dict(zip(columns, target_row))
                        })
                else:
                    results['missing_in_target'] += 1

        return results

    def run_full_validation(self, tables: Dict[str, List[str]]) -> Dict:
        """执行全量校验流程"""
        start_time = time.time()
        results = {}

        for table, columns in tables.items():
            table_result = {'table': table}

            # 行数校验
            count_ok, src_count, tgt_count = self.validate_row_count(table)
            table_result['row_count'] = {
                'status': 'PASS' if count_ok else 'FAIL',
                'source': src_count,
                'target': tgt_count
            }

            # 校验和校验（跳过无校验字段的表）
            if len(columns) > 0:
                cs_ok, src_cs, tgt_cs = self.validate_checksum(table, columns)
                table_result['checksum'] = {
                    'status': 'PASS' if cs_ok else 'FAIL',
                    'source': src_cs,
                    'target': tgt_cs
                }

            # 抽样校验
            sampling = self.validate_sampling(table, columns, sample_size=200)
            integrity = (sampling['matched'] / max(
                sampling['matched'] + sampling['mismatched'] + sampling['missing_in_target'], 1)) * 100
            table_result['sampling'] = {
                'status': 'PASS' if integrity == 100 else 'FAIL',
                'integrity_pct': round(integrity, 2),
                **sampling
            }

            results[table] = table_result

        elapsed = time.time() - start_time
        return {
            'elapsed_seconds': round(elapsed, 2),
            'tables': results,
            'summary': self._compute_summary(results)
        }

    def _compute_summary(self, results: Dict) -> Dict:
        """计算汇总结果"""
        total = len(results)
        passed = sum(
            1 for r in results.values()
            if r.get('row_count', {}).get('status') == 'PASS'
            and r.get('checksum', {}).get('status') in ('PASS', None)
            and r.get('sampling', {}).get('status') == 'PASS'
        )
        return {
            'total_tables': total,
            'passed_tables': passed,
            'failed_tables': total - passed,
            'overall_status': 'PASS' if passed == total else 'FAIL',
            'data_integrity_pct': round((passed / total) * 100, 2) if total > 0 else 100
        }


# 使用示例
if __name__ == '__main__':
    validator = DataValidator(
        source_config={
            'type': 'mysql',
            'params': {'host': 'source_host', 'user': 'user', 'password': 'pass', 'database': 'source_db'}
        },
        target_config={
            'type': 'mysql',
            'params': {'host': 'target_host', 'user': 'user', 'password': 'pass', 'database': 'target_db'}
        }
    )

    validator.connect()
    results = validator.run_full_validation({
        'users': ['id', 'name', 'email', 'created_at'],
        'orders': ['id', 'user_id', 'amount', 'status', 'created_at'],
        'products': ['id', 'name', 'price', 'category_id'],
    })
    validator.close()

    print(json.dumps(results, indent=2, default=str))
```

## Rollback Procedures

### 回滚策略对比

| 策略 | 方法 | 回滚时间 | 数据完整性 | 复杂度 | 适用场景 |
|------|------|----------|------------|--------|----------|
| **Snapshot** | 迁移前创建快照，回滚时恢复 | 快 | 100% | 低 | 小数据量、虚拟机/云环境 |
| **DML Reverse** | 记录反向操作 SQL（INSERT ↔ DELETE, UPDATE ↔ UPDATE） | 中 | 取决于记录完整性 | 中 | 增量迁移 |
| **Parallel Run** | 新旧系统并行运行，切换回旧系统 | 快 | 100% | 高 | 关键系统 |
| **Log Replay** | 使用事务日志反向回滚 | 慢 | 99.9% | 高 | 大数据量 |

### 回滚方案模板

```yaml
rollback_plan:
  strategy: "snapshot"    # snapshot / dml-reverse / parallel-run / log-replay

  pre_conditions:
    - source_system_backup_completed: true
    - rollback_script_tested: true
    - business_approval_obtained: true

  steps:
    - step: 1
      action: "停止目标系统写入流量"
      command: "kubectl scale deployment target-app --replicas=0"
      estimated_time: "1 min"
      validation: "确认目标系统无连接"

    - step: 2
      action: "恢复源系统（从快照）"
      command: "kubectl rollout undo deployment/source-app"
      estimated_time: "5 min"
      validation: "SELECT COUNT(*) FROM source_db.users"

    - step: 3
      action: "验证源系统数据完整性"
      command: "python validate.py --rollback-check"
      estimated_time: "15 min"
      validation: "所有数据校验通过"

    - step: 4
      action: "恢复业务流量到源系统"
      command: "kubectl scale deployment source-app --replicas=3"
      estimated_time: "1 min"
      validation: "业务监控指标正常"

  timing_estimate:
    total_estimated_minutes: 22
    window_available_minutes: 60
    buffer_minutes: 38
```

### 回滚触发条件

```yaml
rollback_triggers:
  critical:
    - "ANY 关键数据表 DATA-INTEGRITY < 100%"
    - "目标系统完全不可用 > 5 分钟"
    - "数据丢失确认"
    - "安全漏洞被发现"

  major:
    - "非关键表 DATA-INTEGRITY < 99.9%"
    - "迁移时间超过窗口 30%"
    - "错误率 > 1%"
    - "性能下降超过 50% 预期"

  auto_rollback:
    enabled: true
    conditions:
      - metric: "error_rate"
        threshold: 0.05
        duration: "30s"
      - metric: "data_integrity"
        threshold: 99.0
        tables: ["orders", "payments"]
```

## Cutover Window Planning

### 割接窗口检查清单

```markdown
## 割接前检查

### T-7天：准备阶段
- [ ] 迁移方案评审通过
- [ ] 回滚方案评审通过
- [ ] 数据量评估完成
- [ ] 资源需求评估完成（存储、网络带宽、计算资源）

### T-1天：预检查阶段
- [ ] 源系统备份完成
- [ ] 目标环境创建完成
- [ ] Schema 映射验证通过
- [ ] 网络连接测试通过
- [ ] 权限配置完成
- [ ] 监控告警配置完成
- [ ] 通知所有相关方

### T-0：割接当天
- [ ] 确认迁移窗口开始
- [ ] 确认无其他变更冲突
- [ ] 暂停非关键批处理任务
- [ ] 开启监控仪表盘
- [ ] 开始执行迁移

### 割接后
- [ ] 业务功能验证通过
- [ ] 性能指标正常
- [ ] 通知所有相关方
- [ ] 切换流量到目标系统
- [ ] 启动 24 小时监控
```

### 时间窗口估算公式

```
总迁移时间 = Σ(每表导出时间 + 传输时间 + 导入时间) + 校验时间 + 缓冲时间

单表导出时间 = 表数据量(MB) / 导出速度(MB/s)
单表传输时间 = 表数据量(MB) / 网络带宽(MB/s)
单表导入时间 = 表数据量(MB) / 导入速度(MB/s)
缓冲时间 = 总迁移时间 × 20%（安全余量）

总迁移时间 ≤ 迁移窗口
```

## Monitoring During Migration

### 实时监控指标

| 指标 | 采集方式 | 告警阈值 | 严重级别 |
|------|----------|----------|----------|
| 迁移进度（%） | 已处理行数/总行数 | < 预期进度 20% | Warning |
| 传输速率 (MB/s) | 定时统计 | < 预估 50% | Warning |
| 错误率 (%) | 失败记录/总记录 | > 0.1% | Critical |
| 数据校验差异 (%) | 即时校验 | > 0% | Critical |
| 源系统 CPU (%) | 系统指标 | > 80% | Warning |
| 目标系统 IOPS | 系统指标 | > 80% 上限 | Warning |

### 监控配置模板

```yaml
monitoring:
  enabled: true
  check_interval_seconds: 30

  metrics:
    - name: "migration_progress"
      query: "SELECT COUNT(*) FROM target_db.users / (SELECT COUNT(*) FROM source_db.users) * 100"
      threshold:
        warning: "current < expected - 20"
        critical: "current < expected - 50"

    - name: "transfer_rate"
      query: "每秒传输数据量(MB)"
      threshold:
        warning: "< expected_rate * 0.5"
        critical: "< expected_rate * 0.2"

    - name: "error_rate"
      query: "错误记录数 / 总处理记录数"
      threshold:
        warning: "> 0.001"
        critical: "> 0.01"

  alerts:
    - condition: "error_rate > 0.01"
      action: "pause_migration"
      notify: ["slack:#migration-alerts", "email:admin@company.com"]

    - condition: "migration_progress < expected - 30 for 5min"
      action: "notify_only"
      notify: ["slack:#migration-alerts"]

  dashboards:
    - name: "Data Migration Dashboard"
      panels:
        - "迁移进度概览"
        - "各表迁移速度"
        - "错误分布"
        - "资源使用率"
```

## Associated Assets

- **Scenario**: `scenarios/migrate-data/SCENARIO.md`
- **Prompt**: `prompts/migrate-data.prompt.md`
- **Agent**: `agents/migrate-data.agent.md`
- **Skill**: `skills/migrate-data/SKILL.md`

## 相关资产

- [traceability-mapping.md](../standards/traceability-mapping.md) — 跨资产可追溯性映射标准，定义迁移数据时的 DC/KPI 映射关系
- [health-check-guidelines.md](../standards/health-check-guidelines.md) — 迁移期间服务健康检查规范，配合零停机迁移策略
- [rollback-drill-report.md](../evaluations/rollback-drill-report.md) — 回滚演练评估报告，验证回滚策略的有效性
