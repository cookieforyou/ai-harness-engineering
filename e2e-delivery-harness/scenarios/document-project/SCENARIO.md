---
name: document-project
version: "1.1.0"
stage: "document-project"
---

# Scenario: 项目文档 (Document Project)

## 概述

项目文档是知识管理和信息传递的关键载体，负责创建和维护项目全生命周期的技术文档。

## 核心决策点

| 阶段 | 决策点 | 输出 |
|------|--------|------|
| 文档规划 | Doc Structure Design | 文档体系 |
| 内容创作 | Content Creation | 初稿 |
| 评审优化 | Review & Refine | 终稿 |
| 发布维护 | Publish & Maintain | 可用文档 |

## 执行流程

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

## 决策检查点

- [ ] **结构合理性**: 文档结构是否便于查找和理解？
- [ ] **内容完整性**: 是否覆盖了目标读者的所有需求？
- [ ] **可维护性**: 文档是否易于更新和维护？
- [ ] **一致性**: 文档风格和格式是否统一？

## 错误处理

| 场景 | 处理方式 |
|------|----------|
| 信息缺失 | 标注 TBD，联系相关方补充 |
| 内容冲突 | 以最新权威来源为准 |
| 过时信息 | 标记并创建更新任务 |

## 交接标准

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

> Define the objectives and scope of the document-project scenario.
>
> This scenario ensures systematic execution of document-project activities with clear decision checkpoints and handover criteria.


## Prerequisites

- [ ] Prerequisite 1: [Description]
- [ ] Prerequisite 2: [Description]
- [ ] Prerequisite 3: [Description]


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

## Error Handling

### Error Scenario 1
**Error**: [Description]
**Handling**: [Resolution steps]

### Error Scenario 2
**Error**: [Description]
**Handling**: [Resolution steps]



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

## Handover Criteria

- [ ] Criterion 1: [Description]
- [ ] Criterion 2: [Description]
- [ ] Criterion 3: [Description]
