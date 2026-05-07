---
name: manage-tech-debt
description: "技术债务管理场景，识别、量化、跟踪和管理软件开发过程中累积的技术债务"
type: scenario
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['workflow', 'process']
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




## Error Handling (错误处理)

> **AI 遇到以下情况时必须按指定流程处理**

### 错误分类体系

| 级别 | 标识 | 描述 | 处理方式 |
|------|------|------|----------|
| P0 - Critical | ERR-CRITICAL | 阻塞性错误，无法继续 | 立即停止，升级人工处理 |
| P1 - Major | ERR-MAJOR | 严重错误，影响核心功能 | 尝试修复，失败则升级 |
| P2 - Minor | ERR-MINOR | 一般错误，可降级处理 | 记录并继续，后续修复 |
| P3 - Warning | ERR-WARNING | 警告信息，不影响执行 | 记录并继续 |

### Error Scenario 1: 通用错误处理

**识别信号**: 
- 检测到异常情况
- 验证失败

**处理流程**:
```
IF 检测到错误
THEN
  1. 识别错误类型和严重程度
  2. 记录错误详情
  3. 根据错误级别采取相应措施
  4. IF P0/P1 级别 THEN 升级到人工处理
  5. 更新状态并继续或停止
END
```

**降级方案**: 根据具体情况选择适当的降级策略

**升级条件**: P0 或 P1 级别错误

**错误日志格式**:
```yaml
error_log:
  error_id: "ERR-{timestamp}-XXX"
  timestamp: "{{ISO8601}}"
  level: "P0/P1/P2/P3"
  type: "{错误类型}"
  description: "{详细描述}"
  action_taken: "{已采取的行动}"
  result: "resolved/blocked/degraded/escalated"
```



## Quality Metrics

> Quality metrics for measuring scenario execution success.

| KPI | Target | Description |
|-----|--------|-------------|
| `DEBT-VISIBILITY` | 100% | 债务可见性：所有已知债务已登记 |
| `PAYDOWN-RATE` | ≥10%/quarter | 偿还率：每季度偿还债务比例 |
| `IMPACT-REDUCTION` | ≥15%/year | 影响降低：债务对交付的影响年降幅 |

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识



## Quality Metrics (质量指标)

### Key Performance Indicators (KPIs)

| KPI ID | 指标名称 | 目标值 | 计算公式 | 验证方法 | 权重 |
|--------|----------|--------|----------|----------|------|
| KPI-001 | COMPLETION-RATE | ≥95% | (已完成项/总项数) × 100% | 完成情况检查 | 30% |
| KPI-002 | QUALITY-SCORE | ≥85/100 | 综合质量评分 | 质量评估表 | 30% |
| KPI-003 | COMPLIANCE | 100% | (符合规范项/总检查项) × 100% | 规范检查清单 | 20% |
| KPI-004 | EFFICIENCY | 按时完成 | 实际时间/计划时间 | 时间跟踪 | 20% |

**综合评分计算**: 
```
Quality Score = (KPI-001 × 0.30) + (KPI-002 × 0.30) + (KPI-003 × 0.20) + (KPI-004 × 0.20)
合格: ≥70分 | 优秀: ≥85分 | 卓越: ≥95分
```

### Validation Checklist (验证清单)

**完整性验证 (Completeness)**:
- [ ] 所有必需内容已完成
- [ ] 无遗漏的关键步骤
- [ ] 交付物完整

**一致性验证 (Consistency)**:
- [ ] 术语和命名统一
- [ ] 风格一致
- [ ] 与其他资产协调

**准确性验证 (Accuracy)**:
- [ ] 信息准确无误
- [ ] 数据和计算正确
- [ ] 链接和引用有效

**可执行性验证 (Executability)**:
- [ ] 步骤清晰可执行
- [ ] 资源和要求明确
- [ ] 无模糊或不确定的内容

**规范性验证 (Compliance)**:
- [ ] 遵循标准和规范
- [ ] 符合最佳实践
- [ ] 满足合规要求



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


## Purpose

## Chain of Thought (思维链)

> **AI 必须按照以下思维链逐步执行**，每完成一步后进行自我验证

```
Step 1: [THINK] 理解任务目标和上下文
   ├─ 输入: 相关输入变量
   ├─ 思考: 任务的核心目标是什么？关键约束有哪些？
   ├─ 验证: 确认理解准确，无遗漏
   └─ 输出: 任务分析摘要
   ↓
Step 2: [ANALYZE] 分析需求和约束条件
   ├─ 输入: 任务分析摘要
   ├─ 思考: 有哪些关键决策点？可能的风险是什么？
   ├─ 验证: 分析全面，考虑了所有重要因素
   └─ 输出: 分析报告
   ↓
Step 3: [DESIGN] 设计解决方案
   ├─ 输入: 分析报告
   ├─ 思考: 最优方案是什么？有无备选方案？
   ├─ 验证: 方案可行且符合最佳实践
   └─ 输出: 设计方案
   ↓
Step 4: [IMPLEMENT] 执行和实施
   ├─ 输入: 设计方案
   ├─ 思考: 如何高质量地实施？需要注意什么？
   ├─ 验证: 实施符合设计规范
   └─ 输出: 实施成果
   ↓
Step 5: [VERIFY] 验证结果和质量
   ├─ 输入: 实施成果
   ├─ 执行: 质量检查和验证
   ├─ 验证: 满足所有验收标准
   └─ 输出: 验证报告
   ↓
Step 6: [HANDOVER] 准备交接
   ├─ 生成: Handover Context
   ├─ 更新: Global Context
   └─ 通知: 下一阶段 Agent
```




> Define the objectives and scope of the manage-tech-debt scenario.
>
> This scenario ensures systematic execution of manage-tech-debt activities with clear decision checkpoints and handover criteria.


## Prerequisites

- [ ] Prerequisite 1: [Description]
- [ ] Prerequisite 2: [Description]
- [ ] Prerequisite 3: [Description]


## Primary Assets

| Asset Type | Path | Description |
|------------|------|-------------|
| Scenario | `scenarios/manage-tech-debt/SCENARIO.md` | This scenario definition |
| Prompt | `prompts/manage-tech-debt.prompt.md` | Execution prompt |
| Instructions | `instructions/manage-tech-debt.instructions.md` | Technical instructions |
| Agent | `agents/manage-tech-debt.agent.md` | Responsible agent |
| Skill | `skills/manage-tech-debt/SKILL.md` | Domain skill |


### Handover Context Template

```yaml
handover:
  header:
    from_stage: "manage-tech-debt"
    to_stage: "unknown"
    handover_id: "HO-{{timestamp}}-{{sequence}}"
    timestamp: "{{ISO8601}}"
    prepared_by: "{{agent.name}}"
    
  summary:
    status: "completed/partial/blocked"
    completion_percentage: {{0-100}}
    quality_score: {{0-100}}
    
  artifacts:
    delivered:
      - name: "{{artifact_name}}"
        path: "{{file_path}}"
        version: "{{version}}"
        checksum: "{{SHA256}}"
      
  decisions:
    - id: "DC-XXX"
      description: "{{决策描述}}"
      rationale: "{{决策理由}}"
      alternatives_considered: ["选项1", "选项2"]
      
  open_issues:
    blocking: []
    non_blocking:
      - id: "ISSUE-XXX"
        description: "{{问题描述}}"
        
  risks:
    - id: "RISK-XXX"
      description: "{{风险描述}}"
      probability: "low/medium/high"
      impact: "low/medium/high"
      mitigation: "{{缓解措施}}"
      
  recommendations:
    - "{{建议1}}"
    - "{{建议2}}"
    
  quality_metrics:
    kpi_results:
      - kpi_id: "KPI-001"
        value: {{actual_value}}
        target: {{target_value}}
        status: "pass/fail"
```

