---
name: plan-disaster-recovery
description: "灾备恢复规划场景的 AI 提示词"
type: prompt
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
language: "zh-CN"
tags: ['prompt', 'ai-execution']
---
# Disaster Recovery Planning Prompt

## Purpose

本提示词指导AI执行灾备恢复规划任务，基于业务服务依赖关系和RTO/RPO目标，设计高可用的灾备架构、制定详细的恢复流程和演练计划，确保业务连续性。

### Key Objectives

- **精确评估风险**: 分析业务影响和恢复优先级，识别关键系统和数据
- **严格满足SLA**: 确保RTO和RPO目标可达标，100%合规
- **设计高可用架构**: 选择最优灾备架构（冷备/暖备/热备/多活）
- **制定可执行流程**: 编写清晰、可操作的故障转移和恢复手册
- **定期验证演练**: 设计演练方案，持续验证和优化灾备能力

## Input Variables (变量定义)

> **AI 在执行前必须确认以下变量已填充**，如未填充则请求用户提供

| Variable | Type | Required | Default | Description | Validation |
|----------|------|----------|---------|-------------|------------|
| `business_services` | array | true | - | 业务服务列表（含关键等级和依赖关系） | 至少1个服务，包含name和criticality |
| `rto_targets` | object | true | - | 各服务恢复时间目标（RTO，单位分钟） | 每个服务RTO>0 |
| `rpo_targets` | object | true | - | 各服务恢复点目标（RPO，单位分钟） | 每个服务RPO≥0 |
| `dr_site_config` | object | false | {} | 灾备站点配置（区域、网络、计算资源） | 包含region和replication_latency |
| `replication_method` | string | false | "async" | 数据复制方式（sync/async/hybrid） | 有效枚举值 |
| `failover_procedure` | string | false | "" | 现有故障转移流程文档路径或内容 | 文件路径或有效内容 |
| `compliance_standards` | array | false | [] | 合规标准列表（如SOC2/ISO27001/PCI-DSS） | 有效的标准名称列表 |

### 示例: 变量的正确格式

```yaml
# 示例: 完整的灾备规划输入
business_services:
  - name: "订单处理系统"
    criticality: "critical"
    dependencies: ["用户服务", "支付网关", "数据库"]
    daily_revenue_impact: 5000000
  - name: "用户中心"
    criticality: "high"
    dependencies: ["数据库", "缓存"]
    daily_revenue_impact: 2000000

rto_targets:
  "订单处理系统": 15
  "用户中心": 60

rpo_targets:
  "订单处理系统": 5
  "用户中心": 15

dr_site_config:
  primary_region: "cn-beijing"
  dr_region: "cn-shanghai"
  replication_latency_ms: 50
  bandwidth_mbps: 10000

replication_method: "sync"
compliance_standards:
  - "ISO27001"
  - "PCI-DSS"
```

## Chain of Thought (思维链)

> **AI 必须按照以下思维链逐步执行**，每完成一步后进行自我验证

```
[THINK] Step 1: 理解灾备规划范围和目标
   ├─ 输入: business_services, rto_targets, rpo_targets, compliance_standards
   ├─ 思考: 哪些是核心关键业务？RTO/RPO目标是否合理？合规要求有哪些？
   ├─ 验证: 确认所有业务服务已识别，SLA目标清晰且可衡量
   └─ 输出: 灾备规划任务分析摘要（含服务优先级、SLA目标、合规清单）
   ↓
[ANALYZE] Step 2: 分析业务影响和恢复需求
   ├─ 输入: 任务分析摘要，business_services
   ├─ 分析: 业务依赖关系、停机影响（财务/声誉/合规）、恢复优先级排序
   ├─ 验证: 影响分析量化合理，依赖关系完整（含隐式依赖）
   └─ 输出: 业务影响分析报告（含BIA分级、依赖图谱、影响量化表）
   ↓
[ASSESS] Step 3: 评估现有灾备能力和差距
   ├─ 输入: dr_site_config, replication_method, failover_procedure
   ├─ 评估: 当前灾备架构是否满足RTO/RPO？差距多大？技术债务和风险在哪？
   ├─ 验证: 现有能力评估基于实际测试数据而非假设
   └─ 输出: 灾备能力评估报告（含差距分析、风险矩阵、改进优先级）
   ↓
[DESIGN] Step 4: 设计灾备架构和恢复策略
   ├─ 输入: BIA报告，能力评估报告，compliance_standards
   ├─ 设计: 选择灾备架构（冷/暖/热/多活）、设计数据复制策略、制定故障转移方案
   ├─ 验证: 架构满足所有RTO/RPO目标，符合合规要求，成本在可接受范围
   └─ 输出: 灾备架构设计方案（含拓扑图、复制策略、组件清单、成本估算）
   ↓
[IMPLEMENT] Step 5: 制定恢复流程和实施计划
   ├─ 输入: 灾备架构设计方案
   ├─ 制定: 灾难声明流程、故障转移步骤、数据恢复步骤、服务启动顺序、沟通模板
   ├─ 验证: 流程步骤清晰可执行，角色和职责明确，涵盖所有恢复场景
   └─ 输出: 灾备操作手册（含流程图、检查清单、通讯录、决策树）
   ↓
[TEST] Step 6: 设计演练计划和验证方案
   ├─ 输入: 灾备操作手册
   ├─ 设计: 演练场景（桌面/功能/全面）、成功标准、验证方法、改进闭环
   ├─ 验证: 演练覆盖所有关键场景，成功标准可衡量，改进机制完善
   └─ 输出: 演练计划（含时间表、场景列表、成功标准、报告模板）
   ↓
[REVIEW] Step 7: 综合评审灾备方案
   ├─ 输入: 所有上述输出
   ├─ 评审: RTO/RPO达标检查、KPI评分、风险再评估、替代方案比较
   ├─ 验证: RTO-COMPLY=100%, RPO-COMPLY=100%, DR-TEST-FREQ≥1次/半年, RECOVERY-SUCCESS≥99%
   └─ 输出: 灾备规划最终报告（含KPI评分、评审结论、待实施事项）
```

## Error Handling (错误处理)

> **AI 在执行过程中遇到以下情况时的处理策略**

### Error Scenario 1: RTO/RPO目标无法满足

**识别信号**: 
- 业务需求的RTO/RPO超出当前技术能力
- 数据复制延迟超过RPO要求
- 恢复步骤耗时超过RTO限制

**处理流程**:
```
IF RTO/RPO目标在技术上无法满足
THEN
  1. 量化技术限制并分析根本原因
  2. 评估改进方案（升级网络/增加带宽/更换复制技术）
  3. 计算改进方案的成本和实施时间
  4. IF 改进后仍无法满足 THEN
       a. 提供分阶段改进路线图
       b. 建议业务方调整RTO/RPO预期
       c. 标记为 [SLA差距-需协商] 并明确当前可达成值
     END
  5. 提供短期缓解措施（如增加备份频率）
END
```

**降级方案**: 提供当前技术可达的RTO/RPO值，建议分阶段逼近目标

**升级条件**: 核心服务的RTO差距>50%或RPO差距>100%

---

### Error Scenario 2: 演练失败

**识别信号**: 
- 故障转移过程中断或超时
- 数据一致性校验失败
- 服务无法在RTO内恢复

**处理流程**:
```
IF 灾备演练失败
THEN
  1. 立即停止演练并恢复生产环境（如适用）
  2. 分析失败根本原因（使用5 Whys方法）
  3. 记录详细失败信息和恢复步骤
  4. 针对失败原因制定修复方案
  5. 在测试环境验证修复效果
  6. 重新安排演练验证
  7. IF 连续2次演练失败 THEN 升级到架构师团队
END
```

**降级方案**: 简化演练范围，先验证核心服务恢复能力，逐步扩大范围

**升级条件**: 核心服务连续2次演练失败

---

### Error Scenario 3: 数据不一致

**识别信号**: 
- 主备数据库数据校验差异
- 复制延迟超出预期
- 日志序列号不一致

**处理流程**:
```
IF 检测到数据不一致
THEN
  1. 立即停止复制进程，防止不一致扩散
  2. 分析差异范围和影响（受损表/行数、差异时间窗口）
  3. 确定不一致的根因（网络问题/配置错误/软件bug）
  4. 选择修复策略（全量同步/增量修复/从备份恢复）
  5. 执行数据修复并验证一致性
  6. 更新复制配置或修复根本问题
  7. 增加数据一致性校验频率和自动化告警
END
```

**降级方案**: 从最近一致快照恢复，接受有限的数据丢失

**升级条件**: 数据不一致影响核心业务表、或无法确定一致点

---

### Error Scenario 4: 合规要求不满足

**识别信号**: 
- 灾备架构不符合行业合规标准
- 数据驻留要求无法满足
- 审计跟踪不完整

**处理流程**:
```
IF 灾备方案不符合合规要求
THEN
  1. 列出不合规的具体条款和要求
  2. 评估合规差距的严重程度和风险
  3. 设计合规改进方案（数据加密、审计日志、访问控制）
  4. 评估合规改进的成本和影响
  5. IF 无法完全合规 THEN
       a. 提供可接受的风险接受方案
       b. 标记为 [合规差距-需审批]
       c. 记录合规风险接受理由
     END
  6. 更新灾备方案以符合合规要求
END
```

**降级方案**: 实施最小合规措施，申请风险接受，制定合规改进计划

**升级条件**: 涉及监管处罚风险的合规要求不满足

## Output Format (输出格式)

> AI必须按照以下结构生成灾备规划交付物

```markdown
# Disaster Recovery Planning Deliverables

## 1. Task Information
- **Task**: Disaster Recovery Plan for {project_name}
- **Planner**: {agent_name}
- **Completion Date**: {current_date}
- **Status**: Completed / Partial / Blocked

## 2. Business Impact Analysis

### 2.1 Service Criticality Matrix
| Service Name | Criticality | RTO Target | RPO Target | Dependencies | Daily Impact |
|-------------|-------------|-----------|-----------|--------------|--------------|
| {service} | Critical/High/Medium/Low | {N}min | {N}min | {deps} | ${N} |

### 2.2 Dependency Graph Summary
- **Critical Path**: {services chain}
- **Single Points of Failure**: {list}
- **External Dependencies**: {list}

## 3. Current Capability Assessment

### 3.1 Gap Analysis
| Requirement | Current Capability | Target | Gap | Risk Level |
|-------------|-------------------|--------|-----|------------|
| RTO for {service} | {N}min | {N}min | {N}min | H/M/L |
| RPO for {service} | {N}min | {N}min | {N}min | H/M/L |

### 3.2 Risk Matrix
| Risk ID | Description | Likelihood | Impact | Risk Level | Mitigation |
|---------|-------------|-----------|--------|------------|------------|
| R-001 | {desc} | H/M/L | H/M/L | Critical/H/M/L | {mitigation} |

## 4. DR Architecture Design

### 4.1 Architecture Overview
- **DR Model**: Cold Standby / Warm Standby / Hot Standby / Active-Active
- **Primary Site**: {region}
- **DR Site**: {region}
- **Replication**: Synchronous / Asynchronous / Hybrid
- **Failover Type**: Automatic / Manual / Semi-automatic

### 4.2 Component Architecture
| Component | Primary | DR | Replication Method | RPO Achievable |
|-----------|---------|-----|-------------------|---------------|
| Database | {config} | {config} | sync/async | {N}min |
| Application | {config} | {config} | - | - |

### 4.3 Cost Estimation
| Item | Description | Estimated Cost |
|------|-------------|---------------|
| DR Site Infrastructure | {desc} | ${N}/月 |
| Data Replication | {desc} | ${N}/月 |
| Network Bandwidth | {desc} | ${N}/月 |

## 5. Recovery Procedures

### 5.1 Disaster Declaration Process
- **Trigger Conditions**: {conditions}
- **Decision Authority**: {role}
- **Declaration Steps**: {steps}

### 5.2 Failover Steps
| Step | Action | Owner | Expected Duration | Verification |
|------|--------|-------|-----------------|--------------|
| 1 | {action} | {role} | {N}min | {verification} |
| 2 | {action} | {role} | {N}min | {verification} |

### 5.3 Recovery Verification
- Service Health Check: {method}
- Data Integrity Check: {method}
- Performance Validation: {method}

## 6. Testing and Drill Plan

### 6.1 Drill Schedule
| Drill Type | Frequency | Scope | Success Criteria |
|-----------|-----------|-------|-----------------|
| Desktop | Quarterly | Team review | All gaps identified |
| Functional | Bi-annual | Single component | RTO/RPO met |
| Full | Annual | End-to-end | Full recovery verified |

### 6.2 Improvement Process
- Post-drill review within 5 business days
- Action items tracked in remediation plan
- Next drill incorporates lessons learned

## 7. Quality Score

- **Overall Score**: {score}/100
- **Grade**: Excellent (≥95) / Good (≥85) / Satisfactory (≥70) / Needs Improvement (<70)
- **KPI Breakdown**:
  - RTO-COMPLY: {value}% (target: 100%) - {pass/fail} (weight: 35%)
  - RPO-COMPLY: {value}% (target: 100%) - {pass/fail} (weight: 35%)
  - DR-TEST-FREQ: {value} (target: ≥1次/半年) - {pass/fail} (weight: 15%)
  - RECOVERY-SUCCESS: {value}% (target: ≥99%) - {pass/fail} (weight: 15%)
```

## Output Validation (输出验证)

> **重要**: 在提交灾备规划报告前，必须完成以下验证步骤

### Validation Checklist

**V-001: RTO Compliance Validation (恢复时间验证)**
- [ ] 所有关键服务的RTO目标已定义
- [ ] 恢复步骤总时间≤RTO目标（含决策和验证时间）
- [ ] 故障转移自动化程度足够满足RTO要求
- [ ] 人员响应时间已纳入RTO计算

**V-002: RPO Compliance Validation (恢复点验证)**
- [ ] 所有关键数据的RPO目标已定义
- [ ] 数据复制延迟≤RPO要求
- [ ] 备份频率满足RPO要求
- [ ] 数据一致性校验机制已建立

**V-003: Architecture Feasibility Validation (架构可行性验证)**
- [ ] DR站点网络带宽满足数据复制需求
- [ ] 主备站点间的延迟在可接受范围内
- [ ] 容量满足灾备切换后的负载需求
- [ ] 安全控制和访问策略已考虑

**V-004: Procedure Completeness Validation (流程完整性验证)**
- [ ] 所有恢复场景都有对应的流程文档
- [ ] 流程步骤清晰可执行，包含具体命令和操作
- [ ] 角色和职责明确，包含备用人员
- [ ] 沟通计划和升级路径已定义

**V-005: Compliance Validation (合规验证)**
- [ ] 灾备方案符合行业合规标准
- [ ] 数据驻留和隐私保护要求已满足
- [ ] 审计跟踪机制已建立
- [ ] 文档版本管理和审批流程已定义

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
| KPI-001 | RTO-COMPLY | =100% | (达标服务数/总服务数) × 100% | 逐服务验证RTO达标情况 | 35% |
| KPI-002 | RPO-COMPLY | =100% | (达标服务数/总服务数) × 100% | 逐服务验证RPO达标情况 | 35% |
| KPI-003 | DR-TEST-FREQ | ≥1次/半年 | 过去12个月演练次数/2 | 检查演练日历和记录 | 15% |
| KPI-004 | RECOVERY-SUCCESS | ≥99% | (成功恢复次数/总恢复次数) × 100% | 检查演练恢复成功率 | 15% |

**综合评分计算**:
```
Quality Score = RTO-COMPLYScore × 35% + RPO-COMPLYScore × 35% + DR-TEST-FREQScore × 15% + RECOVERY-SUCCESSscore × 15%

RTO/RPO指标得分 = (达标服务数/总服务数) × 100
DR-TEST-FREQ得分 = min(实际频率/目标频率 × 100, 100)
RECOVERY-SUCCESS得分 = 成功率 × 100
合格: ≥70分 | 优秀: ≥85分 | 卓越: ≥95分
```

## Handover Context (交接上下文)

> 完成灾备规划后，生成以下交接信息给实施和运维阶段

```yaml
handover:
  header:
    from_stage: "dr_planning"
    to_stage: "dr_implementation"
    handover_id: "HO-{{timestamp}}-{{sequence}}"
    timestamp: "{{ISO8601}}"
    prepared_by: "{{agent.name}}"

  summary:
    status: "completed/partial/blocked"
    services_covered: {{number}}
    critical_services: {{number}}
    architecture_type: "cold/warm/hot/active-active"
    estimated_annual_cost: {{number}}

  artifacts:
    delivered:
      - name: "DR Plan"
        path: "docs/dr-plan.md"
        version: "1.0.0"
      - name: "Recovery Procedures"
        path: "docs/recovery-procedures.md"
        version: "1.0.0"
      - name: "Failover Diagrams"
        path: "diagrams/failover-architecture.drawio"
        version: "1.0.0"
      - name: "Drill Plan"
        path: "docs/drill-plan.md"
        version: "1.0.0"

  metrics:
    rto_compliance: {{percentage}}%
    rpo_compliance: {{percentage}}%
    dr_test_frequency: {{number}}/year
    recovery_success_rate: {{percentage}}%
    overall_score: {{score}}/100

  decisions:
    - id: "DC-001"
      description: "DR architecture selection"
      rationale: "Selected warm standby for cost-efficiency while meeting RTO"
      alternatives_considered: ["Cold standby", "Hot standby", "Active-active"]
      impact: "Affects DR cost and recovery speed"

  open_issues:
    blocking: []
    non_blocking:
      - id: "ISSUE-001"
        description: "Network encryption for cross-region replication needs upgrade"
        risk_level: "medium"
        planned_resolution: "Schedule network upgrade in next maintenance window"
        owner: "Network Team"

  risks:
    - id: "RISK-001"
      description: "DR site capacity may be insufficient during full failover"
      probability: "low"
      impact: "high"
      mitigation: "Reserve 30% buffer capacity at DR site"
      contingency_plan: "Activate cloud burst capacity if needed"

  recommendations:
    - "Conduct full-scale DR drill within 3 months of implementation"
    - "Automate failover procedures to reduce RTO"
    - "Implement continuous data replication monitoring"
    - "Review and update DR plan quarterly"

  next_steps:
    - "Approve DR architecture and budget"
    - "Procure DR site infrastructure"
    - "Configure data replication pipeline"
    - "Schedule first functional drill"

  quality_metrics:
    kpi_results:
      - kpi_id: "KPI-001"
        name: "RTO-COMPLY"
        value: 100
        target: 100
        unit: "%"
        status: "pass"
        weight: 35
      - kpi_id: "KPI-002"
        name: "RPO-COMPLY"
        value: 100
        target: 100
        unit: "%"
        status: "pass"
        weight: 35
      - kpi_id: "KPI-003"
        name: "DR-TEST-FREQ"
        value: 2
        target: 2
        unit: "次/年"
        status: "pass"
        weight: 15
      - kpi_id: "KPI-004"
        name: "RECOVERY-SUCCESS"
        value: 99.5
        target: 99
        unit: "%"
        status: "pass"
        weight: 15
    overall_score: 94
    grade: "excellent"

## Related Assets (关联资产)

| Asset Type | Path | Description |
|------------|------|-------------|
| Agent | `../agents/plan-disaster-recovery.agent.md` | 灾备规划Agent角色 |
| Instruction | `../instructions/plan-disaster-recovery.instructions.md` | 灾备规划技术指令 |

## Related Resources (相关资源)

- **Standards**: 
  - [DR Planning Standards](../standards/dr-planning-standards.md) - 灾备规划标准
  - [Business Continuity Guidelines](../standards/business-continuity-guidelines.md) - 业务连续性指南
- **Evaluations**: 
  - [DR Plan Review](../evaluations/dr-plan-review.md) - 灾备计划评审
