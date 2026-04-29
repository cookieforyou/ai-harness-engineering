# Scenario: 发布准备 (Prepare Release)

## 概述

本场景用于准备版本发布，包括发布计划、变更评审、风险评估、回滚方案等。

## Chain of Thought

```
[THINK] 分析发布需求
├─ 确定发布范围和版本
├─ 识别关联系统和依赖
└─ 评估发布时间窗口

[ANALYZE] 制定发布计划
├─ 确定发布时间表
├─ 分配发布任务
└─ 准备回滚方案

[DESIGN] 设计发布流程
├─ 设计发布步骤
├─ 确定验证检查点
└─ 配置监控指标

[PREPARE] 准备发布资源
├─ 准备发布包/镜像
├─ 准备数据库变更
├─ 准备配置文件
├─ 通知相关方

[VERIFY] 验证发布就绪
├─ 验证环境和资源
├─ 验证回滚方案
└─ 确认沟通计划
```

## Decision Checkpoints

| 检查点 | 条件 | 决策 |
|--------|------|------|
| DC-001 | 发布评审 | 是否通过发布评审？ |
| DC-002 | 回滚方案 | 回滚方案是否就绪？ |
| DC-003 | 发布时间 | 确认发布时间窗口？ |

## Error Handling

| 错误类型 | 处理方式 |
|----------|----------|
| 发布包不完整 | 重新打包并验证 |
| 依赖未就绪 | 延迟发布时间 |
| 回滚失败 | 紧急故障响应 |
| 验证不通过 | 修复后重新验证 |

## Handover Criteria

- [x] 发布计划已审批
- [x] 发布包已验证
- [x] 回滚方案已测试
- [x] 监控告警已配置
- [x] 沟通计划已通知

## 关联资产

- **Prompt**: `prompts/prepare-release.prompt.md`
- **Instruction**: `instructions/prepare-release.instructions.md`
- **Agent**: `agents/release-manager.agent.md`
- **Skill**: `skills/prepare-release/SKILL.md`
