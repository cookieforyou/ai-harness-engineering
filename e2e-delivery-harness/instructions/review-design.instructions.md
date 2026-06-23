---
name: review-design
description: "Detailed technical instructions for review-design scenario execution"
applyTo: "scenarios/review-design/**"
phase: system-design
type: instruction
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-23
status: active
tags: ['instruction', 'technical']
---
# Instruction: 技术方案评审技术规范

## Overview

This instruction establishes the comprehensive technical standards and evaluation criteria for reviewing system and software design artifacts within the E2E delivery lifecycle. It covers design completeness assessment, quality attribute validation, security and scalability review dimensions, ADR evaluation, and traceability verification against requirements. The instruction ensures designs are reviewed systematically with measurable quality gates, capturing risks early before implementation investment.


## Review Dimensions

| 维度 | 评审要点 | 权重 |
|------|----------|------|
| 需求匹配 | 满足业务需求 | 20% |
| 技术可行性 | 技术方案可行 | 20% |
| 安全性 | 安全风险可控 | 20% |
| 性能 | 性能满足要求 | 15% |
| 可维护性 | 易于维护 | 15% |
| 成本 | 成本合理 | 10% |

## Associated Assets

- **Scenario**: `scenarios/review-design/SCENARIO.md`
- **Prompt**: `prompts/review-design.prompt.md`
- **Agent**: `agents/review-design.agent.md`
- **Skill**: `skills/review-design/SKILL.md`


## Review Process (评审流程)

### Phase 1: 评审准备 (Preparation)

**输入**: 设计文档（架构设计、技术方案、ADR）、需求规格说明书

**操作步骤**:
1. 确认评审范围和类型（架构评审/详细设计评审/接口评审）
2. 分配评审角色：主持人、设计方、评审员（至少 2 人）、记录员
3. 提前 48 小时分发设计文档给评审员
4. 评审员提前阅读并标注问题点
5. 收集预评审问题，判断是否需要取消或延期（如文档质量过低）

**产出**: 评审议程、预评审问题清单

### Phase 2: 评审执行 (Execution)

**标准会议议程** (60 分钟):

| 时间段 | 内容 | 负责人 |
|--------|------|--------|
| 0:00-0:05 | 介绍评审目标和范围 | 主持人 |
| 0:05-0:20 | 设计方讲解设计方案（架构图、数据流、接口、关键决策） | 设计方 |
| 0:20-0:45 | 逐维度讨论（需求匹配→技术可行性→安全性→性能→可维护性→成本） | 全体 |
| 0:45-0:55 | 汇总问题、确认严重程度、给出评审结论 | 主持人 |
| 0:55-1:00 | 确认待办项、责任人、时间线 | 记录员 |

**产出**: 评审问题清单、评审结论

### Phase 3: 问题分级与记录

使用标准化严重程度分级：

```yaml
severity_levels:
  P0_Critical:
    label: "阻塞 (Critical)"
    criteria: "方案不可行、安全漏洞、核心需求不满足"
    action: "必须修复后重新评审"
  P1_Major:
    label: "严重 (Major)"
    criteria: "性能不达标、数据一致性问题、关键模块设计缺失"
    action: "必须修复，修复后可变更确认"
  P2_Minor:
    label: "一般 (Minor)"
    criteria: "接口可优化、异常处理缺失、文档不完整"
    action: "建议修复或记录待办"
  P3_Suggestion:
    label: "建议 (Suggestion)"
    criteria: "可选的优化建议"
    action: "可选择性采纳"
```

### Phase 4: 评审报告输出

评审报告模板：

```markdown
# 技术方案评审报告

## 基本信息
- 评审日期: {date}
- 设计文档: {document_name} v{version}
- 设计方: {presenter}
- 评审员: {reviewers}
- 评审类型: {review_type}

## 评审结论
**结论**: 通过 / 有条件通过 / 不通过
**条件** (如有): {conditions}

## 评审统计
- 总发现问题: {total_issues}
- P0 Critical: {p0_count}
- P1 Major: {p1_count}
- P2 Minor: {p2_count}
- P3 Suggestion: {p3_count}

## 问题详情
| ID | 严重程度 | 问题描述 | 建议方案 | 责任人 | 目标日期 | 状态 |
|----|---------|---------|---------|--------|---------|------|
| RV-001 | P1 | {description} | {suggestion} | {owner} | {date} | Open |

## 质量属性评估
| 维度 | 评分(1-5) | 评价 | 风险 |
|------|----------|------|------|
| 需求匹配 | {score} | {comment} | {risk} |
| 技术可行性 | {score} | {comment} | {risk} |
| 安全性 | {score} | {comment} | {risk} |
| 性能 | {score} | {comment} | {risk} |
| 可维护性 | {score} | {comment} | {risk} |
| 成本 | {score} | {comment} | {risk} |

## 后续行动
- {action_items}
```

## Per-Dimension Review Checklist

### 需求匹配 (Requirements Alignment)
- [ ] 所有 P0 功能需求都有对应的设计方案
- [ ] 非功能性需求有量化的设计方案
- [ ] 需求-设计追溯矩阵完整
- [ ] 业务边界和范围与需求一致
- [ ] 验收标准可验证

### 技术可行性 (Technical Feasibility)
- [ ] 技术选型有充分的评估和对比
- [ ] 技术方案在团队能力范围内（或已规划培训/招聘）
- [ ] 关键技术风险已识别并有缓解措施
- [ ] 依赖的外部服务/组件版本明确且可用
- [ ] POC 结果（如有）支持方案可行性

### 安全性 (Security)
- [ ] 认证和授权方案明确
- [ ] 敏感数据传输和存储加密方案明确
- [ ] 输入校验和防注入方案到位
- [ ] 审计日志方案完整
- [ ] 第三方依赖无已知高危漏洞
- [ ] 符合相关合规要求（GDPR/SOC2/PCI-DSS等）

### 性能 (Performance)
- [ ] 有明确的性能目标（P99延迟、TPS、并发用户数）
- [ ] 容量估算有数据支撑
- [ ] 缓存策略明确且合理
- [ ] 数据库查询有索引设计
- [ ] 瓶颈识别和消解方案到位

### 可维护性 (Maintainability)
- [ ] 模块划分遵循 SOLID 原则
- [ ] 依赖方向合理（无循环依赖）
- [ ] 接口设计稳定、向后兼容
- [ ] 异常处理策略完整
- [ ] 日志和监控设计到位
- [ ] 文档充分（ADR + 架构图 + API文档）

### 成本 (Cost)
- [ ] 技术选型考虑许可证成本
- [ ] 基础设施成本估算合理
- [ ] 运维人力成本已考虑
- [ ] 与更简单方案的性价比对比

## Technical Specifications

> Detailed technical requirements and implementation guidelines for review-design.

### Required Tools

| 工具类别 | 推荐工具 | 用途 |
|----------|----------|------|
| 文档平台 | Confluence/Notion/Google Docs | 设计文档编写和共享 |
| 架构图工具 | Draw.io/PlantUML/Structurizr | 架构图审核 |
| 设计协作 | Miro/Figma/Excalidraw | 实时协作评审 |
| 决策记录 | ADR 工具 (adr-tools/Log4brains) | 架构决策记录评审 |
| 静态分析 | SonarQube/Checkstyle | 设计方案质量检查 |
| 安全扫描 | Snyk/Checkmarx | 安全设计审查 |

### Environment Requirements

- 设计文档存储于团队可访问的共享文档平台
- 架构图使用标准符号（C4 Model、UML）
- 评审记录和决策需要长期保存供审计
- 敏感设计内容需要设置访问权限

### Configuration Parameters

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `review_preparation_hours` | number | 48 | 评审资料提前发布时间（小时） |
| `max_review_duration_days` | number | 2 | 评审最大周转天数 |
| `min_reviewers_count` | number | 2 | 最少评审人数 |
| `required_security_review` | boolean | true | 是否需要安全评审 |
| `required_performance_review` | boolean | true | 是否需要性能评审 |
| `max_p0_allowed` | number | 0 | 允许的最大 P0 问题数 |
| `max_p1_allowed` | number | 3 | 允许的最大 P1 问题数 |

## 审批工作流 (Approval Workflow)

```yaml
approval_workflow:
  step_1: "设计方提交设计文档"
    提交物:
      - "设计文档 (Design Document)"
      - "ADR 记录 (Architecture Decision Records)"
      - "需求追溯矩阵 (Requirements Traceability Matrix)"
    
  step_2: "评审组预审"
    操作:
      - "评审员在 48 小时内预读文档"
      - "标注问题和疑问"
    条件:
      - "至少 2 名评审员完成预审"
    
  step_3: "评审会议"
    操作:
      - "按议程召开评审会议"
      - "记录发现的问题"
    条件:
      - "至少 2 名评审员参会"
    
  step_4: "评审结论"
    操作:
      - "得出评审结论"
      - "24 小时内发布评审报告"
    结论类型:
      - "通过 (Approved) → 进入开发阶段"
      - "有条件通过 (Approved w/ Conditions) → 跟踪条件完成"
      - "不通过 (Rejected) → 修订后重新提交"
    
  step_5: "跟踪闭环"
    操作:
      - "有条件通过的问题跟踪"
      - "待改进项的定期复查"
      - "修复完成后变更确认"
```

## Error Handling

### Error Scenario 1: 设计文档质量不足
**症状**: 设计文档缺失关键章节、无架构图、接口定义不完整，评审员无法理解方案
**根因**: 设计方准备不充分，或缺乏设计文档模板指导
**处理**:
1. 主持人判定文档质量是否达到评审门槛
2. 如不达标，取消评审会议，退回设计方补充
3. 给出具体的补全清单和时间要求
4. 设计方在 48 小时内补全并重新发起评审
**升级条件**: 同一设计文档被退回 3 次，升级到技术负责人介入

### Error Scenario 2: 评审意见分歧
**症状**: 设计方和评审员对某个设计决策存在重大分歧，双方各执一词
**根因**: 缺乏客观的评估标准，或对需求/约束的理解不一致
**处理**:
1. 双方列出各自的论据和担忧
2. 引入第三方专家（架构委员会）进行仲裁
3. 如涉及需求理解，回溯需求规格澄清
4. 记录决策和分歧理由到 ADR
**升级条件**: 分歧导致设计超过 3 天无进展，升级到技术负责人决策

### Error Scenario 3: 评审问题长期未关闭
**症状**: 评审中记录的问题超过预定时间未修复或未确认
**根因**: 缺乏问题跟踪机制，或责任人优先级冲突
**处理**:
1. 建立评审问题跟踪表（Issue Tracker）
2. 每周回顾未关闭问题
3. 对超期问题升级到团队 Leader
4. P0/P1 问题阻塞下游阶段的，优先处理
**升级条件**: P0 问题超过 48h 未修复，P1 超过 1 周未修复

## Quality Standards

| 标准 | 指标 | 目标值 | 验证方法 |
|------|------|--------|---------|
| 问题发现率 | ISSUE-DETECTION | ≥95% | (评审发现的问题数 / 实际总问题数) × 100%，通过后续阶段发现的逃逸问题回溯 |
| 评审周期 | REVIEW-TURNAROUND | ≤2 个工作日 | 从发起评审到给出评审结论的时间 |
| 问题逃逸率 | DEFECT-ESCAPE | ≤5% | (评审后才发现的问题 / 总问题数) × 100% |
| 问题关闭率 | ISSUE-CLOSURE | ≥90% | (已关闭的评审问题 / 总评审问题) × 100%，30天内统计 |
| 评审覆盖率 | REVIEW-COVERAGE | 100% | 所有 P0 设计决策必须经过正式评审 |
| 评审参与度 | REVIEWER-COUNT | ≥2 人 | 每次评审至少有 2 名独立评审员参与 |

**综合质量评分**:
```
Quality Score = (ISSUE-DETECTION × 0.30) + (REVIEW-TURNAROUND × 0.20) + (DEFECT-ESCAPE × 0.25) + (ISSUE-CLOSURE × 0.15) + (REVIEW-COVERAGE × 0.10)
合格: ≥70分 | 优秀: ≥85分 | 卓越: ≥95分
```
## References

- [harness-engineering.md](../standards/harness-engineering.md)
- [output-validation-checklist.md](../evaluations/output-validation-checklist.md)
- [regression-checklist.md](../evaluations/regression-checklist.md)
