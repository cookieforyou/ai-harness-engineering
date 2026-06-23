---
name: architecture-doc
type: deliverable-template
version: "1.0.0"
status: active
language: "zh-CN"
---

# 架构设计文档 模板

> 复制本模板到 `docs/` 对应路径，由 Agent 按 [standards/harness-engineering.md](../standards/harness-engineering.md) 填充。

## 元数据

- 项目: {project_name}
- 版本: {version}
- 作者: {author}
- 日期: {ISO8601}

## 正文

## 系统上下文 (C4 - Context)

### 系统范围

{描述系统的业务边界和上下文}

### 外部角色

| 角色 | 描述 | 与系统的交互 |
|------|------|--------------|
| {actor} | {description} | {interaction} |

### 外部系统

| 外部系统 | 交互方式 | 数据流向 | SLA 要求 |
|----------|----------|----------|----------|
| {system_name} | {REST/Event/DB} | {direction} | {SLA} |

### Context Diagram

```
[User] <---> [System] <---> [External System]
```

## 容器视图 (C4 - Container)

### 容器列表

| 容器名称 | 技术选型 | 职责 | 通信协议 |
|----------|----------|------|----------|
| {container_name} | {tech_stack} | {responsibility} | {protocol} |

### 容器交互

- {Container A} --(HTTP/REST)--> {Container B}: {交互说明}
- {Container A} --(Event)--> {Message Queue}: {交互说明}

## 组件视图 (C4 - Component)

### 核心组件

| 组件 | 所属容器 | 职责 | 关键接口 |
|------|----------|------|----------|
| {component} | {container} | {responsibility} | {interfaces} |

### 组件依赖关系

```
{component_diagram_description}
```

## 架构决策 (ADR)

### ADR 模板

每条 ADR 记录以下内容:

**标题**: {决策标题}

**状态**: [Proposed | Accepted | Deprecated | Superseded]

**上下文**: {触发此决策的业务和技术背景}

**决策**: {明确描述所做的架构决策}

**理由**: {选择此决策的原因}

**备选方案**:
- {方案1}: {优缺点}
- {方案2}: {优缺点}

**影响**: {此决策的正面/负面影响}

**关联**: {关联的 ADR 或需求}

### ADR 列表

| ADR ID | 标题 | 状态 | 决策日期 | 负责人 |
|--------|------|------|----------|--------|
| ADR-001 | {title} | Accepted | {ISO8601} | {owner} |

## 质量属性场景

### 可用性场景

- **场景**: {描述可用性相关的具体场景}
- **策略**: {采用的可用性策略,如冗余/故障转移}

### 性能场景

- **场景**: {描述性能相关的具体场景}
- **策略**: {采用的性能策略,如缓存/异步处理}

### 安全场景

- **场景**: {描述安全相关的具体场景}
- **策略**: {采用的安全策略,如加密/认证}

### 可维护性场景

- **场景**: {描述可维护性相关的具体场景}
- **策略**: {采用的可维护性策略,如模块化/标准化}

## 技术选型与理由

### 关键技术选型

| 技术 | 选型理由 | 备选方案 | 否决理由 |
|------|----------|----------|----------|
| {technology} | {rationale} | {alternatives} | {rejection_reasons} |

## 风险分析

| 风险ID | 风险描述 | 概率 | 影响 | 缓解措施 | 应急方案 |
|--------|----------|------|------|----------|----------|
| RSK-001 | {description} | H/M/L | H/M/L | {mitigation} | {contingency} |

## 修订历史

| 版本 | 日期 | 作者 | 变更内容 | 评审人 |
|------|------|------|----------|--------|
| v1.0 | {ISO8601} | {author} | 初稿 | {reviewer} |

## 验证

- [ ] 已通过 [evaluations/output-validation-checklist.md](../evaluations/output-validation-checklist.md)
