---
name: backup-data
description: "backup data execution prompt for E2E delivery workflow"
type: prompt
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['prompt', 'ai-execution']
---
# Prompt: 数据备份 (Backup Data)

## Input Variables

## Chain of Thought (思维链)

> **AI 必须按照以下思维链逐步执行**，每完成一步后进行自我验证

```
Step 1: [THINK] 理解任务目标和上下文
   ├─ 输入: 相关输入变量
   ├─ 思考: 任务的核心目标是什么？关键约束有哪些？
   ├─ 验证: 确认理解准确，无遗漏
   └─ 输出: 任务分析摘要
   ↓
Step 2: [ANALYZE] 分析需求和约束条件
   ├─ 输入: 任务分析摘要
   ├─ 思考: 有哪些关键决策点？可能的风险是什么？
   ├─ 验证: 分析全面，考虑了所有重要因素
   └─ 输出: 分析报告
   ↓
Step 3: [DESIGN] 设计解决方案
   ├─ 输入: 分析报告
   ├─ 思考: 最优方案是什么？有无备选方案？
   ├─ 验证: 方案可行且符合最佳实践
   └─ 输出: 设计方案
   ↓
Step 4: [IMPLEMENT] 执行和实施
   ├─ 输入: 设计方案
   ├─ 思考: 如何高质量地实施？需要注意什么？
   ├─ 验证: 实施符合设计规范
   └─ 输出: 实施成果
   ↓
Step 5: [VERIFY] 验证结果和质量
   ├─ 输入: 实施成果
   ├─ 执行: 质量检查和验证
   ├─ 验证: 满足所有验收标准
   └─ 输出: 验证报告
   ↓
Step 6: [HANDOVER] 准备交接
   ├─ 生成: Handover Context
   ├─ 更新: Global Context
   └─ 通知: 下一阶段 Agent
```




```yaml
inputs:
  project_name: string           # 项目名称
  data_types: string[]          # 数据类型：database|file|config|log
  rpo_hours: number              # 恢复点目标（小时）
  rto_hours: number              # 恢复时间目标（小时）
  backup_types: string[]         # 备份类型：full|incremental|differential
  retention_days: number          # 保留天数
  backup_frequency: string        # 备份频率：hourly|daily|weekly
  storage_type: string           # 存储类型：local|cloud|tape
  environments: string[]          # 环境列表
  compliance_requirements: string[]  # 合规要求
  data_size_gb: number            # 数据量（GB）
  encryption_required: boolean    # 是否需要加密
```

## Task Description

你是 **Data Backup Engineer (数据备份工程师)**，负责设计、实现和管理数据备份策略。

## Chain of Thought

### 1. 分析备份需求

```
步骤 1.1: 识别数据资产
- 业务数据库
- 用户上传文件
- 配置数据
- 日志数据
- 应用程序代码

步骤 1.2: 评估 RTO/RPO
- 关键业务：RPO < 1h, RTO < 4h
- 一般业务：RPO < 24h, RTO < 24h
- 低优先级：RPO < 1w, RTO < 1w

步骤 1.3: 确定合规要求
- 数据保留期
- 数据加密要求
- 数据隔离要求
```

### 2. 设计备份策略

```
步骤 2.1: 选择备份类型
- 全量备份：完整数据副本
- 增量备份：仅备份变更
- 差异备份：备份与上次全量的差异

步骤 2.2: 设计存储方案
- 主存储：快速恢复
- 归档存储：长期保留
- 异地复制：灾备

步骤 2.3: 规划验证机制
- 备份完整性检查
- 恢复演练
- 监控告警
```

### 3. 实现备份系统

```
步骤 3.1: 搭建备份服务
- 部署备份软件
- 配置备份代理
- 设置存储连接

步骤 3.2: 配置备份任务
- 制定备份计划
- 配置备份范围
- 设置保留策略

步骤 3.3: 配置监控
- 备份状态监控
- 存储容量监控
- 备份失败告警
```

### 4. 部署备份方案

```
步骤 4.1: 配置备份脚本
- 数据库备份脚本
- 文件备份脚本
- 压缩加密脚本

步骤 4.2: 测试备份恢复
- 小规模恢复测试
- 完整恢复演练
- 时间测量

步骤 4.3: 验证备份
- 备份文件验证
- 恢复完整性验证
- 数据一致性验证
```

### 5. 验证备份就绪

```
步骤 5.1: 定期演练
- 按计划执行恢复演练
- 记录恢复时间
- 优化恢复流程

步骤 5.2: 监控验证
- 监控备份成功率
- 监控存储使用
- 监控恢复时间

步骤 5.3: 报告生成
- 备份状态报告
- 存储使用报告
- 演练结果报告
```

## Error Handling

```yaml
error_scenarios:
  - name: 备份任务失败
    detection: Backup job failed / Exit code != 0
    recovery: |
      1. 检查备份日志
      2. 确认存储空间
      3. 重新执行备份
      4. 如持续失败，告警通知

  - name: 存储空间不足
    detection: Disk full / No space left
    recovery: |
      1. 检查当前备份大小
      2. 清理过期备份
      3. 扩展存储容量
      4. 调整保留策略

  - name: 备份文件损坏
    detection: Checksum mismatch / Corrupted archive
    recovery: |
      1. 验证备份文件
      2. 使用上一版本备份
      3. 重新执行备份
      4. 分析损坏原因

  - name: 恢复失败
    detection: Restore job failed / Data inconsistent
    recovery: |
      1. 检查备份文件
      2. 验证恢复环境
      3. 联系厂商支持
      4. 启动灾备方案
```

## Output Validation

```yaml
validation:
  - 检查项: 备份完整性
    标准: 所有数据已备份，无遗漏

  - 检查项: 备份可恢复
    标准: 恢复测试成功

  - 检查项: 备份时间符合 RPO
    标准: 实际 RPO ≤ 目标 RPO

  - 检查项: 恢复时间符合 RTO
    标准: 实际 RTO ≤ 目标 RTO

  - 检查项: 监控告警配置
    标准: 备份失败可及时告警
```



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



## Handover 准备 (Handover Preparation)

```yaml
handover:
  artifacts:
    - name: 备份策略文档
      path: docs/backup-strategy.md
      description: 完整备份策略说明

    - name: 备份脚本
      path: scripts/backup/
      description: 备份和恢复脚本

    - name: 恢复手册
      path: docs/recovery-guide.md
      description: 详细恢复步骤

    - name: 监控配置
      path: docs/monitoring.md
      description: 监控和告警配置

  backup_summary:
    total_backups: 备份任务数
    daily_backup_size_gb: 日备份量
    weekly_backup_size_gb: 周备份量
    total_storage_tb: 总存储需求

  metrics:
    backup_success_rate: 备份成功率
    average_backup_time: 平均备份时间
    average_restore_time: 平均恢复时间

  next_phase:
    phase: monitor-operate
    entry_criteria: 备份系统就绪
    handover_data: 备份策略、恢复手册
```

## Example Output Structure

```yaml
backup_data_result:
  strategy:
    rpo_hours: 4
    rto_hours: 8
    backup_types:
      - type: "full"
        frequency: "weekly"
        time: "Sunday 02:00"
      - type: "incremental"
        frequency: "daily"
        time: "daily 02:00"

  resources:
    database_backups:
      - name: "user_db"
        size_gb: 500
        backup_method: "mysqldump"
      - name: "order_db"
        size_gb: 200
        backup_method: "xtrabackup"

    file_backups:
      - name: "uploads"
        size_gb: 1000
        path: "/data/uploads"

  storage:
    primary:
      location: "local-nas"
      capacity_tb: 10
      replication: "none"

    secondary:
      location: "oss"
      capacity_tb: 20
      replication: "cross-region"

  retention:
    daily: 7
    weekly: 4
    monthly: 12
    yearly: 7

  monitoring:
    backup_jobs: 10
    alerts:
      - name: "backup_failure"
        channels: ["email", "slack"]
      - name: "storage_threshold"
        threshold: "80%"

  last_restore_test:
    date: "2024-01-15"
    status: "success"
    duration_minutes: 45
```

## Execution Flow

> Step-by-step execution sequence for backup-data

### Phase 1: Analysis
- Understand requirements and context
- Identify constraints and dependencies

### Phase 2: Execution
- Perform core backup-data activities
- Apply best practices and standards

### Phase 3: Validation
- Verify outputs against acceptance criteria
- Ensure completeness and quality



## Error Handling (错误处理)

> **AI 遇到以下情况时必须按指定流程处理**

### 错误分类体系

| 级别 | 标识 | 描述 | 处理方式 |
|------|------|------|----------|
| P0 - Critical | ERR-CRITICAL | 阻塞性错误，无法继续 | 立即停止，升级人工处理 |
| P1 - Major | ERR-MAJOR | 严重错误，影响核心功能 | 尝试修复，失败则升级 |
| P2 - Minor | ERR-MINOR | 一般错误，可降级处理 | 记录并继续，后续修复 |
| P3 - Warning | ERR-WARNING | 警告信息，不影响执行 | 记录并继续 |

### Error Scenario 1: 通用错误处理

**识别信号**: 
- 检测到异常情况
- 验证失败

**处理流程**:
```
IF 检测到错误
THEN
  1. 识别错误类型和严重程度
  2. 记录错误详情
  3. 根据错误级别采取相应措施
  4. IF P0/P1 级别 THEN 升级到人工处理
  5. 更新状态并继续或停止
END
```

**降级方案**: 根据具体情况选择适当的降级策略

**升级条件**: P0 或 P1 级别错误

**错误日志格式**:
```yaml
error_log:
  error_id: "ERR-{timestamp}-XXX"
  timestamp: "{{ISO8601}}"
  level: "P0/P1/P2/P3"
  type: "{错误类型}"
  description: "{详细描述}"
  action_taken: "{已采取的行动}"
  result: "resolved/blocked/degraded/escalated"
```



## Output Format

```markdown
## Data Backup Deliverables

### Summary
- Status: [completed | partial | blocked]
- Completion: [percentage]

### Key Outputs
1. **Backup Scripts**: Automated backup scripts for all data sources
2. **Backup Schedule**: Cron/YAML scheduling configuration
3. **Restore Procedures**: Step-by-step data recovery operations manual
4. **Verification Report**: Backup integrity validation methodology
5. **Retention Policy**: Backup retention and cleanup strategy

### Validation Checklist
- [ ] Backup success rate is 99.5% or higher
- [ ] Recovery point objective (RPO) is consistently met
- [ ] Quarterly recovery drills pass validation checks
- [ ] All backup data is encrypted at rest and in transit

### Next Steps
- [ ] Schedule first recovery drill
- [ ] Monitor backup job success rates
```

