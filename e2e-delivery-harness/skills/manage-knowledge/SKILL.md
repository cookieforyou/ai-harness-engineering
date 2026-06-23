---
name: manage-knowledge
description: "Domain skill for manage-knowledge execution"
category: governance
type: skill
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
language: "zh-CN"
tags: ['skill', 'knowledge']
---
# Knowledge Management Skill

## Core Knowledge

### 1. Knowledge Management Principles

#### DIKW Pyramid
```
Data → Information → Knowledge → Wisdom
     ↓            ↓           ↓         ↓
   Raw          Processed    Applied   Judged
   Facts        Context      Experience Insight
```

#### Knowledge Types
| Type | Description | Example |
|------|-------------|---------|
| Explicit | Codified, formal | Documentation, procedures |
| Tacit | Personal, contextual | Experience, intuition |
| Embedded | In processes, systems | Best practices |

### 2. Documentation Best Practices

#### Writing Principles
1. **Audience First**: Know your readers
2. **Task-Oriented**: Focus on goals
3. **Progressive Disclosure**: Layer information
4. **Consistent**: Maintain style
5. **Searchable**: Optimize discoverability

#### Structure Principles
1. **Clear Hierarchy**: Logical organization
2. **Progressive Detail**: Overview → Details
3. **Cross-References**: Connect related content
4. **Visual Aids**: Use diagrams, examples

### 3. Content Types

#### Conceptual
- Explain "what" and "why"
- Use analogies
- Provide context
- Keep high-level

#### Procedural
- Explain "how"
- Use numbered steps
- Include checkpoints
- Provide troubleshooting

#### Reference
- Organize alphabetically/categorically
- Be complete
- Use tables
- No explanations

### 4. Documentation Tools

#### Static Site Generators
| Tool | Strengths | Use Case |
|------|-----------|----------|
| MkDocs | Material theme, search | Internal docs |
| Docsify | Lightweight, Markdown | Simple docs |
| Docusaurus | React, versioning | Product docs |
| VuePress | Vue ecosystem | Technical blogs |
| GitBook | Collaboration | Team wikis |

#### Wiki Platforms
| Platform | Strengths | Use Case |
|----------|-----------|----------|
| Confluence | Enterprise features | Large orgs |
| Notion | Flexibility | All-in-one |
| Slite | Simplicity | Small teams |
| Outline | Open source | Self-hosted |

### 5. Knowledge Curation Process

#### Creation
```yaml
creation_workflow:
  1. identify:
     - Gap analysis
     - User requests
     - Compliance needs
     
  2. plan:
     - Outline content
     - Assign owner
     - Set deadline
     
  3. draft:
     - Write content
     - Add examples
     - Include visuals
     
  4. review:
     - Technical accuracy
     - Clarity check
     - Style guide compliance
     
  5. publish:
     - Version control
     - Metadata
     - Notify users
```

#### Maintenance
```yaml
maintenance_triggers:
  - regular_review: quarterly
  - user_feedback: continuous
  - system_change: on-change
  - content_decay: when outdated
  
maintenance_actions:
  - update: "Update with new information"
  - merge: "Combine with related content"
  - archive: "Move to historical"
  - delete: "Remove if obsolete"
```

### 6. Search and Discovery

#### SEO for Documentation
```yaml
on_page_seo:
  title:
    - Include primary keyword
    - Keep under 60 characters
    - Front-load important words
    
  meta_description:
    - 150-160 characters
    - Include keyword
    - Clear value proposition
    
  headings:
    - One H1 per page
    - Include keywords in H2-H6
    - Logical hierarchy
    
  content:
    - Include keywords naturally
    - Use related terms
    - Provide comprehensive coverage
```

### 7. Collaboration

#### Review Workflow
```yaml
review_levels:
  - self_review: "Check before submission"
  - peer_review: "Technical accuracy"
  - editorial_review: "Style and clarity"
  - stakeholder_review: "Business alignment"
  
review_feedback:
  types:
    - correction: "Fix factual errors"
    - clarification: "Make clearer"
    - addition: "Add missing info"
    - deletion: "Remove unnecessary"
```

### 8. Metrics and Measurement

#### Content Performance
| Metric | Good | Needs Improvement |
|--------|------|-------------------|
| Page views | >100/month | <50/month |
| Time on page | >3 min | <1 min |
| Bounce rate | <40% | >70% |
| Task success | >80% | <50% |
| Helpful votes | >80% | <60% |

#### Knowledge Health
```yaml
health_indicators:
  coverage:
    - critical_topics: 100%
    - active_topics: recent_update
    
  quality:
    - accuracy: peer_reviewed
    - completeness: has_examples
    - currency: within_review_cycle
    
  accessibility:
    - findable: indexed_properly
    - readable: appropriate_level
    - usable: actionable
```

## Best Practices

1. **Start with Why**: Help readers understand purpose
2. **Show, Don't Tell**: Use examples liberally
3. **Keep It Current**: Schedule regular reviews
4. **Make It Findable**: Optimize search
5. **Gather Feedback**: Measure and improve
6. **Collaborate**: Involve subject matter experts
7. **Automate**: Use docs-as-code workflows


## Anti-patterns (反模式)

> 与 Common Pitfalls 同义，执行时合并检查。

## Common Pitfalls

> Frequent mistakes to avoid during manage-knowledge execution.

### Pitfall 1: 文档写完不维护 (僵尸文档)
**Risk**: 文档在创建时经过充分审查，但创建后长时间无人更新，内容逐渐与系统实际状态脱节。过时的架构图、错误的API示例和已废弃的流程文档会误导读者，造成决策错误或时间浪费。
**Prevention**: 为每个文档设置Review Owner和Review周期(如季度或半年)，通过自动化工具扫描文档最后更新时间和关联系统变更事件触发审查提醒。将文档维护纳入任务列表和迭代规划，确保知识及时刷新。
**Impact**: 读者不信任文档质量，转而通过口头沟通或亲自阅读代码获取信息，知识管理的投资回报率归零；新团队成员上手时间延长，关键知识集中在少数人脑中。

### Pitfall 2: 知识只存在个人脑中
**Risk**: 关键的系统设计决策、故障处理经验、业务规则和操作步骤仅由少数核心成员掌握，没有通过文档方式显性化。当核心成员休假或离职时，相关知识无法被有效传递和复用。
**Prevention**: 建立"写在设计之前、记录在故障之后"的文化——任何架构决策记录(ADR)、故障复盘(RCA)和运维操作必须产出文档；将知识传递作为转岗和离职交接的必要条件；定期举办内部知识分享会驱动经验输出。
**Impact**: 核心成员缺席或离职时出现关键知识断层，系统维护和故障处理效率骤降；团队对新人的培养成本高且周期长，形成对特定人员的单点依赖风险。

### Pitfall 3: 过度分类增加查找成本
**Risk**: 文档知识库创建了过多层次的分类目录和标签体系，用户需要经过多次点击或猜测才能找到目标文档。复杂的分类结构导致文档发布者也无法确定新文档该放在哪个目录下。
**Prevention**: 采用"扁平化+全文搜索"优先的导航策略，顶层目录不超过8个分类；投入资源优化搜索引擎(如标题权重、同义词扩展、相关性排序)；定期通过对用户的文档查找行为分析优化分类设计。
**Impact**: 知识查找成本超过直接询问同事或重新摸索的成本，知识库逐渐被弃用；重复创建相似内容加剧信息混乱，进一步降低知识库的可用性。
