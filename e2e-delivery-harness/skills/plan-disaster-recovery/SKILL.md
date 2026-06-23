---
name: plan-disaster-recovery
description: "Domain skill for plan-disaster-recovery execution"
category: governance
type: skill
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['skill', 'knowledge']
---
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


## Anti-patterns (反模式)

> 与 Common Pitfalls 同义，执行时合并检查。

## Common Pitfalls

> Frequent mistakes to avoid during plan-disaster-recovery execution.

### Pitfall 1: 灾备方案只写不练
**Risk**: 编制了详细的灾备方案文档，但从未或极少进行实际演练。文档中的步骤可能因环境变更、人员变动或工具升级而过时，灾难发生时才发现方案不可行或关键步骤缺失。
**Prevention**: 设定定期的灾难恢复演练计划——季度桌面推演、半年度部分切换、年度全量切换。每次演练结束后更新灾备方案，修正与实际操作不一致的内容。将演练纳入组织的OKR或KPI考核指标，确保资源投入。
**Impact**: 灾难真实发生时，团队按照过时的方案操作，恢复时间远超RTO目标；关键步骤无法执行导致恢复失败，业务长时间中断，造成重大经济损失和声誉损害。

### Pitfall 2: 忽视网络分区场景
**Risk**: 灾备设计只覆盖了单节点故障或单数据中心故障等简单场景，未考虑网络分区(Network Partition)这类复杂的故障模式——即节点之间的网络连接中断但各自仍正常运行，导致"脑裂"(Split-Brain)问题。
**Prevention**: 在设计阶段引入网络分区假设，测试系统在部分节点无法通信时的行为；使用Quorum(仲裁)机制解决分布式系统的一致性问题；在演练中注入网络分区故障(如通过Chaos Mesh、Gremlin的Network Blackhole实验)验证系统行为。
**Impact**: 网络分区发生时多个数据副本同时写入导致数据不一致；恢复后需要人工介入解决数据冲突，恢复时间大幅延长；严重时需要从备份恢复数据，丢失大量已写入数据。

### Pitfall 3: 恢复后不验证数据一致性
**Risk**: 成功完成灾备切换后，误以为系统已经恢复正常就宣布演练结束或恢复完成，未对数据的完整性、一致性和时效性进行系统性验证。实际恢复的数据可能存在丢失、部分损坏或复制延迟导致的陈旧数据。
**Prevention**: 在灾备切换的Runbook中强制加入数据一致性验证步骤——包括行数对比、Checksum校验、业务逻辑抽样验证和增量数据完整性验证。验证应由独立于切换操作的人员执行。验证未通过时视为切换失败，需执行回滚或修复流程。
**Impact**: 使用不一致的数据对外提供服务，业务决策基于错误数据；累积的数据差异随着时间越来越大，最终导致完全无法使用的数据灾难；合规审计中发现数据不完整引发的法律和监管风险。
