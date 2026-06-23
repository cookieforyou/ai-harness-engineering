---
name: health-check-guidelines
type: standard
version: "2.0.0"
status: active
---

# 健康检查规范

> 本规范定义 E2E Delivery Harness 中所有服务的健康检查端点模式、liveness/readiness 区分、检查频率与超时设置。审查基准见 [harness-engineering.md](harness-engineering.md)。

## 1. 健康检查类型定义

Kubernetes 与云平台普遍支持三种健康检查探针，每种有不同的目的：

| 探针类型 | 用途 | 失败后果 | 类比 |
|----------|------|----------|------|
| **Liveness** | 判断进程是否存活（是否需重启） | 容器重启 (Restart) | "人还有呼吸吗？" |
| **Readiness** | 判断是否可接收流量 | 从 Service 摘除 | "胃能消化食物吗？" |
| **Startup** | 判断初始化是否完成 | 延迟 liveness/readiness 检查 | "人醒了吗？" |

### 1.1 Kubernetes 探针配置示例

```yaml
# Deployment 示例
livenessProbe:
  httpGet:
    path: /healthz
    port: 8080
  initialDelaySeconds: 10
  periodSeconds: 10
  timeoutSeconds: 3
  failureThreshold: 3

readinessProbe:
  httpGet:
    path: /readyz
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 5
  timeoutSeconds: 3
  successThreshold: 1
  failureThreshold: 2

startupProbe:
  httpGet:
    path: /startupz
    port: 8080
  initialDelaySeconds: 0
  periodSeconds: 2
  failureThreshold: 30  # 60s max startup time
```

## 2. 健康检查端点规范

### 2.1 端点路径

| 端点 | 类型 | 功能 | 响应码 |
|------|------|------|--------|
| `/healthz` | Liveness | 进程状态（仅检查内部状态） | 200 OK / 503 Service Unavailable |
| `/readyz` | Readiness | 依赖就绪检查（DB、缓存、下游服务） | 200 OK / 503 Service Unavailable |
| `/startupz` | Startup | 应用启动完成检查 | 200 OK / 503 Service Unavailable |
| `/livez` | Liveness 别名 | 同上 | 同上 |

禁止使用 `/health` 作为唯一的通用健康检查端点 — 必须区分 liveness 和 readiness。

### 2.2 端点响应格式

```json
// HTTP 200: 正常
{
  "status": "ok",
  "timestamp": "2026-06-23T10:30:00Z",
  "version": "2.1.3",
  "checks": {
    "database": { "status": "ok", "latency_ms": 2 },
    "redis": { "status": "ok", "latency_ms": 1 },
    "downstream_api": { "status": "degraded", "latency_ms": 80 },
    "disk_space": { "status": "ok", "used_percent": 65 }
  }
}

// HTTP 503: 不健康
{
  "status": "unhealthy",
  "timestamp": "2026-06-23T10:30:00Z",
  "version": "2.1.3",
  "checks": {
    "database": { "status": "unreachable", "error": "connection timeout" },
    "redis": { "status": "ok", "latency_ms": 1 }
  },
  "degraded_services": [ "database" ]
}
```

### 2.3 端点实现原则

| 原则 | 说明 |
|------|------|
| **轻量** | 不执行完整业务逻辑，不写入数据库 |
| **快速超时** | 每个子检查超时 ≤ 500ms，总响应 ≤ 2s |
| **可缓存** | 设置 `Cache-Control: no-cache` 避免代理缓存 |
| **无认证** | Health 端点不应要求认证（k8s 需要无认证访问） |
| **无副作用** | 不修改系统状态，只读 |

## 3. Liveness 检查细节

### 3.1 检查内容

- 进程是否运行正常（内部 goroutine/线程池状态）
- 内存是否未达到 OOM 风险（通常 > 90% 标记为不健康）
- 关键 goroutine/线程是否卡死（Deadlock 检测）
- 配置文件是否正确加载

### 3.2 注意事项

- Liveness 检查失败会导致容器重启 — 成功率要高于 99%
- **不要**在 liveness 中检查外部依赖（否则外部问题会导致级联重启）
- 设置 `failureThreshold` (通常 3) 避免短暂波动导致重启
- 对于有预热过程的服务，使用 startupProbe 延迟 liveness 检查

### 3.3 反模式

- ❌ Liveness 检查中包含数据库查询
- ❌ Liveness 检查超时设置过短导致频繁重启
- ❌ Liveness 和 Readiness 使用同一个端点

## 4. Readiness 检查细节

### 4.1 检查内容

- 数据库连接池：可用连接数 > 池大小 × 20%
- 缓存（Redis/Memcached）：连接正常，延迟 < 100ms
- 下游依赖：最近请求成功率 > 90%（可降级时标记为 degraded 而非 unhealthy）
- 消息队列：连接正常
- 磁盘空间：使用率 < 90%
- 内存：非 GC/压缩期间的合理使用率

### 4.2 降级语义

| 状态 | HTTP 码 | 行为 |
|------|---------|------|
| `ok` | 200 | 完全就绪，接收流量 |
| `degraded` | 200 (可选 503) | 部分依赖不可用但仍可服务，谨慎接收流量 |
| `unhealthy` | 503 | 不可用，从负载均衡摘除 |

### 4.3 注意事项

- Readiness 失败不会重启容器，仅摘除流量 — 是更安全的机制
- Readiness 检查中任何一个依赖失败是否应标记为 unhealthy？
  - 如果是**关键依赖**（服务不能无该依赖运作）：标记 unhealthy
  - 如果是**非关键依赖**（可降级运行）：标记 degraded，保持 readiness

## 5. 检查频率与超时 (Check Frequencies and Timeouts)

### 5.1 推荐配置

| 环境 | 探针类型 | 周期 | 初始延迟 | 超时 | 失败阈值 |
|------|----------|------|----------|------|----------|
| **Production** | Liveness | 15s | 30s | 5s | 3 |
| **Production** | Readiness | 10s | 10s | 3s | 2 |
| **Production** | Startup | 2s | 0 | 2s | 30 |
| **Staging** | Liveness | 30s | 60s | 5s | 3 |
| **Staging** | Readiness | 15s | 15s | 3s | 2 |
| **Development** | Liveness | 60s | 120s | 10s | 3 |
| **Development** | Readiness | 30s | 30s | 5s | 2 |

### 5.2 公式参考

- **超时 (timeoutSeconds)** ≤ `periodSeconds / 2`（超时应在周期的一半内完成）
- **初始延迟 (initialDelaySeconds)** ≥ 服务启动时间 + buffer（建议 buffer + 30%）
- **总容忍失败时间** = `periodSeconds × (failureThreshold - 1) + timeoutSeconds`

## 6. 自定义业务健康检查

对于关键业务，建议提供专用的业务健康端点 `/business/health`：

```
/business/health
```

示例检查内容：
- 最近 5 分钟 API 请求成功率 ≥ 99%
- 最近 5 分钟核心业务流程完成率（如支付成功率）
- 消息队列积压数 ≤ 阈值
- 可配置的关键指标（按业务定义）

业务健康检查不在 k8s 探针中使用，而是用于：
- 负载均衡器的更精确流量路由
- 自定义监控 dashboard
- 外部健康监测平台集成

## 7. 健康检查合规清单

- [ ] 每个服务至少暴露 `/healthz` 和 `/readyz` 两个端点
- [ ] Liveness 仅检查进程内部状态，不依赖外部服务
- [ ] Readiness 检查覆盖所有关键外部依赖
- [ ] 检查响应时间 ≤ 超时配置
- [ ] 生产环境 Readiness 周期 ≤ 15s
- [ ] 端点不要求认证
- [ ] 检查逻辑无副作用（不写入数据库）
- [ ] 响应格式包含结构化 JSON 而非纯文本
- [ ] StartupProbe 用于需要较长初始化时间的服务

## 引用

- [asset-model.md](asset-model.md)
- [authoring-checklist.md](authoring-checklist.md)
- [sre-best-practices.md](sre-best-practices.md)
- [monitoring-standards.md](monitoring-standards.md)
