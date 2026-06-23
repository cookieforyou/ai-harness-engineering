---
name: setup-infra
description: "Detailed technical instructions for setup-infra scenario execution"
applyTo: "scenarios/setup-infra/**"
phase: deployment
type: instruction
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['instruction', 'technical']
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


## Multi-Language Code Examples

### Terraform HCL - AWS/GCP 多区域高可用基础设施部署

```hcl
# ============================================================
# main.tf - 多区域高可用基础设施部署 (AWS + GCP 混合云)
# ============================================================
# 部署目标:
#   - AWS us-east-1 (Primary)
#   - AWS eu-west-1 (DR/Standby)
#   - GCP us-central1 (Multi-cloud 冗余)
# ============================================================

terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
  # 使用 S3 远程状态存储，支持 state locking
  backend "s3" {
    bucket         = "company-terraform-state"
    key            = "infrastructure/production/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-state-locks"
    encrypt        = true
  }
}

# ============================================================
# 变量定义 (variables.tf)
# ============================================================
variable "environment" {
  description = "部署环境 (production/staging/development)"
  type        = string
  validation {
    condition     = contains(["production", "staging", "development"], var.environment)
    error_message = "Environment must be production, staging, or development."
  }
}

variable "aws_regions" {
  description = "AWS 部署区域列表"
  type        = list(string)
  default     = ["us-east-1", "eu-west-1"]
}

variable "vpc_cidr_blocks" {
  description = "各区域的 VPC CIDR 块"
  type        = map(string)
  default = {
    "us-east-1" = "10.0.0.0/16"
    "eu-west-1" = "10.1.0.0/16"
  }
}

# ============================================================
# AWS Primary Region (us-east-1) - VPC 和网络
# ============================================================
module "vpc_primary" {
  source = "terraform-aws-modules/vpc/aws"
  version = "5.0.0"

  providers = {
    aws = aws.primary
  }

  name = "${var.environment}-vpc-primary"
  cidr = var.vpc_cidr_blocks["us-east-1"]

  # 多 AZ 部署 (最少 3 个可用区)
  azs = ["us-east-1a", "us-east-1b", "us-east-1c"]

  # 子网规划
  public_subnets  = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  private_subnets = ["10.0.11.0/24", "10.0.12.0/24", "10.0.13.0/24"]
  database_subnets = ["10.0.21.0/24", "10.0.22.0/24", "10.0.23.0/24"]

  # NAT Gateway 配置 (每个 AZ 一个，保障高可用)
  enable_nat_gateway     = true
  single_nat_gateway     = false
  one_nat_gateway_per_az = true

  # VPC Flow Logs
  enable_flow_log                      = true
  flow_log_destination_type            = "cloud-watch-logs"
  flow_log_log_group_name_prefix       = "/aws/vpc-flow-logs/${var.environment}-primary-"

  tags = {
    Environment = var.environment
    Region      = "primary"
    ManagedBy   = "terraform"
    CostCenter  = "infrastructure"
  }
}

# ============================================================
# AWS Primary - EKS 集群 (生产级)
# ============================================================
module "eks_primary" {
  source  = "terraform-aws-modules/eks/aws"
  version = "19.15.0"

  providers = {
    aws = aws.primary
  }

  cluster_name    = "${var.environment}-eks-primary"
  cluster_version = "1.28"

  vpc_id     = module.vpc_primary.vpc_id
  subnet_ids = module.vpc_primary.private_subnets

  # 托管节点组
  eks_managed_node_groups = {
    main = {
      desired_size = 3
      min_size     = 3
      max_size     = 10

      instance_types = ["m5.xlarge", "m5a.xlarge"]
      capacity_type  = "ON_DEMAND"

      # 节点自动修复
      update_config = {
        max_unavailable_percentage = 33
      }

      tags = {
        Environment = var.environment
        NodeType    = "application"
      }
    }

    spot = {
      desired_size = 2
      min_size     = 2
      max_size     = 20

      instance_types = ["c5.xlarge", "c5a.xlarge"]
      capacity_type  = "SPOT"

      tags = {
        Environment = var.environment
        NodeType    = "batch"
      }
    }
  }

  # 集群安全组增强规则
  node_security_group_additional_rules = {
    ingress_self_all = {
      description = "Node to node all ports/protocols"
      protocol    = "-1"
      from_port   = 0
      to_port     = 0
      type        = "ingress"
      self        = true
    }
  }
}

# ============================================================
# AWS DR Region (eu-west-1) - 备用基础设施
# ============================================================
module "vpc_dr" {
  source = "terraform-aws-modules/vpc/aws"
  version = "5.0.0"

  providers = {
    aws = aws.dr
  }

  name = "${var.environment}-vpc-dr"
  cidr = var.vpc_cidr_blocks["eu-west-1"]
  azs  = ["eu-west-1a", "eu-west-1b", "eu-west-1c"]

  public_subnets   = ["10.1.1.0/24", "10.1.2.0/24", "10.1.3.0/24"]
  private_subnets  = ["10.1.11.0/24", "10.1.12.0/24", "10.1.13.0/24"]
  database_subnets = ["10.1.21.0/24", "10.1.22.0/24", "10.1.23.0/24"]

  enable_nat_gateway     = true
  single_nat_gateway     = false
  one_nat_gateway_per_az = true
  enable_flow_log        = true

  tags = {
    Environment = var.environment
    Region      = "dr"
    ManagedBy   = "terraform"
  }
}

# ============================================================
# GCP - 多云冗余部署
# ============================================================
resource "google_compute_network" "main" {
  provider = google

  name                    = "${var.environment}-vpc-gcp"
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "private" {
  provider = google

  name          = "${var.environment}-private-gcp"
  network       = google_compute_network.main.id
  region        = "us-central1"
  ip_cidr_range = "10.2.0.0/16"

  private_ip_google_access = true
}

# GKE 集群
resource "google_container_cluster" "primary" {
  provider = google

  name     = "${var.environment}-gke-primary"
  location = "us-central1"

  # 私有集群
  private_cluster_config {
    enable_private_nodes    = true
    enable_private_endpoint = false
    master_ipv4_cidr_block  = "172.16.0.0/28"
  }

  # 节点自动升级和修复
  node_pool_defaults {
    node_config_defaults {
      image_type = "COS_CONTAINERD"
    }
  }

  node_pool {
    name       = "default-pool"
    node_count = 3

    node_config {
      machine_type = "e2-standard-4"
      disk_size_gb = 100
      disk_type    = "pd-ssd"

      oauth_scopes = [
        "https://www.googleapis.com/auth/cloud-platform",
      ]
    }
  }
}
```

### Pulumi - Infrastructure as Code (TypeScript + Python)

```typescript
// ============================================================
// index.ts - Pulumi TypeScript 基础设施定义
// ============================================================
// Pulumi 相比 Terraform 的优势: 完整的编程语言能力 (循环/条件/函数)
// 适用于复杂基础设施逻辑的场景
// ============================================================

import * as aws from "@pulumi/aws";
import * as pulumi from "@pulumi/pulumi";

const config = new pulumi.Config();
const environment = config.require("environment");
const vpcCidr = config.get("vpcCidr") || "10.0.0.0/16";

// ============================================================
// VPC 和网络层
// ============================================================

// 创建 VPC
const vpc = new aws.ec2.Vpc(`${environment}-vpc`, {
    cidrBlock: vpcCidr,
    enableDnsSupport: true,
    enableDnsHostnames: true,
    tags: {
        Name: `${environment}-vpc`,
        Environment: environment,
        ManagedBy: "pulumi",
    },
});

// 创建子网 (遍历 AZ)
const azs = aws.getAvailabilityZones({ state: "available" });
const subnetCount = 3;

const publicSubnets: aws.ec2.Subnet[] = [];
const privateSubnets: aws.ec2.Subnet[] = [];

for (let i = 0; i < subnetCount; i++) {
    // 公有子网 (负载均衡器/NAT)
    const pubSubnet = new aws.ec2.Subnet(`${environment}-public-${i}`, {
        vpcId: vpc.id,
        cidrBlock: `10.0.${i + 1}.0/24`,
        availabilityZone: azs.then(azs => azs.names[i]),
        mapPublicIpOnLaunch: true,
        tags: { Name: `${environment}-public-${i}`, Tier: "public" },
    });
    publicSubnets.push(pubSubnet);

    // 私有子网 (应用服务)
    const privSubnet = new aws.ec2.Subnet(`${environment}-private-${i}`, {
        vpcId: vpc.id,
        cidrBlock: `10.0.${i + 11}.0/24`,
        availabilityZone: azs.then(azs => azs.names[i]),
        tags: { Name: `${environment}-private-${i}`, Tier: "private" },
    });
    privateSubnets.push(privSubnet);
}

// 安全组: Web 层
const webSecurityGroup = new aws.ec2.SecurityGroup(`${environment}-web-sg`, {
    vpcId: vpc.id,
    description: "Web tier security group",
    ingress: [
        { protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] },
        { protocol: "tcp", fromPort: 443, toPort: 443, cidrBlocks: ["0.0.0.0/0"] },
    ],
    egress: [
        { protocol: "-1", fromPort: 0, toPort: 0, cidrBlocks: ["0.0.0.0/0"] },
    ],
    tags: { Name: `${environment}-web-sg` },
});

// 安全组: 应用层
const appSecurityGroup = new aws.ec2.SecurityGroup(`${environment}-app-sg`, {
    vpcId: vpc.id,
    description: "Application tier security group",
    ingress: [
        { protocol: "tcp", fromPort: 8080, toPort: 8080,
          securityGroups: [webSecurityGroup.id] },
    ],
    egress: [
        { protocol: "-1", fromPort: 0, toPort: 0, cidrBlocks: ["0.0.0.0/0"] },
    ],
    tags: { Name: `${environment}-app-sg` },
});

// ============================================================
// ECS Fargate 集群
// ============================================================
const cluster = new aws.ecs.Cluster(`${environment}-cluster`, {
    tags: { Environment: environment },
});

const taskRole = new aws.iam.Role(`${environment}-task-role`, {
    assumeRolePolicy: JSON.stringify({
        Version: "2012-10-17",
        Statement: [{
            Effect: "Allow",
            Principal: { Service: "ecs-tasks.amazonaws.com" },
            Action: "sts:AssumeRole",
        }],
    }),
});

// CloudWatch 日志组
const logGroup = new aws.cloudwatch.LogGroup(`${environment}-app-logs`, {
    retentionInDays: 30,
});

// ECS 服务自动扩缩容
const target = new aws.appautoscaling.Target(`${environment}-app-scaling`, {
    serviceNamespace: "ecs",
    resourceId: pulumi.interpolate`service/${cluster.name}/app-service`,
    scalableDimension: "ecs:service:DesiredCount",
    minCapacity: 2,
    maxCapacity: 10,
});

const scalingPolicy = new aws.appautoscaling.Policy(`${environment}-app-scaling-policy`, {
    serviceNamespace: target.serviceNamespace,
    resourceId: target.resourceId,
    scalableDimension: target.scalableDimension,
    policyType: "TargetTrackingScaling",
    targetTrackingScalingPolicyConfiguration: {
        predefinedMetricSpecification: {
            predefinedMetricType: "ECSServiceAverageCPUUtilization",
        },
        targetValue: 70,
        scaleInCooldown: 300,
        scaleOutCooldown: 60,
    },
});

// 输出关键信息
export const vpcId = vpc.id;
export const clusterName = cluster.name;
export const publicSubnetIds = publicSubnets.map(s => s.id);
export const privateSubnetIds = privateSubnets.map(s => s.id);
```

```python
# ============================================================
# __main__.py - Pulumi Python 基础设施部署
# ============================================================
"""Pulumi Python SDK 示例: 创建 AWS S3 + CloudFront + Route53 基础设施。"""
import pulumi
import pulumi_aws as aws
import pulumi_awsx as awsx
import mimetypes
import os

config = pulumi.Config()
environment = config.require("environment")
domain_name = config.require("domain_name")

# 创建 S3 Bucket (通过 Pulumi 管理已有 Bucket)
bucket = aws.s3.BucketV2(
    f"{environment}-static-assets",
    bucket=f"{environment}-static-{domain_name}",
    force_destroy=False,
    tags={
        "Environment": environment,
        "Purpose": "static-assets",
        "ManagedBy": "pulumi",
    },
)

# 配置静态网站托管
bucket_website = aws.s3.BucketWebsiteConfigurationV2(
    f"{environment}-static-website",
    bucket=bucket.id,
    index_document={"suffix": "index.html"},
    error_document={"key": "error.html"},
)

# 阻止公有访问 (通过 CloudFront OAI 访问)
public_access_block = aws.s3.BlockPublicAccess(
    f"{environment}-block-public-access",
    bucket=bucket.id,
    block_public_acls=True,
    block_public_policy=True,
    ignore_public_acls=True,
    restrict_public_buckets=True,
)

# 创建 CloudFront Origin Access Identity
oai = aws.cloudfront.OriginAccessIdentity(
    f"{environment}-oai",
    comment=f"OAI for {environment} static assets",
)

# S3 Bucket Policy (仅允许 CloudFront 访问)
bucket_policy = aws.s3.BucketPolicy(
    f"{environment}-bucket-policy",
    bucket=bucket.id,
    policy=pulumi.Output.all(bucket.arn, oai.iam_arn).apply(
        lambda args: {
            "Version": "2012-10-17",
            "Statement": [{
                "Effect": "Allow",
                "Principal": {"AWS": args[1]},
                "Action": "s3:GetObject",
                "Resource": f"{args[0]}/*",
            }],
        }
    ),
)

# CloudFront Distribution (全球加速)
distribution = aws.cloudfront.Distribution(
    f"{environment}-cdn",
    enabled=True,
    aliases=[domain_name],
    origins=[{
        "domain_name": bucket.bucket_regional_domain_name,
        "origin_id": "s3-origin",
        "s3_origin_config": {
            "origin_access_identity": oai.cloudfront_access_identity_path,
        },
    }],
    default_cache_behavior={
        "target_origin_id": "s3-origin",
        "viewer_protocol_policy": "redirect-to-https",
        "allowed_methods": ["GET", "HEAD", "OPTIONS"],
        "cached_methods": ["GET", "HEAD"],
        "default_ttl": 3600,
        "max_ttl": 86400,
        "min_ttl": 0,
        "compress": True,
        "forwarded_values": {
            "query_string": False,
            "cookies": {"forward": "none"},
        },
    },
    price_class = "PriceClass_100",  # US/Europe only
    restrictions={
        "geo_restriction": {
            "restriction_type": "whitelist",
            "locations": ["US", "GB", "DE", "JP"],
        },
    },
    viewer_certificate={
        "acm_certificate_arn": config.require("certificate_arn"),
        "ssl_support_method": "sni-only",
        "minimum_protocol_version": "TLSv1.2_2021",
    },
    tags={"Environment": environment},
)

pulumi.export("bucket_name", bucket.id)
pulumi.export("cloudfront_domain", distribution.domain_name)
pulumi.export("cloudfront_id", distribution.id)
```

### Ansible Playbook - 配置管理与自动化部署

```yaml
---
# ============================================================
# playbooks/setup-infrastructure.yml
# Ansible 基础设施配置管理 Playbook
#
# 作用:
#   - 服务器初始化和加固
#   - 中间件安装和配置
#   - 应用部署和健康检查
# ============================================================
- name: "基础设施初始化与配置管理"
  hosts: all
  gather_facts: yes
  become: yes

  vars:
    # ------ 变量定义 ------
    env: "{{ environment | default('production') }}"
    app_user: "appuser"
    app_group: "appgroup"
    app_dir: "/opt/applications"
    log_dir: "/var/log/applications"

    # 安全加固配置
    ssh_port: 22
    fail2ban_enabled: yes
    firewall_enabled: yes

    # 监控 Agent 配置
    monitoring:
      datadog_api_key: "{{ vault_datadog_api_key }}"
      node_exporter_enabled: yes

  # ============================================================
  # 第一阶段: 基础系统加固
  # ============================================================
  tasks:
    - name: "Phase 1: 系统基础加固"
      block:
        - name: "创建应用用户和组"
          group:
            name: "{{ app_group }}"
            state: present
            system: yes

        - name: "创建应用用户"
          user:
            name: "{{ app_user }}"
            group: "{{ app_group }}"
            create_home: no
            shell: /sbin/nologin
            system: yes
            state: present

        - name: "配置 SSH 安全策略"
          lineinfile:
            path: /etc/ssh/sshd_config
            regexp: "{{ item.regexp }}"
            line: "{{ item.line }}"
            state: present
          loop:
            - { regexp: '^PermitRootLogin', line: 'PermitRootLogin no' }
            - { regexp: '^PasswordAuthentication', line: 'PasswordAuthentication no' }
            - { regexp: '^PubkeyAuthentication', line: 'PubkeyAuthentication yes' }
            - { regexp: '^MaxAuthTries', line: 'MaxAuthTries 3' }
          notify: restart sshd

        - name: "安装系统安全包"
          apt:
            name:
              - fail2ban
              - ufw
              - unattended-upgrades
              - auditd
              - rkhunter
            state: present
            update_cache: yes
          when: ansible_os_family == "Debian"

        - name: "配置自动安全更新"
          copy:
            dest: /etc/apt/apt.conf.d/20auto-upgrades
            content: |
              APT::Periodic::Update-Package-Lists "1";
              APT::Periodic::Download-Upgradeable-Packages "1";
              APT::Periodic::AutocleanInterval "7";
              APT::Periodic::Unattended-Upgrade "1";
          when: ansible_os_family == "Debian"

      tags: [security, base]

    # ============================================================
    # 第二阶段: 应用目录和日志
    # ============================================================
    - name: "Phase 2: 应用环境准备"
      block:
        - name: "创建应用目录结构"
          file:
            path: "{{ item }}"
            state: directory
            owner: "{{ app_user }}"
            group: "{{ app_group }}"
            mode: '0755'
          loop:
            - "{{ app_dir }}"
            - "{{ log_dir }}"
            - "{{ app_dir }}/config"
            - "{{ app_dir }}/scripts"

        - name: "配置日志轮转"
          copy:
            dest: /etc/logrotate.d/applications
            content: |
              {{ log_dir }}/*.log {
                  daily
                  rotate 30
                  compress
                  delaycompress
                  missingok
                  notifempty
                  copytruncate
              }

      tags: [app, logging]

    # ============================================================
    # 第三阶段: 监控 Agent 安装
    # ============================================================
    - name: "Phase 3: 监控配置"
      block:
        - name: "安装 Node Exporter (Prometheus)"
          when: monitoring.node_exporter_enabled
          block:
            - name: "下载 Node Exporter"
              get_url:
                url: "https://github.com/prometheus/node_exporter/releases/download/v1.7.0/node_exporter-1.7.0.linux-amd64.tar.gz"
                dest: "/tmp/node_exporter.tar.gz"
                checksum: "sha256:..."
              register: download_result

            - name: "解压并安装 Node Exporter"
              unarchive:
                src: "/tmp/node_exporter.tar.gz"
                dest: "/usr/local/bin"
                remote_src: yes
                creates: "/usr/local/bin/node_exporter"

            - name: "配置 Node Exporter systemd 服务"
              copy:
                dest: /etc/systemd/system/node_exporter.service
                content: |
                  [Unit]
                  Description=Prometheus Node Exporter
                  Wants=network-online.target
                  After=network-online.target

                  [Service]
                  User=nobody
                  ExecStart=/usr/local/bin/node_exporter \
                    --web.listen-address=:9100 \
                    --collector.systemd \
                    --collector.processes
                  Restart=always

                  [Install]
                  WantedBy=multi-user.target
              notify: restart node_exporter

      tags: [monitoring]

  # ============================================================
  # Handlers (服务重启通知)
  # ============================================================
  handlers:
    - name: restart sshd
      systemd:
        name: sshd
        state: restarted
        daemon_reload: yes

    - name: restart node_exporter
      systemd:
        name: node_exporter
        state: restarted
        daemon_reload: yes
        enabled: yes
```

### AWS CloudFormation - 基础设施即代码

```yaml
# ============================================================
# cloudformation/vpc-stack.yaml
# AWS CloudFormation 模板 - VPC + 子网 + 安全组
#
# 适用于需要 AWS 原生基础设施编排的场景
# 优势: 与 AWS 服务深度集成 (Drift Detection, StackSets)
# ============================================================
AWSTemplateFormatVersion: '2010-09-09'
Description: 'Enterprise VPC Infrastructure Stack - Multi-AZ Deployment'

Parameters:
  EnvironmentName:
    Description: Environment name
    Type: String
    AllowedValues: [production, staging, development]
    Default: production

  VpcCIDR:
    Description: CIDR block for the VPC
    Type: String
    Default: 10.0.0.0/16

  PublicSubnetCIDRs:
    Description: CIDR blocks for public subnets (comma-separated)
    Type: CommaDelimitedList
    Default: "10.0.1.0/24,10.0.2.0/24,10.0.3.0/24"

  PrivateSubnetCIDRs:
    Description: CIDR blocks for private subnets (comma-separated)
    Type: CommaDelimitedList
    Default: "10.0.11.0/24,10.0.12.0/24,10.0.13.0/24"

  AvailabilityZones:
    Description: List of Availability Zones
    Type: CommaDelimitedList
    Default: "us-east-1a,us-east-1b,us-east-1c"

Mappings:
  EnvironmentConfig:
    production:
      NatGateways: 3       # 每个 AZ 一个 NAT GW
      FlowLogsEnabled: true
      FlowLogsRetention: 90
    staging:
      NatGateways: 1
      FlowLogsEnabled: true
      FlowLogsRetention: 30
    development:
      NatGateways: 1
      FlowLogsEnabled: false
      FlowLogsRetention: 7

Resources:
  # ============================================================
  # VPC
  # ============================================================
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: !Ref VpcCIDR
      EnableDnsSupport: true
      EnableDnsHostnames: true
      InstanceTenancy: default
      Tags:
        - Key: Name
          Value: !Sub "${EnvironmentName}-vpc"

  # ============================================================
  # 子网 (动态创建)
  # ============================================================
  PublicSubnet1:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      CidrBlock: !Select [0, !Ref PublicSubnetCIDRs]
      AvailabilityZone: !Select [0, !Ref AvailabilityZones]
      MapPublicIpOnLaunch: true
      Tags: [{ Key: Name, Value: !Sub "${EnvironmentName}-public-1" }]

  PublicSubnet2:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      CidrBlock: !Select [1, !Ref PublicSubnetCIDRs]
      AvailabilityZone: !Select [1, !Ref AvailabilityZones]
      MapPublicIpOnLaunch: true
      Tags: [{ Key: Name, Value: !Sub "${EnvironmentName}-public-2" }]

  PrivateSubnet1:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      CidrBlock: !Select [0, !Ref PrivateSubnetCIDRs]
      AvailabilityZone: !Select [0, !Ref AvailabilityZones]
      Tags: [{ Key: Name, Value: !Sub "${EnvironmentName}-private-1" }]

  PrivateSubnet2:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      CidrBlock: !Select [1, !Ref PrivateSubnetCIDRs]
      AvailabilityZone: !Select [1, !Ref AvailabilityZones]
      Tags: [{ Key: Name, Value: !Sub "${EnvironmentName}-private-2" }]

  # ============================================================
  # Internet Gateway
  # ============================================================
  InternetGateway:
    Type: AWS::EC2::InternetGateway
    Properties:
      Tags: [{ Key: Name, Value: !Sub "${EnvironmentName}-igw" }]

  VPCGatewayAttachment:
    Type: AWS::EC2::VPCGatewayAttachment
    Properties:
      VpcId: !Ref VPC
      InternetGatewayId: !Ref InternetGateway

  # ============================================================
  # NAT Gateway (数量取决于环境配置)
  # ============================================================
  NatGatewayEIP:
    Type: AWS::EC2::EIP
    Properties:
      Domain: vpc

  NatGateway:
    Type: AWS::EC2::NatGateway
    Properties:
      AllocationId: !GetAtt NatGatewayEIP.AllocationId
      SubnetId: !Ref PublicSubnet1
      Tags: [{ Key: Name, Value: !Sub "${EnvironmentName}-nat" }]

  # ============================================================
  # 路由表
  # ============================================================
  PublicRouteTable:
    Type: AWS::EC2::RouteTable
    Properties:
      VpcId: !Ref VPC
      Tags: [{ Key: Name, Value: !Sub "${EnvironmentName}-public-rt" }]

  PublicRoute:
    Type: AWS::EC2::Route
    DependsOn: VPCGatewayAttachment
    Properties:
      RouteTableId: !Ref PublicRouteTable
      DestinationCidrBlock: "0.0.0.0/0"
      GatewayId: !Ref InternetGateway

  PrivateRouteTable:
    Type: AWS::EC2::RouteTable
    Properties:
      VpcId: !Ref VPC
      Tags: [{ Key: Name, Value: !Sub "${EnvironmentName}-private-rt" }]

  PrivateRouteToNat:
    Type: AWS::EC2::Route
    Properties:
      RouteTableId: !Ref PrivateRouteTable
      DestinationCidrBlock: "0.0.0.0/0"
      NatGatewayId: !Ref NatGateway

  # ============================================================
  # VPC Flow Logs
  # ============================================================
  FlowLogsRole:
    Condition: EnableFlowLogs
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: 2012-10-17
        Statement:
          - Effect: Allow
            Principal: { Service: vpc-flow-logs.amazonaws.com }
            Action: sts:AssumeRole
      Policies:
        - PolicyName: flow-logs-policy
          PolicyDocument:
            Version: 2012-10-17
            Statement:
              - Effect: Allow
                Action: logs:*
                Resource: "*"

Conditions:
  EnableFlowLogs: !Equals [!FindInMap [EnvironmentConfig, !Ref EnvironmentName, FlowLogsEnabled], true]

Outputs:
  VpcId:
    Description: VPC ID
    Value: !Ref VPC
    Export:
      Name: !Sub "${AWS::StackName}-VpcId"

  PublicSubnetIds:
    Description: List of public subnet IDs
    Value: !Join [",", [!Ref PublicSubnet1, !Ref PublicSubnet2]]

  PrivateSubnetIds:
    Description: List of private subnet IDs
    Value: !Join [",", [!Ref PrivateSubnet1, !Ref PrivateSubnet2]]

  NatGatewayId:
    Description: NAT Gateway ID
    Value: !Ref NatGateway
```

## Error Handling

### Error Scenario 1: 云资源配额不足 (P1)

**触发条件**: Terraform/Pulumi apply 时收到 API 报错 "LimitExceeded" 或 "InsufficientInstanceCapacity"，无法创建所需资源（EC2、EIP、RDS 等）

**处理流程**:
```
IF 收到资源配额不足错误 (QuotaExceeded / InsufficientCapacity)
THEN
  1. 立即识别具体受限资源类型和区域:
     a. 服务配额限制 (VPC/EIP/安全组数量)
     b. 实例容量不足 (特定实例类型在当前 AZ 售罄)
     c. 存储配额限制 (EBS/EFS 容量)
  2. 分类处理:
     IF 服务配额限制:
       a. 通过 AWS Service Quotas / GCP IAM 提交配额提升工单
       b. 优先提升关键资源配额 (VPC: 5→20, EIP: 5→50)
       c. 在 IaC 代码中添加配额检查逻辑
     ELIF 实例容量不足:
       a. 切换到其他可用区 (AZ) 部署
       b. 使用替代实例类型 (m5→m6g, c5→c6a)
       c. 使用 Spot 实例或 ODCR 预留容量
     ELIF 存储配额:
       a. 减少单盘大小，增加盘数（分布式存储）
       b. 清理未使用的快照和旧卷
  3. 实施临时替代方案:
     a. 使用不同区域/AZ 部署受影响资源
     b. 暂用较低规格资源运行，等配额提升后扩容
  4. 更新 IaC 模板，增加配额预检和错误处理逻辑
END
```

**降级方案**: 临时使用不同区域、不同实例类型或不同云提供商替代

**升级条件**: 关键服务（数据库/核心计算）配额无法在 4 小时内得到提升，升级至 Cloud Infrastructure Director 协调

### Error Scenario 2: Terraform State 锁定冲突 (P2)

**触发条件**: 团队成员同时执行 `terraform apply`，DynamoDB State Lock 冲突导致操作失败，错误信息: "Error acquiring the state lock"

**处理流程**:
```
IF Terraform State 锁定冲突
THEN
  1. 不要直接 force-unlock！首先确认谁持有锁:
     a. 运行 terraform plan 确认锁持有者和信息
     b. 在团队沟通渠道发布锁定通知
     c. 联系锁持有者确认当前操作状态
  2. IF 锁由正常操作的团队成员持有:
     a. 等待其操作完成（自动释放锁）
     b. IF 操作正常运行中：等待 max 15 分钟
     c. 沟通确认预计完成时间
  3. IF 锁由已断开连接的会话持有 (Stale Lock):
     a. 运行 terraform force-unlock <LOCK_ID>
     b. 在 force-unlock 前确认无正在运行的 apply
     c. 检查 terraform.tfstate 是否正常
     d. 验证 state 文件未被损坏
  4. 预防措施:
     a. 实施部署审批流程（Only one person at a time）
     b. 使用 CI/CD Pipeline 代替手动 apply
     c. 配置状态文件分区 (每个环境独立的 state)
END
```

**降级方案**: 恢复上一个正常 state 版本 (S3 Versioning)，放弃当前变更

**升级条件**: State 文件损坏或无法恢复，升级至 Infra Lead 从备份恢复

### Error Scenario 3: 安全组规则配置错误 (P1)

**触发条件**: 部署后发现安全组规则过于宽松（如 0.0.0.0/0 开放数据库端口），或过于严格导致服务无法正常通信

**处理流程**:
```
IF 发现安全组规则配置错误
THEN
  1. 立即评估当前风险等级:
     a. 错误类型: 过于宽松 → 立即修复 (P0 安全事件)
     b. 错误类型: 过于严格 → 按依赖关系逐步修复 (P2)
  2. 紧急修复 (过于宽松):
     a. 立即收紧违规规则 (限制源 IP/安全组)
     b. 使用 IaC 更新安全组并 apply
     c. 检查 CloudTrail 日志确认是否有未授权访问
     d. 旋转受影响服务的关键凭据
  3. 影响恢复 (过于严格):
     a. 识别哪些服务间通信被阻断
     b. 按依赖关系图(DAG)逐步修复
     c. 使用自动化测试验证每个修复
  4. 根本原因分析:
     a. 检查 IaC 配置是否使用了过宽的 CIDR
     b. 是否缺少必要的安全组引用规则
     c. 更新安全组设计规范和审查清单
  5. 增加自动化检测:
     a. 添加 terraform-compliance / cfn-guard 策略检查
     b. 实施安全组规则的自动化测试
     c. 配置 Security Hub / GuardDuty 实时监控
END
```

**降级方案**: 对于过于严格的情况，临时开放特定通信路径，后续通过 IaC 固化

**升级条件**: 安全组错误导致数据泄露或核心服务完全不可用，启动安全事件响应

### Error Scenario 4: IaC 部署版本不一致 (P2)

**触发条件**: 多人修改 IaC 代码导致 state drift，实际基础设施与 IaC 配置不一致，再次 apply 产生意外变更

**处理流程**:
```
IF Terraform Plan 显示意外的资源变更 (state drift)
THEN
  1. 全面检查 state drift 的范围:
     a. 运行 terraform plan 生成完整的 diff 报告
     b. 识别哪些是预期的变更，哪些是 drift
     c. 检查是否有手动改动的资源 (Console/CLI 操作)
  2. 处理 drift:
     a. 对于预期的 drift: 更新 terraform state 或接受变更
     b. 对于意外的 drift: 调查谁做了手动变更
     c. 对于已废弃的资源: terraform state rm
  3. 恢复一致性:
     a. 使用 terraform apply 让 IaC 覆盖 drift
     b. 如果 drift 有合理原因，先更新 IaC 代码
     c. 执行 terraform plan 确认只有预期变更
  4. 预防措施:
     a. 实施 Change Control: 所有基础设施变更必须通过 IaC
     b. 配置 Drift Detection: Terraform Cloud / 定期 plan 任务
     c. 添加 pre-commit hook 格式化 IaC 代码
     d. CI/CD 中自动运行 terraform validate + plan
END
```

**降级方案**: 对非关键 drift 手动执行 terraform import 同步 state，不做 apply

**升级条件**: Drift 导致生产环境不稳定，需要回滚 IaC 到上次已知正常版本

## Quality Standards

> Acceptance criteria and quality gates for setup-infra deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | IaC coverage is 95% or higher | Automated check |
| Standard 2 | New environment provisioning is 30 minutes or less | Automated check |
| Standard 3 | Security baseline compliance is 100% | Automated check |
## References

- [harness-engineering.md](../standards/harness-engineering.md)
- [output-validation-checklist.md](../evaluations/output-validation-checklist.md)
- [regression-checklist.md](../evaluations/regression-checklist.md)
