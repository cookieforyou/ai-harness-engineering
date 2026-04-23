# agents / Agent 定义

本目录用于沉淀所有 AI Agent 的角色定义与运行配置。Agent 是 Harness 系统中执行任务的"驾驶员"，其角色卡决定了行为模式与能力边界。

---

## 文件组织

```
agents/
├── README.md
├── senior-engineer.role.md
├── senior-engineer.config.yaml
├── product-manager.role.md
├── product-manager.config.yaml
└── ...
```

---

## 角色卡规范 (`.role.md`)

每个角色卡必须包含以下区块：

```markdown
# {Role Name} / {角色名}

## Goal / 目标
{用一句话描述该 Agent 的核心使命}

## Persona / 人设
{性格特征、沟通风格、专业背景}

## Capabilities / 能力
- [ ] 能力 1
- [ ] 能力 2

## Boundaries / 限制
- 禁止事项 1
- 禁止事项 2

## Tools / 工具集
- `{skill-name}` — 用途说明

## Collaboration / 协作
- 上游输入: {通常接收什么输入}
- 下游输出: {通常产生什么输出}
- 人工介入触发条件: {何时必须让人类接管}
```

---

## 配置规范 (`.config.yaml`)

```yaml
agent_id: "senior-engineer"
version: "1.0.0"
model:
  provider: "openai"
  name: "gpt-4o"
  temperature: 0.2
  max_tokens: 4096
runtime:
  max_iterations: 10
  timeout_seconds: 300
  retry_policy:
    max_retries: 3
    backoff: "exponential"
tools:
  - "skills/static-analysis.yaml"
  - "skills/security-audit.yaml"
observability:
  log_level: "INFO"
  trace_enabled: true
```

---

## 现有 Agent 清单

| Agent | 职责 | 状态 |
| :--- | :--- | :--- |
| `senior-engineer` | 代码审查、架构评审、技术方案评估 | 规划中 |
| `product-manager` | 需求分析、PRD 撰写、优先级排序 | 规划中 |

---

## 新增 Agent 流程

1. 复制 `templates/agent-template/` 到本目录
2. 填写角色卡与配置
3. 在对应 `scenarios/` 中注册引用
4. 补充 `evaluations/` 中针对该 Agent 的专项评估集
5. 提交前自检：是否定义了清晰的人工介入触发条件？
