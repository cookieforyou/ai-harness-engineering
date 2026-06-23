---
name: c4-model
description: "C4 架构模型标准，定义系统上下文、容器、组件和代码四个层级的架构可视化规范与评审要点"
type: standard
version: "2.0.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-23
status: active
language: "zh-CN"
tags: ['standard', 'architecture', 'c4-model', 'visualization']
---

# C4 架构模型

> 本规范定义 E2E Delivery Harness 中使用 C4 模型进行架构可视化的标准，涵盖四个层级的使用场景、绘图规范与评审要点。审查基准见 [harness-engineering.md](../harness-engineering.md)。

## 1. C4 模型概述

C4 模型由 Simon Brown 提出，通过 **4 个由粗到细的抽象层级** 描述软件架构：

```
Level 1: Context (系统上下文)    ← 面向所有人
Level 2: Container (容器)       ← 面向技术团队
Level 3: Component (组件)       ← 面向开发团队
Level 4: Code (代码)            ← 面向单个模块/类
```

> 只画必要的图：每个项目至少完成 Level 1-2；复杂模块需要 Level 3；Level 4 仅在关键或复杂代码处使用。

## 2. Level 1 — System Context (系统上下文)

### 2.1 用途

展示整个系统的高层视图：系统边界、用户角色、外部依赖。使所有人都能快速理解 "这个系统做什么、和谁交互"。

### 2.2 元素类型

| 元素 | 颜色 | 形状 | 定义 |
|------|------|------|------|
| **Person (用户)** | 浅灰 | 人物图标 | 系统的最终用户或上游系统操作者 |
| **Software System (本系统)** | 蓝色 | 矩形 | 当前正在构建的软件系统 |
| **External System (外部系统)** | 浅灰 | 矩形 | 本系统依赖的第三方服务或组织 |

### 2.3 必含信息

- 系统名称 + 简短描述（1-2 句话说明职责）
- 所有外部用户角色（至少 1 个）
- 所有关键外部依赖（数据库、消息队列、第三方 API）
- 交互关系的方向与文字说明（使用直观动词：创建订单、发送通知）
- 图标题左下角标注 `[System Context] {系统名} v{版本}`

### 2.4 何时使用

- 项目启动时必须绘制
- 架构评审 (Architecture Review) 前置图
- 新成员 Onboarding 文档
- 跨团队沟通场景

## 3. Level 2 — Container (容器)

### 3.1 用途

展示系统内部的高层技术切分：每个 Container（独立部署单元或运行时进程）的职责、技术选型与交互关系。

### 3.2 容器类型定义

| 类型 | 示例 | 技术标注 |
|------|------|----------|
| **Web Application** | SPA 前端, SSR 服务 | React 18 + Next.js |
| **API Application** | REST/GraphQL 服务 | Spring Boot 3, FastAPI |
| **Database** | 关系型、NoSQL 存储 | PostgreSQL 16, MongoDB 7 |
| **Message Queue** | 异步消息通道 | Kafka 3.5, RabbitMQ 3.x |
| **Cache** | 缓存层 | Redis 7, Memcached |
| **File Store** | 对象存储 | S3, MinIO |
| **CLI / Batch** | 定时任务、批处理 | Airflow, Quartz |

### 3.3 必含信息

- 每个 Container 的名称 + 技术选型（语言/框架/版本）
- 内部 Container 之间的交互关系与协议（HTTP/REST/gRPC/异步消息）
- 与外部系统的交互（标注协议、数据格式）
- 关键技术决策标注（原因 + 备选方案）

### 3.4 示例结构

```
[User] → (HTTPS) → [Web App: React 18]
                        ↓ (REST/JSON)
                  [API Gateway: Spring Boot 3]
                   ↙       ↓         ↘
           [Auth: Keycloak] [Order: 微服务] [Payment: 微服务]
                              ↓              ↓
                        [PostgreSQL 16]  [Stripe API]
```

### 3.5 何时使用

- 技术方案设计文档必含
- 系统间集成方案沟通
- 部署架构设计
- 技术栈决策记录 (ADR) 的视图

## 4. Level 3 — Component (组件)

### 4.1 用途

展示单个 Container 内部的逻辑组件划分：接口、控制器、服务、仓库等。使开发团队理解代码结构与职责边界。

### 4.2 组件类型 (参考分层架构)

| 层 | 组件 | 职责 |
|----|------|------|
| **Presentation** | Controller, Resolver, Handler | 请求接收 + 响应返回 |
| **Application** | Service, UseCase, CommandHandler | 业务流程编排 |
| **Domain** | Entity, ValueObject, Aggregate | 领域模型与业务规则 |
| **Infrastructure** | Repository, Adapter, Client | 技术实现（DB/消息/外部 API）|

### 4.3 必含信息

- 组件名称 + 职责描述（1-2 句说明）
- 组件间依赖关系（接口依赖 vs 具体依赖）
- 外部依赖适配器（标注使用的协议/框架）
- 关键设计模式标注（Factory, Strategy, Observer）

### 4.4 何时使用

- 复杂模块/微服务的设计文档
- 模块重构或拆分前期分析
- 系统集成测试范围定义

## 5. Level 4 — Code (代码)

### 5.1 用途

展示特定组件内部的关键实现细节：类关系、接口契约、状态机。仅在代码过于复杂需要可视化时使用。

### 5.2 表现形式

- **UML 类图**（推荐 PlantUML / Mermaid）
- **状态图**（State Machine）
- **序列图**（Sequence Diagram）
- **数据流图**（Data Flow）

### 5.3 何时使用

- 核心算法或复杂流程的代码生成
- 高复杂度逻辑的重构计划
- 安全审计的数据流分析

### 5.4 限制

- Level 4 图应作为代码注释或独立的 docs 片段存在
- 图更新应与代码同步（工具自动生成优先于手绘）
- 避免为每一段代码画图 — 只在认知负荷高的地方使用

## 6. 绘图规范 (Diagram Standards)

### 6.1 工具选择

| 工具 | 适用场景 | 存储格式 |
|------|----------|----------|
| **PlantUML** | 可嵌入 Markdown，版本控制友好 | `.puml` 文本文件 |
| **Mermaid** | Markdown 内嵌，GitHub 原生支持 | Markdown code block |
| **Structurizr** | C4 DSL，代码驱动的架构图 | `.dsl` / 代码 |
| **Draw.io / Excalidraw** | 快速原型、非正式沟通 | `.drawio.svg` / `.png` |

> 推荐：正式文档使用 PlantUML 或 Structurizr DSL；README/ Wiki 使用 Mermaid。

### 6.2 通用规范

- 所有图需要使用标准元素形状和颜色（保持视觉一致性）
- 图内元素数量: Context ≤ 12, Container ≤ 15, Component ≤ 20
- 关系连线标注协议（HTTP, gRPC, AMQP）和数据格式（JSON, Protobuf, Avro）
- 图需标注版本号和最后更新日期

### 6.3 元素颜色规范

| 层级 | 本系统 | 外部系统 | 用户 |
|------|--------|----------|------|
| Level 1 | 蓝色 (#438DD5) | 灰色 (#999999) | 深灰 (#333333) |
| Level 2 | 根据技术类型分类 | 灰色 (#999999) | 深灰 (#333333) |
| Level 3 | 按层上色 | N/A | N/A |

## 7. 评审清单 (C4 Review Checklist)

### 7.1 通用

- [ ] 图是否有明确的目的（Context/Container/Component/Code）
- [ ] 元素命名是否清晰，避免技术术语（非开发人员能否看懂 Level 1-2？）
- [ ] 关系是否标注了方向、协议、数据格式
- [ ] 图是否包含版本号和最后更新日期

### 7.2 Level 1

- [ ] 是否包含所有外部用户角色和外部依赖
- [ ] 系统边界是否清晰（什么是本系统、什么是外部系统）
- [ ] 是否省略了次要交互（只保留关键关系）

### 7.3 Level 2

- [ ] 每个 Container 的技术选型是否明确
- [ ] Container 间的通信协议与同步/异步选择是否合理
- [ ] 数据存储方案是否解释了选择理由

### 7.4 Level 3

- [ ] 组件职责是否有单一职责原则 (SRP) 检查
- [ ] 组件间的依赖方向是否合理（内层不知道外层）
- [ ] 是否标注了关键设计模式

## 相关资产

- [asset-model.md](../standards/asset-model.md)
- [authoring-checklist.md](../standards/authoring-checklist.md)
- [coding-standards.md](../standards/coding-standards.md)
