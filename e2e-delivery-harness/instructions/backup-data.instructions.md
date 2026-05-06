---
name: backup-data
description: Detailed technical instructions for backup-data scenario execution
type: instruction
version: "1.1.0"
stage: backup-data
---

# Instructions: 数据备份 (Backup Data)

## Backup Strategy

### 备份类型对比

| 类型 | 备份内容 | 备份时间 | 恢复复杂度 | 存储需求 |
|------|----------|----------|------------|----------|
| 全量备份 | 所有数据 | 长 | 低 | 大 |
| 增量备份 | 变更数据 | 短 | 高 | 小 |
| 差异备份 | 与全量的差异 | 中 | 中 | 中 |

### 备份策略设计

```yaml
# 推荐备份策略
recommended_strategy:
  frequency:
    full_backup:
      schedule: "Weekly (Sunday 02:00)"
      retention: "4 weeks"

    incremental_backup:
      schedule: "Daily (02:00)"
      retention: "7 days"

    log_backup:
      schedule: "Hourly"
      retention: "24 hours"

  3-2-1 原则:
    copies: 3
    storage_types: 2
    offsite_copies: 1
```

### 备份时间窗口

```yaml
# 备份时间窗口规划
backup_windows:
  full_backup:
    duration_hours: 4
    window_start: "02:00"
    window_end: "06:00"
    recommended: true

  incremental_backup:
    duration_hours: 1
    window_start: "02:00"
    window_end: "03:00"
    recommended: true

  realtime_backup:
    duration_hours: "continuous"
    recommended: true
```

## Database Backup Standards

### MySQL 备份

```bash
# 全量备份脚本
#!/bin/bash
BACKUP_DIR="/backup/mysql"
DATE=$(date +%Y%m%d)
MYSQL_USER="backup"
MYSQL_PASSWORD="{{db_password}}"

# 创建备份目录
mkdir -p ${BACKUP_DIR}/${DATE}

# 全量备份
mysqldump \
  --user=${MYSQL_USER} \
  --password=${MYSQL_PASSWORD} \
  --all-databases \
  --single-transaction \
  --routines \
  --triggers \
  --events \
  | gzip > ${BACKUP_DIR}/${DATE}/full_backup.sql.gz

# 验证备份
md5sum ${BACKUP_DIR}/${DATE}/full_backup.sql.gz > ${BACKUP_DIR}/${DATE}/md5.txt
```

### PostgreSQL 备份

```bash
#!/bin/bash
BACKUP_DIR="/backup/postgres"
DATE=$(date +%Y%m%d)

# 全量备份
pg_basebackup -h localhost -U postgres \
  -D ${BACKUP_DIR}/${DATE} \
  -Ft -z -P

# WAL 归档
# 配置 postgresql.conf
# wal_level = replica
# archive_mode = on
# archive_command = 'test ! -f /backup/wal/%f && cp %p /backup/wal/%f'
```

### MongoDB 备份

```bash
#!/bin/bash
BACKUP_DIR="/backup/mongo"
DATE=$(date +%Y%m%d)

# mongodump 全量备份
mongodump \
  --host=mongo-primary:27017 \
  --out=${BACKUP_DIR}/${DATE}

# 压缩备份
tar -czf ${BACKUP_DIR}/mongo_${DATE}.tar.gz ${BACKUP_DIR}/${DATE}
```

## File Backup Standards

### 备份范围定义

```yaml
backup_scope:
  must_include:
    - path: "/data/app/uploads"
      description: "用户上传文件"
      priority: "high"

    - path: "/data/app/config"
      description: "配置文件"
      priority: "critical"

    - path: "/data/app/logs"
      description: "日志文件"
      priority: "medium"

  should_include:
    - path: "{{app_install_dir}}"
      description: "应用程序"
      priority: "medium"

    - path: "/etc/nginx"
      description: "Nginx 配置"
      priority: "low"
```

### Rsync 备份示例

```bash
#!/bin/bash
SOURCE_DIR="/data"
BACKUP_DIR="/backup/files"
DATE=$(date +%Y%m%d)
EXCLUDE_FILE="/backup/excludes.txt"

# 创建备份目录
mkdir -p ${BACKUP_DIR}/${DATE}

# 增量备份
rsync -avz \
  --exclude-from=${EXCLUDE_FILE} \
  --delete \
  ${SOURCE_DIR}/ \
  ${BACKUP_DIR}/${DATE}/

# 硬链接到当前备份
ln -nfs ${BACKUP_DIR}/${DATE} ${BACKUP_DIR}/current
```

## Storage Strategy Standards

### 存储分层

```
┌─────────────────────────────────────────────────────────────────┐
│                      BACKUP STORAGE TIER                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Tier 1: Hot Storage                                          │
│  ┌─────────────────────────────────────┐                       │
│  │  SSD/NVMe                           │                       │
│  │  RTO: < 1 hour                      │                       │
│  │  Retention: 7 days                  │                       │
│  └─────────────────────────────────────┘                       │
│                                                                 │
│  Tier 2: Warm Storage                                         │
│  ┌─────────────────────────────────────┐                       │
│  │  Standard Object Storage            │                       │
│  │  RTO: < 24 hours                    │                       │
│  │  Retention: 30 days                 │                       │
│  └─────────────────────────────────────┘                       │
│                                                                 │
│  Tier 3: Cold Storage                                         │
│  ┌─────────────────────────────────────┐                       │
│  │  Archive/Glacier                    │                       │
│  │  RTO: < 48 hours                    │                       │
│  │  Retention: 7 years                 │                       │
│  └─────────────────────────────────────┘                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 存储容量规划

```yaml
capacity_planning:
  # 增长预估
  growth_rate: "20% monthly"

  # 存储需求计算
  calculation:
    daily_increment_gb: 10
    full_backup_gb: 1000
    retention_days: 30

  # 存储需求
  requirements:
    tier1_gb: 700      # 7天 * 100GB
    tier2_gb: 30000    # 30天 * 1000GB
    tier3_gb: 84000    # 7年 * 1000GB * 12

  # 安全余量
  safety_margin: 1.2
```

## Recovery Drill Standards

### 演练频率

```yaml
restore_test_frequency:
  critical_data:
    frequency: "monthly"
    participants: ["DBA", "DevOps"]

  important_data:
    frequency: "quarterly"
    participants: ["DevOps"]

  general_data:
    frequency: "semi-annually"
    participants: ["DevOps"]
```

### 演练检查清单

```yaml
restore_test_checklist:
  pre_test:
    - name: "通知相关团队"
      required: true
    - name: "准备恢复环境"
      required: true
    - name: "确认备份文件可用"
      required: true

  during_test:
    - name: "记录开始时间"
      required: true
    - name: "执行恢复步骤"
      required: true
    - name: "验证数据完整性"
      required: true
    - name: "记录结束时间"
      required: true

  post_test:
    - name: "清理测试环境"
      required: true
    - name: "编写演练报告"
      required: true
    - name: "优化恢复流程"
      required: false
```

## Monitoring and Alerting Standards

### 监控指标

```yaml
backup_monitoring:
  metrics:
    - name: "backup_job_status"
      type: "boolean"
      alert_on: "failure"

    - name: "backup_duration"
      type: "duration"
      alert_threshold: "> 4 hours"

    - name: "backup_size"
      type: "bytes"
      alert_threshold: "< expected * 0.5"

    - name: "storage_usage"
      type: "percentage"
      alert_threshold: "> 80%"

    - name: "last_successful_backup"
      type: "timestamp"
      alert_threshold: "> 24 hours"
```

### Alert Configuration

```yaml
alert_config:
  critical:
    - name: "backup_failed"
      severity: "critical"
      notification:
        - channels: ["pagerduty", "sms", "call"]
        - recipients: ["oncall-dba", "oncall-ops"]

    - name: "storage_full"
      severity: "critical"
      notification:
        - channels: ["pagerduty", "email"]
        - recipients: ["oncall-ops"]

  warning:
    - name: "backup_duration_exceeded"
      severity: "warning"
      notification:
        - channels: ["slack", "email"]
        - recipients: ["team-channel"]

    - name: "storage_usage_high"
      severity: "warning"
      notification:
        - channels: ["slack"]
        - recipients: ["team-channel"]
```

## Compliance Requirements

### 常见合规标准

| 标准 | 要求 | 保留期 |
|------|------|--------|
| GDPR | 个人数据保护 | 按需 |
| SOC 2 | 审计追踪 | 1 年 |
| ISO 27001 | 信息安全 | 3 年 |
| PCI DSS | 支付数据 | 1 年 |
| HIPAA | 医疗数据 | 6 年 |

### 合规配置

```yaml
compliance_config:
  encryption:
    required: true
    algorithm: "AES-256"
    key_management: "kms"

  access_control:
    principle: "least_privilege"
    mfa_required: true
    audit_logging: true

  data_isolation:
    tenant_isolation: true
    environment_isolation: true

  retention:
    default_retention: "90 days"
    extended_retention: "1 year"
    archive_retention: "7 years"
```


## Overview

> High-level description of the backup-data execution process.
>
> This instruction defines the technical approach, key activities, and success criteria for the backup-data scenario.


## Technical Specifications

> Detailed technical requirements and implementation guidelines for backup-data.

### Required Tools
- [List required tools and frameworks]

### Environment Requirements
- [List environment prerequisites]

### Configuration Parameters
- [List key configuration parameters]


## Best Practices

> Industry-standard best practices for backup-data execution.

1. **Practice 1**: Implement automated backup schedules with verified restoration
2. **Practice 2**: Encrypt backup data at rest and in transit
3. **Practice 3**: Test recovery procedures quarterly with documented results


## Error Handling

> Common error scenarios and resolution strategies for backup-data.

### Error Category 1
**Symptom**: Backup jobs fail silently or produce corrupt archives
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]

### Error Category 2
**Symptom**: Recovery time exceeds business-defined RTO targets
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]


## Quality Standards

> Acceptance criteria and quality gates for backup-data deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | Backup success rate is 99.5% or higher | Automated check |
| Standard 2 | Recovery point objective (RPO) is consistently met | Automated check |
| Standard 3 | Quarterly recovery drills pass validation checks | Automated check |
