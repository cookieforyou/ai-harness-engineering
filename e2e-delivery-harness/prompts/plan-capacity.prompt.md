---
name: plan-capacity
description: "plan capacity execution prompt for E2E delivery workflow"
type: prompt
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['prompt', 'ai-execution']
---
# Capacity Planning Prompt

## Purpose

本提示词指导AI执行容量规划任务，基于当前容量数据、业务增长预测和峰值负载场景，制定科学合理的容量扩展方案，确保系统在高负载下的稳定性和成本效益。

### Key Objectives

- **准确评估现状**: 深入分析当前CPU/内存/存储/网络利用率，识别瓶颈资源
- **科学预测需求**: 基于历史趋势和业务增长，预测未来资源需求
- **制定扩展方案**: 设计垂直/水平/自动扩展策略，平衡性能和成本
- **确保安全余量**: 维护充足的缓冲容量应对突发流量
- **优化资源成本**: 在满足SLA的前提下最小化基础设施支出

## Input Variables (变量定义)

> **AI 在执行前必须确认以下变量已填充**，如未填充则请求用户提供

| Variable | Type | Required | Default | Description | Validation |
|----------|------|----------|---------|-------------|------------|
| `current_capacity` | object | true | - | 当前容量数据（cpu/mem/storage/network及其利用率） | 包含cpu、mem、storage、network的utilization和total |
| `growth_forecast` | object | true | - | 业务增长预测（月增长率、季度趋势、季节性峰值倍数） | 非空，monthly_growth_rate≥0 |
| `peak_load_scenarios` | array | true | - | 峰值负载场景列表 | 至少1个场景，包含time_range和load_multiplier |
| `budget_constraints` | object | false | {} | 预算约束（总预算、分期预算、审批要求） | total_budget≥0 |
| `scaling_strategy` | string | false | "auto" | 扩展策略（vertical/horizontal/auto） | 有效枚举值之一 |
| `time_horizon_months` | number | true | 12 | 规划时间周期（月） | 整数，范围1-60 |

### 示例: 变量的正确格式

```yaml
# 示例: 完整的容量规划输入
current_capacity:
  cpu:
    total_cores: 64
    utilization: 65
    unit: "%"
  memory:
    total_gb: 256
    utilization: 72
  storage:
    total_tb: 50
    utilization: 55
  network:
    total_mbps: 10000
    utilization: 40

growth_forecast:
  monthly_growth_rate: 5
  quarterly_trend: "increasing"
  seasonal_peak_multiplier: 2.5

peak_load_scenarios:
  - name: "双11大促"
    time_range: "2024-11-01~2024-11-15"
    load_multiplier: 3.0
    duration_hours: 48

budget_constraints:
  total_budget: 5000000
  currency: "CNY"
  quarterly_limit: 1500000

scaling_strategy: "auto"
time_horizon_months: 12
```

## Chain of Thought (思维链)

> **AI 必须按照以下思维链逐步执行**，每完成一步后进行自我验证

```
[THINK] Step 1: 理解容量规划目标和约束
   ├─ 输入: current_capacity, growth_forecast, time_horizon_months, budget_constraints
   ├─ 思考: 哪些是关键业务系统？关键资源瓶颈在哪？预算和时间约束是什么？
   ├─ 验证: 确认所有约束条件已识别，业务优先级明确
   └─ 输出: 容量规划任务分析摘要（含约束条件、风险提示、关键指标基线）
   ↓
[ANALYZE] Step 2: 分析当前容量利用率和瓶颈
   ├─ 输入: current_capacity, peak_load_scenarios
   ├─ 分析: 各资源利用率趋势、峰值时段分布、瓶颈资源识别
   ├─ 验证: 利用率数据与监控系统一致，瓶颈判断有数据支撑
   └─ 输出: 当前容量分析报告（含利用率热力图、瓶颈排名、趋势分析）
   ↓
[FORECAST] Step 3: 预测未来资源需求
   ├─ 输入: 容量分析报告, growth_forecast, peak_load_scenarios
   ├─ 预测: 基于增长率计算未来N月资源需求，模拟峰值场景下的资源需求
   ├─ 验证: 预测模型合理，考虑了季节性波动和突发增长（安全系数≥20%）
   └─ 输出: 资源需求预测报告（按月需求曲线、峰值需求、置信区间）
   ↓
[PLAN] Step 4: 制定容量扩展方案
   ├─ 输入: 资源需求预测, budget_constraints, scaling_strategy
   ├─ 规划: 设计扩展时间线、推荐扩展方式（垂直/水平/自动）、计算成本
   ├─ 验证: 方案在预算约束内，满足峰值负载需求，预留≥30%余量
   └─ 输出: 容量扩展方案（含时间线、资源清单、成本预算、ROI分析）
   ↓
[RECOMMEND] Step 5: 提出优化建议和风险提示
   ├─ 输入: 容量扩展方案
   ├─ 建议: 成本优化机会、性能调优建议、风险缓解措施、监控改进方案
   ├─ 验证: 建议可行且成本效益合理，风险已充分识别和分级
   └─ 输出: 优化建议清单（含优先级排序、预期效果、实施难度评估）
   ↓
[REVIEW] Step 6: 综合评审容量规划方案
   ├─ 输入: 所有上述输出
   ├─ 评审: KPI达标检查、方案可行性审核、风险再评估、替代方案比较
   ├─ 验证: FORECAST-ACCURACY≥85%, HEADROOM-MAINTAIN≥30%, COST-ACCURACY偏差≤15%, UTILIZATION-TARGET≥60%
   └─ 输出: 容量规划最终报告（含KPI评分、评审结论、待确认事项）
```

## Error Handling (错误处理)

> **AI 在执行过程中遇到以下情况时的处理策略**

### Error Scenario 1: 历史数据不足或不准确

**识别信号**: 
- 可用历史数据少于3个月
- 数据存在明显缺失或异常值
- 业务增长模式发生根本性变化

**处理流程**:
```
IF 历史数据不足以建立可靠预测
THEN
  1. 评估数据缺失程度和影响范围
  2. 采用行业基准数据作为补充（标注数据来源和置信度）
  3. 增加安全系数至40%（默认20%）
  4. 标注预测为"低置信度"并在输出中突出显示
  5. IF 核心业务系统 THEN 升级到技术负责人确认预测方案
  6. 建议建立完整的数据采集体系
END
```

**降级方案**: 基于行业基准做出保守估计，增加安全余量，建议短期验证后调整

**升级条件**: 核心系统无可用数据、或预测置信度<50%

---

### Error Scenario 2: 预算不足以满足需求

**识别信号**: 
- 扩展方案总成本超出预算上限
- 分阶段预算无法覆盖关键节点
- 最优方案成本超过可用预算120%

**处理流程**:
```
IF 预算不足以满足推荐的容量扩展方案
THEN
  1. 计算资金缺口和优先级排序
  2. 设计降级方案（分阶段实施、优先关键资源、使用预留实例）
  3. 评估降级方案的风险和容量缺口
  4. IF 降级方案仍无法满足核心需求 THEN
       a. 提供详细的成本效益分析报告
       b. 建议调整预算分配或申请额外预算
       c. 标记为 [预算不足-需审批] 并突出风险
     END
  5. 提供至少2个替代方案供决策参考
END
```

**降级方案**: 分阶段实施，优先保障核心资源和峰值场景，标注风险和限制条件

**升级条件**: 核心系统容量无法满足近期峰值需求、或降级方案风险为高

---

### Error Scenario 3: 峰值负载预测超出技术上限

**识别信号**: 
- 预测的峰值负载超过现有架构最大扩展能力
- 单一资源扩展无法满足需求
- 需要架构级变更才能满足需求

**处理流程**:
```
IF 峰值负载超出当前架构技术上限
THEN
  1. 量化需求差距（当前上限 vs 峰值需求）
  2. 评估架构扩展选项（分库分表、微服务拆分、异地多活）
  3. 提供架构升级方案及实施路线图
  4. 评估临时缓解措施（限流降级、优先级队列、缓存优化）
  5. IF 架构变更不可行 THEN
       a. 提供容量受限下的业务降级建议
       b. 明确标注容量限制和业务影响
       c. 升级到架构师团队决策
     END
  6. 更新容量模型，纳入架构级扩展能力
END
```

**降级方案**: 实施临时限流和降级策略，确保核心功能可用，标注架构升级需求

**升级条件**: 峰值负载超过当前架构上限200%，或影响核心业务SLA

---

### Error Scenario 4: 扩展方案成本效益不合理

**识别信号**: 
- 扩展方案ROI低于预期（<15%）
- 存在明显更优的替代方案
- 扩展后资源利用率预期<30%

**处理流程**:
```
IF 扩展方案成本效益不达标
THEN
  1. 重新评估需求预测的准确性
  2. 检查是否有更优的资源配置方案
  3. 考虑使用弹性/按需资源替代预留资源
  4. 评估使用缓存、CDN、压缩等技术优化资源使用效率
  5. IF 仍无法改善 THEN
       a. 记录成本效益分析和替代方案评估
       b. 标注为 [成本效益低-需评审]
       c. 在输出中明确说明原因和建议
     END
  6. 提供优化后的资源配置方案
END
```

**降级方案**: 采用混合策略（预留+按需），优化资源使用效率，减少预留容量

**升级条件**: ROI<5%或存在更优替代方案未被采纳

## Output Format (输出格式)

> AI必须按照以下结构生成容量规划交付物

```markdown
# Capacity Planning Deliverables

## 1. Task Information
- **Task ID**: {task_id}
- **Planning Period**: {time_horizon_months} months
- **Planner**: {agent_name}
- **Completion Date**: {current_date}
- **Status**: Completed / Partial / Blocked

## 2. Current Capacity Analysis

### 2.1 Resource Utilization Summary
| Resource | Total Capacity | Current Usage | Utilization % | Trend | Bottleneck |
|----------|---------------|---------------|---------------|-------|------------|
| CPU | {total_cores} cores | {used_cores} | {N}% | ↑/→/↓ | Yes/No |
| Memory | {total_gb} GB | {used_gb} | {N}% | ↑/→/↓ | Yes/No |
| Storage | {total_tb} TB | {used_tb} | {N}% | ↑/→/↓ | Yes/No |
| Network | {total_mbps} Mbps | {used_mbps} | {N}% | ↑/→/↓ | Yes/No |

### 2.2 Bottleneck Analysis
| Rank | Resource | Current Utilization | Critical Threshold | Risk Level | Impact Description |
|------|----------|-------------------|-------------------|------------|-------------------|
| 1 | {resource} | {N}% | {N}% | High/Medium/Low | {description} |

## 3. Demand Forecast

### 3.1 Monthly Resource Projection
| Month | CPU Required | Memory Required | Storage Required | Network Required | Confidence |
|-------|-------------|-----------------|-----------------|-----------------|------------|
| M+1 | {N} cores | {N} GB | {N} TB | {N} Mbps | High/Medium/Low |
| M+2 | {N} cores | {N} GB | {N} TB | {N} Mbps | High/Medium/Low |

### 3.2 Peak Load Scenario Simulation
| Scenario | Load Multiplier | CPU Peak | Memory Peak | Storage Peak | Network Peak | Duration |
|----------|----------------|----------|-------------|-------------|--------------|----------|
| {name} | {N}x | {N}% | {N}% | {N}% | {N}% | {N}h |

## 4. Capacity Expansion Plan

### 4.1 Recommended Actions
| Phase | Time | Action | Resource Type | Quantity | Est. Cost | Priority |
|-------|------|--------|--------------|----------|-----------|----------|
| Phase 1 | {date} | {action} | {type} | {N} | ${N} | P0/P1/P2 |

### 4.2 Scaling Strategy
- **Strategy**: Vertical / Horizontal / Auto-scaling
- **Trigger Conditions**: {conditions}
- **Cool-down Period**: {N} minutes
- **Max Scale-out Limit**: {N} instances

### 4.3 Cost Projection
| Category | Current Cost | Projected Cost | Increase % | Notes |
|----------|-------------|----------------|------------|-------|
| Compute | ${N}/月 | ${N}/月 | {N}% | {notes} |
| Storage | ${N}/月 | ${N}/月 | {N}% | {notes} |
| Network | ${N}/月 | ${N}/月 | {N}% | {notes} |
| **Total** | **${N}/月** | **${N}/月** | **{N}%** | |

## 5. Headroom Analysis

| Resource | Projected Peak | Planned Capacity | Headroom % | Meets Target(≥30%) |
|----------|---------------|-----------------|------------|--------------------|
| CPU | {N}% | {N}% | {N}% | ✅/❌ |
| Memory | {N}% | {N}% | {N}% | ✅/❌ |

## 6. Recommendations

### 6.1 Optimization Opportunities
| ID | Recommendation | Expected Benefit | Effort | Priority |
|----|---------------|-----------------|--------|----------|
| OPT-001 | {rec} | {benefit} | H/M/L | P0/P1/P2 |

### 6.2 Risks and Mitigation
| Risk ID | Description | Probability | Impact | Mitigation |
|---------|-------------|-------------|--------|------------|
| RISK-001 | {desc} | L/M/H | L/M/H | {mitigation} |

## 7. Quality Score

- **Overall Score**: {score}/100
- **Grade**: Excellent (≥95) / Good (≥85) / Satisfactory (≥70) / Needs Improvement (<70)
- **KPI Breakdown**:
  - FORECAST-ACCURACY: {value}% (target: ≥85%) - {pass/fail} (weight: 30%)
  - HEADROOM-MAINTAIN: {value}% (target: ≥30%) - {pass/fail} (weight: 30%)
  - COST-ACCURACY: {value}% deviation (target: ≤15%) - {pass/fail} (weight: 20%)
  - UTILIZATION-TARGET: {value}% (target: ≥60%) - {pass/fail} (weight: 20%)
```

## Output Validation (输出验证)

> **重要**: 在提交容量规划报告前，必须完成以下验证步骤

### Validation Checklist

**V-001: Forecast Accuracy Validation (预测准确性验证)**
- [ ] 预测模型基于足够的历史数据（≥3个月）
- [ ] 增长率计算考虑了季节性波动
- [ ] 峰值场景模拟覆盖所有已知的业务高峰期
- [ ] 预测结果在合理置信区间内（±15%）
- [ ] 敏感度分析已执行（乐观/基准/悲观场景）

**V-002: Headroom Validation (容量余量验证)**
- [ ] 所有资源至少保留30%缓冲容量
- [ ] 峰值负载下仍有≥20%余量
- [ ] 扩展方案考虑了预留资源到位时间
- [ ] 紧急扩容通道已建立（48小时内可到位）

**V-003: Cost Validation (成本验证)**
- [ ] 总成本在预算约束内
- [ ] 成本估算基于当前供应商报价
- [ ] 预留实例/按需实例比例合理
- [ ] 成本效益分析（ROI）已完成

**V-004: Plan Feasibility Validation (方案可行性验证)**
- [ ] 扩展方案在技术上是可行的
- [ ] 资源和人员的可用性已确认
- [ ] 实施时间线合理，不影响业务连续性
- [ ] 依赖的外部系统和服务已确认

**V-005: Compliance Validation (合规验证)**
- [ ] 方案符合公司IT架构标准
- [ ] 数据驻留和隐私要求已满足
- [ ] 安全和访问控制要求已考虑
- [ ] 审计和合规要求已满足

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
| KPI-001 | FORECAST-ACCURACY | ≥85% | (1 - |实际值-预测值|/实际值) × 100% | 回测验证预测误差 | 30% |
| KPI-002 | HEADROOM-MAINTAIN | ≥30% | (可用容量-峰值需求)/峰值需求 × 100% | 检查各资源余量 | 30% |
| KPI-003 | COST-ACCURACY | 偏差≤15% | |估算成本-实际成本|/实际成本 × 100% | 对比历史采购数据 | 20% |
| KPI-004 | UTILIZATION-TARGET | ≥60% | (实际使用量/总容量) × 100% | 检查扩展后目标利用率 | 20% |

**综合评分计算**:
```
Quality Score = FORECAST-ACCURACYScore × 30% + HEADROOM-MAINTAINScore × 30% + COST-ACCURACYScore × 20% + UTILIZATION-TARGETScore × 20%

各指标得分 = (实际值 / 目标值) × 100, 最高100分
合格: ≥70分 | 优秀: ≥85分 | 卓越: ≥95分
```

## Handover Context (交接上下文)

> 完成容量规划后，生成以下交接信息给审批和实施阶段

```yaml
handover:
  header:
    from_stage: "capacity_planning"
    to_stage: "approval_and_procurement"
    handover_id: "HO-{{timestamp}}-{{sequence}}"
    timestamp: "{{ISO8601}}"
    prepared_by: "{{agent.name}}"

  summary:
    status: "completed/partial/blocked"
    planning_period_months: {{time_horizon_months}}
    total_expansion_cost: {{number}}
    monthly_cost_increase: {{percentage}}%
    critical_bottlenecks_count: {{number}}

  artifacts:
    delivered:
      - name: "Capacity Planning Report"
        path: "reports/capacity-plan.md"
        version: "1.0.0"
      - name: "Demand Forecast Data"
        path: "data/demand-forecast.csv"
        version: "1.0.0"
      - name: "Resource Requirement Plan"
        path: "plans/resource-plan.xlsx"
        version: "1.0.0"

  metrics:
    forecast_accuracy: {{percentage}}%
    headroom_maintained: {{percentage}}%
    cost_accuracy: {{percentage}}%
    utilization_target: {{percentage}}%
    overall_score: {{score}}/100

  decisions:
    - id: "DC-001"
      description: "Scaling strategy selection"
      rationale: "Chose hybrid approach for better cost efficiency"
      alternatives_considered: ["Pure vertical", "Pure horizontal", "Auto-scaling only"]
      impact: "Affects infrastructure cost and operational complexity"

  open_issues:
    blocking: []
    non_blocking:
      - id: "ISSUE-001"
        description: "Storage forecast has lower confidence due to short history"
        risk_level: "low"
        planned_resolution: "Re-forecast after 3 months additional data"
        owner: "Capacity Planner"

  risks:
    - id: "RISK-001"
      description: "Peak load may exceed forecast if business growth accelerates"
      probability: "low"
      impact: "high"
      mitigation: "Include 30% safety buffer; establish emergency procurement channel"
      contingency_plan: "Activate auto-scaling with higher max limits"

  recommendations:
    - "Establish continuous capacity monitoring with threshold alerts at 70%"
    - "Review and adjust forecast quarterly based on actual business data"
    - "Evaluate reserved instance commitments for baseline capacity"
    - "Implement auto-scaling for unexpected traffic spikes"

  next_steps_for_approval:
    - "Review and approve capacity expansion budget"
    - "Initiate procurement process for Phase 1 resources"
    - "Schedule infrastructure upgrade window"

  quality_metrics:
    kpi_results:
      - kpi_id: "KPI-001"
        name: "FORECAST-ACCURACY"
        value: 90
        target: 85
        unit: "%"
        status: "pass"
        weight: 30
      - kpi_id: "KPI-002"
        name: "HEADROOM-MAINTAIN"
        value: 35
        target: 30
        unit: "%"
        status: "pass"
        weight: 30
      - kpi_id: "KPI-003"
        name: "COST-ACCURACY"
        value: 8
        target: 15
        unit: "% deviation"
        status: "pass"
        weight: 20
      - kpi_id: "KPI-004"
        name: "UTILIZATION-TARGET"
        value: 65
        target: 60
        unit: "%"
        status: "pass"
        weight: 20
    overall_score: 92
    grade: "excellent"

## Related Assets (关联资产)

| Asset Type | Path | Description |
|------------|------|-------------|
| Agent | `../agents/plan-capacity.agent.md` | 容量规划Agent角色 |
| Instruction | `../instructions/plan-capacity.instructions.md` | 容量规划技术指令 |

## Related Resources (相关资源)

- **Standards**: 
  - [Capacity Planning Standards](../standards/capacity-planning-standards.md) - 容量规划标准
  - [Cost Optimization Guidelines](../standards/cost-optimization-guidelines.md) - 成本优化指南
- **Evaluations**: 
  - [Capacity Plan Review](../evaluations/capacity-plan-review.md) - 容量计划评审
