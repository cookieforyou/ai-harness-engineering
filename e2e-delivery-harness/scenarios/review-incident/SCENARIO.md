---
name: review-incident
description: "Review Incident scenario for the E2E delivery lifecycle"
type: scenario
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['workflow', 'process']
---
# Incident Review Scenario

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

对已解决的故障进行复盘分析，找出根本原因，制定改进措施，防止同类故障再次发生。

### Step-by-Step Reasoning

**Step 1: 故障还原**
- 问：故障是如何发生和发展的？
- 验证：收集时间线
- 检查：关键节点

**Step 2: 原因分析**
- 问：直接原因是什么？
- 验证：技术层面分析
- 检查：操作记录

**Step 3: 根因识别**
- 问：根本原因是什么？
- 验证：5 Why 分析
- 检查：系统性问题

**Step 4: 影响评估**
- 问：故障影响了什么？
- 验证：用户、数据、业务
- 检查：损失评估

**Step 5: 改进制定**
- 问：如何防止再次发生？
- 验证：可执行性
- 检查：资源需求

## Error Handling

### EH-1: 原因不明确

- **识别信号**：无法确定根本原因
- **处理方式**：
  1. 收集更多证据
  2. 咨询相关专家
  3. 进行更深入分析
- **升级条件**：需要额外资源

### EH-2: 改进措施冲突

- **识别信号**：改进措施之间有冲突
- **处理方式**：
  1. 评估优先级
  2. 制定实施顺序
  3. 协调相关方
- **升级条件**：需要管理层决策

### EH-3: 责任归属争议

- **识别信号**：团队对责任有争议
- **处理方式**：
  1. 聚焦问题而非责任
  2. 关注系统性改进
  3. 达成共识
- **升级条件**：影响复盘结论

### 产出清单

1. **故障复盘报告**：完整的故障分析
2. **根本原因分析**：RCA 文档
3. **改进措施清单**：action items
4. **跟踪计划**：改进落地计划

### 输出格式

```markdown
### 1. 故障概述
- 故障编号：
- 故障时间：
- 恢复时间：
- 影响范围：
- 严重程度：

### 2. 故障时间线
...

### 3. 根本原因分析 (RCA)
...

### 4. 影响评估
...

### 5. 改进措施

| 措施 | 负责人 | 完成日期 | 状态 |
|------|--------|----------|------|
| | | | |

### 6. 经验教训
...
```

## Prerequisites

### 必需前置条件

1. 故障已完全恢复
2. 相关日志可用
3. 关键人员可用

### 可选前置条件

1. 故障报告初稿
2. 相关监控数据
3. 历史类似案例

### 阶段准入

- [ ] 故障已完全恢复
- [ ] 关键人员参与
- [ ] 数据已收集

### 阶段准出

- [ ] 根本原因已确定
- [ ] 改进措施已制定
- [ ] 责任人已确认

## Decision Checkpoints

| ID | 决策点 | 触发条件 | 决策选项 | 选择标准 | 记录位置 |
|----|--------|----------|----------|----------|----------|
| DC-001 | 复盘范围 | 事件关闭后 | 完整复盘 / 轻量复盘 | 严重级别与影响 | Postmortem 大纲 |
| DC-002 | 根因确认 | 分析完成后 | 已确认 / 待验证 | 5 Whys + 证据链 | 根因分析 |
| DC-003 | 改进项优先级 | 行动项列出后 | P0 立即 / 排期实施 | 风险降低幅度 | 改进 backlog |

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
| `POSTMORTEM-COMPLETION` | 100% | 复盘完成率：所有P0/P1有复盘 |
| `ACTION-CLOSURE` | ≥90% | 措施关闭率：改进措施按时关闭 |
| `RECURRENCE-RATE` | ≤5% | 复发率：同类事件再次发生比例 |

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识

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

## Handover Criteria (交接标准)

| 条件项 | 状态 | 说明 |
|--------|------|------|
| 复盘报告 | ☐ | 完整归档 |
| 根本原因 | ☐ | 5 Why 完成 |
| 改进措施 | ☐ | SMART 化 |
| 责任人 | ☐ | 已确认 |

## Workflow

```
1. 收集故障信息
2. 重构故障时间线
3. 分析直接原因
4. 识别根本原因
5. 评估影响
6. 制定改进措施
7. 编写复盘报告
8. 跟踪改进落地
```

## Related Scenarios

- **Related**: [../respond-incident/](../respond-incident/) - Incident Response
- **Related**: [../plan-disaster-recovery/](../plan-disaster-recovery/) - Disaster Recovery Planning

### Handover Context Template

```yaml
handover:
  header:
    from_stage: "review-incident"
    to_stage: "monitor-operate"
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
