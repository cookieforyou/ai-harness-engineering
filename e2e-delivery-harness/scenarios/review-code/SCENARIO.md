---
name: review-code
description: "Review Code scenario for the E2E delivery lifecycle"
type: scenario
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['workflow', 'process']
---
# Code Review Scenario

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

执行代码审查，发现代码质量问题，确保代码符合规范，减少缺陷进入测试阶段。

### Step-by-Step Reasoning

**Step 1: 变更理解**
- 问：这次变更做了什么？
- 验证：理解业务逻辑
- 检查：变更范围是否合理

**Step 2: 规范检查**
- 问：代码符合编码规范吗？
- 验证：逐项对照规范
- 检查：命名、格式、注释

**Step 3: 质量分析**
- 问：代码质量如何？
- 验证：检查复杂度、耦合度
- 检查：是否有坏味道

**Step 4: 风险识别**
- 问：有什么潜在风险？
- 验证：性能、并发、边界
- 检查：是否有遗漏

**Step 5: 安全评估**
- 问：有安全漏洞吗？
- 验证：常见安全检查
- 检查：注入、XSS、权限

## Error Handling

### EH-1: 代码逻辑错误

- **识别信号**：发现业务逻辑问题
- **处理方式**：
  1. 明确指出问题
  2. 说明影响
  3. 提出修改建议
- **升级条件**：影响核心功能

### EH-2: 发现安全漏洞

- **识别信号**：发现安全风险
- **处理方式**：
  1. 标记为安全评论
  2. 说明漏洞类型
  3. 提供修复建议
  4. 优先级设为高
- **升级条件**：高危漏洞

### EH-3: 审查意见分歧

- **识别信号**：开发者不认同审查意见
- **处理方式**：
  1. 解释审查标准
  2. 提供参考案例
  3. 寻求共识
- **升级条件**：无法达成共识

### 产出清单

1. **代码审查报告**：审查结果汇总
2. **审查评论**：具体问题列表
3. **审查结论**：通过/需要修改

### 输出格式

```markdown
### 1. 审查信息
- 变更编号：
- 审查人：
- 日期：
- 代码作者：

### 2. 变更摘要
...

### 3. 审查结果
- 严重问题：N
- 一般问题：N
- 建议改进：N

### 4. 问题详情
...

### 5. 审查结论
...
```

## Prerequisites

### 必需前置条件

1. 代码已提交到审查分支
2. 单元测试已通过
3. 代码规范可用

### 可选前置条件

1. PR 描述完整
2. 相关文档已更新

### 阶段准入

- [ ] 代码已提交审查
- [ ] PR 描述完整
- [ ] 测试已通过

### 阶段准出

- [ ] 所有严重问题已解决
- [ ] 所有一般问题已处理
- [ ] 审查结论已给出

## Decision Checkpoints

| ID | 决策点 | 触发条件 | 决策选项 | 选择标准 | 记录位置 |
|----|--------|----------|----------|----------|----------|
| DC-001 | 审查范围确认 | 开始审查前 | 全量 / 增量 / 关键路径 | 变更影响与风险 | 审查计划 |
| DC-002 | 严重问题处理 | 发现 Blocker 时 | 修复后合并 / 拒绝合并 | 安全与功能影响 | 审查意见 |
| DC-003 | 合并批准 | 问题处理完成后 | 批准 / 条件批准 / 拒绝 | DoD 与测试通过 | PR 状态 |

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
| `DEFECT-DETECTION` | ≥85% | 缺陷检出率：代码审查发现的问题 |
| `REVIEW-TURNAROUND` | ≤24h | 审查周转时间 |
| `SECURITY-FINDINGS` | 0 | 安全漏洞遗留：P0/P1安全漏洞数 |

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识

## Handover Criteria (交接标准)

| 条件项 | 状态 | 说明 |
|--------|------|------|
| 审查报告 | ☐ | 问题清单完整 |
| 严重问题 | ☐ | 全部已解决 |
| 一般问题 | ☐ | 全部已处理 |
| 审查结论 | ☐ | APPROVED/CHANGES |

## Workflow

```
1. 接收审查请求
2. 理解变更内容
3. 执行代码审查
4. 标注问题
5. 给出审查结论
6. 跟踪问题修复
7. 完成审查
```

## Related Scenarios

- **Related**: [../implement-feature/](../implement-feature/) - 开发实现
- **Related**: [../verify-test/](../verify-test/) - 测试验证

### Handover Context Template

```yaml
handover:
  header:
    from_stage: "review-code"
    to_stage: "verify-test"
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
