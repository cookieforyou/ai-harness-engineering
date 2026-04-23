# 监控系统指令 / Monitoring System Instruction

> **效力等级**: L2（场景级约束）
> **适用范围**: `scenarios/health-monitoring/` 及其关联 Agent

---

## 1. 全局行为约束

- 监控设计必须基于明确的 SLO/SLI，禁止无目标的指标堆砌
- 告警必须遵循「 actionable 」原则：每个告警都必须对应明确的排查步骤
- 仪表盘设计遵循「5 秒原则」：核心指标应在 5 秒内帮助定位问题范围
- 输出必须经过 `schema-validator` 校验通过后方可生效

## 2. 安全与合规

- 【强制】监控数据中禁止包含用户敏感信息（PII），如需追踪用户行为必须脱敏
- 【强制】告警通知渠道必须加密传输，禁止通过未加密邮件发送敏感监控信息
- 【强制】日志保留策略需符合合规要求（如 GDPR 要求删除权）

## 3. 输出格式强制规范

- 告警规则使用 Prometheus Rule 标准格式（expr、for、labels、annotations）
- 仪表盘面板定义包含：title、description、query、threshold、unit
- 健康检查定义包含：endpoint、method、expected_status、timeout、retry_policy

## 4. 质量要求

- 指标定义遵循 RED 方法：Rate（请求率）、Errors（错误率）、Duration（延迟）
- 告警分级：Critical（立即响应）、Warning（工作时间响应）、Info（异步处理）
- 必须定义告警抑制规则：维护窗口、级联故障抑制、已知问题静默
- Oncall 手册必须包含：现象描述、排查步骤、常见误操作、升级路径

## 5. 人工介入触发条件

- SLO 持续违反且根因无法自动定位
- 监控基础设施自身故障（如 Prometheus 宕机）
- 需要调整 SLO 阈值或新增业务指标定义
