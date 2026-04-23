# E2E Delivery Harness - AI Engineering Asset Library

## 项目概述

E2E Delivery Harness 是一套面向软件交付全流程的 AI 工程化资产库，旨在为团队提供标准化、可复用的 AI 工作流模板，覆盖从需求分析到监控运维的完整生命周期。

## 核心价值

- **标准化交付流程**：统一的阶段划分、输入输出规范和质量检查标准
- **角色化 AI 协作**：定义清晰的 AI 角色职责，支持多角色协同
- **可复用资产沉淀**：积累最佳实践，形成可迭代的资产库
- **质量一致性保障**：通过规范和检查清单确保交付质量

## 目录结构

```
e2e-delivery-harness/
├── agents/              # AI 角色代理定义
├── evaluations/         # 评估与检查清单
├── instructions/        # 操作指令集
├── prompts/             # AI 提示词模板
├── scenarios/           # 业务场景定义
├── skills/              # AI 技能模块
├── standards/           # 规范与标准
├── templates/           # 资产模板
├── README.md            # 项目说明
├── INTRODUCTION.zh.md   # 中文介绍
├── USAGE.zh.md          # 中文使用指南
└── copilot-instructions.md
```

## 交付阶段

| 阶段 | 角色 | 核心产物 |
|------|------|----------|
| 需求分析与规划 | Requirement Analyst | 需求规格说明书、业务模型 |
| 系统设计 | System Designer | 架构设计文档、技术方案 |
| 任务拆分 | Task Decomposer | 任务分解清单、依赖关系图 |
| 开发实现 | Developer | 源代码、接口文档、单元测试 |
| 测试验证 | Tester | 测试用例、测试报告、缺陷报告 |
| 部署与发布 | DevOps Engineer | 部署包、部署文档、回滚方案 |
| 监控与运维 | SRE Monitor | 监控指标、告警规则、运维手册 |

## 快速开始

请参阅 [USAGE.zh.md](./USAGE.zh.md) 了解详细使用方法。

## License

MIT
