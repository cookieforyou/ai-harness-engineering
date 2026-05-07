---
name: performance-testing
description: "performance testing execution prompt for E2E delivery workflow"
type: execution
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['prompt', 'ai-execution']
---
# Prompt: 性能测试场景执行 Prompt

## Overview

本 Prompt 用于指导 AI Agent 执行性能测试流程，包括性能需求分析、测试计划制定、测试执行和结果分析。

## Input Variables

| 变量名 | 类型 | 必填 | 描述 | 示例 |
|--------|------|------|------|------|
| `system_name` | string | 是 | 系统名称 | "订单管理系统" |
| `system_version` | string | 是 | 测试版本 | "v2.1.0" |
| `performance_requirements` | object | 是 | 性能需求 | 见 PerformanceRequirements 结构 |
| `test_environment` | object | 是 | 测试环境 | 见 TestEnvironment 结构 |
| `business_scenarios` | string[] | 是 | 关键业务场景 | ["下单", "支付", "查询"] |
| `test_tool` | string | 是 | 测试工具 | "JMeter/Locust/k6" |
| `concurrent_users` | number | 是 | 目标并发用户数 | 1000 |
| `test_duration` | number | 是 | 测试持续时间(分钟) | 30 |
| `ramp_up_time` | number | 否 | 预热时间(秒) | 60 |
| `think_time` | number | 否 | 思考时间(秒) | 3 |
| `test_data_volume` | number | 是 | 测试数据量 | 100000 |
| `sla_targets` | object | 是 | SLA 目标 | 见 SLATargets 结构 |

### PerformanceRequirements 结构

```typescript
interface PerformanceRequirements {
  response_time: {
    p50_target: number;       // P50 响应时间目标 (ms)
    p95_target: number;       // P95 响应时间目标 (ms)
    p99_target: number;       // P99 响应时间目标 (ms)
    max_target: number;       // 最大响应时间目标 (ms)
  };
  throughput: {
    tps_target: number;       // TPS 目标
    qps_target: number;       // QPS 目标
  };
  reliability: {
    error_rate_max: number;   // 最大错误率 (%)
    availability_target: number; // 可用性目标 (%)
  };
  scalability: {
    capacity_plan: boolean;   // 是否需要容量规划
    growth_factor: number;   // 预估增长系数
  };
}
```

### TestEnvironment 结构

```typescript
interface TestEnvironment {
  environment_type: 'DEV' | 'STAGING' | 'PROD_LIKE';
  server_config: {
    app_servers: number;      // 应用服务器数量
    db_server: string;        // 数据库配置
    cache_server: string;     // 缓存配置
  };
  network: {
    bandwidth: string;        // 带宽
    latency: number;         // 网络延迟 (ms)
  };
  monitoring: string[];      // 监控工具列表
}
```

### SLATargets 结构

```typescript
interface SLATargets {
  page_load_time: number;    // 页面加载时间 (s)
  api_response_time: number; // API 响应时间 (ms)
  success_rate: number;       // 成功率 (%)
  concurrent_users: number;   // 支持并发用户数
}
```

## Chain of Thought

```
1. [THINK] 理解系统 → 系统架构和技术栈是否清晰？
2. [THINK] 确认指标 → 性能指标是否与 SLA 对齐？
3. [THINK] 设计模型 → 测试模型是否能真实反映业务？
4. [THINK] 准备数据 → 测试数据是否充分且真实？
5. [EXECUTE] 执行测试 → 按计划执行并监控
6. [ANALYZE] 分析结果 → 定位瓶颈和分析原因
7. [VALIDATE] 验证达标 → 性能是否满足目标
8. [OUTPUT] 输出报告 → 完整报告和优化建议
```

## Error Handling

### 情况 1：性能指标不达标

```
IF 响应时间 > SLA 或 吞吐量 < 目标
THEN
  1. 记录未达标指标和偏差程度
  2. 分析未达标场景和时间点
  3. 检查资源使用情况 (CPU/Memory/IO/Network)
  4. 分析数据库慢查询和连接池
  5. 定位瓶颈组件
  6. 提出优化建议
END
```

### 情况 2：测试结果不稳定

```
IF 多次测试结果波动 > 20%
THEN
  1. 检查环境状态
  2. 排除干扰因素
  3. 增加预热时间
  4. 增加测试时长
  5. 使用更稳定的测试模式
END
```

### 情况 3：测试过程中出现错误

```
IF 错误率突然升高
THEN
  1. 检查服务日志
  2. 排查是否是测试数据问题
  3. 检查依赖服务状态
  4. 决定是继续还是暂停
END
```

### 情况 4：资源耗尽

```
IF CPU/Memory/Disk > 90%
THEN
  1. 立即记录资源状态
  2. 分析资源消耗来源
  3. 标记为 [资源瓶颈]
  4. 提出扩容建议
END
```

## Input Format

```markdown
## Input Information

### System Information
- 系统名称: {system_name}
- 版本: {system_version}
- 架构: {架构描述}

### 性能需求
- 响应时间目标: {响应时间目标}
- 吞吐量目标: {吞吐量目标}
- 并发用户: {concurrent_users}

### 业务场景
{业务场景列表}

### 测试环境
{环境配置}
```

## Task Steps

### Step 1: 性能需求分析

1. 分析业务场景优先级
2. 确定关键性能指标 (KPI)
3. 定义性能基线和目标
4. 识别性能测试类型

### Step 2: 性能测试计划

1. 选择性能测试类型
2. 设计测试场景
3. 制定测试脚本
4. 准备测试数据
5. 配置监控告警

### Step 3: 测试脚本开发

1. 录制/编写 API 请求
2. 配置并发模型
3. 设置思考时间
4. 添加断言验证
5. 脚本调试通过

### Step 4: 性能测试执行

1. 执行预热测试
2. 执行基准测试
3. 执行负载测试
4. 执行稳定性测试
5. 执行峰值测试
6. 全程监控记录

### Step 5: 结果分析

1. 收集测试数据
2. 分析性能指标
3. 定位性能瓶颈
4. 对比性能变化
5. 生成分析报告

### Step 6: 优化建议

1. 提出优化方案
2. 评估优化收益
3. 制定优化计划
4. 输出优化建议

## Output Validation

### 验证清单

```markdown
## Self-Validation Report

### V-001: 测试覆盖检查
- [ ] 关键业务场景全部覆盖
- [ ] 测试场景包含正常和异常情况
- [ ] 测试数据充分且真实

### V-002: 测试执行检查
- [ ] 测试按计划执行
- [ ] 监控数据完整
- [ ] 无异常中断

### V-003: 结果分析检查
- [ ] 数据分析准确
- [ ] 瓶颈定位清晰
- [ ] 结论有数据支撑

### V-004: 报告完整性检查
- [ ] 包含测试概述
- [ ] 包含测试结果
- [ ] 包含性能分析
- [ ] 包含优化建议

### 验证结果
- 验证通过: [是/否]
- 未通过的检查项: [列出]
```

### 验证失败时的处理

```
IF 验证未通过
THEN
  1. 识别未通过的验证项
  2. 补充缺失内容
  3. 重新执行验证
END
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



## Handover 准备

在完成验证后，生成以下交接信息：

```yaml
handoff_to_deployment:
  deliverable: "性能测试报告"
  version: "1.0"
  status: "通过/未通过/有条件通过"

  summary:
    test_scenarios: N              # 测试场景数
    total_users: N               # 总并发用户
    peak_tps: N                  # 峰值 TPS
    avg_response_time: ms        # 平均响应时间
    p99_response_time: ms       # P99 响应时间
    error_rate: percentage       # 错误率

  performance_status:
    response_time: "PASS/FAIL"  # 响应时间
    throughput: "PASS/FAIL"     # 吞吐量
    reliability: "PASS/FAIL"     # 可靠性
    overall: "PASS/FAIL"        # 总体

  bottlenecks:
    - component: "组件"
      issue: "问题"
      impact: "影响"
      suggestion: "建议"

  recommendations:
    - priority: "高/中/低"
      description: "建议"
      expected_benefit: "预期收益"

  open_issues:
    count: N
    blocking: [列表]
    non_blocking: [列表]
```

## Constraints

1. **真实模拟**: 测试场景必须真实反映业务场景
2. **数据充分**: 测试数据必须充分以反映真实负载
3. **监控完整**: 必须全程监控以便分析
4. **结论可靠**: 结论必须有数据支撑

## Task Description

> Describe the specific task for the performance-testing scenario execution.
> AI must understand the context, objectives, and success criteria before proceeding.

## Execution Flow

> Step-by-step execution sequence for performance-testing

### Phase 1: Analysis
- Understand requirements and context
- Identify constraints and dependencies

### Phase 2: Execution
- Perform core performance-testing activities
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
## Performance Testing Deliverables

### Summary
- Status: [completed | partial | blocked]
- Completion: [percentage]

### Key Outputs
1. **Test Plan**: Scenarios, load models, and acceptance criteria
2. **Test Scripts**: JMeter/k6/Locust performance test scripts
3. **Test Results**: Metrics, charts, and statistical analysis
4. **Bottleneck Analysis**: Root cause identification for each bottleneck
5. **Tuning Recommendations**: Prioritized optimization suggestions

### Validation Checklist
- [ ] SLO achievement rate is 99.5% or higher
- [ ] All known bottlenecks are identified and documented
- [ ] Test validity correlation is 95% or higher
- [ ] Results are reproducible across runs

### Next Steps
- [ ] Share results with engineering team
- [ ] Create optimization backlog items
```

