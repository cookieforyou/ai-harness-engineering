# Scenario: API 集成 (Integrate API)

## 概述

本场景用于集成第三方 API 或内部服务 API，包括接口对接、认证授权、数据转换、错误处理等。

## Chain of Thought

```
[THINK] 分析 API 需求
├─ 识别需要集成的 API
├─ 了解 API 规范和限制
└─ 评估技术可行性

[ANALYZE] 设计集成方案
├─ 分析 API 认证方式
├─ 设计数据映射规则
├─ 规划错误处理策略

[DESIGN] 设计接口层
├─ 定义内部接口抽象
├─ 设计重试和熔断机制
├─ 规划限流策略

[IMPLEMENT] 实现集成代码
├─ 实现 API 客户端封装
├─ 实现数据转换逻辑
├─ 实现错误处理和日志

[VERIFY] 验证集成正确性
├─ 单元测试覆盖
├─ 集成测试验证
└─ 性能基准测试
```

## Decision Checkpoints

| 检查点 | 条件 | 决策 |
|--------|------|------|
| DC-001 | API 规范确认 | 是否有完整的 API 文档？ |
| DC-002 | 认证方式确认 | OAuth/ApiKey/JWT？ |
| DC-003 | 错误处理策略 | 重试/降级/熔断？ |

## Error Handling

| 错误类型 | 处理方式 |
|----------|----------|
| 网络超时 | 指数退避重试 |
| API 限流 | 等待后重试或降级 |
| 认证失败 | 检查凭证、重新获取 Token |
| 服务不可用 | 降级到本地缓存 |

## Handover Criteria

- [x] API 客户端封装完成
- [x] 数据映射逻辑实现
- [x] 错误处理机制完善
- [x] 单元测试覆盖率 ≥ 80%
- [x] 集成文档已编写

## 关联资产

- **Prompt**: `prompts/integrate-api.prompt.md`
- **Instruction**: `instructions/integrate-api.instructions.md`
- **Agent**: `agents/api-integration-engineer.agent.md`
- **Skill**: `skills/integrate-api/SKILL.md`
