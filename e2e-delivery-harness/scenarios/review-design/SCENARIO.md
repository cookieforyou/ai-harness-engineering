---
name: review-design
description: "Review Design scenario for the E2E delivery lifecycle"
type: scenario
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-23
status: active
language: "zh-CN"
tags: ['workflow', 'process']
---
# Review Design Scenario (技术方案评审场景)

## Purpose

运用ATAM/SAAM架构评估方法论，对系统设计进行结构化的技术评审。评估架构决策的合理性、非功能需求的满足度（性能/安全/可用性/可扩展性）和技术风险的可控性，产出可操作的改进建议和ADR评审意见。

### Business Value

- 架构风险识别率≥90%
- 设计缺陷提前发现率≥80%
- 评审建议采纳率≥75%

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

本场景用于指导 AI Agent 执行技术方案评审工作，评估方案的可行性、安全性、性能和可维护性。

### Think-Aloud Protocol

```
THINK: 理解业务背景和需求
   ↓
THINK: 分析技术方案完整性
   ↓
THINK: 评估技术风险
   ↓
THINK: 检查合规性
   ↓
VALIDATE: 综合评审结论
   ↓
OUTPUT: 输出评审报告
```

### EH-1: 方案信息不足

- **识别信号**：缺少关键设计信息
- **处理方式**：
  1. 列出缺失信息清单
  2. 要求补充
  3. 标注 [待补充]
- **升级条件**：关键信息无法获取

### EH-2: 评审意见分歧

- **识别信号**：评审意见不一致
- **处理方式**：
  1. 讨论达成共识
  2. 记录分歧点
  3. 升级决策
- **升级条件**：无法达成共识

## Decision Checkpoints

| ID | 决策点 | 触发条件 | 决策选项 | 选择标准 | 记录位置 |
|----|--------|----------|----------|----------|----------|
| DC-001 | 评审范围 | 评审启动前 | 架构 / 接口 / 全量 | 变更范围与风险 | 评审议程 |
| DC-002 | 问题处置 | 发现设计缺陷 | 修订后通过 / 重大变更 | 影响分析与 ADR | 评审记录 |
| DC-003 | 准出签字 | 修订完成后 | 通过 / 有条件通过 | KPI 与开放问题 | 评审结论 |

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
| `ISSUE-DETECTION` | ≥95% | 问题检出率：实际发现/潜在问题 |
| `REVIEW-TURNAROUND` | ≤2d | 评审周转时间：提交到结论 |
| `DEFECT-ESCAPE` | ≤5% | 缺陷逃逸率：评审后仍发现的问题 |

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识

## Handover Criteria (交接标准)

| 条件项 | 状态 | 说明 |
|--------|------|------|
| 评审报告 | ☐ | 完整准确 |
| 评审结论 | ☐ | 通过/不通过 |
| 改进建议 | ☐ | 已记录 |

## Prerequisites

- [ ] Prerequisite 1: 设计文档已完成且归档至项目知识库（含架构图、数据模型、API 契约、部署方案）— 缺失任何一项则停止评审
- [ ] Prerequisite 2: 设计评审参与人已确认且全部到场（架构师、Tech Lead、安全代表、DBA，≥4 人），评审材料提前 ≥24h 分发
- [ ] Prerequisite 3: 上次评审的改进项已全部闭环（Action Items 完成率 100%，未闭环项不得启动新评审）

### Handover Context Template

```yaml
handover:
  header:
    from_stage: "review-design"
    to_stage: "decompose-task"
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
