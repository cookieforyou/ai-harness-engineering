# 使用指南

## 1. 资产引用路径规范

所有资产统一以本库根目录为基准进行引用：

```yaml
# 场景编排示例 (scenarios/code-review.yaml)
agent:
  role: "agents/senior-engineer.role.md"
  instructions:
    system: "instructions/code-review-system.md"
    safety: "instructions/safety-guardrails.md"
  skills:
    - "skills/static-analysis.yaml"
    - "skills/security-audit.yaml"
  prompts:
    main: "prompts/code-review/v1.md"
    report: "prompts/code-review/report-template.md"
  evaluation:
    checkpoint: "evaluations/code-review-checkpoint.yaml"
```

---

## 2. 工作流：从需求到交付

### Step 1: 场景识别
根据业务需求，在 `scenarios/` 中匹配或新建场景：
- 若存在匹配场景 → 直接复用并做变量替换
- 若不存在 → 参考 `templates/scenario-skeleton/` 新建

### Step 2: 资产组装
按场景声明，从各模块提取对应资产：
```
Scenario ( orchestration )
  ├── Agent (role + goal)
  ├── Instructions (system + constraints)
  ├── Skills (tool calling + atomic capabilities)
  ├── Prompts (context + task definition)
  └── Evaluation (quality gate + feedback)
```

### Step 3: 运行与评估
1. 使用编排引擎（如 LangChain / AutoGen / 自研 Harness Runner）加载场景
2. Agent 按策略层规划执行
3. 每个 Checkpoint 触发 `evaluations/` 中的评测逻辑
4. 未通过门禁则触发重试或人工介入

### Step 4: 结果沉淀
- 运行日志与轨迹存入观测系统
- 成功的新组合固化回资产库（遵循 `standards/versioning.md`）
- 失败案例补充至 `evaluations/` 作为负例

---

## 3. 目录级使用说明

### agents/
存放角色定义。每个 Agent 至少包含：
- `{agent-name}.role.md` — 角色卡（目标、性格、能力、限制）
- `{agent-name}.config.yaml` — 运行配置（模型参数、工具绑定、超时策略）

### evaluations/
存放评估定义。每个评估点包含：
- `{checkpoint-name}.yaml` — 评估指标、评分维度、通过阈值
- `{checkpoint-name}-dataset.jsonl` — 评测数据集（可选）

### instructions/
存放指令文件。按作用域分类：
- `system/` — 系统级行为约束
- `safety/` — 安全护栏与合规要求
- `format/` — 输出格式强制规范

### prompts/
存放提示词模板。组织方式：
- 按业务域分目录，如 `prompts/code-review/`、`prompts/doc-gen/`
- 每个目录下支持版本管理：`v1.md`、`v2.md`
- 模板变量使用 `{{variable_name}}` 双大括号标记

### scenarios/
存放场景编排。每个场景为一个独立目录：
```
scenarios/{scenario-name}/
├── README.md           # 场景说明、输入输出定义
├── flow.yaml           # 编排定义（节点、边、条件分支）
├── checkpoint.yaml     # 评估点配置
└── assets.lock         # 依赖资产版本锁定
```

### skills/
存放技能模块。每个技能至少包含：
- `{skill-name}.yaml` — 技能描述、输入输出 Schema、实现方式（LLM / Tool / Code）
- `{skill-name}/` — 若技能复杂，可展开为子目录

### standards/
存放规范文档。必读：
- `naming-convention.md` — 命名规范
- `versioning.md` — 版本管理策略
- `quality-checklist.md` — 资产入库检查清单

### templates/
存放项目模板。按需选用：
- `project-scaffold/` — 新项目 AI Harness 初始化模板
- `scenario-skeleton/` — 新建场景的最小结构模板
- `agent-template/` — 新建 Agent 的最小结构模板

---

## 4. 版本锁定与兼容性

场景通过 `assets.lock` 锁定依赖资产版本：

```yaml
# assets.lock 示例
lock_version: "1.0"
dependencies:
  - asset: "prompts/code-review/v1.md"
    checksum: "sha256:abc123..."
  - asset: "skills/static-analysis.yaml"
    version: "^2.1.0"
```

升级依赖时需重新运行评估集验证兼容性。

---

## 5. 本地验证命令（推荐）

```bash
# 校验资产命名规范
python scripts/lint-assets.py

# 运行单个评估集
python scripts/run-eval.py --checkpoint evaluations/code-review-checkpoint.yaml

# 生成场景依赖图谱
python scripts/graph-scenario.py --scenario scenarios/code-review/
```

> 注：`scripts/` 目录可根据需要在本库外独立维护。
