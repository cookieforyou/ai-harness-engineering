---
name: setup-infra
description: Detailed technical instructions for setup-infra scenario execution
type: instruction
version: "1.1.0"
stage: setup-infra
---

# Instructions: 基础设施搭建 (Setup Infrastructure)

## Cloud Provider Selection Standards

### AWS

| 服务 | 用途 | 配置要点 |
|------|------|----------|
| EC2 | 通用计算 | 选择 t3/m5/c5 系列 |
| VPC | 网络隔离 | 合理划分 CIDR |
| RDS | 数据库 | 配置 Multi-AZ |
| ElastiCache | 缓存 | Redis/Memcached |
| ALB/NLB | 负载均衡 | HTTPS 终端 |
| CloudWatch | 监控 | 设置告警阈值 |

### 阿里云

| 服务 | 用途 | 配置要点 |
|------|------|----------|
| ECS | 通用计算 | 选择 ecs.sn2ne/ecs.c5 |
| VPC | 网络隔离 | 使用高级模式 |
| RDS | 数据库 | 主从版/高可用版 |
| Redis | 缓存 | 集群版/读写分离 |
| SLB | 负载均衡 | HTTP/HTTPS |
| ARMS | 监控 | 应用监控 |

### 华为云

| 服务 | 用途 | 配置要点 |
|------|------|----------|
| ECS | 通用计算 | 选择 s6/c3/s3 系列 |
| VPC | 网络隔离 | 合理子网规划 |
| RDS | 数据库 | 主备版/企业版 |
| DCS | 缓存 | Redis/Memcached |
| ELB | 负载均衡 | HTTPS 终端 |
| CloudEye | 监控 | 设置告警规则 |

## VPC 设计规范

### CIDR 规划

```yaml
# 推荐 VPC CIDR 块
10.0.0.0/16    # 默认 VPC
172.16.0.0/12  # 中型网络
192.168.0.0/16 # 小型网络

# 子网划分示例 (10.0.0.0/16)
Public Subnets (10.0.1.0/24, 10.0.2.0/24):
  - Web 层
  - 负载均衡器

Private Subnets (10.0.11.0/24, 10.0.12.0/24):
  - 应用层
  - 中间件

Data Subnets (10.0.21.0/24, 10.0.22.0/24):
  - 数据库层
  - 缓存层
```

### 安全组规则

```yaml
# Web 服务器安全组
Ingress:
  - Port: 80, Source: 0.0.0.0/0    # HTTP
  - Port: 443, Source: 0.0.0.0/0  # HTTPS
  - Port: 22, Source: 10.0.0.0/16 # SSH (限制来源)

Egress:
  - Port: ALL, Dest: 0.0.0.0/0     # 允许所有出站

# 数据库安全组
Ingress:
  - Port: 3306, Source: 10.0.11.0/24  # MySQL (应用层)
  - Port: 5432, Source: 10.0.11.0/24  # PostgreSQL

# 禁止规则
  - Port: 3389, Source: 0.0.0.0/0    # 禁止 RDP
```

## Resource Specification Selection

### 计算资源

| 负载类型 | 推荐配置 | 说明 |
|----------|----------|------|
| 轻量 Web | 2 vCPU, 4GB | 测试/开发环境 |
| 标准 Web | 4 vCPU, 8GB | 中等流量 |
| 计算密集 | 8 vCPU, 16GB | AI/大数据 |
| 内存密集 | 4 vCPU, 32GB | 缓存/数据库 |

### 存储资源

| 存储类型 | 用途 | 性能 |
|----------|------|------|
| SSD (gp3/gp2) | 通用存储 | 100-3000 IOPS |
| Provisioned IOPS | 数据库 | 1000-64000 IOPS |
| Cold Storage | 归档 | 低成本 |
| EFS/SMB | 共享存储 | 网络文件系统 |

## High Availability Architecture

### 多可用区部署

```
                    ┌─────────────┐
                    │   Internet  │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │     ALB     │
                    └──────┬──────┘
           ┌───────────────┼───────────────┐
           │               │               │
    ┌──────▼──────┐  ┌──────▼──────┐  ┌──────▼──────┐
    │  AZ-1: Web  │  │  AZ-2: Web  │  │  AZ-N: Web  │
    └──────┬──────┘  └──────┬──────┘  └──────┬──────┘
           │               │               │
    ┌──────▼──────┐  ┌──────▼──────┐  ┌──────▼──────┐
    │ AZ-1: App   │  │ AZ-2: App   │  │ AZ-N: App   │
    └──────┬──────┘  └──────┬──────┘  └──────┬──────┘
           │               │               │
    ┌──────▼──────┐  ┌──────▼──────┐  ┌──────▼──────┐
    │  AZ-1: DB   │  │  AZ-2: DB   │  │  AZ-N: DB   │
    │ (Primary)   │  │ (Replica)   │  │ (Replica)   │
    └─────────────┘  └─────────────┘  └─────────────┘
```

### 自动扩缩容配置

```yaml
# Auto Scaling Group 配置
min_size: 2
max_size: 10
desired_capacity: 4

scaling_policies:
  - name: "ScaleUp"
    metric: CPUUtilization
    threshold: 70
    adjustment: +1
    cooldown: 300

  - name: "ScaleDown"
    metric: CPUUtilization
    threshold: 30
    adjustment: -1
    cooldown: 600
```

## Monitoring and Alerting Configuration

### 基础监控指标

| 指标 | 告警阈值 | 严重程度 |
|------|----------|----------|
| CPU 使用率 | > 80% | Warning |
| CPU 使用率 | > 95% | Critical |
| 内存使用率 | > 85% | Warning |
| 磁盘使用率 | > 80% | Warning |
| 磁盘使用率 | > 95% | Critical |
| 网络带宽 | > 70% | Warning |
| 实例状态 | 非 Running | Critical |

### 告警通知配置

```yaml
alarm_actions:
  - sns_topic_arn: "arn:aws:sns:xxx:alerts"
    notify_levels: ["Critical", "High"]

  - webhook_url: "https://hooks.slack.com/xxx"
    notify_levels: ["Critical"]
```

## IaC 最佳实践

### Terraform 结构

```
terraform/
├── main.tf                 # 主配置
├── variables.tf            # 变量定义
├── outputs.tf              # 输出定义
├── modules/
│   ├── vpc/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   ├── ec2/
│   └── rds/
└── environments/
    ├── dev/
    ├── staging/
    └── prod/
```

### Status管理

```bash
# 使用远程状态
terraform {
  backend "s3" {
    bucket = "terraform-state"
    key    = "project/env/terraform.tfstate"
    region = "cn-north-1"
  }
}
```

## Cost Optimization

### 成本节省策略

| 策略 | 节省比例 | 适用场景 |
|------|----------|----------|
| 使用 Spot 实例 | 60-90% | 非关键批处理 |
| 预留实例 | 30-60% | 稳定负载 |
| 自动启停 | 40-60% | 开发测试环境 |
| 生命周期策略 | 20-40% | 存储优化 |

### 成本监控

```yaml
# 设置预算告警
budget:
  monthly_limit: 1000
  alert_thresholds:
    - 50%   # 轻度告警
    - 75%   # 中度告警
    - 90%   # 重度告警
    - 100%  # 超预算告警
```


## Overview

> High-level description of the setup-infra execution process.
>
> This instruction defines the technical approach, key activities, and success criteria for the setup-infra scenario.


## Technical Specifications

> Detailed technical requirements and implementation guidelines for setup-infra.

### Required Tools
- [List required tools and frameworks]

### Environment Requirements
- [List environment prerequisites]

### Configuration Parameters
- [List key configuration parameters]


## Best Practices

> Industry-standard best practices for setup-infra execution.

1. **Practice 1**: Define infrastructure as code with version control
2. **Practice 2**: Apply security baseline and network segmentation
3. **Practice 3**: Document environment topology and access controls


## Error Handling

> Common error scenarios and resolution strategies for setup-infra.

### Error Category 1
**Symptom**: Infrastructure deployment is manual and error-prone
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]

### Error Category 2
**Symptom**: Security baseline is not enforced consistently
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]


## Quality Standards

> Acceptance criteria and quality gates for setup-infra deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | IaC coverage is 95% or higher | Automated check |
| Standard 2 | New environment provisioning is 30 minutes or less | Automated check |
| Standard 3 | Security baseline compliance is 100% | Automated check |
