---
name: integrate-api
description: "Domain skill for integrate-api execution"
category: development
type: skill
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-23
status: active
language: "zh-CN"
tags: ['skill', 'knowledge']
---
# Skill: API 集成 (API Integration)

## Overview

本 Skill 定义了 API 集成的核心知识体系。

## Core Knowledge

### API 集成模式

#### Facade 模式

```python
class ExternalApiFacade:
    """
    外部 API 门面模式
    统一封装外部 API 差异
    """

    def __init__(self, api_client):
        self.client = api_client

    def get_user(self, user_id):
        # 转换外部 API 格式为内部格式
        response = self.client.get(f"/users/{user_id}")
        return self._transform_user(response)

    def create_order(self, order_data):
        # 转换内部格式为外部 API 格式
        external_data = self._transform_order(order_data)
        response = self.client.post("/orders", external_data)
        return self._transform_response(response)
```

#### Adapter 模式

```python
class ApiAdapter:
    """
    API 适配器
    处理不同版本的 API 差异
    """

    def __init__(self, api_version='v2'):
        self.api_version = api_version
        self.endpoints = {
            'v1': '/api/v1',
            'v2': '/api/v2'
        }

    def adapt_request(self, endpoint, data):
        """适配请求数据"""
        if self.api_version == 'v1':
            return self._adapt_to_v1(endpoint, data)
        return data

    def adapt_response(self, response):
        """适配响应数据"""
        if self.api_version == 'v1':
            return self._adapt_from_v1(response)
        return response
```

### 错误分类与处理

#### 错误分类

```yaml
error_categories:
  client_errors:
    http_codes: [400, 401, 403, 404, 422]
    retryable: false
    handling: "记录日志，返回用户提示"

  server_errors:
    http_codes: [500, 502, 503, 504]
    retryable: true
    handling: "重试，记录日志"

  network_errors:
    types: ["Timeout", "ConnectionRefused", "DNSError"]
    retryable: true
    handling: "重试，触发熔断"

  rate_limit_errors:
    http_codes: [429]
    retryable: true
    handling: "等待后重试"
```

#### 统一错误处理

```python
class ApiError(Exception):
    """API 统一错误类"""

    def __init__(self, code, message, status_code=None, details=None):
        self.code = code
        self.message = message
        self.status_code = status_code
        self.details = details or {}

    @property
    def retryable(self):
        return self.status_code in [500, 502, 503, 504, 429]


class ApiErrorHandler:
    """API 错误处理器"""

    def handle(self, error):
        if isinstance(error, ApiError):
            if error.retryable:
                return self._retry(error)
            else:
                return self._fail_fast(error)
        return self._handle_unknown(error)
```

### 数据转换

#### JSON Schema 映射

```python
class DataMapper:
    """数据映射器"""

    def __init__(self, schema_map):
        self.schema_map = schema_map

    def to_external(self, internal_data):
        """内部数据转外部格式"""
        result = {}
        for internal_key, mapping in self.schema_map.items():
            if internal_key in internal_data:
                external_key = mapping.get('external', internal_key)
                transformer = mapping.get('transform')
                value = internal_data[internal_key]

                if transformer:
                    value = transformer(value)
                result[external_key] = value
        return result

    def from_external(self, external_data):
        """外部数据转内部格式"""
        reverse_map = {v['external']: k for k, v
                       in self.schema_map.items() if 'external' in v}
        result = {}
        for external_key, value in external_data.items():
            internal_key = reverse_map.get(external_key, external_key)
            result[internal_key] = value
        return result
```

### 缓存策略

#### 多级缓存

```python
class MultiLevelCache:
    """多级缓存"""

    def __init__(self):
        self.l1_cache = LRUCache(capacity=100)  # 内存缓存
        self.l2_cache = RedisCache()             # 分布式缓存

    async def get(self, key):
        # L1 查询
        value = self.l1_cache.get(key)
        if value:
            return value

        # L2 查询
        value = await self.l2_cache.get(key)
        if value:
            self.l1_cache.set(key, value)
        return value

    async def set(self, key, value, ttl=None):
        self.l1_cache.set(key, value)
        await self.l2_cache.set(key, value, ttl)
```

### HTTP Client Patterns

#### Java: OkHttp with Retry + Circuit Breaker

```java
// Java implementation - OkHttp client with retry and circuit breaker
// Dependencies: okhttp, resilience4j (Maven/Gradle)
import okhttp3.*;
import io.github.resilience4j.circuitbreaker.CircuitBreaker;
import io.github.resilience4j.circuitbreaker.CircuitBreakerConfig;
import io.github.resilience4j.retry.Retry;
import io.github.resilience4j.retry.RetryConfig;
import java.time.Duration;
import java.util.concurrent.TimeUnit;
import java.util.function.Supplier;

public class ResilientApiClient {
    private final OkHttpClient httpClient;
    private final CircuitBreaker circuitBreaker;
    private final Retry retry;
    private final MediaType JSON = MediaType.get("application/json; charset=utf-8");

    public ResilientApiClient(String baseUrl) {
        // HTTP client with timeouts
        this.httpClient = new OkHttpClient.Builder()
            .connectTimeout(5, TimeUnit.SECONDS)
            .readTimeout(30, TimeUnit.SECONDS)
            .writeTimeout(10, TimeUnit.SECONDS)
            .addInterceptor(new RetryInterceptor(3))
            .build();

        // Circuit breaker: 50% failure rate opens circuit
        CircuitBreakerConfig cbConfig = CircuitBreakerConfig.custom()
            .failureRateThreshold(50)
            .waitDurationInOpenState(Duration.ofSeconds(30))
            .permittedNumberOfCallsInHalfOpenState(3)
            .slidingWindowSize(10)
            .build();
        this.circuitBreaker = CircuitBreaker.of("api-cb", cbConfig);

        // Retry: max 3 attempts, exponential backoff
        RetryConfig retryConfig = RetryConfig.custom()
            .maxAttempts(3)
            .waitDuration(Duration.ofMillis(500))
            .retryExceptions(IOException.class, SocketTimeoutException.class)
            .build();
        this.retry = Retry.of("api-retry", retryConfig);
    }

    public String get(String path) {
        Request request = new Request.Builder()
            .url(path)
            .header("Accept", "application/json")
            .build();

        // Decorate with circuit breaker and retry
        Supplier<String> decorated = Decorators.ofSupplier(() -> executeRequest(request))
            .withCircuitBreaker(circuitBreaker)
            .withRetry(retry)
            .decorate();

        return decorated.get();
    }

    public String post(String path, String jsonBody) {
        RequestBody body = RequestBody.create(jsonBody, JSON);
        Request request = new Request.Builder()
            .url(path)
            .post(body)
            .header("Content-Type", "application/json")
            .build();

        Supplier<String> decorated = Decorators.ofSupplier(() -> executeRequest(request))
            .withCircuitBreaker(circuitBreaker)
            .withRetry(retry)
            .decorate();

        return decorated.get();
    }

    private String executeRequest(Request request) {
        try (Response response = httpClient.newCall(request).execute()) {
            if (!response.isSuccessful()) {
                throw new IOException("Unexpected code " + response.code());
            }
            return response.body().string();
        } catch (IOException e) {
            throw new RuntimeException("API call failed", e);
        }
    }
}
```

#### Go: net/http with Context Timeout

```go
// Go implementation - net/http client with context timeout and retry
package client

import (
    "bytes"
    "context"
    "encoding/json"
    "fmt"
    "io"
    "math"
    "net/http"
    "time"
    "math/rand"
)

// Client wraps http.Client with retry and circuit breaker
type Client struct {
    baseURL    string
    httpClient *http.Client
    maxRetries int
}

type ClientOption func(*Client)

func WithTimeout(timeout time.Duration) ClientOption {
    return func(c *Client) {
        c.httpClient.Timeout = timeout
    }
}

func WithMaxRetries(n int) ClientOption {
    return func(c *Client) {
        c.maxRetries = n
    }
}

func NewClient(baseURL string, opts ...ClientOption) *Client {
    c := &Client{
        baseURL: baseURL,
        httpClient: &http.Client{
            Timeout: 30 * time.Second,
            Transport: &http.Transport{
                MaxIdleConns:        100,
                IdleConnTimeout:     90 * time.Second,
                DisableCompression:  false,
            },
        },
        maxRetries: 3,
    }
    for _, opt := range opts {
        opt(c)
    }
    return c
}

// Get performs a GET request with retry and context timeout
func (c *Client) Get(ctx context.Context, path string, result interface{}) error {
    url := c.baseURL + path
    return c.doWithRetry(ctx, func() (*http.Response, error) {
        req, err := http.NewRequestWithContext(ctx, http.MethodGet, url, nil)
        if err != nil {
            return nil, err
        }
        req.Header.Set("Accept", "application/json")
        return c.httpClient.Do(req)
    }, result)
}

// Post performs a POST request with retry and context timeout
func (c *Client) Post(ctx context.Context, path string, body, result interface{}) error {
    url := c.baseURL + path
    jsonBody, err := json.Marshal(body)
    if err != nil {
        return fmt.Errorf("marshal body: %w", err)
    }

    return c.doWithRetry(ctx, func() (*http.Response, error) {
        req, err := http.NewRequestWithContext(ctx, http.MethodPost, url, bytes.NewReader(jsonBody))
        if err != nil {
            return nil, err
        }
        req.Header.Set("Content-Type", "application/json")
        req.Header.Set("Accept", "application/json")
        return c.httpClient.Do(req)
    }, result)
}

// doWithRetry executes an HTTP request with exponential backoff retry
func (c *Client) doWithRetry(ctx context.Context, do func() (*http.Response, error), result interface{}) error {
    var lastErr error

    for attempt := 0; attempt <= c.maxRetries; attempt++ {
        resp, err := do()
        if err != nil {
            lastErr = fmt.Errorf("request failed: %w", err)
            if !c.isRetryable(err) {
                return lastErr
            }
            c.backoff(attempt)
            continue
        }
        defer resp.Body.Close()

        // Non-retryable status codes
        if resp.StatusCode == http.StatusBadRequest ||
            resp.StatusCode == http.StatusUnauthorized ||
            resp.StatusCode == http.StatusForbidden ||
            resp.StatusCode == http.StatusNotFound {
            body, _ := io.ReadAll(resp.Body)
            return fmt.Errorf("api error [%d]: %s", resp.StatusCode, string(body))
        }

        // Retryable server errors
        if resp.StatusCode >= 500 || resp.StatusCode == http.StatusTooManyRequests {
            lastErr = fmt.Errorf("server error: %d", resp.StatusCode)
            c.backoff(attempt)
            continue
        }

        // Success
        if result != nil {
            if err := json.NewDecoder(resp.Body).Decode(result); err != nil {
                return fmt.Errorf("decode response: %w", err)
            }
        }
        return nil
    }
    return fmt.Errorf("max retries exceeded: %w", lastErr)
}

func (c *Client) isRetryable(err error) bool {
    // Context canceled or deadline exceeded are not retryable
    if err == context.Canceled || err == context.DeadlineExceeded {
        return false
    }
    return true
}

func (c *Client) backoff(attempt int) {
    // Exponential backoff with jitter: 500ms, 1s, 2s
    wait := time.Duration(math.Pow(2, float64(attempt))) * 500 * time.Millisecond
    jitter := time.Duration(rand.Int63n(int64(wait) / 2))
    time.Sleep(wait + jitter)
}
```

#### Node.js: Axios with Retry Interceptor

```javascript
// Node.js implementation - Axios HTTP client with retry interceptor
// Dependencies: axios, axios-retry (npm install axios axios-retry)
const axios = require('axios');
const axiosRetry = require('axios-retry').default;

class ApiClient {
    constructor(baseURL, options = {}) {
        this.client = axios.create({
            baseURL,
            timeout: options.timeout || 30000,
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            },
            // Connection pooling via http.Agent
            ...(options.maxSockets && {
                httpAgent: new (require('http').Agent)({
                    keepAlive: true,
                    maxSockets: options.maxSockets || 50,
                }),
                httpsAgent: new (require('https').Agent)({
                    keepAlive: true,
                    maxSockets: options.maxSockets || 50,
                }),
            }),
        });

        // Configure retry with exponential backoff
        axiosRetry(this.client, {
            retries: options.retries || 3,
            retryDelay: (retryCount) => {
                return axiosRetry.exponentialDelay(retryCount);
            },
            retryCondition: (error) => {
                // Retry on network errors and 5xx status codes
                return axiosRetry.isNetworkOrIdempotentRequestError(error)
                    || error.response?.status >= 500
                    || error.response?.status === 429;
            },
            onRetry: (retryCount, error, requestConfig) => {
                console.warn(`[API] Retry ${retryCount}/${options.retries} for ${requestConfig.url}: ${error.message}`);
            },
        });

        // Request interceptor: add correlation ID
        this.client.interceptors.request.use((config) => {
            config.headers['X-Correlation-Id'] = require('crypto').randomUUID();
            return config;
        });

        // Response interceptor: unified error handling
        this.client.interceptors.response.use(
            (response) => response,
            (error) => {
                if (error.response) {
                    const { status, data } = error.response;
                    const apiError = new Error(data?.message || `HTTP ${status}`);
                    apiError.status = status;
                    apiError.code = data?.code;
                    apiError.details = data;
                    return Promise.reject(apiError);
                }
                return Promise.reject(error);
            }
        );
    }

    async get(path, params = {}) {
        const response = await this.client.get(path, { params });
        return response.data;
    }

    async post(path, data = {}) {
        const response = await this.client.post(path, data);
        return response.data;
    }

    async put(path, data = {}) {
        const response = await this.client.put(path, data);
        return response.data;
    }

    async delete(path) {
        const response = await this.client.delete(path);
        return response.data;
    }

    // Circuit breaker wrapper
    withCircuitBreaker(options = {}) {
        const CircuitBreaker = require('opossum');
        const breaker = new CircuitBreaker(async (method, ...args) => {
            return this[method](...args);
        }, {
            timeout: options.timeout || 10000,
            errorThresholdPercentage: options.errorThreshold || 50,
            resetTimeout: options.resetTimeout || 30000,
            name: options.name || 'api-cb',
        });

        breaker.fallback(() => {
            console.warn('[CircuitBreaker] Fallback triggered, using cached/default response');
            return options.fallbackResponse || null;
        });

        breaker.on('open', () => console.warn('[CircuitBreaker] Circuit opened'));
        breaker.on('halfOpen', () => console.warn('[CircuitBreaker] Circuit half-open'));
        breaker.on('close', () => console.warn('[CircuitBreaker] Circuit closed'));

        return breaker;
    }
}

// Usage
const client = new ApiClient('https://api.example.com', {
    timeout: 15000,
    retries: 3,
    maxSockets: 50,
});

const data = await client.get('/users/123');
console.log(data);
```

## Best Practices

### API 设计原则

1. **面向失败设计**
   - 假设 API 调用会失败
   - 实现重试和降级
   - 记录详细错误日志

2. **超时控制**
   - 设置合理的超时时间
   - 不设置无限等待
   - 超时时正确处理

3. **幂等性**
   - POST 请求尽量幂等
   - 使用唯一请求 ID
   - 支持重试

4. **监控告警**
   - 记录关键指标
   - 设置告警阈值
   - 定期分析错误趋势

## Toolchain

### API 开发工具

| 工具 | 用途 |
|------|------|
| Postman | API 测试 |
| Insomnia | API 测试 |
| Swagger Editor | API 设计 |
| Stoplight | API 设计 |

### 监控工具

| 工具 | 用途 |
|------|------|
| Datadog | API 监控 |
| New Relic | APM |
| Sentry | 错误追踪 |

## Associated Assets

- **Scenario**: `../../scenarios/integrate-api/SCENARIO.md`
- **Instruction**: `../../instructions/integrate-api.instructions.md`
- **Prompt**: `../../prompts/integrate-api.prompt.md`
- **Agent**: `../../agents/integrate-api.agent.md`


## Core Knowledge

> Essential knowledge domain for integrate-api execution.

### Domain Fundamentals
- **API Gateway 模式**: 通过统一网关入口管理认证、限流、路由和协议转换，简化客户端与服务端的交互复杂度。
- **Circuit Breaker (断路器)**: 防止级联故障的关键模式，当下游服务故障率达到阈值时自动切断调用，保护系统稳定性。
- **Bulkhead (舱壁隔离)**: 将资源池分隔为独立分区，避免某个依赖的故障耗尽所有线程/连接资源，影响其他正常服务。

### Key Principles
1. **集成契约测试先行**: 在实现集成代码之前先编写契约测试，确保 API 提供方和消费方对接口约定达成一致。
2. **超时必有降级**: 所有外部 API 调用必须设置超时时间且提供降级方案，不允许无限等待或直接透传失败。
3. **幂等性设计**: API 集成中消费方应支持幂等重试，提供方应通过幂等令牌确保重复请求不产生副作用。


## Best Practices

> Proven practices for integrate-api excellence.

1. **Retry with Backoff (指数退避重试)**: 对可重试的失败（网络超时、5xx）使用指数退避 + 抖动策略重试，避免重试风暴进一步压垮下游。
2. **分布式追踪传播**: 在 API 调用链中透传 Trace ID 和 Span ID，实现端到端链路追踪，快速定位故障点。
3. **HATEOAS 自描述 API**: 响应中携带关联资源的链接，客户端通过链接导航而非硬编码 URL，降低客户端与服务器端的耦合度。


## Anti-patterns (反模式)

> 与 Common Pitfalls 同义，执行时合并检查。

## Common Pitfalls

> Frequent mistakes to avoid during integrate-api execution.

### Pitfall 1: 无视 API Rate Limit (Ignoring Rate Limits)
**Risk**: 超过 API 提供方的速率限制，触发限流策略导致请求被拒绝，服务中断。
**Prevention**: 集成代码中实现本地速率限制（Token Bucket 算法），监控响应头中的 RateLimit 信息。
**Impact**: API 调用持续失败，业务功能降级或完全不可用，可能被提供方加入黑名单。

### Pitfall 2: 同步调用链路过长 (Excessive Sync Call Chain)
**Risk**: 一个请求端到端同步调用多个外部 API，总延迟等于各调用延迟之和，用户体验差且故障面扩大。
**Prevention**: 将非关键路径的同步调用改为异步（消息队列），关键路径控制在 2-3 跳以内。
**Impact**: API 响应时间长达数秒，用户频繁超时重试，系统负载成倍增加。

### Pitfall 3: 错误吞没无告警 (Silent Error Swallowing)
**Risk**: 捕获异常后仅记录日志不告警，或使用空 catch 块，导致故障长期未被发现。
**Prevention**: 定义清晰的错误分类和处理策略，关键错误通过告警系统实时通知，设置错误率告警阈值。
**Impact**: 系统在降级状态下运行数天甚至数周，数据不一致性累积，修复成本极高。
