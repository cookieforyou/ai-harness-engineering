---
name: plan-rollback
description: "Domain skill for plan-rollback execution"
category: deployment
type: skill
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['skill', 'knowledge']
---
# Rollback Planning Skill

## Core Knowledge

### 1. Deployment Strategies

#### Blue-Green Deployment
```
Environment A (Blue): Production
Environment B (Green): Staging

Process:
1. Deploy to Green
2. Test Green
3. Switch traffic (DNS/LB)
4. Monitor
5. Keep Blue as rollback target
```

#### Canary Deployment
```
Process:
1. Deploy to 5% traffic
2. Monitor metrics
3. If OK → 25% traffic
4. If OK → 50% traffic
5. If OK → 100% traffic
6. If issue → rollback to previous
```

#### Rolling Deployment
```
Process:
1. Update 1 pod
2. Wait for ready
3. Update next pod
4. Continue until all
5. Rollback: Reverse the process
```

### 2. Rollback Patterns

#### Infrastructure as Code Rollback
```bash
# Terraform
terraform apply -target=resource.id
terraform apply -target=resource.id -var="rollback=true"

# Pulumi
pulumi up --target=urn
pulumi rollback
```

#### Database Migration Rollback
```sql
-- Laravel
php artisan migrate:rollback --step=1

-- Django
python manage.py migrate <app_name> <previous_migration>

-- Flyway
flyway.undo()
```

### 3. Feature Toggle Rollback

```javascript
// Feature Flag Configuration
const featureFlags = {
  newCheckout: {
    enabled: true,
    rolloutPercentage: 100,
    override: false
  }
};

// Instant rollback
featureFlags.newCheckout.enabled = false;
```

### 4. State Management

#### Application State
```yaml
state_checklist:
  - Database connections active
  - Cache warmed
  - Session state preserved
  - Background jobs paused
  - Queue messages retained
```

#### Data State
```yaml
data_integrity:
  - Transactions completed
  - No partial updates
  - Foreign key constraints valid
  - Indexes intact
```

## Best Practices

### Pre-Deployment
1. Always have a rollback plan
2. Test rollback in staging
3. Document expected rollback time
4. Configure monitoring alerts
5. Notify stakeholders

### During Deployment
1. Monitor key metrics continuously
2. Have rollback trigger criteria ready
3. Keep communication channel open
4. Don't ignore warning signs

### Post-Rollback
1. Verify service health immediately
2. Communicate status to stakeholders
3. Investigate root cause
4. Plan fix and re-deployment
5. Document lessons learned

## Common Issues

| Issue | Solution |
|-------|----------|
| Database changes can't be rolled back | Design reversible migrations |
| State lost after rollback | Implement state snapshot |
| Rollback takes too long | Automate and test regularly |
| Partial rollback state | Design atomic deployments |
| Can't verify rollback | Implement comprehensive checks |


## Anti-patterns (反模式)

> 与 Common Pitfalls 同义，执行时合并检查。

## Common Pitfalls

> Frequent mistakes to avoid during plan-rollback execution.

### Pitfall 1: 只准备部署不回滚的方案 (Deploy-Only Planning)
**Risk**: 每次部署只关注上线流程，未提前准备回滚方案，出现故障时措手不及。
**Prevention**: 部署前必须编写并评审回滚方案，作为部署就绪检查的必要项。
**Impact**: 故障恢复时间延长 3-5 倍，服务不可用时间大幅增加。

### Pitfall 2: 数据库迁移无法回滚 (Irreversible DB Migration)
**Risk**: 数据库迁移脚本只设计了前向变更，未提供回退脚本，导致数据无法恢复到迁移前状态。
**Prevention**: 所有数据库迁移必须提供 `up` 和 `down` 脚本，并在预发布环境验证回滚完整性。
**Impact**: 数据丢失或损坏，需要 DBA 手动修复，恢复时间不可控。

### Pitfall 3: 回滚后配置不一致 (Post-Rollback Config Mismatch)
**Risk**: 回滚应用代码但未同时回滚配置或依赖服务版本，导致代码与配置不匹配。
**Prevention**: 将配置变更与应用代码变更绑定在同一制品版本中，回滚时整体切换。
**Impact**: 应用启动失败或行为异常，需二次排查，增加故障处理复杂度。
