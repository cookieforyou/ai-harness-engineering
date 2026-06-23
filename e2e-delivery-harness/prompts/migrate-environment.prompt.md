---
name: migrate-environment
description: "migrate environment execution prompt for E2E delivery workflow"
type: prompt
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
language: "zh-CN"
tags: ['prompt', 'ai-execution']
---
# Prompt: 环境迁移 (Migrate Environment)

## Input Variables (变量定义)

| Variable | Type | Required | Description |
|----------|------|----------|-------------|
| `project_name` | string | true | 项目名称 |
| `source_environment` | string | true | 源环境 dev/staging/prod |
| `target_environment` | string | true | 目标环境 |
| `migration_type` | string | true | full/incremental/in-place/blue-green |
| `data_migration` | boolean | false | 是否迁移数据 |
| `config_migration` | boolean | false | 是否迁移配置 |
| `downtime_window` | string | false | 停机窗口 |
| `rollback_required` | boolean | true | 是否需要回滚预案 |

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
  source_environment: string    # 源环境：dev|staging|prod
  target_environment: string    # 目标环境：dev|staging|prod
  migration_type: string        # 迁移类型：full|incremental|in-place|blue-green
  data_migration: boolean       # 是否迁移数据
  config_migration: boolean      # 是否迁移配置
  downtime_window: string       # 停机窗口
  rollback_required: boolean     # 是否需要回滚
```

## Task Description

你是 **DevOps Engineer (运维工程师)**，负责环境迁移的规划、执行和验证。

## Chain of Thought

### 1. 分析迁移需求

```
步骤 1.1: 分析环境差异
- 基础设施差异
- 配置差异
- 数据差异

步骤 1.2: 评估迁移风险
- 数据丢失风险
- 服务中断风险
- 兼容性风险

步骤 1.3: 确定迁移策略
- 全量迁移
- 增量迁移
- 蓝绿部署
```

### 2. 制定迁移计划

```
步骤 2.1: 数据迁移计划
- 数据量评估
- 迁移时间估算
- 增量同步方案

步骤 2.2: 配置迁移计划
- 配置文件清单
- 环境变量映射
- 密钥迁移

步骤 2.3: 回滚方案
- 回滚触发条件
- 回滚步骤
- 验证方法
```

### 3. 执行迁移

```
步骤 3.1: 数据迁移
- 数据导出
- 数据传输
- 数据导入

步骤 3.2: 配置迁移
- 配置导出
- 配置适配
- 配置验证

步骤 3.3: 服务部署
- 服务部署
- 配置更新
- 服务启动
```

### 4. 验证迁移

```
步骤 4.1: 功能验证
- 健康检查
- 功能测试

步骤 4.2: 数据验证
- 数据完整性
- 数据一致性

步骤 4.3: 监控验证
- 监控指标
- 告警验证
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



## Handover Preparation (交接准备)

```yaml
handover:
  artifacts:
    - name: 迁移计划
      path: docs/migration/plan.md
    - name: 验证报告
      path: docs/migration/verification.md
    - name: 回滚手册
      path: docs/migration/rollback.md

  migration_summary:
    duration: 迁移耗时
    data_volume: 数据量
    status: 成功/失败
```

## Execution Flow

> Step-by-step execution sequence for migrate-environment

### Phase 1: Analysis
- Understand requirements and context
- Identify constraints and dependencies

### Phase 2: Execution
- Perform core migrate-environment activities
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




## Output Validation (输出验证)

> 生成最终交付物前必须完成。详见 [evaluations/output-validation-checklist.md](../evaluations/output-validation-checklist.md)。

### Mandatory Validation (V-*)

**V-001 Completeness**: 必填章节齐全；无 `{TODO}` / `[placeholder]`  
**V-002 Consistency**: 术语、数据、与上游 Handover 无矛盾  
**V-003 Accuracy**: 假设已标注；计算与引用正确  
**V-004 Quality**: Scenario KPI 达标（合格线通常 ≥70 分）

### Validation Failure Protocol

```
IF 任一 V-* 未通过
THEN 记录失败项 → P0/P1 必须修复后重验 → P2/P3 可记录 open_issues 并升级人工
```

### Self-Assessment

- Confidence: High | Medium | Low  
- Human Review Required: {列出需人工确认项}

## Output Format

```markdown
## Environment Migration Deliverables

### Summary
- Status: [completed | partial | blocked]
- Completion: [percentage]

### Key Outputs
1. **Migration Strategy**: Rehost/refactor/replace decision and rationale
2. **Cutover Plan**: Step-by-step switchover procedures
3. **Environment Mapping**: Source-to-target configuration mapping
4. **Validation Checklist**: Post-migration verification items
5. **Risk Mitigation**: Identified risks and mitigation measures

### Validation Checklist
- [ ] Migration success rate is 98% or higher
- [ ] New environment performance is 95%+ of original
- [ ] Environment cost is within 110% of original budget
- [ ] All applications pass functional validation

### Next Steps
- [ ] Execute cutover in maintenance window
- [ ] Decommission old environment after stability period
```

## 相关资产

- [harness-engineering.md](../standards/harness-engineering.md) — 六层驾驭模型对齐标准
- [id-generation-quantification.md](../standards/id-generation-quantification.md) — KPI量化体系与指标定义
- [output-quality-rubric.md](../standards/output-quality-rubric.md) — 输出质量评分与验证标准

