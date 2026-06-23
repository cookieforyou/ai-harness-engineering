---
name: 12-factor-app
description: "12-Factor App 方法论标准，定义云原生应用设计的12项核心原则及其实践指南、反模式和合规检查"
type: standard
version: "1.1.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-23
status: active
language: "zh-CN"
tags: ['standard', '12-factor', 'cloud-native', 'architecture']
---

# 12-Factor App 方法论标准

## Overview (概述)

12-Factor App 由 Heroku 于 2011 年提出，是构建云原生 SaaS 应用的权威方法论。本
标准定义 12 项核心原则，适用于微服务架构开发、CI/CD 流水线合规审查及 AI Harness
生成交付物的质量基准。遵循此标准可显著降低环境差异缺陷率，提升发布频率与恢复能力。

## Core Content (核心内容)

### 1. Codebase (基准代码)

**原则：** 一份基准代码，多份部署。

每个应用在版本控制中有且仅有一个代码仓库（repo），可部署到多个环境。代码仓库与
应用一一对应。

- **实践指南：** 每个微服务独立 Git 仓库；Trunk-Based Development 分支策略；
  不同环境通过构建产物版本号区分，而非维护不同分支；共享代码提取为独立库。
- **反模式：** 多应用共享同一仓库；同一应用在多个仓库维护拷贝；使用分支区分环境。

### 2. Dependencies (显式声明依赖)

**原则：** 显式声明并隔离依赖关系。

应用通过依赖清单声明所有外部库，使用 lock 文件确保一致性，绝不依赖系统级包。

- **实践指南：** `pip` + `requirements.txt` / `poetry.lock`；`npm` +
  `package-lock.json`；`go.mod` + `go.sum`；lock 文件必须提交；容器化使用多阶段构建。
- **反模式：** 隐式依赖全局包；不提交 lock 文件；手工下载 JAR 包无版本锁定；拷贝三方库源码。

### 3. Config (配置)

**原则：** 配置存储在环境变量中。

数据库连接、凭证、运行时标识等必须与代码分离。环境变量可跨环境自然切换，无需改代码。

- **实践指南：** 配置通过 `os.getenv` / `process.env` 读取；启动时做配置校验（fail fast）；
  使用 `.env.example` 记录必需变量（不含真实值）；分组配置使用命名空间前缀。
- **反模式：** 代码仓库中硬编码配置或生产密钥；`config/` 目录存放多环境配置文件并提交；
  配置作为编译时常量嵌入二进制。

### 4. Backing Services (后端服务)

**原则：** 把后端服务当作附加资源。

数据库、消息队列、缓存、外部 API 视为可通过网络连接访问的资源。切换实现无需改代码。

- **实践指南：** 连接字符串通过单一环境变量注入（如 `DATABASE_URL`）；
  通过依赖注入解耦服务，方便测试 mock；使用服务发现或 DNS 进行运行时绑定。
- **反模式：** 硬编码数据库主机和凭据；代码中用 if-else 判断环境切换配置；应用管理连接池过紧耦合。

### 5. Build, Release, Run (构建、发布、运行)

**原则：** 严格分离构建、发布、运行三个阶段。

| 阶段 | 输入 | 输出 | 说明 |
|------|------|------|------|
| Build | 代码 + 依赖 | 构建产物 | 编译、打包、依赖安装 |
| Release | 构建产物 + 配置 | 不可变 Release | 合并配置生成发布包 |
| Run | Release 包 | 运行进程 | 启动应用提供服务 |

- **实践指南：** CI/CD 中三个阶段明确定义边界；每次构建生成唯一版本号（SHA + 序号）；
  Release 不可修改——配置变更即创建新 Release；保留最近 N 个 Release 支持快速回滚。
- **反模式：** 运行时动态修改代码或热修补；构建与运行共享环境变量；手动登录服务器替换文件。

### 6. Processes (进程)

**原则：** 以一个或多个无状态进程执行应用。

进程不持有内部状态，持久化数据全部存储在后端服务。进程实例间不做本地内存共享。

- **实践指南：** Shared-Nothing 架构；会话存储在 Redis/Memcached 而非进程内存；
  上传文件持久化到对象存储（S3/MinIO）；增加进程数线性提升吞吐。
- **反模式：** 粘性会话（sticky session）导致负载均衡绑定实例；本地文件系统保存上传文件；
  进程内存维护业务状态，重启后丢失；进程间共享内存通信。

### 7. Port Binding (端口绑定)

**原则：** 通过端口绑定提供服务。

应用自包含 HTTP 服务进程，监听端口对外暴露 API，无需外部 Web 服务器容器。

- **实践指南：** 应用直接绑定端口（`app.listen(PORT)`），`PORT` 由环境变量注入；
  内嵌 HTTP 服务器（Spring Boot Embedded Tomcat、Express.js、FastAPI）；
  反向代理（Nginx/Envoy）作为运行时基础设施而非应用依赖。
- **反模式：** WAR 部署到独立 Tomcat 实例；硬编码监听端口号；反向代理配置编码在应用中。

### 8. Concurrency (并发)

**原则：** 通过进程模型扩展。

不同负载分配不同类型的进程（Web、Worker、Scheduler），通过水平扩展增加处理能力。

- **实践指南：** Web 进程处理 HTTP 请求（事件驱动）；Worker 进程处理异步队列任务；
  Scheduler 进程处理定时任务；利用 Kubernetes HPA 实现自动扩缩。
- **反模式：** 单进程多线程处理所有负载，受限于单机资源上限；API + 定时任务 + 消息消费混跑；
  进程内线程数过高导致上下文切换开销过大。

### 9. Disposability (易处理)

**原则：** 快速启动和优雅终止最大化鲁棒性。

进程随时可被创建或销毁而不影响系统可用性，为弹性伸缩和滚动更新提供保障。

- **实践指南：** 启动时间 < 5 秒；实现 SIGTERM 信号处理——停接新请求、完成进行中的请求、
  关闭连接池；Worker 通过 ACK 机制防止任务丢失。
- **反模式：** 启动耗时 2-3 分钟导致滚动更新不可用；SIGKILL 下数据丢失（未提交事务、
  未确认消息）；未实现 graceful shutdown 直接断连数据库。

### 10. Dev/Prod Parity (环境等价)

**原则：** 保持开发、预发布、生产环境一致。

在时间（部署间隔）、人员（开发者参与运维）、工具（后端服务类型）三维度上缩小差异。

- **实践指南：** 开发环境使用同类型后端服务（同等版本 PostgreSQL/Redis/Kafka）；
  Docker Compose / Minikube 搭建本地完整环境；通过 IaC（Terraform/CloudFormation）确保环境可重复。
- **反模式：** 开发 SQLite 生产 PostgreSQL 带来兼容性问题；跨 OS 差异且未在 CI 测试；
  开发手工部署、生产自动化部署导致流程差异。

### 11. Logs (日志)

**原则：** 把日志当作事件流。

应用将日志写入 stdout（INFO/DEBUG）和 stderr（ERROR/WARN），由执行环境捕获路由。

- **实践指南：** 使用 JSON 结构化日志，含时间戳、级别、服务名、请求 ID；
  通过采集器（Fluentd/Filebeat/Vector）发送到 ELK/Loki/CloudWatch；
  在聚合平台设置告警，而非在应用中判断。
- **反模式：** 日志写入本地文件并自行轮转；应用直接调用日志聚合 API（如直接写 ES）；
  日志输出到数据库表影响业务性能；纯文本日志无法被自动化解析。

### 12. Admin Processes (管理进程)

**原则：** 将管理任务作为一次性进程运行。

数据库迁移、数据修复、控制台等在应用相同环境中作为 one-off 进程执行。

- **实践指南：** 迁移脚本与应用同仓，作为 Release 流程自动执行；管理脚本访问相同环境变量；
  提供 REPL/控制台（Django shell）用于排查；管理操作有审计日志。
- **反模式：** SSH 登录生产手动执行 DDL；使用与线上不同版本的依赖执行管理脚本；
  管理脚本中配置硬编码；管理操作无权限控制。

## Examples (实践示例)

### 示例 1：配置管理

**Bad（不符合 12-Factor）：**
```python
# config.py
DATABASE = {"host": "localhost", "port": 5432, "password": "password123"}
if ENV == "production":
    DATABASE["host"] = "prod-db.internal"
```
问题：密码硬编码、多环境 if-else 分支、生产配置泄漏风险。

**Good（12-Factor 合规）：**
```python
import os, sys
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    print("FATAL: DATABASE_URL not set", file=sys.stderr); sys.exit(1)
```
配置通过环境变量注入，启动时 fail-fast 校验，`.env.example` 记录变量但不含真实值。

### 示例 2：进程无状态

**Bad：**
```python
session_store = {}
@app.route("/login")
def login():
    session_store[session_id] = user_data
```
问题：会话存进程内存，多实例需 sticky session，重启丢失。

**Good（12-Factor 合规）：**
```python
redis_client = redis.from_url(os.getenv("REDIS_URL"))
@app.route("/login")
def login():
    redis_client.setex(f"session:{session_id}", 3600, user_data)
```
会话存储在 Redis 中，任意实例可处理请求，支持水平扩展和进程重启。

### 示例 3：日志处理

**Bad：**
```python
logging.basicConfig(filename="/var/log/myapp.log")
handler = RotatingFileHandler("/var/log/myapp.log", maxBytes=10*1024*1024, backupCount=5)
```
问题：写入本地文件、应用自管理轮转、需 SSH 登录查看。

**Good（12-Factor 合规）：**
```python
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter('{"time":"%(asctime)s","level":"%(levelname)s","msg":"%(message)s"}'))
```
日志输出到 stdout，JSON 结构化格式，由采集器统一收集处理。

## Compliance Checklist (合规检查清单)

- [ ] **代码库**：是否每个应用有独立代码库，多部署共享同一份基准代码？
- [ ] **依赖**：所有依赖是否显式声明并通过 lock 文件锁定版本？
- [ ] **配置**：配置是否通过环境变量注入，而非代码中硬编码？
- [ ] **后端服务**：所有后端服务是否通过绑定方式接入，切换无需改代码？
- [ ] **构建/发布/运行**：三个阶段是否严格分离，Release 是否不可变？
- [ ] **进程**：应用是否无状态、无本地持久化，会话存储在外部服务？
- [ ] **端口绑定**：应用是否自包含并通过端口暴露，而非依赖外部 Web 容器？
- [ ] **并发**：是否通过进程模型实现水平扩展（Web/Worker/Scheduler）？
- [ ] **易处理**：启动时间是否 < 10 秒，是否实现 SIGTERM 优雅终止？
- [ ] **环境等价**：开发、预发布、生产是否使用同类型后端服务？
- [ ] **日志**：日志是否通过 stdout/stderr 输出，由执行环境统一收集？
- [ ] **管理进程**：管理任务是否作为一次性进程在同等环境中运行？

## Key Metrics (关键指标)

| 指标 | 目标值 | 测量方法 |
|------|--------|----------|
| 构建产物版本号唯一率 | 100% | 每次构建生成唯一 SHA+序号标识，无重复版本号 |
| 环境变量配置覆盖率 | 100% | 代码中零硬编码配置项，所有环境相关值通过 `os.getenv` 注入 |
| Release 不可变率 | 100% | 发布后配置修改必须创建新 Release，禁止原地修改已发布 Release |

## Related Standards (相关标准)

- [harness-engineering.md](harness-engineering.md) —— 工程交付质量标准框架
- [asset-model.md](asset-model.md) —— 资产模型定义与引用规则
- [authoring-checklist.md](authoring-checklist.md) —— Agent 交付物编写检查清单
- [output-quality-rubric.md](output-quality-rubric.md) —— 输出质量评分量规
