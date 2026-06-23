---
name: dependency-graph
type: deliverable-template
version: "1.0.0"
status: active
language: "zh-CN"
---

# 依赖关系图 模板

> 复制本模板到 `docs/` 对应路径，由 Agent 按 [standards/harness-engineering.md](../standards/harness-engineering.md) 填充。

## 元数据

- 项目: {project_name}
- 版本: {version}
- 作者: {author}
- 日期: {ISO8601}

## 正文

## 依赖图概览

- **系统/项目**: {system_name}
- **版本**: {version}
- **更新日期**: {ISO8601}
- **维护人**: {maintainer}

## 节点清单

### 服务节点

| 节点ID | 节点名称 | 节点类型 | 版本 | 健康状态 | 负责人 |
|--------|----------|----------|------|----------|--------|
| N-001 | {service_name} | {微服务/数据库/中间件/外部系统} | {version} | {正常/警告/异常} | {owner} |
| N-002 | {service_name} | {微服务/数据库/中间件/外部系统} | {version} | {正常/警告/异常} | {owner} |
| N-003 | {service_name} | {微服务/数据库/中间件/外部系统} | {version} | {正常/警告/异常} | {owner} |

### 基础设施节点

| 节点ID | 节点名称 | 类型 | 配置 | 运行环境 |
|--------|----------|------|------|----------|
| I-001 | {name} | {K8s Cluster / VM / LB / DNS} | {config} | {env} |

## 依赖关系

### 服务间依赖

| 源节点 | 目标节点 | 依赖类型 | 通信方式 | 关键性 | 描述 |
|--------|----------|----------|----------|--------|------|
| N-001 | N-002 | {强依赖/弱依赖} | {HTTP/gRPC/Event} | {核心/非核心} | {description} |
| N-002 | N-003 | {强依赖/弱依赖} | {HTTP/gRPC/Event} | {核心/非核心} | {description} |

### 外部依赖

| 依赖项 | 类型 | 供应商 | 版本 | SLA | 备用方案 |
|--------|------|--------|------|-----|----------|
| {dependency} | {SaaS/API/DB} | {vendor} | {version} | {sla} | {fallback} |

## 关键路径

### 核心请求链路

```
Request Flow: {entry} → N-001 → N-002 → N-003 → {exit}
```

### 关键路径分析

| 路径 | 涉及节点 | 总延迟预算 | 风险等级 | 优化建议 |
|------|----------|------------|----------|----------|
| {path} | {nodes} | {latency} | H/M/L | {recommendation} |

## 风险评估

| 风险ID | 依赖描述 | 故障影响 | 故障概率 | 缓解措施 |
|--------|----------|----------|----------|----------|
| DR-001 | {dependency} | {impact} | H/M/L | {mitigation} |
| DR-002 | {dependency} | {impact} | H/M/L | {mitigation} |

## 版本兼容性矩阵

| 服务A | 服务A版本 | 服务B | 服务B版本 | 兼容性 |
|-------|-----------|-------|-----------|--------|
| {service} | {version} | {service} | {version} | 兼容/不兼容/需验证 |
| {service} | {version} | {service} | {version} | 兼容/不兼容/需验证 |

## 验证

- [ ] 已通过 [evaluations/output-validation-checklist.md](../evaluations/output-validation-checklist.md)
