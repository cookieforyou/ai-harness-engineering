---
name: review-incident
description: "故障复盘执行指南，用于执行故障复盘"
applyTo: "scenarios/review-incident/**"
phase: incident-resolution
type: instruction
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-23
status: active
tags: ['instruction', 'technical']
---
# Incident Review Instruction

## Objective

对已解决的故障进行复盘分析，找出根本原因，制定改进措施，防止同类故障再次发生。

## Prerequisites

1. 故障已完全恢复
2. 相关日志可用
3. 关键人员参与

## Process Steps

### Step 1: 收集信息

1. 收集故障报告
2. 收集监控数据
3. 收集日志
4. 收集沟通记录

### Step 2: 重构时间线

1. 按时间顺序排列事件
2. 标注关键节点
3. 识别触发事件
4. 识别恢复动作

### Step 3: 分析原因

1. 分析直接原因
2. 使用 5 Why 分析
3. 识别根本原因
4. 区分内因外因

### Step 4: 评估影响

1. 用户影响
2. 业务影响
3. 财务影响
4. 声誉影响

### Step 5: 制定改进措施

1. 预防措施
2. 检测措施
3. 响应措施
4. 持续改进

### Step 6: 编写报告

1. 整理复盘内容
2. 分配行动项
3. 确定责任人
4. 归档报告

## Quality Gates

### 准入检查

- [ ] 故障已恢复
- [ ] 数据已收集
- [ ] 人员已确认

### 准出检查

- [ ] 根本原因已确定
- [ ] 改进措施已制定
- [ ] 责任人已确认

## Handoff Criteria

交接给运维前：

- [ ] 复盘报告已完成
- [ ] 行动项已分配
- [ ] 跟踪计划已制定


## Overview

> High-level description of the review-incident execution process.
>
> This instruction defines the technical approach, key activities, and success criteria for the review-incident scenario.
>
> 故障复盘是 E2E 交付生命周期中关键的改进闭环环节。每次故障都是组织学习的机会，通过结构化的复盘流程，将故障经验转化为系统和流程改进，持续提升系统的稳定性和可靠性。

## Technical Specifications

> Detailed technical requirements and implementation guidelines for review-incident.

### Required Tools

| 工具类别 | 推荐工具 | 用途 |
|----------|----------|------|
| 监控系统 | Prometheus/Grafana/Datadog | 获取故障期间的系统指标 |
| 日志平台 | ELK Stack/Splunk/Loki | 查询和分析日志 |
| 告警系统 | PagerDuty/OpsGenie | 获取告警记录和响应时间 |
| 事件管理 | Jira/ServiceNow | 记录和管理 Action Items |
| 文档工具 | Confluence/Notion | 编写和归档复盘报告 |
| 沟通工具 | Slack/钉钉/飞书 | 获取沟通和决策记录 |
| 版本控制 | GitLab/GitHub | 排查代码变更历史 |

### Environment Requirements

- 复盘环境可以是独立的工作空间或复盘会议室
- 需要访问故障相关的所有系统和数据源
- 复盘报告存储路径应统一规划，便于检索
- 敏感信息（如用户数据、安全漏洞）需要脱敏处理

### Configuration Parameters

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `postmortem_sla_hours` | number | 48 | 复盘启动时限（小时） |
| `max_action_items_per_review` | number | 15 | 单次复盘最大改进项数 |
| `tracking_frequency_days` | number | 7 | 改进措施跟踪频率（天） |
| `archival_period_days` | number | 365 | 复盘报告归档保留期限 |
| `severity_for_full_postmortem` | list | ["P0", "P1"] | 需完整复盘的严重级别 |
| `auto_reopen_if_recurrence_days` | number | 90 | 同类故障复发自动重开天数 |

## Best Practices

> Industry-standard best practices for review-incident execution.

1. **Blameless Postmortems**: Conduct blameless postmortems focused on system improvements, not individual blame
2. **Structured Root Cause Analysis**: Identify root cause using structured methods like 5 Whys and Fishbone diagrams
3. **SMART Action Items**: Track action items to completion with defined owners, deadlines, and acceptance criteria
4. **Data-Driven Timeline**: Reconstruct the incident timeline from multiple data sources (monitoring, logs, communications) for accuracy
5. **Systematic Knowledge Capture**: Transform learnings into runbook updates, monitoring rules, and training materials
6. **Timely Execution**: Start postmortem within 48 hours of resolution for P0/P1 incidents

## Postmortem 会议议程模板

### 会议基本信息

| 项目 | 内容 |
|------|------|
| 故障编号 | INC-{{YYYYMMDD}}-{{XXX}} |
| 故障标题 | {{incident_title}} |
| 严重级别 | P0 / P1 / P2 |
| 会议时间 | {{date}} {{time}} |
| 时长 | 60 分钟 |
| 主持人 | {{name}} |
| 参会人员 | {{names}} |

### 议程安排

```
0:00 - 0:05  开场与安全宣导
              - 重申无责文化原则
              - 明确会议目标
              - 介绍议程安排
              
0:05 - 0:15  时间线回顾
              - 按时间顺序呈现关键事件
              - 确认关键时间点准确
              - 标注响应和恢复的延迟点
              
0:15 - 0:20  做得好的方面
              - 列举故障处置中的亮点
              - 哪些自动化/流程起到了作用
              - 值得推广的实践
              
0:20 - 0:25  做得不好的方面
              - 列举改进机会点
              - 哪些环节耗时过长
              - 哪些决策可以优化
              
0:25 - 0:40  根因分析
              - 使用 5 Whys 深入追问
              - 绘制 Fishbone 因果图
              - 确认根本原因（至少到系统和流程层面）
              
0:40 - 0:50  改进措施讨论
              - 头脑风暴改进方案
              - 分类：预防/检测/响应/改进
              - 优先级排序（P0/P1/P2）
              
0:50 - 0:55  分配行动项
              - 每项指定唯一 Owner
              - 设定截止日期
              - 定义验收标准
              
0:55 - 1:00  总结与下一步
              - 确认下次复审时间
              - 确定报告发布时间
              - 会议反馈收集
```

## 时间线重构方法

### 重构步骤

```
时间线重构流程:
1. 从监控系统导出故障期间的指标时间序列
2. 从告警系统导出所有告警记录和时间戳
3. 从日志平台查询关键服务的错误日志
4. 从沟通工具收集故障期间的沟通记录
5. 从变更系统查询故障前的变更记录
6. 将所有事件按 UTC 时间排列到统一时间轴
7. 标注关键里程碑时间点
8. 计算各阶段耗时（TTD、TTE、TTM、TTR）
9. 交叉验证时间点的一致性
10. 识别时间线中的空白或矛盾点
```

### 关键时间指标

| 指标 | 定义 | 目标 | 计算公式 |
|------|------|------|----------|
| TTD (Time to Detect) | 故障发生到被发现的时间 | < 5 分钟 | 发现时间 - 引入时间 |
| TTE (Time to Engage) | 发现到响应启动的时间 | < 2 分钟 | 响应时间 - 发现时间 |
| TTM (Time to Mitigate) | 发现到缓解的时间 | < 15 分钟 | 缓解时间 - 发现时间 |
| TTR (Time to Resolve) | 发现到完全恢复的时间 | < 30 分钟 | 恢复时间 - 发现时间 |

## 根因分析框架

### 5 Whys 深度追问方法

操作步骤:
1. 定义故障现象（症状层面）
2. 问第一个 Why，寻找直接原因
3. 在直接原因基础上继续追问 Why
4. 重复直至找到流程/系统层面的根本原因
5. 验证根因：如果消除这个原因，故障还会发生吗？

```
示例: API 响应超时故障的 5 Whys 追问链

现象: API 响应时间从 100ms 上升到 10s
Why 1: 为什么 API 响应变慢？ → 数据库查询耗时 8s
Why 2: 为什么查询耗时 8s？ → 缺少索引导致全表扫描
Why 3: 为什么缺少索引？ → 上线前未发现这个慢查询
Why 4: 为什么未发现？ → 性能测试未覆盖该查询场景
Why 5: 为什么测试未覆盖？ → 变更流程中缺少性能测试检查点
根因: 变更流程中缺少性能评估环节
```

### Fishbone (鱼骨图) 因果分析

Fishbone 图帮助从多维度系统性地排查原因，避免遗漏:

```
人 (People)                   机 (Machine/Environment)
├── 人员技能不足               ├── 硬件资源不足
├── 人员疲劳/轮值问题          ├── 网络延迟
├── 沟通不畅                   ├── 配置错误
├── 操作失误                   └── 版本兼容
└── 培训不足

料 (Data/Materials)           法 (Methods/Process)
├── 数据质量问题               ├── 变更流程缺陷
├── 监控数据不完整             ├── 测试覆盖不足
├── 日志缺失                   ├── 审批流程缺失
├── 缓存数据不一致             └── 应急预案不完善
└── 配置数据错误

环 (Environment)
├── 依赖服务故障
├── 第三方 API 限流
├── 安全攻击
├── 流量突增
└── 区域故障
```

### Fault Tree 分析 (FTA)

FTA 适用于复杂故障场景，通过逻辑门组合分析故障路径:

```
系统不可用 (AND)
├── 数据库主库故障 (OR)
│   ├── 硬件故障
│   ├── 连接池耗尽
│   └── 慢查询堆积
└── 切换失败 (OR)
    ├── 自动切换未触发
    └── 手动切换超时
```

## 影响评估方法论

### 评估维度与量化方法

| 维度 | 评估内容 | 量化方法 | 数据来源 |
|------|----------|----------|----------|
| 用户影响 | 受影响用户数和范围 | 错误率 × 活跃用户数 | 监控系统、用户反馈 |
| 业务影响 | 直接和间接经济损失 | 交易损失 + 赔偿 + 人力成本 | 业务报表 |
| 系统影响 | SLO/SLA 违规程度 | 可用性指标 + 性能指标 | 监控系统 |
| 安全影响 | 数据泄露和合规风险 | 数据类型 + 数量 + 敏感级别 | 安全审计 |
| 声誉影响 | 品牌和客户信任 | 投诉率 + 媒体曝光度 | 客服 + 社交媒体 |

### 影响等级判定矩阵

```
影响等级 = 影响范围 × 严重程度

影响范围:
  - 单一用户/功能: 1
  - 部分用户/功能: 2
  - 全部用户/核心功能: 3

严重程度:
  - 轻微降级: 1
  - 功能受损: 2
  - 完全不可用: 3

结果:
  1-2: SEV4
  3-4: SEV3
  6:   SEV2
  9:   SEV1
```

## 改进措施优先级矩阵

### 优先级判定矩阵

```
优先级 = 风险降低效果 × 实施可行性

风险降低效果:
  - 高 (3): 显著降低故障复发概率
  - 中 (2): 部分降低风险
  - 低 (1): 微小改进

实施可行性:
  - 高 (3): 1-4 周内可完成，资源已就绪
  - 中 (2): 1-3 月可完成，需协调资源
  - 低 (1): 3 个月以上，需重大投入

优先级:
  - P0: 得分 ≥ 6，立即执行
  - P1: 得分 4-5，排入近期迭代
  - P2: 得分 2-3，排入长期计划
  - P3: 得分 1，暂不执行
```

### 改进措施 SMART 化模板

| 要素 | 示例 |
|------|------|
| S (Specific) | "在变更审批流程中添加 SQL 性能评估检查步骤" |
| M (Measurable) | "变更审批单中必须包含慢查询检测结果截图" |
| A (Achievable) | "在现有变更管理工具中添加一个检查字段" |
| R (Relevant) | "直接防止因缺少性能评估导致的慢查询故障" |
| T (Time-bound) | "在 2026 年 7 月 15 日前完成" |

## 错误处理

> Common error scenarios and resolution strategies for review-incident.

### Error Category 1: 复盘未能识别可执行的改进项
**Symptom**: Postmortem does not identify actionable improvements
**Cause**: 根因分析停留在技术表面，未追问到流程/系统层面；或改进措施过于模糊
**Resolution**: 
1. 重新进行 5 Whys 分析，确保追问到流程/系统层面
2. 将"加强 X"类模糊措施拆解为具体的操作步骤
3. 使用 SMART 原则重新定义每项改进措施
4. 如果核心根因不明确，安排专家会诊

### Error Category 2: 同类故障反复发生
**Symptom**: Similar incidents recur without corrective action
**Cause**: 改进措施未执行或未执行到位；根因识别不准确，治标不治本
**Resolution**: 
1. 检查以前的 Action Items 执行状态
2. 重新评估根因分析是否准确
3. 如有未执行的改进项，分析阻塞原因并推动解决
4. 考虑是否需要架构级改进而非流程级修补
5. 建立更严格的改进措施跟踪机制

### Error Category 3: 复盘会议参与度低
**Symptom**: Key stakeholders skip or leave early from postmortem meetings
**Cause**: 会议时间过长；复盘被理解为追责；改进措施从未落地导致疲劳
**Resolution**:
1. 严格控制会议时长在 60 分钟以内
2. 重申无责文化，增强心理安全感
3. 展示以前复盘的改进成果，证明复盘的价值
4. 会前发送议程和预读材料，提高会议效率
5. 轮流担任复盘主持人，培养全员复盘文化

## Quality Standards

> Acceptance criteria and quality gates for review-incident deliverables.

| Standard | Criteria | Verification Method | Owner |
|----------|----------|---------------------|-------|
| POSTMORTEM-COMPLETION | All P0/P1 incidents have completed postmortems | Automated check in incident management tool | Incident Manager |
| ACTION-CLOSURE | Action item closure rate is 90% or higher | Automated check in tracking system | Engineering Manager |
| RECURRENCE-RATE | Incident recurrence rate is 5% or lower | Quarterly trend analysis | SRE Team |
| REVIEW-TIMELINESS | Postmortem completed within 7 days of resolution | Automated SLA tracking | Incident Manager |
| ACTION-SMART | 100% of action items pass SMART validation | Manual audit of 10% sample | QA Lead |
| BLAMELESS-AUDIT | Postmortem language is blameless and constructive | Automated text analysis | Culture Champion |

## References

- [harness-engineering.md](../standards/harness-engineering.md) — 工程标准
- [output-validation-checklist.md](../evaluations/output-validation-checklist.md) — 输出验证清单
- [regression-checklist.md](../evaluations/regression-checklist.md) — 回归检查清单
- [incident-management.md](../standards/incident-management.md) — 事件管理标准
- [post-mortem-template.md](../templates/post-mortem.template.md) — 复盘报告模板
- [blameless-culture-guide.md](../standards/blameless-culture-guide.md) — 无责文化指南
