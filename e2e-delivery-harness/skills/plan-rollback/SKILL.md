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


## Common Pitfalls

> Frequent mistakes to avoid during plan-rollback execution.

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
