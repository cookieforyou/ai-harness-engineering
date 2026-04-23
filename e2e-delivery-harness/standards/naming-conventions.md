# Naming Conventions - 命名规范

## 概述

本文档定义了 E2E Delivery Harness 资产库的命名规范，确保资产命名的一致性和可识别性。

## 通用命名原则

1. **清晰性**：名称应清晰表达资产内容和用途
2. **一致性**：同类资产采用统一的命名模式
3. **简洁性**：避免不必要的冗长
4. **可搜索性**：支持通过名称快速定位资产

## 文件命名

### 目录命名

| 目录 | 命名规范 | 示例 |
|------|----------|------|
| 角色目录 | agents | agents |
| 指令目录 | instructions | instructions |
| 提示词目录 | prompts | prompts |
| 技能目录 | skills | skills |
| 场景目录 | scenarios | scenarios |
| 规范目录 | standards | standards |
| 模板目录 | templates | templates |
| 评估目录 | evaluations | evaluations |

### 资产文件命名

#### Agent 文件

```regex
^[a-z][a-z0-9-]*\.agent\.md$

示例：
- requirement-analyst.agent.md
- system-designer.agent.md
- developer.agent.md
```

#### Skill 目录与文件

```regex
# 目录
^[a-z][a-z0-9-]*$

# 文件
SKILL.md

示例：
skills/
├── requirement-analysis/
│   └── SKILL.md
├── system-design/
│   └── SKILL.md
```

#### Instruction 文件

```regex
^[a-z][a-z0-9-]*\.instructions\.md$

示例：
- requirement-analysis.instructions.md
- system-design.instructions.md
```

#### Prompt 文件

```regex
^[a-z][a-z0-9-]*\.prompt\.md$

示例：
- analyze-requirement.prompt.md
- design-system.prompt.md
```

#### Scenario 目录与文件

```regex
# 目录
^[a-z][a-z0-9-]*$

# 文件
SCENARIO.md

示例：
scenarios/
├── requirement-analysis/
│   └── SCENARIO.md
├── system-design/
│   └── SCENARIO.md
```

## 变量命名

### YAML 元数据

```yaml
name: <kebab-case>        # 名称
description: <string>    # 描述
category: <kebab-case>    # 分类
version: <semver>        # 版本
```

### Markdown 标题

```markdown
# 页面标题 (Title Case)
## 二级标题 (Title Case)
### 三级标题 (Title Case)
```

## 标签命名

### 标签格式

```regex
^[a-z][a-z0-9-]*$

示例：
- requirement
- design
- development
- testing
- deployment
```

### 常用标签

| 标签 | 用途 |
|------|------|
| requirement | 需求相关 |
| design | 设计相关 |
| development | 开发相关 |
| testing | 测试相关 |
| deployment | 部署相关 |
| monitoring | 监控相关 |
| critical | 关键资产 |
| deprecated | 已废弃 |

## 命名检查清单

### 文件命名检查

- [ ] 使用小写字母
- [ ] 使用连字符分隔单词
- [ ] 包含正确的文件扩展名
- [ ] 不包含特殊字符
- [ ] 不超过 100 字符

### 目录命名检查

- [ ] 使用小写字母
- [ ] 使用连字符分隔单词
- [ ] 不包含空格
- [ ] 不以数字开头
- [ ] 不超过 50 字符

## 反面示例

```markdown
# 错误
Requirement Analyst.md        # 包含空格
requirement_analysis.md       # 使用下划线
REQ-001.md                   # 使用大写
analyze requirement.md       # 包含空格

# 正确
requirement-analyst.agent.md
requirement-analysis.instructions.md
```

## 多语言支持

### 文件命名（中文环境）

```regex
^[a-z][a-z0-9-]*\.[a-z]{2}\.md$

示例：
- introduction.zh.md
- usage.zh.md
- introduction.en.md
- usage.en.md
```

### 资源标识（统一英文）

```yaml
name: requirement-analysis  # 始终使用英文
description: "需求分析相关"  # 描述可使用本地语言
```
