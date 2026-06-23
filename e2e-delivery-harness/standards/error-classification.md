---
name: error-classification
description: "规范化的错误分类、处理和升级策略体系，定义 P0-P4 错误等级及对应的识别信号、处理流程、降级方案和升级条件"
type: standard
version: "2.0.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-23
status: active
tags: ['standard', 'error-handling', 'escalation', 'classification']
---

# 错误分类与处理策略

## 概述

本文件定义了 E2E Delivery Harness 中所有场景的**标准化错误分类体系和处理协议**。各场景应**引用本文件**的基础上，添加领域特定的错误场景，而非逐字复制通用分类表格。

## 错误等级定义 (P0-P4)

| 等级 | 标签 | 定义 | 响应时间 | 处理原则 | 典型示例 |
|------|------|------|---------|---------|---------|
| **P0** | Critical (阻塞) | 导致核心功能完全不可用、数据丢失或安全漏洞 | 立即 (15分钟内) | 停止当前流程，立即修复或回滚 | 生产服务宕机、数据泄漏、部署完全失败 |
| **P1** | High (严重) | 重要功能受损、SLO 突破阈值、有较大业务影响 | 1 小时内 | 优先处理，评估是否降级或回滚 | 核心 API 错误率 >1%、构建失败、关键依赖不可用 |
| **P2** | Medium (一般) | 非核心功能受影响、存在已知可workaround | 24 小时内 | 排入当前迭代修复 | 非核心页面报错、性能退化未达阈值、文档缺失 |
| **P3** | Low (轻微) | 不影响功能的小问题、优化建议 | 下一个迭代 | 排入 backlog，不阻塞当前流程 | UI 样式偏差、日志级别不当、代码注释过时 |
| **P4** | Info (跟踪) | 观察项、需要持续监控的趋势 | 无需立即处理 | 记录跟踪，定期回顾 | 资源使用率上升趋势、技术债务积累 |

## 错误处理标准流程

每个错误场景必须使用以下结构化格式定义：

```yaml
error_scenario:
  id: "EH-{序号}"
  name: "{错误场景名称}"
  severity: "P0/P1/P2/P3"
  
  identification:  # 识别信号
    signals:
      - "{具体的可观测信号1}"
      - "{具体的可观测信号2}"
    detection_method: "{如何检测到这个错误}"
    threshold: "{触发阈值，如有}"
    
  handling_flow:  # IF-THEN 处理流程
    - step: 1
      condition: "IF {条件}"
      action: "{具体操作}"
    - step: 2
      condition: "ELSE IF {条件}"
      action: "{具体操作}"
    - step: 3
      condition: "ELSE"
      action: "{具体操作（兜底）}"
      
  degradation:  # 降级方案
    strategy: "{降级策略描述}"
    impact: "{降级后对用户/系统的影响}"
    recovery_path: "{从降级状态恢复的步骤}"
    
  escalation:  # 升级条件
    trigger: "{触发升级的具体条件（量化）}"
    target: "{升级目标角色/团队}"
    max_auto_retries: 3
    timeout: "{自动处理的最大时限}"
```

## 通用升级触发条件

以下条件触发从 AI Agent 自动处理升级到人工决策：

| 条件 ID | 触发条件 | 升级目标 |
|---------|---------|---------|
| ESC-001 | 同一错误 3 轮自动处理仍无法解决 | 技术负责人 |
| ESC-002 | 质量评分低于 Scenario 规定的合格线 (70分) | 项目管理者 |
| ESC-003 | 变更影响超过阈值（范围蔓延 >20%、关键里程碑延期） | 产品经理 |
| ESC-004 | 安全/合规类 DC-* 无明确授权 | 安全负责人 |
| ESC-005 | 交接必填字段无法从上下文推断且无法澄清 | 上游 Agent |
| ESC-006 | 影响用户数超过预定义阈值 | On-Call 工程师 |
| ESC-007 | 数据丢失或损坏风险 | DBA + 技术负责人 |

## 场景引用方式

各场景的 SCENARIO.md 应按如下方式引用：

```markdown
## Error Handling (错误处理)

> **通用框架**: 遵循 [错误分类与处理策略](../../standards/error-classification.md) 的 P0-P4 等级定义和通用升级条件。
> 每场景必须包含 识别信号→IF-THEN流程→降级方案→升级条件 四要素。

### 领域特定错误场景

#### Error Scenario 1: {场景名称} (P1)
**识别信号**: ...
**处理流程**: ...
**降级方案**: ...
**升级条件**: ...
```

## 错误日志模板

所有错误处理必须生成结构化日志：

```yaml
error_log:
  timestamp: "{{ISO8601}}"
  scenario: "{{scenario.name}}"
  step: "{{current_step}}"
  error:
    id: "ERR-{{timestamp}}-{{seq}}"
    severity: "P0/P1/P2/P3/P4"
    category: "{网络/数据/配置/权限/业务逻辑/外部依赖}"
    signal: "{触发信号}"
    handling:
      attempts: {count}
      actions_taken: ["{action1}", "{action2}"]
      outcome: "resolved/degraded/escalated"
    resolution:
      final_action: "{最终处理}"
      impact_duration: "{持续时间}"
      data_loss: "none/partial/complete"
  escalation:
    escalated: true/false
    reason: "{升级原因}"
    target: "{升级目标}"
    time_to_escalate: "{从发现到升级的时间}"
```

## 反模式 (Anti-patterns)

| 反模式 | 表现 | 正确做法 |
|--------|------|---------|
| 等级通胀 | 所有问题都标 P0 | 严格按影响范围和严重程度分级 |
| 降级无感 | 降级后不告知用户 | 降级后必须通知受影响用户和干系人 |
| 升级延迟 | 已满足升级条件但不升级 | 达到升级阈值立即升级，不犹豫 |
| 重试风暴 | 无限循环重试 | 最多 3 次自动重试，之后升级 |
| 日志缺失 | 处理了错误但不记录 | 结构化记录每次错误处理过程 |

## 相关资产

- [cot-framework.md](cot-framework.md) - CoT 执行框架（含验证失败处理）
- [id-generation-quantification.md](id-generation-quantification.md) - KPI 体系
- [AGENTS.md](../AGENTS.md) - 升级通用条件
