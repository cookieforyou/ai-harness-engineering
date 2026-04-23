# E2E 全生命周期规范 / End-to-End Workflow Lifecycle Specification

> **效力等级**: P0（强制）
> **适用范围**: 本资产库全部场景与跨阶段编排

---

## 1. 生命周期阶段定义

AI Harness 资产库覆盖软件交付的六个核心阶段，构成完整的 E2E 工作流：

| 阶段编号 | 阶段名称 | 场景目录 | 核心目标 | 下游阶段 |
| :--- | :--- | :--- | :--- | :--- |
| P1 | 需求分析 | `scenarios/requirements-analysis/` | 将原始需求转化为结构化 RFC | P2 |
| P2 | 技术架构 | `scenarios/tech-arch-design/` | 基于 RFC 设计技术方案与 ADR | P3 |
| P3 | 任务拆分 | `scenarios/task-decomposition/` | 将 ADR 拆分为可执行任务清单 | P4 |
| P4 | 开发实现 | `scenarios/code-review/` | 代码实现与质量审查 | P5 |
| P5 | 部署迭代 | `scenarios/deployment-pipeline/` | 安全发布与版本迭代 | P6 |
| P6 | 健康监控 | `scenarios/health-monitoring/` | 可观测性与持续健康保障 | P1（反馈闭环） |

---

## 2. 阶段流转规则

### 2.1 单向流转原则

- 标准工作流为单向流转：P1 → P2 → P3 → P4 → P5 → P6
- 允许基于评估结果的回退：
  - 若 P2 评估发现需求缺陷 → 回退至 P1 补充澄清
  - 若 P4 代码审查发现架构风险 → 回退至 P2 调整设计
  - 若 P5 部署验证发现实现缺陷 → 回退至 P4 修复代码
- P6 监控数据作为反馈输入 P1，形成持续改进闭环

### 2.2 阶段准入条件

每个阶段开始前，必须满足：

- [ ] 上游阶段输出已通过 `schema-validator` 校验
- [ ] 上游阶段评估得分 >= 阈值（默认 4.0/5.0）
- [ ] 无未解决的 Critical 级别安全或合规问题
- [ ] `assets.lock` 中依赖资产版本一致

### 2.3 阶段准出条件

每个阶段结束前，必须满足：

- [ ] 主输出通过本阶段 `checkpoint` 评估
- [ ] 输出 Schema 符合 `standards/scenario-integration.md` 中的衔接定义
- [ ] 运行日志与轨迹已归档至观测系统
- [ ] 人工介入节点（如有）已获得明确决策

---

## 3. 反馈闭环机制

### 3.1 P6 → P1 反馈通道

健康监控阶段产生的以下数据应作为需求分析的输入：

- **性能瓶颈报告** → 转化为非功能性需求优化项
- **错误模式分析** → 转化为可靠性需求或验收标准补充
- **用户行为监控** → 转化为新功能需求或现有功能改进

### 3.2 反馈数据格式

反馈数据使用统一的 `feedback-package` Schema：

```json
{
  "feedback_id": "FB-001",
  "source_stage": "P6",
  "target_stage": "P1",
  "type": "performance|reliability|usability|security",
  "severity": "low|medium|high|critical",
  "description": "...",
  "evidence": { "metric_name": "...", "threshold": "...", "actual_value": "..." },
  "suggested_action": "..."
}
```

---

## 4. 异常处理与熔断

### 4.1 阶段内异常

- 单节点失败：触发重试策略（`retry_policy`）
- 重试耗尽：触发人工介入（`human_escalation`）
- 评估未通过：根据分支条件选择重试、降级或人工介入

### 4.2 跨阶段异常

- Schema 不兼容：触发 `schema-validator` 错误，阻塞流转
- 版本冲突：触发 `assets.lock` 校验失败，需人工确认升级路径
- 外部依赖不可用：根据 `fallback` 策略执行降级或暂停

### 4.3 熔断机制

当连续 3 个阶段出现评估失败时，触发全流水线熔断：

1. 暂停后续阶段执行
2. 通知项目管理员与相关阶段负责人
3. 启动根因分析（Retrospective）流程
4. 修复后需全量回归测试方可恢复

---

## 5. 版本与变更管理

### 5.1 流水线版本

E2E 流水线通过 `pipeline.lock` 锁定各场景版本组合：

```yaml
pipeline_id: "e2e-delivery-v1"
version: "1.0.0"
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

### 5.2 变更影响分析

修改任一阶段资产时，必须评估对下游阶段的影响：

- **P1 输出 Schema 变更** → 必须同步更新 P2 输入定义
- **P2 技术选型变更** → 必须同步更新 P3 任务角色分配与 P5 部署配置
- **P3 任务范围变更** → 必须同步更新 P4 代码审查范围
- **P5 部署策略变更** → 必须同步更新 P6 监控指标与告警阈值

影响分析结果记录在 `standards/scenario-integration.md` 的兼容性矩阵中。
