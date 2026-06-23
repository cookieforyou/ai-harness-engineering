---
name: test-coverage-analysis
type: evaluation
version: "1.1.0"
status: active
updated: 2026-06-23
description: >
  测试覆盖率分析评估，四维覆盖率评估(行/分支/函数/变更)、
  按模块分层目标、覆盖率趋势监控和覆盖率缺口分析报告模板。
  用于系统地评估测试对代码的覆盖充分性，持续驱动测试完善。
---

# 测试覆盖率分析评估 (Test Coverage Analysis Evaluation)

## Overview

测试覆盖率分析评估用于多维度评估测试对代码的覆盖充分性，通过行覆盖率、分支覆盖率、函数覆盖率和变更覆盖率四个维度，按模块分层设定差异化的目标值，识别测试缺口并驱动测试持续改进。本评估适用于 CI/CD 流水线中的质量门禁、版本发布前的测试充分性评估和测试投入 ROI 分析。

### 适用场景

- PR 合入前的测试覆盖率门禁检查
- 迭代结束后测试健康度回顾
- 新模块/新功能的测试充分性基线建立
- 测试缺口分析报告生成（哪些代码未被测试覆盖）
- 代码重构前/后的测试覆盖率对比

---

## Evaluation Criteria

| 维度 | 权重 | 目标值 (核心/非核心) | 测量方法 |
|------|------|---------------------|----------|
| 行覆盖率 (Line Coverage) | 25% | Core ≥ 90%, Non-core ≥ 70% | JaCoCo/coverage.py/Istanbul 行覆盖报告 |
| 分支覆盖率 (Branch Coverage) | 30% | Core ≥ 85%, Non-core ≥ 60% | Cobertura/分支覆盖报告 |
| 函数覆盖率 (Function Coverage) | 15% | Core ≥ 95%, Non-core ≥ 80% | 函数/方法级别覆盖报告 |
| 变更覆盖率 (Change Coverage) | 30% | PR 变更 ≥ 85% | diff-cover / git diff 合并分析 |

### 模块分层与目标

| 层级 | 定义 | 行覆盖率 | 分支覆盖率 | 函数覆盖率 |
|------|------|----------|------------|------------|
| Core (核心) | 业务逻辑层、领域模型、公共服务 | ≥ 90% | ≥ 85% | ≥ 95% |
| Non-core (非核心) | 配置、工具、适配器、管理接口 | ≥ 70% | ≥ 60% | ≥ 80% |
| Exempt (豁免) | 自动生成代码、模板、原型 | 不要求 | 不要求 | 不要求 |

### 工具集成指南

| 语言 | 覆盖率工具 | CI 集成 | 门禁配置 |
|------|-----------|---------|----------|
| Java/Kotlin | JaCoCo + diff-cover | `mvn verify jacoco:report` | `diff-cover coverage.xml --fail-under=85` |
| Python | coverage.py + diff-cover | `coverage run -m pytest && coverage xml` | `diff-cover coverage.xml --fail-under=85` |
| JavaScript/TS | Istanbul/nyc | `nyc --reporter=lcov --reporter=text` | `nyc check-coverage --branches 85` |
| Go | go test -cover | `go test -coverprofile=coverage.out` | `go tool cover -func=coverage.out` 检查 |
| C/C++ | gcov/lcov | `lcov --capture --directory . --output-file coverage.info` | `lcov --summary` 解析 |

---

## Scoring Formula

```
行覆盖率得分 = 实际行覆盖率 / 目标行覆盖率 × 100（上限 100）
分支覆盖率得分 = 实际分支覆盖率 / 目标分支覆盖率 × 100（上限 100）
函数覆盖率得分 = 实际函数覆盖率 / 目标函数覆盖率 × 100（上限 100）
变更覆盖率得分 = min(实际变更覆盖率 / 85%, 1) × 100

总分 = 行覆盖率得分 × 25% + 分支覆盖率得分 × 30% + 函数覆盖率得分 × 15% + 变更覆盖率得分 × 30%
```

### 等级划分

| 等级 | 分数范围 | 判定 |
|------|----------|------|
| S (Excellent) | ≥ 90 | 测试覆盖充分，核心模块全部达标 |
| A (Good) | 80-89 | 主要模块达标，有少量测试缺口 |
| B (Fair) | 70-79 | 存在明显覆盖缺口，需补充测试用例 |
| F (Failed) | < 70 | 覆盖严重不足，禁止发布/合入 |

---

## Checklist

### 1. 行覆盖率检查 (6项)

- [ ] **TCA-LC-001**: 核心模块行覆盖率 ≥ 90%，所有核心包/目录均已覆盖
- [ ] **TCA-LC-002**: 非核心模块行覆盖率 ≥ 70%，豁免模块有审批记录
- [ ] **TCA-LC-003**: 覆盖率报告排除规则已配置（排除自动生成代码、Lombok、Protobuf、测试框架代码）
- [ ] **TCA-LC-004**: 新增代码文件的覆盖率 ≥ 目标值（新增文件无 0% 覆盖情况）
- [ ] **TCA-LC-005**: 行覆盖率趋势持续 3 个迭代稳定或增长（无下降趋势）
- [ ] **TCA-LC-006**: 行覆盖率 < 50% 的文件有风险评估和改进计划

### 2. 分支覆盖率检查 (6项)

- [ ] **TCA-BC-001**: 核心模块分支覆盖率 ≥ 85%，if/else/switch/三元运算符分支已覆盖
- [ ] **TCA-BC-002**: 关键业务逻辑分支（权限/状态机/金额计算）分支覆盖达 100%
- [ ] **TCA-BC-003**: 异常捕获分支（catch 块）至少有 1 条测试覆盖
- [ ] **TCA-BC-004**: 循环体中的条件分支在循环不同次数下已验证
- [ ] **TCA-BC-005**: 多条件组合（复合 if 条件中的 &&/||）的各短路路径已覆盖
- [ ] **TCA-BC-006**: 分支覆盖率与行覆盖率比值 ≥ 0.85（分支覆盖接近行覆盖水平）

### 3. 函数覆盖率检查 (5项)

- [ ] **TCA-FC-001**: 核心模块函数覆盖率 ≥ 95%，所有 public 方法有测试
- [ ] **TCA-FC-002**: private 方法通过调用它的 public 方法间接覆盖
- [ ] **TCA-FC-003**: 构造函数和初始化方法已覆盖（特殊参数/依赖注入路径）
- [ ] **TCA-FC-004**: 未被覆盖的遗留函数有 JIRA Ticket 跟踪，并有计划的补充进度
- [ ] **TCA-FC-005**: 新开发的接口/抽象类的所有实现类均有测试覆盖

### 4. 变更覆盖率检查 (6项)

- [ ] **TCA-CC-001**: PR/MR 变更代码的变更覆盖率 ≥ 85%
- [ ] **TCA-CC-002**: 变更覆盖率门禁在 CI 中配置为 mandatory check（阻塞合入）
- [ ] **TCA-CC-003**: 变更覆盖报告中标红（未覆盖）的变更行已人工审查，判断风险可接受或补充测试
- [ ] **TCA-CC-004**: 仅修改测试代码/配置/文档的 PR 不触发变更覆蓋率门禁
- [ ] **TCA-CC-005**: 变更覆盖率的豁免需 Team Lead 审批，设置有效期（≤ 5 个工作日）
- [ ] **TCA-CC-006**: 变更覆盖率数据在每个合入 PR 的评论中自动展示

### 5. 覆盖率趋势监控检查 (4项)

- [ ] **TCA-MON-001**: 覆盖率数据在 CI 流水线中自动采集并存入时序数据库（或覆盖率管理平台）
- [ ] **TCA-MON-002**: 覆盖率趋势仪表盘展示行/分支/函数/变更覆盖率的历史变化曲线
- [ ] **TCA-MON-003**: 覆盖率下降超过 2% 时触发告警通知 QA 负责人
- [ ] **TCA-MON-004**: 每周/每迭代自动生成覆盖率简报，发送给开发团队

---

## Report Template

```markdown
# 测试覆盖率分析报告

## 概要

| 项目 | 值 |
|------|-----|
| 分析对象 | [项目/模块] |
| 分析日期 | YYYY-MM-DD |
| 代码语言 | [Java/Python/Go/TS] |
| 覆盖率工具 | [JaCoCo/coverage.py/Istanbul/Go cover] |
| 总代码行数 | [N] (排除豁免代码) |
| 综合评分 | [XX.X] 分 / 100 |
| 等级判定 | [S/A/B/F] |

## 四维覆盖率

| 维度 | 实际值 | 目标值 (核心模块) | 权重 | 加权得分 |
|------|--------|--------------------|------|----------|
| 行覆盖率 | XX.X% | ≥ 90% | 25% | XX.X |
| 分支覆盖率 | XX.X% | ≥ 85% | 30% | XX.X |
| 函数覆盖率 | XX.X% | ≥ 95% | 15% | XX.X |
| 变更覆盖率 | XX.X% | ≥ 85% | 30% | XX.X |
| **总分** | | | **100%** | **XX.X** |

## 模块覆盖率明细

| 模块 | 层级 | 行覆盖率 | 分支覆盖率 | 函数覆盖率 | 缺口分析 |
|------|------|----------|------------|------------|----------|
| module-a | Core | XX.X% | XX.X% | XX.X% | [高风险区域] |
| module-b | Non-core | XX.X% | XX.X% | XX.X% | [可接受] |
| module-c | Exempt | — | — | — | 自动生成代码 |

## 覆盖率缺口 Top 10 文件

| 文件 | 行覆盖率 | 未覆盖行数 | 未覆盖分支数 | 风险等级 | 改进建议 |
|------|----------|------------|--------------|----------|----------|
| | XX% | N | N | High | 补充测试 |

## 覆盖率趋势 (近 3 个迭代)

| 迭代 | 行覆盖率 | 分支覆盖率 | 函数覆盖率 | 变更覆盖率 |
|------|----------|------------|------------|------------|
| Sprint N-2 | XX% | XX% | XX% | XX% |
| Sprint N-1 | XX% | XX% | XX% | XX% |
| Sprint N | XX% | XX% | XX% | XX% |

## 改进计划

| # | 缺口描述 | 优先级 | 责任人 | 计划完成 | 状态 |
|---|----------|--------|--------|----------|------|
| 1 | 补充 XXX 模块的分支测试 | P1 | | | |

---

## Revision History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | YYYY-MM-DD | Initial report | 评估团队 |
```

---

## 相关评估

- [coverage-analysis.md](../evaluations/coverage-analysis.md)
- [regression-test-suite.md](../evaluations/regression-test-suite.md)
- [code-quality-checklist.md](../evaluations/code-quality-checklist.md)
- [acceptance-criteria-review.md](../evaluations/acceptance-criteria-review.md)
