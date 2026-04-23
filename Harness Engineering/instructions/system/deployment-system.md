# 部署系统指令 / Deployment System Instruction

> **效力等级**: L2（场景级约束）
> **适用范围**: `scenarios/deployment-pipeline/` 及其关联 Agent

---

## 1. 全局行为约束

- 所有部署配置必须遵循 GitOps 原则：配置即代码，变更需经 PR 评审
- 生产环境部署必须包含至少两种验证阶段（staging + canary / blue-green）
- 所有变更必须可追踪、可回滚、可审计
- 输出必须经过 `schema-validator` 校验通过后方可执行

## 2. 安全与合规

- 【强制】禁止在配置文件中硬编码密钥、Token、密码，必须使用 Secret 管理机制
- 【强制】容器镜像必须通过漏洞扫描（CVE 高危漏洞数为 0 方可进入生产）
- 【强制】涉及数据库迁移的部署必须包含预检脚本与回滚脚本
- 【强制】生产环境权限遵循最小权限原则（Least Privilege）

## 3. 输出格式强制规范

- CI/CD 配置使用标准 YAML 格式（GitHub Actions / GitLab CI / ArgoCD）
- Kubernetes Manifest 需符合 API 版本规范，禁止使用已废弃 API
- 回滚方案必须包含明确的触发条件、执行步骤与验证方法

## 4. 质量要求

- 部署策略必须定义流量切换条件（错误率阈值、延迟阈值、自定义指标）
- 健康检查必须包含：readiness（流量准入）、liveness（自愈）、startup（启动保护）
- 流水线必须包含：构建 → 单元测试 → 集成测试 → 安全扫描 → 部署 → 验证

## 5. 人工介入触发条件

- 涉及生产环境数据库 Schema 变更（DDL）
- 安全扫描发现高危漏洞且无法自动修复
- 金丝雀发布期间监控指标异常且自动回滚失败
