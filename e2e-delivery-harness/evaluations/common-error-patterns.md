---
name: common-error-patterns
type: evaluation
version: "1.1.0"
status: active
language: "zh-CN"
updated: 2026-06-23
description: >
  常见错误模式检查清单，覆盖10类编码/架构/配置错误的检测方法、严重等级、
  修复建议和预防措施。用于开发阶段自检和Code Review中的错误模式识别，
  帮助团队系统化减少重复性错误。
---

# 常见错误模式检查 (Common Error Patterns Checklist)

## Overview

本清单汇总了 E2E 交付流程中 10 类常见的编码/架构/配置错误模式，每类模式包含检测方法、严重等级（Critical/High/Medium/Low）、修复建议和预防措施。适用于开发阶段自检、Code Review 评审和事后复盘中的错误模式识别。

### 适用场景

- 代码审查中快速定位已知错误模式
- 开发完成后合入前的质量门禁检查
- 缺陷根因分析时的模式匹配
- 新团队成员的上岗培训和常见陷阱告知

---

## Evaluation Criteria

| 维度 | 权重 | 目标值 | 测量方法 |
|------|------|--------|----------|
| 编码错误模式 (4类) | 35% | 覆盖率 ≥ 90% | 代码检查/SAST工具检出率 |
| 架构错误模式 (3类) | 30% | 合规率 ≥ 85% | 架构评审/依赖分析 |
| 配置错误模式 (3类) | 20% | 合规率 ≥ 95% | 配置审计/Infra as Code检查 |
| 预防机制有效性 | 15% | 同类错误复发率 ≤ 10% | 缺陷回溯/趋势分析 |

---

## Scoring Formula

```
编码得分 = (已覆盖编码模式 / 4) × 100
架构得分 = (已覆盖架构模式 / 3) × 100
配置得分 = (已覆盖配置模式 / 3) × 100
预防得分 = max(0, 100 - 复发率 × 5)

总分 = 编码得分 × 35% + 架构得分 × 30% + 配置得分 × 20% + 预防得分 × 15%
```

### 等级划分

| 等级 | 分数范围 | 判定 |
|------|----------|------|
| S (Excellent) | ≥ 90 | 错误模式管理体系成熟 |
| A (Good) | 75-89 | 主要模式已覆盖，持续改进 |
| B (Fair) | 60-74 | 覆盖不足，需补充模式库 |
| F (Failed) | < 60 | 错误模式管理缺失，需从零构建 |

---

## 错误模式清单

### 1. 编码错误模式 (4类)

#### 1.1 空指针/空引用 (Null Pointer / Null Reference) — Critical

- **检测方法**: 静态分析 (SpotBugs/FindBugs/ESLint no-unbound-method)、代码路径分析
- **严重等级**: Critical — 生产环境直接导致 Crash 或数据不一致
- **修复建议**: (1) 使用 Optional/Option 类型包装可空值；(2) 函数签名显式标注 `@Nullable`/`@NonNull`；(3) 外部输入入口统一做 null check
- **预防措施**: (1) 启用编译器 null-safety 警告并视为错误；(2) 禁止方法返回 null 引用，改为空集合/Optional；(3) Code Review 强制检查外部数据入口

#### 1.2 资源泄漏 (Resource Leak) — Critical

- **检测方法**: 静态分析 (findbugs:OBL_UNSATISFIED_OBLIGATION)、Code Review 资源生命周期追踪
- **严重等级**: Critical — 连接池耗尽导致服务不可用，文件描述符泄漏累积 OOM
- **修复建议**: (1) 使用 try-with-resources (Java) / using (C#) / context manager (Python)；(2) finally 块保证 release；(3) 连接池设置最大生存时间和泄漏检测
- **预防措施**: (1) 资源类必须实现 AutoCloseable/IDisposable；(2) CI 流水线集成资源泄漏检测；(3) 定期（每月）检查连接池监控面板

#### 1.3 并发竞态 (Concurrency Race Condition) — Critical

- **检测方法**: 动态分析 (ThreadSanitizer)、压力测试 + assertion 验证、Code Review 共享变量访问路径
- **严重等级**: Critical — 数据竞争导致脏读、库存超卖、金额计算错误
- **修复建议**: (1) 共享变量使用原子类或锁保护；(2) 优先使用不变对象 (Immutable)；(3) 数据库层面使用乐观锁代替分布式锁
- **预防措施**: (1) 禁止在锁内执行 IO/网络操作；(2) 共享状态最小化原则；(3) 并发代码必须经 Thread Safety Review

#### 1.4 SQL 注入/命令注入 (Injection) — Critical

- **检测方法**: SAST 扫描 (SQLi rules)、Code Review 检查字符串拼接、DAST 渗透测试
- **严重等级**: Critical — 数据泄露、数据篡改、完全失陷
- **修复建议**: (1) 全部使用参数化查询/Prepared Statement；(2) 禁止拼接 SQL 字符串；(3) 严格输入校验白名单
- **预防措施**: (1) ORM 框架配置禁止原生 SQL；(2) 静态分析规则阻断 SQL 拼接模式；(3) 每季度渗透测试覆盖注入场景

### 2. 架构错误模式 (3类)

#### 2.1 循环依赖 (Circular Dependency) — High

- **检测方法**: 依赖图分析 (JDepend/ArchUnit/dependency-cruiser)、构建工具 circular-dependency 插件
- **严重等级**: High — 难以测试、部署顺序耦合、模块无法独立演进
- **修复建议**: (1) 引入接口/抽象层打破循环；(2) 使用事件驱动或依赖注入容器；(3) 提取公共依赖到共享模块
- **预防措施**: (1) 架构规则纳入 CI 门禁，禁止新循环依赖引入；(2) 模块依赖方向遵循分层架构（上层依赖下层）

#### 2.2 过度抽象/过度工程 (Over-engineering) — Medium

- **检测方法**: Code Review 评审、认知负荷评估、复杂性度量 (LCOM/CBO)
- **严重等级**: Medium — 维护成本高、开发效率下降、新成员学习曲线陡峭
- **修复建议**: (1) YAGNI 原则裁剪不必要的抽象层；(2) 简化继承层级（深度 ≤ 4）；(3) 移除未使用的接口/工厂/策略类
- **预防措施**: (1) 架构评审门槛：引入新设计模式需说明必要性；(2) 定期代码清理（重构腐化代码）

#### 2.3 分布式事务滥用 (Distributed Transaction Misuse) — High

- **检测方法**: 代码搜索 `@Transactional` + 多数据源调用、分布式事务框架使用审计
- **严重等级**: High — 性能瓶颈、死锁、一致性窗口扩大
- **修复建议**: (1) 评估是否可降级为最终一致性+补偿机制；(2) 缩短事务边界，事务内不包含 RPC/远程调用；(3) 使用 Saga/TCC 模式替代全局 XA
- **预防措施**: (1) 禁止跨服务事务（@Transactional 只用于单数据源）；(2) 分布式事务必须经架构师审批；(3) 优先设计幂等接口

### 3. 配置错误模式 (3类)

#### 3.1 硬编码配置 (Hardcoded Configuration) — High

- **检测方法**: 代码扫描 (魔法数字/字符串检测)、配置管理审计
- **严重等级**: High — 环境切换困难、机密泄露风险、无法动态调整
- **修复建议**: (1) 所有环境相关配置外移至环境变量/配置中心；(2) 魔法数值提取为常量或配置项；(3) 配置项中心化管理（Apollo/Nacos/Spring Cloud Config）
- **预防措施**: (1) 静态分析规则：禁止代码中出现未经声明的字符串/数值字面量；(2) 配置变更通过 CI/CD 审批流程

#### 3.2 密钥硬编码 (Secret Hardcoding) — Critical

- **检测方法**: 秘密扫描工具 (GitLeaks/TruffleHog/GitGuardian)、提交钩子 pre-commit 扫描
- **严重等级**: Critical — 凭证泄露导致安全事件、合规违规（PCI-DSS/SOC2）
- **修复建议**: (1) 立即轮换泄露密钥；(2) 使用密钥管理服务 (Vault/AWS Secrets Manager/K8s Secrets)；(3) 从 Git 历史中清理（BFG Repo-Cleaner）
- **预防措施**: (1) pre-commit hook 阻断含密钥文件的提交；(2) CI 流水线秘密扫描； (3) 密钥检测接入安全告警

#### 3.3 配置漂移 (Configuration Drift) — Medium

- **检测方法**: 配置审计工具、Infrastructure as Code 与生产环境比对、定期配置一致性检查
- **严重等级**: Medium — 环境不一致导致难以排查的缺陷、部署失败
- **修复建议**: (1) 全部 Infra 配置纳入 GitOps 管理；(2) 定期执行配置一致性检查并修复漂移；(3) 禁止手动变更生产配置
- **预防措施**: (1) 配置即代码 (IaC) 覆盖率 100%；(2) 配置变更必须走 MR/PR 流程；(3) 自动化漂移修复（Drift Detection + Reconciliation）

---

## 错误复发统计

| 错误分类 | 上次评估发现数 | 本次评估发现数 | 复发率 | 趋势 |
|----------|---------------|---------------|--------|------|
| 编码错误 | | | | ↑/→/↓ |
| 架构错误 | | | | ↑/→/↓ |
| 配置错误 | | | | ↑/→/↓ |

---

## Report Template

```markdown
# 常见错误模式检查报告

## 概要

| 项目 | 值 |
|------|-----|
| 评估对象 | [项目/模块/代码库] |
| 评估日期 | YYYY-MM-DD |
| 评估范围 | [代码行数/文件数] |
| 发现总问题数 | [N] |
| 综合评分 | [XX.X] 分 / 100 |
| 等级判定 | [S/A/B/F] |

## 分类统计

| 错误分类 | 发现数 | Critical | High | Medium | Low | 修复率 |
|----------|--------|----------|------|--------|-----|--------|
| 编码错误 | | | | | | |
| 架构错误 | | | | | | |
| 配置错误 | | | | | | |
| **合计** | | | | | | |

## Top 问题详情

| # | 模式类型 | 文件/位置 | 问题描述 | 严重等级 | 修复建议 | 责任人 | 截止日期 |
|---|----------|-----------|----------|----------|----------|--------|----------|
| 1 | | | | | | | |

## 预防措施改进项

| # | 改进内容 | 优先级 | 负责人 | 计划完成 | 状态 |
|---|----------|--------|--------|----------|------|
| 1 | | | | | |

---

## Revision History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | YYYY-MM-DD | Initial assessment | 评估团队 |
```

---

## 自检清单

在提交代码或执行 Code Review 前，逐项确认以下检查项：

### 编码错误检查

- [ ] **EC-001**: 所有外部输入均已做 null/undefined 检查，无直接解引用
- [ ] **EC-002**: 所有资源（连接、文件、锁）均使用 try-with-resources / context manager 模式
- [ ] **EC-003**: 共享变量访问有明确的并发保护策略（原子类/锁/不可变对象）

### 架构错误检查

- [ ] **EA-001**: 外部 API 调用均有超时（≤30s）+ 重试（≤3次）+ 熔断保护
- [ ] **EA-002**: 同步调用链深度 ≤3 层，无阻塞事件循环的风险
- [ ] **EA-003**: 缓存策略有明确的失效机制和一致性问题处理方案

### 配置错误检查

- [ ] **ECF-001**: 敏感信息（密钥/Token/密码）未硬编码，使用 Secret Manager
- [ ] **ECF-002**: 所有环境差异通过配置注入，无环境专属代码分支

### 错误处理检查

- [ ] **EEH-001**: 异常信息不含敏感数据（密钥/内部IP/数据库结构）
- [ ] **EEH-002**: 所有 P0/P1 异常有对应的告警规则和 Runbook 链接

## 相关评估

- [static-code-analysis.md](../evaluations/static-code-analysis.md)
- [code-quality-checklist.md](../evaluations/code-quality-checklist.md)
- [schema-review-checklist.md](../evaluations/schema-review-checklist.md)
- [design-quality-assessment.md](../evaluations/design-quality-assessment.md)
