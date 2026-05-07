---
name: deploy-release
description: "Technical instructions for deployment and release execution"
type: instruction
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['instruction', 'technical']
---
# Deployment Release Instructions

## Purpose

本文档定义了部署发布阶段的标准操作流程、质量检查标准和工作产出规范。部署发布是将测试通过的软件部署到目标环境的过程。

## Investigation Flow

### 流程概览

```
部署规划 → 环境准备 → 部署执行 → 验证检查 → 监控跟踪 → 文档归档
```

### 步骤 1：部署规划

**目的**：制定详细的部署策略和计划

**输入**：
- 测试通过报告
- 部署包清单
- 目标环境信息

**操作**：

1. **部署策略制定**
   - 选择部署方式（蓝绿/滚动/灰度）
   - 确定部署时间窗口
   - 规划回滚策略

2. **部署步骤规划**
   - 分解部署步骤
   - 明确每步验证点
   - 分配责任人

3. **风险评估**
   - 识别部署风险
   - 制定应急预案
   - 准备沟通计划

**输出**：部署计划文档

### 步骤 2：环境准备

**目的**：准备目标部署环境

**输入**：
- 部署计划
- 环境配置
- 资源清单

**操作**：

1. **环境检查**
   - 验证环境可用性
   - 检查资源状态
   - 确认网络连通

2. **配置准备**
   - 准备环境配置
   - 配置参数检查
   - 敏感信息处理

3. **备份准备**
   - 备份当前系统
   - 备份关键数据
   - 验证备份可用

**输出**：就绪的部署环境

### 步骤 3：部署执行

**目的**：按计划执行部署

**输入**：
- 部署计划
- 部署脚本
- 部署包

**操作**：

1. **执行前检查**
   - 确认人员就位
   - 确认通知到位
   - 确认回滚准备

2. **步骤执行**
   - 按计划执行步骤
   - 记录执行日志
   - 及时报告异常

3. **过程监控**
   - 监控部署过程
   - 及时发现异常
   - 快速响应问题

**输出**：部署执行记录

### 步骤 4：验证检查

**目的**：验证部署结果是否符合预期

**输入**：
- 部署执行记录
- 验证检查清单
- 健康检查标准

**操作**：

1. **功能验证**
   - 核心功能检查
   - 业务流程验证
   - 接口调用验证

2. **健康检查**
   - 服务健康状态
   - 资源使用情况
   - 日志无异常

3. **数据验证**
   - 数据完整性
   - 数据一致性
   - 关键业务数据

**输出**：部署验证报告

### 步骤 5：监控跟踪

**目的**：持续监控部署后系统状态

**输入**：
- 部署验证报告
- 监控系统
- 告警配置

**操作**：

1. **持续监控**
   - 监控核心指标
   - 关注异常告警
   - 记录关键数据

2. **问题处理**
   - 及时响应告警
   - 快速定位问题
   - 必要时回滚

3. **状态报告**
   - 定期状态报告
   - 问题汇总报告
   - 干系人通知

**输出**：监控状态报告

### 步骤 6：文档归档

**目的**：完成部署文档和记录归档

**输入**：
- 部署执行记录
- 部署验证报告
- 监控状态报告

**操作**：

1. **文档整理**
   - 整理部署文档
   - 记录变更清单
   - 更新配置文档

2. **经验总结**
   - 记录部署过程问题
   - 总结经验教训
   - 更新部署手册

3. **归档保存**
   - 归档部署记录
   - 保存相关证据
   - 更新知识库

**输出**：归档的部署文档

## What To Check

### 必检项

| 检查项 | 标准 | 检查方法 | 通过条件 |
|--------|------|----------|----------|
| 回滚方案 | 有可执行的回滚方案 | 方案检查 | 方案完整可行 |
| 验证清单 | 有完整的验证清单 | 清单检查 | 清单完整 |
| 备份完成 | 关键数据已备份 | 备份验证 | 备份可用 |
| 通知到位 | 相关人员已通知 | 通知记录 | 100% 已通知 |
| 监控就绪 | 监控系统已配置 | 配置检查 | 配置正确 |

### 建议检查项

| 检查项 | 标准 | 检查方法 | 通过条件 |
|--------|------|----------|----------|
| 资源充足 | 部署资源充足 | 资源检查 | 资源 > 需求 |
| 时间合理 | 部署时间窗口合理 | 计划检查 | 在规定窗口内 |
| 应急预案 | 有完整的应急预案 | 预案检查 | 预案完整 |

## Quality Criteria

### 质量维度

| 维度 | 要求 | 权重 |
|------|------|------|
| 部署安全 | 过程安全可控 | 30% |
| 回滚能力 | 可快速回滚 | 25% |
| 验证完整 | 验证覆盖全面 | 25% |
| 文档完整 | 文档归档完整 | 20% |

## Output Specification

### 产出清单

| 产出 | 格式 | 必填 | 描述 |
|------|------|------|------|
| 部署计划 | .md | 是 | 部署步骤和策略 |
| 回滚方案 | .md | 是 | 回滚操作步骤 |
| 部署检查清单 | .md | 是 | 验证检查项 |
| 部署报告 | .md | 是 | 部署执行记录 |


## Overview

> High-level description of the deploy-release execution process.
>
> This instruction defines the technical approach, key activities, and success criteria for the deploy-release scenario.


## Technical Specifications

> Detailed technical requirements and implementation guidelines for deploy-release.

### Required Tools
- [List required tools and frameworks]

### Environment Requirements
- [List environment prerequisites]

### Configuration Parameters
- [List key configuration parameters]


## Best Practices

> Industry-standard best practices for deploy-release execution.

1. **Practice 1**: Use blue-green or canary deployment to minimize risk
2. **Practice 2**: Automate rollback triggers based on health metrics
3. **Practice 3**: Maintain deployment audit logs for compliance


## Error Handling

> Common error scenarios and resolution strategies for deploy-release.

### Error Category 1
**Symptom**: Deployment causes service degradation or outage
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]

### Error Category 2
**Symptom**: Rollback procedure fails or takes excessive time
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]


## Quality Standards

> Acceptance criteria and quality gates for deploy-release deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | Deployment success rate meets 99% target | Automated check |
| Standard 2 | Rollback completes within 15 minutes | Automated check |
| Standard 3 | Zero-downtime deployment achieved for user-facing services | Automated check |
