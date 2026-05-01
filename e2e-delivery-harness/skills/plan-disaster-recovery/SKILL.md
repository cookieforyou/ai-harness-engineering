# Disaster Recovery Planning Skill

## Core Knowledge

### 1. Business Continuity Fundamentals

#### BCP (Business Continuity Plan)
- 预防和恢复能力
- 关键业务连续性
- 人员安全
- 设施安全

#### DRP (Disaster Recovery Plan)
- IT 系统恢复
- 数据恢复
- 应用恢复
- 基础设施恢复

### 2. Key Metrics

#### RPO (Recovery Point Objective)
```
RPO = Maximum Acceptable Data Loss

Example:
- Backup every 4 hours → RPO = 4 hours
- Sync replication → RPO ≈ 0
```

#### RTO (Recovery Time Objective)
```
RTO = Maximum Acceptable Downtime

Example:
- Manual failover → RTO = 4-8 hours
- Auto failover → RTO = 15-30 minutes
```

### 3. Recovery Strategies

#### Strategy Selection Matrix
| Strategy | RTO | RPO | Cost | Complexity |
|----------|-----|-----|------|------------|
| Backup & Restore | 24h+ | 24h | $ | Low |
| Tape Vaulting | 12-24h | 24h | $$ | Low |
| Pilot Light | 1-4h | Minutes | $$$ | Medium |
| Warm Standby | 1-2h | Minutes | $$$ | Medium |
| Hot Standby | Minutes | Seconds | $$$$ | High |
| Multi-Region Active | Seconds | Near 0 | $$$$$ | Very High |

### 4. Cloud-Native DR Patterns

#### AWS
```yaml
services:
  compute: ECS/EKS with multi-AZ
  database: RDS Multi-AZ
  storage: S3 Cross-Region Replication
  dns: Route 53 Health Checks
  cdn: CloudFront Failover
```

#### Azure
```yaml
services:
  compute: Azure VMs with Availability Sets
  database: Azure SQL Geo-Replication
  storage: GRS (Geo-Redundant Storage)
  dns: Traffic Manager
```

#### GCP
```yaml
services:
  compute: Managed Instance Groups
  database: Cloud SQL HA
  storage: Multi-Regional Storage
  dns: Cloud DNS
```

### 5. Data Replication Patterns

#### Synchronous Replication
- Zero data loss
- Higher latency
- Same region typically
- Oracle Data Guard, SQL Server AlwaysOn

#### Asynchronous Replication
- Some data loss possible
- Lower latency
- Cross-region capable
- RDS Read Replicas, PostgreSQL Streaming

#### Log-Based Replication
- Point-in-time recovery
- Lower bandwidth
- CDC (Change Data Capture)
- Debezium, AWS DMS

### 6. DR Testing

#### Test Types
| Type | Description | Frequency |
|------|-------------|-----------|
| Tabletop | Walk-through scenarios | Monthly |
| Simulation | Partial test without actual failover | Quarterly |
| Partial Failover | Failover non-critical systems | Semi-annually |
| Full Failover | Complete failover to DR site | Annually |

#### Success Criteria
```yaml
test_success:
  rto_achieved: true/false
  rpo_achieved: true/false
  data_integrity: true/false
  communication: effective/not_effective
  documentation: accurate/outdated
```

## Best Practices

### Planning
1. Start with business requirements, not technology
2. Define clear RTO/RPO with business input
3. Design for the failure, not the happy path
4. Keep it simple and well-documented
5. Test regularly and document results

### Implementation
1. Automate everything possible
2. Use infrastructure as code
3. Monitor replication lag
4. Regular backup verification
5. Document all configurations

### Testing
1. Test what you plan to recover
2. Test at least annually
3. Include all stakeholders
4. Document failures and improvements
5. Update plans based on tests
