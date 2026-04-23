# 使用指南

## 1. 资产引用路径规范

所有资产统一以本库根目录为基准进行引用：

```yaml
# 场景编排示例 (scenarios/code-review/flow.yaml)
agent:
  role: "agents/senior-engineer.role.md"
  instructions:
    system: "instructions/system/code-review-system.md"
    safety: "instructions/safety/data-privacy.md"
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

## 2. 工作流：从需求到交付的 E2E 指南

### Step 1: 场景识别（按交付阶段）

根据当前所处交付阶段，在 `scenarios/` 中匹配对应场景：

| 当前阶段 | 选用场景 | 核心输入 | 核心输出 |
| :--- | :--- | :--- | :--- |
| 需求澄清 | `scenarios/requirements-analysis/` | PRD、用户访谈、竞品分析 | 用户故事、RFC、验收标准 |
| 技术设计 | `scenarios/tech-arch-design/` | RFC、约束条件（预算、合规） | 架构文档 ADR、技术选型、接口契约 |
| 迭代规划 | `scenarios/task-decomposition/` | ADR、资源约束 | 任务清单、依赖图、工时估算 |
| 代码审查 | `scenarios/code-review/` | PR Diff、上下文 | 审查报告、修复建议 |
| 发布部署 | `scenarios/deployment-pipeline/` | 构建产物、环境配置 | CI/CD 配置、部署脚本、回滚方案 |
| 运维监控 | `scenarios/health-monitoring/` | 服务清单、SLO 定义 | 监控规则、告警策略、健康报告 |

- 若存在匹配场景 → 直接复用并做变量替换
- 若不存在 → 参考 `templates/scenario-skeleton/` 新建
- 若需全生命周期初始化 → 参考 `templates/lifecycle-scaffold/`

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

**跨阶段衔接时**，需额外校验：
- [ ] 上游输出 Schema 与当前场景 `input_schema` 兼容
- [ ] 使用 `skills/schema-validator.yaml` 执行衔接校验
- [ ] 若不兼容，触发 `standards/scenario-integration.md` 中的降级策略

### Step 3: 运行与评估

1. 使用编排引擎（如 LangChain / AutoGen / 自研 Harness Runner）加载场景
2. Agent 按策略层规划执行
3. 每个 Checkpoint 触发 `evaluations/` 中的评测逻辑
4. **跨阶段流转时**：当前阶段输出需通过衔接校验，方可作为下一阶段输入
5. 未通过门禁则触发重试或人工介入

### Step 4: 结果沉淀

- 运行日志与轨迹存入观测系统
- 成功的新组合固化回资产库（遵循 `standards/versioning.md`）
- 失败案例补充至 `evaluations/` 作为负例
- **跨阶段资产**：若某阶段输出被下游复用，需更新 `standards/schemas/` 中的衔接定义

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
├── README.md           # 场景说明、输入输出定义、阶段衔接说明
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
- `e2e-workflow-lifecycle.md` — E2E 全生命周期规范
- `scenario-integration.md` — 场景集成与衔接规范

### templates/
存放项目模板。按需选用：
- `project-scaffold/` — 新项目 AI Harness 初始化模板
- `scenario-skeleton/` — 新建场景的最小结构模板
- `agent-template/` — 新建 Agent 的最小结构模板
- `lifecycle-scaffold/` — 全生命周期项目脚手架

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

**跨阶段版本锁定**：
当多个场景组成 E2E 流水线时，需在流水线级别维护 `pipeline.lock`，锁定各场景版本组合：

```yaml
# pipeline.lock 示例
pipeline_id: "e2e-delivery-v1"
scenarios:
  - scenario: "scenarios/requirements-analysis"
    version: "1.0.0"
  - scenario: "scenarios/tech-arch-design"
    version: "1.0.0"
  - scenario: "scenarios/task-decomposition"
    version: "1.0.0"
  - scenario: "scenarios/code-review"
    version: "1.0.0"
  - scenario: "scenarios/deployment-pipeline"
    version: "1.0.0"
  - scenario: "scenarios/health-monitoring"
    version: "1.0.0"
```

---

## 5. 本地验证命令（推荐）

```bash
# 校验资产命名规范
python scripts/lint-assets.py

# 运行单个评估集
python scripts/run-eval.py --checkpoint evaluations/code-review-checkpoint.yaml

# 生成场景依赖图谱
python scripts/graph-scenario.py --scenario scenarios/code-review/

# 校验阶段衔接 Schema 兼容性
python scripts/validate-integration.py --from scenarios/requirements-analysis/ --to scenarios/tech-arch-design/

# 运行 E2E 流水线验证
python scripts/run-pipeline.py --pipeline pipeline.lock
```

> 注：`scripts/` 目录可根据需要在本库外独立维护。
