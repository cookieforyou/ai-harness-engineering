---
name: backup-data
description: "backup data execution prompt for E2E delivery workflow"
type: prompt
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
language: "zh-CN"
tags: ['prompt', 'ai-execution']
---
# Prompt: 数据备份 (Backup Data)

## Purpose

本提示词指导AI执行数据备份任务，按照业务需求设计并实现完整的数据备份策略，确保数据安全、可恢复，并满足RPO/RTO目标。

### Key Objectives

- **准确理解备份需求**: 深入分析数据类型、恢复目标和合规要求，确保备份策略匹配业务需求
- **高可靠性备份方案**: 设计分层备份策略（全量/增量/差异），兼顾恢复速度和存储成本
- **备份可恢复验证**: 确保备份数据可完整恢复，定期执行恢复演练
- **安全合规保障**: 实现数据加密、访问控制和合规保留策略
- **规范交接准备**: 生成完整的备份策略文档和恢复手册

## Input Variables (变量定义)

> **AI 在执行前必须确认以下变量已填充**，如未填充则请求用户提供

| Variable | Type | Required | Default | Description | Validation |
|----------|------|----------|---------|-------------|------------|
| `data_types` | array | true | - | 数据类型: database\|file\|config\|log | 至少1种数据类型 |
| `rpo_hours` | number | true | - | 恢复点目标(小时)，最大可接受数据丢失时间窗口 | 正整数，≤24h |
| `rto_hours` | number | true | - | 恢复时间目标(小时)，最大可接受服务中断时间 | 正整数，≤48h |
| `backup_types` | array | true | - | 备份类型: full\|incremental\|differential | 至少包含full |
| `retention_days` | number | true | - | 备份保留天数 | 正整数，≥7 |
| `storage_type` | string | true | - | 存储类型: local\|cloud\|tape | 有效的存储类型 |
| `environments` | array | true | - | 环境列表: dev\|staging\|prod | 非空字符串数组 |
| `encryption_required` | boolean | true | - | 是否需要加密传输和存储 | true/false |

### 示例: 变量的正确格式

```yaml
# 示例: 完整的数据备份输入
data_types:
  - "database"
  - "file"
  - "config"
rpo_hours: 4
rto_hours: 8
backup_types:
  - "full"
  - "incremental"
retention_days: 90
storage_type: "cloud"
environments:
  - "dev"
  - "staging"
  - "prod"
encryption_required: true
```

## Chain of Thought (思维链)

> **AI 必须按照以下思维链逐步执行**，每完成一步后进行自我验证

```
[THINK] Step 1: 理解备份需求和业务约束
   ├─ 输入: data_types, rpo_hours, rto_hours, environments
   ├─ 思考: 哪些数据需要备份？RPO/RTO要求有多严格？有哪些合规约束？
   ├─ 验证: 与业务需求对照，确认无遗漏数据类型
   └─ 输出: 备份需求分析（数据清单、恢复目标、合规要求、风险评估）
   ↓
[ANALYZE] Step 2: 分析备份技术和存储方案
   ├─ 输入: 备份需求分析, storage_type, backup_types, encryption_required
   ├─ 思考: 各数据类型的最佳备份技术？存储成本vs恢复速度权衡？
   ├─ 验证: 方案满足RPO/RTO目标，加密方案符合安全要求
   └─ 输出: 备份技术方案（备份技术选型、存储架构、加密策略）
   ↓
[DESIGN] Step 3: 设计备份策略和计划
   ├─ 输入: 备份技术方案, retention_days, backup_types
   ├─ 思考: 备份频率如何设置？保留周期如何规划？备份窗口如何安排？
   ├─ 验证: 备份窗口在业务低峰期，保留策略满足合规审计要求
   └─ 输出: 备份策略设计（备份计划、保留策略、恢复流程、监控方案）
   ↓
[IMPLEMENT] Step 4: 实现备份系统
   ├─ 输入: 备份策略设计, environments
   ├─ 思考: 备份脚本如何编写？监控告警如何配置？备份验证如何自动化？
   ├─ 验证: 备份任务配置正确，监控告警覆盖所有失败场景
   └─ 输出: 备份脚本 + 配置 + 监控规则 + 自动化验证
   ↓
[VERIFY] Step 5: 验证备份可用性和完整性
   ├─ 输入: 备份系统实现, rpo_hours, rto_hours
   ├─ 执行: 执行恢复测试、校验备份完整性、测量恢复时间
   ├─ 验证: 备份成功率≥99.9%，RPO/RTO符合目标，恢复测试通过
   └─ 输出: 备份验证报告（恢复测试结果、RTO/RPO测量、完整性报告）
   ↓
[HANDOVER] Step 6: 准备交接给运维阶段
   ├─ 生成: Handover Context（备份策略、恢复手册、监控配置）
   ├─ 更新: Global Context（备份状态、存储使用、演练计划）
   └─ 通知: Monitor-Operate Agent（提交运维交接请求）
```

## Error Handling (错误处理)

> **AI 在执行过程中遇到以下情况时的处理策略**

### Error Scenario 1: 备份任务失败

**识别信号**: 
- Backup job failed / Exit code != 0
- 备份日志显示错误信息

**处理流程**:
```
IF 备份任务失败
THEN
  1. 检查备份日志获取错误详情
  2. 确认存储空间是否充足
  3. 检查网络连接和权限配置
  4. 重新执行备份任务
  5. IF 持续失败 THEN 告警通知并升级
END
```

**降级方案**: 切换备用存储位置，使用简化备份策略

**升级条件**: 连续3次失败，或核心数据备份失败

---

### Error Scenario 2: 存储空间不足

**识别信号**: 
- Disk full / No space left on device
- 存储容量告警触发

**处理流程**:
```
IF 存储空间不足
THEN
  1. 检查当前备份大小和增长速度
  2. 清理过期备份释放空间
  3. 评估是否需要扩展存储容量
  4. 调整保留策略或备份频率
  5. 记录存储扩容需求
END
```

**降级方案**: 临时增加清理频率，减少保留版本数

**升级条件**: 存储容量即将耗尽且无法通过清理解决

---

### Error Scenario 3: 备份文件损坏

**识别信号**: 
- Checksum mismatch / Corrupted archive
- 恢复测试失败

**处理流程**:
```
IF 备份文件损坏
THEN
  1. 验证备份文件校验和
  2. 使用上一版本正常备份恢复
  3. 重新执行完整备份
  4. 分析损坏原因（硬件/网络/软件）
  5. 修复根本问题防止再次发生
END
```

**降级方案**: 回退到最近可用的正常备份，增加校验频率

**升级条件**: 连续多个备份版本损坏，或所有备份版本均不可用

---

### Error Scenario 4: 恢复失败

**识别信号**: 
- Restore job failed / Data inconsistent
- 恢复后数据完整性校验不通过

**处理流程**:
```
IF 恢复失败
THEN
  1. 检查备份文件可用性
  2. 验证恢复环境和目标配置
  3. 尝试从其他备份点恢复
  4. IF 所有备份均失败 THEN 启动灾备方案
  5. 记录恢复失败原因和影响范围
END
```

**降级方案**: 启动异地灾备副本恢复，联系厂商技术支持

**升级条件**: 所有恢复路径均失败，影响业务连续性

## Quality Metrics (质量指标)

### Key Performance Indicators (KPIs)

| KPI ID | 指标名称 | 目标值 | 计算公式 | 验证方法 | 权重 |
|--------|----------|--------|----------|----------|------|
| KPI-001 | BACKUP-SUCCESS | ≥99.9% | (成功备份数/总备份数)×100% | 备份任务日志统计 | 30% |
| KPI-002 | RPO-COMPLY | =100% | (RPO达标次数/总验证次数)×100% | 恢复点时间测量 | 25% |
| KPI-003 | RESTORE-TEST | =100% | (成功恢复测试数/总恢复测试数)×100% | 定期恢复演练 | 25% |
| KPI-004 | BACKUP-TIME | ≤4h | 全量备份实际执行时间 | 定时记录 | 20% |

**综合评分计算**: 
```
Quality Score = (BACKUP-SUCCESS达标?分数) × 0.30 + (RPO-COMPLY×100) × 0.25 + (RESTORE-TEST×100) × 0.25 + (BACKUP-TIME达标?分数) × 0.20
合格: ≥70分 | 优秀: ≥85分 | 卓越: ≥95分
```

## Output Format (输出格式)

> AI必须按照以下结构生成数据备份交付物

```markdown
## Data Backup Deliverables

### 1. Summary
- **Status**: completed / partial / blocked
- **Completion**: {percentage}
- **Quality Score**: {score}/100

### 2. Backup Strategy
- **RPO Target**: {rpo_hours}h
- **RTO Target**: {rto_hours}h
- **Backup Types**: {full / incremental / differential}
- **Retention Period**: {retention_days} days
- **Storage Type**: {storage_type}
- **Encryption**: {yes / no}

### 3. Backup Schedule
| Backup Type | Frequency | Time | Retention |
|-------------|-----------|------|-----------|
| Full | Weekly | Sunday 02:00 | 4 weeks |
| Incremental | Daily | Daily 02:00 | 7 days |

### 4. Recovery Procedures
- **Database Restore**: Step-by-step DB recovery process
- **File Restore**: File-level recovery process
- **Disaster Recovery**: Cross-region recovery process

### 5. Verification Results
- **Backup Success Rate**: {X}% (target: ≥99.9%)
- **RPO Compliance**: {X}% (target: 100%)
- **Restore Test Result**: {passed / failed}
- **Full Backup Time**: {X}h (target: ≤4h)

### 6. Quality Score
- **Overall Score**: {score}/100
- **Grade**: Excellent (≥95) / Good (≥85) / Satisfactory (≥70) / Needs Improvement (<70)
- **KPI Breakdown**:
  - BACKUP-SUCCESS: {value}% (target: ≥99.9%) - {pass/fail}
  - RPO-COMPLY: {value}% (target: 100%) - {pass/fail}
  - RESTORE-TEST: {value}% (target: 100%) - {pass/fail}
  - BACKUP-TIME: {value}h (target: ≤4h) - {pass/fail}
```

## Output Validation (输出验证)

> **重要**: 在提交前，必须完成以下验证步骤

### Validation Checklist

**V-001: Backup Completeness (备份完整性验证)**
- [ ] 所有数据类型已配置备份（database/file/config/log）
- [ ] 所有环境已覆盖（dev/staging/prod）
- [ ] 备份范围与数据清单一致，无遗漏

**V-002: Backup Recoverability (备份可恢复验证)**
- [ ] 恢复测试执行成功
- [ ] 恢复后数据一致性校验通过
- [ ] 恢复时间 ≤ 目标RTO

**V-003: RPO/RTO Compliance (恢复目标合规验证)**
- [ ] 实际RPO ≤ 目标RPO（{rpo_hours}h）
- [ ] 实际RTO ≤ 目标RTO（{rto_hours}h）
- [ ] 备份窗口在业务低峰期

**V-004: Security Compliance (安全合规验证)**
- [ ] 备份数据已加密（传输中和存储时）
- [ ] 访问控制已配置（最小权限原则）
- [ ] 合规保留策略已实施

**V-005: Monitoring and Alerting (监控告警验证)**
- [ ] 备份状态监控已配置
- [ ] 存储容量告警已设置
- [ ] 备份失败可及时通知相关人员

### Validation Failure Handling

```
IF any validation check fails
THEN
  1. 识别具体失败项和严重程度
  2. 尝试修复（基于可用信息）
  3. IF 无法修复 THEN 标记为 [NEEDS REVIEW] 并附详细说明
  4. 生成验证报告（每项pass/fail状态）
  5. 高亮关键问题
  6. IF 关键问题存在 THEN 不进行交接
END
```

## Handover Context (交接上下文)

> 完成数据备份任务后，生成以下交接信息

```yaml
handover:
  header:
    from_stage: "backup-data"
    to_stage: "monitor-operate"
    handover_id: "HO-{{timestamp}}-{{sequence}}"
    timestamp: "{{ISO8601}}"
    prepared_by: "{{agent.name}}"

  summary:
    status: "completed/partial/blocked"
    completion_percentage: {{0-100}}
    quality_score: {{0-100}}
    total_backups: {{number}}
    daily_backup_size_gb: {{number}}
    total_storage_tb: {{number}}

  artifacts:
    delivered:
      - name: "Backup Strategy Document"
        path: "docs/backup-strategy.md"
        version: "1.0.0"
      - name: "Backup Scripts"
        path: "scripts/backup/"
        version: "1.0.0"
      - name: "Recovery Guide"
        path: "docs/recovery-guide.md"
        version: "1.0.0"
      - name: "Monitoring Configuration"
        path: "docs/monitoring.md"
        version: "1.0.0"

  metrics:
    backup_success_rate: {{percentage}}
    average_backup_time: {{minutes}}
    average_restore_time: {{minutes}}
    storage_usage_gb: {{number}}

  decisions:
    - id: "DC-001"
      description: "Backup technology selection"
      rationale: "Chose {technology} for data type {type}"
      alternatives_considered: ["{alt1}", "{alt2}"]
      impact: "Affects backup speed and storage cost"

  open_issues:
    blocking: []
    non_blocking:
      - id: "ISSUE-001"
        description: "Recovery drill not completed for {environment}"
        risk_level: "low"
        planned_resolution: "Schedule recovery drill within next sprint"

  risks:
    - id: "RISK-001"
      description: "Cross-region replication latency"
      probability: "low"
      impact: "medium"
      mitigation: "Monitor replication lag"
      contingency_plan: "Activate active-passive DR plan"

  quality_metrics:
    kpi_results:
      - kpi_id: "KPI-001"
        name: "BACKUP-SUCCESS"
        value: 99.95
        target: 99.9
        unit: "%"
        status: "pass"
      - kpi_id: "KPI-002"
        name: "RPO-COMPLY"
        value: 100
        target: 100
        unit: "%"
        status: "pass"
      - kpi_id: "KPI-003"
        name: "RESTORE-TEST"
        value: 100
        target: 100
        unit: "%"
        status: "pass"
      - kpi_id: "KPI-004"
        name: "BACKUP-TIME"
        value: 3.5
        target: 4
        unit: "h"
        status: "pass"
    overall_score: 90
    grade: "good"

  recommendations:
    - "Run quarterly recovery drills for all environments"
    - "Monitor storage growth trends to plan capacity"
    - "Review retention policy annually for compliance"
```

## Related Assets (关联资产)

| Asset Type | Path | Description |
|------------|------|-------------|
| Scenario | `../scenarios/backup-data/SCENARIO.md` | 数据备份场景定义 |
| Agent | `../agents/backup-data.agent.md` | 数据备份Agent角色 |
| Instruction | `../instructions/backup-data.instructions.md` | 数据备份技术指令 |

## Related Resources (相关资源)

- **Standards**: 
  - [Backup Standards](../standards/backup-standards.md) - 备份标准和最佳实践
  - [Security Guidelines](../standards/security-guidelines.md) - 安全配置指南
- **Templates**: 
  - [Recovery Plan Template](../templates/recovery-plan.template.md) - 恢复计划模板
- **Evaluations**: 
  - [Backup Audit Checklist](../evaluations/backup-audit-checklist.md) - 备份审计检查清单

## Handover Preparation (交接准备)

使用 [contexts/unified-handover-template.md](../contexts/unified-handover-template.md)。

```yaml
handover:
  header:
    from_stage: "backup-data"
    to_stage: "monitor-operate"
    handover_id: "HO-{ISO8601}-{sequence}"
    timestamp: "{ISO8601}"
    prepared_by: "backup-data"
  summary:
    status: completed|partial|blocked
    quality_score: {0-100}
  artifacts:
    delivered: []
  decisions: []
  open_issues:
    blocking: []
    non_blocking: []
  risks: []
  quality_metrics:
    kpi_results: []
  recommendations: []
```
