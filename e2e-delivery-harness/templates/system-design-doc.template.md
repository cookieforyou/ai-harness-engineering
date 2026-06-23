---
name: system-design-doc
type: deliverable-template
version: "1.0.0"
status: active
language: "zh-CN"
---

# 系统设计文档 模板

> 复制本模板到 `docs/` 对应路径，由 Agent 按 [standards/harness-engineering.md](../standards/harness-engineering.md) 填充。

## 元数据

- 项目: {project_name}
- 版本: {version}
- 作者: {author}
- 日期: {ISO8601}

## 正文

## 架构总览

### 系统架构图

```
{在此处嵌入架构图或描述架构图位置}
```

### 架构风格

- **架构模式**: {如: 微服务架构 / 分层架构 / 事件驱动架构}
- **设计原则**: {如: SOLID, DDD, Clean Architecture}
- **关键设计决策**: {关键的设计决策摘要}

## 组件视图

### 组件列表

| 组件名称 | 职责 | 依赖组件 | 通信方式 | 部署单元 |
|----------|------|----------|----------|----------|
| {component_name} | {responsibility} | {dependencies} | {RPC/Event/HTTP} | {deployment_unit} |

### 组件详情

#### {Component Name}

- **职责**: {详细描述该组件的职责}
- **输入**: {接收的输入数据}
- **输出**: {产生的输出数据}
- **关键依赖**: {内部和外部依赖}
- **设计约束**: {设计上的约束条件}

## 技术栈

| 层级 | 技术选型 | 版本 | 选型理由 |
|------|----------|------|----------|
| 前端框架 | {technology} | {version} | {rationale} |
| 后端框架 | {technology} | {version} | {rationale} |
| 数据库 | {technology} | {version} | {rationale} |
| 消息队列 | {technology} | {version} | {rationale} |
| 缓存 | {technology} | {version} | {rationale} |
| CI/CD | {technology} | {version} | {rationale} |
| 监控 | {technology} | {version} | {rationale} |

## API 概要

| API 名称 | 方法 | 路径 | 功能描述 | 认证方式 |
|----------|------|------|----------|----------|
| {api_name} | GET/POST/PUT/DELETE | {/api/v1/resource} | {description} | JWT/OAuth/API Key |

## 数据模型概览

### 核心实体

| 实体 | 存储方式 | 主要字段 | 关系 |
|------|----------|----------|------|
| {entity} | {Table/Document} | {key_fields} | {relationships} |

### 数据流

```
{数据流向描述,如: User -> API Gateway -> Service A -> Database}
```

## 部署架构

### 部署拓扑

| 环境 | 服务器/集群 | 资源配置 | 服务部署 | 网络区域 |
|------|-------------|----------|----------|----------|
| Dev | {cluster} | {CPU/Mem/Storage} | {services} | {network_zone} |
| Staging | {cluster} | {CPU/Mem/Storage} | {services} | {network_zone} |
| Production | {cluster} | {CPU/Mem/Storage} | {services} | {network_zone} |

### 网络架构

- **域名**: {domain_name}
- **负载均衡**: {load_balancer_config}
- **防火墙规则**: {firewall_rules}
- **CDN**: {cdn_config}

## 非功能设计

### 性能设计

- **缓存策略**: {缓存层级和策略}
- **数据库优化**: {索引/分片/读写分离策略}
- **异步处理**: {异步任务设计}

### 安全设计

- **认证方案**: {认证机制描述}
- **授权方案**: {权限模型描述}
- **数据加密**: {加密方案}
- **防攻击**: {DDoS/SQL注入等防护措施}

### 可扩展性设计

- **水平扩展**: {扩展策略}
- **垂直扩展**: {扩展策略}
- **自动扩缩**: {Auto-scaling 策略}

## ADR 引用

| ADR ID | 标题 | 决策 | 状态 |
|--------|------|------|------|
| ADR-001 | {title} | {decision} | Accepted/Proposed/Deprecated |

## 修订历史

| 版本 | 日期 | 作者 | 变更内容 | 评审人 |
|------|------|------|----------|--------|
| v1.0 | {ISO8601} | {author} | 初稿 | {reviewer} |

## 验证

- [ ] 已通过 [evaluations/output-validation-checklist.md](../evaluations/output-validation-checklist.md)
