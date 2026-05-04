---
name: code-review
description: 代码审查技能，提供代码评审的方法论和最佳实践
type: skill
version: "1.1.0"
stage: development
---

# Code Review Skill

## Skill Overview

代码审查是保证代码质量的重要手段。本技能提供代码审查的方法论、检查清单和最佳实践。

## Prerequisites

1. 掌握至少一门编程语言
2. 理解编码规范
3. 理解基本设计模式

## Knowledge Base

### 审查维度

| 维度 | 检查内容 | 优先级 |
|------|----------|--------|
| 规范 | 命名、格式、注释 | 高 |
| 质量 | 复杂度、耦合、内聚 | 高 |
| 安全 | 注入、权限、敏感数据 | 高 |
| 测试 | 覆盖、边界、异常 | 中 |
| 性能 | 时间复杂度、资源使用 | 中 |

### 常见问题类型

1. **规范问题**
   - 命名不规范
   - 代码格式不一致
   - 注释缺失或过时

2. **质量问题**
   - 函数过长
   - 圈复杂度过高
   - 过度耦合
   - 重复代码

3. **安全问题**
   - SQL 注入
   - XSS 漏洞
   - 权限绕过
   - 敏感数据泄露

4. **测试问题**
   - 测试覆盖不足
   - 边界条件未覆盖
   - 测试依赖外部环境

### 问题优先级

| 级别 | 描述 | 处理要求 |
|------|------|----------|
| Critical | 安全漏洞、致命错误 | 必须修复 |
| High | 功能错误、性能问题 | 应该修复 |
| Medium | 代码规范、可读性 | 建议修复 |
| Low | 代码风格、注释 | 可选修复 |

## Procedures

### 审查流程

1. 理解变更目的
2. 阅读相关代码
3. 逐文件审查
4. 标注问题
5. 给出结论

### 审查技巧

1. **先理解，后批评**
   - 先理解代码意图
   - 再评估实现方式

2. **聚焦重点**
   - 优先检查关键路径
   - 关注风险点

3. **提供建议**
   - 不仅指出问题
   - 还要提供解决方案

## Tools & Resources

- 代码审查工具
- 静态分析工具
- 编码规范文档
- 安全检查清单

## Validation

### 审查完整性检查

- [ ] 所有变更文件已审查
- [ ] 所有问题已标注
- [ ] 优先级已设置
- [ ] 建议已提供

### 审查质量检查

- [ ] 问题描述准确
- [ ] 优先级合理
- [ ] 建议可行

## Examples

### Example：SQL 注入检查

**代码**：
```python
query = f"SELECT * FROM users WHERE name = '{name}'"
```

**问题**：
- 类型：安全漏洞
- 级别：Critical
- 描述：直接拼接用户输入，存在 SQL 注入风险

**建议**：
```python
query = "SELECT * FROM users WHERE name = %s"
cursor.execute(query, (name,))
```


## Core Knowledge

> Essential knowledge domain for review-code execution.

### Domain Fundamentals
- [Core concept 1]
- [Core concept 2]
- [Core concept 3]

### Key Principles
1. [Principle 1]
2. [Principle 2]
3. [Principle 3]


## Best Practices

> Proven practices for review-code excellence.

1. **Practice 1**: [Description and rationale]
2. **Practice 2**: [Description and rationale]
3. **Practice 3**: [Description and rationale]


## Common Pitfalls

> Frequent mistakes to avoid during review-code execution.

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
