---
name: api-doc
type: deliverable-template
version: "1.0.0"
status: active
language: "zh-CN"
---

# API 文档 模板

> 复制本模板到 `docs/` 对应路径，由 Agent 按 [standards/harness-engineering.md](../standards/harness-engineering.md) 填充。

## 元数据

- 项目: {project_name}
- 版本: {version}
- 作者: {author}
- 日期: {ISO8601}

## 正文

## API 概览

- **基础 URL**: `{base_url}`
- **API 版本**: `{api_version}`
- **协议**: HTTPS
- **数据格式**: JSON
- **字符编码**: UTF-8

## 认证

### 认证方式

- **认证类型**: {Bearer Token / API Key / OAuth2 / Basic Auth}
- **获取方式**: {获取凭证的途径}
- **凭证格式**: `{Authorization: Bearer {token}}`
- **过期时间**: {token 过期策略}

### 错误响应格式

```json
{
  "code": "{error_code}",
  "message": "{error_message}",
  "request_id": "{request_id}",
  "timestamp": "{ISO8601}"
}
```

## 错误码

| HTTP 状态码 | 错误码 | 含义 | 处理建议 |
|-------------|--------|------|----------|
| 400 | BAD_REQUEST | 请求参数错误 | 检查请求参数 |
| 401 | UNAUTHORIZED | 未认证 | 检查认证凭证 |
| 403 | FORBIDDEN | 无权限 | 检查访问权限 |
| 404 | NOT_FOUND | 资源不存在 | 检查资源路径 |
| 409 | CONFLICT | 资源冲突 | 处理冲突条件 |
| 422 | UNPROCESSABLE | 请求语义错误 | 检查请求体格式 |
| 429 | RATE_LIMITED | 请求频率超限 | 降低请求频率 |
| 500 | INTERNAL_ERROR | 服务器内部错误 | 重试或联系运维 |
| 503 | SERVICE_UNAVAILABLE | 服务暂不可用 | 稍后重试 |

## 速率限制

- **限制策略**: {如: Token Bucket / Sliding Window}
- **默认限制**: {rate} 请求/{time_window}
- **超出处理**: {HTTP 429 + Retry-After 头}
- **特殊限制**: {特殊限制说明}

## 接口列表

### {Module Name}

#### {接口名称}

**Endpoint**: `{method} {/api/v1/resource}`
**功能描述**: {简要描述接口功能}

**Request 参数**:

| 参数名 | 位置 | 类型 | 必填 | 默认值 | 描述 | 校验规则 |
|--------|------|------|------|--------|------|----------|
| {param} | path/query/body | string/number | true/false | {default} | {description} | {validation} |

**Request 示例**:

```bash
curl -X {method} {base_url}/api/v1/resource \
  -H "Authorization: Bearer {token}" \
  -H "Content-Type: application/json" \
  -d '{...}'
```

**Response 示例**:

```json
{
  "code": 200,
  "data": {},
  "message": "success"
}
```

**Response 字段说明**:

| 字段名 | 类型 | 必含 | 描述 |
|--------|------|------|------|
| {field} | string/number | true/false | {description} |

**业务规则**:
- {业务规则1}
- {业务规则2}

## API 版本管理

### 版本策略

- **版本格式**: `v{major}` (如 v1, v2)
- **版本传递方式**: URL 路径 / Header
- **兼容性保证**: {兼容性策略}
- **废弃策略**: {API deprecated 流程}

## 修订历史

| 版本 | 日期 | 作者 | 变更内容 | 评审人 |
|------|------|------|----------|--------|
| v1.0 | {ISO8601} | {author} | 初稿 | {reviewer} |

## 验证

- [ ] 已通过 [evaluations/output-validation-checklist.md](../evaluations/output-validation-checklist.md)
