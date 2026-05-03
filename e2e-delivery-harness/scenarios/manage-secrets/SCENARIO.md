# Scenario: 密钥管理 (Manage Secrets)

## 概述

本场景用于管理和保护应用程序密钥、凭证、证书等敏感信息，包括密钥生成、存储、轮换、审计等。

## Chain of Thought

```
[THINK] 分析密钥需求
├─ 识别需要管理的密钥类型
├─ 评估密钥安全等级
└─ 确定密钥使用场景

[ANALYZE] 设计密钥管理方案
├─ 选择密钥管理服务
├─ 设计密钥存储架构
├─ 规划密钥生命周期

[DESIGN] 设计密钥访问策略
├─ 设计访问控制策略
├─ 配置密钥权限
├─ 规划密钥轮换

[IMPLEMENT] 实现密钥管理
├─ 部署密钥管理服务
├─ 配置密钥存储
├─ 实现密钥访问接口

[VERIFY] 验证密钥安全
├─ 密钥访问审计
├─ 密钥轮换测试
└─ 密钥恢复测试
```

## Decision Checkpoints

| 检查点 | 条件 | 决策 |
|--------|------|------|
| DC-001 | 密钥管理服务选型 | Vault/云 KMS/自建？ |
| DC-002 | 密钥存储位置 | 本地/云服务/混合？ |
| DC-003 | 密钥轮换策略 | 自动轮换/手动轮换？ |

## Error Handling

| 错误类型 | 处理方式 |
|----------|----------|
| 密钥访问失败 | 检查权限、重试 |
| 密钥过期 | 自动续期或重新生成 |
| 密钥泄露 | 立即轮换、审计 |
| 密钥服务不可用 | 降级到本地缓存 |

## Handover Criteria

- [x] 密钥管理服务部署完成
- [x] 密钥访问策略已配置
- [x] 密钥轮换机制已设置
- [x] 密钥审计日志已启用
- [x] 密钥恢复方案已测试

## 关联资产

- **Prompt**: `prompts/manage-secrets.prompt.md`
- **Instruction**: `instructions/manage-secrets.instructions.md`
- **Agent**: `agents/manage-secrets.agent.md`
- **Skill**: `skills/manage-secrets/SKILL.md`


## Purpose

> Define the objectives and scope of the manage-secrets scenario.
>
> This scenario ensures systematic execution of manage-secrets activities with clear decision checkpoints and handover criteria.


## Prerequisites

- [ ] Prerequisite 1: [Description]
- [ ] Prerequisite 2: [Description]
- [ ] Prerequisite 3: [Description]


## Primary Assets

| Asset Type | Path | Description |
|------------|------|-------------|
| Scenario | `scenarios/manage-secrets/SCENARIO.md` | This scenario definition |
| Prompt | `prompts/manage-secrets.prompt.md` | Execution prompt |
| Instructions | `instructions/manage-secrets.instructions.md` | Technical instructions |
| Agent | `agents/manage-secrets.agent.md` | Responsible agent |
| Skill | `skills/manage-secrets/SKILL.md` | Domain skill |
