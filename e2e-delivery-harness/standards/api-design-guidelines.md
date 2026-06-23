---
name: api-design-guidelines
type: standard
version: "2.0.0"
status: active
---

# API 设计规范

> 本规范定义 E2E Delivery Harness 中所有公开/内部 API 的设计标准，涵盖 RESTful 约定、版本管理、错误格式与限流。审查基准见 [harness-engineering.md](harness-engineering.md)。

## 1. RESTful 设计约定

### 1.1 URL 命名规范

| 资源 | URL 模式 | HTTP 方法 | 说明 |
|------|----------|-----------|------|
| **集合** | `/api/v1/orders` | GET | 查询订单列表 |
| **单个资源** | `/api/v1/orders/{id}` | GET | 查询单个订单 |
| **创建** | `/api/v1/orders` | POST | 创建新订单 |
| **更新** | `/api/v1/orders/{id}` | PUT | 全量更新订单 |
| **部分更新** | `/api/v1/orders/{id}` | PATCH | 部分字段更新 |
| **删除** | `/api/v1/orders/{id}` | DELETE | 删除订单（逻辑删除优先） |
| **子资源** | `/api/v1/orders/{id}/items` | GET | 订单包含的商品 |
| **操作** | `/api/v1/orders/{id}/cancel` | POST | 执行特定操作（动词结尾） |

### 1.2 命名规则

- **全部小写**: `/api/v1/user-profiles` ✅, `/api/v1/userProfiles` ❌
- **kebab-case**: `/api/v1/order-items` ✅, `/api/v1/orderItems` ❌, `/api/v1/order_items` ❌
- **复数名词**: `/api/v1/users` ✅, `/api/v1/user` ❌
- **扁平 ≤ 3 级**: `/api/v1/a/b/c` ✅, `/api/v1/a/b/c/d/e` ❌
- **动词仅在操作资源时**: `/api/v1/orders/{id}/refund` ✅, `/api/v1/getOrder` ❌

### 1.3 HTTP 方法语义

| 方法 | 幂等性 | 安全性 | 缓存性 | Body 说明 |
|------|--------|--------|--------|-----------|
| GET | 是 | 是 | 是 | 无 Body |
| POST | 否 | 否 | 否 | 创建/操作参数 |
| PUT | 是 | 否 | 否 | 全量资源 |
| PATCH | 否 | 否 | 否 | 变更字段集 |
| DELETE | 是 | 否 | 否 | 无 Body（或可选） |

## 2. 版本管理 (Versioning)

### 2.1 版本策略

| 策略 | 推荐度 | 说明 | 示例 |
|------|--------|------|------|
| **URL 路径** | 推荐 | 最清晰，适用于公共 API | `/api/v1/orders`, `/api/v2/orders` |
| **请求 Header** | 可接受 | 用于内部 API 或特定场景 | `Accept: application/vnd.harness.v1+json` |
| **Query 参数** | 不推荐 | 容易被忽略，Caching 困难 | `/api/orders?version=1` |

### 2.2 版本声明周期

```
v1.0 (GA) ── v1.1 (小功能增强) ── v1.2 (小功能增强) ── v1.3 (deprecated) ── v1 removed
v2.0 (GA) ──────────────────────────────────────────────────────────────────────────
```

| 阶段 | 行为 | 维护要求 | 持续时间 |
|------|------|----------|----------|
| **GA** | 正式发布 | 全量支持 | 从 GA 起 ≥ 12 个月 |
| **Deprecated** | 仍可用，返回 Warning Header | 仅修复安全漏洞 | ≥ 6 个月 |
| **Removed** | 返回 410 Gone | 无 | — |

停用通知: `Sunset: Sat, 30 Jun 2027 00:00:00 GMT` + `Warning: 299 - "v1 will be removed on 2027-06-30"`

### 2.3 向后兼容性要求

- 新增字段：允许（客户端忽略不认识的字段）
- 移除字段：必须发版 deprecation 通知（大版本移除）
- 修改字段类型：禁止（必须新增字段+大版本）
- 修改枚举值：允许新增值，禁止删除/重命名已有值
- 修改 URL：支持旧 URL 重定向 301/308

## 3. 错误响应格式 (Error Response Format)

### 3.1 标准错误响应

```json
{
  "error": {
    "code": "ORDER_NOT_FOUND",
    "message": "Order with ID 'ord_abc123' not found",
    "details": {
      "order_id": "ord_abc123",
      "field": "id"
    },
    "request_id": "req_xyz789",
    "timestamp": "2026-06-23T10:30:00Z",
    "status": 404
  }
}
```

### 3.2 HTTP 状态码使用

| 范围 | 使用场景 | 状态码说明 |
|------|----------|-----------|
| **2xx** | 成功 | 200 (OK), 201 (Created), 202 (Accepted), 204 (No Content) |
| **4xx** | 客户端错误 | 400 (Bad Request), 401 (Unauthorized), 403 (Forbidden), 404 (Not Found), 409 (Conflict), 422 (Unprocessable Entity), 429 (Too Many Requests) |
| **5xx** | 服务端错误 | 500 (Internal Server Error), 502 (Bad Gateway), 503 (Service Unavailable), 504 (Gateway Timeout) |

**状态码使用原则**:
- 400: 请求体校验失败
- 401: 缺少或无效认证凭据
- 403: 认证通过但无权限
- 404: 资源不存在（不暴露资源是否存在）
- 409: 资源冲突（重复创建、版本冲突）
- 422: 业务语义错误（库存不足、余额不够）
- 429: 限流触发，必须包含 `Retry-After` header
- 500: 未预期的服务内部错误
- 503: 服务负载过高或正在维护

### 3.3 错误码命名规范

`<DOMAIN>_<ERROR_TYPE>` (UPPER_SNAKE_CASE):

| 域 (Domain) | 示例 |
|-------------|------|
| `VALIDATION_` | `VALIDATION_REQUIRED_FIELD`, `VALIDATION_INVALID_FORMAT` |
| `AUTH_` | `AUTH_TOKEN_EXPIRED`, `AUTH_UNAUTHORIZED` |
| `BUSINESS_` | `BUSINESS_INSUFFICIENT_BALANCE`, `BUSINESS_ORDER_ALREADY_PAID` |
| `SYSTEM_` | `SYSTEM_INTERNAL_ERROR`, `SYSTEM_DEPENDENCY_UNAVAILABLE` |
| `RATE_LIMIT_` | `RATE_LIMIT_EXCEEDED` |

## 4. 限流策略 (Rate Limiting)

### 4.1 限流级别

| 级别 | 窗口 | 默认限制 | 适用 API |
|------|------|----------|----------|
| **Global** | 1 秒 | 10,000 请求/s | 全局 API gateway 级别 |
| **Per User** | 1 分钟 | 100 请求/min | 用户级别 API |
| **Per IP** | 1 小时 | 500 请求/h | 匿名/公共端点 |
| **Per Endpoint** | 1 秒 | 50 请求/s | 高负载端点（搜索、批量） |

### 4.2 限流响应

```http
HTTP/1.1 429 Too Many Requests
Content-Type: application/json
Retry-After: 30
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1687500000
```

```json
{
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Rate limit exceeded. Retry after 30 seconds.",
    "details": {
      "limit": 100,
      "remaining": 0,
      "reset_at": "2026-06-23T10:30:30Z"
    },
    "request_id": "req_xyz789",
    "timestamp": "2026-06-23T10:30:00Z",
    "status": 429
  }
}
```

### 4.3 限流 Header 规范

| Header | 说明 | 必填 |
|--------|------|------|
| `X-RateLimit-Limit` | 窗口内最大请求数 | 是 |
| `X-RateLimit-Remaining` | 当前窗口剩余请求数 | 是 |
| `X-RateLimit-Reset` | 窗口重置的 Unix 时间戳 | 是 |
| `Retry-After` | 限流后客户端应等待的秒数 | 429 时必填 |

## 5. 分页规范 (Pagination)

### 5.1 Cursor-based 分页（推荐）

```http
GET /api/v1/orders?cursor=eyJpZCI6IjEyMyJ9&limit=20
```

```json
{
  "data": [ ... ],
  "pagination": {
    "next_cursor": "eyJpZCI6IjE0MyJ9",
    "has_more": true,
    "limit": 20
  }
}
```

### 5.2 Offset-based 分页（备选）

```http
GET /api/v1/orders?offset=0&limit=20
```

```json
{
  "data": [ ... ],
  "pagination": {
    "offset": 0,
    "limit": 20,
    "total": 156,
    "has_more": true
  }
}
```

**规则**:
- 默认 `limit = 20`, 最大 `limit = 100`（超限视为 100）
- 超出最大 limit 返回 400 或自动截断
- 分页参数对所有 GET 集合端点一致

## 6. 请求/响应规范

### 6.1 标准 Header

| Header | 必填 | 说明 |
|--------|------|------|
| `Content-Type` | 是 | `application/json` |
| `Accept` | 是 | `application/json` 或版本化 media type |
| `Authorization` | 认证时必填 | `Bearer <token>` |
| `X-Request-Id` | 推荐 | 客户端生成请求 ID，用于链路追踪 |
| `X-Idempotency-Key` | 创建操作推荐 | 幂等性保证，key 有效期 24h |

### 6.2 字段命名

- JSON 字段使用 **camelCase**: `orderId` ✅, `order_id` ❌, `OrderId` ❌
- 日期使用 **ISO 8601**: `2026-06-23T10:30:00Z`
- 枚举使用 **UPPER_SNAKE_CASE**: `STATUS_PAID`, `STATUS_PENDING`
- 货币使用 ISO 4217: `currency: "USD"`, `amount: 1999` (单位: 分/最小单位)

## 引用

- [asset-model.md](asset-model.md)
- [authoring-checklist.md](authoring-checklist.md)
- [coding-standards.md](coding-standards.md)
- [testing-guidelines.md](testing-guidelines.md)
