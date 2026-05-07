---
name: respond-incident
description: 事件响应场景的技术指令
type: instructions
stage: "respond-incident"
version: "1.1.0"
---

# Incident Response Instructions

## Overview

This instruction defines the technical execution standards and operational procedures for incident response across the E2E delivery lifecycle. It covers incident classification and severity assignment, triage procedures, communication cadences, escalation paths, mitigation techniques, and post-incident stabilization procedures. The instruction ensures rapid, coordinated response to production incidents with clear roles, defined service level targets for detection and resolution, and continuous improvement through blameless post-incident reviews.


## Incident Lifecycle

```
Detection → Triage → Response → Mitigation → Resolution → Follow-up
     │          │         │          │            │           │
  告警触发   严重程度    组建团队    临时修复     根本解决    复盘改进
```

## Severity Response Matrix

| Severity | Response Time | Mitigation SLA | Resolution SLA | Communication |
|----------|---------------|----------------|----------------|---------------|
| P0 | 5 min | 15 min | 1 hour | Every 15 min |
| P1 | 15 min | 1 hour | 4 hours | Every 30 min |
| P2 | 1 hour | 4 hours | 8 hours | Every 2 hours |
| P3 | 4 hours | 8 hours | 24 hours | Daily |

## On-Call Best Practices

### Rotation Structure
```yaml
oncall_rotation:
  primary:
    name: "Primary On-Call"
    escalation: 1
    response_time: 5 min
    
  secondary:
    name: "Secondary On-Call"
    escalation: 2
    response_time: 15 min
    
  manager:
    name: "On-Call Manager"
    escalation: 3
    response_time: 30 min
```

### Escalation Rules
```yaml
escalation:
  - condition: "No response in 5 min"
    action: "Escalate to secondary"
    
  - condition: "Issue not resolved in 30 min"
    action: "Escalate to manager"
    
  - condition: "P0 incident"
    action: "Immediate all-hands"
```

## Diagnostic Commands

### System Health
```bash
# CPU and Memory
top -bn1 | head -20
free -m
uptime

# Disk
df -h
iostat -x 5 3

# Network
netstat -tuln
ss -s
```

### Application Health
```bash
# Process status
ps aux | grep <process>
systemctl status <service>

# Logs
tail -f {{log_dir}}/<service>.log
journalctl -u <service> -n 100

# Port check
lsof -i :<port>
```

### Kubernetes
```bash
# Pod status
kubectl get pods -n <namespace>
kubectl describe pod <pod> -n <namespace>

# Events
kubectl get events -n <namespace> --sort-by='.lastTimestamp'

# Logs
kubectl logs <pod> -n <namespace> --tail=100
kubectl logs <pod> -n <namespace> --previous
```

## Common Fix Patterns

### Pattern 1: Pod Restart
```bash
kubectl rollout restart deployment/<name> -n <namespace>
kubectl rollout undo deployment/<name> -n <namespace>
```

### Pattern 2: Scale Up
```bash
kubectl scale deployment/<name> --replicas=10 -n <namespace>
```

### Pattern 3: Resource Adjustment
```bash
kubectl patch deployment/<name> -n <namespace> -p '{"spec":{"template":{"spec":{"containers":[{"name":"<container>","resources":{"limits":{"memory":"2Gi"}}}]}}}}'
```

### Pattern 4: Config Reload
```bash
kubectl exec <pod> -n <namespace> -- kill -HUP 1
```

## Communication Templates

### Incident Declaration
```markdown
## Incident Declaration

**事件 ID**: INC-2024-001
**严重程度**: P1
**状态**: Active
**时间**: 2024-01-01 14:30 UTC

### 影响
- 服务: API Gateway
- 影响范围: 约 30% 请求失败
- 用户影响: 部分用户无法下单

### 当前状态
- 已识别根因
- 正在执行修复

### 下次更新时间
15:00 UTC

### 事件频道
#incident-2024-001
```

### Status Update
```markdown
## Status Update (15:00 UTC)

**事件 ID**: INC-2024-001
**更新次数**: 3

### 当前状态
- [x] 根因已识别
- [x] 修复方案已确定
- [ ] 修复执行中
- [ ] 验证中

### 最新进展
正在执行 Pod 重启，预计 10 分钟内完成

### 下次更新时间
15:30 UTC
```

### Incident Resolution
```markdown
## Incident Resolution

**事件 ID**: INC-2024-001
**解决时间**: 15:45 UTC
**总持续时间**: 1 小时 15 分钟

### 摘要
API Gateway 因配置变更导致内存泄漏，已通过回滚配置解决

### 时间线
- 14:30 - 首次告警
- 14:35 - 事件升级 P1
- 14:50 - 根因识别
- 15:30 - 开始修复
- 15:45 - 服务恢复

### 影响统计
- 受影响用户: ~5,000
- 失败请求: ~50,000
- 业务损失: ~$1,000

### 后续行动
- [ ] 改进配置变更流程
- [ ] 增加内存监控告警
- [ ] 制定容量规划

### 复盘会议
时间: 2024-01-03 14:00 UTC
```

## Runbooks

### Runbook 1: High CPU
```bash
#!/bin/bash
# High CPU Investigation

# 1. Identify top CPU processes
top -bn1 -o %CPU | head -15

# 2. Check for runaway processes
ps aux --sort=-%cpu | head -10

# 3. Container-level CPU
docker stats --no-stream

# 4. Application logs
grep -i "error\|warning" {{log_dir}}/app.log | tail -50

# 5. If necessary, restart
systemctl restart <service>
```

### Runbook 2: Database Connection Exhaustion
```bash
#!/bin/bash
# Database Connection Issue

# 1. Check connection count
SELECT count(*) FROM pg_stat_activity;

# 2. Check long-running queries
SELECT * FROM pg_stat_activity WHERE state = 'active' AND query_start < now() - interval '5 minutes';

# 3. Kill long-running queries (if needed)
SELECT pg_terminate_backend(pid);

# 4. Check application connection pool
curl -s <app>/actuator/metrics/hikaricp.connections.active
```

### Runbook 3: Service Not Responding
```bash
#!/bin/bash
# Service Not Responding

# 1. Check if service is running
systemctl status <service>
curl -v {{health_endpoint}}

# 2. Check network connectivity
telnet <host> <port>
nc -zv <host> <port>

# 3. Check upstream dependencies
curl -v http://<upstream>/health

# 4. Check DNS resolution
nslookup <service>
dig <service>

# 5. If healthy, restart
systemctl restart <service>
```

## SLA Calculator

```python
def calculate_impact(sla_target, downtime_minutes, users_affected, total_users):
    """
    Calculate business impact of an incident
    
    Args:
        sla_target: SLA percentage (e.g., 99.95)
        downtime_minutes: Total downtime in minutes
        users_affected: Number of users affected
        total_users: Total users
    """
    current_uptime = 100 - (downtime_minutes / (30 * 24 * 60) * 100)
    users_impact_pct = (users_affected / total_users) * 100
    revenue_impact = estimate_revenue_impact(downtime_minutes)
    
    return {
        "current_uptime": current_uptime,
        "sla_violation": current_uptime < sla_target,
        "users_impact_pct": users_impact_pct,
        "revenue_impact": revenue_impact
    }
```


## Technical Specifications

> Detailed technical requirements and implementation guidelines for respond-incident.

### Required Tools
- [List required tools and frameworks]

### Environment Requirements
- [List environment prerequisites]

### Configuration Parameters
- [List key configuration parameters]


## Best Practices

> Industry-standard best practices for respond-incident execution.

1. **Practice 1**: Acknowledge alerts promptly and assess severity
2. **Practice 2**: Communicate status updates to stakeholders regularly
3. **Practice 3**: Document timeline and actions for post-incident review


## Error Handling

> Common error scenarios and resolution strategies for respond-incident.

### Error Category 1
**Symptom**: Incident response is delayed or uncoordinated
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]

### Error Category 2
**Symptom**: Communication to stakeholders is missing or delayed
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]


## Quality Standards

> Acceptance criteria and quality gates for respond-incident deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | Mean time to recovery (MTTR) is 1 hour or less | Automated check |
| Standard 2 | Escalation accuracy is 90% or higher | Automated check |
| Standard 3 | First communication is sent within 15 minutes | Automated check |
