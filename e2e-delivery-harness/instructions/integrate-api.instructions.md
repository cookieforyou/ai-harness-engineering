# Instructions: API 集成 (Integrate API)

## 认证方式规范

### 认证类型对比

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

## 重试策略规范

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

## 限流策略规范

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

## 熔断器规范

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

## 日志与监控规范

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
