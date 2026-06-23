---
name: respond-incident
description: "事件响应场景，定义生产环境事故的发现、响应、处理和恢复流程"
type: scenario
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['workflow', 'process']
---
# Incident Response Scenario

## Overview

事件响应是保障服务稳定性的关键能力，涵盖从发现问题到恢复服务的完整流程。本场景定义事件的分级、响应流程、处理步骤和复盘改进机制。

## Severity Levels

### P0 - Critical

| Aspect | Definition |
|--------|------------|
| 影响 | 核心服务完全不可用，影响所有用户 |
| SLA | 响应时间: 5 分钟，恢复时间: 1 小时 |
| 人员 | 全员响应，管理层介入 |
| 沟通 | 每 15 分钟状态更新 |

### P1 - High

| Aspect | Definition |
|--------|------------|
| 影响 | 核心功能受损，影响大部分用户 |
| SLA | 响应时间: 15 分钟，恢复时间: 4 小时 |
| 人员 | On-call + 值班经理 |
| 沟通 | 每 30 分钟状态更新 |

### P2 - Medium

| Aspect | Definition |
|--------|------------|
| 影响 | 非核心功能异常，影响部分用户 |
| SLA | 响应时间: 1 小时，恢复时间: 8 小时 |
| 人员 | On-call 工程师 |
| 沟通 | 每 2 小时状态更新 |

### P3 - Low

| Aspect | Definition |
|--------|------------|
| 影响 | 功能降级或小范围问题 |
| SLA | 响应时间: 4 小时，恢复时间: 24 小时 |
| 人员 | 工作时间处理 |
| 沟通 | 每日状态更新 |

## Chain of Thought

```
1. 检测与确认
   ↓
2. 评估与定级
   ↓
3. 组建响应团队
   ↓
4. 沟通启动
   ↓
5. 诊断分析
   ↓
6. 制定解决方案
   ↓
7. 执行修复
   ↓
8. 验证恢复
   ↓
9. 事后复盘
   ↓
10. 预防改进
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
| 诊断困难 | 请求更多资源，多角度分析 |
| 修复失败 | 回滚到上一版本，重复修复 |
| 影响扩大 | 立即升级，启动应急响应 |
| 数据损坏 | 启动数据恢复流程 |


## Quality Metrics

> Quality metrics for measuring scenario execution success.

| KPI | Target | Description |
|-----|--------|-------------|
| `MTTR` | ≤1h | 恢复时间目标 |
| `ESCALATION-ACCURACY` | ≥90% | 升级准确性：正确触发升级的比例 |
| `COMM-TIMELINESS` | ≤15min | 沟通及时性：首次沟通时间 |

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

- [ ] 事件已恢复
- [ ] 影响已评估
- [ ] 根本原因已识别
- [ ] 修复已验证
- [ ] 监控已加强
- [ ] 复盘已完成

## Expected Artifacts

| Artifact | Description |
|----------|-------------|
| incident-timeline.md | 事件时间线 |
| resolution-steps.md | 解决步骤 |
| impact-report.md | 影响评估报告 |
| follow-up-actions.md | 后续行动项 |

## Related Scenarios

- [monitor-operate](./monitor-operate/SCENARIO.md) - 监控运维
- [review-incident](./review-incident/SCENARIO.md) - 事件复盘
- [plan-rollback](./plan-rollback/SCENARIO.md) - 回滚计划
- [plan-disaster-recovery](./plan-disaster-recovery/SCENARIO.md) - 灾备恢复



### Handover Context Template

```yaml
handover:
  header:
    from_stage: "respond-incident"
    to_stage: "review-incident"
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

