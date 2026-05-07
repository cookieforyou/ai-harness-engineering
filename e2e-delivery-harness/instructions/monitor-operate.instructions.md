---
name: monitor-operate
description: "Technical instructions for monitoring and operations execution"
type: instruction
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['instruction', 'technical']
---
# Monitoring Operations Instructions

## Purpose

本文档定义了监控运维阶段的标准操作流程、质量检查标准和工作产出规范。监控运维是保障系统稳定运行、持续改进运维效率的阶段。

## Investigation Flow

### 流程概览

```
监控配置 → 日常巡检 → 告警处理 → 故障排查 → 容量管理 → 运维优化
```

### 步骤 1：监控配置

**目的**：配置完善的监控指标和告警规则

**输入**：
- 系统架构文档
- 部署完成报告
- 监控需求

**操作**：

1. **指标体系设计**
   - 定义基础监控指标（CPU、内存、磁盘、网络）
   - 定义应用监控指标（QPS、响应时间、错误率）
   - 定义业务监控指标（核心业务指标）

2. **告警规则配置**
   - 设置告警阈值
   - 配置告警级别（P0/P1/P2/P3）
   - 配置告警通知渠道

3. **监控视图**
   - 创建仪表盘视图
   - 配置数据展示
   - 设置刷新频率

**输出**：监控配置文档

### 步骤 2：日常巡检

**目的**：定期检查系统运行状态，及时发现潜在问题

**输入**：
- 监控仪表盘
- 巡检检查清单
- 历史巡检记录

**操作**：

1. **巡检执行**
   - 检查系统健康状态
   - 检查资源使用情况
   - 检查业务运行指标

2. **问题识别**
   - 识别异常指标
   - 分析潜在风险
   - 记录观察结果

3. **巡检报告**
   - 汇总巡检结果
   - 提出改进建议
   - 归档巡检记录

**输出**：巡检报告

### 步骤 3：告警处理

**目的**：及时响应和处理告警事件

**输入**：
- 告警通知
- 告警处理流程
- 应急预案

**操作**：

1. **告警响应**
   - 确认告警信息
   - 评估告警级别
   - 启动相应流程

2. **告警处理**
   - 定位告警原因
   - 执行处理措施
   - 验证处理结果

3. **告警闭环**
   - 确认告警消除
   - 更新告警记录
   - 分析告警根因

**输出**：告警处理记录

### 步骤 4：故障排查

**目的**：定位和解决系统故障

**输入**：
- 故障现象描述
- 系统日志和监控数据
- 故障排查手册

**操作**：

1. **故障确认**
   - 确认故障现象
   - 评估故障影响
   - 确定故障级别

2. **故障定位**
   - 收集相关日志
   - 分析调用链路
   - 定位故障原因

3. **故障修复**
   - 制定修复方案
   - 执行修复操作
   - 验证修复结果

4. **故障总结**
   - 编写故障报告
   - 分析故障根因
   - 提出改进措施

**输出**：故障报告

### 步骤 5：容量管理

**目的**：评估和规划系统容量

**输入**：
- 性能监控数据
- 业务增长趋势
- 容量规划标准

**操作**：

1. **容量评估**
   - 分析当前容量
   - 评估资源使用率
   - 识别容量瓶颈

2. **需求预测**
   - 分析业务增长
   - 预测容量需求
   - 制定扩容计划

3. **容量优化**
   - 优化资源配置
   - 优化应用性能
   - 优化成本效益

**输出**：容量规划报告

### 步骤 6：运维优化

**目的**：持续改进运维效率

**输入**：
- 运维数据分析
- 故障和告警记录
- 团队反馈

**操作**：

1. **流程优化**
   - 分析运维流程
   - 识别优化点
   - 改进运维效率

2. **工具优化**
   - 评估工具效果
   - 引入新的工具
   - 自动化常见操作

3. **知识沉淀**
   - 更新运维文档
   - 完善故障手册
   - 分享运维经验

**输出**：优化建议报告

## What To Check

### 必检项

| 检查项 | 标准 | 检查方法 | 通过条件 |
|--------|------|----------|----------|
| 监控完整 | 核心指标有监控 | 配置检查 | 覆盖率 > 95% |
| 告警有效 | 告警阈值设置合理 | 历史分析 | 无频繁误报 |
| 巡检执行 | 按计划执行巡检 | 巡检记录 | 100% 已执行 |
| 故障闭环 | 故障及时处理 | 故障记录 | 处理时效达标 |

### 建议检查项

| 检查项 | 标准 | 检查方法 | 通过条件 |
|--------|------|----------|----------|
| 响应及时 | 告警响应及时 | 响应记录 | 响应时效达标 |
| 文档完善 | 运维文档完整 | 文档检查 | 文档更新及时 |
| 知识共享 | 经验有效沉淀 | 知识库检查 | 知识更新及时 |

## Quality Criteria

### 质量维度

| 维度 | 要求 | 权重 |
|------|------|------|
| 稳定性 | 系统稳定运行 | 30% |
| 响应性 | 问题及时响应 | 25% |
| 可观测性 | 监控完善有效 | 25% |
| 持续改进 | 运维持续优化 | 20% |

## Output Specification

### 产出清单

| 产出 | 格式 | 必填 | 描述 |
|------|------|------|------|
| 监控方案 | .md | 是 | 监控指标和告警规则 |
| 运维手册 | .md | 是 | 日常运维指南 |
| 应急预案 | .md | 是 | 故障处理流程 |
| 巡检报告 | .md | 是 | 周期巡检结果 |
| 容量报告 | .md | 否 | 容量评估建议 |


## Overview

> High-level description of the monitor-operate execution process.
>
> This instruction defines the technical approach, key activities, and success criteria for the monitor-operate scenario.


## Technical Specifications

> Detailed technical requirements and implementation guidelines for monitor-operate.

### Required Tools
- [List required tools and frameworks]

### Environment Requirements
- [List environment prerequisites]

### Configuration Parameters
- [List key configuration parameters]


## Best Practices

> Industry-standard best practices for monitor-operate execution.

1. **Practice 1**: Define SLOs with measurable error budgets
2. **Practice 2**: Configure actionable alerts with clear runbooks
3. **Practice 3**: Maintain operational dashboards for real-time visibility


## Error Handling

> Common error scenarios and resolution strategies for monitor-operate.

### Error Category 1
**Symptom**: Alerts are noisy or fail to signal real issues
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]

### Error Category 2
**Symptom**: Mean time to detect (MTTD) exceeds target
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]


## Quality Standards

> Acceptance criteria and quality gates for monitor-operate deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | MTTD is 5 minutes or less | Automated check |
| Standard 2 | Alert noise rate is 20% or lower | Automated check |
| Standard 3 | SLO compliance is 99.5% or higher | Automated check |
