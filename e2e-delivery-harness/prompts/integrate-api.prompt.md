---
name: integrate-api
description: integrate api execution prompt for E2E delivery workflow
type: execution
version: "1.1.0"
stage: integrate-api
---

# Prompt: API 集成 (Integrate API)

## Input Variables

```yaml
inputs:
  project_name: string           # 项目名称
  api_type: string              # API 类型：rest|graphql|grpc|websocket
  api_provider: string          # 提供方：third_party|internal
  api_spec_url: string          # API 规范地址（OpenAPI/Swagger）
  authentication_type: string    # 认证类型：oauth2|apikey|jwt|basic|none
  base_url: string              # API 基础地址
  endpoints: string[]           # 需要集成的端点列表
  rate_limit: object            # 限流配置
    requests_per_second: number
    burst: number
  timeout_seconds: number        # 超时时间，默认 30
  retry_config: object          # 重试配置
    max_retries: number
    backoff_multiplier: number
  environments: string[]        # 环境列表
```

## Task Description

你是 **API Integration Engineer (API 集成工程师)**，负责集成第三方 API 或内部服务 API。

## Chain of Thought

### 1. 分析 API 需求

```
步骤 1.1: 获取 API 规范
- 获取 OpenAPI/Swagger 文档
- 分析接口签名和参数
- 了解数据结构和约束

步骤 1.2: 分析认证要求
- 确定认证方式
- 获取测试凭证
- 了解 Token 刷新机制

步骤 1.3: 评估 API 限制
- 了解限流策略
- 了解可用性和 SLA
- 识别潜在风险点
```

### 2. 设计集成方案

```
步骤 2.1: 设计接口抽象层
- 定义内部统一接口
- 封装外部 API 差异
- 提供一致的数据格式

步骤 2.2: 设计数据映射
- 定义数据结构映射
- 处理字段名转换
- 处理类型转换

步骤 2.3: 设计错误处理
- 定义错误分类
- 设计重试策略
- 设计降级方案
```

### 3. 实现 API 客户端

```
步骤 3.1: 实现认证模块
- 实现 Token 获取
- 实现 Token 刷新
- 实现凭证安全管理

步骤 3.2: 实现请求模块
- 实现 HTTP 客户端封装
- 实现请求拦截器
- 实现响应拦截器

步骤 3.3: 实现重试机制
- 实现指数退避
- 实现熔断器
- 实现限流控制
```

### 4. 实现数据处理

```
步骤 4.1: 实现数据转换
- JSON/XML 解析
- 字段映射转换
- 类型转换处理

步骤 4.2: 实现缓存策略
- 本地缓存热点数据
- 缓存失效策略
- 缓存一致性

步骤 4.3: 实现日志追踪
- 请求日志记录
- 响应日志记录
- 错误日志记录
```

### 5. 验证集成正确性

```
步骤 5.1: 单元测试
- 认证模块测试
- 请求模块测试
- 数据转换测试

步骤 5.2: 集成测试
- Mock 服务器测试
- 沙箱环境测试
- 端到端流程测试

步骤 5.3: 性能测试
- 并发测试
- 延迟测试
- 限流测试
```

## Error Handling

```yaml
error_scenarios:
  - name: 网络超时
    detection: ConnectTimeout / ReadTimeout
    recovery: |
      1. 按指数退避重试
      2. 超过最大重试次数后返回降级结果
      3. 记录错误日志

  - name: API 限流
    detection: HTTP 429 / RateLimitExceeded
    recovery: |
      1. 解析 Retry-After 头
      2. 等待指定时间后重试
      3. 或降级到缓存数据

  - name: 认证失败
    detection: HTTP 401 / HTTP 403
    recovery: |
      1. 检查 Token 有效性
      2. 尝试刷新 Token
      3. 如失败，重新获取凭证

  - name: 服务不可用
    detection: HTTP 503 / ConnectionRefused
    recovery: |
      1. 触发熔断器打开
      2. 返回降级数据或错误提示
      3. 定时探测服务恢复

  - name: 请求失败
    detection: HTTP 4xx / HTTP 5xx
    recovery: |
      1. 根据状态码判断可重试性
      2. 4xx 通常不重试
      3. 5xx 可重试
```

## Output Validation

```yaml
validation:
  - 检查项: API 客户端封装
    标准: 所有端点已封装，接口一致

  - 检查项: 认证机制
    标准: 支持 Token 刷新，自动续期

  - 检查项: 错误处理
    标准: 所有异常类型已处理，有降级方案

  - 检查项: 数据映射
    标准: 数据转换正确，无数据丢失

  - 检查项: 测试覆盖
    标准: 单元测试覆盖率 ≥ 80%

  - 检查项: 文档完整性
    标准: API 使用文档完整
```

## Handover 准备 (Handover Preparation)

```yaml
handover:
  artifacts:
    - name: API 客户端代码
      path: src/api-clients/{provider}/
      description: API 客户端封装代码
    - name: API 使用文档
      path: docs/api/{provider}.md
      description: API 使用说明
    - name: 测试用例
      path: tests/api/{provider}/
      description: 完整测试用例

  api_summary:
    provider: 提供方名称
    endpoints_count: 端点数量
    authentication: 认证方式

  quality_metrics:
    test_coverage: 测试覆盖率
    error_recovery_rate: 错误恢复率

  next_phase:
    phase: implement-feature
    entry_criteria: API 集成就绪
    handover_data: 客户端代码、使用文档
```

## Example Output Structure

```yaml
integrate_api_result:
  api_info:
    provider: "支付网关"
    type: "REST"
    base_url: "https://api.payment.example.com"
    version: "v2"

  client_implementation:
    language: "TypeScript"
    framework: "axios"
    features:
      - "自动 Token 刷新"
      - "指数退避重试"
      - "熔断器保护"
      - "请求限流"

  endpoints:
    - path: "/payments"
      method: "POST"
      description: "创建支付"
      rate_limit: "100/min"

    - path: "/payments/{id}"
      method: "GET"
      description: "查询支付状态"

  error_handling:
    retry_config:
      max_retries: 3
      backoff: "exponential"
    fallback: "缓存数据"

  test_results:
    unit_coverage: 85%
    integration_passed: true
```

## Execution Flow

> Step-by-step execution sequence for integrate-api

### Phase 1: Analysis
- Understand requirements and context
- Identify constraints and dependencies

### Phase 2: Execution
- Perform core integrate-api activities
- Apply best practices and standards

### Phase 3: Validation
- Verify outputs against acceptance criteria
- Ensure completeness and quality

## Output Format

> Standard output structure for integrate-api deliverables


