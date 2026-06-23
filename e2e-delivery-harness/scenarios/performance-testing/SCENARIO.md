---
name: performance-testing
description: "Performance Testing scenario for the E2E delivery lifecycle"
type: scenario
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['workflow', 'process']
---
# Performance Testing Scenario (性能测试场景)

## Purpose

在生产级负载条件下验证系统的性能表现，通过负载测试、压力测试、稳定性测试和峰值测试，识别系统吞吐量上限、响应时间瓶颈和资源饱和度。确保系统在上线前满足SLA要求（如P95延迟≤200ms、吞吐量≥1000 RPS）。

### Business Value

- SLO达成率≥99%
- 瓶颈识别准确率≥90%
- 性能基线覆盖率=100%

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

本场景用于指导 AI Agent 执行完整的性能测试流程，包括性能需求分析、测试计划制定、性能测试执行、结果分析与优化建议。

### Think-Aloud Protocol

```
THINK: 理解业务场景和性能目标
   ↓
THINK: 识别关键业务路径和性能指标
   ↓
THINK: 设计性能测试模型
   ↓
THINK: 执行负载测试并监控指标
   ↓
THINK: 分析测试结果和瓶颈
   ↓
VALIDATE: 验证性能是否达标
   ↓
OUTPUT: 输出性能报告和优化建议
```

### Step-by-Step Reasoning

**Step 1: 性能需求分析**
- 问：业务场景的性能要求是什么？
- 验证：性能指标与业务 SLA 对齐
- 检查：指标定义清晰可测量

**Step 2: 性能测试设计**
- 问：测试模型是否能真实反映业务场景？
- 验证：测试脚本覆盖关键路径
- 检查：测试数据准备充分

**Step 3: 测试执行与监控**
- 问：测试执行是否按计划进行？
- 验证：监控指标采集完整
- 检查：无异常发生

**Step 4: 结果分析与优化**
- 问：性能瓶颈的根本原因是什么？
- 验证：数据支撑分析结论
- 检查：优化建议可执行

### Agent
- **Agent**: [../../agents/performance-testing.agent.md](../../agents/performance-testing.agent.md)

### Instruction
- **Instruction**: [../../instructions/performance-testing.instructions.md](../../instructions/performance-testing.instructions.md)

### Prompt
- **Prompt**: [../../prompts/performance-testing.prompt.md](../../prompts/performance-testing.prompt.md)

### Skills
- **Skill**: [../../skills/performance-testing/SKILL.md](../../skills/performance-testing/SKILL.md)

### EH-1: 性能指标不达标

- **识别信号**：响应时间 > SLA、吞吐量 < 目标、错误率 > 阈值
- **处理方式**：
  1. 记录未达标指标
  2. 分析未达标原因
  3. 定位性能瓶颈
  4. 提出优化建议
- **升级条件**：关键指标严重超标需立即升级

### EH-2: 测试环境不稳定

- **识别信号**：测试结果波动大、多次执行结果不一致
- **处理方式**：
  1. 检查环境状态
  2. 排除环境干扰因素
  3. 增加预热时间
  4. 多次执行取平均值
- **升级条件**：环境问题影响测试结论

### EH-3: 测试数据不足

- **识别信号**：测试结果与预期差异大、数据相关性差
- **处理方式**：
  1. 补充测试数据
  2. 使用生产数据脱敏
  3. 调整数据分布
- **升级条件**：无法准备足够测试数据

### 产出清单

1. **性能测试计划**：测试范围、策略、资源计划
2. **性能测试脚本**：自动化测试脚本
3. **性能测试报告**：测试结果、数据分析、结论
4. **优化建议**：瓶颈分析、优化方案、预期收益

### 输出格式

```markdown
### 1. 测试概述
### 2. 测试环境
### 3. 测试结果
### 4. 性能分析
### 5. 优化建议
### 6. 结论
```

## Prerequisites

### 必需前置条件

1. 系统已完成功能测试
2. 测试环境已部署完成
3. 性能基线数据已收集（如有）
4. 测试数据已准备

### 可选前置条件

1. 历史性能数据
2. 性能监控工具
3. 压测工具授权

### 阶段准入

- [ ] 功能测试已通过
- [ ] 测试环境就绪
- [ ] 性能指标已定义
- [ ] 测试工具可用

### 阶段准出

- [ ] 性能测试执行完成
- [ ] 测试数据完整
- [ ] 报告已输出
- [ ] 结论已确认

## Decision Checkpoints

| ID | 决策点 | 触发条件 | 决策选项 | 选择标准 | 记录位置 |
|----|--------|----------|----------|----------|----------|
| DC-001 | 范围确认 | 执行启动前 | 继续 / 缩小范围 / 升级 | 与上游 Handover 一致 | 执行记录 |
| DC-002 | 质量门禁 | 产出验证前 | 修复后继续 / 记录 open_issues | Scenario KPI ≥70 | 验证报告 |
| DC-003 | 交接准出 | 阶段完成前 | 完成交接 / 部分交接 / 阻塞 | Handover 必填字段齐全 | Handover YAML |

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
| `SLO-ACHIEVE` | ≥99.5% | SLO达成率 |
| `BOTTLENECK-ID` | 100% | 瓶颈识别率：所有已知瓶颈被定位 |
| `TEST-VALIDITY` | ≥95% | 测试有效性：结果与生产环境相关性 |

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识

## Handover Criteria (交接标准)

| 条件项 | 状态 | 说明 |
|--------|------|------|
| 性能测试计划 | ☐ | 已评审通过 |
| 测试脚本 | ☐ | 已开发并调试 |
| 测试报告 | ☐ | 完整且准确 |
| 优化建议 | ☐ | 可执行有效 |

### 交接检查清单

- [ ] 产出文档完整
- [ ] 评审已通过
- [ ] 遗留问题已记录
- [ ] 下一阶段已知晓

## Workflow

```
1. 启动 → 性能需求分析
2. 设计 → 测试计划制定
3. 准备 → 脚本开发和数据准备
4. 执行 → 性能测试执行
5. 分析 → 结果分析和报告
6. 完成 → 输出交付物
```

## Related Scenarios

- **Next**: [../deploy-release/SCENARIO.md](../deploy-release/SCENARIO.md) - 部署发布
- **Previous**: [../verify-test/SCENARIO.md](../verify-test/SCENARIO.md) - 测试验证

### Handover Context Template

```yaml
handover:
  header:
    from_stage: "performance-testing"
    to_stage: "deploy-release"
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
