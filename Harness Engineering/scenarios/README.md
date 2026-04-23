# scenarios / 场景编排

本目录定义端到端（E2E）AI 工作流场景。每个场景是一次完整的交付单元，覆盖从输入接收到最终产出的全生命周期。

---

## 设计理念

> **场景即交付**: 场景不是单个 Prompt，而是多个 Agent、Skill、评估点的编排结果。

- **声明式编排**: 通过 `flow.yaml` 描述"做什么"，而非"怎么做"
- **可观测**: 每个节点都有明确的输入输出契约与日志规范
- **人机协作**: 明确定义人工介入点（Human-in-the-loop），避免全自动带来的风险
- **版本锁定**: 场景依赖的资产通过 `assets.lock` 精确锁定，确保可复现

---

## 文件组织

```
scenarios/
├── README.md
├── requirements-analysis/          # P1 需求分析
│   ├── README.md
│   ├── flow.yaml
│   └── assets.lock
├── tech-arch-design/               # P2 技术架构
│   ├── README.md
│   ├── flow.yaml
│   └── assets.lock
├── task-decomposition/             # P3 任务拆分
│   ├── README.md
│   ├── flow.yaml
│   └── assets.lock
├── code-review/                    # P4 代码审查
│   ├── README.md
│   ├── flow.yaml
│   ├── assets.lock
│   └── checkpoint.yaml
├── deployment-pipeline/            # P5 部署迭代
│   ├── README.md
│   ├── flow.yaml
│   └── assets.lock
├── health-monitoring/              # P6 健康监控
│   ├── README.md
│   ├── flow.yaml
│   └── assets.lock
└── ...
```

---

## 场景目录规范

每个场景目录必须包含：

| 文件 | 说明 |
| :--- | :--- |
| `README.md` | 场景业务说明、预期输入输出、成功标准 |
| `flow.yaml` | 编排定义：节点、边、条件分支、并行策略 |
| `checkpoint.yaml` | 本场景专用的评估点配置（可选，可引用全局） |
| `assets.lock` | 依赖资产版本锁定文件 |

---

## flow.yaml 规范

```yaml
scenario_id: "code-review"
version: "1.0.0"
description: "自动化代码审查与报告生成"

input_schema:
  type: "object"
  required: ["pr_id", "diff"]
  properties:
    pr_id: { type: "string" }
    diff: { type: "string" }
    context: { type: "string" }

nodes:
  - id: "parse-diff"
    type: "skill"
    skill_ref: "skills/diff-parser.yaml"
    input: "{{input.diff}}"
    output: "parsed_files"

  - id: "security-scan"
    type: "agent"
    agent_ref: "agents/security-auditor"
    input:
      files: "{{nodes.parse-diff.output.parsed_files}}"
    output: "security_findings"

  - id: "code-review"
    type: "agent"
    agent_ref: "agents/senior-engineer"
    input:
      pr_title: "{{input.pr_id}}"
      diff: "{{input.diff}}"
      context: "{{input.context}}"
    output: "review_report"

  - id: "merge-report"
    type: "skill"
    skill_ref: "skills/report-merger.yaml"
    input:
      security: "{{nodes.security-scan.output.security_findings}}"
      review: "{{nodes.code-review.output.review_report}}"
    output: "final_report"

  - id: "quality-gate"
    type: "checkpoint"
    checkpoint_ref: "evaluations/code-review-checkpoint.yaml"
    input: "{{nodes.merge-report.output.final_report}}"
    branches:
      pass:
        next: "notify-success"
      fail:
        next: "human-escalation"

  - id: "human-escalation"
    type: "human"
    action: "pause_and_notify"
    notification:
      channel: "slack"
      message: "代码审查质量门禁未通过，需人工复核"

  - id: "notify-success"
    type: "skill"
    skill_ref: "skills/notification.yaml"
    input:
      report: "{{nodes.merge-report.output.final_report}}"

edges:
  - from: "start"
    to: "parse-diff"
  - from: "parse-diff"
    to: "security-scan"
  - from: "parse-diff"
    to: "code-review"
  - from: "security-scan"
    to: "merge-report"
  - from: "code-review"
    to: "merge-report"
  - from: "merge-report"
    to: "quality-gate"
```

---

## 新增场景流程

1. 复制 `templates/scenario-skeleton/` 到新目录
2. 编写 `README.md` 明确业务价值与成功标准
3. 设计 `flow.yaml`，遵循节点单一职责原则
4. 识别所有依赖资产（agents/skills/prompts/instructions/evaluations）
5. 生成 `assets.lock` 锁定版本
6. 在 `evaluations/` 中注册至少一个质量门禁
7. 进行端到端试运行并记录轨迹日志
