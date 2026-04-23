# E2E 交付全流程操作手册 / Delivery Playbook

> **效力等级**: P1（重要）
> **适用范围**: 使用 AI Harness 资产库进行端到端软件交付的全部项目
> **目标读者**: 技术负责人、项目经理、AI 资产管理员

---

## 1. 流程总览

AI Harness E2E 交付流程覆盖软件交付的六个核心阶段，构成单向流转、支持回退、闭环反馈的完整工作流：

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  P1 需求分析  │ ──→ │  P2 技术架构  │ ──→ │  P3 任务拆分  │
│  (RFC)       │     │  (ADR)       │     │  (执行计划)   │
└──────────────┘     └──────────────┘     └──────────────┘
       ↑                                          │
       │     ┌──────────────┐     ┌──────────────┐│
       └──── │  P6 健康监控  │ ←── │  P5 部署迭代  │←┘
             │  (反馈闭环)   │     │  (上线)       │
             └──────────────┘     └──────────────┘
                    ↑
             ┌──────────────┐
             │  P4 开发实现  │
             │  (代码审查)   │
             └──────────────┘
```

---

## 2. 执行前准备

### 2.1 环境检查清单

- [ ] 已阅读 `standards/e2e-workflow-lifecycle.md` 了解阶段定义与流转规则
- [ ] 已阅读 `standards/scenario-integration.md` 了解阶段间数据契约
- [ ] 已确认 `agents/` 中涉及的角色已配置有效的模型 API Key
- [ ] 已确认 `skills/` 中引用的外部服务（如通知渠道、归档存储）已就绪
- [ ] 已根据项目特点调整 `evaluations/` 中的质量门禁阈值（如需）

### 2.2 项目初始化

1. 复制 `templates/project-scaffold/` 至项目工作区
2. 填写项目基本信息（名称、团队规模、技术约束）
3. 在 `pipeline.lock` 中锁定本项目的场景版本组合（参考 `standards/e2e-workflow-lifecycle.md` 第 5 节）
4. 运行自检命令（如适用）：验证所有依赖资产版本一致且 `assets.lock` checksum 有效

---

## 3. 分阶段执行指南

### 3.1 P1 — 需求分析

**触发条件**: 收到原始需求（PRD、会议纪要、用户反馈）

**执行步骤**:
1. 准备输入：整理 `raw_requirements`、`source_type`、`project_context`、`focus_areas`
2. 调用场景：`scenarios/requirements-analysis/flow.yaml`
3. 等待 `quality-gate` 结果：
   - **通过** → 获取 `final_rfc`，进入 P2
   - **有条件通过** → 人工澄清 `open_questions`，确认后进入 P2
   - **失败** → 人工复核需求质量，决定重试或终止

**质量检查要点**:
- 所有 `must_have` 需求均有 Given-When-Then 验收标准
- `open_questions` 为空或已人工确认
- RFC JSON 通过 Schema 校验

**常见陷阱**:
- ❌ 原始需求过长（>5000 字）未分段处理 → ✅ 先拆分再合并
- ❌ 臆测补全模糊需求 → ✅ 必须放入 `open_questions`

---

### 3.2 P2 — 技术架构设计

**触发条件**: P1 输出 `final_rfc` 已通过质量门禁

**执行步骤**:
1. 准备输入：传递 `rfc_doc`，补充 `constraints`、`existing_system`、`focus_areas`
2. 调用场景：`scenarios/tech-arch-design/flow.yaml`
3. 等待 `quality-gate` 结果：
   - **通过** → 获取 `final_adr`，进入 P3
   - **有条件通过** → 人工审阅风险项，确认后进入 P3
   - **失败** → 人工复核架构方案，决定重试或回退至 P1 补充需求

**质量检查要点**:
- 技术选型有明确理由与风险等级
- 接口契约包含错误码与边界情况
- ADR 数量 >= 3，覆盖关键决策

**常见陷阱**:
- ❌ 推荐团队不熟悉的激进技术 → ✅ 遵循 `constraints` 中团队技能约束
- ❌ 忽略存量系统兼容性 → ✅ 必须包含迁移路径

---

### 3.3 P3 — 任务拆分

**触发条件**: P2 输出 `final_adr` 已通过质量门禁

**执行步骤**:
1. 准备输入：传递 `adr_doc`，补充 `team_capacity`、`iteration_constraints`、`risk_appetite`
2. 调用场景：`scenarios/task-decomposition/flow.yaml`
3. 等待 `quality-gate` 结果：
   - **通过** → 获取 `final_plan`，进入 P4
   - **有条件通过** → 人工审阅资源分配与里程碑，确认后进入 P4
   - **失败** → 人工复核拆分合理性，决定重试或回退至 P2 调整架构

**质量检查要点**:
- 单任务工时 <= 3 天
- 依赖关系无环（DAG）
- 关键路径任务分配经验丰富人员

**常见陷阱**:
- ❌ 任务粒度过大（>5 天） → ✅ 进一步拆分
- ❌ 忽略外部依赖的提前启动时间 → ✅ 外部依赖需提前至少一个迭代

---

### 3.4 P4 — 开发实现

**触发条件**: P3 输出 `final_plan` 已通过质量门禁，开发人员完成代码编写并提交 PR

**执行步骤**:
1. 准备输入：PR 标题、描述、Diff、项目上下文
2. 调用场景：`scenarios/code-review/flow.yaml`
3. 等待 `quality-gate` 结果：
   - **通过** → 代码可合并，进入 P5
   - **有条件通过** → 处理中低风险建议后合并，进入 P5
   - **失败** → 修复代码后重试，或回退至 P2 调整架构（若发现架构风险）

**质量检查要点**:
- 无 Critical/High 级别安全漏洞
- 审查建议具体、可执行
- Diff 范围与 P3 任务清单对应

**常见陷阱**:
- ❌ 审查大 Diff（>500 行）未拆分 → ✅ 先由 `diff-parser` 预拆分
- ❌ 忽略架构风险类 finding → ✅ 此类问题应触发回退至 P2

---

### 3.5 P5 — 部署迭代

**触发条件**: P4 代码已合并，准备发布新版本

**执行步骤**:
1. 准备输入：`service_name`、`tech_stack`、`environment`、`version`、`previous_deployment`、`compliance_requirements`
2. 调用场景：`scenarios/deployment-pipeline/flow.yaml`
3. 等待 `quality-gate` 结果：
   - **通过** → 执行部署，进入 P6
   - **有条件通过** → 人工审阅后执行部署（限非生产环境），进入 P6
   - **失败** → 修复部署配置后重试，或回退至 P4 修复代码

**质量检查要点**:
- 生产环境至少两种验证阶段（staging + canary）
- 密钥无硬编码
- 回滚时间 <= 5 分钟

**常见陷阱**:
- ❌ 直接全量发布至生产环境 → ✅ 必须 staging 验证
- ❌ 回滚方案未实际演练 → ✅ 定期演练回滚流程

---

### 3.6 P6 — 健康监控

**触发条件**: P5 部署完成，服务已上线运行

**执行步骤**:
1. 准备输入：`service_name`、`tech_stack`、`slo`、`alert_channels`、`existing_monitoring`
2. 调用场景：`scenarios/health-monitoring/flow.yaml`
3. 等待 `quality-gate` 结果：
   - **通过** → 监控方案生效，生成 `feedback_package` 供 P1 使用
   - **有条件通过** → 人工调优告警阈值后生效
   - **失败** → 修复监控配置后重试

**质量检查要点**:
- 告警有 `for` 持续时间，避免误报
- Critical 告警有明确升级路径
- 仪表盘遵循「5 秒原则」

**反馈闭环操作**:
1. 定期（建议每周/每迭代）导出监控数据
2. 将性能瓶颈、错误模式、用户行为数据打包为 `feedback-package`
3. 作为 `project_context` 补充输入至 P1，启动下一轮需求分析

---

## 4. 异常处理与回退策略

### 4.1 阶段内失败

| 阶段 | 失败场景 | 处理策略 |
| :--- | :--- | :--- |
| P1 | 需求无法结构化 | 人工介入补充上下文，重试 |
| P2 | 技术选型与约束冲突 | 回退至 P1 放宽约束或补充资源 |
| P3 | 任务无法拆分到可执行粒度 | 回退至 P2 简化架构或增加资源 |
| P4 | 代码审查发现架构风险 | 回退至 P2 调整设计 |
| P5 | 部署验证发现实现缺陷 | 回退至 P4 修复代码 |
| P6 | 监控指标异常 | 回退至 P5 回滚，或 P4 修复 |

### 4.2 跨阶段异常

| 异常 | 处理策略 |
| :--- | :--- |
| Schema 不兼容 | 触发 `schema-validator` 错误，阻塞流转，修复上游输出或下游输入映射 |
| 版本冲突 | `assets.lock` 校验失败，人工确认升级路径 |
| 外部依赖不可用 | 根据 `fallback` 策略执行降级或暂停 |
| 连续 3 个阶段评估失败 | 触发全流水线熔断，启动根因分析（Retrospective） |

---

## 5. 角色职责汇总

| 角色 | 主要职责 | 介入阶段 |
| :--- | :--- | :--- |
| **Product Analyst** | 需求结构化、验收标准编写、冲突识别 | P1 |
| **Solution Architect** | 技术选型、架构设计、ADR 撰写 | P2 |
| **Project Manager** | 任务拆分、工时估算、里程碑规划 | P3 |
| **Senior Engineer** | 代码审查、架构评审、技术方案评估 | P4 |
| **DevOps Engineer** | CI/CD 设计、部署执行、监控配置 | P5, P6 |
| **人类产品经理** | 确认需求优先级、澄清业务问题 | P1 |
| **人类技术负责人** | 审批架构方案、接受风险项 | P2, P4 |
| **人类项目经理** | 确认资源分配、审批里程碑 | P3 |
| **人类 SRE** | 审阅部署策略、确认 Oncall 路径 | P5, P6 |

---

## 6. 质量门禁速查

| 阶段 | 评估文件 | 通过阈值 | Mandatory 维度 |
| :--- | :--- | :--- | :--- |
| P1 | `evaluations/requirements-analysis-checkpoint.yaml` | >= 4.0/5.0 | safety |
| P2 | `evaluations/tech-arch-checkpoint.yaml` | >= 4.0/5.0 | safety |
| P3 | `evaluations/task-decomposition-checkpoint.yaml` | >= 4.0/5.0 | safety |
| P4 | `evaluations/code-review-checkpoint.yaml` | >= 4.0/5.0 | safety |
| P5 | `evaluations/deployment-checkpoint.yaml` | >= 4.0/5.0 | safety |
| P6 | `evaluations/monitoring-checkpoint.yaml` | >= 4.0/5.0 | safety |

---

## 7. 工具与模板索引

| 用途 | 路径 |
| :--- | :--- |
| 新建场景 | `templates/scenario-skeleton/` |
| 新建 Agent | `templates/agent-template/` |
| 新建技能 | `templates/skill-skeleton.yaml` |
| 项目初始化 | `templates/project-scaffold/` |
| 全局评分量规 | `standards/quality-rubric.yaml` |
| 命名规范 | `standards/naming-convention.md` |
| 版本管理 | `standards/versioning.md` |
| 质量检查清单 | `standards/quality-checklist.md` |
