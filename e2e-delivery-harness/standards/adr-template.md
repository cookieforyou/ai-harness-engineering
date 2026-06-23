---
name: adr-template
description: "架构决策记录(ADR)模板标准，定义ADR的完整结构、编号规范、存储约定和评审流程"
type: standard
version: "1.1.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-23
status: active
language: "zh-CN"
tags: ['standard', 'adr', 'architecture', 'decision-record']
---

# 架构决策记录 (ADR) 模板标准

> 本文件为 E2E Delivery Harness 团队使用的架构决策记录标准。审查基准见 [harness-engineering.md](harness-engineering.md)。

## Overview

### 目的

架构决策记录（Architecture Decision Record, ADR）用于记录项目中做出的重要架构决策，包括决策的上下文、方案选择、推理过程和已知后果。ADR 的核心目标是让当前和未来的团队成员理解"为什么"做出了某个架构选择，而不仅仅是"选择了什么"。

### 适用范围

本标准适用于 E2E Delivery Harness 项目中所有需要记录的技术和架构决策，包括但不限于：技术栈选型、框架与库的选择、API 设计范式、数据模型与存储方案、部署架构、安全策略、性能优化方案、以及跨团队协作接口约定。

### 谁应该编写 ADR

- 架构师、Tech Lead 和高级工程师在做出重大技术决策时
- 任何团队成员在发起技术提案时
- Code Review 中如果发现决策缺少记录，评审者有责任要求补充 ADR

## Core Content

### ADR 编号规范

ADR 编号格式为 `ADR-{YYYYMMDD}-{NNN}`，例如：`ADR-20240601-001`。

- **YYYYMMDD**：表示决策提出日期（ISO 8601 格式，无分隔符）
- **NNN**：当天连续序号，从 001 开始，三位数字
- **序号按年独立分配**，每年从 001 重新开始
- **编号永不重用**，即使 ADR 被否决或废弃，原编号也不得重新分配给其他决策
- **已废弃的 ADR 保留原编号**，通过状态字段标记为 Deprecated 或 Superseded，并注明替代 ADR 编号

### 存储位置约定

- **目录**：所有 ADR 文件统一存储在项目根目录下的 `docs/adr/` 目录中
- **文件命名规则**：`{NNN}-{kebab-case-title.md}`，其中标题使用小写英文单词，连字符分隔，例如 `001-microservice-communication-pattern.md`
- **索引文件**：`docs/adr/README.md` 文件维护一个按编号逆序排列的 ADR 清单，包含编号、标题、状态、日期和简要描述，方便快速浏览

### 完整 ADR 模板

每份 ADR 文件应遵循以下结构：

```markdown
---
title: "ADR-{NNN}: {Title}"
date: YYYY-MM-DD
status: Proposed | Accepted | Deprecated | Superseded
superseded-by: ADR-{NNN}  # 仅当 status 为 Superseded 时
deciders: ["姓名1", "姓名2"]
tags: ['architecture', 'decision']
---

# ADR-{NNN}: {标题}

## Status

- **状态**：Proposed | Accepted | Deprecated | Superseded by ADR-{NNN}
- **提出日期**：YYYY-MM-DD
- **最后更新**：YYYY-MM-DD
- **决策者**：[姓名1, 姓名2]

## Context

描述当前面临的问题、背景信息、约束条件和影响因素。包括：
- 触发决策的业务或技术驱动力
- 相关的系统边界和约束
- 需要考虑的技术债务或兼容性影响

## Decision

明确陈述所做出的决策，包括：
- 选择的方案是什么
- 选择的理由（基于 Context 中列出的因素）
- 决策是如何做出的（投票、Lazy Consensus、架构评审等）

## Consequences

记录决策带来的后果，分为正面和负面：

**正面**：
- 列出一个或多个主要收益

**负面**：
- 列出一个或多个权衡与代价

## Alternatives

列出考虑过的其他方案及被拒绝的原因：
- **方案 A**：简要描述。被拒绝原因：xxx。
- **方案 B**：简要描述。被拒绝原因：xxx。

## References

- 相关 ADR：链接到相关的其他 ADR 文档
- 相关文档：链接到设计文档、RFC、标准文档等
- 外部资料：链接到相关的技术文章或规范标准
```

### YAML Frontmatter 示例

每份 ADR 文件必须包含 YAML frontmatter 元数据块。以下为完整字段说明：

```yaml
---
title: "ADR-20240601-001: 微服务通信模式选型"
date: 2024-06-01
status: Accepted
superseded-by: ""              # 可选，仅当被取代时填写
deciders:
  - "张三"
  - "李四"
  - "王五"
tags:
  - architecture
  - microservice
  - communication
---
```

| 字段 | 必填 | 说明 |
|------|------|------|
| `title` | 是 | ADR 编号加标题，与文档 H1 一致 |
| `date` | 是 | 提出日期 |
| `status` | 是 | 当前生命周期状态 |
| `superseded-by` | 否 | 仅当被取代时填写 |
| `deciders` | 是 | 参与决策的人员列表 |
| `tags` | 是 | 至少一个标签，用于分类检索 |

### ADR 生命周期

ADR 遵循以下生命周期流转：

```
Proposed → Reviewed → Accepted → Deprecated
                                    ↓
                              Superseded by ADR-{NNN}
```

1. **Proposed**：初始状态。任何人可提出 ADR 并标记为此状态
2. **Reviewed**：ADR 进入评审阶段，评审人通过 PR 评论或线下会议提出反馈
3. **Accepted**：达成共识并被正式采纳。评审要求：
   - 最少 2 名评审者批准（Approved）
   - 评审者应为相关领域的技术负责人或有经验的工程师
   - 如有重大分歧，升级至架构委员会决策
4. **Deprecated**：该决策不再有效，但未被其他 ADR 直接取代（例如因项目方向变更）
5. **Superseded**：该决策被新的 ADR 取代，需在 `superseded-by` 字段中注明新 ADR 编号

**评审要点**：
- 评审聚焦于决策合理性而非个人偏好
- 评审者应关注 Context 是否准确、Alternatives 是否充分、Consequences 是否全面
- 超过 14 天无进展的 Proposed ADR 应进行提醒或关闭

### 最佳实践

1. **原子性**：每份 ADR 只记录一个决策，避免在单个 ADR 中捆绑多个独立决策
2. **理由优先**：重点记录"为何做此选择"而非"做了什么"——代码本身可以说明做了什么
3. **链接标准**：如果决策涉及团队已发布的技术标准，应在 References 中引用对应标准文档
4. **时效性**：决策做出后应在一周内完成 ADR 编写，避免事后回忆遗漏关键信息
5. **负面后果诚实记录**：不回避决策的负面后果，诚实记录有助于未来评估是否需要重新审视
6. **更新即机会**：当决策变更时，优先编写新 ADR 并废弃旧 ADR，而非修改历史记录
7. **搜索友好**：在 Context 和 Decision 中使用项目相关的关键词，便于日后通过全文搜索定位

## Examples

### 良好的 ADR 示例

以下是一个结构完整、信息充分的 ADR 示例：

```
---
title: "ADR-20240601-001: 采用 gRPC 作为服务间通信协议"
date: 2024-06-01
status: Accepted
deciders: ["张三", "李四"]
tags: ['architecture', 'microservice', 'communication']
---

# ADR-20240601-001: 采用 gRPC 作为服务间通信协议

## Status
- **状态**：Accepted
- **提出日期**：2024-06-01

## Context
订单系统需要与库存系统之间进行高频、低延迟的 RPC 调用。当前使用 REST/JSON 的方案存在序列化开销大、无内建流式支持的问题。团队已确定使用 Kubernetes 部署，服务发现由 Istio 提供服务。

## Decision
采用 gRPC (HTTP/2 + Protocol Buffers) 作为主要服务间通信协议。选择理由：强类型 IDL 保证接口契约；基于 HTTP/2 的流式支持适用于库存订阅场景；Protobuf 二进制序列化性能优于 JSON；与 Istio 兼容。

## Consequences
正面：性能提升约 40%；内建流式支持；强类型接口减少沟通成本。
负面：浏览器端无法直接调用 gRPC（需要 gRPC-Web 网关）；团队需要学习 Protobuf 语法；调试工具不如 REST 成熟。

## Alternatives
- REST/JSON：现有方案，维护成本低但不满足性能与流式需求。
- Apache Thrift：性能相近但社区活跃度低于 gRPC，Kubernetes 集成不如 gRPC 成熟。

## References
- ADR-20240515-002：微服务拆分方案
- gRPC 官方文档：https://grpc.io/docs/
```

**为什么这是一个良好的 ADR？**
- Context 清晰描述了问题和约束条件
- Decision 不仅说明了选择，还给出了具体选择理由
- Consequences 同时列出了正面和负面影响
- Alternatives 解释了被否定的其他方案及其原因
- References 提供了补充信息的链接

### 不良的 ADR 示例

```
## Context
需要选择消息队列。

## Decision
我们使用 RabbitMQ。

## Consequences
使用 RabbitMQ。

## Alternatives
无。
```

**为什么这是一个不良的 ADR？**
- Context 过于简单，没有说明业务场景、性能要求和约束条件
- Decision 没有解释为什么选择 RabbitMQ 而非其他方案
- Consequences 只有结果重述，没有分析正负面后果
- Alternatives 为空，无法判断是否经过了充分的方案对比

## Compliance Checklist

编写或评审 ADR 时，请逐项检查以下内容：

- [ ] ADR 编号是否正确且唯一？格式符合 `ADR-{YYYYMMDD}-{NNN}` 要求
- [ ] 是否包含 Context/Decision/Consequences/Alternatives 四要素？
- [ ] 状态是否正确标记（Proposed/Accepted/Deprecated/Superseded）？
- [ ] 是否存储在 docs/adr/ 目录下？
- [ ] 文件名是否符合 `{NNN}-{kebab-case-title.md}` 格式？
- [ ] 是否引用了相关 ADR 和标准文档？
- [ ] 是否经过至少 2 人评审？
- [ ] 是否记录了所有被考虑的替代方案及其被拒绝的理由？

## Related Standards

- [harness-engineering.md](harness-engineering.md)
- [asset-model.md](asset-model.md)
- [authoring-checklist.md](authoring-checklist.md)
