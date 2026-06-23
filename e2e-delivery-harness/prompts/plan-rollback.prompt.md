---
name: plan-rollback
description: "回滚计划场景的 AI 提示词"
type: prompt
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['prompt', 'ai-execution']
---
# Rollback Planning Prompt

## Purpose

本提示词指导AI执行回滚规划任务，基于发布版本和变更内容制定详细、可执行的回滚方案，确保在部署出现问题时能够快速、安全地恢复到稳定状态，最小化业务影响。

### Key Objectives

- **全面评估风险**: 分析变更影响范围，识别高风险组件和依赖关系
- **制定回滚策略**: 选择最佳回滚方式（Blue-Green/Canary/Feature Toggle/DB Migration）
- **准备自动化脚本**: 编写经过验证的回滚脚本，确保幂等性和可靠性
- **保障数据一致**: 设计数据回滚方案，确保数据完整性和一致性
- **优化恢复速度**: 确保RTO≤15分钟，最大限度减少停机时间

## Input Variables (变量定义)

> **AI 在执行前必须确认以下变量已填充**，如未填充则请求用户提供

| Variable | Type | Required | Default | Description | Validation |
|----------|------|----------|---------|-------------|------------|
| `release_version` | string | true | - | 发布版本号 | 非空字符串，格式：vX.Y.Z |
| `rollback_triggers` | array | true | - | 回滚触发条件列表 | 至少1个条件，包含指标和阈值 |
| `affected_services` | array | true | - | 受影响的服务列表 | 至少1个服务，含名称和版本 |
| `rollback_steps` | array | true | - | 回滚步骤列表 | 至少1个步骤，含操作和负责人 |
| `data_migration_plan` | object | false | {} | 数据迁移/回滚方案 | 包含forward和rollback脚本路径 |
| `approval_chain` | array | false | [] | 审批链（角色列表） | 至少1个审批角色 |
| `communication_plan` | object | false | {} | 沟通计划模板 | 包含通知模板和升级路径 |

### 示例: 变量的正确格式

```yaml
# 示例: 完整的回滚规划输入
release_version: "v2.1.0"
rollback_to_version: "v2.0.0"

rollback_triggers:
  - metric: "error_rate"
    threshold: 5
    unit: "%"
    duration_minutes: 5
    auto_rollback: true
  - metric: "response_time_p99"
    threshold: 2000
    unit: "ms"
    duration_minutes: 10
    auto_rollback: false

affected_services:
  - name: "api-gateway"
    version: "v2.1.0"
    rollback_version: "v2.0.0"
    strategy: "blue-green"
  - name: "user-service"
    version: "v2.1.0"
    rollback_version: "v2.0.0"
    strategy: "rolling-update"

rollback_steps:
  - step 1: "停止新版本流量" | owner: SRE | 2min
  - step 2: "执行数据库回滚" | owner: DBA | 5min
  - step 3: "回退应用到v2.0.0" | owner: SRE | 3min
  - step 4: "验证服务健康状态" | owner: QA | 5min

data_migration_plan:
  has_migration: true
  forward_script: "scripts/migrate-v2.1.0.sql"
  rollback_script: "scripts/rollback-v2.1.0.sql"
  estimated_time_minutes: 10

approval_chain:
  - role: "Tech Lead" | required: true | escalation_timeout: 5min
  - role: "Release Manager" | required: true | escalation_timeout: 3min

communication_plan:
  slack: "#release-war-room"
  templates:
    rollback_started: "【回滚通知】版本 {version} 回滚已启动，原因：{reason}"
    rollback_completed: "【回滚完成】版本 {version} 已成功回滚到 {target_version}"
    rollback_failed: "【回滚失败】版本 {version} 回滚失败，需人工介入"
```

## Chain of Thought (思维链)

> **AI 必须按照以下思维链逐步执行**，每完成一步后进行自我验证

```
[THINK] Step 1: 理解回滚需求和应用上下文
   ├─ 输入: release_version, affected_services, rollback_triggers
   ├─ 思考: 本次回滚的触发条件是什么？受影响的服务有哪些？目标版本是什么？
   ├─ 验证: 版本号正确，回滚目标明确，触发条件量化可衡量
   └─ 输出: 回滚任务分析摘要（含版本信息、触发条件、影响范围概览）
   ↓
[ANALYZE] Step 2: 分析变更影响和回滚风险
   ├─ 输入: 任务分析摘要, data_migration_plan, affected_services
   ├─ 分析: 代码/配置/数据变更的影响范围，回滚的依赖关系和风险点
   ├─ 验证: 影响分析全面，考虑了数据、配置、依赖服务的回滚影响
   └─ 输出: 影响分析报告（含变更清单、依赖图谱、风险评估矩阵）
   ↓
[PLAN] Step 3: 制定回滚策略和步骤
   ├─ 输入: 影响分析报告, rollback_steps, data_migration_plan
   ├─ 规划: 选择回滚策略（Blue-Green/Canary/Feature Toggle/DB Rollback），编排步骤顺序
   ├─ 验证: 策略选择合理，步骤覆盖所有受影响组件，总时间≤15min
   └─ 输出: 回滚策略方案（含策略选择、步骤编排、时间估算、资源清单）
   ↓
[PREPARE] Step 4: 准备回滚脚本和验证工具
   ├─ 输入: 回滚策略方案, data_migration_plan
   ├─ 准备: 编写自动化回滚脚本、数据回滚脚本、验证脚本，配置监控告警
   ├─ 验证: 脚本语法正确，幂等性验证通过，回滚时间满足RTO要求
   └─ 输出: 回滚脚本集（含部署回滚、配置回滚、数据库回滚、验证脚本）
   ↓
[EXECUTE] Step 5: 执行回滚验证和演练
   ├─ 输入: 回滚脚本集, approval_chain, communication_plan
   ├─ 执行: 在测试环境演练回滚流程，验证每一步的时间和结果
   ├─ 验证: 回滚后系统功能正常、数据完整、监控恢复，RTO≤15min
   └─ 输出: 回滚演练报告（含演练结果、时间记录、问题清单、优化建议）
   ↓
[VERIFY] Step 6: 验证回滚方案完整性和KPI达标
   ├─ 输入: 所有上述输出
   ├─ 验证: ROLLBACK-TESTED=100%, RECOVERY-RTO≤15min, DATA-CONSISTENCY=100%, AUTOMATION-LEVEL≥80%
   ├─ 确认: 审批链完整，沟通计划就绪，回滚方案可用于生产
   └─ 输出: 回滚规划最终报告（含KPI评分、审批状态、就绪确认）
```

## Error Handling (错误处理)

> **AI 在执行过程中遇到以下情况时的处理策略**

### Error Scenario 1: 回滚脚本执行超时

**识别信号**: 单步超时预估150% / 数据库回滚超时 / 健康检查超时

**处理流程**:
```
IF 回滚脚本执行超时
THEN 停止回滚 → 评估系统状态（部分/未回滚/不一致）
  → 部分回滚：检查已回滚组件状态，决定继续或回退
  → 完全未回滚：分析原因（资源/脚本/依赖），修复后重试
  → 无法恢复：升级为P0事故，启动应急响应
END
```

**降级方案**: 手动执行关键步骤，跳过非关键步骤，优先恢复核心服务

**升级条件**: 核心服务回滚超时>30分钟或数据状态不一致

---

### Error Scenario 2: 回滚后服务仍然异常

**识别信号**: 健康检查失败 / 错误率未恢复 / 功能验证不通过

**处理流程**:
```
IF 回滚后服务仍然异常
THEN 确认回滚完整性（版本/配置）→ 分析异常原因（上下游/数据/环境）
  → 检查依赖服务和数据版本匹配
  → 回滚完整但问题依旧：上一版本可能也有该问题，重新制定方案
  → 无法快速解决：升级到技术负责人
END
```

**降级方案**: 回滚到更早的稳定版本，或启用维护页面

**升级条件**: 核心服务回滚后15分钟内仍无法恢复

---

### Error Scenario 3: 数据库回滚失败

**识别信号**: SQL错误 / 外键约束冲突 / 数据量超时

**处理流程**:
```
IF 数据库回滚失败
THEN 停止操作 → 评估数据状态（部分/未回滚/损坏）
  → 脚本错误：修复并在测试环境验证后重试
  → 数据量过大或约束冲突：评估备份恢复方案
  → 无法恢复：升级到DBA团队和数据架构师
END
```

**降级方案**: 从最近可用备份全量恢复，接受有限数据丢失

**升级条件**: 核心业务表数据损坏，或恢复时间超过RTO

---

### Error Scenario 4: 回滚审批延迟

**识别信号**: 审批人超时未响应 / 审批链无法联系 / 权限不足

**处理流程**:
```
IF 回滚审批延迟
THEN 按审批链升级 → 使用备用联系方式
  → 超过紧急阈值（P0:3min/P1:5min）：自动升级更高权限人
  → 按紧急授权规则执行回滚，记录异常情况
  → 事后复盘改进审批流程
END
```

**降级方案**: 按照紧急授权规则执行回滚，事后补办审批手续

**升级条件**: P0超过3分钟、P1超过5分钟无审批响应

## Output Format (输出格式)

> AI必须按照以下结构生成回滚规划交付物

```markdown
# Rollback Planning Deliverables

## 1. Task Information
- **Release Version**: {release_version}
- **Rollback Target**: {rollback_target_version}
- **Planner**: {agent_name}
- **Completion Date**: {current_date}
- **Status**: Completed / Partial / Blocked

## 2. Change Analysis

### 2.1 Change Scope
| Change Type | Description | Risk Level | Rollback Complexity |
|-------------|-------------|------------|-------------------|
| Code | {description} | H/M/L | H/M/L |
| Configuration | {description} | H/M/L | H/M/L |
| Data Migration | {description} | H/M/L | H/M/L |

### 2.2 Dependency Mapping
| Service | Depends On | Affected By Rollback | Rollback Order |
|---------|-----------|---------------------|----------------|
| {service} | {deps} | Yes/No | {N} |

### 2.3 Risk Assessment
| Risk ID | Description | Probability | Impact | Mitigation |
|---------|-------------|-------------|--------|------------|
| R-001 | {description} | L/M/H | L/M/H | {mitigation} |

## 3. Rollback Strategy

### 3.1 Strategy Selection
| Service | Strategy | Rationale | Estimated RTO |
|---------|---------|-----------|---------------|
| {service} | Blue-Green/Canary/Feature-Toggle/DB-Rollback | {rationale} | {N}min |

### 3.2 Rollback Steps
| Step | Action | Owner | Duration | Auto/Manual | Verification |
|------|--------|-------|----------|-------------|--------------|
| 1 | {action} | {role} | {N}min | Auto/Manual | {check} |
| 2 | {action} | {role} | {N}min | Auto/Manual | {check} |
| **Total** | | | **{N}min** | | |

## 4. Rollback Scripts

### 4.1 Script Inventory
| Script Name | Purpose | Language | Tested | Idempotent |
|------------|---------|----------|--------|------------|
| rollback-app.sh | 应用版本回滚 | bash | ✅/❌ | ✅/❌ |
| rollback-db.sql | 数据库回滚 | SQL | ✅/❌ | ✅/❌ |
| verify-health.sh | 健康检查验证 | bash | ✅/❌ | ✅/❌ |

### 4.2 Automation Level
- **Automated Steps**: {N}/{Total} ({percentage}%)
- **Manual Steps**: {N}/{Total} ({percentage}%)
- **Target Automation**: ≥80%

## 5. Rollback Drill Results

### 5.1 Test Environment Validation
| Test Scenario | Result | Actual RTO | Issues Found |
|--------------|--------|-----------|--------------|
| Full rollback | Pass/Fail | {N}min | {issues} |
| Data rollback | Pass/Fail | {N}min | {issues} |
| Partial rollback | Pass/Fail | {N}min | {issues} |

### 5.2 Data Consistency Verification
- **Pre-rollback Data Snapshot**: ✅/❌
- **Post-rollback Data Integrity**: ✅/❌
- **Data Loss Assessment**: {N} records / None
- **Consistency Rate**: {percentage}%

## 6. Communication & Approval

### 6.1 Approval Chain
| Order | Role | Required | Status |
|-------|------|----------|--------|
| 1 | {role} | Yes/No | Approved/Pending/Escalated |
| 2 | {role} | Yes/No | Approved/Pending/Escalated |

### 6.2 Communication Templates
- **Rollback Start**: {template}
- **Rollback Complete**: {template}
- **Rollback Failed**: {template}

## 7. Quality Score

- **Overall Score**: {score}/100
- **Grade**: Excellent (≥95) / Good (≥85) / Satisfactory (≥70) / Needs Improvement (<70)
- **KPI Breakdown**:
  - ROLLBACK-TESTED: {value}% (target: 100%) - {pass/fail} (weight: 30%)
  - RECOVERY-RTO: {value}min (target: ≤15min) - {pass/fail} (weight: 30%)
  - DATA-CONSISTENCY: {value}% (target: 100%) - {pass/fail} (weight: 25%)
  - AUTOMATION-LEVEL: {value}% (target: ≥80%) - {pass/fail} (weight: 15%)
```

## Output Validation (输出验证)

> **重要**: 在提交回滚规划报告前，必须完成以下验证步骤

### Validation Checklist

**V-001: Rollback Completeness Validation (回滚完整性验证)**
- [ ] 所有受影响的服务都有明确的回滚步骤
- [ ] 代码、配置、数据回滚均已被覆盖
- [ ] 回滚步骤覆盖了所有环境（staging/production）
- [ ] 依赖服务的回滚顺序正确

**V-002: RTO Compliance Validation (恢复时间验证)**
- [ ] 总回滚时间（含决策和验证）≤15分钟
- [ ] 每步的时间估算合理且有依据
- [ ] 并行步骤已识别并优化
- [ ] 验证时间已纳入RTO计算

**V-003: Data Consistency Validation (数据一致性验证)**
- [ ] 数据库回滚脚本已验证
- [ ] 回滚后数据完整性检查方案已定义
- [ ] 数据迁移的逆向操作已测试
- [ ] 回滚后缓存/索引重建已考虑

**V-004: Automation Validation (自动化验证)**
- [ ] ≥80%的回滚步骤已自动化
- [ ] 自动化脚本已在测试环境验证通过
- [ ] 脚本具备幂等性（可重复执行）
- [ ] 错误处理和回退机制已实现

**V-005: Communication Validation (沟通验证)**
- [ ] 审批链完整且联系方式就绪
- [ ] 通知模板已准备
- [ ] 升级路径已定义
- [ ] 干系人列表已更新

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
| KPI-001 | ROLLBACK-TESTED | =100% | (已验证的组件数/总组件数) × 100% | 检查回滚演练覆盖范围 | 30% |
| KPI-002 | RECOVERY-RTO | ≤15min | 从回滚开始到服务恢复的总时间 | 在测试环境演练计时 | 30% |
| KPI-003 | DATA-CONSISTENCY | =100% | (一致性校验通过项/总校验项) × 100% | 回滚后数据完整性检查 | 25% |
| KPI-004 | AUTOMATION-LEVEL | ≥80% | (自动化步骤数/总步骤数) × 100% | 统计脚本自动化覆盖比例 | 15% |

**综合评分计算**:
```
Quality Score = ROLLBACK-TESTEDScore × 30% + RECOVERY-RTOScore × 30% + DATA-CONSISTENCYScore × 25% + AUTOMATION-LEVELScore × 15%

ROLLBACK-TESTED得分 = 覆盖率 × 100
RECOVERY-RTO得分 = IF RTO≤15min THEN 100 ELSE max(0, 100 - (实际RTO-15)×5)
DATA-CONSISTENCY得分 = 一致率 × 100
AUTOMATION-LEVEL得分 = 自动化率 × 100
合格: ≥70分 | 优秀: ≥85分 | 卓越: ≥95分
```

## Handover Context (交接上下文)

> 完成回滚规划后，生成以下交接信息给部署发布阶段

```yaml
handover:
  header:
    from_stage: "rollback_planning"
    to_stage: "deploy_release"
    handover_id: "HO-{{timestamp}}-{{sequence}}"
    timestamp: "{{ISO8601}}"
    prepared_by: "{{agent.name}}"

  summary:
    status: "completed/partial/blocked"
    release_version: "{{release_version}}"
    rollback_target: "{{rollback_target}}"
    estimated_rto: {{number}}min
    automation_level: {{percentage}}%
    services_covered: {{number}}

  artifacts:
    delivered:
      - name: "Rollback Plan"
        path: "docs/rollback-plan.md"
        version: "1.0.0"
      - name: "Rollback Scripts"
        path: "scripts/rollback/"
        version: "1.0.0"
      - name: "Rollback Drill Report"
        path: "docs/drill-report.md"
        version: "1.0.0"
      - name: "Communication Templates"
        path: "docs/communication-templates.md"
        version: "1.0.0"

  metrics:
    rollback_tested: {{percentage}}%
    recovery_rto: {{number}}min
    data_consistency: {{percentage}}%
    automation_level: {{percentage}}%
    overall_score: {{score}}/100

  decisions:
    - id: "DC-001"
      description: "Rollback strategy per service"
      rationale: "Selected Blue-Green for api-gateway to minimize downtime"
      alternatives_considered: ["Rolling update", "Recreate"]
      impact: "Affects rollback speed and resource requirements"

  open_issues:
    blocking: []
    non_blocking:
      - id: "ISSUE-001"
        description: "Database rollback script needs performance optimization"
        risk_level: "low"
        planned_resolution: "Optimize SQL and add indexing in next sprint"
        owner: "DBA Team"

  risks:
    - id: "RISK-001"
      description: "Database rollback may exceed RTO for large datasets"
      probability: "low"
      impact: "medium"
      mitigation: "Pre-warmed database snapshots for fast recovery"
      contingency_plan: "Fail over to read replica and rebuild"

  recommendations:
    - "Automate remaining manual rollback steps to improve RTO"
    - "Perform rollback drill before each production deployment"
    - "Monitor rollback triggers in real-time during deployment"
    - "Keep rollback plan updated with each release"

  next_steps_for_deployment:
    - "Integrate rollback triggers into CI/CD pipeline"
    - "Verify rollback scripts are accessible in deployment environment"
    - "Brief on-call team on rollback procedures"
    - "Confirm approval chain availability during deployment window"

  quality_metrics:
    kpi_results:
      - kpi_id: "KPI-001"
        name: "ROLLBACK-TESTED"
        value: 100
        target: 100
        unit: "%"
        status: "pass"
        weight: 30
      - kpi_id: "KPI-002"
        name: "RECOVERY-RTO"
        value: 12
        target: 15
        unit: "min"
        status: "pass"
        weight: 30
      - kpi_id: "KPI-003"
        name: "DATA-CONSISTENCY"
        value: 100
        target: 100
        unit: "%"
        status: "pass"
        weight: 25
      - kpi_id: "KPI-004"
        name: "AUTOMATION-LEVEL"
        value: 85
        target: 80
        unit: "%"
        status: "pass"
        weight: 15
    overall_score: 93
    grade: "excellent"

## Related Assets (关联资产)

| Asset Type | Path | Description |
|------------|------|-------------|
| Agent | `../agents/plan-rollback.agent.md` | 回滚规划Agent角色 |
| Instruction | `../instructions/plan-rollback.instructions.md` | 回滚规划技术指令 |

## Related Resources (相关资源)

- **Standards**: 
  - [Rollback Planning Standards](../standards/rollback-planning-standards.md) - 回滚规划标准
  - [Release Management Guidelines](../standards/release-management-guidelines.md) - 发布管理指南
- **Evaluations**: 
  - [Rollback Plan Review](../evaluations/rollback-plan-review.md) - 回滚计划评审
