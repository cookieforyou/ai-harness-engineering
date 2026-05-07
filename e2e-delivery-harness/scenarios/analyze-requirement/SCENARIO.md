---
name: analyze-requirement
description: "需求分析场景，负责将原始业务需求转换为结构化的需求规格说明书"
version: "1.2.0"
type: scenario
category: analysis
stage: requirement-analysis
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: [analysis, requirements, stakeholder]
---
# Analyze Requirement

## Purpose

将原始业务需求转换为结构化的需求规格说明书，确保需求的完整性、一致性和可追溯性。

### Business Value

- **降低需求风险**: 通过系统化分析识别模糊和冲突的需求，避免后期返工
- **提升干系人满意度**: 全面识别干系人诉求，确保关键需求不被遗漏
- **建立清晰基线**: 形成可追溯、可验证的需求基线，为后续设计和开发提供明确输入
- **提高交付质量**: 明确的验收标准和非功能需求定义，减少交付偏差

## Chain of Thought

> AI 执行时的思维引导，帮助逐步完成需求分析工作

### Think-Aloud Protocol (强制遵循)

```
[THINK] Step 1: 理解业务背景和目标
   ├─ 问：业务背景和核心目标是什么？需求解决的痛点或机会是什么？
   ├─ 验证：与业务方确认理解准确性
   └─ 检查：业务目标是否SMART（具体、可衡量、可达成、相关、有时限）
   ↓
[ANALYZE] Step 2: 识别干系人和诉求
   ├─ 问：谁是主要干系人？他们各自的诉求和期望是什么？
   ├─ 验证：列出干系人矩阵，评估影响力和优先级
   └─ 检查：是否覆盖所有关键干系人类型（决策者、使用者、影响者、监管者）
   ↓
[GATHER] Step 3: 收集和整理需求
   ├─ 问：收集到的需求是否完整？功能需求与非功能需求是否都覆盖？
   ├─ 验证：需求覆盖所有业务场景和用户旅程
   └─ 检查：使用"As a... I want... so that..."格式规范化需求描述
   ↓
[MODEL] Step 4: 构建业务模型
   ├─ 问：业务流程是否清晰？关键决策点和异常处理是否明确？
   ├─ 验证：绘制业务流程图和用例模型
   └─ 检查：流程边界清晰，无遗漏的关键路径
   ↓
[SPECIFY] Step 5: 编写需求规格
   ├─ 问：每条需求是否符合SMART原则？验收标准是否可测试？
   ├─ 验证：需求可追溯到业务目标，验收标准可量化
   └─ 检查：非功能需求完整（性能、安全、可用性、可维护性）
   ↓
[VALIDATE] Step 6: 与干系人确认并准备交接
   ├─ 组织评审会议，收集反馈
   ├─ 根据反馈修订需求文档
   └─ 获得干系人签字确认，准备交接给系统设计阶段
```



## Decision Checkpoints

| ID | 决策点 | 触发条件 | 决策选项 | 选择标准 | 记录位置 |
|----|--------|----------|----------|----------|----------|
| DC-001 | 干系人确认完整性 | 干系人识别完成后 | 已覆盖所有关键角色 / 存在遗漏风险 | 必须覆盖决策者、使用者、影响者三类 | 干系人分析报告 |
| DC-002 | 需求模糊处理 | 发现需求描述不清晰时 | 主动澄清 / 基于假设标注 / 标记为待确认 | 优先主动澄清，无法澄清时明确标注假设 | 需求规格说明书 |
| DC-003 | 需求冲突解决 | 不同干系人诉求矛盾时 | 协商折中方案 / 高层拍板 / 分阶段实现 | 评估业务价值和影响范围，寻求共赢方案 | 冲突解决记录 |
| DC-004 | 优先级排序 | 需求列表完成后 | P0(核心) / P1(重要) / P2(次要) / P3(可选) | 基于业务价值、紧急程度、依赖关系综合评估 | 需求优先级矩阵 |
| DC-005 | 非功能需求定义 | 功能需求确认后 | 根据系统类型确定NFR范围和指标 | 参考行业标准和类似项目经验值 | 非功能需求章节 |

## Error Handling (错误处理)

> **AI 遇到以下情况时必须按指定流程处理**

### Error Scenario 1: 需求模糊不清

**识别信号**: 
- 需求描述使用“大概”、“可能”、“最好能”等模糊词汇
- 同一需求存在多种理解方式
- 缺乏具体的业务场景或用户故事支撑

**处理流程**:
```
IF 检测到需求模糊
THEN
  1. 列出所有可能的理解方式（至少2种）
  2. 为每种理解方式生成假设和业务场景
  3. 主动向业务方提出澄清问题（最多3轮）
  4. IF 仍无法澄清 THEN 在文档中标注 [需要确认] 并说明各种可能性
  5. 记录决策依据和假设前提
END
```

**降级方案**: 基于最常见业务场景做出合理假设，但必须在文档中明确标注为“假设”，并在评审时重点确认

**升级条件**: 经过3轮澄清后业务方仍无法明确需求，升级到产品负责人或项目发起人决策

---

### Error Scenario 2: 干系人诉求冲突

**识别信号**: 
- 不同干系人对同一功能有相反要求
- 资源分配存在竞争关系
- 优先级排序出现明显分歧

**处理流程**:
```
IF 检测到干系人冲突
THEN
  1. 识别冲突的具体点和涉及的干系人
  2. 分析各方诉求背后的业务目标和利益考量
  3. 提出折中方案（至少2个备选方案）
  4. 组织冲突解决会议，引导达成共识
  5. IF 无法达成共识 THEN 升级到更高层级决策者拍板
  6. 记录最终决策和理由
END
```

**降级方案**: 暂时搁置冲突需求，先推进无争议部分，同时安排专项会议解决冲突

**升级条件**: 经过2轮协商仍无法达成共识，或冲突涉及核心业务目标

---

### Error Scenario 3: 需求范围蔓延

**识别信号**: 
- 新增需求超出原定业务范围
- 需求复杂度持续增加，超出团队产能
- 频繁出现“顺便也做一下...”类需求

**处理流程**:
```
IF 检测到范围蔓延
THEN
  1. 标记新增需求，与原定范围对比
  2. 评估新增需求对进度、成本、质量的影响
  3. 与产品负责人确认：纳入当前迭代 or 放入后续迭代
  4. IF 纳入当前迭代 THEN 调整计划，移除低优先级需求保持平衡
  5. IF 放入后续迭代 THEN 记录到需求池，更新路线图
  6. 更新范围基线文档
END
```

**降级方案**: 将新增需求记录到“未来考虑”清单，不影响当前迭代计划

**升级条件**: 新增需求影响超过20%原定范围，或导致关键里程碑延期



## Quality Metrics

### Key Performance Indicators (KPIs)

| KPI ID | 指标名称 | 目标值 | 计算公式 | 验证方法 | 权重 |
|--------|----------|--------|----------|----------|------|
| KPI-001 | REQ-COVERAGE | ≥95% | (已分析需求数/总需求数) × 100% | 需求清单核对 | 25% |
| KPI-002 | STAKEHOLDER-ID | 100% | (已识别关键干系人/实际关键干系人) × 100% | 干系人矩阵检查 | 20% |
| KPI-003 | AC-CLARITY | ≥90% | (有明确验收标准的需求数/总需求数) × 100% | 验收标准审查 | 20% |
| KPI-004 | TRACEABILITY | 100% | (可追溯到业务目标的需求数/总需求数) × 100% | 追溯矩阵检查 | 20% |
| KPI-005 | CONFLICT-RESOLUTION | ≤5% | (未解决冲突数/总冲突数) × 100% | 冲突解决记录 | 15% |

**综合评分计算**: 
```
Quality Score = (KPI-001 × 0.25) + (KPI-002 × 0.20) + (KPI-003 × 0.20) + (KPI-004 × 0.20) + (KPI-005 × 0.15)
合格: ≥70分 | 优秀: ≥85分 | 卓越: ≥95分
```

### Validation Checklist (验证清单)

**完整性验证 (Completeness)**:
- [ ] 所有必需章节已完成（业务背景、干系人、功能需求、非功能需求、用例模型）
- [ ] 每个功能需求都有明确的验收标准
- [ ] 非功能需求覆盖性能、安全、可用性等关键维度
- [ ] 业务流程图完整，包含主要路径和异常处理

**一致性验证 (Consistency)**:
- [ ] 术语和命名在整个文档中保持一致
- [ ] 需求之间无逻辑冲突或矛盾
- [ ] 需求与业务目标保持一致
- [ ] 与其他相关文档（如架构设计）协调一致

**准确性验证 (Accuracy)**:
- [ ] 业务理解经干系人确认无误
- [ ] 数据流和业务流程描述准确
- [ ] 技术约束和假设合理且已标注
- [ ] 链接和引用有效

**可测试性验证 (Testability)**:
- [ ] 每条需求都可转化为具体的测试用例
- [ ] 验收标准使用可量化的指标
- [ ] 边界条件和异常场景已考虑
- [ ] 测试数据和预期结果明确

**规范性验证 (Compliance)**:
- [ ] 遵循需求编写最佳实践（SMART原则、用户故事格式）
- [ ] 符合组织的需求管理规范
- [ ] 满足行业标准和合规要求



## Handover Criteria

```
✅ 需求规格说明书已完成
✅ 干系人分析报告已输出
✅ 业务流程图已绘制
✅ 用例模型已构建
✅ 需求已评审通过
✅ 所有疑问已澄清
```

### Handover Context Template

```yaml
handover:
  header:
    from_stage: "requirement-analysis"
    to_stage: "system-design"
    handover_id: "HO-{{timestamp}}-{{sequence}}"
    timestamp: "{{ISO8601}}"
    prepared_by: "{{agent.name}}"
    
  summary:
    status: "completed/partial/blocked"
    completion_percentage: {{0-100}}
    quality_score: {{0-100}}
    
  artifacts:
    delivered:
      - name: "{{artifact_name}}"
        path: "{{file_path}}"
        version: "{{version}}"
        checksum: "{{SHA256}}"
      
  decisions:
    - id: "DC-XXX"
      description: "{{决策描述}}"
      rationale: "{{决策理由}}"
      alternatives_considered: ["选项1", "选项2"]
      
  open_issues:
    blocking: []
    non_blocking:
      - id: "ISSUE-XXX"
        description: "{{问题描述}}"
        
  risks:
    - id: "RISK-XXX"
      description: "{{风险描述}}"
      probability: "low/medium/high"
      impact: "low/medium/high"
      mitigation: "{{缓解措施}}"
      
  recommendations:
    - "{{建议1}}"
    - "{{建议2}}"
    
  quality_metrics:
    kpi_results:
      - kpi_id: "KPI-001"
        value: {{actual_value}}
        target: {{target_value}}
        status: "pass/fail"
```
## Related Assets (关联资产)

| Asset Type | Path | Description |
|------------|------|-------------|
| Agent | `../../agents/analyze-requirement.agent.md` | 需求分析Agent角色定义 |
| Prompt | `../../prompts/analyze-requirement.prompt.md` | 需求分析提示词模板 |
| Skill | `../../skills/analyze-requirement/SKILL.md` | 需求分析技能包 |
| Instruction | `../../instructions/analyze-requirement.instructions.md` | 需求分析技术指令 |

## Related Resources (相关资源)

- **Standards**: 
  - [SMART Criteria](../standards/smart-criteria.md) - 需求编写标准
  - [User Story Format](../standards/user-story-format.md) - 用户故事格式规范
- **Templates**: 
  - [Requirements Specification Template](../templates/requirements-spec.template.md) - 需求规格说明书模板
  - [Stakeholder Analysis Template](../templates/stakeholder-analysis.template.md) - 干系人分析模板
- **Evaluations**: 
  - [Requirement Quality Checklist](../evaluations/requirement-quality-checklist.md) - 需求质量检查清单

## Prerequisites

### 必需前置条件

1. 业务方提出需求请求
2. 具备项目背景信息
3. 可联系到关键干系人

### 期望输入

| 输入项 | 必填 | 描述 |
|--------|------|------|
| `project_name` | 是 | 项目名称 |
| `raw_requirements` | 是 | 原始需求描述 |
| `stakeholders` | 否 | 已知干系人列表 |
| `business_context` | 否 | 业务背景信息 |
