---
name: plan-rollback
description: "回滚计划场景的技术指令"
applyTo: "scenarios/plan-rollback/**"
phase: deployment
type: instruction
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['instruction', 'technical']
---
# Rollback Planning Instructions

## Overview

This instruction establishes the technical standards and detailed procedures for safe and efficient rollback planning within release management. It covers rollback trigger conditions, data consistency preservation during rollback, stateful vs. stateless rollback strategies, communication protocols, and post-rollback validation procedures. The instruction ensures every release has a tested, executable rollback plan that can restore service within defined recovery time objectives while preserving data integrity.


## Rollback Strategy Comparison

| Strategy | Best For | RTT | Cost | Complexity |
|----------|----------|-----|------|------------|
| Blue-Green | Critical services | 1-5 min | High | Medium |
| Canary | Feature releases | 1-5 min | Medium | Medium |
| Feature Toggle | Feature switches | Seconds | Low | Low |
| Database Migration | Schema changes | Varies | Medium | High |
| Instant Rollback | All | Seconds | Low | Low |

## Rollback Triggers

### Automatic Triggers

```yaml
automatic_triggers:
  error_rate:
    threshold: 5%
    window: 5 min
    action: stop + alert

  latency_p99:
    threshold: 2000ms
    window: 5 min
    action: stop + alert

  http_5xx_rate:
    threshold: 3%
    window: 2 min
    action: stop + alert

  health_check:
    threshold: 2 consecutive failures
    action: immediate rollback
```

### Manual Triggers

```yaml
manual_triggers:
  - Business metrics degradation
  - Customer complaints spike
  - SLA violation risk
  - Security incident
  - On-call engineer decision
```

## Rollback Procedures

### 1. Kubernetes Rollback

```bash
# Deployment rollback
kubectl rollout undo deployment/<name>
kubectl rollout undo deployment/<name> --to-revision=<n>

# Check rollout status
kubectl rollout status deployment/<name>

# Rollback history
kubectl rollout history deployment/<name>
```

### 2. Helm Rollback

```bash
# List releases
helm list -n <namespace>

# Rollback
helm rollback <release> -n <namespace>

# Rollback to specific version
helm rollback <release> <revision> -n <namespace>
```

### 3. Database Rollback

```sql
-- MySQL: Point-in-time recovery
mysqlbinlog --stop-datetime="2024-01-01 12:00:00" | mysql

-- PostgreSQL: Point-in-time recovery
-- Using pg_basebackup + recovery.conf
pg_restore -d <db> <backup.dump>

-- MongoDB: Replay oplog
mongorestore --oplogReplay --oplogFile=<oplog.bson>
```

### 4. Configuration Rollback

```bash
# GitOps rollback
git revert <commit>
git push

# Kubernetes ConfigMap
kubectl apply -f configmap-previous.yaml

# Consul KV
consul kv delete -flags= <key>
```

## Verification Checklist

### Health Checks

```bash
# Service Health
curl -f http://<service>/health
curl -f http://<service>/ready

# Database Connection
psql -c "SELECT 1"
mysqladmin ping

# Cache Status
redis-cli ping
```

### Functional Verification

```bash
# API Tests
curl -X POST http://<service>/api/test \
  -H "Content-Type: application/json" \
  -d '{"test": true}'

# End-to-End Tests
newman run postman-collection.json

# Smoke Tests
pytest tests/smoke/
```

### Performance Verification

```bash
# Latency Check
curl -w "%{time_total}" -o /dev/null http://<service>/api/endpoint

# Load Test
k6 run --vus 10 --duration 60s load-test.js
```

## Rollback Time Estimation

### Component-Based Estimation

| Component | Typical Rollback Time |
|-----------|----------------------|
| Stateless Service | 1-3 minutes |
| Database Schema | 5-30 minutes |
| Data Migration | 10-60 minutes |
| Configuration | 1-5 minutes |
| DNS/Load Balancer | 1-15 minutes |
| Full Stack | 15-60 minutes |

### Measurement Formula

```
RTT = Detection Time + Decision Time + Execution Time + Verification Time

Where:
- Detection Time: 1-5 min (automatic monitoring)
- Decision Time: 5-15 min (human decision)
- Execution Time: Varies by component
- Verification Time: 5-10 min
```

## Rollback Script Template

```bash
#!/bin/bash
# rollback.sh - Automated Rollback Script

set -e

# Configuration
SERVICE_NAME="${SERVICE_NAME:-app}"
NAMESPACE="${NAMESPACE:-production}"
PREVIOUS_VERSION="${PREVIOUS_VERSION}"
BACKUP_ENABLED="${BACKUP_ENABLED:-true}"

# Logging
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Pre-rollback backup
backup() {
    if [ "$BACKUP_ENABLED" = "true" ]; then
        log "Creating pre-rollback backup..."
        # Backup commands here
    fi
}

# Execute rollback
rollback_deployment() {
    log "Rolling back deployment..."
    kubectl rollout undo deployment/${SERVICE_NAME} -n ${NAMESPACE}
    kubectl rollout status deployment/${SERVICE_NAME} -n ${NAMESPACE} --timeout=300s
}

# Verify rollback
verify() {
    log "Verifying rollback..."
    
    # Health check
    curl -f http://${SERVICE_NAME}/health || exit 1
    
    # Check replicas
    kubectl wait --for=condition=available deployment/${SERVICE_NAME} -n ${NAMESPACE} --timeout=300s
    
    log "Rollback verification passed"
}

# Execute
log "Starting rollback for ${SERVICE_NAME}"
backup
rollback_deployment
verify
log "Rollback completed successfully"
```

## Communication Template

### Rollback Notification

```markdown
## Rollback Notification

**服务**: <SERVICE_NAME>
**版本**: <VERSION> → <PREVIOUS_VERSION>
**时间**: <TIMESTAMP>
**触发人**: <TRIGGERED_BY>

### 原因
<REASON_FOR_ROLLBACK>

### 影响
- 用户影响: <USER_IMPACT>
- 预计恢复时间: <ESTIMATED_RECOVERY_TIME>

### Status
- [ ] 回滚已启动
- [ ] 回滚执行中
- [ ] 回滚完成
- [ ] 验证通过

### 后续行动
- [ ] 根本原因分析
- [ ] 问题修复
- [ ] 重新部署验证

### 联系方式
- On-call: <ON_CALL_CONTACT>
- 负责人: <PRIMARY_CONTACT>
```

## Best Practices

### Do's

1. **提前准备**: 部署前必须准备好回滚方案
2. **自动化**: 优先使用自动化回滚脚本
3. **幂等性**: 回滚脚本必须可重复执行
4. **可验证**: 回滚后必须验证服务正常
5. **备份**: 回滚前先备份当前状态
6. **文档**: 记录回滚步骤和结果

### Don'ts

1. **不要手动回滚**: 避免手工操作引入错误
2. **不要跳过验证**: 必须验证回滚成功
3. **不要隐瞒问题**: 及时通知相关方
4. **不要仓促决定**: 给团队决策时间
5. **不要忘记复盘**: 回滚后必须总结改进


## Technical Specifications

> Detailed technical requirements and implementation guidelines for plan-rollback.

### Required Tools
- [List required tools and frameworks]

### Environment Requirements
- [List environment prerequisites]

### Configuration Parameters
- [List key configuration parameters]


## Error Handling

> Common error scenarios and resolution strategies for plan-rollback.

### Error Category 1
**Symptom**: Rollback procedure is untested or incomplete
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]

### Error Category 2
**Symptom**: Rollback causes data inconsistency or corruption
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]


## Quality Standards

> Acceptance criteria and quality gates for plan-rollback deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | Rollback plan is tested for all release scenarios | Automated check |
| Standard 2 | Recovery time objective (RTO) is 15 minutes or less | Automated check |
| Standard 3 | Data consistency is maintained after rollback | Automated check |
## References

- [harness-engineering.md](../standards/harness-engineering.md)
- [output-validation-checklist.md](../evaluations/output-validation-checklist.md)
- [regression-checklist.md](../evaluations/regression-checklist.md)
