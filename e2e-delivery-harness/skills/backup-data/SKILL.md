---
name: backup-data
description: "Domain skill for backup-data execution"
type: skill
version: "1.1.0"
stage: "backup-data"
---

# Skill: 数据备份 (Data Backup)

## Overview

本 Skill 定义了数据备份的核心知识体系。

## Core Knowledge

### 备份概念

#### RTO 和 RPO

```python
# RTO (Recovery Time Objective) - 恢复时间目标
# 系统中断后，恢复到可用状态的最长时间

# RPO (Recovery Point Objective) - 恢复点目标
# 可接受的最大数据丢失时间窗口

recovery_objectives = {
    "tier1_critical": {
        "rto_hours": 4,
        "rpo_hours": 1,
        "description": "核心业务系统"
    },
    "tier2_important": {
        "rto_hours": 24,
        "rpo_hours": 24,
        "description": "重要业务系统"
    },
    "tier3_general": {
        "rto_hours": 72,
        "rpo_hours": 168,  # 1 week
        "description": "一般业务系统"
    }
}
```

### 备份策略模式

#### 3-2-1 备份原则

```
┌─────────────────────────────────────────────────────────────┐
│                    3-2-1 BACKUP STRATEGY                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  3 - 3 copies of your data                                  │
│       │                                                    │
│       ├── Primary Data                                     │
│       ├── Local Backup ─────┐                              │
│       └── Offsite Backup ───┼──┘                            │
│                                                             │
│  2 - 2 different storage types                            │
│       │                                                    │
│       ├── Disk (NAS/ SAN) ────┤                              │
│       └── Cloud (OSS/S3) ─────┘                            │
│                                                             │
│  1 - 1 copy offsite                                        │
│       │                                                    │
│       └──异地灾备中心                                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

#### 备份类型

```python
backup_types = {
    "full": {
        "description": "完整数据副本",
        "pros": ["恢复简单", "数据完整"],
        "cons": ["耗时", "占用空间大"],
        "frequency": "weekly"
    },

    "incremental": {
        "description": "仅备份自上次备份以来的变更",
        "pros": ["速度快", "空间占用小"],
        "cons": ["恢复复杂", "依赖链"],
        "frequency": "daily"
    },

    "differential": {
        "description": "备份与上次全量的差异",
        "pros": ["速度较快", "恢复较快"],
        "cons": ["空间占用中等"],
        "frequency": "daily"
    }
}
```

### 备份存储技术

#### 云存储对比

| 云服务商 | 服务 | 类型 | 成本 | 适用场景 |
|----------|------|------|------|----------|
| AWS | S3 Glacier | 冷存储 | $0.004/GB | 长期归档 |
| AWS | S3 Standard | 热存储 | $0.023/GB | 日常备份 |
| 阿里云 | OSS Standard | 热存储 | ¥0.12/GB | 日常备份 |
| 阿里云 | OSS Archive | 冷存储 | ¥0.033/GB | 长期归档 |
| 华为云 | OBS Standard | 热存储 | ¥0.12/GB | 日常备份 |
| 华为云 | OBS Cold | 冷存储 | ¥0.035/GB | 长期归档 |

#### 存储成本优化

```python
class BackupStorageOptimizer:
    """备份存储优化"""

    def tiered_storage(self, backups):
        """分层存储策略"""
        storage_tiers = {
            "hot": {
                "retention": "7 days",
                "storage": "S3 Standard",
                "cost_per_gb_month": 0.023
            },
            "warm": {
                "retention": "30 days",
                "storage": "S3 IA",
                "cost_per_gb_month": 0.0125
            },
            "cold": {
                "retention": "90 days",
                "storage": "S3 Glacier",
                "cost_per_gb_month": 0.004
            },
            "archive": {
                "retention": "1 year+",
                "storage": "S3 Glacier Deep",
                "cost_per_gb_month": 0.00099
            }
        }

        # 自动分层
        return self.auto_tier(backups, storage_tiers)
```

### 数据库备份

#### MySQL 备份方案

```python
mysql_backup_strategies = {
    "small_db": {
        "method": "mysqldump",
        "full_backup": "daily",
        "incremental": "binlog",
        "estimated_time_per_gb": "1-2 min"
    },

    "medium_db": {
        "method": "xtrabackup",
        "full_backup": "weekly",
        "incremental": "daily",
        "estimated_time_per_gb": "30 sec"
    },

    "large_db": {
        "method": "xtrabackup + streaming",
        "full_backup": "weekly",
        "incremental": "hourly",
        "estimated_time_per_gb": "10-20 sec"
    }
}
```

#### PostgreSQL 备份方案

```python
postgres_backup_strategies = {
    "logical_backup": {
        "method": "pg_dump",
        "use_case": "小规模数据库"
    },

    "physical_backup": {
        "method": "pg_basebackup",
        "use_case": "大规模数据库"
    },

    "continuous_archiving": {
        "method": "WAL archiving",
        "use_case": "PITR 恢复"
    }
}
```

### 备份加密

#### 加密策略

```python
encryption_config = {
    "at_rest": {
        "algorithm": "AES-256-GCM",
        "key_management": "KMS",
        "key_rotation": "90 days"
    },

    "in_transit": {
        "protocol": "TLS 1.2+",
        "verify": true
    }
}
```

### 恢复验证

#### 恢复测试框架

```python
class BackupRestoreTest:
    """备份恢复测试"""

    def test_restore_point(self, backup_file, target_time):
        """测试恢复到指定时间点"""
        steps = [
            "prepare_restore_environment",
            "extract_backup",
            "apply_transaction_logs",
            "verify_data_integrity",
            "compare_checksums",
            "run_validation_queries"
        ]

        result = self.execute_restore(backup_file, target_time, steps)
        return result

    def measure_rto(self, backup_file):
        """测量实际 RTO"""
        start_time = time.time()

        # 执行恢复
        self.restore(backup_file)

        end_time = time.time()
        actual_rto = end_time - start_time

        return {
            "actual_rto_minutes": actual_rto / 60,
            "target_rto_minutes": self.target_rto
        }
```

## Best Practices

### 备份检查清单

```yaml
backup_best_practices:
  pre_backup:
    - "确认备份存储可用"
    - "确认备份工具正常"
    - "通知相关团队"

  during_backup:
    - "监控备份进度"
    - "检查备份日志"
    - "验证备份文件"

  post_backup:
    - "验证备份完整性"
    - "确认备份元数据"
    - "更新备份目录"
    - "告警通知结果"
```

### FAQ处理

```python
common_issues = {
    "backup_too_slow": {
        "causes": ["网络带宽不足", "磁盘 IO 瓶颈"],
        "solutions": ["使用压缩", "调整备份窗口", "升级存储"]
    },

    "backup_storage_full": {
        "causes": ["数据增长快", "保留策略过长"],
        "solutions": ["清理过期备份", "扩展存储", "优化保留策略"]
    },

    "restore_failed": {
        "causes": ["备份文件损坏", "恢复环境问题"],
        "solutions": ["使用上一个备份", "检查恢复环境", "联系厂商支持"]
    }
}
```

## Toolchain

### 备份工具

| 类型 | 工具 | 说明 |
|------|------|------|
| 数据库 | mysqldump, xtrabackup | MySQL 备份 |
| 数据库 | pg_dump, Barman | PostgreSQL 备份 |
| 数据库 | mongodump | MongoDB 备份 |
| 文件 | rsync, rclone | 文件同步备份 |
| 企业 | Veeam, Commvault | 企业备份软件 |
| 云原生 | AWS Backup | AWS 备份服务 |

### 监控工具

| 工具 | 用途 |
|------|------|
| Zabbix | 备份监控 |
| Prometheus | 指标采集 |
| Grafana | 监控面板 |
| ELK | 日志分析 |

## Associated Assets

- **Scenario**: `../../scenarios/backup-data/SCENARIO.md`
- **Instruction**: `../../instructions/backup-data.instructions.md`
- **Prompt**: `../../prompts/backup-data.prompt.md`
- **Agent**: `../../agents/backup-data.agent.md`


## Core Knowledge

> Essential knowledge domain for backup-data execution.

### Domain Fundamentals
- [Core concept 1]
- [Core concept 2]
- [Core concept 3]

### Key Principles
1. [Principle 1]
2. [Principle 2]
3. [Principle 3]


## Best Practices

> Proven practices for backup-data excellence.

1. **Practice 1**: [Description and rationale]
2. **Practice 2**: [Description and rationale]
3. **Practice 3**: [Description and rationale]


## Common Pitfalls

> Frequent mistakes to avoid during backup-data execution.

### Pitfall 1: [Name]
**Risk**: [Description]
**Prevention**: [How to avoid]
**Impact**: [Consequences if not avoided]

### Pitfall 2: [Name]
**Risk**: [Description]
**Prevention**: [How to avoid]
**Impact**: [Consequences if not avoided]

### Pitfall 3: [Name]
**Risk**: [Description]
**Prevention**: [How to avoid]
**Impact**: [Consequences if not avoided]
