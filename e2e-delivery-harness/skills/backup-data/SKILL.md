---
name: backup-data
description: "Domain skill for backup-data execution"
category: operations
type: skill
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-23
status: active
tags: ['skill', 'knowledge']
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

### Backup Implementation Examples

#### Java: Spring Boot Backup Scheduler

```java
// Java implementation - Spring Boot scheduled database backup
// Dependencies: spring-boot-starter, spring-boot-starter-jdbc
package com.example.backup;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import javax.annotation.PostConstruct;
import java.io.IOException;
import java.nio.file.*;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

@Component
@EnableScheduling
public class DatabaseBackupScheduler {
    private static final Logger log = LoggerFactory.getLogger(DatabaseBackupScheduler.class);

    @Value("${backup.db.host}")
    private String dbHost;

    @Value("${backup.db.name}")
    private String dbName;

    @Value("${backup.db.user}")
    private String dbUser;

    @Value("${backup.db.password}")
    private String dbPassword;

    @Value("${backup.output.dir:/data/backups}")
    private String outputDir;

    @Value("${backup.retention.days:30}")
    private int retentionDays;

    @PostConstruct
    public void init() throws IOException {
        Files.createDirectories(Paths.get(outputDir));
    }

    // Full backup every Sunday at 2:00 AM
    @Scheduled(cron = "0 0 2 * * SUN")
    public void fullBackup() throws Exception {
        String timestamp = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyyMMdd_HHmmss"));
        String filename = String.format("%s/full_%s_%s.sql.gz", outputDir, dbName, timestamp);

        ProcessBuilder pb = new ProcessBuilder(
            "mysqldump",
            "--host=" + dbHost,
            "--user=" + dbUser,
            "--password=" + dbPassword,
            "--single-transaction",
            "--routines",
            "--triggers",
            "--events",
            dbName
        );

        // Pipe through gzip for compression
        pb.redirectOutput(ProcessBuilder.Redirect.to(new java.io.File(filename)));
        Process process = pb.start();

        int exitCode = process.waitFor();
        if (exitCode != 0) {
            throw new RuntimeException("Backup failed with exit code: " + exitCode);
        }

        log.info("Full backup completed: {}", filename);
        cleanupOldBackups();
    }

    private void cleanupOldBackups() throws IOException {
        Path backupDir = Paths.get(outputDir);
        LocalDateTime cutoff = LocalDateTime.now().minusDays(retentionDays);

        try (DirectoryStream<Path> stream = Files.newDirectoryStream(backupDir, "*.sql.gz")) {
            for (Path entry : stream) {
                FileTime creationTime = (FileTime) Files.getAttribute(entry, "creationTime");
                LocalDateTime fileTime = creationTime.toInstant()
                    .atZone(java.time.ZoneId.systemDefault()).toLocalDateTime();
                if (fileTime.isBefore(cutoff)) {
                    Files.delete(entry);
                    log.info("Deleted expired backup: {}", entry.getFileName());
                }
            }
        }
    }
}
```

#### Go: Cron Backup Service

```go
// Go implementation - Cron-backed database backup service
// Dependencies: github.com/robfig/cron/v3
package main

import (
    "compress/gzip"
    "fmt"
    "io"
    "log"
    "os"
    "os/exec"
    "path/filepath"
    "time"

    "github.com/robfig/cron/v3"
)

type BackupConfig struct {
    DBHost        string
    DBPort        string
    DBUser        string
    DBPassword    string
    DBName        string
    OutputDir     string
    RetentionDays int
}

type BackupService struct {
    config BackupConfig
}

func NewBackupService(config BackupConfig) *BackupService {
    if err := os.MkdirAll(config.OutputDir, 0755); err != nil {
        log.Fatalf("create backup dir: %v", err)
    }
    return &BackupService{config: config}
}

// RunFullBackup executes a full database backup with compression
func (s *BackupService) RunFullBackup() error {
    timestamp := time.Now().Format("20060102_150405")
    filename := fmt.Sprintf("full_%s_%s.sql.gz", s.config.DBName, timestamp)
    filepath := filepath.Join(s.config.OutputDir, filename)

    // Create gzipped output file
    f, err := os.Create(filepath)
    if err != nil {
        return fmt.Errorf("create file: %w", err)
    }
    defer f.Close()

    gzWriter := gzip.NewWriter(f)
    defer gzWriter.Close()

    // Execute mysqldump
    cmd := exec.Command("mysqldump",
        "--host="+s.config.DBHost,
        "--port="+s.config.DBPort,
        "--user="+s.config.DBUser,
        "--password="+s.config.DBPassword,
        "--single-transaction",
        "--routines",
        "--triggers",
        "--events",
        s.config.DBName,
    )

    stdout, err := cmd.StdoutPipe()
    if err != nil {
        return fmt.Errorf("create stdout pipe: %w", err)
    }

    if err := cmd.Start(); err != nil {
        return fmt.Errorf("start mysqldump: %w", err)
    }

    written, err := io.Copy(gzWriter, stdout)
    if err != nil {
        return fmt.Errorf("compress backup: %w", err)
    }

    if err := cmd.Wait(); err != nil {
        return fmt.Errorf("mysqldump failed: %w", err)
    }

    log.Printf("full backup completed: %s (%d bytes)", filepath, written)
    s.cleanupOldBackups()
    return nil
}

// cleanupOldBackups removes backups older than retention period
func (s *BackupService) cleanupOldBackups() {
    cutoff := time.Now().AddDate(0, 0, -s.config.RetentionDays)

    filepath.Walk(s.config.OutputDir, func(path string, info os.FileInfo, err error) error {
        if err != nil || info.IsDir() {
            return err
        }
        if info.ModTime().Before(cutoff) && filepath.Ext(path) == ".gz" {
            if err := os.Remove(path); err != nil {
                log.Printf("failed to remove %s: %v", path, err)
            } else {
                log.Printf("removed expired backup: %s", path)
            }
        }
        return nil
    })
}

func main() {
    config := BackupConfig{
        DBHost:        getEnv("DB_HOST", "localhost"),
        DBPort:        getEnv("DB_PORT", "3306"),
        DBUser:        getEnv("DB_USER", "root"),
        DBPassword:    getEnv("DB_PASSWORD", ""),
        DBName:        getEnv("DB_NAME", "mydb"),
        OutputDir:     getEnv("BACKUP_DIR", "/data/backups"),
        RetentionDays: 30,
    }

    service := NewBackupService(config)

    c := cron.New()
    // Daily backup at 1:00 AM
    c.AddFunc("0 1 * * *", func() {
        if err := service.RunFullBackup(); err != nil {
            log.Printf("backup failed: %v", err)
        }
    })
    c.Start()

    log.Println("backup service started")
    select {} // block forever
}

func getEnv(key, fallback string) string {
    if val := os.Getenv(key); val != "" {
        return val
    }
    return fallback
}
```

#### Node.js: node-cron Backup Script

```javascript
// Node.js implementation - node-cron scheduled backup script
// Dependencies: node-cron, mysql2, archiver (npm install node-cron mysql2 archiver)
const cron = require('node-cron');
const mysql = require('mysql2/promise');
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const { createGzip } = require('zlib');
const { createReadStream, createWriteStream } = require('fs');
const { pipeline } = require('stream/promises');

class BackupService {
    constructor(config) {
        this.config = config;
        this.ensureDir(config.outputDir);
    }

    ensureDir(dir) {
        if (!fs.existsSync(dir)) {
            fs.mkdirSync(dir, { recursive: true });
        }
    }

    async runFullBackup() {
        const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
        const filename = `full_${this.config.dbName}_${timestamp}.sql.gz`;
        const filepath = path.join(this.config.outputDir, filename);

        const dumpArgs = [
            `--host=${this.config.dbHost}`,
            `--port=${this.config.dbPort}`,
            `--user=${this.config.dbUser}`,
            `--password=${this.config.dbPassword}`,
            '--single-transaction',
            '--routines',
            '--triggers',
            '--events',
            this.config.dbName,
        ];

        try {
            const startTime = Date.now();

            // Execute mysqldump and pipe through gzip
            const { spawn } = require('child_process');
            const dump = spawn('mysqldump', dumpArgs);
            const gzip = createGzip();
            const output = createWriteStream(filepath);

            await pipeline(dump.stdout, gzip, output);

            const duration = ((Date.now() - startTime) / 1000).toFixed(2);
            const stats = fs.statSync(filepath);
            const sizeMB = (stats.size / 1024 / 1024).toFixed(2);

            console.log(`[Backup] Completed: ${filename} (${sizeMB}MB in ${duration}s)`);
            await this.cleanupOldBackups();
            return { filename, sizeMB, duration };
        } catch (err) {
            console.error(`[Backup] Failed: ${err.message}`);
            throw err;
        }
    }

    async backupToCloud(s3Client, bucket) {
        // Upload to S3-compatible storage after local backup
        const result = await this.runFullBackup();
        const filepath = path.join(this.config.outputDir, result.filename);

        const fileStream = createReadStream(filepath);
        await s3Client.putObject({
            Bucket: bucket,
            Key: `backups/${result.filename}`,
            Body: fileStream,
        });
        console.log(`[Backup] Uploaded to S3: ${result.filename}`);
    }

    async cleanupOldBackups() {
        const cutoff = Date.now() - (this.config.retentionDays * 24 * 60 * 60 * 1000);
        const files = fs.readdirSync(this.config.outputDir);

        for (const file of files) {
            if (!file.endsWith('.gz')) continue;
            const filepath = path.join(this.config.outputDir, file);
            const stat = fs.statSync(filepath);
            if (stat.mtimeMs < cutoff) {
                fs.unlinkSync(filepath);
                console.log(`[Backup] Removed expired: ${file}`);
            }
        }
    }

    start() {
        // Schedule: daily at 2:00 AM
        const expression = this.config.cronExpression || '0 2 * * *';
        cron.schedule(expression, () => {
            this.runFullBackup().catch(err => {
                console.error(`[Backup] Scheduled backup error: ${err.message}`);
            });
        });
        console.log(`[Backup] Service started, schedule: ${expression}`);
    }
}

// Usage
const backupService = new BackupService({
    dbHost: process.env.DB_HOST || 'localhost',
    dbPort: process.env.DB_PORT || '3306',
    dbUser: process.env.DB_USER || 'root',
    dbPassword: process.env.DB_PASSWORD,
    dbName: process.env.DB_NAME || 'mydb',
    outputDir: process.env.BACKUP_DIR || '/data/backups',
    retentionDays: parseInt(process.env.RETENTION_DAYS || '30', 10),
    cronExpression: '0 2 * * *',
});

backupService.start();
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
- **3-2-1 备份原则**: 至少保留 3 份数据副本，存储在 2 种不同存储介质上，其中 1 份存放在异地，防止单点故障。
- **全量/增量/差异备份**: 全量备份完整数据；增量备份仅备份上次任意备份后的变化；差异备份备份上次全量备份后的变化。
- **WAL (Write-Ahead Log) 备份**: 数据库预写日志备份支持时间点恢复(PITR)，实现秒级数据恢复精度。

### Key Principles
1. **备份必须可恢复**: 备份的核心目的是恢复，未经验证可恢复的备份等同于没有备份，定期验证备份完整性。
2. **异地存储强制化**: 所有关键数据的至少一份副本必须存放在异地（不同可用区、不同区域），抵御区域性灾难。
3. **备份加密不可省略**: 备份数据在传输和存储阶段必须加密，防止存储介质泄露导致数据泄露。


## Best Practices

> Proven practices for backup-data excellence.

1. **定期恢复演练 (每季度)**: 每季度至少执行一次全流程恢复演练，验证备份数据的可恢复性和恢复时间是否符合 RTO 要求。
2. **备份完整性自动校验**: 每次备份完成后自动执行校验（校验和比对、抽样恢复验证），确保备份文件未损坏。
3. **冷热数据分层备份**: 根据数据访问频率和恢复需求，制定分层备份策略——热数据快速备份恢复，冷数据压缩归档降成本。


## Anti-patterns (反模式)

> 与 Common Pitfalls 同义，执行时合并检查。

## Common Pitfalls

> Frequent mistakes to avoid during backup-data execution.

### Pitfall 1: 备份成功但恢复失败 (Backup Succeeds But Restore Fails)
**Risk**: 备份日志显示成功，但恢复时发现备份文件损坏或不完整，无法正常恢复数据。
**Prevention**: 每次备份完成后自动执行恢复验证（如恢复至隔离环境并校验数据一致性），而非仅检查文件存在性。
**Impact**: 灾难发生时发现无法恢复数据，造成不可逆的数据丢失，业务连续性完全中断。

### Pitfall 2: 只备份数据不备份配置 (Data-Only Backup)
**Risk**: 仅备份数据库数据而未备份应用配置、环境变量、网络策略等，恢复后服务无法正常工作。
**Prevention**: 将配置管理纳入备份范围，使用 IaC 工具管理配置并归档，确保恢复时能完整重建环境。
**Impact**: 数据恢复后应用无法启动，需要手工配置环境，恢复时间远超 RTO。

### Pitfall 3: 忽视备份存储成本增长 (Ignoring Backup Cost Growth)
**Risk**: 随着数据量增长，备份存储成本线性上升，未及时优化导致成本失控。
**Prevention**: 实施数据生命周期管理，定期评估备份保留策略，使用分层存储（热/冷/归档）降低长期成本。
**Impact**: 备份成本占 IT 预算比例过高，为降低成本被迫缩短保留周期，违反合规要求。
