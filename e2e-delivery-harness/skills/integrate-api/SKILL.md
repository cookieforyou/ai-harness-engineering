---
name: integrate-api
description: "Domain skill for integrate-api execution"
category: development
type: skill
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
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
- [Core concept 1]
- [Core concept 2]
- [Core concept 3]

### Key Principles
1. [Principle 1]
2. [Principle 2]
3. [Principle 3]


## Best Practices

> Proven practices for integrate-api excellence.

1. **Practice 1**: [Description and rationale]
2. **Practice 2**: [Description and rationale]
3. **Practice 3**: [Description and rationale]


## Anti-patterns (反模式)

> 与 Common Pitfalls 同义，执行时合并检查。

## Common Pitfalls

> Frequent mistakes to avoid during integrate-api execution.

### Pitfall 1: [Name]
**Risk**: [Description]
**Prevention**: [How to avoid]
**Impact**: [Consequences if not avoided]

### Pitfall 2: [Name]
**Risk**: [Description]
**Prevention**: [How to avoid]
**Impact**: [Consequences if not avoided]

### Pitfall 3: [Name]
**Risk**: [Description]
**Prevention**: [How to avoid]
**Impact**: [Consequences if not avoided]
