---
name: manage-dependencies
description: "依赖管理场景，管理系统和项目依赖，确保依赖的安全性、兼容性和可维护性"
type: scenario
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['workflow', 'process']
---
# Dependency Management Scenario

## Overview

依赖管理是软件开发中的关键环节，涉及识别、分析、更新和维护项目所依赖的外部库、框架和工具。本场景确保依赖的安全性、兼容性和可维护性。

## Trigger Conditions

- 新项目初始化时
- 定期依赖审计（每月/每季度）
- 安全漏洞披露时
- 版本升级前
- 代码审查中发现依赖问题时

## Chain of Thought

```
1. 分析依赖清单
   ↓
2. 识别直接依赖和传递依赖
   ↓
3. 检查安全漏洞和许可证合规
   ↓
4. 评估版本兼容性和更新风险
   ↓
5. 制定更新策略和回滚计划
   ↓
6. 执行更新并验证
   ↓
7. 更新依赖锁定文件
   ↓
8. 验证构建和测试通过
```

## Decision Checkpoints

| ID | 决策点 | 触发条件 | 决策选项 | 选择标准 | 记录位置 |
|----|--------|----------|----------|----------|----------|
| DC-001 | 范围确认 | 执行启动前 | 继续 / 缩小范围 / 升级 | 与上游 Handover 一致 | 执行记录 |
| DC-002 | 质量门禁 | 产出验证前 | 修复后继续 / 记录 open_issues | Scenario KPI ≥70 | 验证报告 |
| DC-003 | 交接准出 | 阶段完成前 | 完成交接 / 部分交接 / 阻塞 | Handover 必填字段齐全 | Handover YAML |


## Error Handling

| Error Scenario | Handling Strategy |
|----------------|-------------------|
| 依赖冲突 | 绘制依赖图，识别冲突源，使用版本约束解决 |
| 脆弱依赖 | 评估替代方案，制定迁移计划 |
| 许可证冲突 | 咨询法务，评估替换或购买许可 |
| 更新后构建失败 | 自动回滚，分析兼容性变更 |




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
| `VULN-DETECTION` | 100% | 漏洞检测率：已知CVE全部识别 |
| `LICENSE-COMPLY` | 100% | 许可证合规率：无禁止许可证 |
| `UPDATE-LATENCY` | ≤30d | 更新延迟：关键补丁应用时间 |

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

- [ ] 依赖清单完整且准确
- [ ] 安全漏洞已评估和处理
- [ ] 更新计划已制定并评审
- [ ] 依赖锁定文件已更新
- [ ] 构建和测试通过
- [ ] 文档已更新

## Expected Artifacts

| Artifact | Description |
|----------|-------------|
| dependency-report.md | 完整依赖分析报告 |
| update-plan.md | 更新计划和风险评估 |
| vulnerability-assessment.md | 安全漏洞评估报告 |
| lockfile | 更新的依赖锁定文件 |

## Related Scenarios

- [implement-feature](./implement-feature/SCENARIO.md) - 功能实现
- [audit-security](./audit-security/SCENARIO.md) - 安全审计
- [verify-test](./verify-test/SCENARIO.md) - 测试验证



### Handover Context Template

```yaml
handover:
  header:
    from_stage: "manage-dependencies"
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

