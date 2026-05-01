# Technical Debt Management Skill

## Core Knowledge

### 1. Technical Debt Fundamentals

#### Definition
> "Technical debt is a concept in software development that reflects the implied cost of additional rework caused by choosing an easy solution now instead of a better approach that would take longer." - Ward Cunningham

#### Debt Metaphor
- **Principal**: 债务本金（代码质量问题本身）
- **Interest**: 利息（债务带来的额外成本）
- **Repayment**: 偿还（修复债务的行动）

#### Common Causes
- 赶进度牺牲代码质量
- 缺乏代码审查
- 技术选型不当
- 需求频繁变更
- 缺乏测试覆盖
- 文档缺失

### 2. Debt Categories

#### Code Debt
| Type | Description | Impact |
|------|-------------|--------|
| Duplicated Code | 复制粘贴 | 修改困难，bug 传播 |
| Long Method | 过长函数 | 难以理解和测试 |
| Large Class | 职责过多的类 | 难以维护和扩展 |
| Dead Code | 死代码 | 混淆和无效维护 |
| Magic Numbers | 魔法数字 | 缺乏可读性 |

#### Architecture Debt
| Type | Description | Impact |
|------|-------------|--------|
| Circular Dependency | 循环依赖 | 难以独立测试 |
| God Object | 上帝对象 | 紧耦合 |
| Missing Abstraction | 缺乏抽象 | 难以替换实现 |
| Premature Optimization | 过早优化 | 增加复杂度 |

#### Test Debt
| Type | Description | Impact |
|------|-------------|--------|
| Low Coverage | 覆盖不足 | bug 难以发现 |
| Brittle Tests | 脆弱测试 | CI 不稳定 |
| Test Logic Duplication | 测试逻辑重复 | 测试维护困难 |

#### Documentation Debt
| Type | Description | Impact |
|------|-------------|--------|
| Outdated Docs | 过期文档 | 误导开发者 |
| Missing Docs | 缺失文档 | 知识流失 |
| Comment Debt | 注释债务 | 代码难以理解 |

### 3. Quantification Methods

#### Simple Interest Model
```
Total Cost = Principal + (Interest × Time)

Example:
Principal = 3 days (to fix)
Interest = 0.5 days/month
Time = 6 months
Total Cost = 3 + (0.5 × 6) = 6 days
```

#### SonarQube Technical Debt Formula
```
Technical Debt = Remediation Cost / (Remediation Cost + Build Cost) × 100%
```

#### Weighted Score Model
```
Score = Σ (Occurrence × Complexity × Risk) / Σ Occurrence

Where:
- Occurrence: 出现次数
- Complexity: 修复复杂度 (1-5)
- Risk: 业务风险 (1-5)
```

### 4. Repayment Strategies

#### Boy Scout Rule
- 每次离开代码时比发现时更干净
- 适用于日常债务偿还
- 需要团队共识和标准

#### Scheduled Debt Sprints
- 专门的时间段处理债务
- 通常每季度 1-2 周
- 适合大规模债务

#### 20% Investment Time
- 每周分配固定时间
- 适用于持续债务管理
- 需要管理层支持

#### Feature-Driven Refactoring
- 将重构嵌入功能开发
- 适用于关联债务
- 需要良好规划

### 5. Refactoring Techniques

#### Small-Scale Refactoring
| Technique | Description |
|-----------|-------------|
| Extract Method | 提取重复代码 |
| Rename Variable | 改进命名 |
| Inline Method | 简化调用 |
| Remove Dead Code | 删除无用代码 |
| Introduce Parameter Object | 参数对象化 |

#### Medium-Scale Refactoring
| Technique | Description |
|-----------|-------------|
| Extract Class | 拆分大类 |
| Move Method | 移动方法 |
| Replace Conditional with Polymorphism | 条件多态化 |
| Introduce Null Object | 空对象模式 |

#### Large-Scale Refactoring
| Technique | Description |
|-----------|-------------|
| Extract Module/Library | 提取模块 |
| Strangler Fig Pattern | 绞杀者模式 |
| Branch by Abstraction | 抽象分支 |
| Parallel Change | 并行变更 |

### 6. Prevention Practices

#### Code Review Standards
- 强制代码审查
- 债务审查清单
- 质量门禁
- 小步提交

#### Quality Gates in CI
```yaml
gates:
  max_complexity: 10
  min_coverage: 80%
  max_duplication: 3%
  max_critical_issues: 0
```

#### Agile Practices
- Sprint 回顾中的债务讨论
- Definition of Done 包含代码质量
- 技术故事纳入 Sprint
- 债务任务可视化

## Best Practices

1. **Track Debt**: 建立债务清单，持续跟踪
2. **Quantify Impact**: 用数据展示债务成本
3. **Prioritize**: 聚焦高影响债务
4. **Plan Regular Time**: 分配专门时间偿还
5. **Prevent Accumulation**: 建立预防机制
6. **Communicate**: 与业务方沟通债务风险
7. **Celebrate Progress**: 展示债务减少的成果
