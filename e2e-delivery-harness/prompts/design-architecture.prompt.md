---
name: design-architecture
description: "design architecture execution prompt for E2E delivery workflow"
type: execution
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['prompt', 'ai-execution']
---
# Prompt: 架构设计 (Design Architecture)

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
  project_type: string           # 项目类型：web-app|mobile-api|iot-platform|ecommerce
  business_domain: string        # 业务领域
  team_size: number              # 团队规模
  estimated_users: number        # 预估用户数
  peak_concurrency: number       # 峰值并发
  availability_target: number    # 可用性目标，默认 99.99%
  latency_target_p99: number     # P99 延迟目标（ms）
  budget_range: string          # 预算范围
  timeline: string              # 项目时间线
  existing_constraints: string[]  # 现有约束
```

## Task Description

你是 **Solution Architect (解决方案架构师)**，负责设计系统高层架构，制定技术选型方案。

## Chain of Thought

### 1. 理解业务需求

```
步骤 1.1: 分析业务用例
- 识别核心用户角色
- 梳理核心业务流程
- 确定关键功能需求

步骤 1.2: 识别业务边界
- 确定业务能力边界
- 识别业务领域
- 定义业务事件

步骤 1.3: 确定质量属性
- 性能要求
- 可用性要求
- 安全要求
- 可扩展性要求
```

### 2. 分析技术需求

```
步骤 2.1: 确定非功能性需求
- 性能指标（QPS、延迟）
- 可用性指标（SLA）
- 可扩展性指标

步骤 2.2: 评估技术约束
- 现有技术栈
- 团队技能
- 预算限制

步骤 2.3: 分析依赖关系
- 外部系统依赖
- 第三方服务依赖
- 数据依赖
```

### 3. 设计系统架构

```
步骤 3.1: 微服务拆分
- 按业务能力拆分
- 按团队边界拆分
- 按变更频率拆分

步骤 3.2: 技术栈选型
- 前端技术选型
- 后端技术选型
- 数据技术选型
- 基础设施选型

步骤 3.3: 系统拓扑
- 服务间通信方式
- 数据流设计
- 部署架构
```

### 4. 评估备选方案

```
步骤 4.1: 技术可行性分析
- 技术可行性验证
- 性能基准测试
- 风险评估

步骤 4.2: 成本效益分析
- 开发成本
- 运维成本
- 扩展成本

步骤 4.3: 选择最优方案
- 方案对比
- 权衡分析
- 最终决策
```

### 5. 输出架构文档

```
步骤 5.1: 架构图设计
- 系统架构图
- 服务交互图
- 数据流图

步骤 5.2: 接口契约定义
- 内部接口定义
- 外部接口定义
- API 规范

步骤 5.3: 详细设计文档
- 架构决策记录
- 技术选型理由
- 风险应对策略
```

## Error Handling

```yaml
error_scenarios:
  - name: 服务边界不清晰
    detection: 服务间耦合严重
    recovery: |
      1. 重新分析业务能力
      2. 调整服务边界
      3. 重构服务接口

  - name: 技术选型不合理
    detection: 技术不满足需求
    recovery: |
      1. 重新评估技术选型
      2. POC 验证备选方案
      3. 调整技术栈

  - name: 性能不达标
    detection: 性能测试失败
    recovery: |
      1. 分析性能瓶颈
      2. 优化架构设计
      3. 调整技术方案

  - name: 成本超预算
    detection: 成本估算超标
    recovery: |
      1. 评估成本优化方案
      2. 调整技术选型
      3. 分阶段实施
```

## Output Validation

```yaml
validation:
  - 检查项: 架构完整性
    标准: 覆盖所有业务需求

  - 检查项: 服务拆分合理性
    标准: 服务边界清晰，低耦合

  - 检查项: 技术选型合理性
    标准: 满足需求，团队可驾驭

  - 检查项: 性能设计
    标准: 可满足性能指标

  - 检查项: 架构评审通过
    标准: 评审委员会通过
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
    - name: 架构设计文档
      path: docs/architecture/design.md
      description: 完整架构设计文档

    - name: 架构图
      path: docs/architecture/diagrams/
      description: 架构图集

    - name: 接口契约
      path: docs/architecture/contracts/
      description: API 接口定义

    - name: ADR
      path: docs/architecture/adr/
      description: 架构决策记录

  architecture_summary:
    services: 服务数量
    databases: 数据库数量
    estimated_cost: 预估成本

  review_status:
    architecture_review: 通过
    security_review: 通过

  next_phase:
    phase: design-system
    entry_criteria: 架构设计已评审
    handover_data: 架构文档、服务列表
```

## Example Output Structure

```yaml
design_architecture_result:
  overview:
    project: "电商平台 2.0"
    architecture_type: "微服务架构"
    deployment: "Kubernetes on Cloud"

  services:
    - name: "user-service"
      type: "core"
      team: "用户团队"
      tech_stack: "Java/Spring Boot"

    - name: "product-service"
      type: "core"
      team: "商品团队"
      tech_stack: "Java/Spring Boot"

    - name: "order-service"
      type: "core"
      team: "订单团队"
      tech_stack: "Go"

  data_architecture:
    databases:
      - name: "users"
        type: "MySQL"
        purpose: "用户数据"

      - name: "products"
        type: "MongoDB"
        purpose: "商品数据"

      - name: "orders"
        type: "PostgreSQL"
        purpose: "订单数据"

  non_functional:
    availability: "99.99%"
    latency_p99: "< 200ms"
    throughput: "10,000 QPS"
    data_retention: "3 years"

  estimated_cost:
    monthly: "$50,000"
    yearly: "$600,000"
```

## Execution Flow

> Step-by-step execution sequence for design-architecture

### Phase 1: Analysis
- Understand requirements and context
- Identify constraints and dependencies

### Phase 2: Execution
- Perform core design-architecture activities
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
## Architecture Design Deliverables

### Summary
- Status: [completed | partial | blocked]
- Completion: [percentage]

### Key Outputs
1. **Architecture Vision**: Target architecture state description
2. **Architecture Decisions**: ADRs with rationale and trade-offs
3. **Component Model**: System decomposition diagrams
4. **Deployment Model**: Environment topology and infrastructure mapping
5. **Quality Attribute Scenarios**: Measurable quality goals and strategies

### Validation Checklist
- [ ] All quality attributes have verifiable scenarios
- [ ] ADRs are complete with rationale and trade-offs
- [ ] Architecture review achieves stakeholder consensus
- [ ] Design aligns with organizational constraints

### Next Steps
- [ ] Schedule architecture review
- [ ] Proceed to detailed system design
```

