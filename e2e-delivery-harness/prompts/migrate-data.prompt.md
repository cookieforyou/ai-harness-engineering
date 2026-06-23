---
name: migrate-data
description: "migrate data execution prompt for E2E delivery workflow"
type: prompt
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-23
status: active
tags: ['prompt', 'ai-execution']
---
# Prompt: 数据迁移场景执行 Prompt

## Overview

本 Prompt 用于指导 AI Agent 执行数据迁移流程，包括迁移评估、方案设计、迁移执行和数据验证。遵循零数据丢失、可回滚、可审计的原则，在预定时间窗口内安全高效地完成数据迁移。

## Input Variables

| 变量名 | 类型 | 必填 | 描述 | 示例 | 校验规则 |
|--------|------|------|------|------|----------|
| `source_system` | `SourceSystem` | 是 | 源系统信息 | `{"type": "mysql", "version": "5.7", "host": "10.0.1.1"}` | type 必须为支持的数据库类型 |
| `target_system` | `TargetSystem` | 是 | 目标系统信息 | `{"type": "tidb", "version": "6.0", "host": "10.0.2.1"}` | type 必须为支持的数据库类型 |
| `migration_scope` | `MigrationScope` | 是 | 迁移范围 | 见 MigrationScope 结构 | 至少包含一个表 |
| `data_volume` | `DataVolume` | 是 | 数据量评估 | 见 DataVolume 结构 | 预估数据总量 > 0 |
| `migration_window` | datetime | 是 | 迁移时间窗口 | "2024-01-15 02:00" | 符合 ISO8601 格式 |
| `allowed_downtime` | number | 是 | 允许停机时间(小时) | 4 | 必须 > 0 |
| `migration_strategy` | enum | 是 | 迁移策略 | "PHASE" | BIG_BANG / PARALLEL / PHASE / CDC |
| `transformation_rules` | string | 否 | 数据转换规则 | "email: LOWER()" | SQL 表达式或脚本 |
| `rollback_strategy` | enum | 否 | 回滚策略 | "snapshot" | snapshot / dml-reverse / parallel-run |
| `consistency_level` | enum | 否 | 一致性级别 | "strong" | strong / eventual |
| `notification_channels` | array | 否 | 通知渠道 | ["slack", "email"] | 至少一个渠道 |

### 数据结构定义

```typescript
interface SourceSystem {
  type: "mysql" | "postgresql" | "mongodb" | "oracle" | "sqlserver";
  version: string;
  host: string;
  port: number;
  database: string;
  username: string;
  connection_string: string;
}

interface TargetSystem {
  type: "mysql" | "postgresql" | "mongodb" | "tidb" | "clickhouse";
  version: string;
  host: string;
  port: number;
  database: string;
  username: string;
  connection_string: string;
}

interface MigrationScope {
  tables: string[];              // 迁移表列表
  records_estimate: number;       // 预估记录数
  total_size_gb: number;         // 总数据大小(GB)
  dependencies: string[];         // 依赖关系（表间外键依赖）
  critical_data: string[];        // 关键数据表（需优先验证）
  exclude_tables: string[];       // 排除表列表
  where_clauses: Record<string, string>;  // 每张表的过滤条件
}

interface DataVolume {
  tables: {
    name: string;
    rows: number;
    size_mb: number;
    growth_rate: number;          // 月增长率 %
    has_blob: boolean;            // 是否含大字段
    primary_key: string;          // 主键字段
    partition_key: string;        // 分区键（如有）
  }[];
  total_rows: number;
  total_size_gb: number;
  estimated_transfer_time: number; // 预估迁移时间（分钟）
  peak_transfer_rate: number;      // 峰值传输速率（MB/s）
}

interface ErrorThreshold {
  max_error_rate: number;               // 最大错误率（如 0.001 = 0.1%）
  max_inconsistency_rate: number;       // 最大不一致率
  max_duration_minutes: number;         // 最大执行时间（分钟）
  on_threshold_breach: "pause" | "rollback" | "continue";
}
```

## Chain of Thought (详细思维链)

> **AI 必须按照以下思维链逐步执行**，每完成一步后进行自我验证

```
[THINK] Step 1: 迁移评估 — 理解源系统和目标系统
   ├─ 分析: 源数据库类型、版本、架构（单机/主从/集群）
   ├─ 分析: 目标数据库类型、版本、存储引擎、字符集
   ├─ 分析: Schema 映射关系、数据类型兼容性
   ├─ 分析: 数据量、增长趋势、大表识别
   ├─ 分析: 依赖关系（外键、引用、下游系统）
   ├─ 验证: 评估结果与输入一致，无遗漏
   └─ 输出: 迁移评估报告
   ↓

[ANALYZE] Step 2: 方案设计 — 选择迁移策略和设计流程
   ├─ 选择: 迁移策略（BIG_BANG / PARALLEL / PHASE / CDC）
   ├─ 设计: 数据抽取方式（全量/增量/CDC）
   ├─ 设计: 数据转换映射规则
   ├─ 设计: 分批策略和并行度
   ├─ 设计: 回滚方案和回滚触发条件
   ├─ 验证: 方案满足停机窗口和一致性要求
   └─ 输出: 迁移方案设计文档
   ↓

[PREPARE] Step 3: 预迁移检查 — 确认环境和数据就绪
   ├─ 检查: 源数据质量（空值、重复、异常值）
   ├─ 检查: 目标环境就绪（权限、存储、网络）
   ├─ 检查: 回滚方案可行性（演练验证）
   ├─ 配置: 监控指标和告警阈值
   ├─ 配置: 日志记录和审计追踪
   ├─ 验证: 所有前置条件满足
   └─ 输出: 预检查清单 + 回滚方案
   ↓

[EXECUTE] Step 4: 迁移执行 — 按方案执行数据迁移
   ├─ 执行: 创建目标表结构（DDL）
   ├─ 执行: 关闭外键检查和约束
   ├─ 执行: 分批抽取源数据并加载到目标
   ├─ 监控: 实时监控进度、性能、错误率
   ├─ 监控: 比对实际速度与预估速度
   ├─ 处理: 异常时按预设策略处理
   ├─ 验证: 每批完成后校验数据
   └─ 输出: 迁移执行日志 + 进度报告
   ↓

[VALIDATE] Step 5: 数据验证 — 多维度校验数据完整性
   ├─ 校验: 行数一致性（逐表对比 COUNT）
   ├─ 校验: 校验和一致性（逐表计算 CHECKSUM）
   ├─ 校验: 抽样数据逐行对比（关键字段）
   ├─ 校验: 业务规则验证（参照完整性、业务逻辑）
   ├─ 校验: 性能验证（查询响应时间）
   ├─ 验证: 所有 KPI 达标
   └─ 输出: 数据验证报告
   ↓

[HANDOVER] Step 6: 割接与交接
   ├─ 执行: 割接切换（DNS/连接串切换）
   ├─ 验证: 业务功能验证
   ├─ 生成: Handover Context YAML
   ├─ 更新: 监控配置和告警规则
   └─ 通知: 下一阶段 Agent（monitor-operate）
```

## Error Scenarios

### ES-1: 数据不一致（Data Inconsistency）

**识别信号**:
- `SELECT COUNT(*)` 源和目标不一致
- `CHECKSUM` 比对不匹配
- 抽样数据逐字段对比有差异

**处理流程**:
```
IF 校验发现数据不一致
THEN
  1. 记录不一致的表和字段详情
  2. 分析不一致原因（数据类型截断/时区差异/编码问题）
  3. IF 不一致率 ≤ threshold
     THEN 修复特定记录并重新校验
     ELSE 触发回滚流程
  4. 更新验证报告
END
```

**升级条件**: 不一致率 > 0.1% 或关键数据表不一致

---

### ES-2: 迁移超时（Migration Timeout）

**识别信号**:
- 迁移执行时间接近或超过迁移窗口
- 预估剩余时间超过窗口余量

**处理流程**:
```
IF 迁移时间可能超出窗口
THEN
  1. 检查当前进度和剩余数据量
  2. 评估可加速方案（增加并行度/减少校验）
  3. IF 可在窗口内完成
     THEN 优化参数继续执行
     ELSE 评估回滚或延期方案
  4. 通知相关方
END
```

**升级条件**: 剩余时间 > 窗口余量 30%

---

### ES-3: 回滚触发（Rollback Required）

**识别信号**:
- 数据不一致率超过阈值
- 目标数据库不可用
- 业务发现迁移数据错误

**处理流程**:
```
IF 需要回滚
THEN
  1. 停止迁移任务
  2. 评估回滚范围（全量回滚/部分回滚）
  3. 执行回滚脚本
  4. 验证源系统数据完整
  5. 恢复业务流量到源系统
  6. 记录回滚原因和影响
END
```

**升级条件**: 任何 P0/P1 级别错误

---

### ES-4: 性能瓶颈（Performance Bottleneck）

**识别信号**:
- 传输速率低于预期 50%
- 目标端写入延迟超过 1 秒
- 源系统 CPU/IO 使用率 > 80%

**处理流程**:
```
IF 性能低于阈值
THEN
  1. 检查网络带宽和延迟
  2. 检查源和目标系统负载
  3. 调整批处理大小（如 1000→5000）
  4. 调整并行线程数
  5. 监控调整后效果
END
```

## Output Format

### 迁移计划输出模板

```markdown
## Data Migration Plan

### 1. 迁移概述
- 源系统: {{source_system.type}} {{source_system.version}}
- 目标系统: {{target_system.type}} {{target_system.version}}
- 迁移策略: {{migration_strategy}}
- 迁移窗口: {{migration_window}} ({{allowed_downtime}}小时)
- 数据总量: {{data_volume.total_size_gb}} GB / {{data_volume.total_rows}} 行

### 2. 迁移步骤时间线
| 步骤 | 操作 | 预计耗时 | 可回滚 | 校验方法 |
|------|------|----------|--------|----------|
| 1 | Schema 创建 | 5 min | 是 | DDL 执行结果 |
| 2 | 表 A 迁移 | N min | 是 | 行数+校验和 |
| 3 | 表 B 迁移 | N min | 是 | 行数+校验和 |
| ... | ... | ... | ... | ... |
| N | 业务验证 | 30 min | N/A | 功能测试 |

### 3. 风险分析
| 风险 | 概率 | 影响 | 缓解措施 |
|------|------|------|----------|
| 网络中断 | 低 | 高 | 断点续传 |
| 数据不一致 | 中 | 高 | 全量校验+修复脚本 |
| 超时 | 中 | 中 | 并行加速/请求延期 |

### 4. 回滚方案
- 回滚策略: {{rollback_strategy}}
- 回滚耗时: 预估 {{X}} 分钟
- 回滚验证: 恢复后校验源数据完整性
```

### 执行日志模板

```yaml
migration_execution_log:
  session_id: "MIG-{{timestamp}}-{{sequence}}"
  start_time: "{{ISO8601}}"
  end_time: "{{ISO8601}}"
  migration_strategy: "{{strategy}}"

  steps:
    - step_id: 1
      name: "table_users_migration"
      start_time: "{{ISO8601}}"
      end_time: "{{ISO8601}}"
      rows_processed: 500000
      size_mb: 2048
      throughput_mbps: 85
      status: "completed"
      errors: []
      validation:
        source_count: 500000
        target_count: 500000
        checksum_match: true

    - step_id: 2
      name: "table_orders_migration"
      start_time: "{{ISO8601}}"
      end_time: "{{ISO8601}}"
      rows_processed: 1200000
      size_mb: 5120
      throughput_mbps: 72
      status: "completed"
      errors:
        - type: "retryable"
          count: 5
          resolved: true
      validation:
        source_count: 1200000
        target_count: 1200000
        checksum_match: true

  summary:
    total_tables: 10
    tables_completed: 10
    tables_failed: 0
    total_rows: 5000000
    total_size_gb: 200
    total_duration_minutes: 180
    avg_throughput_mbps: 78
    error_rate: 0.0001
    status: "completed"
```

### 验证报告模板

```markdown
## Data Validation Report

### 整体结果
- **验证状态**: {{PASS / FAIL}}
- **DATA-INTEGRITY**: {{percentage}}%（目标: 100%）
- **CHECKSUM-MATCH**: {{percentage}}%（目标: 100%）
- **MIGRATION-DURATION**: {{actual}} / {{budget}} 分钟

### 逐表校验结果
| 表名 | 源行数 | 目标行数 | 行数一致 | 校验和匹配 | 抽样一致 | 状态 |
|------|--------|----------|----------|------------|----------|------|
| users | 500,000 | 500,000 | PASS | PASS | 100% | OK |
| orders | 1,200,000 | 1,200,000 | PASS | PASS | 100% | OK |
| ... | ... | ... | ... | ... | ... | ... |

### 差异详情
{{如果有差异，详细列出}}

### 修复建议
{{如果存在不一致，提供修复方案}}
```

## Handover 准备

```yaml
handover_to_monitor:
  deliverable: "数据迁移报告"
  version: "1.0"
  status: "成功/失败/部分成功"

  summary:
    source_system: "{{source}}"
    target_system: "{{target}}"
    tables_migrated: N
    records_migrated: N
    total_size_gb: {{size}}
    duration_minutes: {{minutes}}
    success_rate: "{{percentage}}"

  quality_metrics:
    data_integrity: "100%"
    checksum_match: "100%"
    rollback_ready: "yes"
    within_window: "yes"

  validation:
    completeness: PASS/FAIL
    accuracy: PASS/FAIL
    integrity: PASS/FAIL

  monitoring:
    target_db_connections: {{count}}
    target_db_queries_per_sec: {{qps}}
    target_db_error_rate: "0%"
    dashboard_url: "{{Grafana URL}}"

  open_issues:
    blocking: []
    non_blocking:
      - "{{issue_description}}"

  next_steps:
    - "Notify downstream ETL pipelines of migration completion"
    - "Monitor target database for first 24 hours"
    - "Schedule source system decommission after 30 days"
```

## Constraints

1. **零丢失**: 关键数据不能丢失，DATA-INTEGRITY 必须达到 100%
2. **可回滚**: 必须有回滚方案并在执行前验证
3. **可追溯**: 迁移过程必须完整记录日志，支持审计
4. **时间窗口**: 迁移必须在预定时间窗口内完成
5. **幂等性**: 迁移脚本必须支持重复执行
