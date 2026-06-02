---
name: manage-change
description: "变更管理技能，提供变更评估和管理的方法论"
category: operations
type: skill
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['skill', 'knowledge']
---
# Change Management Skill

## Skill Overview

变更管理是确保项目变更可控、可追溯的过程。本技能提供变更评估、决策和实施的方法论。

## Prerequisites

1. 理解软件开发流程
2. 理解需求管理
3. 理解项目管理基础知识

## Knowledge Base

### 变更类型

| 类型 | 描述 | 影响程度 |
|------|------|----------|
| 新增 | 添加新功能 | 高 |
| 修改 | 更改现有功能 | 中-高 |
| 删除 | 移除功能 | 中 |
| 优化 | 性能或体验改进 | 低-中 |

### 影响分析维度

1. **功能影响**
   - 新增/修改/删除的功能
   - 对已有功能的影响
   - 对用户体验的影响

2. **技术影响**
   - 代码变更范围
   - 数据库变更
   - API 变更
   - 第三方依赖

3. **测试影响**
   - 新增测试用例
   - 回归测试范围
   - 测试环境变更

4. **文档影响**
   - 用户文档
   - 技术文档
   - 培训材料

### Decision框架

```
变更决策 = f(价值, 成本, 风险, 时间)

接受条件: 价值 > 成本 + 风险
```

### 变更优先级

| 优先级 | 条件 | 处理时间 |
|--------|------|----------|
| P0 | 影响核心功能，紧急 | 24小时内 |
| P1 | 影响重要功能 | 3天内 |
| P2 | 影响一般功能 | 1周内 |
| P3 | 影响小，可延迟 | 计划迭代 |

## Procedures

### 影响评估流程

1. 理解变更请求
2. 分解变更范围
3. 逐项分析影响
4. 评估影响程度
5. 汇总评估结果
6. 制定决策建议

### 变更评审流程

1. 准备评审材料
2. 组织评审会议
3. 讨论变更内容
4. 达成变更决策
5. 记录决策结果

## Tools & Resources

- 需求管理工具
- 影响分析模板
- 变更评审清单
- 版本控制系统

## Validation

### 变更评估检查

- [ ] 变更范围清晰
- [ ] 影响分析完整
- [ ] 成本估算合理
- [ ] 风险识别充分

### 变更实施检查

- [ ] 文档已更新
- [ ] 代码已实现
- [ ] 测试已通过
- [ ] 相关方已通知

## Examples

### Example：新增功能变更

**变更内容**：在用户管理模块新增批量导入功能

**影响分析**：
- 功能影响：新增批量导入功能
- 技术影响：新增导入接口、导入服务、数据验证
- 测试影响：新增导入测试用例、边界测试
- 文档影响：更新用户文档

**评估结果**：
- 工作量：5 人天
- 影响程度：中
- 建议：接受


## Core Knowledge

> Essential knowledge domain for manage-change execution.

### Domain Fundamentals
- [Core concept 1]
- [Core concept 2]
- [Core concept 3]

### Key Principles
1. [Principle 1]
2. [Principle 2]
3. [Principle 3]


## Best Practices

> Proven practices for manage-change excellence.

1. **Practice 1**: [Description and rationale]
2. **Practice 2**: [Description and rationale]
3. **Practice 3**: [Description and rationale]


## Anti-patterns (反模式)

> 与 Common Pitfalls 同义，执行时合并检查。

## Common Pitfalls

> Frequent mistakes to avoid during manage-change execution.

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
