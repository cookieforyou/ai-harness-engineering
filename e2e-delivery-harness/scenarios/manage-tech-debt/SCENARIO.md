---
name: manage-tech-debt
type: scenario
version: 1.0.0
description: 技术债务管理场景，识别、量化、跟踪和管理软件开发过程中累积的技术债务
trigger: 当需要进行技术债务清理或优化时触发
agent: solution-architect
phase: implement-feature
tags:
  - technical-debt
  - code-quality
  - refactoring
  - maintainability
input:
  - project_name
  - project_path
  - debt_categories
  - priority_threshold
output:
  - debt-inventory.md
  - repayment-plan.md
  - refactoring-guide.md
  - quality-metrics.md
---

# Technical Debt Management Scenario

## Overview

技术债务是指为了快速交付而在代码质量、设计或架构上做出的妥协，如同金融债务一样，技术债务也会产生"利息"，随着时间推移影响开发效率和系统稳定性。本场景帮助识别、量化和管理技术债务。

## Trigger Conditions

- 常规技术债务审查（每季度）
- 新功能开发前的预处理
- 系统性能下降时
- 代码审查中发现大量债务
- 团队合并或代码交接时
- 技术升级规划前

## Chain of Thought

```
1. 扫描代码库识别债务
   ↓
2. 分类和量化债务
   ↓
3. 评估债务影响和偿还成本
   ↓
4. 制定偿还策略
   ↓
5. 优先级排序
   ↓
6. 执行偿还计划
   ↓
7. 建立监控机制
   ↓
8. 预防新债务产生
```

## Debt Categories

### Category 1: 代码债务
| Type | Description | Examples |
|------|-------------|----------|
| 代码重复 | 复制粘贴代码 | 相似函数多次实现 |
| 长函数 | 函数过长 | 超过 100 行的函数 |
| 大类 | 类职责过多 | God Class |
| 命名不当 | 变量/函数命名混乱 | a, b, temp 等 |

### Category 2: 架构债务
| Type | Description | Examples |
|------|-------------|----------|
| 紧耦合 | 模块间依赖过强 | 循环依赖 |
| 缺乏抽象 | 直接依赖实现 | 无接口抽象 |
| 扩张性差 | 难以扩展功能 | 硬编码值 |

### Category 3: 测试债务
| Type | Description | Examples |
|------|-------------|----------|
| 低覆盖 | 测试覆盖率不足 | < 70% |
| 脆弱测试 | 测试不稳定 | Flaky tests |
| 缺乏集成测试 | 仅单元测试 | 端到端缺失 |

### Category 4: 文档债务
| Type | Description | Examples |
|------|-------------|----------|
| 过期文档 | 文档与代码不符 | 过时的 API 文档 |
| 缺失文档 | 关键代码无注释 | 复杂算法无说明 |
| 无架构图 | 系统设计无图示 | 白板图未保存 |

## Decision Checkpoints

### Checkpoint 1: 债务识别
- 是否覆盖所有债务类型？
- 债务定义是否清晰？
- 量化标准是否一致？

### Checkpoint 2: 影响评估
- 债务对业务的影响？
- 债务对开发效率的影响？
- 债务的风险等级？

### Checkpoint 3: 偿还决策
- 立即偿还还是计划偿还？
- 增量偿还还是大规模重构？
- 是否需要额外资源？

### Checkpoint 4: 预防策略
- 如何防止新债务累积？
- 代码审查标准是否足够？
- 自动化检查是否到位？

## Error Handling

| Error Scenario | Handling Strategy |
|----------------|-------------------|
| 债务过多无从下手 | 分批处理，聚焦高影响债务 |
| 偿还影响正常迭代 | 纳入 Sprint 规划，分配固定时间 |
| 团队抗拒重构 | 展示债务成本，争取管理层支持 |
| 偿还后引入新问题 | 小步前进，充分测试，TDD |

## Handover Criteria

- [ ] 技术债务清单完整
- [ ] 每项债务已量化评分
- [ ] 偿还计划已评审
- [ ] 预防机制已建立
- [ ] 监控指标已定义
- [ ] 文档已更新

## Expected Artifacts

| Artifact | Description |
|----------|-------------|
| debt-inventory.md | 完整技术债务清单 |
| repayment-plan.md | 偿还计划和优先级 |
| refactoring-guide.md | 重构指南和最佳实践 |
| quality-metrics.md | 质量指标基线和目标 |

## Related Scenarios

- [implement-feature](./implement-feature/SCENARIO.md) - 功能实现
- [review-code](./review-code/SCENARIO.md) - 代码审查
- [review-design](./review-design/SCENARIO.md) - 设计审查
- [verify-test](./verify-test/SCENARIO.md) - 测试验证
