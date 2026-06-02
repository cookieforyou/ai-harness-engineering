---
name: prepare-release
description: "Detailed technical instructions for prepare-release scenario execution"
applyTo: "scenarios/prepare-release/**"
phase: deployment
type: instruction
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['instruction', 'technical']
---
# Instructions: 发布准备 (Prepare Release)

## Release Type Standards

### 版本号规范

```yaml
# 语义化版本 (Semantic Versioning)
version_format: "MAJOR.MINOR.PATCH"

# 版本规则
version_rules:
  major:
    trigger: "破坏性变更"
    example: "2.0.0"
    description: "不兼容的 API 变更"

  minor:
    trigger: "新增功能"
    example: "1.2.0"
    description: "向后兼容的功能新增"

  patch:
    trigger: "缺陷修复"
    example: "1.1.1"
    description: "向后兼容的缺陷修复"

  pre_release:
    trigger: "预发布"
    example: "1.0.0-alpha.1"
    description: "测试版本"

  apply-hotfix:
    trigger: "紧急修复"
    example: "1.0.1"
    description: "生产问题紧急修复"
```

## Release Process Standards

### 发布阶段

```
┌─────────────────────────────────────────────────────────────┐
│                     RELEASE PHASES                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌───────────┐   ┌───────────┐   ┌───────────┐   ┌─────────┐ │
│  │  PLANNING │ → │ PREPARING │ → │ EXECUTING │ → │ CLOSING │ │
│  └───────────┘   └───────────┘   └───────────┘   └─────────┘ │
│       ↓              ↓               ↓              ↓       │
│   发布计划        发布准备        发布执行       发布收尾    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 发布检查清单

```yaml
# Pre-Release 检查清单
pre_release_checklist:
  code_quality:
    - name: "代码评审完成"
      required: true
    - name: "代码静态检查通过"
      required: true
    - name: "无新引入的 P0/P1 bug"
      required: true

  testing:
    - name: "单元测试覆盖率 ≥ 80%"
      required: true
    - name: "集成测试全部通过"
      required: true
    - name: "E2E 测试全部通过"
      required: true
    - name: "性能测试达标"
      required: false

  security:
    - name: "安全扫描通过"
      required: true
    - name: "依赖漏洞扫描通过"
      required: true
    - name: "敏感信息检查通过"
      required: true

  documentation:
    - name: "API 文档更新"
      required: true
    - name: "变更日志更新"
      required: true
    - name: "用户文档更新"
      required: false
```

## Release Review Standards

### 评审委员会

```yaml
release_review_board:
  members:
    - role: "Release Manager"
      responsibility: "发布协调"
    - role: "Tech Lead"
      responsibility: "技术决策"
    - role: "QA Lead"
      responsibility: "质量评估"
    - role: "Product Manager"
      responsibility: "业务确认"

  decision_modes:
    - mode: "GO"
      description: "可以发布"
    - mode: "NO-GO"
      description: "不允许发布"
    - mode: "CONDITIONAL-GO"
      description: "有条件发布"
```

### 评审检查项

| 检查项 | 权重 | 通过标准 |
|--------|------|----------|
| 测试完成度 | 20% | ≥ 95% |
| 代码质量 | 20% | 无高危问题 |
| 性能指标 | 15% | 达标 |
| 安全合规 | 25% | 无高危漏洞 |
| 文档完整性 | 10% | 完整 |
| 回滚方案 | 10% | 可行 |

## Rollback Plan Standards

### 回滚触发条件

```yaml
rollback_triggers:
  p0:
    - "核心功能不可用"
    - "数据一致性严重问题"
    - "安全漏洞"
    response_time: "5 分钟"

  p1:
    - "主要功能异常"
    - "性能严重下降"
    response_time: "30 分钟"

  p2:
    - "次要功能异常"
    - "非核心问题"
    response_time: "4 小时"
```

### 回滚流程

```
                    ┌─────────────┐
                    │  触发回滚   │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │  评估影响   │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │  审批回滚   │ ← 需 Release Manager 审批
                    └──────┬──────┘
                           │
         ┌─────────────────┼─────────────────┐
         │                 │                 │
  ┌──────▼──────┐    ┌──────▼──────┐    ┌──────▼──────┐
  │ 回滚应用    │    │ 回滚数据    │    │ 回滚配置    │
  └──────┬──────┘    └──────┬──────┘    └──────┬──────┘
         │                 │                 │
         └─────────────────┼─────────────────┘
                           │
                    ┌──────▼──────┐
                    │  验证回滚   │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │  通知干系人 │
                    └─────────────┘
```

### 回滚时间目标

| 环境 | 回滚时间目标 (RTO) |
|------|-------------------|
| 单实例 | 30 分钟 |
| 集群 | 15 分钟 |
| 容器 | 10 分钟 |
| Serverless | 5 分钟 |

## Release Window Standards

### 推荐发布时间

```yaml
# 生产环境发布时间窗口
production_window:
  preferred:
    - day: "Tuesday-Thursday"
      time: "22:00 - 02:00"
      reason: "业务低峰期"

  acceptable:
    - day: "Saturday-Sunday"
      time: "14:00 - 18:00"
      reason: "业务低峰期"

  avoided:
    - day: "Monday"
      reason: "周初业务高峰"
    - day: "Friday"
      reason: "周末前"
    - day: "Holiday"
      reason: "节假日"
```

### 值班安排

```yaml
oncall_requirements:
  release_window:
    duration_hours: 4
    team_size: 2
    roles:
      - "研发值班"
      - "运维值班"
      - "测试值班"

  escalation:
    level1: "值班人员"
    level2: "Team Lead"
    level3: "技术总监"
```

## Monitoring and Alerting Standards

### 发布监控指标

```yaml
# 关键监控指标
key_metrics:
  application:
    - name: "错误率"
      threshold: "> 1%"
      alert: true

    - name: "响应时间 P99"
      threshold: "> 500ms"
      alert: true

    - name: "QPS"
      threshold: "< expected * 0.5"
      alert: true

  infrastructure:
    - name: "CPU 使用率"
      threshold: "> 80%"
      alert: false

    - name: "内存使用率"
      threshold: "> 85%"
      alert: false

    - name: "磁盘使用率"
      threshold: "> 80%"
      alert: true
```

### 监控仪表盘

```yaml
# 发布监控仪表盘
release_dashboard:
  sections:
    - name: "业务指标"
      charts:
        - "请求量趋势"
        - "错误率趋势"
        - "响应时间分布"

    - name: "系统指标"
      charts:
        - "CPU/Memory"
        - "网络流量"
        - "数据库连接"

    - name: "对比视图"
      charts:
        - "发布前后对比"
        - "同环比分析"
```

## Communication Standards

### 发布通知模板

```markdown
# 【发布通知】{项目名称} {版本号}

## Release Time
{日期} {时间}

## Release Content
1. 功能更新
   - {功能1}
   - {功能2}

2. 问题修复
   - {BUG-123}: {问题描述}

## Impact Scope
- {系统A}: 无影响
- {系统B}: 需要配合升级

## Notes
- {注意事项1}
- {注意事项2}

## Rollback Plan
如遇问题，请联系 {联系方式}

## Contacts
- 技术负责人: {姓名}
- 值班电话: {电话}
```

## Post-release Review

### Post-Release Review

```yaml
post_release_review:
  timing: "发布后 24 小时"

  agenda:
    - name: "发布回顾"
      items:
        - "发布是否按计划完成"
        - "是否有遗漏项"

    - name: "问题分析"
      items:
        - "发布中发现的问题"
        - "潜在风险"

    - name: "改进建议"
      items:
        - "流程优化建议"
        - "工具改进建议"

  participants:
    - "Release Manager"
    - "研发团队"
    - "运维团队"
    - "测试团队"
```


## Overview

> High-level description of the prepare-release execution process.
>
> This instruction defines the technical approach, key activities, and success criteria for the prepare-release scenario.


## Technical Specifications

> Detailed technical requirements and implementation guidelines for prepare-release.

### Required Tools
- [List required tools and frameworks]

### Environment Requirements
- [List environment prerequisites]

### Configuration Parameters
- [List key configuration parameters]


## Best Practices

> Industry-standard best practices for prepare-release execution.

1. **Practice 1**: Validate all checklist items are completed before release
2. **Practice 2**: Ensure release notes accurately reflect changes
3. **Practice 3**: Obtain all required approvals per governance policy


## Error Handling

> Common error scenarios and resolution strategies for prepare-release.

### Error Category 1
**Symptom**: Release is blocked by incomplete prerequisites
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]

### Error Category 2
**Symptom**: Release notes contain errors or omissions
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]


## Quality Standards

> Acceptance criteria and quality gates for prepare-release deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | Pre-release checklist completion is 100% | Automated check |
| Standard 2 | Release notes accuracy is 98% or higher | Automated check |
| Standard 3 | All required approvals are obtained and documented | Automated check |
## References

- [harness-engineering.md](../standards/harness-engineering.md)
- [output-validation-checklist.md](../evaluations/output-validation-checklist.md)
- [regression-checklist.md](../evaluations/regression-checklist.md)
