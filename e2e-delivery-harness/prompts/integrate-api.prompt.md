---
name: integrate-api
description: "integrate api execution prompt for E2E delivery workflow"
type: prompt
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['prompt', 'ai-execution']
---
# Prompt: API 集成 (Integrate API)

## Purpose

本提示词指导AI执行API集成任务，按照API规范设计并实现第三方或内部服务API的集成代码，确保安全、可靠、高效。

### Key Objectives

- **准确理解API规范**: 深入分析API文档、认证方式和数据模型，确保集成实现与规范一致
- **健壮的集成层设计**: 构建可维护的API客户端抽象层，封装外部差异，提供统一接口
- **全面的错误处理**: 实现重试、熔断、降级等弹性模式，确保集成可靠性
- **安全合规保障**: 安全存储凭证、加密传输数据、遵循最小权限原则
- **规范交接准备**: 生成完整的API客户端代码、使用文档和集成测试

## Input Variables (变量定义)

> **AI 在执行前必须确认以下变量已填充**，如未填充则请求用户提供

| Variable | Type | Required | Default | Description | Validation |
|----------|------|----------|---------|-------------|------------|
| `api_specs` | string | true | - | API规范文档地址或内容(OpenAPI/Swagger) | 有效的URL或YAML/JSON内容 |
| `auth_method` | string | true | - | 认证方式: oauth2\|apikey\|jwt\|basic\|none | 枚举值之一 |
| `rate_limits` | object | false | {} | 限流配置(请求数/秒，突发值) | 包含requests_per_second字段 |
| `timeout_config` | object | true | {connect:10,read:30} | 超时配置(连接超时/读取超时，秒) | 正整数 |
| `retry_strategy` | object | false | {max:3,backoff:"exponential"} | 重试策略(最大重试次数、退避算法) | 包含max_retries和backoff字段 |
| `error_mappings` | array | false | [] | 错误码映射表(外部错误→内部错误) | 包含source和target字段 |
| `target_services` | array | true | - | 目标服务列表 | 非空字符串数组 |

### 示例: 变量的正确格式

```yaml
# 示例: 完整的API集成输入
api_specs: "https://api.example.com/openapi/v3.yaml"
auth_method: "oauth2"
rate_limits:
  requests_per_second: 100
  burst: 200
timeout_config:
  connect: 10
  read: 30
  write: 30
retry_strategy:
  max_retries: 3
  backoff: "exponential"
  max_backoff_ms: 30000
error_mappings:
  - source: "401"
    target: "UNAUTHORIZED"
    action: "refresh_token"
  - source: "429"
    target: "RATE_LIMITED"
    action: "retry_with_backoff"
  - source: "503"
    target: "SERVICE_UNAVAILABLE"
    action: "circuit_break"
target_services:
  - "payment-gateway"
  - "notification-service"
```

## Chain of Thought (思维链)

> **AI 必须按照以下思维链逐步执行**，每完成一步后进行自我验证

```
[THINK] Step 1: 理解API集成需求和约束
   ├─ 输入: api_specs, target_services, auth_method
   ├─ 思考: API功能范围是什么？认证流程如何工作？有哪些约束和限制？
   ├─ 验证: 与API规范逐条对照，确认理解准确无歧义
   └─ 输出: API集成需求分析（接口清单、认证流程、数据模型、约束条件）
   ↓
[ANALYZE] Step 2: 分析集成方案和弹性模式
   ├─ 输入: API集成需求分析, rate_limits, timeout_config, retry_strategy, error_mappings
   ├─ 思考: 哪些弹性模式需要实现？限流和重试策略如何配置？
   ├─ 验证: 方案覆盖所有异常场景，弹性策略合理
   └─ 输出: 集成技术方案（接口抽象设计、弹性策略、错误映射、缓存方案）
   ↓
[DESIGN] Step 3: 设计API客户端和数据映射
   ├─ 输入: 集成技术方案, api_specs
   ├─ 思考: 接口抽象层如何设计？数据映射如何处理类型差异？
   ├─ 验证: 接口设计一致性好，字段映射完整无遗漏
   └─ 输出: API客户端设计（类图、接口定义、数据模型、映射规则）
   ↓
[IMPLEMENT] Step 4: 实现API客户端和测试
   ├─ 输入: API客户端设计, auth_method, error_mappings
   ├─ 思考: 认证模块如何实现？重试和熔断如何集成？测试如何覆盖？
   ├─ 验证: 实现符合设计规范，认证和重试逻辑正确
   └─ 输出: API客户端代码 + 认证模块 + 错误处理 + 单元测试
   ↓
[VERIFY] Step 5: 验证集成正确性和性能
   ├─ 输入: API客户端代码, 单元测试
   ├─ 执行: 集成测试(Mock/沙箱)、并发测试、错误场景测试
   ├─ 验证: 集成测试通过率≥95%，延迟满足SLA，错误处理覆盖所有场景
   └─ 输出: 集成验证报告（测试结果、性能指标、错误覆盖分析）
   ↓
[HANDOVER] Step 6: 准备交接给功能实现阶段
   ├─ 生成: Handover Context（客户端代码、使用文档、测试报告）
   ├─ 更新: Global Context（API状态、已知问题、使用注意事项）
   └─ 通知: Implement Feature Agent（提交代码审查请求）
```

## Error Handling (错误处理)

> **AI 在执行过程中遇到以下情况时的处理策略**

### Error Scenario 1: 网络超时

**识别信号**: 
- ConnectTimeout / ReadTimeout
- HTTP请求无响应

**处理流程**:
```
IF 网络超时
THEN
  1. 按指数退避策略重试（最多{retry_strategy.max_retries}次）
  2. 每增加一次重试，等待时间加倍
  3. 超过最大重试次数后返回降级结果
  4. 记录超时错误日志和重试历史
END
```

**降级方案**: 返回缓存数据或友好的错误提示

**升级条件**: 连续5次超时，触发熔断器

---

### Error Scenario 2: API限流

**识别信号**: 
- HTTP 429 Too Many Requests
- RateLimitExceeded 错误

**处理流程**:
```
IF API限流
THEN
  1. 解析 Retry-After 响应头
  2. 等待指定时间后重试
  3. 使用本地限流控制避免再次触发
  4. IF 频繁限流 THEN 调整客户端限流参数
END
```

**降级方案**: 降级到缓存数据，减少请求频率

**升级条件**: 限流导致核心业务流程中断

---

### Error Scenario 3: 认证/授权失败

**识别信号**: 
- HTTP 401 Unauthorized / HTTP 403 Forbidden
- Token过期或无效

**处理流程**:
```
IF 认证失败
THEN
  1. 检查Token有效期和状态
  2. 尝试Token刷新流程（refresh_token可用时）
  3. 刷新成功则重试原始请求
  4. 刷新失败则重新获取凭证
END
```

**降级方案**: 提示用户重新认证，使用只读模式

**升级条件**: 认证完全不可用，无法获取有效Token

---

### Error Scenario 4: 服务不可用

**识别信号**: 
- HTTP 503 Service Unavailable
- Connection Refused

**处理流程**:
```
IF 服务不可用
THEN
  1. 触发熔断器打开（停止后续请求）
  2. 返回降级数据或错误提示
  3. 启动定时探测（每隔X秒发送健康检查）
  4. 服务恢复后关闭熔断器
END
```

**降级方案**: 使用本地缓存数据，提示用户服务暂时不可用

**升级条件**: 熔断器长时间未恢复（>5分钟），需人工介入

---

### Error Scenario 5: 数据映射错误

**识别信号**: 
- 响应解析失败 / 字段类型不匹配
- 数据转换异常

**处理流程**:
```
IF 数据映射错误
THEN
  1. 记录原始响应和异常详情
  2. 检查API版本是否与规范一致
  3. 尝试宽松解析（忽略未知字段）
  4. 标记为[需确认-数据映射]通知集成方
END
```

**降级方案**: 返回部分可用数据，标记缺失字段

**升级条件**: 关键字段映射失败，影响业务流程

## Quality Metrics (质量指标)

### Key Performance Indicators (KPIs)

| KPI ID | 指标名称 | 目标值 | 计算公式 | 验证方法 | 权重 |
|--------|----------|--------|----------|----------|------|
| KPI-001 | INTEGRATION-PASS | ≥95% | (通过测试数/总测试数)×100% | 集成测试执行 | 30% |
| KPI-002 | ERROR-HANDLE | =100% | (已覆盖错误码数/总错误码数)×100% | 错误覆盖审查 | 25% |
| KPI-003 | LATENCY-SLA | ≥99% | (SLA内请求数/总请求数)×100% | 延迟监控统计 | 25% |
| KPI-004 | RETRY-SUCCESS | ≥90% | (重试成功数/总重试数)×100% | 重试日志分析 | 20% |

**综合评分计算**: 
```
Quality Score = (INTEGRATION-PASS×100) × 0.30 + (ERROR-HANDLE×100) × 0.25 + (LATENCY-SLA×100) × 0.25 + (RETRY-SUCCESS×100) × 0.20
合格: ≥70分 | 优秀: ≥85分 | 卓越: ≥95分
```

## Output Format (输出格式)

> AI必须按照以下结构生成API集成交付物

```markdown
## API Integration Deliverables

### 1. Summary
- **Status**: completed / partial / blocked
- **Completion**: {percentage}
- **Quality Score**: {score}/100

### 2. Integration Overview
- **API Provider**: {target_services}
- **Authentication**: {auth_method}
- **Endpoints Integrated**: {N}
- **Client Language**: {language}

### 3. Client Implementation
- **Features**:
  - {auth_method} authentication with auto-refresh
  - Exponential backoff retry (max {retry_strategy.max_retries} times)
  - Circuit breaker protection
  - Rate limiting ({rate_limits.requests_per_second}/s)
- **Error Mappings**: {N} error codes mapped
- **Timeout Config**: connect {timeout_config.connect}s / read {timeout_config.read}s

### 4. Test Results
- **Integration Test Pass Rate**: {X}% (target: ≥95%)
- **Error Handling Coverage**: {X}% (target: 100%)
- **Latency SLA Compliance**: {X}% (target: ≥99%)
- **Retry Success Rate**: {X}% (target: ≥90%)

### 5. Quality Score
- **Overall Score**: {score}/100
- **Grade**: Excellent (≥95) / Good (≥85) / Satisfactory (≥70) / Needs Improvement (<70)
- **KPI Breakdown**:
  - INTEGRATION-PASS: {value}% (target: ≥95%) - {pass/fail}
  - ERROR-HANDLE: {value}% (target: 100%) - {pass/fail}
  - LATENCY-SLA: {value}% (target: ≥99%) - {pass/fail}
  - RETRY-SUCCESS: {value}% (target: ≥90%) - {pass/fail}
```

## Output Validation (输出验证)

> **重要**: 在提交前，必须完成以下验证步骤

### Validation Checklist

**V-001: Client Completeness (客户端完整性验证)**
- [ ] 所有目标API端点已封装，接口一致
- [ ] 认证机制完整（获取/刷新/续期）
- [ ] 请求/响应拦截器已配置

**V-002: Error Handling (错误处理验证)**
- [ ] 所有HTTP错误码有对应处理逻辑
- [ ] 重试机制正确实现（指数退避）
- [ ] 熔断器保护已配置并测试

**V-003: Data Mapping (数据映射验证)**
- [ ] 字段映射完整，无数据丢失
- [ ] 类型转换正确处理
- [ ] 枚举值映射一致性确认

**V-004: Security and Compliance (安全合规验证)**
- [ ] 凭证安全存储（非明文）
- [ ] 传输加密（TLS/HTTPS）
- [ ] 日志不记录敏感信息

**V-005: Test Coverage (测试覆盖验证)**
- [ ] 单元测试覆盖率 ≥ 80%
- [ ] 集成测试覆盖所有端点
- [ ] 错误场景测试覆盖所有映射

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

> 完成API集成任务后，生成以下交接信息

```yaml
handover:
  header:
    from_stage: "integrate-api"
    to_stage: "implement-feature"
    handover_id: "HO-{{timestamp}}-{{sequence}}"
    timestamp: "{{ISO8601}}"
    prepared_by: "{{agent.name}}"

  summary:
    status: "completed/partial/blocked"
    completion_percentage: {{0-100}}
    quality_score: {{0-100}}
    endpoints_count: {{number}}
    test_coverage: {{percentage}}

  artifacts:
    delivered:
      - name: "API Client Code"
        path: "src/api-clients/{service}/"
        version: "1.0.0"
      - name: "API Documentation"
        path: "docs/api/{service}.md"
        version: "1.0.0"
      - name: "Integration Tests"
        path: "tests/api/{service}/"
        version: "1.0.0"

  metrics:
    integration_pass_rate: {{percentage}}
    error_handle_coverage: {{percentage}}
    latency_sla_compliance: {{percentage}}
    retry_success_rate: {{percentage}}

  decisions:
    - id: "DC-001"
      description: "API client architecture"
      rationale: "Chose abstract client pattern for consistency"
      alternatives_considered: ["Direct HTTP calls", "Auto-generated client"]
      impact: "Affects maintainability and onboarding"

  open_issues:
    blocking: []
    non_blocking:
      - id: "ISSUE-001"
        description: "{feature} endpoint not covered by integration tests"
        risk_level: "low"
        planned_resolution: "Add tests in next iteration"

  risks:
    - id: "RISK-001"
      description: "API version upgrade may break integration"
      probability: "low"
      impact: "high"
      mitigation: "Version-pinned client with contract tests"
      contingency_plan: "Fallback to previous API version"

  quality_metrics:
    kpi_results:
      - kpi_id: "KPI-001"
        name: "INTEGRATION-PASS"
        value: 97
        target: 95
        unit: "%"
        status: "pass"
      - kpi_id: "KPI-002"
        name: "ERROR-HANDLE"
        value: 100
        target: 100
        unit: "%"
        status: "pass"
      - kpi_id: "KPI-003"
        name: "LATENCY-SLA"
        value: 99.5
        target: 99
        unit: "%"
        status: "pass"
      - kpi_id: "KPI-004"
        name: "RETRY-SUCCESS"
        value: 95
        target: 90
        unit: "%"
        status: "pass"
    overall_score: 91
    grade: "excellent"

  recommendations:
    - "Set up API consumption monitoring dashboard"
    - "Review error mapping when API version updates"
    - "Consider adding circuit breaker metrics"
```

## Related Assets (关联资产)

| Asset Type | Path | Description |
|------------|------|-------------|
| Scenario | `../scenarios/integrate-api/SCENARIO.md` | API集成场景定义 |
| Agent | `../agents/integrate-api.agent.md` | API集成Agent角色 |
| Instruction | `../instructions/integrate-api.instructions.md` | API集成技术指令 |

## Related Resources (相关资源)

- **Standards**: 
  - [API Design Standards](../standards/api-design-standards.md) - API设计规范
  - [Security Guidelines](../standards/security-guidelines.md) - 安全配置指南
- **Templates**: 
  - [API Client Template](../templates/api-client.template.md) - API客户端代码模板
- **Evaluations**: 
  - [Integration Test Checklist](../evaluations/integration-test-checklist.md) - 集成测试检查清单

## Handover Preparation (交接准备)

使用 [contexts/unified-handover-template.md](../contexts/unified-handover-template.md)。

```yaml
handover:
  header:
    from_stage: "integrate-api"
    to_stage: "implement-feature"
    handover_id: "HO-{ISO8601}-{sequence}"
    timestamp: "{ISO8601}"
    prepared_by: "integrate-api"
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
