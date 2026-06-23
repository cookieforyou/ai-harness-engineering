---
name: automate-test
description: "Automate Test scenario for the E2E delivery lifecycle"
type: scenario
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['workflow', 'process']
---
# Scenario: 自动化测试 (Automate Test)

## Overview

本场景用于搭建自动化测试框架、编写自动化测试用例、集成 CI/CD 流水线。

## Chain of Thought

```
[THINK] 理解测试需求
├─ 确定测试范围和目标
├─ 分析被测系统架构
└─ 评估测试工具选型

[ANALYZE] 设计测试框架
├─ 选择测试框架（pytest/jest/JUnit）
├─ 设计测试分层结构
└─ 制定测试数据策略

[DESIGN] 编写测试用例
├─ 设计测试用例结构
├─ 编写测试数据构造器
└─ 实现测试断言库

[IMPLEMENT] 实现测试脚本
├─ 编写 Page Object 模型
├─ 实现测试用例脚本
└─ 添加测试报告生成

[INTEGRATE] 集成 CI/CD
├─ 配置测试执行流水线
├─ 设置测试报告收集
└─ 配置失败自动通知
```

## Decision Checkpoints

| 检查点 | 条件 | 决策 |
|--------|------|------|
| DC-001 | 测试框架选型确认 | 是否选择当前框架？ |
| DC-002 | 测试用例评审 | 用例是否覆盖核心路径？ |
| DC-003 | CI 集成方案 | 测试触发时机？ |

## Error Handling

| 错误类型 | 处理方式 |
|----------|----------|
| 测试环境不可用 | 等待环境就绪或通知 DevOps |
| 依赖安装失败 | 检查 pip/npm 配置 |
| 测试数据缺失 | 构造测试数据或联系数据团队 |




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
| `AUTO-COVERAGE` | ≥70% | 自动化覆盖率：可自动化场景占比 |
| `FLAKY-RATE` | ≤5% | 不稳定率： flaky test 占比 |
| `EXEC-TIME` | ≤30min | 执行时间：全量自动化测试耗时 |

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

- [x] 测试框架搭建完成
- [x] 核心用例覆盖率 ≥ 80%
- [x] CI 流水线集成成功
- [x] 测试报告可正常生成
- [x] 维护文档已编写

## Associated Assets

- **Prompt**: `prompts/automate-test.prompt.md`
- **Instruction**: `instructions/automate-test.instructions.md`
- **Agent**: `agents/automate-test.agent.md`
- **Skill**: `skills/automate-test/SKILL.md`



### Handover Context Template

```yaml
handover:
  header:
    from_stage: "automate-test"
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

