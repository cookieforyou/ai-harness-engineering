---
name: setup-infra
description: "Domain skill for setup-infra execution"
type: skill
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['skill', 'knowledge']
---
# Skill: 基础设施搭建 (Infrastructure Setup)

## Overview

本 Skill 定义了云基础设施搭建的核心知识体系。

## Core Knowledge

### 云计算基础

#### IaaS vs PaaS vs SaaS

```
┌─────────────────────────────────────────┐
│                 SaaS                     │
│  Gmail, Office 365, Slack              │
├─────────────────────────────────────────┤
│                 PaaS                     │
│  Heroku, Azure App Service, AWS Beanstalk│
├─────────────────────────────────────────┤
│                 IaaS                     │
│  AWS EC2, 阿里云 ECS, 华为云 ECS        │
├─────────────────────────────────────────┤
│              Physical                     │
│            物理服务器                     │
└─────────────────────────────────────────┘
```

### VPC 网络设计

#### VPC 组件

```yaml
VPC Components:
  - Virtual Private Cloud (虚拟私有云)
  - Subnets (子网)
    - Public Subnet: 有公网访问
    - Private Subnet: 无公网访问
  - Route Tables (路由表)
  - Internet Gateway (互联网网关)
  - NAT Gateway (NAT 网关)
  - Security Groups (安全组)
  - Network ACLs (网络访问控制列表)
```

#### 网络流量

```
公网 → Internet Gateway → Route Table → Public Subnet
                                              ↓
                                    NAT Gateway
                                              ↓
Private Subnet (通过 NAT 访问公网)

Private Subnet ← Security Group ← Public Subnet
```

### 高可用设计

#### 多可用区架构

```python
# AZ 分布策略
availability_zones = ["az-1a", "az-1b", "az-1c"]

# 最小高可用配置
min_az_count = 2
min_instance_count_per_az = 2

# 计算实例分布
def distribute_instances(total, az_count):
    per_az = total // az_count
    remainder = total % az_count
    return [per_az + (1 if i < remainder else 0) for i in range(az_count)]
```

### 存储层次

| 存储类型 | 延迟 | 成本 | 用途 |
|----------|------|------|------|
| 内存 | < 1ms | $$$$ | Redis, 缓存 |
| NVMe SSD | 1-5ms | $$$ | 数据库 |
| SSD | 5-20ms | $$ | 通用存储 |
| HDD | 50-100ms | $ | 归档 |

### 安全最佳实践

#### 纵深防御

```
Internet
    ↓
WAF/CDN (Layer 7)
    ↓
Load Balancer (Layer 4)
    ↓
Security Group (实例级别)
    ↓
Network ACL (子网级别)
    ↓
VPC (网络隔离)
```

#### IAM 最小权限

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeInstances",
        "ec2:DescribeVpcs",
        "ec2:DescribeSubnets"
      ],
      "Resource": "*"
    }
  ]
}
```

### Cost Optimization

#### 成本分类

| 类别 | 说明 | 优化策略 |
|------|------|----------|
| 计算 | EC2/ECS 实例 | Spot/Preemptible |
| 存储 | EBS/OSS | 生命周期策略 |
| 网络 | 流量/带宽 | CDN/压缩 |
| 数据传输 | 跨区流量 | 同区域优先 |

#### TCO 计算

```python
def calculate_monthly_cost(resources):
    total = 0
    for r in resources:
        if r.type == "compute":
            total += r.hours * r.price_per_hour
        elif r.type == "storage":
            total += r.gb_month * r.price_per_gb
        elif r.type == "network":
            total += r.gb_out * r.price_per_gb
    return total

# 节省推荐
savings_tips = [
    "使用 Reserved/Savings Plan 可节省 30-60%",
    "非生产环境使用 Spot 实例可节省 60-90%",
    "开启实例休眠减少运行时间",
    "使用生命周期策略自动归档数据"
]
```

## Toolchain

### IaC 工具

| 工具 | 特点 | 适用场景 |
|------|------|----------|
| Terraform | 声明式、多云支持 | 复杂基础设施 |
| Ansible | 过程式、配置管理 | 服务器配置 |
| Pulumi | 代码化、通用语言 | 开发者友好 |
| CloudFormation | AWS 原生 | AWS 专用 |

### 监控工具

| 工具 | 平台 | 用途 |
|------|------|------|
| CloudWatch | AWS | 监控告警 |
| ARMS | 阿里云 | APM |
| CloudEye | 华为云 | 监控 |
| Datadog | 多云 | 统一监控 |

## Associated Assets

- **Scenario**: `../../scenarios/setup-infra/SCENARIO.md`
- **Instruction**: `../../instructions/setup-infra.instructions.md`
- **Prompt**: `../../prompts/setup-infra.prompt.md`
- **Agent**: `../../agents/setup-infra.agent.md`


## Core Knowledge

> Essential knowledge domain for setup-infra execution.

### Domain Fundamentals
- [Core concept 1]
- [Core concept 2]
- [Core concept 3]

### Key Principles
1. [Principle 1]
2. [Principle 2]
3. [Principle 3]


## Best Practices

> Proven practices for setup-infra excellence.

1. **Practice 1**: [Description and rationale]
2. **Practice 2**: [Description and rationale]
3. **Practice 3**: [Description and rationale]


## Common Pitfalls

> Frequent mistakes to avoid during setup-infra execution.

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
