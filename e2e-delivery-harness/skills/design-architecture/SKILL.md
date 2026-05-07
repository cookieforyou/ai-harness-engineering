---
name: design-architecture
description: "Domain skill for design-architecture execution"
type: skill
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['skill', 'knowledge']
---
# Skill: 架构设计 (Architecture Design)

## Overview

本 Skill 定义了架构设计的核心知识体系。

## Core Knowledge

### 架构模式

```python
class ArchitecturePattern:
    """架构模式"""

    @staticmethod
    def microservice_pattern():
        """微服务架构"""
        return {
            "characteristics": [
                "服务独立部署",
                "松耦合",
                "技术多样性",
                "按业务边界拆分"
            ],
            "benefits": [
                "独立扩展",
                "故障隔离",
                "技术自由"
            ],
            "challenges": [
                "分布式复杂度",
                "服务治理",
                "数据一致性"
            ]
        }

    @staticmethod
    def event_driven_pattern():
        """事件驱动架构"""
        return {
            "components": [
                "Event Producer",
                "Event Channel (MQ)",
                "Event Consumer"
            ],
            "patterns": [
                "Publish-Subscribe",
                "Event Sourcing",
                "CQRS"
            ]
        }

    @staticmethod
    def hexagonal_architecture():
        """六边形架构"""
        return {
            "layers": [
                "Domain (核心业务)",
                "Application (用例)",
                "Infrastructure (适配器)"
            ],
            "benefits": [
                "业务逻辑与基础设施分离",
                "易于测试",
                "技术无关性"
            ]
        }
```

### 服务拆分方法

```python
class ServiceDecomposition:
    """服务拆分方法"""

    @staticmethod
    def by_business_capability():
        """按业务能力拆分"""
        decomposition = {
            "ecommerce": [
                "用户服务 (用户、认证)",
                "商品服务 (商品、库存)",
                "订单服务 (订单、购物车)",
                "支付服务 (支付、退款)",
                "物流服务 (配送、跟踪)"
            ]
        }
        return decomposition

    @staticmethod
    def by_domain_driven_design():
        """按领域驱动设计拆分"""
        return {
            "bounded_contexts": [
                "用户上下文",
                "商品上下文",
                "订单上下文",
                "支付上下文"
            ],
            "relationships": [
                "上下文映射",
                "防腐层"
            ]
        }

    @staticmethod
    def by_team():
        """按团队拆分"""
        return {
            "two_pizza_rule": "6-10 人一团队",
            "service_per_team": "1-2 服务/团队",
            "independent_deployment": "团队自主部署"
        }
```

### 容量规划

```python
class CapacityPlanning:
    """容量规划"""

    @staticmethod
    def estimate_requests_per_second(peak_users, requests_per_user):
        """估算 QPS"""
        # 假设峰值用户占比 10%
        peak_users = total_users * 0.1
        # QPS = 峰值用户 * 每用户请求数 / 峰值持续时间
        qps = (peak_users * requests_per_user) / peak_duration_seconds
        return qps

    @staticmethod
    def estimate_instances(desired_qps, capacity_per_instance):
        """估算实例数"""
        instances = desired_qps / capacity_per_instance
        # 考虑冗余
        return int(instances * 1.5)

    @staticmethod
    def estimate_database_capacity(data_size_gb, growth_rate):
        """估算数据库容量"""
        monthly_growth = data_size_gb * growth_rate
        yearly_growth = monthly_growth * 12
        # 考虑 3 年规划 + 50% 余量
        return (data_size_gb + yearly_growth * 3) * 1.5
```

### 可用性设计

```python
class AvailabilityDesign:
    """可用性设计"""

    availability_levels = {
        "99%": "3.65 days downtime/year",
        "99.9%": "8.76 hours downtime/year",
        "99.99%": "52.6 minutes downtime/year",
        "99.999%": "5.26 minutes downtime/year"
    }

    @staticmethod
    def design_for_availability(target):
        """可用性设计策略"""
        strategies = {
            "redundancy": "多副本冗余",
            "failover": "自动故障转移",
            "circuit_breaker": "熔断器保护",
            "graceful_degradation": "优雅降级",
            "health_check": "健康检查"
        }

        if target >= "99.99%":
            return [
                "多区域部署",
                "自动故障转移",
                "实时监控",
                "快速恢复能力"
            ]
        return ["单区域多 AZ", "健康检查"]
```

### 架构评估框架

```python
class ArchitectureAssessment:
    """架构评估"""

    criteria = {
        "scalability": {
            "weight": 0.2,
            "questions": [
                "能否水平扩展？",
                "扩展成本如何？"
            ]
        },
        "availability": {
            "weight": 0.25,
            "questions": [
                "目标 SLA 是多少？",
                "故障恢复时间？"
            ]
        },
        "maintainability": {
            "weight": 0.2,
            "questions": [
                "代码可维护性？",
                "部署复杂度？"
            ]
        },
        "cost": {
            "weight": 0.15,
            "questions": [
                "基础设施成本？",
                "运维成本？"
            ]
        },
        "security": {
            "weight": 0.2,
            "questions": [
                "安全合规要求？",
                "数据保护措施？"
            ]
        }
    }

    @staticmethod
    def evaluate(architecture):
        """评估架构"""
        scores = {}
        for criterion, config in ArchitectureAssessment.criteria.items():
            score = evaluate_criterion(architecture, criterion)
            scores[criterion] = score * config["weight"]

        total_score = sum(scores.values())
        return {
            "total_score": total_score,
            "breakdown": scores,
            "recommendation": "通过" if total_score >= 70 else "需改进"
        }
```

## Architecture Decision Records (ADR)

```markdown
# ADR-001: 使用微服务架构

## Status
已接受

## Context
电商平台需要支持日活 100 万用户，峰值 QPS 10,000

## Decision
采用微服务架构，按业务域拆分为用户、商品、订单、支付等服务

## Consequences
- 正面：独立部署、故障隔离、技术自由
- 负面：分布式复杂度增加

## Trade-offs
增加运维复杂度，换取业务敏捷性
```

## Toolchain

### 架构设计工具

| 工具 | 用途 |
|------|------|
| C4 Model | 架构可视化 |
| draw.io | 架构图绘制 |
| PlantUML | 架构图代码化 |
| Structurizr | C4 模型工具 |

### 评估工具

| 工具 | 用途 |
|------|------|
| ArchUnit | 架构测试 |
| SonarQube | 代码质量 |
| LoadRunner | 性能测试 |

## Associated Assets

- **Scenario**: `../../scenarios/design-architecture/SCENARIO.md`
- **Instruction**: `../../instructions/design-architecture.instructions.md`
- **Prompt**: `../../prompts/design-architecture.prompt.md`
- **Agent**: `../../agents/design-architecture.agent.md`


## Core Knowledge

> Essential knowledge domain for design-architecture execution.

### Domain Fundamentals
- [Core concept 1]
- [Core concept 2]
- [Core concept 3]

### Key Principles
1. [Principle 1]
2. [Principle 2]
3. [Principle 3]


## Best Practices

> Proven practices for design-architecture excellence.

1. **Practice 1**: [Description and rationale]
2. **Practice 2**: [Description and rationale]
3. **Practice 3**: [Description and rationale]


## Common Pitfalls

> Frequent mistakes to avoid during design-architecture execution.

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
