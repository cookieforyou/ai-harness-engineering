# Instruction: 紧急修复技术规范

## 概述

本文档定义了紧急修复阶段的技术规范和执行标准。

## 紧急修复流程

```
问题报告 → 评估 → 定位 → 修复 → 验证 → 上线
```

## 响应时间要求

| 严重等级 | 响应时间 | 修复时间 | 上线时间 |
|----------|----------|----------|----------|
| P0 | 15 分钟 | 1 小时 | 2 小时 |
| P1 | 30 分钟 | 4 小时 | 8 小时 |
| P2 | 1 小时 | 24 小时 | 48 小时 |

## 关联资产

- **Scenario**: `scenarios/hotfix/SCENARIO.md`
- **Prompt**: `prompts/hotfix.prompt.md`
- **Agent**: `agents/hotfix-engineer.agent.md`
- **Skill**: `skills/hotfix/SKILL.md`
