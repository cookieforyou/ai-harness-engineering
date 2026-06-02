---
name: manage-change
description: "Manage Change scenario for the E2E delivery lifecycle"
type: scenario
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['workflow', 'process']
---
# Change Management Scenario

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




管理需求变更请求，评估变更影响，制定变更实施计划，确保变更可控可追溯。

## Chain of Thought (思维链)

```
THINK: 理解变更请求
   ↓
THINK: 评估变更影响
   ↓
THINK: 制定决策方案
   ↓
THINK: 规划实施步骤
   ↓
THINK: 更新相关文档
   ↓
THINK: 沟通变更计划
```

### Step-by-Step Reasoning

**Step 1: 变更理解**
- 问：变更的背景和原因是什么？
- 验证：与变更发起人确认
- 检查：变更范围是否清晰

**Step 2: 影响评估**
- 问：变更会影响哪些部分？
- 验证：逐项分析影响
- 检查：是否需要重新设计

**Step 3: 决策制定**
- 问：接受/拒绝/延迟的理由？
- 验证：权衡利弊
- 检查：决策是否合理

**Step 4: 实施规划**
- 问：如何在不影响进度的情况下实施？
- 验证：评估资源需求
- 检查：是否有风险

## Error Handling

### EH-1: 变更范围蔓延

- **识别信号**：变更范围不断扩大
- **处理方式**：
  1. 明确原变更范围
  2. 将扩展部分作为新变更
  3. 重新评估
- **升级条件**：影响核心功能

### EH-2: 变更与现有设计冲突

- **识别信号**：变更与已实现功能冲突
- **处理方式**：
  1. 分析冲突点
  2. 评估重构成本
  3. 考虑替代方案
- **升级条件**：需要大量返工

### EH-3: 变更影响无法评估

- **识别信号**：无法确定变更影响
- **处理方式**：
  1. 进行更深入分析
  2. 咨询相关专家
  3. 分阶段实施
- **升级条件**：影响决策

## Primary Assets

- **Agent**: [../../agents/manage-change.agent.md](../../agents/manage-change.agent.md)
- **Instruction**: [../../instructions/manage-change.instructions.md](../../instructions/manage-change.instructions.md)
- **Prompt**: [../../prompts/manage-change.prompt.md](../../prompts/manage-change.prompt.md)

## Expected Output

### 产出清单

1. **变更评估报告**：变更影响的完整分析
2. **变更决策**：接受/拒绝/延迟的决策
3. **实施计划**：变更实施的时间表
4. **更新文档**：需求规格和相关文档

### 输出格式

```markdown
## Change Assessment Report

### 1. 变更信息
- 变更编号：
- 发起人：
- 日期：
- 状态：

### 2. 变更描述
...

### 3. 影响评估
...

### 4. 变更决策
...

### 5. 实施计划
...

### 6. 更新记录
...
```

## Prerequisites

### 必需前置条件

1. 有明确的变更请求
2. 有原始需求文档
3. 有相关干系人

### 可选前置条件

1. 变更影响的相关分析
2. 类似的变更案例

## Quality Gates

### 阶段准入

- [ ] 有正式的变更请求
- [ ] 变更描述清晰
- [ ] 变更原因明确

### 阶段准出

- [ ] 变更评估完成
- [ ] 变更决策已做出
- [ ] 实施计划已制定
- [ ] 相关文档已更新

## Decision Checkpoints

| ID | 决策点 | 触发条件 | 决策选项 | 选择标准 | 记录位置 |
|----|--------|----------|----------|----------|----------|
| DC-001 | 范围确认 | 执行启动前 | 继续 / 缩小范围 / 升级 | 与上游 Handover 一致 | 执行记录 |
| DC-002 | 质量门禁 | 产出验证前 | 修复后继续 / 记录 open_issues | Scenario KPI ≥70 | 验证报告 |
| DC-003 | 交接准出 | 阶段完成前 | 完成交接 / 部分交接 / 阻塞 | Handover 必填字段齐全 | Handover YAML |


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
| `CHANGE-SUCCESS` | ≥95% | 变更成功率：按计划完成且无回退 |
| `APPROVAL-SLA` | ≤24h | 审批SLA：提交到批准时间 |
| `INCIDENT-CORRELATION` | ≤2% | 事件关联率：变更引发的事件占比 |

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



## Handover Criteria (交接标准)

| 条件项 | 状态 | 说明 |
|--------|------|------|
| 变更评估报告 | ☐ | 含风险等级 |
| 变更决策记录 | ☐ | 审批完成 |
| 实施计划 | ☐ | 含回滚方案 |
| 执行记录 | ☐ | 完整可追溯 |

## Workflow

```
1. 接收变更请求
2. 分析变更内容
3. 评估影响范围
4. 制定决策建议
5. 评审变更决策
6. 制定实施计划
7. 执行变更
8. 更新文档
```

## Related Scenarios

- **Related**: [../analyze-requirement/](../analyze-requirement/) - 需求分析
- **Related**: [../design-system/](../design-system/) - 系统设计
- **Related**: [../implement-feature/](../implement-feature/) - 开发实现

## Metrics

| 指标 | 目标 | 测量方法 |
|------|------|----------|
| 评估完整性 | > 95% | 检查清单覆盖率 |
| 决策合理性 | 100% | 评审通过率 |
| 实施成功率 | > 90% | 实施完成率 |


### Handover Context Template

```yaml
handover:
  header:
    from_stage: "manage-change"
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

