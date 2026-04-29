# Scenario: 性能优化 (Optimize Performance)

## 概述

本场景用于识别和解决系统性能瓶颈，包括代码优化、数据库优化、缓存优化、网络优化等。

## Chain of Thought

```
[ANALYZE] 分析性能问题
├─ 确定性能指标基线
├─ 识别性能瓶颈
└─ 分析瓶颈原因

[MEASURE] 测量性能数据
├─ 性能分析工具
├─ 性能测试
└─ 监控数据

[OPTIMIZE] 实施优化
├─ 代码级优化
├─ 数据库优化
├─ 缓存优化
├─ 并发优化

[VERIFY] 验证优化效果
├─ 性能回归测试
├─ 压力测试
└─ 稳定性测试
```

## Decision Checkpoints

| 检查点 | 条件 | 决策 |
|--------|------|------|
| DC-001 | 瓶颈定位 | 哪个环节最慢？ |
| DC-002 | 优化方案选择 | 缓存/索引/重构？ |
| DC-003 | 优化优先级 | 哪个收益最大？ |

## Handover Criteria

- [x] 性能瓶颈已定位
- [x] 优化方案已实施
- [x] 性能指标已达标
- [x] 性能回归测试通过

## 关联资产

- **Prompt**: `prompts/optimize-performance.prompt.md`
- **Instruction**: `instructions/optimize-performance.instructions.md`
- **Agent**: `agents/performance-engineer.agent.md`
- **Skill**: `skills/optimize-performance/SKILL.md`
