# Skill: 发布准备 (Release Preparation)

## 概述

本 Skill 定义了发布准备的核心知识体系。

## 核心知识

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

## 工具链

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

## 关联资产

- **Scenario**: `../../scenarios/prepare-release/SCENARIO.md`
- **Instruction**: `../../instructions/prepare-release.instructions.md`
- **Prompt**: `../../prompts/prepare-release.prompt.md`
- **Agent**: `../../agents/release-manager.agent.md`


## Core Knowledge

> Essential knowledge domain for prepare-release execution.

### Domain Fundamentals
- [Core concept 1]
- [Core concept 2]
- [Core concept 3]

### Key Principles
1. [Principle 1]
2. [Principle 2]
3. [Principle 3]


## Best Practices

> Proven practices for prepare-release excellence.

1. **Practice 1**: [Description and rationale]
2. **Practice 2**: [Description and rationale]
3. **Practice 3**: [Description and rationale]


## Common Pitfalls

> Frequent mistakes to avoid during prepare-release execution.

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
