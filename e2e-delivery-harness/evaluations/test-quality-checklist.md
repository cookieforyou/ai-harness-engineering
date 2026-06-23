---
name: test-quality-checklist
type: evaluation
version: "1.0.0"
status: active
description: "测试质量清单，用于评估测试用例的覆盖率、有效性和执行效率"
author: AI Harness Engineering Team
created: 2026-06-23
updated: 2026-06-23
tags: ['evaluation', 'test', 'quality', 'checklist']
---

# 测试质量检查清单 (Test Quality Checklist)

## Purpose

本清单用于评估测试活动的整体质量，涵盖测试用例质量、覆盖率、缺陷质量与自动化质量四个核心维度。适用于测试计划评审、测试执行阶段评估和测试准出门禁。

## Scoring

- **PASS**: 完全满足要求
- **PARTIAL**: 大部分满足，少量偏差可接受
- **FAIL**: 不满足要求，必须改进
- **NA**: 不适用

## 使用时机

- 测试计划编写完成后评审
- 测试执行阶段质量评估
- 测试准出前的最终核查

---

## 1. 测试用例质量 (Test Case Quality)

- [ ] **TCQ-001**: 每条测试用例有唯一 ID（TC-*），标题清晰描述被测场景和预期结果
- [ ] **TCQ-002**: 测试步骤完整、可执行（新工程师按步骤可独立执行，无需额外解释）
- [ ] **TCQ-003**: 测试数据已预定义（输入值、期望值、前置条件），无"使用测试数据"这种模糊描述
- [ ] **TCQ-004**: 等价类划分与边界值分析已应用：每个输入字段至少覆盖有效等价类、无效等价类、边界值
- [ ] **TCQ-005**: 异常场景覆盖率 ≥ 60%（网络超时、服务降级、非法输入、并发冲突等场景）
- [ ] **TCQ-006**: 测试用例与需求的追溯矩阵完整（每条 REQ 至少对应 1 条 TC，核心需求 ≥ 3 条 TC）
- [ ] **TCQ-007**: 测试用例通过评审（reviewer 非编写者），评审记录可查

## 2. 覆盖率分析 (Coverage Analysis)

- [ ] **TCA-001**: 代码行覆盖率 ≥ 80%（核心模块 ≥ 90%），覆盖率数据来自 CI 构建报告
- [ ] **TCA-002**: 分支覆盖率 ≥ 70%（if/else/switch/case 分支覆盖），未覆盖分支有正当理由
- [ ] **TCA-003**: 接口/API 覆盖率 100%（所有对外暴露的 REST/gRPC 端点至少有一个正向测试用例）
- [ ] **TCA-004**: 需求覆盖率 100%（所有功能需求和非功能需求均已映射到测试用例）
- [ ] **TCA-005**: 覆盖率趋势分析：本次覆盖率不低于上个版本的覆盖率（允许 ≤ 2% 的合理波动）
- [ ] **TCA-006**: 新增代码覆盖率 ≥ 85%（本次迭代新增/修改的代码行）

## 3. 缺陷质量 (Defect Quality)

- [ ] **TDF-001**: 每条缺陷有唯一编号（BUG-*），标题格式为"[模块] 场景描述: 具体问题"
- [ ] **TDF-002**: 缺陷可复现：包含复现步骤、环境信息（OS/浏览器/版本）、前置条件和截图/日志附件
- [ ] **TDF-003**: 缺陷分级正确：P0（阻塞/崩溃）→ 立即修复、P1（功能不可用）→ 本迭代、P2（次要功能异常）→ 可延期
- [ ] **TDF-004**: 缺陷与根因关联：每条缺陷标记了根因分类（代码错误/配置错误/设计缺陷/环境问题/需求问题）
- [ ] **TDF-005**: 缺陷修复验证标准明确：修复验证包含"确认修复"和"确认未引入回归"两个步骤
- [ ] **TDF-006**: 缺陷关闭前已由测试人员验证通过，非开发人员自行关闭

## 4. 自动化质量 (Automation Quality)

- [ ] **TAU-001**: 自动化测试用例与手工用例分离管理，CI 流水线仅执行自动化用例
- [ ] **TAU-002**: 自动化测试稳定性 ≥ 95%（非 flaky：连续运行 5 次结果一致）
- [ ] **TAU-003**: 自动化测试执行时间 ≤ 30 分钟（全量回归套件），超过需分层（快速层 + 完整层）
- [ ] **TAU-004**: UI 自动化测试使用了稳定 selector（data-testid/aria-label），非 CSS class 或 XPath 位置
- [ ] **TAU-005**: 测试代码经过代码评审，遵循同样的编码规范（无重复代码、硬编码等反模式）
- [ ] **TAU-006**: 测试数据清理机制完善：每个测试执行后恢复初始状态，无测试间数据污染
- [ ] **TAU-007**: CI 流水线中失败用例自动通知相关人员，且失败原因分析 ≤ 1 小时

---

## Summary

| 维度 | PASS | PARTIAL | FAIL | 通过率 |
|------|------|---------|------|--------|
| 测试用例质量 | __ | __ | __ | __% |
| 覆盖率分析 | __ | __ | __ | __% |
| 缺陷质量 | __ | __ | __ | __% |
| 自动化质量 | __ | __ | __ | __% |
| **总计** | **__** | **__** | **__** | **__%** |

### 判定标准

| 通过率 | 结果 |
|--------|------|
| ≥ 90% | PASS - 测试质量良好，可准出 |
| 75-89% | PARTIAL - 关键项修复后准出 |
| < 75% | FAIL - 测试不充分，禁止准出 |

### 测试准出判定

- [ ] 可准出（所有 P0/P1 缺陷已修复验证）
- [ ] 有条件准出（缺陷列表附后，不影响核心功能）
- [ ] 不可准出（存在未修复的 P0 缺陷）

### 关键指标

| 指标 | 实际值 | 目标值 | 状态 |
|------|--------|--------|------|
| 用例执行率 | __% | ≥ 95% | PASS/PARTIAL/FAIL |
| 用例通过率 | __% | ≥ 95% | PASS/PARTIAL/FAIL |
| P0 缺陷修复率 | __% | 100% | PASS/PARTIAL/FAIL |
| 自动化通过率 | __% | ≥ 90% | PASS/PARTIAL/FAIL |

---

## References

- [regression-checklist.md](regression-checklist.md)
- [regression-test-suite.md](regression-test-suite.md)
- [coverage-analysis.md](coverage-analysis.md)
- [test-coverage-analysis.md](test-coverage-analysis.md)
- [defect-analysis.md](defect-analysis.md)
- [standards/harness-engineering.md](../standards/harness-engineering.md)

## 相关评估

- [regression-checklist.md](regression-checklist.md) — 回归检查清单
- [code-quality-checklist.md](code-quality-checklist.md) — 代码质量清单
- [deployment-quality-checklist.md](deployment-quality-checklist.md) — 部署质量清单
- [coverage-analysis.md](coverage-analysis.md) — 覆盖率分析
