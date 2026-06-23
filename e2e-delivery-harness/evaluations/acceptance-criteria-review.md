---
name: acceptance-criteria-review
type: evaluation
version: "1.1.0"
status: active
language: "zh-CN"
updated: 2026-06-23
description: >
  验收标准审查清单，覆盖AC完整性、可测性、清晰度和商业价值对齐四个维度。
  确保每一条 Given-When-Then 满足可验证、可执行、可观测的要求，P0需求AC覆盖率达100%。
---

# 验收标准审查清单 (Acceptance Criteria Review)

## Overview

验收标准审查清单用于评审用户故事/需求的验收标准（AC）质量，确保每一条 AC 满足完整性、可测性、清晰度和商业价值对齐四个维度的要求。本清单适用于需求评审阶段、Sprint 规划会议以及开发前的最终验收。

### 适用场景

- 需求分析阶段 AC 编写完成后自检
- Backlog Refinement 会议中的 AC 评审
- 开发团队接收需求前的 QA 准入检查
- 测试用例（TC）编写前的 AC 基线确认

### 使用指南

1. **评审时机**：AC 编写完成后、开发任务开始前逐条评审
2. **参与角色**：Product Owner + QA + Developer 三方共同评审
3. **判定标准**：每项检查标记 PASS / FAIL / NA，FAIL 项必须修复
4. **准出条件**：P0 需求全部 PASS，总分 ≥ 80 方可进入开发

---

## Evaluation Criteria

| 维度 | 权重 | 目标值 | 测量方法 |
|------|------|--------|----------|
| AC完整性检查 | 30% | ≥ 90% 通过 | 逐项核查 AC 是否覆盖关键要素 |
| AC可测性检查 | 30% | ≥ 95% 可自动验证 | 评估 Then 断言是否可工具化 |
| AC清晰度检查 | 25% | 主观词数量 = 0 | 检查是否使用模糊/主观表述 |
| 商业价值对齐 | 15% | P0需求 100% 覆盖 | 追溯矩阵 AC ↔ OBJ 覆盖率 |

---

## Scoring Formula

### 加权评分

```
总分 = 完整性得分 × 30% + 可测性得分 × 30% + 清晰度得分 × 25% + 价值对齐得分 × 15%
```

### 等级划分

| 等级 | 分数范围 | 判定 |
|------|----------|------|
| S (Excellent) | 90-100 | 所有 AC 均可直接用于 TC 编写 |
| A (Good) | 80-89 | 少量改进点，修复后进入开发 |
| B (Fair) | 70-79 | 需显著改进，返工后重新评审 |
| F (Failed) | < 70 | 禁止进入开发阶段，需整体重写 |

---

## Checklist

### 1. AC 完整性检查 (5项)

- [ ] **AC-INT-001**: 每条用户故事至少包含 1 条验收标准，P0 需求至少 3 条
- [ ] **AC-INT-002**: Given 前置条件明确完整，包括用户身份、系统状态、数据前提
- [ ] **AC-INT-003**: When 触发动作具体可执行，包含操作类型和输入参数
- [ ] **AC-INT-004**: Then 期望结果包含具体可检查产物（状态码、字段值、响应时间、文件输出）
- [ ] **AC-INT-005**: 异常/边界场景存在对应 AC（错误输入、权限不足、超时、空数据）

### 2. AC 可测性检查 (5项)

- [ ] **AC-TST-001**: Then 断言可映射到具体的 HTTP 状态码/错误码/响应体字段
- [ ] **AC-TST-002**: Given 前置条件可通过 API 调用/DB 预置/Mock 服务 30 秒内准备完成
- [ ] **AC-TST-003**: 测试数据可隔离，不依赖共享数据库中的特定记录
- [ ] **AC-TST-004**: AC 不包含非功能性约束（性能/SLA 单独在 NFR 中定义）
- [ ] **AC-TST-005**: AC 执行结果具有确定性（相同输入 ⇒ 相同输出）

### 3. AC 清晰度检查 (4项)

- [ ] **AC-CLR-001**: 不使用模糊主观词：快速、友好、稳定、高效、易于、充分
- [ ] **AC-CLR-002**: 数值和时间表述具体化（非"大量""很快""若干"），使用精确数字或范围
- [ ] **AC-CLR-003**: 业务术语使用项目术语表定义，首次出现时标注定义来源
- [ ] **AC-CLR-004**: 否定条件或异常分支的 AC 明确标注"当...时"的触发条件

### 4. 商业价值对齐检查 (3项)

- [ ] **AC-BVA-001**: 每条 AC 可追溯至至少一条业务目标（OBJ-*），存在追溯矩阵
- [ ] **AC-BVA-002**: P0 (Must-have) 需求的 AC 覆盖率达到 100%，无遗漏关键流程
- [ ] **AC-BVA-003**: AC 不包含超出当前迭代范围的镀金需求（Gold-plating），已与 PO 确认

---

## Report Template

```markdown
# 验收标准审查报告

## 概要

| 项目 | 值 |
|------|-----|
| 需求/故事 | STORY-XXX: [标题] |
| 审查日期 | YYYY-MM-DD |
| 审查人 | [姓名/角色] |
| AC 总数 | [N] 条 |
| AC 通过数 | [N] 条 |
| 综合评分 | [XX.X] 分 / 100 |
| 等级判定 | [S/A/B/F] |

## 四个维度评分

| 维度 | 得分 | 权重 | 加权得分 |
|------|------|------|----------|
| AC完整性检查 | XX/100 | 30% | XX.X |
| AC可测性检查 | XX/100 | 30% | XX.X |
| AC清晰度检查 | XX/100 | 25% | XX.X |
| 商业价值对齐 | XX/100 | 15% | XX.X |
| **总分** | | **100%** | **XX.X** |

## 未通过项明细

| AC ID | 检查维度 | 问题描述 | 严重等级 | 修复建议 |
|-------|----------|----------|----------|----------|
| AC-XXX | 完整性 | Given 缺少用户登录状态 | High | 补充 "Given 用户已登录" |
| AC-XXX | 可测性 | Then 使用"系统显示成功" | High | 改为"Then 响应状态码 200" |
| AC-XXX | 清晰度 | 使用"快速"主观词 | Medium | 替换为"≤ 2秒" |

## 改进建议

1. [建议一]
2. [建议二]

---

## 修订历史

| 版本 | 日期 | 变更内容 | 责任人 |
|------|------|----------|--------|
| 1.0 | YYYY-MM-DD | 初始评审 | [姓名] |
```

---

## Related Evaluations

- [requirement-quality-checklist.md](requirement-quality-checklist.md)
- [output-validation-checklist.md](output-validation-checklist.md)
- [test-coverage-analysis.md](test-coverage-analysis.md)
- [common-error-patterns.md](common-error-patterns.md)
- [regression-checklist.md](regression-checklist.md)
- [standards/harness-engineering.md](../standards/harness-engineering.md)
