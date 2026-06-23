# E2E 交付全流程 AI Harness 资产库

> **合规状态**：🟢 **95.3% A+** | 282 资产全部 A 级 | 8/8 类别 A 级

## 项目简介

E2E Delivery Harness 是一套基于 **Harness Engineering（驾驭工程）** 理念的 AI 工程化资产库。通过 37 个场景 × 5 类资产（Scenario + Agent + Prompt + Instruction + Skill）共 185 个一一映射的核心执行单元，覆盖软件交付全生命周期（需求 → 设计 → 开发 → 测试 → 部署 → 运维 → 治理），提供标准化、可复用、可评估、可自我修复的企业级 AI 工作流。

## 设计理念

本资产库对齐 **Harness Engineering（驾驭工程）** 六层模型（Goal / Strategy / Tooling / Constraint / Feedback / Observability），遵循 **"人类掌舵、Agent 执行"** 的核心原则。详见 [standards/harness-engineering.md](./standards/harness-engineering.md) 与 [AGENTS.md](./AGENTS.md)。

五类执行资产职责分离：

- **Scenario（场景）**：轻量导航层 — 业务目的、思维链 (CoT)、决策点 (DC-*)、错误处理 (EH-*)、KPI 定义
- **Agent（角色代理）**：身份边界 — 角色定义、工作规则、I/O 契约、Handoff YAML、工具声明
- **Prompt（提示词）**：重型执行脚本 — 变量绑定、逐步 CoT、输出验证 (V-*)、Handover 准备
- **Instruction（操作指令）**：操作 Runbook — 领域特定工具列表、环境要求、配置参数、检查清单
- **Skill（技能模块）**：领域知识包 — 方法论、最佳实践、反模式 (Common Pitfalls)、代码示例

## 核心优势

1. **全流程覆盖**：37 个场景覆盖七大阶段（需求/设计/开发/测试/部署/运维/治理），核心 7 场景对齐 Pipeline 阶段
2. **量化质量保障**：7 个 Q-* 质量门禁 + 28 个 MET-* 指标 + 27 个 Evaluation 评估清单 + 1974 项自动合规检查
3. **强制思维链**：7 步标签体系（THINK→ANALYZE→DESIGN→IMPLEMENT→VERIFY→HANDOVER），每步自检验证
4. **可机器读交接**：100% Agent 使用结构化 YAML Handoff，`to_stage` 100% 正确路由
5. **可自我修复**：P0-P4 错误升级机制 + 10 类反模式库（检测方法+修复建议+预防措施）
6. **全库 A 级合规**：282 个资产文件全部达到 A 级标准，零占位符残留

## 资产统计

| 类别 | 数量 | 说明 |
|------|------|------|
| Scenario | 37 | 场景入口定义 |
| Agent | 37 | AI 角色代理 |
| Prompt | 37 | 执行提示词 |
| Instruction | 37 | 操作指令 |
| Skill | 37 | 领域技能 |
| Standard | 44 | 标准规范 |
| Evaluation | 27 | 评估清单 |
| Template | 26 | 交付物模板 |
| Workflow | 2 | Pipeline 编排 |
| Context | 4 | 上下文与交接模板 |
| **总计** | **282** | **合规评分 95.3% A+** |

## 适用场景

- 新项目启动的全流程规划与执行
- 现有项目的单阶段 AI 辅助增强
- 团队协作流程的标准化与沉淀
- 最佳实践、Runbook 和 Agent 技能的持续积累
- 企业级交付质量门禁与合规审计

## 开始使用

1. 阅读 [AGENTS.md](./AGENTS.md) 了解 Agent 执行协议（R1-R5）
2. 阅读 [使用指南](./USAGE.zh.md) 了解资产使用方法
3. 运行 `python3 scripts/harness-compliance-check.py` 确认合规状态
4. 参考 [深度分析报告](./资产库全面评估深度分析报告.md) 了解全库评估详情
5. 根据项目阶段选择对应 [场景](./scenarios/) 开始执行
