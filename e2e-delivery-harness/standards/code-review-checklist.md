---
name: code-review-checklist
description: "代码审查清单标准，定义分层代码审查流程、通用审查项、安全审查和性能审查规范"
type: standard
version: "2.0.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-23
status: active
language: "zh-CN"
tags: ['standard', 'code-review', 'quality', 'security']
---

# 代码审查清单

> 本规范提供 E2E Delivery Harness 中代码审查的分层检查项，涵盖语言通用项、安全、性能与特定语言要点。审查基准见 [harness-engineering.md](../harness-engineering.md)。详细编码规范见 [coding-standards.md](../standards/coding-standards.md)。

## 1. 代码审查通用流程

### 1.1 审查者时间预估

| PR 大小 | 预计审查时间 | 建议 |
|---------|-------------|------|
| ≤ 100 行 | 10-15 分钟 | 逐行审查 |
| 100-300 行 | 15-30 分钟 | 关注核心逻辑 |
| 300-500 行 | 30-45 分钟 | 要求拆分或重点审查 |
| > 500 行 | > 45 分钟 | 建议拆分为多个 PR |

### 1.2 审查阶段

```
Phase 1: 全局理解 (2 min)
  ├── 阅读 PR 描述，理解变更目的
  ├── 确认是否关联了 Issue/Ticket
  └── 快速浏览变更文件列表

Phase 2: 逐项检查 (核心)
  ├── 按以下清单逐项检查
  ├── 高影响区域优先（数据、安全、API）
  └── 标注阻塞性问题 (Blocking) 和建议性意见 (Nit)

Phase 3: 反馈提交
  ├── 总结 3 个最关键的问题
  ├── 区分 Blocking 和 Nit
  └── 在 GitHub/GitLab 使用 Suggestion 功能
```

## 2. 通用代码审查项 (Language-agnostic)

### 2.1 设计

- [ ] 代码是否符合 SOLID 原则（尤其是 SRP 和 DIP）？
- [ ] 是否存在过度设计（YOAGNI — You Ain't Gonna Need It）？
- [ ] 模块/类之间的耦合是否合理？
- [ ] 是否引入了循环依赖？
- [ ] 抽象层是否合理（是否泄漏实现细节）？

### 2.2 正确性

- [ ] 边界条件是否处理？（空集合、null/undefined、超长字符串、负数）
- [ ] 并发操作是否有竞态条件？（共享状态是否线程安全）
- [ ] 数据转换/序列化是否有精度损失或溢出风险？
- [ ] 正则表达式是否有 ReDoS 风险（避免使用用户输入构造正则）？
- [ ] 时间处理是否使用时区感知（时区 + UTC 转换）？

### 2.3 可读性

- [ ] 变量/函数命名是否清晰表达意图？（参见 coding-standards.md）
- [ ] 函数是否过长？（建议 ≤ 40 行，单屏幕可见）
- [ ] 注释是 "为什么" 而不是 "是什么"？（代码自解释优先）
- [ ] 是否存在魔法数字/字符串需要命名常量？
- [ ] 条件逻辑的嵌套深度是否 ≤ 3 层？

### 2.4 可测试性

- [ ] 新增代码是否可单元测试（依赖注入/接口抽象）？
- [ ] 是否有测试覆盖了新逻辑？（不少于 80% 覆盖率）
- [ ] 测试是否关注行为而不是实现方式？
- [ ] 是否存在无法测试的代码（静态方法、硬编码依赖、全局状态）？

## 3. 安全审查点 (Security Review Points)

### 3.1 OWASP Top 10 检查

- [ ] **注入**: 用户输入是否经过参数化查询 / ORM 安全 API？（SQL/NoSQL/OS 命令注入）
- [ ] **XSS**: 用户输出是否经过转义？（反映型/存储型/ DOM 型 XSS）
- [ ] **认证**: 密码/Token 是否安全存储？认证绕过风险？
- [ ] **授权**: API 端点是否有权限校验（不只是前端隐藏按钮）？
- [ ] **敏感数据**: 日志中是否避免输出密码、Token、PII？
- [ ] **CSRF**: 跨站请求伪造是否防范？（CSRF Token / SameSite Cookie）
- [ ] **SSRF**: 用户可控制的 URL 是否限制了内网访问？
- [ ] **文件上传**: 文件类型/大小检查、路径穿越防护
- [ ] **依赖**: 新增依赖是否有已知 CVE？
- [ ] **配置**: 默认密码、debug 模式、CORS 是否过于宽松？

### 3.2 依赖安全

- [ ] 新增依赖的来源是否可信？（npm/PyPI 上游源验证）
- [ ] 依赖版本是否固定而非 `^` 或 `>=`？
- [ ] 是否引入了 tree-shaking 不需要的大型依赖？
- [ ] 依赖许可证是否与项目兼容？（GPL 需特别注意）

## 4. 性能审查点 (Performance Review Checklist)

### 4.1 数据库

- [ ] 是否存在 N+1 查询问题？（批量操作使用 `IN` 或 batch load）
- [ ] 查询是否使用了索引？（EXPLAIN 分析慢查询）
- [ ] 事务范围是否最小化？（避免长事务持有锁）
- [ ] 连接是否释放？（连接池用完归还）

### 4.2 I/O 与网络

- [ ] HTTP 调用是否有超时设置？
- [ ] 是否对下游设置了 Circuit Breaker / Bulkhead？
- [ ] 大文件/流是否使用 Streaming 而非全部加载到内存？
- [ ] 重复数据是否使用缓存？（Cache-Aside 模式）

### 4.3 计算

- [ ] 循环内是否有不必要的计算？（提取到循环外）
- [ ] 大数据集是否有分页或分批处理？
- [ ] 是否存在过早优化？（Profiling 前不做无根据优化）
- [ ] 锁粒度是否合适？（行锁 vs 表锁 vs 乐观锁）

## 5. 特定语言审查项

### 5.1 TypeScript / JavaScript

| 检查项 | 说明 |
|--------|------|
| `strict` 模式是否启用 | `tsconfig.json` 中 `strict: true` |
| `any` 类型使用 | 禁止使用 `any`，优先 `unknown` 或具体类型 |
| 异步错误处理 | `async/await` 是否有 try/catch |
| Promise 未处理 | 链式 `.catch()` 或 `try/await/catch` |
| `null` vs `undefined` | 是否一致使用 |
| 循环中闭包 | 使用 `let` 或 `forEach` 避免经典闭包陷阱 |

### 5.2 Python

| 检查项 | 说明 |
|--------|------|
| 类型提示 | 函数参数和返回值标注类型 (PEP 484) |
| 异常处理 | 捕获具体异常而非 `except:` |
| 上下文管理器 | 文件/数据库连接使用 `with` 语句 |
| 可变默认参数 | `def f(x=[])` → `def f(x=None)` |
| 列表推导 | 简单映射用推导，复杂逻辑保留 for 循环 |
| GIL 影响 | CPU 密集型任务考虑 multiprocessing 或 asyncio |

### 5.3 Java / Kotlin

| 检查项 | 说明 |
|--------|------|
| Null Safety | 使用 `Optional` 或 `@Nullable` / `@NonNull` 注解 |
| Stream API | 避免 `forEach` 中修改外部状态 |
| 日志框架 | 使用 SLF4J，避免字符串拼接占位符 |
| 线程安全 | 共享状态使用 `ConcurrentHashMap` 或锁 |
| try-with-resources | 确保资源自动关闭 |
| 不可变类 | 使用 `record` (Java 14+) 或 `@Value` (Lombok) |

### 5.4 Go

| 检查项 | 说明 |
|--------|------|
| 错误处理 | 每个 `error` 返回值必须检查，不 `_` 忽略 |
| `defer` 使用 | 资源关闭确保使用 `defer` |
| Goroutine 泄漏 | `go func()` 是否有生命周期管理（context 取消） |
| 接口大小 | 接口定义 ≤ 3 个方法（小接口原则） |
| 零值初始化 | 确认结构体零值安全（可为 nil 的字段处理） |

## 6. 审查评论分级

| 级别 | 标签 | 含义 | 是否需要修改 |
|------|------|------|--------------|
| **Blocking** | `[Blocking]` | 功能错误、安全问题、数据一致性受损 | 必须修改后合并 |
| **Should Fix** | `[Should]` | 设计问题、潜在 bug、性能风险 | 建议修改 |
| **Nitpick** | `[Nit]` | 样式偏好、命名建议、微小改进 | 可修改可忽略 |
| **Question** | `[Q]` | 不理解代码逻辑，需要解释 | 回答即可 |
| **Praise** | `[Praise]` | 认可优秀的代码设计 | 鼓励正面反馈 |

## 相关资产

- [asset-model.md](../standards/asset-model.md)
- [authoring-checklist.md](../standards/authoring-checklist.md)
- [coding-standards.md](../standards/coding-standards.md)
- [testing-guidelines.md](../standards/testing-guidelines.md)
