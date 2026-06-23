---
name: static-code-analysis
type: evaluation
version: "1.1.0"
status: active
updated: 2026-06-23
description: >
  静态代码分析评估，覆盖工具配置标准(SonarQube/ESLint/golangci-lint/Checkstyle)、
  规则集推荐、质量门禁阈值、误报管理流程和技术债务量化。
  用于持续保障代码质量，在CI/CD流水线中执行自动化代码审查。
---

# 静态代码分析评估 (Static Code Analysis Evaluation)

## Overview

静态代码分析评估用于确保静态分析工具在项目中正确配置、有效运行，并产出可量化的质量指标。本评估涵盖工具选型和配置、规则集管理、质量门禁阈值、误报处理和技术债务跟踪。适用于新项目初始化时的工具链搭建、存量项目的工具审计和季度代码质量健康度检查。

### 适用场景

- 新项目/新仓库静态分析工具链搭建检查
- CI/CD 流水线中静态分析门禁的合规审核
- 季度技术债务回顾与量化分析
- 误报率治理和规则集优化专项

---

## Evaluation Criteria

| 维度 | 权重 | 目标值 | 测量方法 |
|------|------|--------|----------|
| 工具配置标准 | 25% | 工具覆盖率 100% | 按语言/框架检查工具安装和配置 |
| 规则集推荐 | 20% | 激活规则合规率 ≥ 95% | 安全规则全开 + 质量规则覆盖率 |
| 质量门禁阈值 | 25% | Bug 数 = 0, 漏洞 = 0, 异味 ≤ 5% | SonarQube Quality Gate / CI 检查 |
| 误报管理流程 | 15% | 误报率 ≤ 10% | 误报标记数 / 总问题数 |
| 技术债务量化 | 15% | 债务比 ≤ 5% | 修复成本 / 开发成本 |

### 支持工具矩阵

| 工具 | 适用语言 | 配置文件 | 关键门禁指标 |
|------|----------|----------|-------------|
| SonarQube/SonarCloud | Java/C#/TS/Python/Go/等 | `sonar-project.properties` | Bugs=0, Vulnerabilities=0, Debt Ratio ≤ 5% |
| ESLint + @typescript-eslint | JavaScript/TypeScript | `.eslintrc.js` / `eslint.config.js` | Errors=0, Warnings ≤ 10 |
| golangci-lint | Go | `.golangci.yml` | Issues=0, 或 Suppressed 授权 |
| Checkstyle | Java | `checkstyle.xml` / `google_checks.xml` | Errors=0, Warnings ≤ 20 |
| Pylint / Flake8 | Python | `.pylintrc` / `.flake8` | Score ≥ 9.0 / Errors=0 |
| RuboCop | Ruby | `.rubocop.yml` | Offenses=0 |

---

## Scoring Formula

```
工具得分   = 已配置工具数 / 应配置工具数 × 100
规则得分   = (安全规则激活率 × 50% + 质量规则覆盖率 × 50%) × 100
门禁得分   = 
  Bugs=0 且 Vulns=0 且 DebtRatio≤5% → 100
  Bugs=0 且 Vulns=0 → 70
  Bugs>0 或 Vulns>0 → 0

误报得分 = max(0, 100 - 误报率 × 200)
债务得分 = max(0, 100 - 债务比 × 500)          // 债务比每超1%扣5分

总分 = 工具得分 × 25% + 规则得分 × 20% + 门禁得分 × 25% + 误报得分 × 15% + 债务得分 × 15%
```

### 等级划分

| 等级 | 分数范围 | 判定 |
|------|----------|------|
| S (Excellent) | ≥ 90 | 静态分析体系成熟，技术债务可控 |
| A (Good) | 80-89 | 主要指标达标，优化空间有限 |
| B (Fair) | 70-79 | 存在明显问题，需专项治理 |
| F (Failed) | < 70 | 静态分析体系缺失或严重失效 |

---

## Checklist

### 1. 工具配置标准检查 (6项)

- [ ] **SCA-CFG-001**: 项目语言对应的静态分析工具已安装并正确配置，配置文件纳入版本控制
- [ ] **SCA-CFG-002**: 工具在 CI/CD 流水线中集成，每次 PR/MR 自动执行扫描
- [ ] **SCA-CFG-003**: 工具扫描范围为整个代码库（含测试目录），排除自动生成代码和第三方依赖
- [ ] **SCA-CFG-004**: 工具配置了增量扫描模式（仅检测变更文件），全量扫描至少每周执行一次
- [ ] **SCA-CFG-005**: 工具版本固定（lock 版本号），升级需经过回归验证
- [ ] **SCA-CFG-006**: 多模块/多语言项目覆盖所有子模块，无语言或模块遗漏

### 2. 规则集管理检查 (6项)

- [ ] **SCA-RUL-001**: 安全相关规则集全部激活（OWASP Top 10 / CWE Top 25 对应规则）
- [ ] **SCA-RUL-002**: 代码质量规则按照项目语言的最佳实践激活（Google Style / Airbnb Style / Effective Go）
- [ ] **SCA-RUL-003**: 规则禁用有正式审批，禁用理由记录在配置注释中
- [ ] **SCA-RUL-004**: 规则集每季度审查一次，跟进工具版本升级的新规则
- [ ] **SCA-RUL-005**: 自定义规则/规则增强已文档化（解决的问题、适用范围、判定标准）
- [ ] **SCA-RUL-006**: 规则按严重等级分类：Blocker/Critical/Major/Minor/Info，门禁至少覆盖 Critical 及以上

### 3. 质量门禁阈值检查 (5项)

- [ ] **SCA-GAT-001**: Quality Gate 门禁：Bugs = 0, Vulnerabilities = 0, Security Hotspots Reviewed = 100%
- [ ] **SCA-GAT-002**: 新增代码的 Code Smell 密度 ≤ 3%（新增代码异味行 / 新增代码总行数）
- [ ] **SCA-GAT-003**: 重复代码密度 ≤ 3%（SonarQube Duplicated Lines (%)）
- [ ] **SCA-GAT-004**: 门禁失败阻塞流水线，PR/MR 禁止合入（门禁违规 → 需要审批豁免或修复）
- [ ] **SCA-GAT-005**: 门禁阈值团队共识，调整需通过架构师评审并记录变更

### 4. 误报管理流程检查 (5项)

- [ ] **SCA-FPR-001**: 误报率 ≤ 10%（被标记为误报的问题数 / 总发现问题数）
- [ ] **SCA-FPR-002**: 误报标记带有注释说明原因，非静默忽略（Wont Fix / False Positive 注释）
- [ ] **SCA-FPR-003**: 误报定期审查（每月）并推动工具规则改进以消除误报模式
- [ ] **SCA-FPR-004**: 通过规则的 Suppress/Warn 机制而非全局禁用来处理误报
- [ ] **SCA-FPR-005**: 误报分析结果反馈给工具维护者或社区（规则改进 PR/Issue）

### 5. 技术债务量化检查 (4项)

- [ ] **SCA-DEB-001**: 技术债务比率 ≤ 5%（SonarQube: 修复所有问题的估算时间 / 重写代码的估算时间）
- [ ] **SCA-DEB-002**: 技术债务按模块/组件分解，Top 5 技术债务模块有改进计划
- [ ] **SCA-DEB-003**: 技术债务趋势在最近 3 个迭代中稳定或下降（无持续增长）
- [ ] **SCA-DEB-004**: 每个迭代分配 ≥ 20% 的容量用于偿还技术债务（或固定时间预算）

---

## Report Template

```markdown
# 静态代码分析评估报告

## 概要

| 项目 | 值 |
|------|-----|
| 评估对象 | [项目/仓库] |
| 评估日期 | YYYY-MM-DD |
| 代码语言 | [Java/Python/Go/TS] |
| 代码行数 | [N] (排除自动生成) |
| 扫描工具 | [SonarQube/ESLint/golangci-lint] |
| 综合评分 | [XX.X] 分 / 100 |
| 等级判定 | [S/A/B/F] |

## 质量指标

| 指标 | 当前值 | 目标值 | 达标 |
|------|--------|--------|------|
| Bugs | N | 0 | Y/N |
| Vulnerabilities | N | 0 | Y/N |
| Security Hotspots | N/Reviewed | 100% | Y/N |
| Code Smells | N | — | — |
| Smell Density | X.X% | ≤ 3% | Y/N |
| Duplicated Lines | X.X% | ≤ 3% | Y/N |
| Debt Ratio | X.X% | ≤ 5% | Y/N |
| Coverage | XX.X% | ≥ 80% | Y/N |

## Top 问题清单

| 严重等级 | 规则 | 文件 | 问题描述 | 标记 |
|----------|------|------|----------|------|
| Critical | | | | |
| Major | | | | |
| Minor | | | | |

## 误报统计

| 周期 | 总问题数 | 误报标记数 | 误报率 | 主要误报模式 |
|------|----------|------------|--------|-------------|
| | | | | |

## 技术债务分解

| 模块 | 债务比 | 预估修复人天 | 主要债务来源 | 改进负责人 |
|------|--------|-------------|-------------|-----------|
| | | | | |

## 改进计划

| # | 改进项 | 优先级 | 责任人 | 截止日期 | 状态 |
|---|--------|--------|--------|----------|------|
| 1 | | | | | |

---

## Revision History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | YYYY-MM-DD | Initial report | 评估团队 |
```

---

## 相关评估

- [code-quality-checklist.md](../evaluations/code-quality-checklist.md)
- [common-error-patterns.md](../evaluations/common-error-patterns.md)
- [design-quality-assessment.md](../evaluations/design-quality-assessment.md)
- [coverage-analysis.md](../evaluations/coverage-analysis.md)
