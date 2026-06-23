---
name: prepare-release
description: "prepare release execution prompt for E2E delivery workflow"
type: prompt
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
language: "zh-CN"
tags: ['prompt', 'ai-execution']
---
# Release Preparation Prompt

## Purpose

本提示词指导AI执行发布准备任务，作为Release Manager协调版本发布的完整准备工作，确保发布包、文档、审批和回滚方案全部就绪，保障发布过程安全可控。

### Key Objectives

- **完整发布清单**: 确保发布检查清单100%完成，无遗漏项
- **准确文档同步**: 确保发布说明、变更记录和部署文档100%准确
- **严格审批合规**: 确保所有必需的审批和评审已100%完成
- **高成功率保障**: 确保发布成功率≥95%，通过充分的准备工作降低风险
- **回滚就绪确认**: 验证回滚方案已经过测试，可在紧急情况下立即执行

## Input Variables (变量定义)

> **AI 在执行前必须确认以下变量已填充**，如未填充则请求用户提供

| Variable | Type | Required | Default | Description | Validation |
|----------|------|----------|---------|-------------|------------|
| `release_version` | string | true | - | 发布版本号 | 非空字符串，格式：vX.Y.Z |
| `release_notes` | markdown | true | - | 发布说明文档 | 包含功能列表、Bug修复、已知问题 |
| `deployment_plan` | object | true | - | 部署计划（步骤、环境、时间窗口） | 包含部署步骤和回滚步骤 |
| `rollback_plan` | object | true | - | 回滚方案引用 | 有效的回滚计划路径或内容 |
| `approval_list` | array | true | - | 审批人列表 | 至少包含Tech Lead和Release Manager |
| `communication_template` | string | false | "" | 沟通通知模板 | 包含发布前/中/后的通知内容模板 |
| `go_nogo_criteria` | array | true | - | Go/No-Go决策标准列表 | 至少3个可量化的决策标准 |

### 示例: 变量的正确格式

```yaml
# 示例: 完整的发布准备输入
release_version: "v3.0.0"

release_notes: |
  # Release v3.0.0
  
  ## New Features
  - 用户画像2.0: 新增行为分析和标签系统
  - 推荐算法优化: 引入深度学习模型，推荐准确率提升15%
  
  ## Bug Fixes
  - BUG-123: 修复登录超时问题
  - BUG-456: 修复支付并发扣款问题
  
  ## Known Issues
  - 旧版API将在下个版本弃用

deployment_plan:
  environments: ["staging", "production"]
  time_window: { date: "2024-06-15", start: "22:00", end: "02:00", tz: "CST" }
  strategy: "rolling-update"
  steps: ["DB迁移", "后端部署", "前端部署", "功能验证"]
  validation: ["健康检查", "冒烟测试", "回归测试"]

rollback_plan:
  reference: "docs/rollback-plan-v3.0.0.md"
  tested: true
  last_drill: "2024-06-10"

approval_list:
  - { role: "Tech Lead", name: "张三", required: true }
  - { role: "QA Lead", name: "李四", required: true }
  - { role: "Release Manager", name: "王五", required: true }

communication_template:
  pre: "【预通知】版本 {version} 将于 {time} 部署"
  during: "【进行中】版本 {version} 进度: {progress}%"
  post: "【完成】版本 {version} 已部署到 {environment}"

go_nogo_criteria:
  - criterion: "P0/P1 Bug已修复" | check: Bug系统 | pass: P0=0,P1=0
  - criterion: "测试通过率≥95%" | check: 测试报告 | pass: ≥95%
  - criterion: "代码评审完成" | check: PR状态 | pass: 全部approved
  - criterion: "回滚方案已验证" | check: 演练报告 | pass: RTO≤15min
```

## Chain of Thought (思维链)

> **AI 必须按照以下思维链逐步执行**，每完成一步后进行自我验证

```
[THINK] Step 1: 理解发布需求和范围
   ├─ 输入: release_version, release_notes, deployment_plan
   ├─ 思考: 本次发布包含哪些功能和修复？目标环境是什么？发布时间窗口和策略？
   ├─ 验证: 发布范围清晰，版本号与Release Notes一致，部署策略合适
   └─ 输出: 发布任务分析摘要（含发布范围、时间计划、策略选择）
   ↓
[ANALYZE] Step 2: 分析发布依赖和风险
   ├─ 输入: 任务分析摘要, deployment_plan, rollback_plan
   ├─ 分析: 依赖服务是否就绪？数据库变更是否兼容？是否有并行发布冲突？
   ├─ 验证: 外部依赖已确认，数据迁移兼容前后版本，无发布窗口冲突
   └─ 输出: 发布依赖和风险评估报告（含依赖清单、冲突检测、风险矩阵）
   ↓
[PLAN] Step 3: 制定详细发布计划
   ├─ 输入: 依赖和风险评估报告, go_nogo_criteria, approval_list
   ├─ 规划: 制定分阶段发布步骤、检查点设置、Go/No-Go决策时刻、通讯计划
   ├─ 验证: 步骤完整覆盖部署/验证/回滚，检查点设置合理，沟通路径清晰
   └─ 输出: 详细发布计划（含阶段划分、任务分配、时间线、检查点）
   ↓
[PREPARE] Step 4: 准备发布包和文档
   ├─ 输入: 发布计划, release_notes, communication_template
   ├─ 准备: 构建发布包、编写/审核Release Notes、准备部署脚本、准备沟通模板
   ├─ 验证: 发布包完整性校验通过，文档100%准确，脚本语法正确
   └─ 输出: 发布交付物（含发布包、Release Notes、部署脚本、沟通通知）
   ↓
[VERIFY] Step 5: 验证发布就绪状态
   ├─ 输入: 发布交付物, go_nogo_criteria, approval_list
   ├─ 验证: 逐项检查Go/No-Go标准、确认审批完成、验证回滚方案就绪
   ├─ 验证: CHECKLIST-COMPLETE=100%, DOC-ACCURACY=100%, APPROVAL-COMPLY=100%
   └─ 输出: 发布就绪验证报告（含Go/No-Go检查表、审批状态、风险审查）
   ↓
[APPROVE] Step 6: 获取最终发布批准
   ├─ 输入: 发布就绪验证报告
   ├─ 执行: 召开Go/No-Go会议、记录决策、通知所有干系人
   ├─ 验证: 所有审批人已签署，Go条件全部满足，无阻止性障碍
   └─ 输出: 发布批准确认（含Go/No-Go决策记录、审批签名、最终确认）
```

## Error Handling (错误处理)

> **AI 在执行过程中遇到以下情况时的处理策略**

### Error Scenario 1: 发布包构建失败

**识别信号**: 编译错误 / 镜像构建失败 / 依赖冲突 / 签名校验失败

**处理流程**:
```
IF 发布包构建失败
THEN 收集日志 → 分析原因（代码/依赖/环境）
  → 代码问题：通知开发团队修复
  → 依赖问题：检查版本和仓库
  → 环境问题：检查构建环境配置
  → 修复后重新构建，连续3次失败升级到Tech Lead
END
```

**降级方案**: 使用上个成功构建版本为基础，应用增量变更

**升级条件**: 核心发布包连续3次构建失败

---

### Error Scenario 2: Go/No-Go条件不满足

**识别信号**: 测试通过率<95% / 存在未修复P0/P1 Bug / 回滚未验证 / 审批未完成

**处理流程**:
```
IF Go条件不满足
THEN 列出未满足条件 → 评估影响
  → 可快速修复（<1h）：分配责任人修复并重验
  → 无法在窗口前修复：建议推迟发布，记录原因
  → 必须按计划（紧急修复）：记录风险接受，获例外批准，标记[有条件发布]
END
```

**降级方案**: 推迟发布，或通过风险接受流程有条件下发

**升级条件**: P0/P1 Go条件不满足且无法快速修复

---

### Error Scenario 3: 关键审批人不可用

**识别信号**: 审批人未响应 / 无法联系 / 权限变更

**处理流程**:
```
IF 关键审批人不可用
THEN 尝试备用联系方式 → 15分钟无法联系则升级替补审批人
  → 无可用审批人：升级更高级别管理者，请求临时授权
  → 记录异常情况，事后完善审批流程
END
```

**降级方案**: 请求临时授权或升级到更高级别管理者审批

**升级条件**: 所有审批人路径均不可用且无临时授权机制

---

### Error Scenario 4: 环境就绪检查失败

**识别信号**: 环境资源不足 / 依赖服务异常 / 网络不通 / 安全策略错误

**处理流程**:
```
IF 目标环境就绪检查失败
THEN 确认失败环境和资源 → 评估修复时间
  → 资源不足：协调扩容或检查备用环境
  → 依赖异常：通知负责人，评估降级部署
  → 无法在窗口前修复：使用备用环境或推迟发布
END
```

**降级方案**: 使用备用环境部署，或调整部署顺序跳过不可用依赖

**升级条件**: 生产环境核心资源不可用，或无法在发布窗口前修复

## Output Format (输出格式)

> AI必须按照以下结构生成发布准备交付物

```markdown
# Release Preparation Deliverables

## 1. Task Information
- **Release Version**: {release_version}
- **Release Manager**: {agent_name}
- **Completion Date**: {current_date}
- **Status**: Completed / Partial / Blocked

## 2. Release Summary

### 2.1 Release Scope
| Category | Count | Details |
|----------|-------|---------|
| New Features | {N} | {feature list} |
| Bug Fixes | {N} | {bug list} |
| Infrastructure Changes | {N} | {change list} |
| Data Migrations | {N} | {migration list} |

### 2.2 Deployment Plan
- **Environment**: staging → production
- **Strategy**: Rolling Update / Blue-Green / Canary
- **Time Window**: {date} {start_time} - {end_time} ({timezone})
- **Estimated Duration**: {N} hours

## 3. Release Artifacts

### 3.1 Build Artifacts
| Artifact | Version | Build Status | Checksum | Size |
|----------|---------|-------------|----------|------|
| {service}-{version}.jar | {version} | ✅/❌ | {sha256} | {N}MB |

### 3.2 Documentation
| Document | Status | Reviewer | Last Updated |
|----------|--------|----------|-------------|
| Release Notes | ✅ Complete / ⚠️ Pending | {reviewer} | {date} |
| Deployment Guide | ✅ Complete / ⚠️ Pending | {reviewer} | {date} |
| Rollback Guide | ✅ Complete / ⚠️ Pending | {reviewer} | {date} |

## 4. Go/No-Go Decision

### 4.1 Criteria Status
| Criterion | Verification Method | Status | Notes |
|-----------|-------------------|--------|-------|
| {criterion} | {method} | ✅ Pass / ❌ Fail | {notes} |
| {criterion} | {method} | ✅ Pass / ❌ Fail | {notes} |

### 4.2 Decision
- **Decision**: Go / No-Go / Conditional Go
- **Decision Time**: {timestamp}
- **Approved By**: {approver_name}
- **Conditions (if any)**: {conditions}

## 5. Approvals

| Role | Approver | Status | Time | Notes |
|------|---------|--------|------|-------|
| Tech Lead | {name} | ✅/⏳/❌ | {timestamp} | |
| QA Lead | {name} | ✅/⏳/❌ | {timestamp} | |
| Release Manager | {name} | ✅/⏳/❌ | {timestamp} | |

## 6. Rollback Readiness

| Item | Status | Details |
|------|--------|---------|
| Rollback Plan | ✅ Ready / ❌ Not Ready | version {N} |
| Rollback Tested | ✅ Yes / ❌ No | last drill: {date} |
| Rollback RTO | {N}min | target: ≤15min |
| Auto-Rollback | ✅ Enabled / ❌ Manual | trigger: {condition} |

## 7. Communication Status

| Stakeholder Group | Notified | Acknowledged | Channel |
|------------------|----------|-------------|---------|
| Development Team | ✅/❌ | ✅/❌ | Slack |
| QA Team | ✅/❌ | ✅/❌ | Slack |
| Operations Team | ✅/❌ | ✅/❌ | Slack |
| Product Team | ✅/❌ | ✅/❌ | Email |

## 8. Quality Score

- **Overall Score**: {score}/100
- **Grade**: Excellent (≥95) / Good (≥85) / Satisfactory (≥70) / Needs Improvement (<70)
- **KPI Breakdown**:
  - CHECKLIST-COMPLETE: {value}% (target: 100%) - {pass/fail} (weight: 30%)
  - DOC-ACCURACY: {value}% (target: 100%) - {pass/fail} (weight: 25%)
  - APPROVAL-COMPLY: {value}% (target: 100%) - {pass/fail} (weight: 25%)
  - RELEASE-SUCCESS: {value}% (target: ≥95%) - {pass/fail} (weight: 20%)
```

## Output Validation (输出验证)

> **重要**: 在提交发布准备报告前，必须完成以下验证步骤

### Validation Checklist

**V-001: Release Readiness Validation (发布就绪验证)**
- [ ] 所有Go/No-Go标准已检查，满足Go条件
- [ ] 发布包完整性校验通过
- [ ] 部署环境就绪（资源、网络、依赖服务）
- [ ] 发布时间窗口已确认，无冲突

**V-002: Documentation Accuracy Validation (文档准确性验证)**
- [ ] Release Notes与实际变更一致
- [ ] 部署文档中的步骤和命令正确
- [ ] 回滚方案版本匹配
- [ ] 文档中无占位符和TODO标记
- [ ] 已知问题已明确标注

**V-003: Approval Compliance Validation (审批合规验证)**
- [ ] 所有强制审批人已完成审批
- [ ] Go/No-Go决策有正式记录
- [ ] 审批超时和升级有处理记录
- [ ] 风险接受有书面确认

**V-004: Rollback Readiness Validation (回滚就绪验证)**
- [ ] 回滚方案已通过演练验证
- [ ] 回滚脚本在目标环境可用
- [ ] 回滚RTO满足≤15分钟
- [ ] 回滚触发条件已配置到监控系统

**V-005: Communication Validation (沟通验证)**
- [ ] 所有干系人已收到发布通知
- [ ] 沟通模板已准备完毕
- [ ] 升级路径和联系方式已确认
- [ ] 发布状态更新机制已建立

### Validation Failure Handling

```
IF any validation check fails
THEN
  1. Identify specific failed items and severity
  2. Attempt to fix based on available information
  3. IF cannot fix THEN mark as [NEEDS REVIEW] with detailed explanation
  4. Generate validation report with pass/fail status for each check
  5. Highlight critical issues requiring immediate attention
  6. Provide recommendations for improvement
  7. IF critical issues exist THEN do not proceed to handover
END
```

## Quality Metrics (质量指标)

### Key Performance Indicators (KPIs)

| KPI ID | 指标名称 | 目标值 | 计算公式 | 验证方法 | 权重 |
|--------|----------|--------|----------|----------|------|
| KPI-001 | CHECKLIST-COMPLETE | =100% | (已完成检查项/总检查项) × 100% | 逐项检查发布清单 | 30% |
| KPI-002 | DOC-ACCURACY | =100% | (通过审核的文档数/总文档数) × 100% | 干系人评审确认 | 25% |
| KPI-003 | APPROVAL-COMPLY | =100% | (已完成审批/总必需审批) × 100% | 检查审批系统记录 | 25% |
| KPI-004 | RELEASE-SUCCESS | ≥95% | (成功发布次数/总发布次数) × 100% | 历史发布成功率统计 | 20% |

**综合评分计算**:
```
Quality Score = CHECKLIST-COMPLETEScore × 30% + DOC-ACCURACYScore × 25% + APPROVAL-COMPLYScore × 25% + RELEASE-SUCCESSScore × 20%

各指标得分 = (实际值 / 目标值) × 100, 最高100分
合格: ≥70分 | 优秀: ≥85分 | 卓越: ≥95分
```

## Handover Context (交接上下文)

> 完成发布准备后，生成以下交接信息给部署发布阶段

```yaml
handover:
  header:
    from_stage: "release_preparation"
    to_stage: "deploy_release"
    handover_id: "HO-{{timestamp}}-{{sequence}}"
    timestamp: "{{ISO8601}}"
    prepared_by: "{{agent.name}}"

  summary:
    status: "completed/partial/blocked"
    release_version: "{{release_version}}"
    go_nogo_decision: "go/no-go/conditional"
    deployment_strategy: "{{deployment_strategy}}"
    release_window: "{{date}} {{start}}-{{end}}"

  artifacts:
    delivered:
      - name: "Release Package"
        path: "artifacts/release-{{version}}/"
        version: "{{version}}"
        checksum: "{{SHA256}}"
      - name: "Release Notes"
        path: "docs/release-notes-v{{version}}.md"
        version: "{{version}}"
      - name: "Deployment Plan"
        path: "docs/deployment-plan-v{{version}}.md"
        version: "{{version}}"
      - name: "Rollback Plan"
        path: "docs/rollback-plan-v{{version}}.md"
        version: "{{version}}"

  metrics:
    checklist_complete: {{percentage}}%
    doc_accuracy: {{percentage}}%
    approval_comply: {{percentage}}%
    release_success: {{percentage}}%
    overall_score: {{score}}/100

  approvals:
    - role: "Tech Lead"
      name: "{{name}}"
      status: "approved/pending"
      timestamp: "{{ISO8601}}"
    - role: "QA Lead"
      name: "{{name}}"
      status: "approved/pending"
      timestamp: "{{ISO8601}}"
    - role: "Release Manager"
      name: "{{name}}"
      status: "approved/pending"
      timestamp: "{{ISO8601}}"

  open_issues:
    blocking: []
    non_blocking:
      - id: "ISSUE-001"
        description: "Performance test shows 5% degradation on report generation"
        risk_level: "low"
        decision: "Accept for this release, optimize in next iteration"
        owner: "Performance Team"

  risks:
    - id: "RISK-001"
      description: "Database migration may cause brief read-only window"
      probability: "medium"
      impact: "medium"
      mitigation: "Schedule migration during lowest traffic period"
      contingency_plan: "Fail over to read replica during migration"

  recommendations:
    - "Monitor error rates closely for first 30 minutes post-deployment"
    - "Keep rollback team on standby during deployment window"
    - "Schedule post-release review within 48 hours"
    - "Document lessons learned for process improvement"

  next_steps_for_deployment:
    - "Execute deployment per plan at scheduled time window"
    - "Monitor deployment progress and system health"
    - "Execute post-deployment validation"
    - "Confirm rollback readiness before leaving deployment window"

  quality_metrics:
    kpi_results:
      - kpi_id: "KPI-001"
        name: "CHECKLIST-COMPLETE"
        value: 100
        target: 100
        unit: "%"
        status: "pass"
        weight: 30
      - kpi_id: "KPI-002"
        name: "DOC-ACCURACY"
        value: 100
        target: 100
        unit: "%"
        status: "pass"
        weight: 25
      - kpi_id: "KPI-003"
        name: "APPROVAL-COMPLY"
        value: 100
        target: 100
        unit: "%"
        status: "pass"
        weight: 25
      - kpi_id: "KPI-004"
        name: "RELEASE-SUCCESS"
        value: 97
        target: 95
        unit: "%"
        status: "pass"
        weight: 20
    overall_score: 95
    grade: "excellent"

## Related Assets (关联资产)

| Asset Type | Path | Description |
|------------|------|-------------|
| Agent | `../agents/prepare-release.agent.md` | 发布准备Agent角色 |
| Instruction | `../instructions/prepare-release.instructions.md` | 发布准备技术指令 |

## Related Resources (相关资源)

- **Standards**: 
  - [Release Management Standards](../standards/release-management-standards.md) - 发布管理标准
  - [Change Management Guidelines](../standards/change-management-guidelines.md) - 变更管理指南
- **Evaluations**: 
  - [Release Readiness Review](../evaluations/release-readiness-review.md) - 发布就绪评审
