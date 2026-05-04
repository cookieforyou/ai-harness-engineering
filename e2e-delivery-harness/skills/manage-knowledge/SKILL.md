---
name: manage-knowledge
description: "Domain skill for manage-knowledge execution"
type: skill
version: "1.1.0"
stage: "manage-knowledge"
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


## Common Pitfalls

> Frequent mistakes to avoid during manage-knowledge execution.

### Pitfall 1: [Name]
**Risk**: [Description]
**Prevention**: [How to avoid]
**Impact**: [Consequences if not avoided]

### Pitfall 2: [Name]
**Risk**: [Description]
**Prevention**: [How to avoid]
**Impact**: [Consequences if not avoided]

### Pitfall 3: [Name]
**Risk**: [Description]
**Prevention**: [How to avoid]
**Impact**: [Consequences if not avoided]
