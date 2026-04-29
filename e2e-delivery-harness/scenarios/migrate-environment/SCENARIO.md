# Scenario: 环境迁移 (Migrate Environment)

## 概述

本场景用于将应用程序从一个环境迁移到另一个环境，包括开发、测试、预发布、生产环境之间的迁移。

## Chain of Thought

```
[ANALYZE] 分析迁移需求
├─ 确定源环境和目标环境
├─ 分析差异和依赖
└─ 评估迁移风险

[PLAN] 制定迁移计划
├─ 数据迁移策略
├─ 配置迁移策略
├─ 回滚方案

[PREPARE] 准备迁移
├─ 备份数据
├─ 准备配置文件
├─ 验证目标环境

[MIGRATE] 执行迁移
├─ 数据迁移
├─ 配置迁移
├─ 服务部署

[VERIFY] 验证迁移
├─ 功能验证
├─ 数据验证
├─ 监控验证
```

## Decision Checkpoints

| 检查点 | 条件 | 决策 |
|--------|------|------|
| DC-001 | 迁移方案 | 全量迁移还是增量迁移？ |
| DC-002 | 数据同步 | 在线迁移还是停机迁移？ |
| DC-003 | 回滚方案 | 是否需要保留回滚能力？ |

## Handover Criteria

- [x] 迁移计划已评审
- [x] 数据已备份
- [x] 迁移已执行
- [x] 验证已通过

## 关联资产

- **Prompt**: `prompts/migrate-environment.prompt.md`
- **Instruction**: `instructions/migrate-environment.instructions.md`
- **Agent**: `agents/devops-engineer.agent.md`
- **Skill**: `skills/migrate-environment/SKILL.md`
