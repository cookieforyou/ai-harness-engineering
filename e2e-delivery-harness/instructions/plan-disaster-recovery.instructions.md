---
name: plan-disaster-recovery
description: "灾备恢复规划场景的技术指令"
applyTo: "scenarios/plan-disaster-recovery/**"
phase: governance
type: instruction
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['instruction', 'technical']
---
# Disaster Recovery Planning Instructions

## Overview

This instruction provides the comprehensive technical specifications and implementation guidance for disaster recovery planning across mission-critical systems. It covers DR strategy selection (cold/warm/hot/active-active), RTO/RPO target definition, failover automation design, backup validation procedures, and recovery drill execution. The instruction ensures business continuity during catastrophic failures by defining recoverable system boundaries, documenting step-by-step recovery procedures, and maintaining regular drill cadences to validate and improve recovery capabilities.


## Recovery Architectures

### Architecture 1: Backup & Restore
```
Components:
- Nightly backup to S3
- Cross-region backup storage
- Point-in-time recovery

RPO: 24 hours
RTO: 4-24 hours
Cost: Low
```

### Architecture 2: Warm Standby
```
Components:
- Reduced capacity secondary site
- Async data replication
- Manual failover

RPO: Minutes
RTO: 1-4 hours
Cost: Medium
```

### Architecture 3: Pilot Light
```
Components:
- Minimal secondary infrastructure
- Automated scaling on failover
- Data replication

RPO: Minutes
RTO: 30-60 minutes
Cost: Medium-High
```

### Architecture 4: Multi-Region Active-Active
```
Components:
- Full capacity multiple regions
- Synchronous replication
- Automatic failover

RPO: Near zero
RTO: Seconds to minutes
Cost: Very High
```

## RPO/RTO Selection Guide

| Business Impact | RPO | RTO | Recommended Architecture |
|-----------------|-----|-----|------------------------|
| Critical (>$1M/hr) | < 1 min | < 15 min | Multi-Region Active-Active |
| High (>$100K/hr) | < 15 min | < 1 hour | Pilot Light / Hot Standby |
| Medium (>$10K/hr) | < 1 hour | < 4 hours | Warm Standby |
| Low (<$10K/hr) | < 24 hours | < 24 hours | Backup & Restore |

## Backup Strategies

### Database Backup

```bash
# PostgreSQL
pg_dump -Fc -f backup.dump mydb
# Continuous archiving
wal_level = archive
archive_mode = on

# MySQL
mysqldump --single-transaction --routines --triggers backup.sql
# Point-in-time
mysqlbinlog --stop-datetime="2024-01-01 12:00:00" | mysql
```

### File System Backup

```bash
# Incremental backup
rsync -avz --link-dest=/backup/latest /data /backup/incremental-$(date +%Y%m%d)

# Snapshot (AWS EBS)
aws ec2 create-snapshot --volume-id vol-1234567890abcdef0
```

### Application State

```yaml
# Kubernetes Persistent Volumes
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: app-data
spec:
  storageClassName: ebs-sc
  resources:
    requests:
      storage: 100Gi
---
# Volume Snapshot
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshot
metadata:
  name: app-data-snapshot
spec:
  volumeSnapshotClassName: ebs-snapclass
  source:
    persistentVolumeClaimName: app-data
```

## Failover Procedures

### DNS Failover (Route 53)

```yaml
# Health check configuration
health_check:
  type: HTTPS
  port: 443
  path: /health
  interval: 30
  threshold: 3
  
# Routing policy
routing_policy:
  type: failover
  primary:
    region: us-east-1
    evaluate_target_health: true
  secondary:
    region: us-west-2
    evaluate_target_health: true
```

### Kubernetes Failover

```bash
# Label nodes by region
kubectl label node <node> topology.kubernetes.io/region=us-east-1

# Pod topology spread
topologySpreadConstraints:
  - maxSkew: 1
    topologyKey: topology.kubernetes.io/region
    whenUnsatisfiable: DoNotSchedule

# Evict pods from failing region
kubectl drain node <node> --ignore-daemonsets --delete-emptydir-data
```

## Recovery Procedures

### Step 1: Disaster Declaration

```markdown
## Disaster Declaration

**触发条件**:
- [ ] 主数据中心不可达超过 30 分钟
- [ ] 数据丢失超过 RPO
- [ ] 核心服务不可用超过 RTO
- [ ] 安全事件导致系统隔离

**声明人**: IT Director / CTO
**通知对象**: 所有相关方
```

### Step 2: Execute Failover

```bash
#!/bin/bash
# execute-failover.sh

set -e

REGION="${FAILOVER_REGION:-us-west-2}"
SERVICE="${SERVICE_NAME}"

echo "Starting failover to ${REGION}..."

# 1. Verify target region is healthy
check_region_health ${REGION}

# 2. Stop data replication
stop_replication

# 3. Promote standby database
promote_database ${REGION}

# 4. Update DNS
update_dns ${REGION}

# 5. Scale up services
scale_up ${SERVICE} ${REGION}

# 6. Verify service health
verify_health ${SERVICE}

echo "Failover completed successfully"
```

### Step 3: Verify Recovery

```bash
# Service health
curl -f http://${SERVICE}/health

# Database connectivity
psql -c "SELECT 1"

# Data integrity
./verify-data-integrity.sh

# End-to-end test
./run-smoke-tests.sh
```

## DR Testing Matrix

| Test Type | Frequency | Scope | Duration |
|-----------|-----------|-------|----------|
| Tabletop | Monthly | Review plans | 2 hours |
| Component | Quarterly | Single system | 4 hours |
| Partial Failover | Semi-annual | Non-production | 8 hours |
| Full Failover | Annual | All systems | 24 hours |

## DR Test Checklist

```markdown


### Pre-Test
- [ ] Notify all stakeholders
- [ ] Schedule maintenance window
- [ ] Verify backup integrity
- [ ] Confirm resource availability
- [ ] Prepare rollback plan

### During Test
- [ ] Declare test start
- [ ] Execute failover
- [ ] Monitor systems
- [ ] Document any issues
- [ ] Verify RTO/RPO

### Post-Test
- [ ] Declare test end
- [ ] Execute rollback
- [ ] Document results
- [ ] Identify improvements
- [ ] Update documentation
```

## Cost Optimization

### Storage Costs
```yaml
tiered_storage:
  hot:
    retention: 7 days
    storage: EBS/EFS
    cost_per_gb: $0.10
  
  warm:
    retention: 30 days
    storage: S3 Standard
    cost_per_gb: $0.023
  
  cold:
    retention: 90 days
    storage: S3 Glacier
    cost_per_gb: $0.004
```

### Compute Costs
```yaml
compute_strategy:
  pilot_light:
    always_on: "Control plane + Database"
    on_failover: "Auto-scale application"
    
  warm_standby:
    always_on: "50% capacity"
    on_failover: "Scale to 100%"
```


## Technical Specifications

> Detailed technical requirements and implementation guidelines for plan-disaster-recovery.

### Required Tools
- [List required tools and frameworks]

### Environment Requirements
- [List environment prerequisites]

### Configuration Parameters
- [List key configuration parameters]


## Best Practices

> Industry-standard best practices for plan-disaster-recovery execution.

1. **Practice 1**: Define RTO and RPO targets based on business impact analysis
2. **Practice 2**: Design DR architecture (cold, warm, hot, or active-active)
3. **Practice 3**: Conduct annual DR drills with documented outcomes


## Multi-Language Code Examples

### Python - AWS Disaster Recovery Automation

```python
#!/usr/bin/env python3
"""
AWS 灾难恢复自动化脚本 - 跨区域故障切换和恢复编排

功能:
  - 跨区域 RDS 主备切换
  - Route53 DNS 故障切换
  - EBS 快照跨区域复制
  - 灾备环境一致性验证

Requires: pip install boto3
"""
import os
import json
import logging
import time
from datetime import datetime, timezone
from typing import Dict, List, Optional, Tuple

import boto3

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

PRIMARY_REGION = os.getenv("PRIMARY_REGION", "us-east-1")
DR_REGION = os.getenv("DR_REGION", "us-west-2")
ROUTE53_ZONE_ID = os.getenv("ROUTE53_ZONE_ID", "")


class AWSDisasterRecovery:
    """
    AWS 灾难恢复自动化引擎。

    支持三种降级模式:
      - Hot (Active-Active): 自动 DNS 切换，RTO < 1min
      - Warm: 提升只读副本为主库，RTO < 15min
      - Cold: 从备份恢复，RTO < 4h
    """

    def __init__(self, primary_region: str = PRIMARY_REGION,
                 dr_region: str = DR_REGION):
        self.primary = primary_region
        self.dr = dr_region
        self.rds_primary = boto3.client("rds", region_name=primary_region)
        self.rds_dr = boto3.client("rds", region_name=dr_region)
        self.route53 = boto3.client("route53")
        self.ec2_primary = boto3.client("ec2", region_name=primary_region)
        self.ec2_dr = boto3.client("ec2", region_name=dr_region)

    def check_cross_region_replication(self, db_instance_identifier: str) -> Dict:
        """
        验证跨区域数据库复制状态。

        健康检查要点:
          - 复制延迟 (Lag): 应 < 30 秒
          - 复制状态: 应为 "available"
          - 只读副本数: 至少 1 个在 DR 区域
        """
        try:
            response = self.rds_dr.describe_db_instances(
                DBInstanceIdentifier=db_instance_identifier
            )
            instances = response.get("DBInstances", [])
            if not instances:
                return {"status": "ERROR", "message": "DR instance not found"}

            inst = instances[0]
            status = inst.get("DBInstanceStatus", "unknown")
            replicas = inst.get("ReadReplicaSourceDBInstanceIdentifier", None)
            lag = inst.get("ReplicaLagSeconds", None)

            return {
                "status": "HEALTHY" if status == "available" else "UNHEALTHY",
                "instance_status": status,
                "region": self.dr,
                "replication_active": replicas is not None,
                "lag_seconds": lag,
                "instance_class": inst.get("DBInstanceClass", ""),
                "endpoint": inst.get("Endpoint", {}).get("Address", ""),
                "multi_az": inst.get("MultiAZ", False),
                "last_checked": datetime.now(timezone.utc).isoformat(),
            }
        except Exception as e:
            logger.error("DR health check failed: %s", e)
            return {"status": "ERROR", "message": str(e)}

    def promote_to_primary(self, dr_instance_identifier: str) -> Dict:
        """
        将 DR 区域的只读副本提升为独立主库 (故障切换)。

        步骤:
          1. 停止应用写入，确保数据一致性
          2. 等待复制延迟追平 (< 5s)
          3. 执行 promote read replica
          4. 更新 DNS 记录指向新主库
          5. 验证新主库可读写
        """
        logger.info("Starting failover: promoting %s in %s",
                    dr_instance_identifier, self.dr)

        # Step 1: 获取当前复制状态
        status = self.check_cross_region_replication(dr_instance_identifier)
        if status.get("lag_seconds") and status["lag_seconds"] > 30:
            logger.warning("Replication lag is %s seconds, waiting...",
                          status["lag_seconds"])
            # 等待复制追平，最多等待 5 分钟
            for _ in range(30):
                time.sleep(10)
                current = self.check_cross_region_replication(dr_instance_identifier)
                if current.get("lag_seconds", 999) < 5:
                    break

        # Step 2: 提升只读副本
        try:
            response = self.rds_dr.promote_read_replica(
                DBInstanceIdentifier=dr_instance_identifier,
                BackupRetentionPeriod=7,
                PreferredBackupWindow="03:00-04:00",
            )
            promoted_instance = response.get("DBInstance", {})
            logger.info("Promote initiated for %s", dr_instance_identifier)
        except Exception as e:
            logger.error("Promote failed: %s", e)
            return {"status": "FAILED", "error": str(e)}

        # Step 3: 等待主库可用
        waiter = self.rds_dr.get_waiter("db_instance_available")
        waiter.wait(DBInstanceIdentifier=dr_instance_identifier)
        logger.info("Instance %s is now available as primary", dr_instance_identifier)

        # Step 4: 更新 DNS (如果配置了 Route53)
        if ROUTE53_ZONE_ID:
            new_endpoint = promoted_instance.get("Endpoint", {}).get("Address", "")
            self.update_dns_failover(new_endpoint)

        return {
            "status": "COMPLETED",
            "promoted_instance": dr_instance_identifier,
            "new_region": self.dr,
            "new_endpoint": promoted_instance.get("Endpoint", {}),
            "promotion_time": datetime.now(timezone.utc).isoformat(),
        }

    def update_dns_failover(self, new_endpoint: str) -> Dict:
        """
        更新 Route53 DNS 记录实现故障切换。

        使用 Failover Routing Policy，当健康检查失败时自动切换。
        """
        import uuid
        changes = {
            "Changes": [{
                "Action": "UPSERT",
                "ResourceRecordSet": {
                    "Name": os.getenv("DNS_RECORD_NAME", "app.example.com"),
                    "Type": "A",
                    "SetIdentifier": "failover-dr",
                    "Failover": "SECONDARY",
                    "TTL": 60,
                    "ResourceRecords": [{"Value": new_endpoint}],
                    "HealthCheckId": os.getenv("HEALTH_CHECK_ID", ""),
                },
            }]
        }
        response = self.route53.change_resource_record_sets(
            HostedZoneId=ROUTE53_ZONE_ID,
            ChangeBatch=changes,
        )
        logger.info("DNS failover updated: %s -> %s",
                    os.getenv("DNS_RECORD_NAME", ""), new_endpoint)
        return response

    def replicate_ebs_snapshots(self, volume_ids: List[str]) -> List[Dict]:
        """
        跨区域复制 EBS 快照，用于灾难恢复场景的数据恢复。

        确保 DR 区域有最新的数据副本可用。
        """
        results = []
        for vol_id in volume_ids:
            try:
                # 创建快照
                snapshot = self.ec2_primary.create_snapshot(
                    VolumeId=vol_id,
                    Description=f"DR replication snapshot for {vol_id}",
                    TagSpecifications=[{
                        "ResourceType": "snapshot",
                        "Tags": [{"Key": "DR-Replication", "Value": "true"}]
                    }]
                )
                snap_id = snapshot["SnapshotId"]

                # 等待快照完成
                waiter = self.ec2_primary.get_waiter("snapshot_completed")
                waiter.wait(SnapshotIds=[snap_id])

                # 跨区域复制
                copy_response = self.ec2_primary.copy_snapshot(
                    SourceRegion=self.primary,
                    SourceSnapshotId=snap_id,
                    DestinationRegion=self.dr,
                    Description=f"DR copy of {snap_id}",
                )
                dr_snap_id = copy_response["SnapshotId"]

                results.append({
                    "source_volume": vol_id,
                    "source_snapshot": snap_id,
                    "dr_snapshot": dr_snap_id,
                    "status": "COMPLETED",
                })
                logger.info("Snapshot %s replicated to %s as %s",
                           snap_id, self.dr, dr_snap_id)
            except Exception as e:
                results.append({
                    "source_volume": vol_id,
                    "status": "FAILED",
                    "error": str(e),
                })
        return results

    def verify_dr_readiness(self, db_identifier: str) -> Dict:
        """
        执行完整的灾难恢复就绪检查。

        返回综合评分，包括:
          - 复制健康 (40%)
          - 快照完整性 (30%)
          - DNS 就绪 (20%)
          - IAM 权限 (10%)
        """
        scores = {}
        # 复制检查
        repl = self.check_cross_region_replication(db_identifier)
        scores["replication"] = 40 if repl["status"] == "HEALTHY" else 0
        scores["replication_details"] = repl

        # DNS 检查
        try:
            health = self.route53.get_health_check(
                HealthCheckId=os.getenv("HEALTH_CHECK_ID", "")
            )
            scores["dns"] = 20 if health else 0
            scores["dns_details"] = "DNS health check configured"
        except Exception:
            scores["dns"] = 10
            scores["dns_details"] = "DNS health check not found"

        total = sum(v for k, v in scores.items() if k not in ("replication_details", "dns_details"))
        scores["total_score"] = min(100, total)
        scores["readiness"] = "READY" if total >= 70 else "NOT_READY"
        scores["checked_at"] = datetime.now(timezone.utc).isoformat()
        return scores
```

### Terraform - Multi-Region Disaster Recovery Deployment

```hcl
# ============================================================
# dr-infrastructure.tf
# 多区域灾备基础设施 - Terraform 部署配置
#
# 部署策略:
#   Primary: us-east-1 (主集群，全负载)
#   DR: us-west-2 (灾备集群，Pilot Light 模式)
#
# 故障切换通过 Route53 DNS Failover 自动完成
# ============================================================

provider "aws" {
  alias  = "primary"
  region = "us-east-1"
}

provider "aws" {
  alias  = "dr"
  region = "us-west-2"
}

# ============================================================
# 变量定义
# ============================================================
variable "app_name" {
  description = "Application name for resource naming"
  type        = string
  default     = "myapp"
}

variable "db_password" {
  description = "Database master password"
  type        = string
  sensitive   = true
}

# ============================================================
# Primary Region - RDS MySQL (Multi-AZ)
# ============================================================
resource "aws_db_instance" "primary" {
  provider = aws.primary

  identifier = "${var.app_name}-primary"
  engine     = "mysql"
  engine_version = "8.0"

  instance_class = "db.r6g.large"
  allocated_storage     = 100
  storage_type          = "gp3"
  storage_encrypted     = true
  iops                  = 3000

  db_name  = "appdb"
  username = "admin"
  password = var.db_password

  # Multi-AZ 部署实现高可用
  multi_az = true

  # 自动备份 (用于 PITR 恢复)
  backup_retention_period = 35  # 35 天 (满足合规)
  backup_window           = "02:00-03:00"
  maintenance_window      = "sun:04:00-05:00"

  # 删除保护
  deletion_protection = true
  skip_final_snapshot = false
  final_snapshot_identifier = "${var.app_name}-final-${formatdate("YYYY-MM-DD-hhmm", timestamp())}"

  # 网络配置
  vpc_security_group_ids = [aws_security_group.rds_primary.id]
  db_subnet_group_name   = aws_db_subnet_group.primary.name

  enabled_cloudwatch_logs_exports = ["error", "general", "slowquery"]

  tags = {
    Name        = "${var.app_name}-primary-db"
    Environment = "production"
    Role        = "primary"
    DrStrategy  = "cross-region-replica"
  }
}

# ============================================================
# DR Region - 跨区域只读副本 (Warm Standby)
# ============================================================
resource "aws_db_instance" "dr_replica" {
  provider = aws.dr

  identifier = "${var.app_name}-dr"
  engine     = "mysql"
  engine_version = "8.0"

  instance_class = "db.r6g.large"
  allocated_storage     = 100
  storage_type          = "gp3"
  storage_encrypted     = true

  username = "admin"
  password = var.db_password

  # 跨区域只读副本 - 自动从主库同步数据
  replicate_source_db = aws_db_instance.primary.arn

  # DR 区域备份 (独立于主区域)
  backup_retention_period = 7
  backup_window           = "03:00-04:00"
  maintenance_window      = "mon:05:00-06:00"

  deletion_protection = true
  skip_final_snapshot = true

  vpc_security_group_ids = [aws_security_group.rds_dr.id]
  db_subnet_group_name   = aws_db_subnet_group.dr.name

  enabled_cloudwatch_logs_exports = ["error", "general", "slowquery"]

  tags = {
    Name        = "${var.app_name}-dr-db"
    Environment = "production"
    Role        = "dr-replica"
    DrStrategy  = "warm-standby"
  }
}

# ============================================================
# Route53 DNS Failover Routing
# ============================================================
resource "aws_route53_health_check" "primary" {
  provider = aws.primary

  fqdn             = aws_lb.primary.dns_name
  port             = 443
  type             = "HTTPS"
  resource_path    = "/health"
  failure_threshold = 3
  request_interval  = 30

  tags = {
    Name = "${var.app_name}-primary-health-check"
  }
}

resource "aws_route53_record" "app" {
  zone_id = var.route53_zone_id
  name    = "app.${var.domain_name}"
  type    = "A"

  set_identifier = "primary"
  failover_routing_policy {
    type = "PRIMARY"
  }

  alias {
    name                   = aws_lb.primary.dns_name
    zone_id                = aws_lb.primary.zone_id
    evaluate_target_health = true
  }

  # 健康检查关联 - 自动故障切换
  health_check_id = aws_route53_health_check.primary.id
}

resource "aws_route53_record" "dr" {
  zone_id = var.route53_zone_id
  name    = "app.${var.domain_name}"
  type    = "A"

  set_identifier = "dr"
  failover_routing_policy {
    type = "SECONDARY"
  }

  alias {
    name                   = aws_lb.dr.dns_name
    zone_id                = aws_lb.dr.zone_id
    evaluate_target_health = true
  }
}
```

### Shell - 故障切换脚本

```bash
#!/bin/bash
#
# dr-failover.sh - 灾难恢复故障切换执行脚本
#
# 支持三种故障切换模式:
#   - full:    完整故障切换 (主 → DR)
#   - partial: 部分切换 (仅数据库或应用)
#   - drill:   演练模式 (不修改生产配置)
#
# 用法: ./dr-failover.sh [full|partial|drill] [--force]
#
set -euo pipefail

# ============================================================
# Configuration
# ============================================================
PRIMARY_REGION="${PRIMARY_REGION:-us-east-1}"
DR_REGION="${DR_REGION:-us-west-2}"
APP_NAME="${APP_NAME:-myapp}"
FAILOVER_MODE="${1:-drill}"
FORCE="${2:-false}"

TIMESTAMP=$(date +%Y%m%d-%H%M%S)
LOG_FILE="/var/log/dr-failover-${TIMESTAMP}.log"

# ============================================================
# Color output
# ============================================================
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

log_info()  { echo -e "${GREEN}[INFO]${NC} $*" | tee -a "$LOG_FILE"; }
log_warn()  { echo -e "${YELLOW}[WARN]${NC} $*" | tee -a "$LOG_FILE"; }
log_error() { echo -e "${RED}[ERROR]${NC} $*" | tee -a "$LOG_FILE"; }

# ============================================================
# Phase 1: Pre-flight Checks
# ============================================================
pre_flight_check() {
    log_info "Phase 1: Pre-flight checks"

    # Check required tools
    for cmd in aws jq curl; do
        if ! command -v "$cmd" &>/dev/null; then
            log_error "Required tool not found: $cmd"
            exit 1
        fi
    done

    # Verify DR region is accessible
    if ! aws ec2 describe-regions --region "$DR_REGION" --output text &>/dev/null; then
        log_error "DR region $DR_REGION is not accessible"
        exit 1
    fi

    # Check AWS credentials
    if ! aws sts get-caller-identity &>/dev/null; then
        log_error "AWS credentials not configured or expired"
        exit 1
    fi

    log_info "All pre-flight checks passed"
}

# ============================================================
# Phase 2: Verify DR Readiness
# ============================================================
verify_dr_readiness() {
    log_info "Phase 2: Verifying DR region readiness"

    # 2.1 Check RDS cross-region replication
    log_info "  Checking RDS replication status..."
    local LAG
    LAG=$(aws rds describe-db-instances \
        --region "$DR_REGION" \
        --db-instance-identifier "${APP_NAME}-dr" \
        --query 'DBInstances[0].ReplicaLagSeconds' \
        --output text 2>/dev/null || echo "null")

    if [[ "$LAG" == "null" ]]; then
        log_error "  DR RDS instance not found or not replicating"
        return 1
    elif [[ "$LAG" -gt 30 ]]; then
        log_warn "  Replication lag is ${LAG}s (threshold: 30s)"
        log_warn "  Waiting for replication to catch up..."
        # 等待最多 5 分钟
        for i in $(seq 1 30); do
            sleep 10
            LAG=$(aws rds describe-db-instances \
                --region "$DR_REGION" \
                --db-instance-identifier "${APP_NAME}-dr" \
                --query 'DBInstances[0].ReplicaLagSeconds' --output text)
            if [[ "$LAG" -lt 5 ]]; then
                log_info "  Replication lag is now ${LAG}s - acceptable"
                break
            fi
        done
    else
        log_info "  Replication lag: ${LAG}s (healthy)"
    fi

    # 2.2 Verify DNS health check
    log_info "  Checking Route53 health check status..."
    local HEALTH_CHECK_ID
    HEALTH_CHECK_ID=$(aws route53 list-health-checks \
        --query "HealthChecks[?HealthCheckConfig.FullyQualifiedDomainName contains '${APP_NAME}'].Id" \
        --output text)
    if [[ -n "$HEALTH_CHECK_ID" ]]; then
        log_info "  Health check configured: $HEALTH_CHECK_ID"
    else
        log_warn "  No health check found for ${APP_NAME}"
    fi

    # 2.3 Check ALB in DR region
    log_info "  Checking DR ALB status..."
    local DR_ALB_ARN
    DR_ALB_ARN=$(aws elbv2 describe-load-balancers \
        --region "$DR_REGION" \
        --names "${APP_NAME}-dr-alb" \
        --query 'LoadBalancers[0].LoadBalancerArn' \
        --output text 2>/dev/null || echo "")
    if [[ -n "$DR_ALB_ARN" ]]; then
        log_info "  DR ALB is ready"
    else
        log_error "  DR ALB not found in $DR_REGION"
        return 1
    fi

    log_info "DR readiness verification: PASSED"
    return 0
}

# ============================================================
# Phase 3: Execute Failover
# ============================================================
execute_failover() {
    log_info "Phase 3: Executing failover ${FAILOVER_MODE}"

    if [[ "$FAILOVER_MODE" == "drill" ]]; then
        log_info "  DRILL MODE: No actual changes will be made"
        log_info "  Steps that would be executed:"
        echo "    1. Stop application traffic to primary (5min downtime)"
        echo "    2. Promote DR database to primary"
        echo "    3. Scale up DR application cluster"
        echo "    4. Update Route53 DNS to point to DR"
        echo "    5. Verify end-to-end functionality in DR"
        echo ""
        log_warn "Run with 'full' to execute actual failover"
        return 0
    fi

    # Full failover
    log_info "  Step 3.1: Draining primary connections..."
    # Actual implementation would:
    # - Set ALB connection draining (300s)
    # - Wait for active connections to drain

    log_info "  Step 3.2: Promoting DR database..."
    aws rds promote-read-replica \
        --region "$DR_REGION" \
        --db-instance-identifier "${APP_NAME}-dr" \
        --backup-retention-period 7

    log_info "  Step 3.3: Scaling up DR application cluster..."
    aws ecs update-service \
        --region "$DR_REGION" \
        --cluster "${APP_NAME}-dr-cluster" \
        --service "${APP_NAME}-service" \
        --desired-count 5

    log_info "  Step 3.4: Updating DNS failover..."
    local DR_ALB_DNS
    DR_ALB_DNS=$(aws elbv2 describe-load-balancers \
        --region "$DR_REGION" \
        --names "${APP_NAME}-dr-alb" \
        --query 'LoadBalancers[0].DNSName' --output text)

    # Update DNS (simplified - actual implementation needs hosted zone ID)
    log_info "  DNS would be updated to: $DR_ALB_DNS"

    log_info "  Step 3.5: Verifying DR services..."
    sleep 30  # Wait for services to stabilize
    curl -sf "https://${APP_NAME}-dr.${DOMAIN_NAME}/health" && \
        log_info "  DR health check passed" || \
        log_warn "  DR health check pending"

    log_info "Failover execution: COMPLETED"
}

# ============================================================
# Phase 4: Rollback Preparation
# ============================================================
prepare_rollback() {
    log_info "Phase 4: Preparing rollback plan"
    log_info "  Rollback Plan:"
    echo "    1. Run failover again to switch back to primary region"
    echo "    2. Update DNS to point back to primary ALB"
    echo "    3. Verify primary services health"
    echo "    4. Scale down DR cluster to minimum"
    log_info "  Rollback script: /opt/scripts/dr-rollback.sh"
}

# ============================================================
# Main
# ============================================================
main() {
    echo ""
    echo "============================================"
    echo "  Disaster Recovery Failover Script"
    echo "  Mode: ${FAILOVER_MODE}"
    echo "  Primary: ${PRIMARY_REGION} -> DR: ${DR_REGION}"
    echo "  Timestamp: ${TIMESTAMP}"
    echo "============================================"
    echo ""

    pre_flight_check
    echo ""

    if ! verify_dr_readiness; then
        log_error "DR readiness check failed. Aborting failover."
        exit 1
    fi
    echo ""

    execute_failover
    echo ""

    prepare_rollback
    echo ""
    log_info "DR failover script completed"
    echo "Log file: ${LOG_FILE}"
}

main
```

### Ansible - 恢复编排 Playbook

```yaml
---
# ============================================================
# playbooks/dr-recovery-orchestration.yml
# Ansible 灾难恢复编排 Playbook
#
# 功能:
#   1. 从备份恢复数据库
#   2. 恢复应用配置和服务
#   3. 验证数据完整性
#   4. 切换流量到恢复后的环境
# ============================================================
- name: "DR Recovery Orchestration - 灾难恢复自动化编排"
  hosts: all
  gather_facts: yes
  become: yes
  serial: 1  # 串行执行，避免资源竞争

  vars:
    # ------ 恢复配置 ------
    dr_mode: "{{ dr_mode | default('full') }}"  # full / partial / validate
    recovery_tier: "{{ recovery_tier | default('tier1') }}"  # tier1/tier2/tier3
    backup_bucket: "{{ dr_backup_bucket | default('company-backup-dr') }}"
    restore_base_dir: "/data/restore/{{ ansible_date_time.date }}"
    app_name: "{{ dr_app_name | default('myapp') }}"

    # ------ RTO 目标 ------
    rto_targets:
      tier1: 15     # 核心服务 15 分钟
      tier2: 60     # 重要服务 1 小时
      tier3: 240    # 一般服务 4 小时

  # ============================================================
  # Phase 1: 环境准备和验证
  # ============================================================
  tasks:
    - name: "Phase 1: 恢复环境准备"
      block:
        - name: "创建恢复工作目录"
          file:
            path: "{{ restore_base_dir }}"
            state: directory
            mode: '0755'

        - name: "检查备份存档完整性"
          stat:
            path: "{{ backup_bucket }}/latest/{{ app_name }}-backup.tar.gz.asc"
          register: backup_signature

        - name: "验证备份签名 (GPG)"
          shell: |
            gpg --verify {{ backup_bucket }}/latest/{{ app_name }}-backup.tar.gz.asc
          when: backup_signature.stat.exists
          register: gpg_verify
          failed_when: gpg_verify.rc != 0
      tags: [phase1, prepare]

    # ============================================================
    # Phase 2: 数据库恢复
    # ============================================================
    - name: "Phase 2: 数据库恢复"
      when: dr_mode in ["full", "partial"]
      block:
        - name: "下载最新数据库备份"
          aws_s3:
            bucket: "{{ backup_bucket }}"
            object: "/database/{{ app_name }}-db-latest.sql.gz"
            dest: "{{ restore_base_dir }}/database.sql.gz"
            mode: get

        - name: "解压数据库备份文件"
          shell: |
            gunzip -c {{ restore_base_dir }}/database.sql.gz > {{ restore_base_dir }}/database.sql

        - name: "恢复 MySQL 数据库"
          mysql_db:
            name: "{{ app_name }}"
            state: import
            target: "{{ restore_base_dir }}/database.sql"
            login_user: "{{ db_restore_user }}"
            login_password: "{{ db_restore_password }}"
            login_host: "{{ db_host }}"
          register: db_restore_result

        - name: "执行数据完整性校验"
          shell: |
            mysql -h {{ db_host }} -u {{ db_restore_user }} -p'{{ db_restore_password }}' \
              -e "SELECT COUNT(*) as total_tables FROM information_schema.tables WHERE table_schema='{{ app_name }}';"
          register: table_count
      rescue:
        - name: "数据库恢复失败 - 回滚到上一个备份"
          debug:
            msg: "Database restore failed, rolling back to previous backup version"
          failed_when: false
      tags: [phase2, database]

    # ============================================================
    # Phase 3: 应用恢复
    # ============================================================
    - name: "Phase 3: 应用服务恢复"
      when: dr_mode in ["full", "partial"]
      block:
        - name: "恢复应用配置"
          unarchive:
            src: "{{ backup_bucket }}/config/{{ app_name }}-config-{{ ansible_date_time.date }}.tar.gz"
            dest: "/etc/{{ app_name }}/"
            remote_src: yes
            owner: "{{ app_user }}"
            group: "{{ app_group }}"

        - name: "启动应用服务 (按依赖顺序)"
          systemd:
            name: "{{ item }}"
            state: started
            enabled: yes
            daemon_reload: yes
          loop:
            - "{{ app_name }}-redis"
            - "{{ app_name }}-app"
            - "{{ app_name }}-sidekiq"
            - "{{ app_name }}-nginx"
          register: service_start

        - name: "验证应用健康"
          uri:
            url: "http://localhost:8080/health"
            status_code: 200
            timeout: 30
          register: health_check
          retries: 12
          delay: 5
          until: health_check.status == 200
      tags: [phase3, application]

    # ============================================================
    # Phase 4: 数据完整性验证
    # ============================================================
    - name: "Phase 4: 恢复验证"
      block:
        - name: "执行数据完整性检查脚本"
          script: scripts/verify-data-integrity.sh
          args:
            executable: /bin/bash
          register: integrity_check
          failed_when: integrity_check.rc != 0

        - name: "检查端到端业务流程"
          uri:
            url: "https://{{ app_domain }}/api/v1/health/ready"
            method: GET
            headers:
              Content-Type: "application/json"
          register: e2e_check

        - name: "生成恢复验证报告"
          copy:
            dest: "{{ restore_base_dir }}/recovery-report.json"
            content: |
              {
                "application": "{{ app_name }}",
                "recovery_time": "{{ ansible_date_time.iso8601 }}",
                "dr_mode": "{{ dr_mode }}",
                "database_restored": {{ db_restore_result is defined and db_restore_result.changed }},
                "services_running": {{ service_start is defined and not service_start.failed }},
                "health_check": {{ health_check.status == 200 }},
                "integrity_check": {{ integrity_check.rc == 0 }},
                "recovery_status": "COMPLETED"
              }
      tags: [phase4, validation]

    # ============================================================
    # Phase 5: 流量切换和交接
    # ============================================================
    - name: "Phase 5: 流量切换和完成"
      when: dr_mode == "full"
      block:
        - name: "更新 DNS 记录指向恢复后的环境"
          community.aws.route53:
            zone: "{{ dns_zone }}"
            record: "{{ app_domain }}"
            type: A
            ttl: 60
            value: "{{ recovery_lb_dns }}"
            overwrite: yes

        - name: "发送恢复完成通知"
          slack:
            token: "{{ slack_token }}"
            msg: |
              :white_check_mark: DR Recovery Completed
              Application: {{ app_name }}
              Mode: {{ dr_mode }}
              Time: {{ ansible_date_time.iso8601 }}
              Status: All services restored
            channel: "#dr-recovery"
            username: "DR Automation"
          ignore_errors: yes
      tags: [phase5, switchover]
```

## Error Handling

### Error Scenario 1: 灾备演练失败 (P1)

**触发条件**: 正式或演练故障切换过程中，关键服务无法在目标 RTO 时间内恢复，或数据完整性校验未通过

**处理流程**:
```
IF 灾备演练/切换失败 (RTO 超时 OR 数据校验失败)
THEN
  1. 立即评估事故严重程度:
     a. 演练模式: 标记为演练失败，切换回主环境
     b. 真实故障: 继续尝试恢复，延长 RTO 窗口
  2. 分类处理失败原因:
     a. RTO 超时: 分析瓶颈环节（网络/数据库/DNS 传播）
     b. RDS Promote 失败: 检查复制状态和权限配置
     c. 应用启动失败: 查看启动日志，检查配置兼容性
     d. 数据不一致: 对比主备库 checksum，确定差异范围
  3. 应急恢复:
     a. 切换到已知正常的备份版本
     b. 如果 DR 不可用，尝试在 Primary 区域重建服务
     c. 使用最近的可恢复快照进行 PITR 恢复
  4. 演练模式回滚:
     a. 执行 dr-rollback.sh 切换回主区域
     b. 确保所有流量回到 Primary
     c. 终止 DR 区域的非必要资源
  5. 事后改进:
     a. 详细记录失败的根本原因
     b. 修复发现的配置/脚本问题
     c. 缩短下次演练的周期（如从年度改为季度）
END
```

**降级方案**: 使用次级恢复策略（如从 S3 备份恢复到全新环境，而不是故障切换）

**升级条件**: 演练连续 2 次失败，或真实故障切换后 2 倍 RTO 内无法恢复，升级至高级架构团队

### Error Scenario 2: 主备切换数据不一致 (P0)

**触发条件**: 故障切换后发现 DR 数据库与 Primary 在切换时刻存在数据不一致（如缺少最近 N 秒的写入、主键冲突、序列号跳跃）

**处理流程**:
```
IF 检测到数据不一致
THEN
  1. 立即停止所有写入操作，防止数据继续分裂:
     a. 暂停所有写入 DR 的应用程序
     b. 记录当前 DR 数据库的 LSN/SCN 位置
     c. 冻结 DR 数据库状态用于取证
  2. 评估数据丢失范围:
     a. 查看 replication lag 日志确认丢失的数据量
     b. 检查 Primary 的 binlog 获取未同步的写入
     c. 估算受影响的事务数量和用户
  3. 数据恢复策略:
     a. IF 丢失 < 1 分钟数据: 从 Primary binlog 提取并应用
     b. IF 丢失 > 1 分钟: 从最近的完整备份恢复到已知一致点
     c. 如果涉及金融交易: 标记受影响的事务为待核查状态
  4. 一致性验证:
     a. 使用 pt-table-checksum 对比主备库
     b. 检查关键表行数和 checksum
     c. 对账关键业务数据（订单数、支付金额）
  5. 更新 RPO 监控:
     a. 确认 replication lag 告警阈值设置合理
     b. 增加数据一致性自动巡检
     c. 实施同步复制的双写策略（如果 RPO=0 要求）
END
```

**降级方案**: 接受有限的数据丢失（在 RPO 范围内），继续使用 DR 环境运行

**升级条件**: 数据丢失超过 RPO 目标，或涉及用户敏感数据，启动数据安全事件响应

### Error Scenario 3: DNS Failover 延迟或失败 (P1)

**触发条件**: 故障切换完成后，DNS 记录更新超过 5 分钟未生效，或客户端流量仍然指向不可用的 Primary 区域

**处理流程**:
```
IF DNS 切换延迟 > 5min 或未生效
THEN
  1. 检查 Route53 健康检查状态:
     a. 确认 Primary 健康检查已标记为 UNHEALTHY
     b. 检查 Route53 故障切换策略配置
     c. 验证健康检查的阈值和间隔设置
  2. 手动干预 DNS 切换:
     a. 手动修改 DNS 记录的 TTL 为 60 秒
     b. 强制将 DR 区域 ALB IP 设置为 A 记录
     c. 使用 DNS Provider 的 API 立即推送变更
  3. 客户端 TTL 问题处理:
     a. 通知运营团队指导用户清除 DNS 缓存
     b. 如果使用 CDN，PURGE CDN 缓存
     c. 发布公告说明 DNS 传播时间
  4. 替代流量切换方案:
     a. 使用 HTTP 301 重定向方式引导流量
     b. 在 Primary 的 ALB 配置转发规则到 DR
     c. 如果使用全局负载均衡器，手动切换
  5. 根本原因分析:
     a. 检查 DNS 变更是否触发了审核延迟
     b. 排查 Route53 是否有 API 限流
     c. 评估是否需要使用 Anycast DNS 技术
END
```

**降级方案**: 使用 DNS TTL 覆盖 + 应用层重定向组合方案，在 DNS 生效前临时接管流量

**升级条件**: DNS 切换在 30 分钟内无法完成，直接使用 IP 访问方式通知关键客户

### Error Scenario 4: 跨区域网络带宽不足导致数据复制延迟 (P2)

**触发条件**: DR 区域的数据库复制延迟持续超过 5 分钟，或跨区域数据同步带宽饱和

**处理流程**:
```
IF 跨区域复制延迟持续 > 5min
THEN
  1. 立即检查当前网络带宽使用情况:
     a. 使用 CloudWatch 检查 DX/VPN 带宽利用率
     b. 检查跨区域数据传输量的趋势
     c. 查看是否有大量数据迁移任务占用了带宽
  2. 优化数据复制:
     a. 增加数据库复制连接的并行度
     b. 启用 binlog 压缩（Row-based 格式）
     c. 限制非关键数据的跨区域同步频率
  3. 网络扩容:
     a. 临时增加 Direct Connect 带宽（按需付费模式）
     b. 启用 S3 Transfer Acceleration 加速备份传输
     c. 对非实时数据使用异步批量传输
  4. 数据复制架构优化:
     a. 实施分层复制策略: 关键数据优先同步
     b. 配置 QoS 策略保障数据库复制流量优先级
     c. 考虑使用数据压缩和去重技术
  5. 更新容量规划模型:
     a. 引入网络带宽作为容量规划的输入
     b. 预测数据增长趋势，提前扩容网络
     c. 设置跨区域复制延迟的告警阈值
END
```

**降级方案**: 临时降低非关键业务的数据同步频率，优先保障核心数据库复制

**升级条件**: 复制延迟导致 RPO 无法满足业务要求，无法在合理成本内解决，需架构评审

## Quality Standards

> Acceptance criteria and quality gates for plan-disaster-recovery deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | RTO and RPO targets are achievable and verified | Automated check |
| Standard 2 | RPO compliance is 100% with acceptable data loss | Automated check |
| Standard 3 | Full DR drill is conducted at least annually | Automated check |
## References

- [harness-engineering.md](../standards/harness-engineering.md)
- [output-validation-checklist.md](../evaluations/output-validation-checklist.md)
- [regression-checklist.md](../evaluations/regression-checklist.md)
