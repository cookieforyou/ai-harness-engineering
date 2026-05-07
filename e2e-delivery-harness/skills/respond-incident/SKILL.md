---
name: respond-incident
description: "Domain skill for respond-incident execution"
type: skill
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['skill', 'knowledge']
---
# Incident Response Skill

## Core Knowledge

### 1. Incident Management Framework

#### The Three Tenets
1. **Prepare**: 做好准备，建立流程和工具
2. **Respond**: 快速响应，控制局面
3. **Learn**: 持续学习，改进预防

#### Incident Roles
| Role | Responsibility |
|------|----------------|
| Incident Commander | 统一指挥，协调资源 |
| Technical Lead | 技术诊断，问题解决 |
| Comms Lead | 对外沟通，状态更新 |
| Scribe | 记录时间线，维护文档 |

### 2. Severity Classification

#### P0 - Critical
- 核心服务完全不可用
- 数据丢失或损坏
- 安全事件
- 多服务故障

#### P1 - High
- 核心功能不可用
- >25% 用户受影响
- 性能严重下降

#### P2 - Medium
- 非核心功能异常
- <25% 用户受影响
- 可接受的降级

#### P3 - Low
- 小范围问题
- 用户可绕过的故障
- 非紧急

### 3. Root Cause Analysis

#### 5 Whys Method
```
Problem: Service is down
Why 1: Server crashed
Why 2: Out of memory
Why 3: Memory leak in application
Why 4: Connection not closed properly
Why 5: Missing try-finally block
Root Cause: 代码缺少资源释放
```

#### Fault Tree Analysis
```
Service Down
├── Hardware Failure
│   ├── Power Supply
│   ├── Disk Failure
│   └── Network Card
├── Software Failure
│   ├── Application Crash
│   │   ├── Memory Leak
│   │   └── Unhandled Exception
│   └── Configuration Error
└── Network Failure
    ├── DNS Resolution
    ├── Load Balancer
    └── Firewall Rules
```

### 4. Post-Incident Review

#### Timeline Template
```yaml
timeline:
  - time: "14:30"
    event: "告警触发"
    actor: "监控系统"
  - time: "14:31"
    event: "值班工程师响应"
    actor: "On-call"
  - time: "14:35"
    event: "事件升级 P1"
    actor: "值班工程师"
```

#### Postmortem Template
```markdown
## Incident Postmortem

### Summary
- 日期: 2024-01-01
- 持续时间: 2 小时
- 严重程度: P1
- 影响: 5,000 用户受影响

### Timeline
- 详细时间线

### Root Cause
- 根本原因分析

### What Went Well
- 做得好的方面

### What Could Be Improved
- 需要改进的方面

### Action Items
- 改进措施和责任人
```

### 5. Alert Fatigue Prevention

#### Alert Quality Criteria
- **Actionable**: 每个告警都应可操作
- **Relevant**: 只告警重要事件
- **Timely**: 及时但不过度
- **Contextual**: 提供足够上下文

#### SLO-Based Alerting
```yaml
slo:
  availability: 99.9%
  latency_p99: 500ms
  
alert_thresholds:
  availability:
    warning: 99.5%
    critical: 99.0%
  latency_p99:
    warning: 400ms
    critical: 600ms
```

## Best Practices

### Before Incident
1. 建立清晰的事件响应流程
2. 保持响应团队培训
3. 维护最新的联系信息
4. 定期演练事件响应
5. 优化监控和告警

### During Incident
1. 快速确认和评估
2. 及时升级和通知
3. 专注问题解决
4. 保持清晰沟通
5. 记录关键事件

### After Incident
1. 及时复盘总结
2. 制定改进措施
3. 跟踪行动项完成
4. 更新流程和文档
5. 分享学习经验


## Common Pitfalls

> Frequent mistakes to avoid during respond-incident execution.

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
