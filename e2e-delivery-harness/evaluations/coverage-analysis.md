---
name: coverage-analysis
type: evaluation
version: "1.1.0"
status: active
updated: 2026-06-23
description: >
  覆盖率分析评估，从行覆盖率、分支覆盖率、函数覆盖率和变更覆盖率四个维度
  衡量测试充分性。基于 JaCoCo/coverage.py/Istanbul 报告解读，
  按模块分层设定目标值，识别测试缺口并驱动覆盖率持续提升。
---

# 覆盖率分析评估 (Coverage Analysis Evaluation)

## Overview

覆盖率分析评估从四个维度衡量测试对代码的覆盖程度，帮助团队识别未覆盖的风险区域，制定针对性的测试补充策略。本评估适用于 CI/CD 流水线中的质量门禁、版本发布前的质量审核以及定期测试健康度检查。

### 适用场景

- CI 流水线中 PR 合并前的覆盖率门禁检查
- 迭代结束后覆盖率趋势回顾
- 新模块/新功能上线的测试充分性评估
- 测试缺口分析（识别高风险低覆盖模块）

---

## Evaluation Criteria

| 维度 | 权重 | 目标值 | 测量方法 |
|------|------|--------|----------|
| 行覆盖率 (Line Coverage) | 30% | 核心模块 ≥ 90%，非核心 ≥ 70% | JaCoCo/coverage.py/Istanbul XML/HTML 报告 |
| 分支覆盖率 (Branch Coverage) | 30% | 核心模块 ≥ 85%，非核心 ≥ 60% | Cobertura/coverage.py branch 报告 |
| 函数覆盖率 (Function Coverage) | 15% | 核心模块 ≥ 95%，非核心 ≥ 80% | 测试框架函数覆盖报告 |
| 变更覆盖率 (Change Coverage) | 25% | PR 变更行覆盖 ≥ 85% | diff-cover / git diff + 覆盖率合并分析 |

### 模块分层定义

| 层级 | 定义 | 范围举例 |
|------|------|----------|
| 核心模块 (Core) | 业务核心逻辑、公共基础设施、安全模块 | domain/model、service/core、security/auth |
| 非核心模块 (Non-core) | 辅助功能、管理界面、非关键路径 | admin、utils、integration-adapter |

### 工具支持

| 工具 | 适用语言 | 输出格式 | 关键命令 |
|------|----------|----------|----------|
| JaCoCo | Java/Kotlin | XML/HTML/CSV | `mvn jacoco:report` / `gradle jacocoTestReport` |
| coverage.py | Python | XML/HTML/JSON | `coverage run && coverage xml` |
| Istanbul/nyc | JavaScript/TypeScript | JSON/LCOV/HTML | `nyc --reporter=lcov --reporter=text` |
| gcov/lcov | C/C++ | LCOV/HTML | `lcov --capture --directory . --output-file coverage.info` |
| Go cover | Go | HTML/out | `go test -coverprofile=coverage.out -covermode=atomic` |

---

## Scoring Formula

```
行覆盖率得分 = 实际行覆盖率 / 目标行覆盖率 × 100（上限 100）
分支覆盖率得分 = 实际分支覆盖率 / 目标分支覆盖率 × 100（上限 100）
函数覆盖率得分 = 实际函数覆盖率 / 目标函数覆盖率 × 100（上限 100）
变更覆盖率得分 = 实际变更覆盖率 / 85% × 100（上限 100）

总分 = 行覆盖率得分 × 30% + 分支覆盖率得分 × 30% + 函数覆盖率得分 × 15% + 变更覆盖率得分 × 25%
```

### 等级划分

| 等级 | 分数范围 | 判定 |
|------|----------|------|
| S (Excellent) | ≥ 90 | 测试覆盖充分，核心模块达标 |
| A (Good) | 80-89 | 主要模块达标，少量改进空间 |
| B (Fair) | 70-79 | 存在明显覆盖缺口，需补充测试 |
| F (Failed) | < 70 | 覆盖严重不足，禁止发布 |

---

## Checklist

### 1. 行覆盖率检查 (5项)

- [ ] **CV-LC-001**: 核心模块行覆盖率 ≥ 90%，基于 JaCoCo/coverage.py/Istanbul 报告确认
- [ ] **CV-LC-002**: 非核心模块行覆盖率 ≥ 70%，豁免模块有正式审批记录
- [ ] **CV-LC-003**: 覆盖率报告排除自动生成代码（Lombok、代码生成器产物、Protobuf 生成类）
- [ ] **CV-LC-004**: 覆盖率趋势在最近 3 个迭代中无下降（或下降有合理解释）
- [ ] **CV-LC-005**: 新增代码文件均有覆盖率数据（无 0% 覆盖率的已合入文件）

### 2. 分支覆盖率检查 (5项)

- [ ] **CV-BC-001**: 核心模块分支覆盖率 ≥ 85%，if/else/switch/case 分支均覆盖
- [ ] **CV-BC-002**: 关键条件分支（权限判断、状态流转、金额计算）分支覆盖达 100%
- [ ] **CV-BC-003**: 三元运算符和逻辑运算符（&&/||）短路分支已覆盖
- [ ] **CV-BC-004**: try/catch 异常分支已覆盖（至少一条 catch 路径有测试）
- [ ] **CV-BC-005**: 分支覆盖率与行覆盖率的比值 ≥ 0.85（分支覆盖接近行覆盖水平）

### 3. 函数覆盖率检查 (4项)

- [ ] **CV-FC-001**: 核心模块函数覆盖率 ≥ 95%，所有 public 方法有对应测试
- [ ] **CV-FC-002**: private 辅助方法通过 public 方法的测试间接覆盖（无需直接测试）
- [ ] **CV-FC-003**: 未被测试覆盖的函数已标记 `@NotTested` 并注明理由
- [ ] **CV-FC-004**: 入口函数（Controller/API Handler/Event Consumer）覆盖率达 100%

### 4. 变更覆盖率检查 (6项)

- [ ] **CV-CC-001**: PR 差异代码的变更覆盖率 ≥ 85%（通过 diff-cover 或 CI 插件测量）
- [ ] **CV-CC-002**: 变更覆盖报告中标红的未覆盖行均已人工确认并添加测试
- [ ] **CV-CC-003**: 测试代码本身的覆盖率不计入变更覆盖率统计
- [ ] **CV-CC-004**: 变更覆盖门禁在 CI 中配置为 mandatory check（阻塞合入）
- [ ] **CV-CC-005**: 变更不降低整体覆盖率（整体覆盖率下降 < 0.5%）
- [ ] **CV-CC-006**: 重构/迁移类变更允许临时豁免，但需在 2 个迭代内补齐

---

## Report Template

```markdown
# 覆盖率分析报告

## 概要

| 项目 | 值 |
|------|-----|
| 分析对象 | [项目/模块] |
| 分析日期 | YYYY-MM-DD |
| 代码语言 | [Java/Python/Go/TS] |
| 覆盖工具 | [JaCoCo/coverage.py/Istanbul] |
| 总代码行数 | [N] (排除自动生成代码) |
| 综合评分 | [XX.X] 分 / 100 |
| 等级判定 | [S/A/B/F] |

## 四维覆盖率

| 维度 | 实际值 | 目标值 (核心模块) | 加权得分 |
|------|--------|--------------------|----------|
| 行覆盖率 | XX.X% | ≥ 90% | XX.X |
| 分支覆盖率 | XX.X% | ≥ 85% | XX.X |
| 函数覆盖率 | XX.X% | ≥ 95% | XX.X |
| 变更覆盖率 | XX.X% | ≥ 85% | XX.X |
| **总分** | | | **XX.X** |

## 模块明细

| 模块 | 层级 | 行覆盖率 | 分支覆盖率 | 函数覆盖率 | 缺口分析 |
|------|------|----------|------------|------------|----------|
| module-a | Core | XX.X% | XX.X% | XX.X% | [缺口描述] |
| module-b | Non-core | XX.X% | XX.X% | XX.X% | [缺口描述] |

## 覆盖率缺口 (Top 未覆盖文件)

| 文件 | 行覆盖率 | 未覆盖行数 | 风险等级 | 建议 |
|------|----------|------------|----------|------|
| src/main/java/.../Xxx.java | XX% | N | High | 补充条件分支测试 |
| src/main/java/.../Yyy.java | XX% | N | Medium | 补充异常路径测试 |

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

- [test-coverage-analysis.md](../evaluations/test-coverage-analysis.md)
- [regression-test-suite.md](../evaluations/regression-test-suite.md)
- [code-quality-checklist.md](../evaluations/code-quality-checklist.md)
- [common-error-patterns.md](../evaluations/common-error-patterns.md)
