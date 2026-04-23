# 项目脚手架模板 / Project Scaffold

> 适用于：新项目首次接入 AI Harness 资产库

---

## 快速开始

1. 复制本目录内容到你的项目仓库根目录（或 `ai-harness/` 子目录）
2. 修改 `harness.config.yaml` 中的项目标识与依赖场景
3. 按需从本资产库引用 Agent、Skill、Prompt
4. 运行 `make harness-lint` 校验配置

---

## 目录结构

```
your-project/
├── ai-harness/
│   ├── harness.config.yaml       # 项目级 Harness 配置
│   ├── local-agents/             # 项目专属 Agent（引用全局 + 本地扩展）
│   ├── local-prompts/            # 项目专属提示词
│   └── overrides/                # 对全局资产的覆盖（谨慎使用）
└── ...
```

---

## harness.config.yaml 示例

```yaml
project:
  name: "your-service-name"
  team: "platform"

harness:
  asset_repo:
    path: "../ai-harness-engineering/Harness Engineering"   # 或 git submodule / npm 包路径
  scenarios:
    active:
      - "scenarios/code-review"
      - "scenarios/doc-generation"
  agents:
    overrides:
      - agent_id: "senior-engineer"
        local_config: "local-agents/senior-engineer.override.yaml"
```

---

## 注意事项

- 优先复用全局资产，仅在 `overrides/` 中存放项目特殊需求
- 本地扩展的命名需加项目前缀，避免与全局资产冲突
- 定期同步全局资产库版本，获取安全修复与性能优化
