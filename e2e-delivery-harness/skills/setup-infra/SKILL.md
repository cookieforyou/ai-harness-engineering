---
name: setup-infra
description: "Domain skill for setup-infra execution"
category: deployment
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
- **IaC (Infrastructure as Code)**: 通过代码而非手动流程来管理和配置基础设施的基础实践。声明式(如Terraform)或过程式(如Ansible)定义基础设施状态，确保环境一致性、可重复性和版本控制。
- **Immutable Infrastructure**: 基础设施组件一旦部署即不可修改的理念。任何变更通过替换整个组件而非原地更新来实现，消除了配置漂移，简化了回滚和扩缩容操作。
- **Defense in Depth (纵深防御)**: 多层安全防护架构，在网络边界、主机、应用和数据层面分别设置安全控制措施。任何单层防御被突破时，后续层级仍能提供保护。

### Key Principles
1. **幂等性 (Idempotency)**: IaC脚本无论执行一次还是多次都应该产生相同的结果状态。幂等性是基础设施自动化的基石，确保重复执行不会导致不可预期的副作用或资源重复创建。
2. **最小权限 (Least Privilege)**: 每个身份(用户/服务/角色)仅授予完成其职责所必需的最小权限集合。遵循此原则可以限制潜在攻击面，减少因凭证泄露或误操作造成的损害范围。
3. **基础设施版本化**: 所有基础设施定义代码、配置文件和部署参数都必须纳入版本控制系统。版本化提供变更审计轨迹、回滚能力和团队协作基础，是IaC实践的核心前提。


## Best Practices

> Proven practices for setup-infra excellence.

1. **Terraform模块化设计**: 将基础设施拆分为可复用的模块(Module)，每个模块封装特定资源组(如VPC网络、数据库集群、Kubernetes节点池)。模块化设计通过输入变量和输出值定义清晰的接口边界，提高代码复用性、降低维护复杂度，并支持团队并行开发不同模块。

2. **多AZ高可用部署**: 在每个可用区(Availability Zone)中部署至少一个计算实例，配合负载均衡器实现跨AZ流量分发。多AZ架构消除单点故障，当单个AZ因电力、网络或硬件故障不可用时，流量自动路由到其他健康AZ，确保业务连续性。

3. **成本标签管理**: 为所有云资源施加统一的标签(Tag)策略，包含环境(Environment)、项目(Project)、团队(Team)、成本中心(Cost Center)等维度。标签策略使成本分析和优化具备可操作性，支持按维度展示账单、设置预算告警，以及自动执行基于标签的运维策略。

## Anti-patterns (反模式)

> 与 Common Pitfalls 同义，执行时合并检查。

## Common Pitfalls

> Frequent mistakes to avoid during setup-infra execution.

### Pitfall 1: 手动修改IaC管理的资源 (配置漂移)
**Risk**: 通过云控制台或CLI直接手动修改由IaC创建的资源的配置。这些手动变更不会被IaC状态文件记录，导致下次执行IaC时配置被强制还原，或出现无法预期的错误。
**Prevention**: 对所有生产环境资源严格执行"禁止手动修改"策略。如需变更，必须修改IaC代码并通过CI/CD管道部署。使用Drift Detection工具(如Terraform Plan、CloudFormation Drift Detection)定期扫描并告警漂移。
**Impact**: 配置漂移累积导致基础设施状态不可信，故障时难以排查根因，严重时可能导致误删除生产资源或服务中断。

### Pitfall 2: 硬编码敏感信息
**Risk**: 在IaC代码或配置文件中直接写入API密钥、数据库密码、SSH私钥等敏感信息。硬编码的敏感信息会被提交到版本控制系统，构成严重的安全泄露风险。
**Prevention**: 使用云服务商提供的Secret管理服务(如AWS Secrets Manager、AWS KMS、Azure Key Vault、GCP Secret Manager)或HashiCorp Vault存储敏感信息。IaC代码通过引用方式获取密钥，绝不在代码库中明文存储。
**Impact**: 敏感信息一旦泄露可能导致数据泄露、账户盗用、资源滥用和重大财务损失，且违规行为可能违反合规要求(如PCI DSS、GDPR)。

### Pitfall 3: 忽视区域容量限制
**Risk**: 在单一云区域中部署全部关键资源，未考虑云服务商的区域服务容量限制(如EC2实例类型配额、VPC数量限制、API请求速率限制)。高峰期或大规模扩缩容时可能遭遇配额不足。
**Prevention**: 在架构设计阶段即确认区域服务配额，并提交配额提升请求；关键业务采用多区域部署分散风险；通过云服务商配额监控工具设置接近阈值告警。
**Impact**: 紧急扩缩容时因配额不足受阻，导致服务容量无法满足业务需求；严重情况下所有流量集中单一区域，区域故障时导致完全服务中断。
