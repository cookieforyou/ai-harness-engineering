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
language: "zh-CN"
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

## Multi-Language Code Examples

### Kubernetes: kubectl rollout undo 回滚脚本

```bash
#!/bin/bash
# k8s-rollback.sh — Kubernetes 自动化回滚脚本
set -euo pipefail

NAMESPACE="${1:?Usage: $0 <namespace> <deployment> [revision]}"
DEPLOYMENT="${2:?Usage: $0 <namespace> <deployment> [revision]}"
REVISION="${3:-}"

# 颜色输出
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

log_info()  { echo -e "${GREEN}[INFO]${NC} $(date '+%H:%M:%S') $1"; }
log_error() { echo -e "${RED}[ERROR]${NC} $(date '+%H:%M:%S') $1"; }
log_warn()  { echo -e "${YELLOW}[WARN]${NC} $(date '+%H:%M:%S') $1"; }

# === Step 1: 记录回滚前的状态 ===
log_info "=== Step 1: Recording current state ==="
kubectl get deployment "${DEPLOYMENT}" -n "${NAMESPACE}" -o yaml > "pre-rollback-${DEPLOYMENT}.yaml"
log_info "Current state saved to pre-rollback-${DEPLOYMENT}.yaml"

# === Step 2: 检查回滚历史 ===
log_info "=== Step 2: Checking rollout history ==="
kubectl rollout history deployment/"${DEPLOYMENT}" -n "${NAMESPACE}"

# === Step 3: 执行回滚 ===
log_info "=== Step 3: Executing rollback ==="
if [ -n "$REVISION" ]; then
    log_info "Rolling back to revision: ${REVISION}"
    kubectl rollout undo deployment/"${DEPLOYMENT}" \
      -n "${NAMESPACE}" \
      --to-revision="${REVISION}"
else
    log_info "Rolling back to previous revision"
    kubectl rollout undo deployment/"${DEPLOYMENT}" -n "${NAMESPACE}"
fi

# === Step 4: 等待回滚完成 ===
log_info "=== Step 4: Waiting for rollback to complete ==="
if kubectl rollout status deployment/"${DEPLOYMENT}" \
   -n "${NAMESPACE}" \
   --timeout=300s; then
    log_info "Rollback completed successfully"
else
    log_error "Rollback timeout or failed"
    # 检查 Pod 状态
    kubectl get pods -n "${NAMESPACE}" -l app="${DEPLOYMENT}"
    exit 1
fi

# === Step 5: 健康检查 ===
log_info "=== Step 5: Running health checks ==="
sleep 5  # 等待服务完全就绪

# 检查可用副本数
AVAILABLE=$(kubectl get deployment "${DEPLOYMENT}" \
  -n "${NAMESPACE}" -o jsonpath='{.status.availableReplicas}')
DESIRED=$(kubectl get deployment "${DEPLOYMENT}" \
  -n "${NAMESPACE}" -o jsonpath='{.status.replicas}')

if [ "${AVAILABLE:-0}" -lt "${DESIRED:-0}" ]; then
    log_error "Not all replicas are available: ${AVAILABLE}/${DESIRED}"
    exit 1
fi
log_info "All replicas available: ${AVAILABLE}/${DESIRED}"

# 应用层健康检查
log_info "Performing application health check..."
if kubectl run health-check-${DEPLOYMENT} --image=curlimages/curl:latest \
  -n "${NAMESPACE}" --rm --restart=Never -- \
  -f http://${DEPLOYMENT}:8080/health --max-time 10 2>/dev/null; then
    log_info "Health check passed"
else
    log_warn "Health check failed, but rollback completed"
    log_warn "Manual verification required"
fi

# === Step 6: 验证完成 ===
log_info "=== Rollback Summary ==="
echo "Namespace: ${NAMESPACE}"
echo "Deployment: ${DEPLOYMENT}"
echo "Target Revision: ${REVISION:-previous}"
echo "Pre-rollback State: pre-rollback-${DEPLOYMENT}.yaml"
echo "Timestamp: $(date -u '+%Y-%m-%dT%H:%M:%SZ')"
```

### Helm: Release 回滚

```bash
#!/bin/bash
# helm-rollback.sh — Helm Release 回滚脚本
set -euo pipefail

RELEASE_NAME="${1:?Usage: $0 <release> <namespace> [revision]}"
NAMESPACE="${2:?Usage: $0 <release> <namespace> [revision]}"
REVISION="${3:-}"
BACKUP_DIR="./helm-backups/$(date +%Y%m%d-%H%M%S)"

echo "=== Helm Rollback Procedure ==="
echo "Release: ${RELEASE_NAME}"
echo "Namespace: ${NAMESPACE}"

# === Step 1: 获取当前 release 信息 ===
echo "[1/6] Getting release information..."
mkdir -p "${BACKUP_DIR}"
helm get all "${RELEASE_NAME}" -n "${NAMESPACE}" > "${BACKUP_DIR}/pre-rollback-values.yaml" 2>&1 || true

# === Step 2: 列出历史版本 ===
echo "[2/6] Listing release history..."
helm history "${RELEASE_NAME}" -n "${NAMESPACE}" \
  --max 10 \
  -o yaml > "${BACKUP_DIR}/release-history.yaml"

echo "Recent revisions:"
helm history "${RELEASE_NAME}" -n "${NAMESPACE}" --max 5

# === Step 3: 执行回滚 ===
echo "[3/6] Executing rollback..."
ROLLBACK_ARGS=()
if [ -n "$REVISION" ]; then
    ROLLBACK_ARGS+=("$REVISION")
    echo "Rolling back to revision: ${REVISION}"
else
    echo "Rolling back to previous revision"
fi
ROLLBACK_ARGS+=("--namespace=${NAMESPACE}")
ROLLBACK_ARGS+=("--timeout=10m")
ROLLBACK_ARGS+=("--wait")
ROLLBACK_ARGS+=("--cleanup-on-fail")  # 失败时清理创建的资源

helm rollback "${RELEASE_NAME}" "${ROLLBACK_ARGS[@]}"

# === Step 4: 验证部署状态 ===
echo "[4/6] Validating deployment..."
helm status "${RELEASE_NAME}" -n "${NAMESPACE}" \
  -o yaml > "${BACKUP_DIR}/post-rollback-status.yaml"

# 等待所有资源就绪
kubectl wait --for=condition=available --timeout=120s \
  deployment -l "app.kubernetes.io/instance=${RELEASE_NAME}" \
  -n "${NAMESPACE}"

# === Step 5: 运行功能验证 ===
echo "[5/6] Running post-rollback smoke tests..."
# 通过 Helm test 执行预定义的测试
helm test "${RELEASE_NAME}" -n "${NAMESPACE}" --timeout 60s || {
    echo "WARNING: Smoke tests failed, manual verification required"
}

# === Step 6: 记录回滚信息 ===
echo "[6/6] Recording rollback information..."
cat > "${BACKUP_DIR}/rollback-summary.yaml" <<EOF
rollback:
  release: "${RELEASE_NAME}"
  namespace: "${NAMESPACE}"
  timestamp: "$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  target_revision: ${REVISION:-previous}
  pre_rollback_backup: "${BACKUP_DIR}/pre-rollback-values.yaml"
  status: "completed"
EOF

echo "=== Rollback Complete ==="
echo "Rollback logs saved to: ${BACKUP_DIR}"
```

### Terraform: 状态回滚

```bash
#!/bin/bash
# terraform-rollback.sh — Terraform 基础设施状态回滚
set -euo pipefail

ENVIRONMENT="${1:?Usage: $0 <environment> [state-version]}"
TARGET_VERSION="${2:-}"

BACKUP_DIR="./tf-rollback-${ENVIRONMENT}-$(date +%Y%m%d-%H%M%S)"
mkdir -p "${BACKUP_DIR}"

echo "=== Terraform State Rollback ==="
echo "Environment: ${ENVIRONMENT}"

# === Step 1: 备份当前状态 ===
echo "[1/7] Backing up current state..."
terraform state pull > "${BACKUP_DIR}/current-state.json"
echo "Current state backed up to ${BACKUP_DIR}/current-state.json"

# === Step 2: 列出可用版本（如果使用 S3 版本控制） ===
echo "[2/7] Listing state versions..."
if [ -z "$TARGET_VERSION" ]; then
    echo "Available state versions (S3 versioning):"
    aws s3api list-object-versions \
      --bucket "${TF_STATE_BUCKET}" \
      --prefix "env:/${ENVIRONMENT}/terraform.tfstate" \
      --query "Versions[?IsLatest==\`false\`].[VersionId,LastModified]" \
      --output table | head -20
    echo "Please specify a target version ID"
    exit 1
fi

# === Step 3: 下载指定版本的状态文件 ===
echo "[3/7] Downloading target state version..."
aws s3api get-object \
  --bucket "${TF_STATE_BUCKET}" \
  --key "env:/${ENVIRONMENT}/terraform.tfstate" \
  --version-id "${TARGET_VERSION}" \
  "${BACKUP_DIR}/target-state.json" > /dev/null

# === Step 4: 推送目标状态为当前状态 ===
echo "[4/7] Pushing target state..."
terraform state push "${BACKUP_DIR}/target-state.json"

# === Step 5: Plan 验证 ===
echo "[5/7] Running terraform plan to verify..."
terraform plan -detailed-exitcode -out="${BACKUP_DIR}/rollback.tfplan"
PLAN_EXIT=$?

case $PLAN_EXIT in
    0)
        echo "No changes — state rollback successful"
        ;;
    2)
        echo "Changes detected — reviewing plan..."
        terraform show "${BACKUP_DIR}/rollback.tfplan"
        ;;
    *)
        echo "ERROR: Terraform plan failed"
        exit 1
        ;;
esac

# === Step 6: Apply 回滚变更 ===
echo "[6/7] Applying rollback..."
terraform apply "${BACKUP_DIR}/rollback.tfplan"

# === Step 7: 验证 ===
echo "[7/7] Verification..."
terraform output > "${BACKUP_DIR}/post-rollback-output.txt"
echo "Post-rollback outputs saved to ${BACKUP_DIR}/post-rollback-output.txt"
echo "=== Terraform Rollback Complete ==="
```

```hcl
# rollback.tf — Terraform 版本回滚配置示例
# 使用 terraform state mv 实现细粒度资源回滚

# 将指定资源恢复到前一版本
resource "null_resource" "rollback_resource" {
  triggers = {
    # 触发回滚的条件
    rollback_trigger = var.rollback_version
  }

  provisioner "local-exec" {
    command = <<EOT
      # 导出特定资源的旧状态
      terraform state rm aws_instance.app
      terraform import aws_instance.app i-${var.rollback_instance_id}
    EOT
  }
}
```

### Database: Flyway / Liquibase 迁移回滚

```sql
-- Flyway 数据库迁移回滚
-- -------------------------------------------------------
-- Flyway 使用 undo 迁移（需 Flyway Teams/Enterprise 版）
-- 回滚文件命名规范: V<version>__<description>.sql (正向)
-- 撤销文件命名规范: U<version>__<description>.sql (回滚)

-- V2__add_users_table.sql (正向迁移)
CREATE TABLE users (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_users_email (email),
    UNIQUE INDEX idx_users_username (username)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- U2__add_users_table.sql (回滚迁移 — 与正向迁移配对)
DROP TABLE IF EXISTS users;
```

```xml
<!-- pom.xml — Flyway 插件配置 -->
<project>
  <build>
    <plugins>
      <plugin>
        <groupId>org.flywaydb</groupId>
        <artifactId>flyway-maven-plugin</artifactId>
        <version>9.22.3</version>
        <configuration>
          <url>${db.url}</url>
          <user>${db.username}</user>
          <password>${db.password}</password>
          <!-- 迁移版本表 -->
          <table>flyway_schema_history</table>
          <!-- 自动回滚（需要团队版） -->
          <cleanDisabled>false</cleanDisabled>
        </configuration>
      </plugin>
    </plugins>
  </build>
</project>
```

```bash
# Flyway 回滚命令
flyway undo          # 撤销最近一次迁移（需 Teams/Enterprise）
flyway info          # 查看迁移状态
flyway migrate       # 执行正向迁移
flyway repair       # 修复 schema 历史表

# 手动回滚（社区版替代方案）
# 1. 编写回滚 SQL
cat > U1.1__rollback_user_changes.sql <<'EOF'
-- 回滚 V1.1 的变更
ALTER TABLE users DROP COLUMN IF EXISTS last_login;
ALTER TABLE users DROP INDEX IF EXISTS idx_last_login;
EOF

# 2. 执行回滚
mysql -h ${DB_HOST} -u ${DB_USER} -p${DB_PASS} ${DB_NAME} < U1.1__rollback_user_changes.sql

# 3. 更新 Flyway 历史表标记
mysql -h ${DB_HOST} -u ${DB_USER} -p${DB_PASS} ${DB_NAME} <<'SQL'
DELETE FROM flyway_schema_history WHERE version = '1.1';
SQL
```

```xml
<!-- liquibase.xml — Liquibase 数据库变更集（支持回滚） -->
<?xml version="1.0" encoding="UTF-8"?>
<databaseChangeLog
    xmlns="http://www.liquibase.org/xml/ns/dbchangelog"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog
                        http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-4.20.xsd">

    <!-- 变更集：每个变更集都必须包含回滚逻辑 -->
    <changeSet id="20240601-add-orders-table" author="platform-team">
        <comment>添加 orders 订单表</comment>

        <!-- 正向迁移 -->
        <createTable tableName="orders">
            <column name="id" type="BIGINT" autoIncrement="true">
                <constraints primaryKey="true" nullable="false"/>
            </column>
            <column name="user_id" type="BIGINT">
                <constraints nullable="false"
                    foreignKeyName="fk_orders_user"
                    references="users(id)"/>
            </column>
            <column name="total_amount" type="DECIMAL(10,2)">
                <constraints nullable="false"/>
            </column>
            <column name="status" type="VARCHAR(20)" defaultValue="PENDING">
                <constraints nullable="false"/>
            </column>
            <column name="created_at" type="TIMESTAMP"
                defaultValueComputed="CURRENT_TIMESTAMP"/>
        </createTable>

        <createIndex indexName="idx_orders_user_status"
                     tableName="orders">
            <column name="user_id"/>
            <column name="status"/>
        </createIndex>

        <!-- 回滚逻辑 -->
        <rollback>
            <dropIndex tableName="orders" indexName="idx_orders_user_status"/>
            <dropTable tableName="orders"/>
        </rollback>
    </changeSet>

    <!-- 变更集：数据迁移（包含 precondition） -->
    <changeSet id="20240602-migrate-user-data" author="platform-team">
        <preConditions onFail="MARK_RAN">
            <tableExists tableName="users_old"/>
        </preConditions>

        <sql>
            INSERT INTO users (username, email)
            SELECT name, email FROM users_old
            WHERE NOT EXISTS (
                SELECT 1 FROM users u WHERE u.email = users_old.email
            );
        </sql>

        <rollback>
            <sql>
                DELETE FROM users WHERE email IN (
                    SELECT email FROM users_old
                );
            </sql>
        </rollback>
    </changeSet>

</databaseChangeLog>
```

```bash
# Liquibase 回滚命令
# 按指定数量回滚
liquibase rollbackCount 1                  # 回滚最近 1 个变更集

# 按指定日期回滚
liquibase rollbackToDate 2024-06-01        # 回滚到 2024-06-01 之前的版本

# 按指定标签回滚
liquibase tag v1.0.0                       # 标记当前版本
liquibase rollback v1.0.0                  # 回滚到标记版本

# 回滚预览
liquibase rollbackOneChangeSet             # 交互式回滚单个变更集

# 回滚指定文件中的变更集
liquibase rollbackCount 1 \
  --changeLogFile=liquibase.xml \
  --url=jdbc:mysql://${DB_HOST}:3306/${DB_NAME}

# 生成回滚 SQL 脚本（不直接执行）
liquibase rollbackCount 1 --outputFile=rollback.sql
```

## Error Handling

### Error Scenario 1: 回滚脚本未测试 (P1)

**触发条件**: 生产环境需要执行回滚时，发现回滚脚本未经过测试验证或脚本不完整

**处理流程**:
```
IF 回滚脚本执行失败或发现脚本未经过测试
THEN
  1. 立即评估回滚风险：
     - 检查脚本语法错误（bash -n script.sh）
     - 确认脚本依赖的工具和权限是否就绪
  2. 执行手动回滚步骤（如脚本不可用）：
     - 依靠文档化的手动回滚流程
     - 逐步骤执行并验证中间结果
  3. 并行修复回滚脚本：
     - 逐个命令手工执行并验证
     - 将已验证的命令序列及时写入脚本
     - 在隔离环境重新测试脚本
  4. 回滚完成后强制要求：
     - 所有回滚脚本必须通过 "dry-run" 测试
     - 在发布的预检阶段自动运行脚本语法和依赖检查
     - 将脚本测试纳入 CI/CD 流水线
  5. 建立回滚演练制度：每月至少一次完整回滚演练
END
```

**降级方案**: 使用基础设施层的快照/备份恢复（AWS AMI 回退、VM Snapshot、数据库 PITR）替代应用层回滚脚本

**升级条件**: 脚本不可用导致回滚时间超过 RTO（15 分钟），或需要 DBA/运维专家介入手动操作

### Error Scenario 2: 数据库回滚失败 (P0)

**触发条件**: 数据库迁移回滚过程中出现错误，Schema 变更无法撤销或数据丢失

**处理流程**:
```
IF 数据库回滚执行出错（语法错误、约束冲突、外键依赖阻塞）
THEN
  1. 立即暂停回滚操作，防止数据进一步损坏
  2. 评估回滚失败的具体原因：
     - 语法错误 → 检查回滚 SQL 语法
     - 外键约束 → 检查依赖关系，可能需要先删除子表数据
     - 数据丢失 → 检查是否有数据被误删
     - 锁等待 → 检查是否有长事务阻塞
  3. 根据情况选择恢复策略：
     - 策略 A: 修复回滚 SQL 后重试
     - 策略 B: 使用数据库时间点恢复（PITR）恢复到回滚前状态
     - 策略 C: 使用全量备份恢复到迁移前版本
     - 策略 D: 前向修复（应用新的迁移来修正问题）— 最后手段
  4. 验证数据完整性：
     - 检查行数是否匹配预期
     - 检查外键约束是否全部满足
     - 抽样验证关键数据字段
  5. 更新 Alembic / Flyway / Liquibase 的 schema 历史表以反映当前状态
  6. 记录详细的问题原因和解决方案到知识库
END
```

**降级方案**: 从最近的数据库全量备份 + WAL 日志执行时间点恢复（PITR），然后重新执行正向迁移（跳过已失败的变更集）

**升级条件**: 数据丢失涉及超过 1000 行记录，或核心业务表结构损坏无法修复

### Error Scenario 3: 回滚后服务发现异常 (P1)

**触发条件**: 应用版本回滚后，服务注册中心（Consul / Eureka / Kubernetes Service）未及时更新，导致流量路由到不存在的实例

**处理流程**:
```
IF 回滚完成后部分流量仍路由到旧版本或 503 错误增加
THEN
  1. 检查服务注册状态：
     - K8s: kubectl get endpoints -n <ns> 检查端点是否匹配回滚后的 Pod IP
     - Consul: consul catalog services 检查服务注册信息
     - Eureka: /eureka/apps API 检查应用实例列表
  2. 触发服务注册刷新：
     - K8s: 删除旧的 EndpointSlice 对象触发重建
     - Consul: consul reload 重新加载配置
     - 重启服务注册中心客户端侧缓存
  3. 检查健康检查探针配置：
     - K8s: 确认 readinessProbe 是否指向正确的路径和端口
     - 确认新/旧版本的 readiness 端点返回 200
  4. 清理 DNS 缓存：
     - CoreDNS: kubectl rollout restart -n kube-system deployment/coredns
     - 应用侧: 清除 HTTP 连接池和 DNS 缓存
  5. 验证流量路由恢复：
     - 抽样请求确认正确路由到回滚后的实例
     - 监控错误率恢复至正常水平
     - 确认无 503/502 错误
END
```

**降级方案**: 手动编辑服务端点/ELB 目标组，直接绑定到回滚后的实例 IP，绕过服务发现机制

**升级条件**: 服务发现异常导致超过 20% 的请求失败，或持续超过 10 分钟


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
