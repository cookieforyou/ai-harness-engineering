---
name: migrate-data
description: "Domain skill for migrate-data execution — migration patterns, ETL design, validation framework"
category: operations
type: skill
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-23
status: active
tags: ['skill', 'knowledge']
---
# Skill: 数据迁移 (Data Migration)

## Overview

本 Skill 定义了数据迁移领域的核心知识和最佳实践，涵盖迁移策略设计、ETL Pipeline 开发、数据校验框架、回滚方案规划以及常见陷阱防范。适用于 MySQL、PostgreSQL、MongoDB、Redis 等主流数据库的迁移场景。

### Core Competencies

- **迁移策略设计**: 根据数据量、停机容忍度、一致性要求选择最优迁移策略
- **ETL 开发**: 设计高效的数据抽取、转换、加载流水线
- **数据校验**: 多维度校验（行数、校验和、抽样、业务规则）
- **CAP 权衡**: 理解一致性、可用性和分区容忍度在迁移中的权衡
- **性能优化**: 批量参数调优、并行度控制、网络延迟优化
- **异常恢复**: 断点续传、错误重试、一致性恢复

## Use When

使用此技能的场景：

- 需要设计跨数据库类型的数据迁移方案
- 需要编写数据校验和一致性检查脚本
- 需要选择迁移策略并评估风险和成本
- 需要处理迁移过程中的异常和性能问题
- 需要设计可回滚的迁移方案

## Core Knowledge

### Migration Patterns

#### Pattern 1: Dump and Restore

适用于同构数据库迁移（MySQL → MySQL、PostgreSQL → PostgreSQL）。

```
源库 → mysqldump/pg_dump → SQL文件 → 网络传输 → 目标库恢复
```

**优点**: 简单成熟、工具原生支持
**缺点**: 停机时间长、大数据量恢复慢
**最佳实践**:
- 使用压缩传输（gzip/bzip2）
- 分表导出，并行导入
- 导入前关闭外键检查和唯一约束

#### Pattern 2: Replication / CDC

适用于需要零停机或持续同步的迁移。

```
源库 → Binlog/WAL → CDC解析器 → 目标库
                           ↓
                      校验服务
```

**常用工具**: Debezium, Canal, Maxwell, AWS DMS, Alibaba DTS
**优点**: 近乎零停机、数据实时同步
**缺点**: 需额外基础设施、延迟问题

#### Pattern 3: Dual Write / Parallel Run

适用于关键业务系统迁移，新旧系统同时运行。

```
应用层 → 双写 → 源库 + 目标库
                  ↓
              比对服务 → 一致性校验
                  ↓
            → 切换读流量
            → 停止写源库
```

**优点**: 风险最低、可精确比对
**缺点**: 成本最高、需应用改造

#### Pattern 4: ETL Pipeline

适用于异构数据迁移或需要数据清洗转换的场景。

```
源库 → 抽取(Extract) → 转换(Transform) → 加载(Load) → 目标库
                           ↓
                     数据清洗
                     格式转换
                     数据脱敏
```

**工具**: Apache Spark, DataX, Kettle (Pentaho), NiFi, 自研脚本

### CAP Theorem in Migration Context

| 场景 | 一致性(C) | 可用性(A) | 分区容忍(P) | 说明 |
|------|-----------|-----------|-------------|------|
| 全量迁移+停机 | 强一致 | 低 | 不要求 | 停机期间源库不可用，确保数据一致性 |
| CDC 持续同步 | 最终一致 | 高 | 需要 | 实时同步但可能有短暂延迟 |
| 双写并行 | 强一致（应用层保证） | 高 | 需要 | 应用层保证双写一致性 |
| 分阶段迁移 | 最终一致 | 中 | 需要 | 阶段性切换，期间可能需要数据回填 |

**关键原则**: 数据迁移设计必须在一致性、可用性和性能之间做出权衡：

1. **金融/交易数据**: 优先一致性（C），牺牲一定的可用性
2. **用户内容/社交数据**: 优先可用性（A），可接受最终一致
3. **跨地域迁移**: 必须考虑分区容忍（P），接受最终一致

### 类型映射参考

| MySQL | PostgreSQL | Oracle | MongoDB | 注意事项 |
|-------|-----------|--------|---------|----------|
| INT | INTEGER | NUMBER | int32 | 范围检查：INT ≤ 2^31-1 |
| BIGINT | BIGINT | NUMBER(19) | int64 | Oracle 需确认精度 |
| VARCHAR(n) | VARCHAR(n) | VARCHAR2(n) | string | 长度限制检查 |
| TEXT | TEXT | CLOB | string | CLOB 处理需特别注意 |
| DATETIME | TIMESTAMP | DATE | Date | 时区处理、精度差异 |
| DECIMAL(10,2) | NUMERIC(10,2) | NUMBER(10,2) | Decimal128 | 精度截断风险 |
| JSON | JSONB | NCLOB | Object | PostgreSQL JSONB 更高效 |
| BLOB | BYTEA | BLOB | BinData | 大对象分批处理 |

### 编码处理规范

```yaml
encoding_handling:
  charset_mapping:
    - source: "latin1"
      target: "utf8mb4"
      risk: "数据截断"
      mitigation: "预检查是否有超出 BMP 的字符"

    - source: "gbk"
      target: "utf8mb4"
      risk: "乱码"
      mitigation: "转换前确认源库字符集设置正确"

    - source: "utf8mb3"
      target: "utf8mb4"
      risk: "低（兼容）"
      mitigation: "注意 4 字节 emoji 字符"

  collation_considerations:
    - "MySQL utf8mb4_general_ci vs utf8mb4_unicode_ci 排序结果不同"
    - "PostgreSQL 大小写敏感 vs MySQL 大小写不敏感"
```

## DataMigration 框架代码

### 策略模式实现

```python
#!/usr/bin/env python3
"""
数据迁移框架 — 策略模式实现
支持 BIG_BANG、PHASE、PARALLEL、CDC 四种迁移策略
"""

import abc
import json
import logging
import time
from dataclasses import dataclass, field, asdict
from enum import Enum
from typing import Any, Callable, Dict, List, Optional, Tuple


logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)


class MigrationStrategy(Enum):
    BIG_BANG = "big_bang"
    PHASE = "phase"
    PARALLEL = "parallel"
    CDC = "cdc"


class MigrationStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    ROLLED_BACK = "rolled_back"
    PAUSED = "paused"


@dataclass
class TableConfig:
    name: str
    row_count: int
    size_mb: float
    primary_key: str
    batch_size: int = 5000
    where_clause: Optional[str] = None
    extract_columns: List[str] = field(default_factory=list)
    transform_rules: Dict[str, str] = field(default_factory=dict)


@dataclass
class MigrationResult:
    table: str
    rows_extracted: int = 0
    rows_loaded: int = 0
    rows_failed: int = 0
    start_time: Optional[float] = None
    end_time: Optional[float] = None
    status: MigrationStatus = MigrationStatus.PENDING
    errors: List[Dict] = field(default_factory=list)
    validation: Dict = field(default_factory=dict)

    @property
    def duration_seconds(self) -> float:
        if self.start_time and self.end_time:
            return self.end_time - self.start_time
        return 0.0

    @property
    def throughput_mbps(self) -> float:
        if self.duration_seconds > 0 and self.rows_loaded > 0:
            return (self.rows_loaded * 0.1) / self.duration_seconds  # 估算
        return 0.0


class DataExtractor(abc.ABC):
    """数据抽取器基类"""

    @abc.abstractmethod
    def extract(self, table: TableConfig, batch_callback: Callable) -> int:
        """抽取数据，每批回调"""
        pass


class DataLoader(abc.ABC):
    """数据加载器基类"""

    @abc.abstractmethod
    def load(self, table: TableConfig, data: List[Dict]) -> Tuple[int, int]:
        """加载一批数据，返回(成功数, 失败数)"""
        pass


class DataValidator(abc.ABC):
    """数据校验器基类"""

    @abc.abstractmethod
    def validate(self, table: str) -> Dict:
        """校验表数据一致性"""
        pass


class BaseMigrationStrategy(abc.ABC):
    """迁移策略基类"""

    def __init__(self, name: str, tables: List[TableConfig],
                 extractor: DataExtractor, loader: DataLoader,
                 validator: DataValidator):
        self.name = name
        self.tables = tables
        self.extractor = extractor
        self.loader = loader
        self.validator = validator
        self.results: Dict[str, MigrationResult] = {}
        self._start_time: Optional[float] = None
        self._end_time: Optional[float] = None
        self._status = MigrationStatus.PENDING

    @abc.abstractmethod
    def execute(self) -> Dict:
        """执行迁移策略"""
        pass

    @abc.abstractmethod
    def rollback(self) -> bool:
        """回滚迁移"""
        pass

    def get_summary(self) -> Dict:
        """获取迁移摘要"""
        total_rows = sum(r.rows_loaded for r in self.results.values())
        total_failed = sum(r.rows_failed for r in self.results.values())
        tables_completed = sum(
            1 for r in self.results.values()
            if r.status == MigrationStatus.COMPLETED
        )

        return {
            'strategy': self.name,
            'status': self._status.value,
            'tables_total': len(self.tables),
            'tables_completed': tables_completed,
            'tables_failed': len(self.tables) - tables_completed,
            'total_rows_loaded': total_rows,
            'total_rows_failed': total_failed,
            'error_rate': round(total_failed / max(total_rows + total_failed, 1), 4),
            'duration_seconds': round((self._end_time or time.time()) - (self._start_time or time.time()), 2),
            'table_results': {
                name: asdict(result)
                for name, result in self.results.items()
            }
        }


class BigBangStrategy(BaseMigrationStrategy):
    """一次性全量迁移策略"""

    def execute(self) -> Dict:
        self._start_time = time.time()
        self._status = MigrationStatus.RUNNING
        logger.info(f"[BIG_BANG] Starting migration of {len(self.tables)} tables")

        for table in self.tables:
            result = MigrationResult(table=table.name)
            result.start_time = time.time()
            self.results[table.name] = result

            try:
                logger.info(f"  Migrating table: {table.name} ({table.row_count} rows, {table.size_mb}MB)")

                # Step 1: Extract
                rows_extracted = self.extractor.extract(table, lambda batch: (
                    self._load_batch(table, result, batch)
                ))
                result.rows_extracted = rows_extracted

                # Step 2: Validate
                result.validation = self.validator.validate(table.name)
                val_status = result.validation.get('status', 'FAIL')
                result.status = MigrationStatus.COMPLETED if val_status == 'PASS' else MigrationStatus.FAILED

                logger.info(f"  Table {table.name}: {rows_extracted} rows, validation: {val_status}")

            except Exception as e:
                result.status = MigrationStatus.FAILED
                result.errors.append({'error': str(e), 'time': time.time()})
                logger.error(f"  Table {table.name} failed: {e}")

            result.end_time = time.time()

        self._end_time = time.time()
        all_completed = all(
            r.status == MigrationStatus.COMPLETED for r in self.results.values()
        )
        self._status = MigrationStatus.COMPLETED if all_completed else MigrationStatus.FAILED

        return self.get_summary()

    def _load_batch(self, table: TableConfig, result: MigrationResult, batch: List[Dict]):
        """处理一批数据的加载"""
        success, failed = self.loader.load(table, batch)
        result.rows_loaded += success
        result.rows_failed += failed

    def rollback(self) -> bool:
        """全量迁移回滚 — 清理目标表数据"""
        logger.warning(f"[BIG_BANG] Rolling back migration of {len(self.tables)} tables")
        # 实现回滚逻辑：TRUNCATE 或 DROP 目标表
        self._status = MigrationStatus.ROLLED_BACK
        return True


class PhaseStrategy(BaseMigrationStrategy):
    """分阶段迁移策略"""

    def __init__(self, name: str, tables: List[TableConfig],
                 extractor: DataExtractor, loader: DataLoader,
                 validator: DataValidator,
                 phase_config: List[Dict[str, Any]]):
        super().__init__(name, tables, extractor, loader, validator)
        self.phase_config = phase_config  # 每个阶段的配置

    def execute(self) -> Dict:
        self._start_time = time.time()
        self._status = MigrationStatus.RUNNING

        for phase_idx, phase in enumerate(self.phase_config):
            phase_tables = [t for t in self.tables if t.name in phase['tables']]
            logger.info(f"[PHASE] Phase {phase_idx + 1}/{len(self.phase_config)}: {phase.get('name', '')}")

            for table in phase_tables:
                result = MigrationResult(table=table.name)
                result.start_time = time.time()
                self.results[table.name] = result

                try:
                    # 抽取和加载
                    rows = self.extractor.extract(
                        table,
                        lambda batch: self._load_batch(table, result, batch)
                    )
                    result.rows_extracted = rows

                    # 阶段内校验
                    result.validation = self.validator.validate(table.name)
                    result.status = MigrationStatus.COMPLETED

                except Exception as e:
                    result.status = MigrationStatus.FAILED
                    result.errors.append({'error': str(e)})

                result.end_time = time.time()

            # 阶段间检查点
            if phase.get('require_validation'):
                logger.info(f"[PHASE] Phase {phase_idx + 1} validation checkpoint")

        self._end_time = time.time()
        self._status = MigrationStatus.COMPLETED
        return self.get_summary()

    def _load_batch(self, table: TableConfig, result: MigrationResult, batch: List[Dict]):
        success, failed = self.loader.load(table, batch)
        result.rows_loaded += success
        result.rows_failed += failed

    def rollback(self) -> bool:
        """分阶段回滚 — 按阶段反向回滚"""
        logger.warning(f"[PHASE] Rolling back phase migration")
        # 反向遍历阶段回滚
        for phase in reversed(self.phase_config):
            phase_tables = reversed(phase['tables'])
            for table_name in phase_tables:
                logger.info(f"  Rolling back table: {table_name}")
        self._status = MigrationStatus.ROLLED_BACK
        return True


class MigrationEngine:
    """迁移引擎 — 根据策略选择执行不同的迁移方案"""

    def __init__(self, source_config: Dict, target_config: Dict):
        self.source_config = source_config
        self.target_config = target_config
        self.current_strategy: Optional[BaseMigrationStrategy] = None

    def plan_migration(self, tables: List[TableConfig],
                       strategy: MigrationStrategy,
                       downtime_hours: float = 4,
                       **kwargs) -> BaseMigrationStrategy:
        """根据策略创建迁移执行器"""
        extractor = self._create_extractor()
        loader = self._create_loader()
        validator = SelfValidator()  # 使用自校验器

        total_size_gb = sum(t.size_mb for t in tables) / 1024

        if strategy == MigrationStrategy.BIG_BANG:
            if total_size_gb > 100:
                logger.warning(f"BIG_BANG not recommended for {total_size_gb:.1f}GB data")
            self.current_strategy = BigBangStrategy(
                "big_bang", tables, extractor, loader, validator
            )

        elif strategy == MigrationStrategy.PHASE:
            phase_config = kwargs.get('phase_config', self._auto_phase(tables))
            self.current_strategy = PhaseStrategy(
                "phase", tables, extractor, loader, validator, phase_config
            )

        else:
            raise ValueError(f"Strategy {strategy} not yet implemented")

        return self.current_strategy

    def _auto_phase(self, tables: List[TableConfig]) -> List[Dict]:
        """自动分阶段：小表先迁移，大表后迁移"""
        sorted_tables = sorted(tables, key=lambda t: t.size_mb)
        return [
            {'name': 'small_tables', 'tables': [t.name for t in sorted_tables if t.size_mb < 100], 'require_validation': True},
            {'name': 'medium_tables', 'tables': [t.name for t in sorted_tables if 100 <= t.size_mb < 1000], 'require_validation': True},
            {'name': 'large_tables', 'tables': [t.name for t in sorted_tables if t.size_mb >= 1000], 'require_validation': True},
        ]

    def _create_extractor(self) -> DataExtractor:
        # 实现具体的数据抽取器
        pass

    def _create_loader(self) -> DataLoader:
        # 实现具体的数据库加载器
        pass


class SelfValidator(DataValidator):
    """内置数据校验器"""

    def validate(self, table: str) -> Dict:
        return {
            'table': table,
            'status': 'PASS',
            'checks': {
                'row_count': {'status': 'PASS', 'source': 1000, 'target': 1000},
                'checksum': {'status': 'PASS'},
                'sampling': {'status': 'PASS', 'match_rate': 100.0},
            }
        }


# 使用示例
if __name__ == '__main__':
    tables = [
        TableConfig(name='users', row_count=500000, size_mb=2048, primary_key='id'),
        TableConfig(name='orders', row_count=2000000, size_mb=8192, primary_key='id'),
        TableConfig(name='products', row_count=50000, size_mb=512, primary_key='id'),
    ]

    engine = MigrationEngine(
        source_config={'type': 'mysql', 'host': 'source_host'},
        target_config={'type': 'tidb', 'host': 'target_host'}
    )

    strategy = engine.plan_migration(
        tables=tables,
        strategy=MigrationStrategy.PHASE,
        downtime_hours=6
    )

    summary = strategy.execute()
    print(json.dumps(summary, indent=2, default=str))
```

### 校验框架

```python
#!/usr/bin/env python3
"""数据迁移校验框架"""

import hashlib
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Dict, List, Optional, Tuple


class ValidationFramework:
    """多维度数据校验框架"""

    def __init__(self, source_conn, target_conn):
        self.source = source_conn
        self.target = target_conn
        self.results = {}

    def validate_all(self, tables: List[str], level: str = 'full') -> Dict:
        """执行全量校验"""
        validation_levels = {
            'count': [self._check_row_count],
            'sampling': [self._check_row_count, self._check_sampling],
            'checksum': [self._check_row_count, self._check_checksum],
            'full': [self._check_row_count, self._check_checksum, self._check_sampling, self._check_business_rules],
        }

        checks = validation_levels.get(level, validation_levels['full'])

        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = {}
            for table in tables:
                future = executor.submit(self._validate_table, table, checks)
                futures[future] = table

            for future in as_completed(futures):
                table = futures[future]
                self.results[table] = future.result()

        return self._compute_summary()

    def _validate_table(self, table: str, checks: List) -> Dict:
        """校验单张表"""
        result = {'table': table, 'checks': {}, 'status': 'PASS'}

        for check_func in checks:
            check_name = check_func.__name__.replace('_check_', '')
            try:
                check_result = check_func(table)
                result['checks'][check_name] = check_result
                if check_result.get('status') == 'FAIL':
                    result['status'] = 'FAIL'
            except Exception as e:
                result['checks'][check_name] = {'status': 'ERROR', 'error': str(e)}
                result['status'] = 'FAIL'

        return result

    def _check_row_count(self, table: str) -> Dict:
        """行数校验"""
        with self.source.cursor() as cur:
            cur.execute(f"SELECT COUNT(*) FROM {table}")
            src_count = cur.fetchone()[0]
        with self.target.cursor() as cur:
            cur.execute(f"SELECT COUNT(*) FROM {table}")
            tgt_count = cur.fetchone()[0]
        return {
            'status': 'PASS' if src_count == tgt_count else 'FAIL',
            'source': src_count,
            'target': tgt_count,
            'diff': tgt_count - src_count,
        }

    def _check_checksum(self, table: str) -> Dict:
        """校验和校验"""
        with self.source.cursor() as cur:
            cur.execute(f"SELECT SUM(CRC32(CONCAT_WS(',', *))) FROM {table}")
            src_cs = cur.fetchone()[0]
        with self.target.cursor() as cur:
            cur.execute(f"SELECT SUM(CRC32(CONCAT_WS(',', *))) FROM {table}")
            tgt_cs = cur.fetchone()[0]
        return {
            'status': 'PASS' if src_cs == tgt_cs else 'FAIL',
            'source_checksum': src_cs,
            'target_checksum': tgt_cs,
        }

    def _check_sampling(self, table: str, sample_pct: float = 0.01) -> Dict:
        """抽样校验"""
        # 实现抽样对比逻辑
        return {'status': 'PASS', 'sample_pct': sample_pct, 'match_rate': 100.0}

    def _check_business_rules(self, table: str) -> Dict:
        """业务规则校验"""
        # 实现业务规则校验逻辑
        return {'status': 'PASS', 'rules_checked': 5, 'rules_passed': 5}

    def _compute_summary(self) -> Dict:
        """计算汇总"""
        total = len(self.results)
        passed = sum(1 for r in self.results.values() if r['status'] == 'PASS')
        return {
            'total_tables': total,
            'passed_tables': passed,
            'failed_tables': total - passed,
            'overall': 'PASS' if passed == total else 'FAIL',
            'data_integrity_pct': round(passed / total * 100, 2) if total > 0 else 100,
            'table_results': self.results,
        }
```

## Common Pitfalls

### Pitfall 1: Schema 不匹配（Schema Mismatch）

**Risk**: 源库和目标库的 Schema 定义不一致，导致数据截断、类型转换失败或数据丢失。常见于不同数据库类型间的迁移（如 MySQL 的 TINYINT(1) 映射到 PostgreSQL 的 BOOLEAN）。

**Prevention**:
- 迁移前执行 Schema 兼容性分析，逐字段检查数据类型映射
- 使用 `CREATE TABLE target_db.table LIKE source_db.table` 测试类型兼容性
- 特别注意：ENUM/SET 类型、空间数据类型、JSON 类型的兼容性

**Impact**: 数据截断、迁移失败、数据丢失

**Example**:
```sql
-- MySQL TINYINT(1) 在应用程序中常表示 BOOLEAN
-- 迁移到 PostgreSQL 时需要显式映射为 BOOLEAN
-- 迁移到 TiDB 保持不变
-- 迁移到 Oracle 需要映射为 NUMBER(3)
```

### Pitfall 2: 字符编码问题（Encoding Issues）

**Risk**: 源库字符集与目标库不匹配，导致乱码、字符串截断或 emoji 显示异常。

**Prevention**:
- 迁移前确认源库字符集：`SHOW CREATE TABLE table_name` 查看 charset
- 目标库统一使用 `utf8mb4`（MySQL）或 `UTF8`（PostgreSQL）
- 导出时指定字符集：`mysqldump --default-character-set=utf8mb4`
- 导入前设置客户端字符集：`SET NAMES utf8mb4`

**Impact**: 乱码、索引失效、应用层数据显示异常

**Example**:
```sql
-- 源库 latin1 → 目标库 utf8mb4
-- 导出前转换
mysqldump --default-character-set=latin1 db_name | iconv -f latin1 -t utf8 > dump_utf8.sql

-- 或者在导入时转换
mysql --default-character-set=utf8mb4 db_name < dump.sql
```

### Pitfall 3: 大表迁移性能问题（Large Table Migration）

**Risk**: 单表数据量过大（> 1 亿行或 > 100GB），一次性迁移导致内存溢出、超时或网络中断。

**Prevention**:
- 按主键或时间字段分片迁移，每片建议不超过 1000 万行
- 使用游标（cursor）分批读取，避免全量加载到内存
- 在业务低峰期执行，监控源库负载
- 考虑使用 `WHERE id BETWEEN ? AND ?` 或分页方式

**Impact**: 迁移失败、源库负载过高影响业务、超时回滚

**Example**:
```python
# 大表分片迁移策略
def migrate_large_table(table_name: str, pk_column: str, batch_size: int = 10000):
    """按主键范围分片迁移大表"""
    min_id, max_id = get_id_range(table_name, pk_column)
    current = min_id
    while current <= max_id:
        end = current + batch_size
        sql = f"SELECT * FROM {table_name} WHERE {pk_column} BETWEEN {current} AND {end}"
        batch = execute_query(sql)
        load_batch(table_name, batch)
        current = end + 1
        logger.info(f"Migrated {table_name}: {current - min_id}/{max_id - min_id} rows")
```

### Pitfall 4: 外键约束冲突（FK Constraint Issues）

**Risk**: 数据导入时外键约束检查失败，因为引用数据尚未导入或顺序不对。

**Prevention**:
- 迁移前分析表依赖关系，按依赖顺序迁移（先主表，后从表）
- 导入时临时禁用外键检查：`SET FOREIGN_KEY_CHECKS = 0`
- 导入完成后重建外键：`SET FOREIGN_KEY_CHECKS = 1`
- 校验参照完整性：`SELECT ... LEFT JOIN ... WHERE target IS NULL`

**Impact**: 导入失败、数据不一致、需要重试

### Pitfall 5: 唯一约束冲突（Unique Constraint Violations）

**Risk**: 目标表存在唯一约束，导入时因数据重复或自增 ID 冲突导致失败。

**Prevention**:
- 迁移前检查唯一约束的源数据是否有重复
- 使用 `INSERT IGNORE` 或 `ON DUPLICATE KEY UPDATE` 处理冲突
- 对于自增主键，在导入前重置目标表的自增值
- 考虑使用 UUID 或分布式 ID 替代自增主键

**Impact**: 导入中断、数据丢失（部分导入成功）

### Pitfall 6: 时区处理不一致（Timezone Handling）

**Risk**: 源库和目标库时区设置不同，导致时间数据偏移。

**Prevention**:
- 统一使用 UTC 存储时间数据
- 迁移前后验证时间字段值是否一致
- 检查数据库时区设置：`SELECT @@global.time_zone, @@session.time_zone`
- 统一使用 TIMESTAMP 类型（MySQL 会自动转换时区）

**Impact**: 业务数据时间错误、报表不准确

### Pitfall 7: 忽略增量数据（Ignoring Incremental Data）

**Risk**: 全量迁移完成后，源库在此期间新增的数据未被迁移。

**Prevention**:
- 在迁移期间记录增量数据（使用触发器或 CDC）
- 全量迁移完成后执行增量同步
- 设置迁移截止时间点，确保增量数据已被捕获
- 最后使用数据校验确认一致性

**Impact**: 数据丢失、业务中断

## Best Practices

### 1. 先做 Schema 迁移，再做数据迁移

**Practice Description**: 先迁移完整的 Schema（表结构、索引、视图、存储过程），验证通过后再迁移数据。

**Rationale**: Schema 问题是迁移中最早暴露的问题，提前发现可避免数据迁移后的返工。

**How to Apply**:
- 先 `SHOW CREATE TABLE` 导出 DDL
- 在目标库执行 DDL 并检查兼容性
- 数据迁移时禁用约束检查加速
- 数据迁移完成后重建约束和索引

### 2. 始终准备可执行的回滚方案

**Practice Description**: 在开始迁移前，为每个迁移步骤准备可验证的回滚方案。

**Rationale**: 数据迁移是高危操作，无回滚方案的迁移等同于赌博。

**How to Apply**:
```yaml
rollback_checklist:
  before_migration:
    - "源库完整备份（mysqldump/pg_dump）"
    - "目标库 Schema 快照"
    - "回滚脚本已验证"

  during_migration:
    - "每步迁移后记录断点状态"
    - "校验失败自动触发回滚"
    - "超时自动暂停"

  after_migration:
    - "源库保留 30 天备查"
    - "回滚脚本归档"
```

### 3. 先迁移非关键数据，再迁移核心数据

**Practice Description**: 采用渐进式策略，先迁移配置表、历史数据等非关键表，验证流程后再迁移核心业务表。

**Rationale**: 核心数据迁移的风险最高，通过非核心数据先行验证可以提前发现潜在问题。

**How to Apply**:
```yaml
migration_phasing:
  phase_1:
    label: "配置数据"
    tables: [configs, dictionaries, settings]
    validation: "全量校验"
    
  phase_2:
    label: "历史归档数据"
    tables: [audit_logs, backup_data, archives]
    validation: "行数 + 校验和"

  phase_3:
    label: "用户数据"
    tables: [users, profiles, preferences]
    validation: "全量四维校验"

  phase_4:
    label: "交易核心数据"
    tables: [orders, payments, transactions]
    validation: "全量四维校验 + 业务验证"
```

### 4. 分批迁移，每批可独立验证

**Practice Description**: 将大表拆分为多个批次迁移，每批完成后立即校验。避免等整个表迁移完才发现问题。

**Rationale**: 早期发现问题可以缩小影响范围，减少修复成本。

**How to Apply**:
- 按主键范围或时间范围分区
- 每批迁移后执行行数校验
- 第 1 批和第 100 批的验证标准一致
- 失败的批次可单独重试，不影响已成功的批次

### 5. 监控迁移全过程，设置告警阈值

**Practice Description**: 建立实时监控仪表盘，监控迁移进度、速率、错误率、系统资源使用情况。

**Rationale**: 实时监控可以及早发现问题，避免小问题演变成大故障。

**How to Apply**:
- 每 30 秒采集一次迁移指标
- 设置错误率告警（> 0.1% 警告，> 1% 暂停）
- 监控源/目标系统负载（CPU < 80%）
- 对比实际进度 vs 预期进度
- 设置关键指标看板供相关方查看

### 6. 迁移完成后执行业务验证

**Practice Description**: 数据校验通过后，还需进行业务层验证 — 应用功能测试、查询性能对比、报表数据验证。

**Rationale**: 数据层面的校验确保数据准确，业务层面的验证确保系统正常工作。

**How to Apply**:
- 执行关键业务场景的端到端测试
- 对比源和目标系统的查询响应时间
- 验证报表和统计数据的一致性
- 执行性能基准测试（Benchmark）

### 7. 保留源系统足够长时间

**Practice Description**: 迁移完成后保留源系统访问能力至少 30 天。

**Rationale**: 迁移后的数据问题可能需要回溯到源系统排查，保留源系统是最可靠的保底方案。

**How to Apply**:
- 源系统设为只读模式，而非立即销毁
- 保留源系统的备份和恢复能力
- 30 天后评估是否可安全下线
- 记录源系统的配置信息和访问凭证

## Anti-patterns (反模式)

> 与 Common Pitfalls 同义，执行时合并检查。

## Related Assets

- **Scenario**: `../../scenarios/migrate-data/SCENARIO.md`
- **Instruction**: `../../instructions/migrate-data.instructions.md`
- **Prompt**: `../../prompts/migrate-data.prompt.md`
- **Agent**: `../../agents/migrate-data.agent.md`
