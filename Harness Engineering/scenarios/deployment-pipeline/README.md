# 部署迭代场景 / Deployment Pipeline Scenario

> **阶段**: P5 — 部署迭代
> **核心 Agent**: `agents/devops-engineer`
> **目标输出**: 部署规范（CI/CD 配置、部署清单、回滚策略、密钥管理）
> **效力等级**: P0（强制）

---

## 场景概述

本场景基于 P4 阶段（开发实现）完成并通过代码审查的代码，设计安全、可观测、可回滚的部署流水线。输出物包含 CI/CD 配置、部署清单（K8s/Docker Compose/Terraform）、部署策略、回滚方案及密钥管理策略，确保服务安全上线。

---

## 输入规范

| 字段 | 类型 | 必填 | 说明 |
| :--- | :--- | :--- | :--- |
| `service_name` | `string` | 是 | 服务名称 |
| `tech_stack` | `string` | 是 | 技术栈（框架、运行时、部署平台） |
| `environment` | `string` | 是 | 目标环境：`development` / `staging` / `production` |
| `version` | `string` | 是 | 部署版本号 |
| `previous_deployment` | `object` | 否 | 上一版本部署信息（用于蓝绿/金丝雀策略） |
| `compliance_requirements` | `string` | 否 | 合规要求 |

---

## 输出规范

主输出为 JSON 格式，Schema 定义如下：

```json
{
  "deployment_spec": {
    "service_name": "...",
    "version": "...",
    "environment": "...",
    "strategy": "rolling|blue-green|canary",
    "pipeline_config": {
      "format": "github-actions|gitlab-ci|argo-cd",
      "content": "YAML 字符串"
    },
    "manifest": {
      "format": "kubernetes|docker-compose|terraform",
      "content": "YAML 字符串"
    },
    "rollback_plan": {
      "strategy": "...",
      "trigger_conditions": ["..."],
      "steps": ["..."],
      "estimated_rollback_time_seconds": 60
    },
    "secrets_management": {
      "tool": "vault|aws-secrets-manager|kubernetes-secrets",
      "notes": ["..."]
    },
    "health_checks": {
      "readiness": "/health/ready",
      "liveness": "/health/live",
      "startup": "/health/startup"
    },
    "compliance_notes": ["..."]
  }
}
```

---

## 角色职责

| 角色 | 职责 | 输出物 |
| :--- | :--- | :--- |
| **DevOps Engineer** | CI/CD 流水线设计、部署清单生成、回滚策略制定、密钥管理 | 部署规范 JSON |
| **人类 SRE / DevOps 负责人** | 审阅生产环境部署策略、确认回滚方案可执行性、批准上线 | 已批准的上线计划 |

---

## 质量检查要点

- [ ] 生产环境部署包含至少两种验证阶段（如 staging + canary）
- [ ] 所有涉及密钥的配置使用 Secret 引用，禁止硬编码
- [ ] 回滚方案可在 5 分钟内完成核心服务恢复
- [ ] 流水线包含安全扫描步骤（镜像扫描、依赖漏洞扫描）
- [ ] 金丝雀发布定义明确的流量切换指标（错误率、延迟、自定义业务指标）
- [ ] 输出通过 `evaluations/deployment-checkpoint.yaml` 质量门禁

---

## 上游衔接

接收 `scenarios/code-review/` 的通过结果（代码已审查并合并）。
衔接规范详见 `standards/scenario-integration.md#P4→P5`。

## 下游衔接

本场景输出直接作为 `scenarios/health-monitoring/` 的输入（部署清单中的健康检查端点与 SLO）。
衔接规范详见 `standards/scenario-integration.md#P5→P6`。
