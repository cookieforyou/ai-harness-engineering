---
name: document-project
description: "Document Project scenario for the E2E delivery lifecycle"
type: scenario
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['workflow', 'process']
---
# Scenario: 项目文档 (Document Project)

## Overview

项目文档是知识管理和信息传递的关键载体，负责创建和维护项目全生命周期的技术文档。

## Core Decision Points

| 阶段 | 决策点 | 输出 |
|------|--------|------|
| 文档规划 | Doc Structure Design | 文档体系 |
| 内容创作 | Content Creation | 初稿 |
| 评审优化 | Review & Refine | 终稿 |
| 发布维护 | Publish & Maintain | 可用文档 |

## Execution Flow

```python
class ProjectDocumentation:
    """项目文档流程"""

    def execute(self, project_context, doc_requirements):
        """
        1. 规划文档结构 (30分钟)
        2. 编写核心文档 (60分钟)
        3. 评审与修订 (30分钟)
        4. 发布与维护 (持续)
        """
        # Step 1: 规划文档结构
        doc_structure = self.plan_doc_structure(project_context, doc_requirements)

        # Step 2: 编写核心文档
        drafts = self.create_content(doc_structure)

        # Step 3: 评审与修订
        final_docs = self.review_and_refine(drafts)

        # Step 4: 发布与维护
        published_docs = self.publish_and_maintain(final_docs)

        return DocumentationPackage(published_docs, doc_structure)

    def plan_doc_structure(self, context, requirements):
        """规划文档结构"""
        # 1. 识别文档类型
        # 2. 定义文档层级
        # 3. 规划信息架构
        pass

    def create_content(self, structure):
        """编写内容"""
        # 1. 收集信息
        # 2. 组织内容
        # 3. 编写初稿
        pass
```

## Decision Checkpoints

- [ ] **结构合理性**: 文档结构是否便于查找和理解？
- [ ] **内容完整性**: 是否覆盖了目标读者的所有需求？
- [ ] **可维护性**: 文档是否易于更新和维护？
- [ ] **一致性**: 文档风格和格式是否统一？

## Error Handling

| 场景 | 处理方式 |
|------|----------|
| 信息缺失 | 标注 TBD，联系相关方补充 |
| 内容冲突 | 以最新权威来源为准 |
| 过时信息 | 标记并创建更新任务 |

## Handover Standards

### 文档交付完成标准

```
✅ 文档结构符合项目规范
✅ 核心章节内容完整
✅ 代码示例经过验证
✅ 图表和截图清晰准确
✅ 术语和缩写已统一
✅ 评审意见已处理
```

### 交付物

1. **文档结构**: 文档目录和层级
2. **文档内容**: 各类型文档正文
3. **更新日志**: 文档变更记录

## Associated Assets

| 类型 | 路径 |
|------|------|
| SCENARIO | `scenarios/document-project/SCENARIO.md` |
| PROMPT | `prompts/document-project.prompt.md` |
| INSTRUCTIONS | `instructions/document-project.instructions.md` |
| AGENT | `agents/document-project.agent.md` |
| SKILL | `skills/document-project/SKILL.md` |


## Purpose

## Chain of Thought (思维链)

> **AI 必须按照以下思维链逐步执行**，每完成一步后进行自我验证

```
Step 1: [THINK] 理解任务目标和上下文
   ├─ 输入: 相关输入变量
   ├─ 思考: 任务的核心目标是什么？关键约束有哪些？
   ├─ 验证: 确认理解准确，无遗漏
   └─ 输出: 任务分析摘要
   ↓
Step 2: [ANALYZE] 分析需求和约束条件
   ├─ 输入: 任务分析摘要
   ├─ 思考: 有哪些关键决策点？可能的风险是什么？
   ├─ 验证: 分析全面，考虑了所有重要因素
   └─ 输出: 分析报告
   ↓
Step 3: [DESIGN] 设计解决方案
   ├─ 输入: 分析报告
   ├─ 思考: 最优方案是什么？有无备选方案？
   ├─ 验证: 方案可行且符合最佳实践
   └─ 输出: 设计方案
   ↓
Step 4: [IMPLEMENT] 执行和实施
   ├─ 输入: 设计方案
   ├─ 思考: 如何高质量地实施？需要注意什么？
   ├─ 验证: 实施符合设计规范
   └─ 输出: 实施成果
   ↓
Step 5: [VERIFY] 验证结果和质量
   ├─ 输入: 实施成果
   ├─ 执行: 质量检查和验证
   ├─ 验证: 满足所有验收标准
   └─ 输出: 验证报告
   ↓
Step 6: [HANDOVER] 准备交接
   ├─ 生成: Handover Context
   ├─ 更新: Global Context
   └─ 通知: 下一阶段 Agent
```




> Define the objectives and scope of the document-project scenario.
>
> This scenario ensures systematic execution of document-project activities with clear decision checkpoints and handover criteria.


## Prerequisites

- [ ] Prerequisite 1: Documentation scope and target audience are defined
- [ ] Prerequisite 2: Source artifacts and reference materials are available
- [ ] Prerequisite 3: Documentation style guide is approved


## Primary Assets

| Asset Type | Path | Description |
|------------|------|-------------|
| Scenario | `scenarios/document-project/SCENARIO.md` | This scenario definition |
| Prompt | `prompts/document-project.prompt.md` | Execution prompt |
| Instructions | `instructions/document-project.instructions.md` | Technical instructions |
| Agent | `agents/document-project.agent.md` | Responsible agent |
| Skill | `skills/document-project/SKILL.md` | Domain skill |


## Chain of Thought

1. Understand the context and requirements for document-project
2. Analyze dependencies and constraints
3. Execute core activities systematically
4. Validate outputs against acceptance criteria
5. Document decisions and handover state


## Decision Checkpoints

| Checkpoint | Question | Decision Options |
|------------|----------|-----------------|



## Error Handling (错误处理)

> **AI 遇到以下情况时必须按指定流程处理**

### 错误分类体系

| 级别 | 标识 | 描述 | 处理方式 |
|------|------|------|----------|
| P0 - Critical | ERR-CRITICAL | 阻塞性错误，无法继续 | 立即停止，升级人工处理 |
| P1 - Major | ERR-MAJOR | 严重错误，影响核心功能 | 尝试修复，失败则升级 |
| P2 - Minor | ERR-MINOR | 一般错误，可降级处理 | 记录并继续，后续修复 |
| P3 - Warning | ERR-WARNING | 警告信息，不影响执行 | 记录并继续 |

### Error Scenario 1: 通用错误处理

**识别信号**: 
- 检测到异常情况
- 验证失败

**处理流程**:
```
IF 检测到错误
THEN
  1. 识别错误类型和严重程度
  2. 记录错误详情
  3. 根据错误级别采取相应措施
  4. IF P0/P1 级别 THEN 升级到人工处理
  5. 更新状态并继续或停止
END
```

**降级方案**: 根据具体情况选择适当的降级策略

**升级条件**: P0 或 P1 级别错误

**错误日志格式**:
```yaml
error_log:
  error_id: "ERR-{timestamp}-XXX"
  timestamp: "{{ISO8601}}"
  level: "P0/P1/P2/P3"
  type: "{错误类型}"
  description: "{详细描述}"
  action_taken: "{已采取的行动}"
  result: "resolved/blocked/degraded/escalated"
```



## Quality Metrics

> Quality metrics for measuring scenario execution success.

| KPI | Target | Description |
|-----|--------|-------------|
| `DOC-COMPLETENESS` | ≥95% | 文档完整性：必需章节覆盖率 |
| `STALE-DOC-RATE` | ≤10% | 文档过时率：未及时更新的文档占比 |
| `USER-SATISFACTION` | ≥4.0/5 | 用户满意度：文档使用方评分 |

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识



## Quality Metrics (质量指标)

### Key Performance Indicators (KPIs)

| KPI ID | 指标名称 | 目标值 | 计算公式 | 验证方法 | 权重 |
|--------|----------|--------|----------|----------|------|
| KPI-001 | COMPLETION-RATE | ≥95% | (已完成项/总项数) × 100% | 完成情况检查 | 30% |
| KPI-002 | QUALITY-SCORE | ≥85/100 | 综合质量评分 | 质量评估表 | 30% |
| KPI-003 | COMPLIANCE | 100% | (符合规范项/总检查项) × 100% | 规范检查清单 | 20% |
| KPI-004 | EFFICIENCY | 按时完成 | 实际时间/计划时间 | 时间跟踪 | 20% |

**综合评分计算**: 
```
Quality Score = (KPI-001 × 0.30) + (KPI-002 × 0.30) + (KPI-003 × 0.20) + (KPI-004 × 0.20)
合格: ≥70分 | 优秀: ≥85分 | 卓越: ≥95分
```

### Validation Checklist (验证清单)

**完整性验证 (Completeness)**:
- [ ] 所有必需内容已完成
- [ ] 无遗漏的关键步骤
- [ ] 交付物完整

**一致性验证 (Consistency)**:
- [ ] 术语和命名统一
- [ ] 风格一致
- [ ] 与其他资产协调

**准确性验证 (Accuracy)**:
- [ ] 信息准确无误
- [ ] 数据和计算正确
- [ ] 链接和引用有效

**可执行性验证 (Executability)**:
- [ ] 步骤清晰可执行
- [ ] 资源和要求明确
- [ ] 无模糊或不确定的内容

**规范性验证 (Compliance)**:
- [ ] 遵循标准和规范
- [ ] 符合最佳实践
- [ ] 满足合规要求



## Handover Criteria

- [ ] Criterion 1: All required documentation types are produced
- [ ] Criterion 2: Documentation is reviewed and approved by stakeholders
- [ ] Criterion 3: Documentation is published to the knowledge repository


### Handover Context Template

```yaml
handover:
  header:
    from_stage: "document-project"
    to_stage: "unknown"
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

