---
name: migrate-data
description: "migrate data execution prompt for E2E delivery workflow"
type: execution
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['prompt', 'ai-execution']
---
# Prompt: 数据迁移场景执行 Prompt

## Overview

本 Prompt 用于指导 AI Agent 执行数据迁移流程，包括迁移评估、方案设计、迁移执行和数据验证。

## Input Variables

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




| 变量名 | 类型 | 必填 | 描述 | 示例 |
|--------|------|------|------|------|
| `source_system` | string | 是 | 源系统名称 | "旧订单系统" |
| `target_system` | string | 是 | 目标系统名称 | "新订单系统" |
| `migration_scope` | object | 是 | 迁移范围 | 见 MigrationScope 结构 |
| `data_volume` | object | 是 | 数据量评估 | 见 DataVolume 结构 |
| `migration_window` | datetime | 是 | 迁移时间窗口 | "2024-01-15 02:00" |
| `allowed_downtime` | number | 是 | 允许停机时间(小时) | 4 |
| `migration_strategy` | enum | 是 | 迁移策略 | BIG_BANG/PARALLEL/PHASE |

### MigrationScope 结构

```typescript
interface MigrationScope {
  tables: string[];              // 迁移表列表
  records_estimate: number;       // 预估记录数
  total_size_gb: number;         // 总数据大小(GB)
  dependencies: string[];         // 依赖关系
  critical_data: string[];        // 关键数据
}
```

### DataVolume 结构

```typescript
interface DataVolume {
  tables: {
    name: string;
    rows: number;
    size_mb: number;
    growth_rate: number;        // 月增长率 %
  }[];
  total_rows: number;
  total_size_gb: number;
}
```

## Chain of Thought

```
1. [THINK] 理解系统 → 源和目标系统架构？
2. [THINK] 评估数据 → 数据量和复杂度？
3. [THINK] 设计方案 → 迁移策略和步骤？
4. [THINK] 准备脚本 → 数据清洗转换规则？
5. [EXECUTE] 执行迁移 → 按计划执行
6. [VALIDATE] 验证数据 → 完整性准确性
7. [OUTPUT] 输出报告 → 迁移结果
```

## Error Handling

### EH-1: 数据不一致

```
IF 校验发现数据不一致
THEN
  1. 记录不一致数据详情
  2. 分析不一致原因
  3. 修复或重新迁移
  4. 重新执行校验
END
```

### EH-2: 迁移超时

```
IF 迁移任务超时
THEN
  1. 检查任务执行状态
  2. 评估剩余工作量
  3. 决定继续或回滚
  4. 通知相关方
END
```

## Output Validation

### 验证清单

```markdown
## Self-Validation Report

### V-001: 数据完整性
- [ ] 记录数一致
- [ ] 数据量一致
- [ ] 校验通过

### V-002: 数据准确性
- [ ] 字段值正确
- [ ] 业务规则正确
- [ ] 关联关系正确

### V-003: 功能验证
- [ ] 查询功能正常
- [ ] 写入功能正常
- [ ] 业务逻辑正常

### 验证结果
- 验证通过: [是/否]
```



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



## Handover 准备

```yaml
handover_to_production:
  deliverable: "数据迁移报告"
  status: "成功/失败/部分成功"

  summary:
    tables_migrated: N
    records_migrated: N
    duration: minutes
    success_rate: percentage

  validation:
    completeness: PASS/FAIL
    accuracy: PASS/FAIL
    integrity: PASS/FAIL
```

## Constraints

1. **零丢失**: 关键数据不能丢失
2. **可回滚**: 必须有回滚方案
3. **可追溯**: 迁移过程必须可追溯

## Task Description

> Describe the specific task for the migrate-data scenario execution.
> AI must understand the context, objectives, and success criteria before proceeding.

## Execution Flow

> Step-by-step execution sequence for migrate-data

### Phase 1: Analysis
- Understand requirements and context
- Identify constraints and dependencies

### Phase 2: Execution
- Perform core migrate-data activities
- Apply best practices and standards

### Phase 3: Validation
- Verify outputs against acceptance criteria
- Ensure completeness and quality



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



## Output Format

```markdown
## Data Migration Deliverables

### Summary
- Status: [completed | partial | blocked]
- Completion: [percentage]

### Key Outputs
1. **Migration Plan**: Detailed execution plan with timelines
2. **Migration Scripts**: ETL/migration scripts with rollback capability
3. **Validation Queries**: Data consistency check SQL/scripts
4. **Rollback Procedures**: Step-by-step rollback instructions
5. **Performance Estimates**: Migration duration and resource projections

### Validation Checklist
- [ ] Data integrity validation passes 100%
- [ ] Downtime is within budget constraints
- [ ] Rollback capability is maintained throughout migration
- [ ] All downstream consumers are notified and validated

### Next Steps
- [ ] Execute migration in approved window
- [ ] Validate downstream systems post-migration
```

