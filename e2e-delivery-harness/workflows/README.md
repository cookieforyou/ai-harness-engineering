# Workflows - 工作流定义

Workflows 是**端到端工作流**定义，将多个 Scenario 按特定顺序组合，形成完整的交付流程。

## 概述

Workflows 提供：

- **Pipeline 定义**：完整的端到端流程编排
- **阶段组合**：多个 Scenario 的有序连接
- **数据传递**：阶段间的输入输出规范
- **回退策略**：异常情况下的处理机制

## 目录结构

```
workflows/
├── README.md                    # 本文档
├── e2e-delivery.pipeline.md    # E2E 交付全流程
├── requirement-to-design.pipeline.md    # 需求到设计流程
├── development-cycle.pipeline.md        # 开发周期流程
└── incident-response.pipeline.md       # 故障响应流程
```

## Pipeline 模型

```yaml
---
name: pipeline-name
type: pipeline
version: "1.0"
description: 流程描述
stages: [stage1, stage2, ...]
---
```

### Pipeline 结构

```markdown
# Pipeline Name

## Overview
流程概述

## Stage Flow
阶段流程图

## Stages
### Stage 1: [Name]
- Scenario: [link]
- Entry Criteria: [criteria]
- Exit Criteria: [criteria]

### Stage 2: [Name]
...

## Data Flow
数据流向

## Error Handling
异常处理
```

## 预定义 Pipeline

### E2E Delivery Pipeline

完整覆盖 7 个交付阶段的端到端流程：

```
需求分析 → 系统设计 → 任务拆分 → 开发实现 → 测试验证 → 部署发布 → 监控运维
```

## 使用方式

1. **选择 Pipeline**：根据任务选择合适的流程
2. **按序执行**：按 Pipeline 定义的顺序执行各 Stage
3. **验证交接**：每个 Stage 完成后验证输出
4. **处理异常**：按回退策略处理问题

## 相关资产

- **Scenarios**: [../scenarios/](..//scenarios/) - 场景定义
- **Contexts**: [../contexts/](..//contexts/) - 共享上下文
