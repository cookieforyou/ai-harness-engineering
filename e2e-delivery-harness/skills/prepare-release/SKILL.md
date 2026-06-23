---
name: prepare-release
description: "Domain skill for prepare-release execution"
category: deployment
type: skill
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
language: "zh-CN"
tags: ['skill', 'knowledge']
---
# Skill: 发布准备 (Release Preparation)

## Overview

本 Skill 定义了发布准备的核心知识体系。

## Core Knowledge

### 发布生命周期

```
┌─────────────────────────────────────────────────────────────────┐
│                    RELEASE LIFECYCLE                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐        │
│  │   PLAN  │ → │ PREPARE │ → │ EXECUTE │ → │ MONITOR │        │
│  └─────────┘   └─────────┘   └─────────┘   └─────────┘        │
│       ↓             ↓             ↓             ↓             │
│    制定计划      准备资源      执行发布      监控验证         │
│                                                                 │
│                      ┌─────────┐                               │
│                      │  CLOSE  │                               │
│                      └─────────┘                               │
│                           ↓                                    │
│                      发布收尾                                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 发布策略

#### 蓝绿部署

```
┌────────────────────────────────────────────────────────────�─┐
│                      BLUE-GREEN DEPLOYMENT                 │
├────────────────────────────────────────────────────────────┤
│                                                             │
│   ┌─────────┐         ┌─────────┐         ┌─────────┐     │
│   │  Load   │─────────▶│  Blue   │         │  Green  │     │
│   │ Balancer│         │  v1.0   │         │  v2.0   │     │
│   └─────────┘         └─────────┘         └─────────┘     │
│                           │                   │           │
│                      [当前版本]           [待发布版本]     │
│                                                             │
│   切换过程:                                                 │
│   1. 部署 Green 环境 (v2.0)                                  │
│   2. 验证 Green 环境                                        │
│   3. 切换流量到 Green                                        │
│   4. 保留 Blue 环境作为回滚                                  │
│                                                             │
└────────────────────────────────────────────────────────────┘
```

#### 灰度发布

```python
class CanaryRelease:
    """灰度发布策略"""

    strategies = {
        "random": {
            "percentage": 10,
            "description": "随机 10% 流量"
        },

        "user_based": {
            "criteria": "user_id",
            "method": "hash(user_id) % 100 < percentage",
            "description": "基于用户 ID 灰度"
        },

        "region_based": {
            "regions": ["cn-north"],
            "description": "按区域灰度"
        }
    }

    def rollout_progression(self):
        """灰度进度"""
        return [
            {"stage": 1, "percentage": 5, "duration": "1h"},
            {"stage": 2, "percentage": 20, "duration": "2h"},
            {"stage": 3, "percentage": 50, "duration": "4h"},
            {"stage": 4, "percentage": 100, "duration": "1h"}
        ]
```

### 回滚策略

#### 回滚决策矩阵

```yaml
rollback_decision:
  # 必须回滚
  must_rollback:
    - "核心功能完全不可用"
    - "数据丢失或损坏"
    - "安全漏洞被利用"
    - "P0 缺陷未在发布前发现"

  # 应该回滚
  should_rollback:
    - "主要功能异常影响 > 10% 用户"
    - "性能下降 > 50%"
    - "错误率 > 5%"

  # 可以回滚
  may_rollback:
    - "非核心功能异常"
    - "用户体验问题"
    - "次要 bug"

  # 不建议回滚
  not_recommended:
    - "新功能采用率低"
    - "非关键性能指标下降"
    - "单一用户问题"
```

#### 回滚执行时间

```python
rollback_time_breakdown = {
    "detection": "1-2 min",      # 问题发现
    "decision": "5-10 min",       # 决策确认
    "preparation": "2-5 min",     # 准备回滚
    "execution": {
        "simple_app": "5-10 min",
        "cluster_app": "10-15 min",
        "database_change": "15-30 min"
    },
    "verification": "5-10 min",   # 验证确认
    "total": {
        "best_case": "15 min",
        "worst_case": "60 min"
    }
}
```

### 发布风险评估

#### 风险矩阵

```yaml
risk_assessment:
  dimensions:
    - name: "技术风险"
      factors:
        - "代码复杂度"
        - "依赖复杂度"
        - "架构变更程度"

    - name: "业务风险"
      factors:
        - "功能重要性"
        - "用户影响范围"
        - "数据变更范围"

    - name: "运营风险"
      factors:
        - "团队经验"
        - "工具成熟度"
        - "监控覆盖度"

  risk_level:
    low:
      score: "1-3"
      action: "正常发布流程"
      monitor: "标准监控"

    medium:
      score: "4-6"
      action: "加强评审"
      monitor: "加强监控"

    high:
      score: "7-9"
      action: "分阶段发布"
      monitor: "实时监控"

    critical:
      score: "10"
      action: "取消或推迟"
      monitor: "专家驻场"
```

### 发布验收标准

#### Go/No-Go Criteria

```yaml
go_criteria:
  must_pass:
    - name: "测试通过率"
      threshold: "≥ 95%"

    - name: "无 P0/P1 未修复 bug"
      threshold: "0"

    - name: "代码评审通过"
      threshold: "100%"

    - name: "安全扫描通过"
      threshold: "无高危漏洞"

    - name: "性能测试达标"
      threshold: "P99 < 200ms"

  should_pass:
    - name: "单元测试覆盖率"
      threshold: "≥ 80%"

    - name: "文档更新完成"
      threshold: "100%"

    - name: "回滚方案已验证"
      threshold: "通过"

no_go_criteria:
  - "存在未解决 P0 bug"
  - "安全漏洞未修复"
  - "核心功能测试失败"
  - "性能测试不达标"
  - "发布评审未通过"
```

## Toolchain

### 发布管理平台

| 平台 | 特点 |
|------|------|
| ArgoCD | GitOps |
| Spinnaker | 多云支持 |
| Jenkins X | 云原生 |
| GitHub Actions | 简单易用 |

### 部署工具

| 工具 | 用途 |
|------|------|
| Helm | Kubernetes 包管理 |
| Kustomize | Kubernetes 配置管理 |
| Ansible | 自动化配置 |
| Terraform | 基础设施部署 |

### 监控工具

| 工具 | 用途 |
|------|------|
| Prometheus | 指标采集 |
| Grafana | 可视化 |
| Jaeger | 链路追踪 |
| ELK | 日志分析 |

## Associated Assets

- **Scenario**: `../../scenarios/prepare-release/SCENARIO.md`
- **Instruction**: `../../instructions/prepare-release.instructions.md`
- **Prompt**: `../../prompts/prepare-release.prompt.md`
- **Agent**: `../../agents/prepare-release.agent.md`


## Core Knowledge

> Essential knowledge domain for prepare-release execution.

### Domain Fundamentals
- **Release Lifecycle Management**: 覆盖从计划、准备、执行、监控到收尾的完整发布生命周期管理体系。每个阶段定义明确的活动、角色和验收标准，确保发布流程标准化、可重复且可控。
- **Go/No-Go 决策框架**: 基于预定义的质量门禁和风险指标做出的发布决策机制。在发布窗口前由相关角色(PM、QA、Ops、安全)共同评审，确认所有验收标准通过方可放行，未通过则推迟或取消发布。
- **语义化版本 (SemVer)**: 采用 `MAJOR.MINOR.PATCH` 格式的版本号规范，分别代表不兼容的API变更、向下兼容的功能新增和向下兼容的问题修复。严格的版本号管理支撑依赖解析、发布策略和变更沟通。

### Key Principles
1. **发布可追溯**: 每一次发布都应当能够追溯到具体的代码提交、构建产物、配置变更和审批记录。完整的可追溯性是问题排查、合规审计和责任界定的基础保障。
2. **回滚优先**: 每个发布计划必须首先制定回滚方案，确认回滚路径有经过验证、执行时间可接受。先想好如何失败，再考虑如何成功——回滚能力决定了发布的安全边界。
3. **渐进式交付**: 通过灰度发布、蓝绿部署或金丝雀发布等策略，将变更逐步推广到用户群体。渐进式交付将爆炸半径最小化，在影响扩大前有机会发现和修正问题。


## Best Practices

> Proven practices for prepare-release excellence.

1. **标准化发布检查清单**: 建立统一的发布检查清单，涵盖代码审查完成度、测试通过率、安全扫描结果、性能基准、文档更新状态、数据库迁移验证和回滚方案确认。清单作为发布的准入条件，由系统强制执行或人工逐项确认，确保无关键步骤遗漏。

2. **灰度发布前置验证**: 正式全量发布前，先向小比例用户群体(如5%-10%)推送新版本，持续监控核心业务指标和系统稳定性指标。在灰度期间收集早期反馈和问题，根据发现的问题决定继续扩大范围、回滚或修复后重新灰度。

3. **发布窗口管理**: 设定明确的发布窗口(如周二至周四上午10:00-16:00)，避开周末、节假日和业务高峰期。窗口管理确保有充足的应急响应时间和团队资源可用。紧急修复需走特批流程，并缩短观察窗口。

## Anti-patterns (反模式)

> 与 Common Pitfalls 同义，执行时合并检查。

## Common Pitfalls

> Frequent mistakes to avoid during prepare-release execution.

### Pitfall 1: 跳过预发验证
**Risk**: 出于进度压力或过度自信，跳过在预发(Staging)环境上的完整验证流程，直接将代码从开发环境发布到生产环境。预发环境是最接近生产的测试阵地，跳过它将暴露大量集成和环境差异问题。
**Prevention**: 在CI/CD管道中设置强制门禁——必须先通过预发环境的冒烟测试、回归测试和性能基线检查，才能获得生产发布权限。预发环境应尽可能与生产环境保持配置一致。
**Impact**: 生产环境出现本可在预发阶段发现的回归缺陷，导致紧急回滚或热修复，影响用户体验和团队声誉。

### Pitfall 2: 忽视配置变更的发布风险
**Risk**: 发布过程中只关注代码变更，而忽视同时发生的配置变更(如数据库连接串调整、功能开关切换、限流阈值修改)。配置变更同样可能引入故障，甚至有更广泛的影响面。
**Prevention**: 将配置变更纳入发布检查清单的必检项；配置变更应经过与代码变更同等的测试流程；建立配置变更差分审查机制，通过自动化工具对比变更前后差异。
**Impact**: 配置错误引发连锁故障(如连接池耗尽、超时参数不当导致雪崩)，排查困难且修复需要额外发布周期。

### Pitfall 3: 发布后不监控
**Risk**: 发布完成后未对关键业务指标和系统指标进行持续监控(至少观察30-60分钟)，错过了早期发现问题的黄金窗口期。很多问题在低流量下不会立即显现，需要时间窗口暴露。
**Prevention**: 建立发布后监控的Standard Operating Procedure(SOP)，明确需要观察的指标清单(错误率、延迟P50/P99、吞吐量、资源利用率)和阈值；设置自动告警，在指标异常时立即通知发布责任人。
**Impact**: 问题在用户大规模体验后才被发现，影响范围扩大；修复成本增加，且需要在更高压力的场景下执行紧急修复。
