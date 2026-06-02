---
name: manage-knowledge
description: "知识管理场景的技术指令"
applyTo: "scenarios/manage-knowledge/**"
phase: governance
type: instruction
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['instruction', 'technical']
---
# Knowledge Management Instructions

## Overview

This instruction provides the comprehensive technical specifications and governance framework for knowledge management across engineering teams. It covers knowledge base architecture, taxonomy design, documentation lifecycle management, search and retrieval optimization, and content quality standards. The instruction ensures organizational knowledge is captured, discoverable, and maintained as a first-class engineering asset. Key focus areas include ownership models, review cadences, deprecation policies, and integration with developer workflows to maximize knowledge reuse and minimize silos.


## Documentation Types

### Tutorial (教程)
```yaml
purpose: "Learning by doing"
structure:
  - Prerequisites
  - Step-by-step instructions
  - Expected outcome
  - Next steps
style: "Conversational, encouraging"
```

### How-To Guide (操作指南)
```yaml
purpose: "Achieve a specific goal"
structure:
  - Goal statement
  - Prerequisites
  - Steps
  - Verification
  - Troubleshooting
style: "Direct, practical"
```

### Reference (参考文档)
```yaml
purpose: "Look up facts"
structure:
  - Overview
  - Parameters/Functions
  - Examples
  - Related
style: "Precise, complete"
```

### Explanation (解释说明)
```yaml
purpose: "Understanding"
structure:
  - Context
  - Key concepts
  - Perspectives
  - Further reading
style: "Educational, balanced"
```

## Documentation Structure

### Folder Structure
```
docs/
├── getting-started/
│   ├── quick-start.md
│   ├── installation.md
│   └── configuration.md
├── guides/
│   ├── deployment/
│   │   ├── kubernetes.md
│   │   └── aws.md
│   └── development/
│       ├── setup.md
│       └── testing.md
├── reference/
│   ├── api/
│   │   ├── rest-api.md
│   │   └── graphql-api.md
│   └── configuration/
│       └── config-reference.md
├── explanations/
│   ├── architecture/
│   └── decisions/
└── templates/
    ├── design-doc.md
    └── runbook.md
```

### Frontmatter Template
```yaml
---
title: "Document Title"
description: "Brief description"
author: "Author Name"
date: "2024-01-01"
version: "1.1.0"
category: "guides"
tags: ["tag1", "tag2"]
status: "published|draft|archived"
reviewers: ["reviewer1", "reviewer2"]
last_reviewed: "2024-01-01"
next_review: "2024-04-01"
---
```

## Writing Guidelines

### Style Guide

```markdown
## Voice and Tone
- Use active voice
- Be concise
- Use consistent terminology
- Write for scanning (headings, lists)

## Formatting
- Headings: Sentence case
- Code blocks: Specify language
- Lists: Parallel structure
- Links: Descriptive text

## Terminology
- Use consistent terms
- Define acronyms
- Use industry standard
```

### Code Block Examples

```markdown
```typescript
// Good: Descriptive variable names
const userAuthenticationToken = await authenticateUser(credentials);

// Bad: Cryptic abbreviations
const authToken = await authUser(creds);

// Better: Comment explains why
// Using short variable for brevity in this example
const authToken = await authUser(creds);
`````

## Knowledge Base Tools

### Wiki Platforms
| Platform | Best For | Features |
|----------|----------|----------|
| Confluence | Enterprise | Rich editing, JIRA integration |
| Notion | Flexible | All-in-one, API |
| GitBook | Developer | Git-based, API docs |
| MkDocs | Technical | Markdown, search |
| Docusaurus | Docs sites | React, versioning |

### Documentation Generators
```bash
# MkDocs
mkdocs new my-project
mkdocs serve
mkdocs build

# Docusaurus
npx create-docusaurus@latest my-website classic
npm run build

# VuePress
npm install -D vuepress
npm run docs:build
```

## Knowledge Lifecycle

### Creation
```yaml
workflow:
  - idea: "Identify knowledge need"
  - draft: "Create initial content"
  - review: "Peer review"
  - edit: "Incorporate feedback"
  - publish: "Release to knowledge base"
```

### Maintenance
```yaml
maintenance_schedule:
  monthly:
    - "Review high-traffic articles"
    - "Update outdated information"
    
  quarterly:
    - "Full documentation audit"
    - "Archive obsolete content"
    - "Gather user feedback"
    
  annually:
    - "Major content reorganization"
    - "Style guide review"
    - "Tool evaluation"
```

### Archival
```yaml
archival_criteria:
  - content_older_than: "2 years"
  - page_views_below: "10/month"
  - no_updates_since: "18 months"
  
archival_process:
  - notify_users: "30 days notice"
  - create_archive: "PDF/static version"
  - set_redirect: "point to related content"
```

## Search Optimization

### Metadata Best Practices
```yaml
metadata:
  title:
    - include_keywords
    - front-load important words
    - avoid filler words
    
  description:
    - 150-160 characters
    - include primary keyword
    - clear value proposition
    
  tags:
    - use consistent vocabulary
    - include synonyms
    - group related terms
```

### Content Organization
```yaml
findability_factors:
  - clear_hierarchy: true
  - consistent_naming: true
  - cross_linking: true
  - related_content: true
  - breadcrumbs: true
```

## Quality Metrics

### Content Metrics
| Metric | Target | Measurement |
|--------|--------|-------------|
| Page views | >100/month | Analytics |
| Time on page | >2 minutes | Analytics |
| Helpful votes | >80% | User feedback |
| Search success | >90% | Search logs |
| Update frequency | quarterly | Last modified |

### Quality Checklist
```markdown
## Content Quality Checklist
- [ ] Accurate and up-to-date
- [ ] Clear and understandable
- [ ] Well-structured
- [ ] Contains examples
- [ ] Has no broken links
- [ ] Follows style guide
- [ ] Peer-reviewed
```


## Technical Specifications

> Detailed technical requirements and implementation guidelines for manage-knowledge.

### Required Tools
- [List required tools and frameworks]

### Environment Requirements
- [List environment prerequisites]

### Configuration Parameters
- [List key configuration parameters]


## Best Practices

> Industry-standard best practices for manage-knowledge execution.

1. **Practice 1**: Organize knowledge by domain with clear ownership
2. **Practice 2**: Maintain freshness with periodic review cycles
3. **Practice 3**: Enable discoverability through indexing and tagging


## Error Handling

> Common error scenarios and resolution strategies for manage-knowledge.

### Error Category 1
**Symptom**: Knowledge is fragmented and difficult to locate
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]

### Error Category 2
**Symptom**: Documentation is outdated or unmaintained
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]


## Quality Standards

> Acceptance criteria and quality gates for manage-knowledge deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | Knowledge indexing coverage is 95% or higher | Automated check |
| Standard 2 | User search success rate is 80% or higher | Automated check |
| Standard 3 | Content updated within last 6 months is 90% or higher | Automated check |
## References

- [harness-engineering.md](../standards/harness-engineering.md)
- [output-validation-checklist.md](../evaluations/output-validation-checklist.md)
- [regression-checklist.md](../evaluations/regression-checklist.md)
