---
name: backup-data
description: "Detailed technical instructions for backup-data scenario execution"
applyTo: "scenarios/backup-data/**"
phase: operations
type: instruction
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['instruction', 'technical']
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


## Multi-Language Code Examples

### Python (boto3 S3备份)

```python
import boto3
import os
import logging
from datetime import datetime, timedelta
from typing import Optional

# S3备份客户端
class S3BackupClient:
    """生产级S3备份封装，支持加密、生命周期管理和完整性校验"""
    
    def __init__(self, bucket: str, prefix: str = "backup"):
        self.s3 = boto3.client(
            "s3",
            aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
            aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
        )
        self.bucket = bucket
        self.prefix = prefix
        self.logger = logging.getLogger(__name__)
    
    def upload_backup(self, local_path: str, backup_name: str) -> bool:
        """上传备份文件至S3，附带完整性校验"""
        key = f"{self.prefix}/{datetime.now():%Y/%m/%d}/{backup_name}"
        try:
            # 上传前计算MD5
            import hashlib
            with open(local_path, "rb") as f:
                md5_before = hashlib.md5(f.read()).hexdigest()
            
            # 上传文件
            self.s3.upload_file(
                Filename=local_path,
                Bucket=self.bucket,
                Key=key,
                ExtraArgs={
                    "ServerSideEncryption": "AES256",
                    "Metadata": {"source-md5": md5_before}
                }
            )
            
            # 校验MD5
            response = self.s3.head_object(Bucket=self.bucket, Key=key)
            self.logger.info(f"Upload successful: {key}, size={response['ContentLength']}")
            return True
        except Exception as e:
            self.logger.error(f"Upload failed: {key}, error={e}")
            return False
    
    def list_backups(self, days: int = 30) -> list:
        """列出指定天数内的备份文件"""
        cutoff = datetime.now() - timedelta(days=days)
        response = self.s3.list_objects_v2(
            Bucket=self.bucket,
            Prefix=self.prefix
        )
        return [obj["Key"] for obj in response.get("Contents", [])
                if obj["LastModified"].replace(tzinfo=None) > cutoff]

# 使用示例
if __name__ == "__main__":
    client = S3BackupClient(bucket="prod-backup-bucket")
    success = client.upload_backup("/data/dump.sql.gz", "mysql_full_20260623.sql.gz")
    assert success, "S3 backup upload failed!"
```

### Java (AWS SDK S3)

```java
package com.company.backup;

import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.core.sync.RequestBody;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.*;
import software.amazon.awssdk.services.s3.presigner.S3Presigner;
import software.amazon.awssdk.services.s3.presigner.model.GetObjectPresignRequest;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import java.io.File;
import java.net.URL;
import java.time.Duration;
import java.time.LocalDate;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class S3BackupManager {
    private static final Logger log = LoggerFactory.getLogger(S3BackupManager.class);
    private final S3Client s3;
    private final String bucket;
    private final String prefix;

    public S3BackupManager(String bucket, String prefix) {
        this.s3 = S3Client.builder()
                .credentialsProvider(DefaultCredentialsProvider.create())
                .build();
        this.bucket = bucket;
        this.prefix = prefix;
    }

    /**
     * 上传备份文件并启用服务端加密
     */
    public PutObjectResponse uploadBackup(File localFile, String backupName) {
        String key = String.format("%s/%s/%s", prefix, LocalDate.now(), backupName);
        
        PutObjectRequest request = PutObjectRequest.builder()
                .bucket(bucket)
                .key(key)
                .serverSideEncryption(ServerSideEncryption.AES256)
                .metadata(Map.of("source", localFile.getName(), 
                                 "timestamp", String.valueOf(System.currentTimeMillis())))
                .build();

        PutObjectResponse response = s3.putObject(request, 
                RequestBody.fromFile(localFile));
        
        log.info("Backup uploaded: bucket={}, key={}, etag={}", 
                bucket, key, response.eTag());
        return response;
    }

    /**
     * 获取预签名下载URL（用于恢复操作）
     */
    public URL generatePresignedUrl(String key, Duration expiry) {
        S3Presigner presigner = S3Presigner.create();
        GetObjectPresignRequest presignRequest = GetObjectPresignRequest.builder()
                .signatureDuration(expiry)
                .getObjectRequest(req -> req.bucket(bucket).key(key))
                .build();
        return presigner.presignGetObject(presignRequest).url();
    }

    /**
     * 清理过期备份
     */
    public void cleanExpiredBackups(int retentionDays) {
        LocalDate cutoff = LocalDate.now().minusDays(retentionDays);
        String continuationToken = null;
        int deleted = 0;

        do {
            ListObjectsV2Request listReq = ListObjectsV2Request.builder()
                    .bucket(bucket).prefix(prefix)
                    .continuationToken(continuationToken).build();
            ListObjectsV2Response listResp = s3.listObjectsV2(listReq);

            for (S3Object obj : listResp.contents()) {
                if (obj.lastModified().toLocalDate().isBefore(cutoff)) {
                    s3.deleteObject(DeleteObjectRequest.builder()
                            .bucket(bucket).key(obj.key()).build());
                    deleted++;
                }
            }
            continuationToken = listResp.nextContinuationToken();
        } while (continuationToken != null);

        log.info("Expired backups cleaned: count={}, retentionDays={}", 
                deleted, retentionDays);
    }
}
```

### Go (文件/数据库备份脚本)

```go
package main

import (
    "compress/gzip"
    "crypto/md5"
    "fmt"
    "io"
    "log"
    "os"
    "os/exec"
    "path/filepath"
    "time"
)

// BackupConfig 备份配置
type BackupConfig struct {
    SourceDir    string // 源文件目录
    TargetDir    string // 备份目标目录
    DBType       string // 数据库类型: mysql/postgres
    DBConnection string // 数据库连接字符串
    Retention    int    // 保留天数（默认30）
}

// BackupResult 备份结果
type BackupResult struct {
    FilePath string
    Size     int64
    Checksum string
    Duration time.Duration
    Success  bool
}

// RunBackup 执行完整备份流程
func RunBackup(cfg BackupConfig) (*BackupResult, error) {
    timestamp := time.Now().Format("20060102_150405")
    backupFile := filepath.Join(cfg.TargetDir, fmt.Sprintf("backup_%s.tar.gz", timestamp))
    
    log.Printf("Starting backup: source=%s, target=%s", cfg.SourceDir, backupFile)
    start := time.Now()

    // Step 1: 创建目标目录
    if err := os.MkdirAll(cfg.TargetDir, 0755); err != nil {
        return nil, fmt.Errorf("create target dir: %w", err)
    }

    // Step 2: 执行数据库备份（如配置）
    if cfg.DBConnection != "" {
        dbDumpFile := filepath.Join(cfg.TargetDir, fmt.Sprintf("db_%s.sql", timestamp))
        if err := dumpDatabase(cfg.DBType, cfg.DBConnection, dbDumpFile); err != nil {
            return nil, fmt.Errorf("database backup: %w", err)
        }
        defer os.Remove(dbDumpFile)
    }

    // Step 3: 打包压缩
    if err := tarCompress(cfg.SourceDir, backupFile); err != nil {
        return nil, fmt.Errorf("compress backup: %w", err)
    }

    // Step 4: 计算校验和
    checksum, err := computeMD5(backupFile)
    if err != nil {
        return nil, fmt.Errorf("checksum: %w", err)
    }

    // Step 5: 清理过期备份
    if err := cleanOldBackups(cfg.TargetDir, cfg.Retention); err != nil {
        log.Printf("Warning: cleanup failed: %v", err)
    }

    fi, _ := os.Stat(backupFile)
    result := &BackupResult{
        FilePath: backupFile,
        Size:     fi.Size(),
        Checksum: checksum,
        Duration: time.Since(start),
        Success:  true,
    }
    log.Printf("Backup complete: size=%d, checksum=%s, duration=%v",
        result.Size, result.Checksum, result.Duration)
    return result, nil
}

func computeMD5(path string) (string, error) {
    f, err := os.Open(path)
    if err != nil {
        return "", err
    }
    defer f.Close()
    h := md5.New()
    if _, err := io.Copy(h, f); err != nil {
        return "", err
    }
    return fmt.Sprintf("%x", h.Sum(nil)), nil
}

func main() {
    cfg := BackupConfig{
        SourceDir:    "/data/app",
        TargetDir:    "/backup/app",
        DBConnection: "postgres://user:pass@localhost:5432/db",
        Retention:    30,
    }
    result, err := RunBackup(cfg)
    if err != nil {
        log.Fatalf("Backup failed: %v", err)
    }
    // 写入校验文件
    os.WriteFile(result.FilePath+".md5", []byte(result.Checksum), 0644)
}
```

### JavaScript (node-cron定时备份)

```javascript
// backup-scheduler.js
const cron = require('node-cron');
const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs').promises;
const crypto = require('crypto');

class BackupScheduler {
  /**
   * @param {Object} config
   * @param {string} config.sourcePath - 备份源路径
   * @param {string} config.destPath - 备份目标路径
   * @param {number} config.retentionDays - 保留天数
   */
  constructor(config) {
    this.sourcePath = config.sourcePath;
    this.destPath = config.destPath;
    this.retentionDays = config.retentionDays || 30;
  }

  /**
   * 启动定时备份任务
   * @param {string} cronExpression - cron 表达式，默认每天凌晨2点
   */
  start(cronExpression = '0 2 * * *') {
    console.log(`Backup scheduler started: ${cronExpression}`);
    cron.schedule(cronExpression, async () => {
      try {
        await this.executeBackup();
      } catch (err) {
        console.error('Scheduled backup failed:', err.message);
        // 告警通知
        this.sendAlert(err);
      }
    });
  }

  /**
   * 执行单次备份
   * @returns {Promise<{file: string, checksum: string, size: number}>}
   */
  async executeBackup() {
    const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
    const backupDir = path.join(this.destPath, timestamp);
    
    // Step 1: 创建备份目录
    await fs.mkdir(backupDir, { recursive: true });
    
    // Step 2: 执行 rsync 增量备份
    execSync(`rsync -avz --delete ${this.sourcePath}/ ${backupDir}/`, {
      stdio: 'inherit',
      timeout: 7200000, // 2小时超时
    });
    
    // Step 3: 创建校验文件
    const checksum = await this.computeChecksum(backupDir);
    await fs.writeFile(
      path.join(backupDir, 'checksum.sha256'),
      checksum
    );
    
    // Step 4: 清理过期备份
    await this.cleanOldBackups();
    
    return {
      file: backupDir,
      checksum,
      size: await this.getDirSize(backupDir),
    };
  }

  /**
   * 计算目录校验和
   */
  async computeChecksum(dir) {
    const hash = crypto.createHash('sha256');
    const files = await fs.readdir(dir);
    for (const file of files.sort()) {
      const content = await fs.readFile(path.join(dir, file));
      hash.update(file).update(content);
    }
    return hash.digest('hex');
  }

  /**
   * 清理超过保留期的备份
   */
  async cleanOldBackups() {
    const cutoff = Date.now() - this.retentionDays * 86400000;
    const dirs = await fs.readdir(this.destPath);
    
    for (const dir of dirs) {
      const dirPath = path.join(this.destPath, dir);
      const stat = await fs.stat(dirPath);
      if (stat.isDirectory() && stat.mtimeMs < cutoff) {
        await fs.rm(dirPath, { recursive: true });
        console.log(`Cleaned old backup: ${dir}`);
      }
    }
  }

  sendAlert(err) {
    // 集成告警通道（Slack/PagerDuty）
    console.error(`[ALERT] Backup failed: ${err.message}`);
  }
}

// 使用示例
const scheduler = new BackupScheduler({
  sourcePath: '/data/production',
  destPath: '/backup/daily',
  retentionDays: 30,
});
scheduler.start('0 2 * * *'); // 每天凌晨2点执行

module.exports = BackupScheduler;
```

## Best Practices

> Industry-standard best practices for backup-data execution.

1. **Practice 1**: Implement automated backup schedules with verified restoration
2. **Practice 2**: Encrypt backup data at rest and in transit
3. **Practice 3**: Test recovery procedures quarterly with documented results


## Error Handling

> Common error scenarios and resolution strategies for backup-data.

### Error Scenario 1: 备份任务失败 (P1)

**触发条件**: 定时备份任务执行异常退出，或备份文件生成不完整（文件大小异常偏小），或备份进程返回非零退出码。

**处理流程**:
```
IF backup_job_status == failed OR backup_size < expected_size * 0.5
THEN
  1. 立即触发告警通知（PagerDuty/SMS），通知On-Call DBA和运维工程师
  2. 检查备份源端状态：数据库连接/文件系统权限/磁盘空间是否充足
  3. 查看备份客户端日志（/var/log/backup/），定位具体失败行和错误码
  4. 修复问题后手动触发增量备份，验证新备份文件完整性（checksum + sample restore）
  5. 补跑因失败遗漏的备份任务，更新备份状态仪表盘
END
```

**降级方案**: 切换至备用备份路径（如从主库切换到从库拿备份），或临时启用实时binlog同步作为过渡方案。

**升级条件**: 备份失败持续超过2个备份周期，或数据丢失风险被确认，需升级至技术总监和存储架构师。

### Error Scenario 2: 存储空间不足 (P1)

**触发条件**: 备份目标存储（本地磁盘/NFS挂载点/S3 Bucket）可用容量低于阈值（< 10%），或备份写入时返回磁盘已满（ENOSPC）错误。

**处理流程**:
```
IF storage_usage > 90% OR backup_write returns ENOSPC
THEN
  1. 暂停所有非关键备份任务，仅保留核心数据库备份
  2. 执行存储清理：按策略删除过期备份（超过保留期的全量/增量/归档文件）
  3. 触发冷备分层迁移：将超过30天的备份从热存储转移至Glacier/归档存储
  4. 扩容存储：动态增加EBS卷大小或扩展NFS容量配额
  5. 恢复暂停的备份任务，验证新备份写入正常
END
```

**降级方案**: 临时将新备份写入备用存储路径（如从主NAS切换到备用NAS，或从Tier1切到Tier2），待主存储扩容后迁移回。

**升级条件**: 紧急扩容操作 > 1小时未完成，或可用容量低于5%且无过期备份可清理，需升级至基础设施总监审批紧急存储扩容预算。

### Error Scenario 3: 恢复验证失败 (P0)

**触发条件**: 恢复演练或实际灾备恢复中，从备份文件还原的数据无法通过完整性校验（行数不符、checksum不匹配、主键冲突），或恢复后的服务无法正常启动。

**处理流程**:
```
IF restore_validation.status == failed AND (row_count_diff > 0 OR checksum_mismatch == true)
THEN
  1. 立即隔离恢复环境，防止不一致数据扩散到生产环境
  2. 回滚至上一个已知良好的备份时间点，重新执行恢复步骤
  3. 逐个验证备份文件链：全量备份 > 增量备份 > WAL/binlog归档的连续性和完整性
  4. 若文件链断裂，尝试从异地备份（offsite copy）拉取副本进行恢复
  5. 恢复成功后执行全量数据校验（表行数对比 + 关键字段checksum + 业务探活ping），出具恢复验证报告
END
```

**降级方案**: 从异地灾备站点（DR Site）的完整副本直接拉起服务，接受最多1小时的数据回退窗口。启动生产环境从灾备站点的流量切换预案。

**升级条件**: P0级别恢复失败立即触发War Room，召集DBA、基础架构、应用开发和业务Owner四方会诊；若30分钟内无法从任一备份副本成功恢复，需启动异地灾备切换流程。


## Quality Standards

> Acceptance criteria and quality gates for backup-data deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | Backup success rate is 99.5% or higher | Automated check |
| Standard 2 | Recovery point objective (RPO) is consistently met | Automated check |
| Standard 3 | Quarterly recovery drills pass validation checks | Automated check |
## References

- [harness-engineering.md](../standards/harness-engineering.md)
- [output-validation-checklist.md](../evaluations/output-validation-checklist.md)
- [regression-checklist.md](../evaluations/regression-checklist.md)
