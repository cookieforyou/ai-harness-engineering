---
name: document-project
description: Detailed technical instructions for document-project scenario execution
type: instruction
version: "1.1.0"
stage: document-project
---

# Instructions: 项目文档 (Document Project)

## Overview

本文档定义了项目文档编写的详细技术规范和最佳实践。

## Document Type Standards

### 文档类型矩阵

| 类型 | 受众 | 深度 | 长度 | 更新频率 |
|------|------|------|------|----------|
| 入门指南 | 新用户 | 基础 | 中等 | 低 |
| 用户手册 | 终端用户 | 完整 | 长 | 中 |
| API 参考 | 开发者 | 深入 | 长 | 高 |
| 部署指南 | 运维人员 | 完整 | 中等 | 中 |
| 开发者指南 | 贡献者 | 深入 | 长 | 中 |

### 文档结构模板

#### 入门指南模板

```markdown
# {项目名称} 入门指南

## What is {project_name}
{一句话描述项目及其核心价值}

## Quick Start
### 安装
```bash
pip install {package-name}
```

### 第一个例子
```python
import {package}

# 5 行代码完成基本功能
result = {package}.do_something()
print(result)
```

## Next Steps
- 想深入了解？查看 [用户手册](user-guide.md)
- 遇到问题？查看 [FAQ](faq.md)

## Getting Help
- GitHub Issues
- 社区论坛
```

#### API 参考模板

```markdown
# API 参考

## Authentication
所有 API 请求需要认证令牌。

### 获取令牌
```bash
curl -X POST /api/auth/token \
  -H "Content-Type: application/json" \
  -d '{"api_key": "your-key"}'
```

## User API

### 创建用户
创建新用户账户。

**请求**
```http
POST /api/users
Content-Type: application/json

{
  "username": "string",
  "email": "string"
}
```

**响应**
```json
{
  "id": "123",
  "username": "string",
  "email": "string",
  "created_at": "2024-01-01T00:00:00Z"
}
```

**错误码**
| 状态码 | 说明 |
|--------|------|
| 400 | 请求参数错误 |
| 409 | 用户名已存在 |

### 获取用户
获取指定用户信息。

**请求**
```http
GET /api/users/{id}
```

**响应**
```json
{
  "id": "123",
  "username": "string",
  "email": "string"
}
```
```

## Writing Standards

### Markdown 规范

```python
MARKDOWN_STYLE_GUIDE = """
# Markdown 编写规范

## Heading Levels
- H1: 文档标题 (每个文档只有一个)
- H2: 主要章节
- H3: 子章节
- H4: 更细的分节

## Code Blocks
- 必须指定语言: ```python
- 代码行号仅在需要时添加
- 过长代码应分段说明

## Lists
- 使用有序列表表示步骤
- 使用无序列表表示要点
- 嵌套不超过 3 层

## Links
- 使用相对路径链接内部文档
- 使用完整 URL 链接外部资源
"""

def format_markdown(content):
    """格式化 Markdown 内容"""
    # 1. 检查标题层级
    validate_heading_levels(content)

    # 2. 验证代码块语法
    validate_code_blocks(content)

    # 3. 检查链接有效性
    validate_links(content)

    return content
```

### 技术文档规范

```yaml
technical_doc_standards:
  # 代码示例规范
  code_examples:
    - must_be_runnable: true
      must_have_comments: true
      max_length: 50 lines
      explain_before: true

  # 图表规范
  diagrams:
    - format: ["png", "svg"]
      max_size: "2MB"
      include_alt_text: true

  # 术语规范
  terminology:
    - use_project_glossary: true
    - define_acronyms: true
    - consistent_spelling: true
```

## Documentation Toolchain

### 文档生成工具

| 工具 | 用途 | 配置 |
|------|------|------|
| MkDocs | 静态站点生成 | mkdocs.yml |
| Docusaurus | React 文档站点 | docusaurus.config.js |
| Sphinx | Python 文档 | conf.py |
| VuePress | Vue 文档站点 | config.js |

### MkDocs 配置示例

```yaml
# mkdocs.yml
site_name: 项目文档
site_description: 项目详细文档

theme:
  name: material
  features:
    - navigation.instant
    - navigation.tracking
    - content.code.copy

nav:
  - Home: index.md
  - Getting Started:
    - Installation: getting-started/installation.md
    - Quick Start: getting-started/quickstart.md
  - Guides:
    - Deployment: guides/deployment.md
    - Configuration: guides/configuration.md
  - API Reference:
    - Overview: api/index.md
    - Endpoints: api/endpoints.md

markdown_extensions:
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.superfences
  - admonition
  - tables
```

## Documentation Quality Checks

### 检查清单

```python
DOCUMENTATION_CHECKLIST = """
## Pre-release Checklist

### 内容检查
[ ] 所有章节都有实质内容
[ ] 没有占位符文本 (TBD, TODO 需要填写)
[ ] 代码示例经过测试可运行
[ ] 术语和缩写首次出现时已定义

### 结构检查
[ ] 标题层级正确
[ ] 目录结构清晰
[ ] 交叉引用正确

### 格式检查
[ ] Markdown 语法正确
[ ] 代码高亮正确
[ ] 图片 alt 文本完整

### 一致性检查
[ ] 与项目其他文档风格一致
[ ] 术语使用统一
[ ] 版本号正确
"""

def quality_check(doc):
    """文档质量检查"""
    issues = []

    # 检查占位符
    if has_placeholders(doc):
        issues.append("存在未填充的占位符")

    # 检查代码示例
    if not code_examples_verified(doc):
        issues.append("代码示例未验证")

    # 检查链接
    if has_broken_links(doc):
        issues.append("存在失效链接")

    return issues
```

## Documentation Maintenance Process

### 版本管理

```python
class DocVersionManager:
    """文档版本管理"""

    def update_doc(self, doc_path, new_content, version):
        """
        文档更新流程
        """
        # 1. 创建备份
        self.backup(doc_path)

        # 2. 更新内容
        self.write(doc_path, new_content)

        # 3. 更新版本日志
        changelog = self.get_changelog()
        changelog.add_entry(version, new_content)

        # 4. 提交审核
        self.create_pr(doc_path, changelog)
```

### 发布流程

```yaml
documentation_release:
  steps:
    - name: 本地预览
      command: mkdocs serve

    - name: 拼写检查
      command: vale doc/

    - name: 链接检查
      command: mkdocs build --strict

    - name: 部署
      command: mkdocs gh-deploy
```

## Best Practices

### DO

1. **读者导向**: 始终考虑目标读者的背景和需求
2. **渐进式**: 从基础到深入，循序渐进
3. **示例丰富**: 每个概念都配有实际示例
4. **及时更新**: 代码变更后同步更新文档
5. **版本同步**: 文档版本与代码版本对应

### DON'T

1. **不要假设**: 不要假设读者了解上下文
2. **不要模糊**: 避免模糊的描述和指令
3. **不要过时**: 不要保留过时或错误的信息
4. **不要重复**: 避免重复内容，使用交叉引用
5. **不要孤立**: 文档应该与项目其他部分关联

## Associated Assets

| 类型 | 路径 |
|------|------|
| SCENARIO | `../../scenarios/document-project/SCENARIO.md` |
| PROMPT | `../../prompts/document-project.prompt.md` |
| AGENT | `../../agents/document-project.agent.md` |
| SKILL | `../../skills/document-project/SKILL.md` |


## Technical Specifications

> Detailed technical requirements and implementation guidelines for document-project.

### Required Tools
- [List required tools and frameworks]

### Environment Requirements
- [List environment prerequisites]

### Configuration Parameters
- [List key configuration parameters]


## Error Handling

> Common error scenarios and resolution strategies for document-project.

### Error Category 1
**Symptom**: Documentation is incomplete or outdated
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]

### Error Category 2
**Symptom**: Users report difficulty finding required information
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]


## Quality Standards

> Acceptance criteria and quality gates for document-project deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | Documentation completeness covers all required topics | Automated check |
| Standard 2 | Stale documentation rate is below 10% | Automated check |
| Standard 3 | User satisfaction rating is 4.0 or higher out of 5 | Automated check |
