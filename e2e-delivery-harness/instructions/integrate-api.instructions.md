---
name: integrate-api
description: "Detailed technical instructions for integrate-api scenario execution"
applyTo: "scenarios/integrate-api/**"
phase: development
type: instruction
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
language: "zh-CN"
tags: ['instruction', 'technical']
---
# Instructions: API 集成 (Integrate API)

## Authentication方式规范

### Authentication类型对比

| 类型 | 适用场景 | 实现复杂度 | 安全性 |
|------|----------|------------|--------|
| API Key | 简单验证 | 低 | 中 |
| Basic Auth | 测试/开发 | 低 | 低 |
| OAuth 2.0 | 第三方授权 | 高 | 高 |
| JWT | 无状态认证 | 中 | 高 |
| HMAC | 签名验证 | 中 | 高 |

### OAuth 2.0 实现规范

```yaml
# OAuth 2.0 流程
flows:
  client_credentials:
    use_case: "服务端到服务端"
    token_endpoint: "/oauth/token"

  authorization_code:
    use_case: "用户授权"
    endpoints:
      - "/oauth/authorize"
      - "/oauth/token"
      - "/oauth/revoke"

# Token 管理
token_management:
  storage: "加密存储"
  refresh_threshold: "过期前 5 分钟"
  refresh_strategy: "主动刷新 + 被动检测"
```

### JWT 实现规范

```python
# JWT 配置示例
jwt_config = {
    "algorithm": "RS256",  # 推荐使用非对称算法
    "expiration": 3600,    # 1 小时
    "refresh_expiration": 86400,  # 24 小时
    "claims": {
        "iss": "api-provider",
        "aud": "client-app",
        "scope": ["read", "write"]
    }
}
```

## HTTP 客户端规范

### 客户端选择

| 语言 | 推荐客户端 | 特点 |
|------|------------|------|
| JavaScript/TypeScript | axios / ky | Promise 支持、拦截器 |
| Python | requests / httpx | 简单易用、异步支持 |
| Java | Retrofit / OkHttp | 类型安全、功能丰富 |
| Go | net/http / colly | 轻量、并发支持 |
| Go | Resty | 简洁、链式调用 |

### 请求配置规范

```yaml
# 通用请求配置
request_config:
  timeout:
    connect: 5      # 连接超时（秒）
    read: 30        # 读取超时（秒）
    write: 30       # 写入超时（秒）

  headers:
    default:
      Content-Type: "application/json"
      Accept: "application/json"
      User-Agent: "{app-name}/1.0"

  retry:
    max_attempts: 3
    backoff:
      type: "exponential"
      base: 2
      max_delay: 60

  circuit_breaker:
    failure_threshold: 5      # 失败次数
    success_threshold: 2      # 成功次数恢复
    timeout: 60               # 熔断超时（秒）
```

## Retry Strategy Standards

### 重试决策矩阵

```yaml
retry_decision:
  # 可以重试
  retryable:
    - HTTP 408 (Request Timeout)
    - HTTP 429 (Too Many Requests)
    - HTTP 500 (Internal Server Error)
    - HTTP 502 (Bad Gateway)
    - HTTP 503 (Service Unavailable)
    - HTTP 504 (Gateway Timeout)
    - 网络错误 (Timeout, Connection Reset)

  # 不应重试
  non_retryable:
    - HTTP 400 (Bad Request)
    - HTTP 401 (Unauthorized)
    - HTTP 403 (Forbidden)
    - HTTP 404 (Not Found)
    - HTTP 409 (Conflict)
```

### 指数退避算法

```python
def calculate_backoff(attempt, base=2, max_delay=60):
    """
    指数退避计算
    attempt: 重试次数（从 1 开始）
    base: 退避基数
    max_delay: 最大延迟（秒）
    """
    # 添加 jitter 避免惊群效应
    import random
    delay = min(base ** attempt + random.uniform(0, 1), max_delay)
    return delay

# 示例
# attempt=1: delay=2-3s
# attempt=2: delay=4-5s
# attempt=3: delay=8-9s
# attempt=4: delay=16-17s
# attempt=5: delay=32-33s
```

## Rate Limiting Standards

### 限流算法

| 算法 | 特点 | 实现难度 |
|------|------|----------|
| 固定窗口 | 简单 | 低 |
| 滑动窗口 | 精确 | 中 |
| 令牌桶 | 允许突发 | 中 |
| 漏桶 | 流量平滑 | 中 |

### 限流实现

```python
import time
from collections import deque

class TokenBucket:
    """令牌桶限流器"""

    def __init__(self, rate, capacity):
        self.rate = rate           # 每秒令牌数
        self.capacity = capacity    # 桶容量
        self.tokens = capacity
        self.last_update = time.time()

    def acquire(self, tokens=1):
        """获取令牌"""
        now = time.time()
        elapsed = now - self.last_update

        # 补充令牌
        self.tokens = min(
            self.capacity,
            self.tokens + elapsed * self.rate
        )
        self.last_update = now

        if self.tokens >= tokens:
            self.tokens -= tokens
            return True
        return False

    def wait_and_acquire(self, tokens=1, timeout=30):
        """等待并获取令牌"""
        start = time.time()
        while time.time() - start < timeout:
            if self.acquire(tokens):
                return True
            time.sleep(0.1)
        return False
```

## Circuit Breaker Standards

### 熔断器状态机

```
┌─────────────┐
│   CLOSED    │  正常状态，请求通过
└──────┬──────┘
       │ 失败次数超过阈值
       ▼
┌─────────────┐
│   OPEN      │ 熔断状态，请求被拒绝
└──────┬──────┘
       │ 超时后进入半开
       ▼
┌─────────────┐
│ HALF-OPEN   │ 探测状态，允许部分请求
└──────┬──────┘
       │ 成功/失败
       ▼
  CLOSED 或 OPEN
```

### 熔断器实现

```python
class CircuitBreaker:
    """熔断器实现"""

    def __init__(self, failure_threshold=5, success_threshold=2,
                 timeout=60):
        self.failure_threshold = failure_threshold
        self.success_threshold = success_threshold
        self.timeout = timeout

        self.failure_count = 0
        self.success_count = 0
        self.state = 'CLOSED'  # CLOSED, OPEN, HALF_OPEN
        self.last_failure_time = None

    def call(self, func, *args, **kwargs):
        """执行带熔断保护的调用"""
        if self.state == 'OPEN':
            if self._should_attempt_reset():
                self.state = 'HALF_OPEN'
            else:
                raise CircuitOpenError()

        try:
            result = func(*args, **kwargs)
            self._on_success()
            return result
        except Exception as e:
            self._on_failure()
            raise e

    def _on_success(self):
        self.failure_count = 0
        if self.state == 'HALF_OPEN':
            self.success_count += 1
            if self.success_count >= self.success_threshold:
                self.state = 'CLOSED'

    def _on_failure(self):
        self.failure_count += 1
        self.last_failure_time = time.time()

        if self.state == 'HALF_OPEN':
            self.state = 'OPEN'
        elif self.failure_count >= self.failure_threshold:
            self.state = 'OPEN'

    def _should_attempt_reset(self):
        elapsed = time.time() - self.last_failure_time
        return elapsed >= self.timeout
```

## Logging and Monitoring Standards

### 日志规范

```yaml
# API 调用日志
api_log:
  required_fields:
    - timestamp
    - request_id
    - method
    - url
    - status_code
    - response_time_ms
    - error_message (if any)

  sensitive_fields:
    - api_key
    - authorization
    - request_body (部分)
    - response_body (部分)

  log_levels:
    DEBUG: "详细调试信息"
    INFO: "正常请求"
    WARN: "重试、限流"
    ERROR: "请求失败"
```

### 监控指标

```yaml
# API 监控指标
metrics:
  - name: "api_request_total"
    type: "counter"
    labels: ["provider", "endpoint", "status"]

  - name: "api_request_duration_seconds"
    type: "histogram"
    labels: ["provider", "endpoint"]

  - name: "api_retry_total"
    type: "counter"
    labels: ["provider", "reason"]

  - name: "api_circuit_breaker_state"
    type: "gauge"
    labels: ["provider", "state"]

  - name: "api_rate_limit_remaining"
    type: "gauge"
    labels: ["provider"]
```


## Overview

> High-level description of the integrate-api execution process.
>
> This instruction defines the technical approach, key activities, and success criteria for the integrate-api scenario.


## Technical Specifications

> Detailed technical requirements and implementation guidelines for integrate-api.

### Required Tools
- **Postman / Insomnia / Hoppscotch**: API 调试与测试
- **Swagger Editor / OpenAPI Generator / Stoplight**: API 设计、文档生成与代码生成
- **Apigee / Kong / AWS API Gateway**: API 网关管理
- **curl / httpie / wscat**: 命令行 API 调试工具
- **pytest + requests / Karate / REST Assured**: API 自动化测试框架
- **WireMock / Mockoon / Prism**: API Mock 服务

### Environment Requirements
- API 契约（OpenAPI 3.0+ / gRPC proto 文件）已发布且在 API Registry 中可发现
- 集成测试环境与生产 API 版本一致（版本漂移容忍度 ≤1 Minor）
- API 网关（如 Kong/APISIX）已部署且路由规则已配置
- Mock 服务已就绪（用于隔离外部依赖进行测试）

### Configuration Parameters
- `API_TIMEOUT`: API 调用超时时间（内部 API ≤5s，外部 API ≤30s）
- `RETRY_POLICY`: 重试策略（最大 3 次，指数退避 base=1s，仅幂等操作可重试）
- `RATE_LIMIT`: 速率限制（每 Token 每秒 100 请求，超过返回 429）
- `CIRCUIT_BREAKER`: 熔断配置（错误率 >50% 时熔断，60s 后半开探测）
- `API_VERSION_HEADER`: API 版本控制方式（Header: Accept-Version / URL: /v1/）


## Multi-Language Code Examples

> Production-grade API client implementations demonstrating resilience patterns with circuit breaker, retry, exponential backoff, and bulkhead isolation.

### Java (OkHttp + Resilience4j)

```java
// Java (OkHttp + Resilience4j) - API Client with Circuit Breaker, Retry, and Bulkhead
import okhttp3.*;
import io.github.resilience4j.circuitbreaker.*;
import io.github.resilience4j.retry.*;
import io.github.resilience4j.bulkhead.*;
import io.github.resilience4j.decorators.Decorators;

import java.io.IOException;
import java.time.Duration;
import java.util.concurrent.TimeUnit;
import java.util.function.Supplier;

public class ResilientApiClient {
    private final OkHttpClient httpClient;
    private final CircuitBreaker circuitBreaker;
    private final Retry retry;
    private final Bulkhead bulkhead;

    public ResilientApiClient() {
        // HTTP 客户端配置：连接超时、读写超时、连接池
        this.httpClient = new OkHttpClient.Builder()
            .connectTimeout(5, TimeUnit.SECONDS)
            .readTimeout(30, TimeUnit.SECONDS)
            .writeTimeout(30, TimeUnit.SECONDS)
            .connectionPool(new ConnectionPool(50, 5, TimeUnit.MINUTES))
            .addInterceptor(new AuthenticationInterceptor())
            .addInterceptor(new LoggingInterceptor())
            .build();

        // CircuitBreaker 配置：滑动窗口统计、半开探测、异常记录
        CircuitBreakerConfig cbConfig = CircuitBreakerConfig.custom()
            .failureRateThreshold(50)                       // 失败率阈值 50%
            .waitDurationInOpenState(Duration.ofSeconds(30)) // 熔断持续时间 30s
            .permittedNumberOfCallsInHalfOpenState(3)        // 半开状态允许 3 次探测
            .slidingWindowSize(10)                           // 滑动窗口大小 10
            .minimumNumberOfCalls(5)                         // 最少调用数 5
            .recordExceptions(IOException.class,
                              java.net.SocketTimeoutException.class)
            .build();
        this.circuitBreaker = CircuitBreaker.of("api-cb", cbConfig);

        // Retry 配置：指数退避 + 状态码过滤
        RetryConfig retryConfig = RetryConfig.custom()
            .maxAttempts(3)
            .waitDuration(Duration.ofSeconds(1))
            .retryOnResult(response -> {
                int code = ((Response) response).code();
                return code >= 500 || code == 408 || code == 429;
            })
            .retryExceptions(IOException.class)
            .build();
        this.retry = Retry.of("api-retry", retryConfig);

        // Bulkhead 信号量隔离：最大并发 + 等待队列
        BulkheadConfig bulkheadConfig = BulkheadConfig.custom()
            .maxConcurrentCalls(20)
            .maxWaitDuration(Duration.ofMillis(500))
            .build();
        this.bulkhead = Bulkhead.of("api-bulkhead", bulkheadConfig);
    }

    public Response callApi(Request request) {
        Supplier<Response> decoratedSupplier = Decorators.ofSupplier(() -> {
            try {
                return httpClient.newCall(request).execute();
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        })
        .withCircuitBreaker(circuitBreaker)
        .withRetry(retry)
        .withBulkhead(bulkhead)
        .decorate();

        return decoratedSupplier.get();
    }

    // CircuitBreaker 状态监控（供 Prometheus 采集）
    public String getCircuitBreakerState() {
        return circuitBreaker.getState().name();
    }

    public CircuitBreaker.Metrics getCircuitBreakerMetrics() {
        return circuitBreaker.getMetrics();
    }

    // Authentication 拦截器 - 注入 OAuth2 Token
    private static class AuthenticationInterceptor implements Interceptor {
        @Override
        public Response intercept(Chain chain) throws IOException {
            Request original = chain.request();
            String token = TokenManager.getAccessToken();
            Request request = original.newBuilder()
                .header("Authorization", "Bearer " + token)
                .header("X-Request-Id", java.util.UUID.randomUUID().toString())
                .build();
            return chain.proceed(request);
        }
    }

    // 性能日志拦截器
    private static class LoggingInterceptor implements Interceptor {
        @Override
        public Response intercept(Chain chain) throws IOException {
            long start = System.currentTimeMillis();
            Request request = chain.request();
            Response response = chain.proceed(request);
            long duration = System.currentTimeMillis() - start;
            System.out.printf("[API] %s %s - %d (%dms)%n",
                request.method(), request.url(), response.code(), duration);
            return response;
        }
    }
}
```

### Go (net/http + retry)

```go
// Go (net/http + retry) - HTTP Client with Exponential Backoff and Retry
package client

import (
	"context"
	"fmt"
	"io"
	"math"
	"math/rand"
	"net/http"
	"time"
)

// RetryableClient 支持自动重试和指数退避的 HTTP 客户端
type RetryableClient struct {
	client     *http.Client
	maxRetries int
	baseDelay  time.Duration
	maxDelay   time.Duration
}

type Option func(*RetryableClient)

func WithMaxRetries(n int) Option {
	return func(c *RetryableClient) { c.maxRetries = n }
}

func WithBaseDelay(d time.Duration) Option {
	return func(c *RetryableClient) { c.baseDelay = d }
}

func WithMaxDelay(d time.Duration) Option {
	return func(c *RetryableClient) { c.maxDelay = d }
}

func NewRetryableClient(opts ...Option) *RetryableClient {
	c := &RetryableClient{
		client: &http.Client{
			Timeout: 30 * time.Second,
			Transport: &http.Transport{
				MaxIdleConns:        100,
				MaxIdleConnsPerHost: 20,
				IdleConnTimeout:     90 * time.Second,
				DisableCompression:  false,
			},
		},
		maxRetries: 3,
		baseDelay:  1 * time.Second,
		maxDelay:   60 * time.Second,
	}
	for _, opt := range opts {
		opt(c)
	}
	return c
}

// backoff 指数退避 + 随机 jitter 计算
func (c *RetryableClient) backoff(attempt int) time.Duration {
	delay := float64(c.baseDelay) * math.Pow(2, float64(attempt))
	jitter := rand.Float64() * float64(c.baseDelay) // 添加 jitter 避免惊群效应
	total := time.Duration(math.Min(delay+jitter, float64(c.maxDelay)))
	return total
}

// isRetryable 判断 HTTP 状态码是否可重试
func isRetryable(statusCode int) bool {
	switch statusCode {
	case http.StatusRequestTimeout,       // 408
		http.StatusTooManyRequests,       // 429
		http.StatusInternalServerError,   // 500
		http.StatusBadGateway,            // 502
		http.StatusServiceUnavailable,    // 503
		http.StatusGatewayTimeout:        // 504
		return true
	}
	return false
}

func (c *RetryableClient) Do(req *http.Request) (*http.Response, error) {
	var resp *http.Response
	var err error
	var body io.ReadCloser

	for attempt := 0; attempt <= c.maxRetries; attempt++ {
		// 重试时复用 request body
		if attempt > 0 && req.Body != nil {
			req.Body = io.NopCloser(body)
		}

		resp, err = c.client.Do(req)
		if err != nil {
			// 网络错误，等待后重试
			if attempt < c.maxRetries {
				time.Sleep(c.backoff(attempt))
				continue
			}
			return nil, fmt.Errorf(
				"request failed after %d retries: %w", c.maxRetries, err)
		}

		if isRetryable(resp.StatusCode) && attempt < c.maxRetries {
			// 读取并关闭 body 以复用连接
			body = resp.Body
			io.Copy(io.Discard, resp.Body)
			resp.Body.Close()
			time.Sleep(c.backoff(attempt))
			continue
		}

		return resp, nil
	}

	return resp, nil
}
```

### JavaScript (Axios + Opossum)

```javascript
// JavaScript (Axios + Opossum) - Axios Client with Circuit Breaker Pattern
const axios = require('axios');
const CircuitBreaker = require('opossum');
const crypto = require('crypto');

// 创建 Axios 实例 - 全局配置
const apiClient = axios.create({
  baseURL: process.env.API_BASE_URL || 'https://api.example.com',
  timeout: 30000,
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  },
  // HTTP 连接池配置
  httpAgent: new (require('http').Agent)({
    keepAlive: true,
    maxSockets: 50,
    maxFreeSockets: 10,
    scheduling: 'lifo',
  }),
});

// 请求拦截器 - 注入认证 Token 和请求追踪 ID
apiClient.interceptors.request.use(
  (config) => {
    config.headers['Authorization'] = `Bearer ${getAccessToken()}`;
    config.headers['X-Request-Id'] = crypto.randomUUID();
    config.metadata = { startTime: Date.now() };
    return config;
  },
  (error) => Promise.reject(error)
);

// 响应拦截器 - 性能日志 + Token 自动刷新
apiClient.interceptors.response.use(
  (response) => {
    const duration = Date.now() - response.config.metadata.startTime;
    console.log(
      `[API] ${response.config.method.toUpperCase()} ${response.config.url} ` +
      `- ${response.status} (${duration}ms)`
    );
    // 上报 Prometheus 指标
    recordApiMetric(response.config, response.status, duration);
    return response;
  },
  async (error) => {
    const originalRequest = error.config;
    // Token 过期自动刷新
    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      await refreshToken();
      originalRequest.headers['Authorization'] =
        `Bearer ${getAccessToken()}`;
      return apiClient(originalRequest);
    }
    return Promise.reject(error);
  }
);

// Opossum 熔断器配置
const breakerOptions = {
  timeout: 30000,                // 请求超时 30s
  errorThresholdPercentage: 50,  // 错误率阈值 50%
  resetTimeout: 30000,           // 熔断重置时间 30s
  name: 'api-circuit-breaker',
  rollingCountTimeout: 60000,    // 滑动窗口 60s
  rollingCountBuckets: 10,       // 滑动窗口桶数
  volumeThreshold: 5,            // 最少请求数阈值
};

const apiCircuitBreaker = new CircuitBreaker(
  (config) => apiClient(config),
  breakerOptions
);

// 熔断器事件监听 - 对接监控告警
apiCircuitBreaker.on('open', () => {
  console.warn('[CB] Circuit OPEN - 请求被熔断拒绝');
  alertManager.sendAlert('circuit_breaker_open', { service: 'api' });
});
apiCircuitBreaker.on('halfOpen', () => {
  console.info('[CB] Circuit HALF_OPEN - 发送探测请求');
});
apiCircuitBreaker.on('close', () => {
  console.info('[CB] Circuit CLOSED - 服务恢复正常');
  alertManager.resolveAlert('circuit_breaker_open', { service: 'api' });
});

// 带熔断保护的 API 调用封装
async function callApiWithProtection(config) {
  try {
    const response = await apiCircuitBreaker.fire(config);
    return response;
  } catch (error) {
    if (apiCircuitBreaker.opened) {
      // 熔断时返回降级数据
      return getDegradedResponse(config.url);
    }
    throw error;
  }
}
```


## Best Practices

> Industry-standard best practices for integrate-api execution.

1. **Practice 1**: Design resilient clients with retry and circuit breaker patterns
2. **Practice 2**: Version APIs to maintain backward compatibility
3. **Practice 3**: Document integration contracts with examples


## Error Handling

> API 集成过程中的异常处理策略与自动恢复流程，涵盖超时降级、Rate Limit 触发、认证失败三大核心场景。

### Error Scenario 1: API超时降级 (P1)

**触发条件**: 上游 API 响应时间超过配置的超时阈值（默认 30s），连续 5 次调用失败触发熔断器打开

**处理流程**:
```
IF api_response_time > timeout_threshold
   OR circuit_breaker_state = OPEN
THEN
  1. 熔断器状态切换为 OPEN，直接拒绝请求（快速失败）
  2. 返回降级响应（本地缓存数据或预配置的默认值）
  3. 触发 P1 告警通知（通知 API 负责人和值班 on-call）
  4. 启动健康检查探针，以 10s 间隔探测上游 API 恢复状态
  5. 探测成功连续 3 次后，熔断器状态切换为 HALF_OPEN，允许少量探测流量
END
```

**降级方案**: 返回本地缓存数据（TTL < 30s）或预设的默认响应；启用服务端 Mock 数据模块；限流至原流量的 20%

**升级条件**: 熔断持续时间超过 5 分钟或降级流量超过总流量的 50%，升级为 P0 事件，启动容灾切换流程

### Error Scenario 2: Rate Limit触发 (P2)

**触发条件**: 客户端请求速率超过上游 API 的 Rate Limit 配额，收到 HTTP 429 Too Many Requests 响应

**处理流程**:
```
IF http_status = 429 OR rate_limit_remaining = 0
THEN
  1. 读取响应头 Retry-After 字段，计算等待时间
  2. 请求进入本地等待队列，按指数退避策略调度重试
  3. 动态降低请求速率（滑动窗口算法），调整为原速率的 50%
  4. 记录限流日志（包含 Provider、剩余配额、重置时间戳）
  5. 如重试 3 次仍被限流，则将请求转发至备用 Provider
END
```

**降级方案**: 请求排队等待（最大排队时间 30s）；非关键请求延迟处理；切换到备用 API Provider 或降级数据源

**升级条件**: 持续限流超过 15 分钟或备用 Provider 也触发限流，升级为 P1 事件，触发流量调度

### Error Scenario 3: 认证失败重试 (P1)

**触发条件**: API 返回 HTTP 401 Unauthorized，检测到 Access Token 过期或认证凭据无效

**处理流程**:
```
IF http_status = 401 AND retry_count < max_retries
THEN
  1. 检查 Token 过期时间戳，判断是否由过期引起
  2. 主动调用 Token 刷新端点（/oauth/token），获取新的 Access Token
  3. 使用新 Token 重新发起原始请求（最多重试 2 次）
  4. 如果重试后仍返回 401，则进入认证重置流程（重新获取 Client Credentials）
  5. 触发 P1 告警，通知安全团队检查认证服务健康状况
END
```

**降级方案**: 使用本地缓存的短期 Token（若在有效期内）；切换到 Backup 认证服务 Provider；回退到 API Key 认证模式（仅限内网环境且需安全审批）

**升级条件**: Token 刷新连续失败 3 次或认证服务持续不可用超过 5 分钟，升级为 P0 事件，触发紧急认证切换流程


## Quality Standards

> Acceptance criteria and quality gates for integrate-api deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | Integration test pass rate is 95% or higher | Automated check |
| Standard 2 | All error codes have corresponding handling logic | Automated check |
| Standard 3 | API latency P99 is within SLA thresholds | Automated check |
## References

- [harness-engineering.md](../standards/harness-engineering.md)
- [output-validation-checklist.md](../evaluations/output-validation-checklist.md)
- [regression-checklist.md](../evaluations/regression-checklist.md)
