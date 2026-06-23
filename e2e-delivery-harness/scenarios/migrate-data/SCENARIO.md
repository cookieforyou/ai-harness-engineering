---
name: migrate-data
description: "Migrate Data scenario for the E2E delivery lifecycle"
type: scenario
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-23
status: active
tags: ['workflow', 'process']
---
# Migrate Data Scenario (数据迁移场景)

## Purpose

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

本场景用于指导 AI Agent 执行数据迁移工作，包括迁移方案设计、数据清洗转换、迁移执行验证和回滚方案准备。

### Think-Aloud Protocol

```
THINK: 理解源系统和目标系统
   ↓
THINK: 分析数据结构和迁移复杂度
   ↓
THINK: 设计迁移方案和策略
   ↓
THINK: 准备数据清洗和转换规则
   ↓
EXECUTE: 执行数据迁移
   ↓
VALIDATE: 验证数据完整性
   ↓
OUTPUT: 输出迁移报告
```

### Step-by-Step Reasoning

**Step 1: 迁移评估**
- 问：数据量和复杂度如何？
- 验证：评估准确性
- 检查：依赖关系完整

**Step 2: 方案设计**
- 问：迁移方案是否可行？
- 验证：风险可控
- 检查：回滚方案完备

**Step 3: 数据准备**
- 问：数据清洗是否完整？
- 验证：数据质量达标
- 检查：转换规则正确

**Step 4: 迁移执行**
- 问：迁移过程是否正常？
- 验证：进度符合预期
- 检查：无异常发生

**Step 5: 数据验证**
- 问：数据是否完整准确？
- 验证：校验通过
- 检查：业务功能正常

### EH-1: 数据不一致

- **识别信号**：校验发现数据不一致
- **处理方式**：
  1. 定位不一致数据
  2. 分析不一致原因
  3. 修复或重新迁移
  4. 重新校验
- **升级条件**：不一致率 > 阈值

### EH-2: 迁移超时

- **识别信号**：迁移任务超时
- **处理方式**：
  1. 检查任务状态
  2. 分析超时原因
  3. 决定继续或回滚
- **升级条件**：预估超时严重

### EH-3: 依赖失败

- **识别信号**：依赖服务不可用
- **处理方式**：
  1. 暂停迁移
  2. 等待依赖恢复
  3. 继续或回滚
- **升级条件**：依赖长时间不可用

## Decision Checkpoints

| ID | 决策点 | 触发条件 | 决策选项 | 选择标准 | 记录位置 |
|----|--------|----------|----------|----------|----------|
| DC-001 | 范围确认 | 执行启动前 | 继续 / 缩小范围 / 升级 | 与上游 Handover 一致 | 执行记录 |
| DC-002 | 质量门禁 | 产出验证前 | 修复后继续 / 记录 open_issues | Scenario KPI ≥70 | 验证报告 |
| DC-003 | 交接准出 | 阶段完成前 | 完成交接 / 部分交接 / 阻塞 | Handover 必填字段齐全 | Handover YAML |

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

## Quality Metrics

> Quality metrics for measuring scenario execution success.

| KPI | Target | Description | Verification Method |
|-----|--------|-------------|---------------------|
| `DATA-INTEGRITY` | 100% | 数据完整性：迁移前后数据一致性校验通过 | 全量数据逐行校验 + 业务抽样验证 |
| `ROLLBACK-READY` | 100% | 回滚就绪：迁移全程可回滚，回滚方案经过演练验证 | 回滚方案评审 + 演练测试报告 |
| `MIGRATION-DURATION` | Within window | 迁移在预定时间窗口内完成 | 计时监控 + 预警通知 |
| `DATA-VALIDATION` | 100% | 校验通过率：迁移后数据源与目标源校验一致 | 自动化校验脚本执行 |
| `CHECKSUM-MATCH` | 100% | 数据校验和匹配率 | 逐表或分片计算校验和比对 |
| `DOWNTIME` | ≤{{downtime_budget}} | 停机时间：在预算范围内 | 实时监控 + 停机计时器 |

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识

## Handover Criteria (交接标准)

| 条件项 | 状态 | 说明 |
|--------|------|------|
| 迁移方案 | ☐ | 已评审通过 |
| 回滚方案 | ☐ | 已测试验证 |
| 迁移脚本 | ☐ | 已测试通过 |
| 验证报告 | ☐ | 完整准确 |

## Prerequisites

- [ ] Prerequisite 1: Source and target schemas are documented and aligned
- [ ] Prerequisite 2: Data volume and transformation rules are analyzed
- [ ] Prerequisite 3: Rollback procedures are prepared and tested

### Handover Context Template

```yaml
handover:
  header:
    from_stage: "migrate-data"
    to_stage: "monitor-operate"
    handover_id: "HO-{{timestamp}}-{{sequence}}"
    timestamp: "{{ISO8601}}"
    prepared_by: "{{agent.name}}"
    
  summary:
    status: "completed/partial/blocked"
    completion_percentage: {{0-100}}
    quality_score: {{0-100}}
    
  artifacts:
    delivered:
      - name: "{{artifact_name}}"
        path: "{{file_path}}"
        version: "{{version}}"
        checksum: "{{SHA256}}"
      
  decisions:
    - id: "DC-XXX"
      description: "{{决策描述}}"
      rationale: "{{决策理由}}"
      alternatives_considered: ["选项1", "选项2"]
      
  open_issues:
    blocking: []
    non_blocking:
      - id: "ISSUE-XXX"
        description: "{{问题描述}}"
        
  risks:
    - id: "RISK-XXX"
      description: "{{风险描述}}"
      probability: "low/medium/high"
      impact: "low/medium/high"
      mitigation: "{{缓解措施}}"
      
  recommendations:
    - "{{建议1}}"
    - "{{建议2}}"
    
  quality_metrics:
    kpi_results:
      - kpi_id: "KPI-001"
        value: {{actual_value}}
        target: {{target_value}}
        status: "pass/fail"
```
