---
name: apply-hotfix
description: "apply-hotfix execution prompt for E2E delivery workflow"
type: execution
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['prompt', 'ai-execution']
---
# Prompt: 紧急修复场景执行 Prompt

## Overview

本 Prompt 用于指导 AI Agent 执行紧急缺陷修复工作。

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
| `issue_id` | string | 是 | 问题编号 | "BUG-001" |
| `issue_title` | string | 是 | 问题标题 | "支付失败" |
| `severity` | enum | 是 | 严重等级 | P0/P1/P2 |
| `affected_services` | string[] | 是 | 影响服务 | ["支付服务"] |
| `affected_users` | number | 是 | 影响用户数 | 1000 |
| `reporter` | string | 是 | 上报人 | "监控系统" |
| `detection_time` | datetime | 是 | 发现时间 | "2024-01-15 14:00" |
| `first_occurrence` | datetime | 否 | 首次出现 | "2024-01-15 13:30" |

## Chain of Thought

```
1. [THINK] 理解问题 → 影响范围和严重性？
2. [THINK] 定位根因 → 问题出在哪里？
3. [THINK] 设计修复 → 如何快速修复？
4. [EXECUTE] 执行修复 → 代码修改
5. [VALIDATE] 验证修复 → 测试确认
6. [OUTPUT] 输出报告 → 修复总结
```

## Error Handling

### EH-1: 根因不明

```
IF 30分钟内无法定位根因
THEN
  1. 收集更多信息
  2. 尝试临时止血方案
  3. 升级到专家团队
END
```

## Output Validation

### 验证清单

```markdown
## Self-Validation Report

### V-001: 修复验证
- [ ] 问题已修复
- [ ] 无引入新问题
- [ ] 回归测试通过

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
handover_to_support:
  deliverable: "紧急修复报告"
  status: "成功/失败"

  summary:
    issue_id: string
    duration: minutes
    root_cause: string
    fix_description: string
```

## Constraints

1. **快速响应**: 必须立即响应
2. **最小化修复**: 只修复必要部分
3. **可回滚**: 修复必须可回滚

## Task Description

> Describe the specific task for the apply-hotfix scenario execution.
> AI must understand the context, objectives, and success criteria before proceeding.

## Execution Flow

> Step-by-step execution sequence for apply-hotfix

### Phase 1: Analysis
- Understand requirements and context
- Identify constraints and dependencies

### Phase 2: Execution
- Perform core apply-hotfix activities
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
## Hotfix Deliverables

### Summary
- Status: [completed | partial | blocked]
- Severity: [P0 | P1 | P2]
- Completion: [percentage]

### Key Outputs
1. **Hotfix Code**: Emergency fix with minimal change scope
2. **Test Results**: Validation results for the fix
3. **Deployment Package**: Release package and configuration
4. **Communication Notice**: Customer/user notification content
5. **Follow-up Plan**: Plan for permanent fix and regression testing

### Validation Checklist
- [ ] Hotfix resolves the target defect without regression
- [ ] Hotfix deploys within SLA for severity level
- [ ] All affected scenarios are regression tested
- [ ] Permanent fix is scheduled for next regular release

### Next Steps
- [ ] Deploy to production with monitoring
- [ ] Schedule permanent fix in backlog
```

