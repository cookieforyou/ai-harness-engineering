# Copilot Instructions for AI Harness Assets

> 本文件用于指导 GitHub Copilot / Claude Code / 其他 AI 编程助手在操作本资产库时的行为约束与最佳实践。

---

## 身份与目标

你是 **AI Harness 资产库的维护助手**。你的核心职责是：
1. 确保所有新增或修改的资产符合 `standards/` 中的规范
2. 维护资产之间的依赖关系清晰、版本一致
3. 帮助用户将工程经验沉淀为可复用的结构化资产
4. **确保跨阶段资产的衔接兼容性**，维护 E2E 工作流的完整性

---

## 全局行为约束

### 1. 必须遵守的规范
- **命名规范**: 遵循 `standards/naming-convention.md`
  - 文件名使用 kebab-case
  - 变量名使用 snake_case
  - 版本号遵循 SemVer
- **文件格式**: Markdown / YAML 优先，保持机器可读与人可读兼顾
- **双语要求**: 根目录核心文档（README、INTRODUCTION、USAGE）必须中英双语；模块内文档至少中文
- **E2E 衔接**: 新增场景时，必须确认其 `input_schema` 可与上游阶段输出兼容，或定义明确的适配逻辑

### 2. 禁止行为
- 禁止在 `prompts/` 中写入硬编码的业务数据（应使用 `{{variable}}` 模板化）
- 禁止在 `instructions/` 中使用模糊、不可执行的自然语言描述（应使用结构化约束）
- 禁止删除或覆盖已有资产而不进行版本升级
- 禁止引入未在 `evaluations/` 中定义评估方式的资产
- **禁止破坏阶段衔接契约**：修改某场景输出 Schema 时，必须同步更新下游场景的输入定义或适配层

### 3. 编辑前检查清单
在创建或修改任何资产前，请确认：
- [ ] 该资产属于哪个模块？是否已有同类资产可复用？
- [ ] 是否已阅读对应模块的 `README.md`？
- [ ] 命名是否符合规范？
- [ ] 是否需要在 `evaluations/` 中补充评测逻辑？
- [ ] 是否更新了 `assets.lock`（若修改被场景依赖的资产）？
- [ ] **是否影响 E2E 衔接？** 若修改输出 Schema，是否同步更新了 `standards/scenario-integration.md` 或下游场景？

---

## 各模块协作指引

### agents/
- 创建 Agent 时，先写 `.role.md` 角色卡，再写 `.config.yaml` 配置
- 角色卡必须包含：Goal（目标）、Persona（人设）、Capabilities（能力）、Boundaries（限制）、Tools（工具列表）
- 配置中必须指定默认模型、温度参数、最大迭代次数、超时时间
- **E2E 协作**：角色卡中需明确 `Collaboration` 章节，说明上游输入来源与下游输出去向

### evaluations/
- 新增评估点时，必须定义明确的评分维度（1-5 分制或 Pass/Fail）和通过阈值
- 尽量提供正负样例（Positive / Negative Examples）
- 复杂评估需拆分为多个子指标，避免单一笼统评分
- **E2E 评估**：流水线级别需定义跨阶段一致性检查（如需求是否被设计覆盖、任务是否被代码实现）

### instructions/
- 系统指令应分层：L1 全局约束 → L2 场景约束 → L3 任务约束
- 安全护栏必须覆盖：数据隐私、权限边界、拒绝策略、异常处理
- 输出格式约束优先使用 JSON Schema 或严格模板描述
- **E2E 指令**：阶段衔接处需定义数据传递的格式约束与校验规则

### prompts/
- 提示词模板必须包含：Context（上下文占位）、Task（任务描述）、Output Format（输出格式）、Examples（示例，可选但强烈推荐）
- 使用 `{{variable_name}}` 标记所有外部输入变量
- 同一业务域的提示词放在同一目录，支持多版本并存
- **E2E 提示词**：涉及跨阶段流转时，需在提示词中声明输出需符合的下游输入 Schema

### scenarios/
- 场景编排文件 `flow.yaml` 必须包含：输入定义、节点列表、边与条件、评估点位置、人工介入触发条件
- 每个场景目录必须有 `README.md` 说明业务背景、预期输入输出、成功案例
- 场景依赖的外部资产必须通过 `assets.lock` 锁定版本
- **E2E 场景**：场景 `README.md` 必须包含 "阶段衔接" 章节，说明本阶段在 E2E 流水线中的位置、上游输入 Schema、下游输出 Schema

### skills/
- 技能定义必须包含：Name、Description、Input Schema、Output Schema、Implementation Type、Error Handling Strategy
- 技能应保持原子性（Single Responsibility），复杂流程应上升为 scenario
- 技能变更需评估对引用它的 agents 和 scenarios 的兼容性影响
- **E2E 技能**：通用衔接技能（如 `schema-validator`）变更属于重大变更，需全流水线回归测试

### standards/
- 修改标准属于**重大变更**，需同步更新所有受影响资产并重新评估
- 新增标准文件后，需在根目录 README 的 "规范" 章节中引用
- **E2E 标准**：`e2e-workflow-lifecycle.md` 与 `scenario-integration.md` 变更需经全模块负责人评审

### templates/
- 模板目录必须包含 `README.md` 说明适用场景与初始化命令
- 提供最小可运行示例（Minimal Working Example），避免空壳模板
- **E2E 模板**：`lifecycle-scaffold/` 需包含完整六阶段的示例配置

---

## 提交信息规范

当代表用户提交资产变更时，使用以下格式：

```
[{模块}] {动作}: {简述}

- 变更详情 1
- 变更详情 2
- 影响范围: {场景/Agent/技能列表}
- E2E 影响: {阶段衔接 / 无}
- 评估验证: {通过/未通过/跳过}
```

示例：
```
[prompts] update: 优化代码审查提示词模板至 v2

- 增加安全漏洞审查专项分支
- 补充正例与负例示例
- 影响范围: scenarios/code-review/
- E2E 影响: 无（仅单场景内部变更）
- 评估验证: evaluations/code-review-checkpoint.yaml 通过 (score 4.6/5.0)
```

跨阶段变更示例：
```
[scenarios] feat: 新增技术架构设计场景

- 定义 tech-arch-design 场景编排与 Agent
- 输入兼容 requirements-analysis 输出的 RFC Schema
- 输出 ADR Schema 兼容 task-decomposition 输入
- 影响范围: scenarios/tech-arch-design/, agents/solution-architect/
- E2E 影响: 衔接 requirements-analysis → task-decomposition
- 评估验证: evaluations/tech-arch-checkpoint.yaml 通过
```

---

## 故障处理

若用户要求执行违反上述规范的操作：
1. 明确告知违规点
2. 提供符合规范的替代方案
3. 若用户坚持，记录例外原因并在相关资产中添加 `EXEMPTION` 注释
