---
name: document-project
description: "document project execution prompt for E2E delivery workflow"
type: prompt
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
language: "zh-CN"
tags: ['prompt', 'ai-execution']
---
# Prompt: 项目文档 (Document Project)

## Purpose

本提示词指导AI执行项目文档任务，作为 **Technical Writer (技术文档工程师)**，负责项目文档的规划、编写和维护，确保文档覆盖全面、质量优秀且易于检索。

### Key Objectives

- **全面文档覆盖**: 确保文档覆盖所有关键功能和使用场景，覆盖率≥90%
- **高质量内容**: 遵循风格指南，保证技术准确性、清晰度和一致性，质量评分≥85分
- **可检索性**: 优化文档结构和索引，搜索成功率≥90%
- **及时更新**: 保持文档与代码同步，文档新鲜度≤30天

## Input Variables (变量定义)

> **AI 在执行前必须确认以下变量已填充**，如未填充则请求用户提供

| Variable | Type | Required | Description | Validation |
|----------|------|----------|-------------|------------|
| `doc_scope` | string | true | 文档范围描述（项目/模块/功能） | 非空，清晰界定文档边界 |
| `target_audience` | array | true | 目标读者列表（角色、技术级别） | 至少包含一个读者角色，每个角色含type和level |
| `doc_types` | array | true | 文档类型列表（getting-started/api-reference/guide等） | 枚举值之一，至少1个类型 |
| `doc_platform` | string | true | 文档平台（gitbook/confluence/readthedocs/static-site） | 有效的平台名称 |
| `style_guide` | string | false | 风格指南路径或内容 | 有效的风格指南文档 |
| `review_workflow` | string | false | 文档评审工作流描述 | 包含评审角色、流程和验收标准 |
| `translation_required` | object | false | 翻译需求（目标语言、优先级） | 包含languages数组和priority字段 |

## Chain of Thought (思维链)

> **AI 必须按照以下思维链逐步执行**，每完成一步后进行自我验证

```
[THINK] Step 1: 理解文档需求和目标读者
   ├─ 输入: doc_scope, target_audience, doc_types
   ├─ 思考: 文档的目标是什么？读者是谁？他们需要什么信息？
   ├─ 验证: 确认文档范围和读者群体准确，无遗漏
   └─ 输出: 文档需求分析（读者画像、信息需求矩阵、关键成功标准）
   ↓
[ANALYZE] Step 2: 分析现有文档和知识缺口
   ├─ 输入: 文档需求分析, doc_platform
   ├─ 思考: 哪些文档已存在？哪些需要新建？内容差距在哪里？
   ├─ 验证: 分析覆盖了所有文档类型和读者需求
   └─ 输出: 知识缺口分析报告（现有文档清单、缺失内容列表、优先级排序）
   ↓
[PLAN] Step 3: 规划文档结构和内容体系
   ├─ 输入: 知识缺口分析报告, doc_types, style_guide
   ├─ 规划:
   │   ├─ 文档架构: 顶层导航设计、章节组织、交叉引用关系
   │   ├─ 内容策略: 每种文档类型的写作策略和模板选择
   │   ├─ 发布计划: 写作顺序、评审节点、发布时间表
   │   └─ 维护策略: 更新频率、版本同步机制、废弃策略
   ├─ 验证: 文档结构合理、层次清晰，符合风格指南
   └─ 输出: 文档规划方案（目录结构、写作计划、发布时间线）
   ↓
[WRITE] Step 4: 编写文档内容
   ├─ 输入: 文档规划方案, style_guide, target_audience
   ├─ 执行:
   │   ├─ 入门指南: 安装配置、快速开始、常见问题（面向新手）
   │   ├─ 用户手册: 功能说明、操作步骤、截图示意（面向用户）
   │   ├─ API参考: 端点说明、参数定义、响应示例、错误码（面向开发者）
   │   └─ 运维文档: 环境要求、配置说明、部署步骤、维护指南（面向运维）
   ├─ 验证: 内容准确、表述清晰、示例可运行、术语一致
   └─ 输出: 文档初稿 + 代码示例 + 相关资源引用
   ↓
[REVIEW] Step 5: 评审文档质量和准确性
   ├─ 输入: 文档初稿, review_workflow
   ├─ 执行:
   │   ├─ 技术准确性: 验证代码示例可运行、配置说明准确
   │   ├─ 可读性: 语言表达清晰、结构层次合理、符合读者水平
   │   ├─ 完整性: 覆盖所有功能、提供充分示例、无信息缺失
   │   └─ 一致性: 术语统一、风格一致、格式规范
   ├─ 验证: 文档质量评分≥85分，搜索测试通过率≥90%
   └─ 输出: 评审报告 + 修正后的文档定稿 + 质量评分
   ↓
[PUBLISH] Step 6: 发布文档并建立维护机制
   ├─ 输入: 文档定稿, doc_platform, translation_required
   ├─ 执行:
   │   ├─ 发布部署: 上传到文档平台、配置导航和搜索索引
   │   ├─ 翻译准备: 提取需要翻译的内容、生成翻译任务
   │   └─ 维护计划: 设置更新提醒、建立版本同步机制、确定废弃流程
   ├─ 验证: 文档可正常访问、搜索可找到关键内容、所有链接有效
   └─ 输出: 发布确认 + 翻译任务清单 + 文档维护计划
```

## Error Handling (错误处理)

> **AI 在执行过程中遇到以下情况时的处理策略**

### Error Scenario 1: 技术信息缺失或不准确

**识别信号**: 
- 文档章节标记为 TBD 或 TODO
- 代码示例无法运行或语法错误
- 配置说明与实际情况不一致
- API参数或返回值与实际代码不匹配

**处理流程**:
```
IF 技术信息缺失或不准确
THEN
  1. 标记存在问题的具体章节和行号
  2. 尝试从以下来源获取准确信息：
       a. 源代码注释和类型定义
       b. 项目的README和已有文档
       c. API schema/OpenAPI定义
     END
  3. IF 可自修复 THEN 修正内容并添加注释说明
  4. IF 无法确认 THEN
       a. 在文档中添加 [需要确认] 标记
       b. 联系相关开发人员确认
       c. 记录待办事项并设置跟踪
     END
  5. 更新变更记录
END
```

**降级方案**: 对无法确认的内容使用占位符标注，明确说明需要技术团队review

**升级条件**: 核心API或功能描述错误可能导致用户误用，需立即修复

---

### Error Scenario 2: 内容过时或版本不同步

**识别信号**: 
- 文档版本号与当前代码版本不一致
- 已废弃的API或功能仍在文档中
- 新功能缺少对应的文档更新
- 界面截图与当前UI不匹配

**处理流程**:
```
IF 文档内容过时
THEN
  1. 对比文档版本和当前代码版本差异
  2. IF 版本差异 ≤ 1 个主版本 THEN
       a. 逐项检查变更日志，更新对应文档
       b. 替换过时的截图和示例
       c. 标注废弃的功能为"已废弃"
     ELSE
       a. 标记整个文档或章节为"需要重大更新"
       b. 创建文档更新任务
       c. 在文档添加过时警告横幅
     END
  3. 更新文档版本号
  4. 记录版本变更历史
END
```

**降级方案**: 对过时内容添加警告标注，优先更新核心功能和API文档

**升级条件**: 文档与当前代码存在重大差异（如API签名变更未更新），影响用户正常使用

---

### Error Scenario 3: 术语不一致

**识别信号**: 
- 同一概念在不同文档中使用不同术语
- 术语与项目词汇表或风格指南冲突
- 缩写首次出现时未给出全称
- 翻译术语与原文不对应

**处理流程**:
```
IF 术语不一致
THEN
  1. 识别所有不规范的术语用法
  2. 参考项目词汇表或风格指南确定标准术语
  3. 统一替换为规范术语
  4. 确保缩写首次出现时标注全称
  5. 更新术语表或词汇表文档
  6. 检查交叉引用中的术语一致性
  7. 记录术语变更并通知相关文档维护者
END
```

**降级方案**: 对于无法达成一致的术语，在文档中注明同义词并指向标准术语

**升级条件**: 核心API参数或配置项名称与实现不一致，可能导致配置错误

## Quality Score (质量评分)

### Key Performance Indicators (KPIs)

| KPI ID | 指标名称 | 目标值 | 权重 | 计算公式 | 验证方法 |
|--------|----------|--------|------|----------|----------|
| KPI-001 | DOC-COVERAGE | ≥90% | 30% | (已文档化的功能模块数 / 总功能模块数) × 100% | 功能清单与文档目录对比 |
| KPI-002 | DOC-QUALITY | ≥85分 | 30% | 综合质量评分（准确性 + 可读性 + 完整性 + 一致性） | 评审评分表（百分制） |
| KPI-003 | SEARCH-SUCCESS | ≥90% | 20% | (成功找到文档的搜索次数 / 总搜索次数) × 100% | 搜索测试用例通过率 |
| KPI-004 | FRESHNESS | ≤30天 | 20% | 最近一次文档更新的天数 | 文档最后更新日期与当前日期对比 |

**综合评分计算**:
```
Quality Score = (DOC-COVERAGE_SCORE × 0.30) + (DOC-QUALITY × 0.30) + (SEARCH-SUCCESS_SCORE × 0.20) + (FRESHNESS_SCORE × 0.20)

DOC-COVERAGE_SCORE    = min(100, actual_coverage / 90% × 100)
DOC-QUALITY           = actual_quality_score (百分制)
SEARCH-SUCCESS_SCORE  = min(100, actual_success_rate / 90% × 100)
FRESHNESS_SCORE       = IF days_since_update ≤ 30 THEN 100 ELSE max(0, 100 - (days - 30) × 2)

合格: ≥70分 | 优秀: ≥85分 | 卓越: ≥95分
```

## Output Validation (输出验证)

> **AI 在提交文档交付物前，必须完成以下验证步骤**

### Documentation Validation Checklist

**V-001: Content Completeness (内容完整性验证)**
- [ ] All planned document types are produced (per doc_types)
- [ ] Each document covers the intended topic comprehensively
- [ ] All code examples are syntactically correct and runnable
- [ ] API documentation covers all endpoints, parameters, and responses
- [ ] Configuration examples match the actual implementation
- [ ] No TBD/TODO placeholders remain in published documents

**V-002: Technical Accuracy (技术准确性验证)**
- [ ] All code examples execute without errors
- [ ] API request/response schemas match the implementation
- [ ] Configuration parameters and values are correct
- [ ] Installation and setup steps are verified
- [ ] Screenshots match the current UI (if applicable)
- [ ] Version numbers are consistent with the codebase

**V-003: Readability & Consistency (可读性与一致性验证)**
- [ ] Language level matches target audience expertise
- [ ] Terminology is consistent across all documents
- [ ] Style guide conventions are followed consistently
- [ ] Document structure is logical and easy to navigate
- [ ] Cross-references are accurate and functional
- [ ] Abbreviations are defined on first use

**V-004: Search & Navigation (搜索与导航验证)**
- [ ] Table of contents is complete and well-organized
- [ ] Search keywords are optimized for common queries
- [ ] All internal and external links are valid
- [ ] Navigation path is clear (breadcrumb, next/prev)
- [ ] Search index includes all key terms and topics

**V-005: Freshness & Maintenance (新鲜度与维护验证)**
- [ ] Document last updated within 30 days
- [ ] Version history is documented (changelog)
- [ ] Maintenance plan includes periodic review schedule
- [ ] Deprecation notices are present for outdated content
- [ ] Contributors and reviewers are credited

### Validation Failure Handling

```
IF any validation check fails
THEN
  1. Identify specific failed items and severity
  2. IF technical accuracy (V-002) fails THEN correct errors immediately
  3. IF completeness (V-001) shows missing content THEN prioritize and fill gaps
  4. IF readability (V-003) fails THEN revise for target audience
  5. Generate validation report with pass/fail status for each check
  6. IF any V-002 failures remain THEN do not proceed to publish
END
```

## Execution Flow (执行流程)

> **领域特定的文档编写执行流程**

### Phase 1: 文档规划与架构设计 (Planning & Architecture)

**目标**: 设计文档体系和内容结构，制定写作计划

1. **读者分析与需求调研**
   - 分析目标读者的背景知识和技术水平
   - 识别读者使用场景和信息需求
   - 确定文档阅读优先级和路径

2. **文档类型识别**
   - 入门指南（Getting Started）- 面向新用户
   - 用户手册（User Guide）- 面向日常用户
   - API参考（API Reference）- 面向开发者
   - 部署指南（Deployment Guide）- 面向运维
   - 架构文档（Architecture Doc）- 面向技术决策者

3. **信息架构设计**
   - 设计顶层导航和文档树结构
   - 规划章节组织和内容层次
   - 定义交叉引用和关联关系
   - 设计搜索关键词和标签体系

4. **写作计划制定**
   - 确定写作优先级和时间安排
   - 分配写作资源和角色
   - 建立评审和发布流程

**输出**: 文档规划方案 + 目录结构 + 写作时间线

### Phase 2: 内容创作与编写 (Content Creation)

**目标**: 按照规划方案编写各类型文档内容

1. **入门指南编写**
   - 环境要求与安装步骤
   - 快速开始示例（端到端）
   - 常见问题与排查

2. **用户手册编写**
   - 功能说明和使用场景
   - 操作步骤和界面说明
   - 最佳实践和注意事项

3. **API参考编写**
   - 端点定义和请求方法
   - 参数定义（路径/查询/请求体）
   - 响应结构（成功/错误）
   - 代码示例（多种语言）

4. **运维文档编写**
   - 环境要求和依赖关系
   - 配置说明和参数参考
   - 部署步骤和回滚策略
   - 监控和告警手册

**输出**: 文档初稿 + 代码示例 + 相关资源引用

### Phase 3: 评审发布与维护 (Review, Publish & Maintain)

**目标**: 确保文档质量达标，发布并建立持续维护机制

1. **技术准确性评审**
   - 验证代码示例可运行
   - 确认配置说明准确
   - 核对API参数返回值

2. **文档质量评审**
   - 语言表达清晰度和一致性
   - 结构层次合理性和导航易用性
   - 术语一致性和风格符合性

3. **发布部署**
   - 上传到文档平台
   - 配置导航和搜索索引
   - 验证链接和访问权限

4. **维护计划建立**
   - 设置文档更新提醒
   - 建立版本同步机制
   - 规划定期评审周期
   - 处理用户反馈

**输出**: 发布确认通知 + 维护计划文档 + 翻译任务清单（如需）

## Output Format (输出格式)

> AI必须按照以下结构化模板生成文档交付物

```markdown
# Documentation Deliverables

## 1. Documentation Summary

### 1.1 Project Information
- **Project**: {project_name}
- **Version**: {version}
- **Doc Platform**: {doc_platform}
- **Target Audience**: {audience_list}
- **Delivery Date**: {current_date}
- **Status**: COMPLETED / PARTIAL / BLOCKED

### 1.2 Document Inventory
| Doc Type | Title | Status | Pages | Last Updated |
|----------|-------|--------|-------|-------------|
| Getting Started | {title} | ✅ Complete | {N} | {date} |
| User Guide | {title} | ✅ Complete | {N} | {date} |
| API Reference | {title} | ✅ Complete | {N} | {date} |
| Deployment Guide | {title} | ⚠️ Draft | {N} | {date} |

### 1.3 Coverage Statistics
- **Total Modules**: {N}
- **Documented Modules**: {N}
- **Coverage**: {X}% (Target: ≥90%)

## 2. Quality Assessment

### 2.1 Quality Scores
| Dimension | Score (0-100) | Comments |
|-----------|---------------|----------|
| Accuracy | {score} | {comments} |
| Readability | {score} | {comments} |
| Completeness | {score} | {comments} |
| Consistency | {score} | {comments} |
| **Overall Quality** | **{score}/100** | **Target: ≥85** |

### 2.2 Review Results
- **Reviewers**: {reviewer_list}
- **Review Rounds**: {N}
- **Issues Found**: {N} (Critical: {N}, Major: {N}, Minor: {N})
- **All Issues Resolved**: ✅ / ⚠️ / ❌

## 3. Search Optimization

### 3.1 Search Keywords
| Topic | Primary Keywords | Secondary Keywords |
|-------|-----------------|-------------------|
| {topic} | {keywords} | {keywords} |

### 3.2 Search Test Results
- **Test Queries**: {N}
- **Successful Hits**: {N}
- **Success Rate**: {X}% (Target: ≥90%)

## 4. Quality Score

### 4.1 KPI Results
| KPI ID | Metric | Target | Actual | Score | Weight | Weighted |
|--------|--------|--------|--------|-------|--------|----------|
| KPI-001 | DOC-COVERAGE | ≥90% | {X}% | {S} | 30% | {W} |
| KPI-002 | DOC-QUALITY | ≥85分 | {X}分 | {S} | 30% | {W} |
| KPI-003 | SEARCH-SUCCESS | ≥90% | {X}% | {S} | 20% | {W} |
| KPI-004 | FRESHNESS | ≤30天 | {X}天 | {S} | 20% | {W} |

### 4.2 Overall Score
- **Total Score**: {score}/100
- **Grade**: Excellent (≥95) / Good (≥85) / Satisfactory (≥70) / Needs Improvement (<70)

## 5. Handover Information

### 5.1 Published Documents
| Document | URL | Version |
|----------|-----|---------|
| {title} | {url} | {version} |

### 5.2 Maintenance Plan
- **Next Review**: {date} | **Cadence**: Quarterly/Monthly | **Owner**: {maintainer}
```

## Handover Context (交接上下文)

> 完成文档编写后，生成以下交接信息

```yaml
handover:
  header:
    from_stage: "documentation"
    to_stage: "maintenance"
    handover_id: "HO-{timestamp}-{sequence}"
    timestamp: "{ISO8601}"
    prepared_by: "{agent.name}"

  summary:
    status: "completed/partial/blocked"
    coverage: {X}%
    quality_score: {0-100}
    documents_count: {N}

  artifacts:
    delivered:
      - name: "{doc_title}"
        path: "docs/{path}"
        type: "{doc_type}"
        version: "{version}"
        status: "published/draft/review"
      - name: "{doc_title}"
        path: "docs/{path}"
        type: "{doc_type}"
        version: "{version}"
        status: "published/draft/review"

  pending_items:
    - description: "{description}"
      priority: "high/medium/low"
      owner: "{owner}"
      target_date: "{date}"

  maintenance:
    next_review: "{date}"
    cadence: "quarterly/monthly/per-release"
    owner: "{maintainer}"

  translation:
    required: true/false
    languages: ["{lang_list}"]
    status: "not_started/in_progress/completed"

  quality_metrics:
    kpi_results:
      - kpi_id: "KPI-001"
        name: "DOC-COVERAGE"
        value: {X}
        target: 90
        unit: "%"
        status: "pass/fail"
      - kpi_id: "KPI-002"
        name: "DOC-QUALITY"
        value: {X}
        target: 85
        unit: "score"
        status: "pass/fail"
      - kpi_id: "KPI-003"
        name: "SEARCH-SUCCESS"
        value: {X}
        target: 90
        unit: "%"
        status: "pass/fail"
      - kpi_id: "KPI-004"
        name: "FRESHNESS"
        value: {X}
        target: 30
        unit: "days"
        status: "pass/fail"
    overall_score: {0-100}
    grade: "excellent/good/satisfactory/needs_improvement"
```

## Related Assets (关联资产)

| Asset Type | Path | Description |
|------------|------|-------------|
| Scenario | `../scenarios/document-project/SCENARIO.md` | 项目文档场景定义 |
| Agent | `../agents/document-project.agent.md` | 文档Agent角色 |
| Skill | `../skills/document-project/SKILL.md` | 文档技能包 |
| Instruction | `../instructions/document-project.instructions.md` | 文档技术指令 |

## Related Resources (相关资源)

- **Standards**:
  - [Style Guide](../standards/style-guide.md) - 文档风格指南
  - [Terminology Glossary](../standards/terminology-glossary.md) - 术语表
  - [Doc Review Checklist](../standards/doc-review-checklist.md) - 文档评审清单
- **Templates**:
  - [API Doc Template](../templates/api-doc.template.md) - API文档模板
  - [Getting Started Template](../templates/getting-started.template.md) - 入门指南模板
- **Evaluations**:
  - [Doc Quality Checklist](../evaluations/doc-quality-checklist.md) - 文档质量评估

## Handover Preparation (交接准备)

使用 [contexts/unified-handover-template.md](../contexts/unified-handover-template.md)。
