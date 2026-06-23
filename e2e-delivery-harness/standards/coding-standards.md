---
name: coding-standards
type: standard
version: "2.0.0"
status: active
---

# 编码规范

> 本规范定义 E2E Delivery Harness 中所有代码资产的编写标准，涵盖命名、组织、错误处理、日志与代码审查。审查基准见 [harness-engineering.md](harness-engineering.md)。

## 1. 命名规范 (Naming Conventions)

### 1.1 通用规则

| 实体 | 风格 | 示例 | 说明 |
|------|------|------|------|
| **类/类型/接口** | PascalCase | `PaymentProcessor`, `UserService` | 名词或名词短语 |
| **函数/方法** | camelCase | `processPayment()`, `getUserById()` | 动词或动词+名词 |
| **变量/参数** | camelCase | `userName`, `paymentAmount` | 有意义的名词短语 |
| **常量** | UPPER_SNAKE_CASE | `MAX_RETRY_COUNT`, `DEFAULT_TIMEOUT` | 编译期不可变值 |
| **枚举** | PascalCase 值 + UPPER_SNAKE_CASE 成员 | `enum Color { RED, GREEN, BLUE }` | 类型大写，成员大写 |
| **文件/目录** | kebab-case | `payment-service.ts`, `user-profile/` | 小写字母 + 连字符 |
| **环境变量** | UPPER_SNAKE_CASE | `DB_CONNECTION_STRING` | 前缀加服务名 |

### 1.2 语义命名原则

- **不要缩写**: `usrName` → `userName`, `cfg` → `config`, `btn` → `button`
- **标准缩写保留**: `id`, `url`, `html`, `http`, `db`（全小写或按语境）
- **布尔变量**: `is`, `has`, `should`, `can` 前缀 — `isActive`, `hasPermission`, `shouldRetry`
- **集合/数组**: 复数形式 — `users`, `orderList`, `itemSet`
- **Map/Dict**: `userMap` 或 `userById`（表明键值含义）
- **临时变量**: `i`, `j` 仅限循环索引；临时结果用 `result`, `tmp` 需附带注释说明

### 1.3 命名反模式

- ❌ 拼音缩写 (`szData`, `ysData`)
- ❌ 单字母变量（除循环索引、坐标 `x/y`、数学运算）
- ❌ 类型前缀 (`strName`, `intCount`, `arrItems`) — 类型由语言/IDE 管理
- ❌ 命名与类型冲突 (`order = Order()` 改为 `newOrder` 或 `orderInstance`)
- ❌ 过于通用 (`data`, `info`, `temp`, `stuff`)

## 2. 代码组织 (Code Organization)

### 2.1 项目目录结构

```
src/
├── core/                    # 核心业务逻辑（无框架依赖）
│   ├── domain/              # 领域模型 / 实体
│   ├── ports/               # 接口定义（依赖倒置）
│   └── services/            # 业务服务实现
├── infra/                   # 基础设施实现（DB、消息队列、外部 API）
│   ├── persistence/         # 数据库 repository 实现
│   ├── messaging/           # 消息队列 producer/consumer
│   └── http/                # HTTP 客户端/服务端实现
├── api/                     # API 层（Controller / Handler / Resolver）
│   ├── routes/              # 路由定义
│   ├── middleware/          # 中间件（auth, rate-limit, logging）
│   └── validators/          # 请求校验
├── config/                  # 配置读取、环境变量绑定
└── shared/                  # 跨模块共享的工具函数、常量、类型
```

### 2.2 包/模块职责

- **单一职责**: 每个文件/模块只做一件事，文件行数 ≤ 500
- **依赖方向**: 外层可依赖内层，内层不依赖外层（依赖倒置原则）
- **循环依赖**: 严格禁止。使用接口抽象或事件总线解耦
- **公共 API**: 模块内用 `index.ts` / `__init__.py` 导出公共接口，隐藏内部实现

### 2.3 文件组织规则

- 一个文件一个主要类型（class/component），辅助类型不超过 3 个
- 文件内顺序：imports → 类型定义 → 常量 → 主逻辑 → helper 函数
- 文件末尾空行；import 按类别分组（标准库/第三方/内部），组间空行分隔

## 3. 错误处理模式 (Error Handling Patterns)

### 3.1 错误分类与响应

| 错误类别 | HTTP 等价 | 处理策略 | 日志级别 |
|----------|-----------|----------|----------|
| **验证错误 (Validation)** | 400 | 返回结构化错误信息 | WARN |
| **认证/授权错误 (Auth)** | 401/403 | 重定向或拒绝，不暴露细节 | WARN |
| **未找到 (Not Found)** | 404 | 返回标准 Not Found 响应 | INFO |
| **业务冲突 (Conflict)** | 409 | 返回冲突原因 + 当前状态 | WARN |
| **限流 (Rate Limited)** | 429 | 返回 Retry-After header | WARN |
| **内部错误 (Internal)** | 500 | 返回通用错误，记录完整堆栈 | ERROR |
| **依赖超时/不可用** | 502/503 | 返回 CircuitBreaker 状态 | ERROR |

### 3.2 异常处理原则

- **不要吞异常**: 空 catch 块禁止。至少记录 WARN 级别日志
- **不要重复包裹**: 不需要在每一层都 wrap 同一异常
- **面向调用方错误**: 底层抛技术异常，上层转为业务异常
- **自定义异常**: 继承标准异常，包含 error code、message、source
- **全局处理器**: 框架层统一捕获未处理异常，返回标准错误响应

### 3.3 错误响应格式

```json
{
  "error": {
    "code": "PAYMENT_TIMEOUT",
    "message": "Payment processing timed out after 30s",
    "details": { "transactionId": "txn_abc123", "retryable": true },
    "requestId": "req_xyz789",
    "timestamp": "2026-06-23T10:30:00Z"
  }
}
```

### 3.4 重试策略

| 可重试条件 | 重试间隔 | 最大次数 | 退避策略 |
|------------|----------|----------|----------|
| 网络超时 / 5xx | 100ms → 200ms → 400ms | 3 | 指数退避 + Jitter |
| 限流 (429) | Retry-After header | 2 | 按header值 |
| 数据库死锁 (40P1) | 随机 100-500ms | 3 | 随机退避 |
| 4xx (非429) | 不重试 | 0 | 直接返回 |

## 4. 日志标准 (Logging Standards)

### 4.1 日志级别定义

| 级别 | 含义 | 示例 | 输出目标 |
|------|------|------|----------|
| **DEBUG** | 调试信息，仅开发用 | SQL 语句、变量值 | 本地 stdout (默认关闭) |
| **INFO** | 正常流程记录 | 请求开始/结束、状态转换 | stdout / 日志平台 |
| **WARN** | 异常但可恢复 | 重试、降级、超时、熔断触发 | stdout + 告警平台 (条件) |
| **ERROR** | 功能受损，需人工关注 | 调用失败、数据不一致 | stdout + 告警平台 |
| **FATAL** | 系统不可用 | 启动失败、严重配置错误 | stdout + P0 电话告警 |

### 4.2 日志内容规范

- **结构化日志**: JSON 格式，禁止字符串拼接
```json
{"level":"ERROR","ts":"2026-06-23T10:30:00Z","msg":"Payment failed","txn_id":"txn_abc","error":"timeout","duration_ms":30000}
```
- **必填字段**: `level`, `ts`, `msg`, `service`, `trace_id`
- **禁止记录**: 密码、token、PII（姓名、手机号、身份证号）
- **上下文**: 请求级别的 `trace_id` 贯穿所有日志，关联上下游调用

### 4.3 日志反模式

- ❌ `System.out.println` / `console.log` 直接输出（日志框架接管）
- ❌ 在循环中打印 DEBUG 日志（可能导致日志爆炸）
- ❌ 日志中包含敏感信息（即使脱敏也要确认）
- ❌ 无 `trace_id` 的游离日志（无法关联请求上下文）
- ❌ ERROR 级别中没有异常堆栈或关键参数

## 5. 代码审查清单 (Code Review Checklist)

### 5.1 功能性 (Functionality)

- [ ] 代码是否实现了所有需求？有没有遗漏边界情况
- [ ] 错误处理是否覆盖合理路径与异常路径
- [ ] 并发/竞态条件下是否线程安全
- [ ] 是否有硬编码值需要替换为配置项

### 5.2 可维护性 (Maintainability)

- [ ] 命名是否清晰表达意图
- [ ] 函数/方法是否过长（建议 ≤ 40 行，单方法 ≤ 100 行）
- [ ] 是否有重复代码可以提取抽象
- [ ] 注释是否必要而不是多余（代码自解释优先）
- [ ] 测试是否覆盖了新代码的各个分支

### 5.3 安全性 (Security)

- [ ] 用户输入是否经过校验/清理（XSS/SQL 注入/SSTI）
- [ ] 认证/授权是否在正确层级执行（不信任前端传入的权限）
- [ ] 敏感信息是否可被日志泄露
- [ ] 是否对批量 API 做了限流/分页保护

### 5.4 性能 (Performance)

- [ ] N+1 查询问题是否避免（数据加载是否批量/Batched）
- [ ] 长列表是否有分页或流式处理
- [ ] 是否有不必要的序列化/反序列化
- [ ] 锁粒度是否合理（表锁 vs 行锁 vs 乐观锁）

### 5.5 可靠性 (Reliability)

- [ ] 外部调用是否有超时设置（无默认 infinite）
- [ ] 是否使用 Circuit Breaker / Bulkhead 模式保护依赖
- [ ] 重试是否有退避策略（防止 thundering herd）
- [ ] 数据一致性是否通过事务或 Saga 保证

## 引用

- [asset-model.md](asset-model.md)
- [authoring-checklist.md](authoring-checklist.md)
- [code-review-checklist.md](code-review-checklist.md)
- [testing-guidelines.md](testing-guidelines.md)
