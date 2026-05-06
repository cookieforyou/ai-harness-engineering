---
name: plan-disaster-recovery
description: 灾备恢复规划场景的技术指令
type: instructions
stage: "plan-disaster-recovery"
version: "1.1.0"
---

# Disaster Recovery Planning Instructions

## Overview

本指令提供灾备恢复规划的详细技术规范和实施指南。

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


## Error Handling

> Common error scenarios and resolution strategies for plan-disaster-recovery.

### Error Category 1
**Symptom**: DR plan does not meet RTO/RPO targets
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]

### Error Category 2
**Symptom**: DR procedures are untested or outdated
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]


## Quality Standards

> Acceptance criteria and quality gates for plan-disaster-recovery deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | RTO and RPO targets are achievable and verified | Automated check |
| Standard 2 | RPO compliance is 100% with acceptable data loss | Automated check |
| Standard 3 | Full DR drill is conducted at least annually | Automated check |
