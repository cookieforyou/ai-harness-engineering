---
name: design-system
description: "系统设计场景，负责设计系统架构、技术方案、数据模型和接口规范"
version: "1.2.0"
type: scenario
category: design
stage: system-design
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: [design, architecture, technical]
---
# Design System Scenario

## Purpose

基于需求规格说明书，设计系统的整体架构、技术方案和数据模型，为开发实现提供技术指导。

### Business Value

- **技术风险降低**: 通过系统化架构设计识别潜在技术风险和瓶颈
- **开发效率提升**: 清晰的架构蓝图和接口契约减少团队沟通成本
- **可维护性增强**: 模块化设计和单一职责原则提升代码可维护性
- **可扩展性保障**: 预留扩展点支持业务增长和技术演进

## Chain of Thought (思维链)

### Think-Aloud Protocol (强制遵循)

```
[THINK] Step 1: 理解系统边界和范围
   ├─ 问：系统的边界和核心模块是什么？外部依赖有哪些？
   ├─ 验证：与需求规格说明书对照，确认功能清单完整
   └─ 检查：识别所有外部系统集成点和数据流
   ↓
[ANALYZE] Step 2: 分析非功能性需求和技术约束
   ├─ 问：性能、安全、可用性的量化指标是什么？团队技术能力如何？
   ├─ 验证：指标可测量且合理，技术约束明确
   └─ 检查：预算和时间约束已考虑
   ↓
[DESIGN] Step 3: 设计系统架构和模块划分
   ├─ 问：架构风格是否适合业务需求？模块间如何解耦？
   ├─ 验证：满足非功能性需求，符合单一职责原则
   └─ 检查：模块高内聚低耦合，技术栈选择合理
   ↓
[EVALUATE] Step 4: 设计数据模型和接口方案
   ├─ 问：核心实体关系是否清晰？接口契约是否稳定？
   ├─ 验证：满足业务场景，符合范式和扩展性要求
   └─ 检查：API设计规范，版本兼容性已考虑
   ↓
[DOCUMENT] Step 5: 输出系统设计文档
   ├─ 生成系统架构图、组件图、部署图
   ├─ 编写数据模型（ER图、数据字典）
   └─ 定义接口规范（API文档、协议规范）
   ↓
[VALIDATE] Step 6: 评审确认并准备交接
   ├─ 组织技术评审会议，收集反馈
   ├─ 根据反馈修订设计方案
   └─ 获得技术委员会签字确认，准备交接给任务拆分阶段
```

## Decision Checkpoints (决策检查点)

| ID | 决策点 | 触发条件 | 决策选项 | 选择标准 | 记录位置 |
|----|--------|----------|----------|----------|----------|
| DC-001 | 架构风格选择 | 完成非功能性分析后 | 单体/微服务/事件驱动/Serverless | 基于业务复杂度、团队规模、扩展性需求综合评估 | 架构设计文档 |
| DC-002 | 技术栈选型 | 架构确定后 | 具体技术框架和工具 | 成熟度、社区支持、团队熟悉度、长期维护成本 | 技术方案文档 |
| DC-003 | 模块划分策略 | 设计核心模块时 | 按功能/按领域/按层次 | 内聚性、耦合度、可维护性、团队组织结构 | 模块设计文档 |
| DC-004 | 数据存储方案 | 数据建模完成后 | SQL/NoSQL/混合/缓存层 | 数据结构、查询模式、一致性要求、扩展性 | 数据设计文档 |
| DC-005 | 通信协议选择 | 定义接口规范时 | REST/gRPC/GraphQL/消息队列 | 实时性要求、客户端类型、性能需求 | API设计文档 |

## Error Handling (错误处理)

> **AI 在执行过程中遇到以下情况时的处理策略**

### Error Scenario 1: 架构决策困难

**识别信号**: 
- 多种架构方案各有优劣，难以抉择
- 团队对架构方向存在分歧
- 技术评估结果不明确

**处理流程**:
```
IF 检测到架构决策困难
THEN
  1. 列出各方案的优缺点对比表（功能、性能、成本、风险）
  2. 根据非功能性需求权重评分（性能30%、可维护性25%、成本20%、风险25%）
  3. 选择综合得分最高的方案
  4. IF 分数接近 THEN 选择团队最熟悉的方案，降低实施风险
  5. 记录决策依据和备选方案评估（ADR）
  6. 提交技术委员会评审确认
END
```

**降级方案**: 采用保守方案（团队最熟悉的），预留重构空间，制定演进路线图

**升级条件**: 团队无法达成共识或风险等级为High，需要CTO或架构委员会介入

---

### Error Scenario 2: 技术风险识别

**识别信号**: 
- 关键技术存在不确定性或团队缺乏经验
- 新技术未经生产环境验证
- 依赖外部因素（第三方服务、开源项目）

**处理流程**:
```
IF 检测到技术风险
THEN
  1. 识别所有技术风险点（新技术、复杂算法、外部依赖）
  2. 评估风险概率和影响（高/中/低）
  3. 制定应对策略：规避/转移/缓解/接受
  4. IF 高风险 THEN 安排POC验证或增加技术预研阶段
  5. 在设计方案中标注风险及应对措施
  6. 更新风险管理文档
END
```

**降级方案**: 采用成熟技术替代，或分阶段实施（先MVP验证，再全面推广）

**升级条件**: 风险等级为High/Critical且无有效缓解措施，需要技术负责人和项目管理者决策

---

### Error Scenario 3: 需求与设计冲突

**识别信号**: 
- 设计方案无法满足某些需求
- 需求之间存在矛盾（如高性能vs低成本）
- 技术约束导致需求调整

**处理流程**:
```
IF 检测到需求与设计冲突
THEN
  1. 分析冲突的根本原因（需求不完整、技术限制、资源不足）
  2. 与Requirement Analyst确认需求优先级和可调整范围
  3. 提出设计调整建议或需求修改建议
  4. IF 影响核心功能 THEN 组织架构评审会议讨论
  5. 记录冲突和解决方案（ADR）
  6. 更新需求规格说明书或设计方案
END
```

**降级方案**: 暂时标注为已知问题，在Handover中说明，留待后续迭代解决

**升级条件**: 影响核心功能实现或需要重大设计变更，需要产品经理和系统设计师共同决策

## Quality Metrics (质量指标)

### Key Performance Indicators (KPIs)

| KPI ID | 指标名称 | 目标值 | 计算公式 | 验证方法 | 权重 |
|--------|----------|--------|----------|----------|------|
| KPI-001 | DESIGN-COVERAGE | ≥95% | (有设计的功能数/总功能数) × 100% | 需求-设计映射表 | 25% |
| KPI-002 | ARCH-REVIEW-PASS | ≥90% | (通过的评审项/总评审项) × 100% | 技术评审记录 | 25% |
| KPI-003 | ADR-COMPLETENESS | 100% | (有ADR的决策数/总决策数) × 100% | ADR文档检查 | 20% |
| KPI-004 | RISK-IDENTIFICATION | ≥95% | (已识别风险数/实际风险数) × 100% | 风险评估回顾 | 15% |
| KPI-005 | DOC-QUALITY | ≥85/100 | 文档完整性、清晰度、可执行性评分 | 文档审查 | 15% |

**综合评分计算**: 
```
Quality Score = (KPI-001 × 0.25) + (KPI-002 × 0.25) + (KPI-003 × 0.20) + (KPI-004 × 0.15) + (KPI-005 × 0.15)
合格: ≥70分 | 优秀: ≥85分 | 卓越: ≥95分
```

### Validation Checklist (验证清单)

**完整性验证 (Completeness)**:
- [ ] 所有功能需求都有对应的设计实现
- [ ] 非功能性需求（性能、安全、可用性）得到满足
- [ ] 架构文档包含所有必需章节（概述、架构、模块、数据、接口、部署、风险）
- [ ] 关键设计决策有ADR记录

**一致性验证 (Consistency)**:
- [ ] 术语和命名在整个设计文档中保持一致
- [ ] 架构图与文字描述一致
- [ ] 数据模型与接口定义一致
- [ ] 与其他相关文档（需求规格、数据库设计）协调一致

**可行性验证 (Feasibility)**:
- [ ] 技术方案在团队能力范围内
- [ ] 预算和时间约束可满足
- [ ] 技术风险可控，有应对策略
- [ ] 依赖的外部服务或组件可获得

**规范性验证 (Compliance)**:
- [ ] 遵循架构设计最佳实践（如SOLID、DRY）
- [ ] 符合安全和合规要求（GDPR、ISO 27001等）
- [ ] API设计符合RESTful规范或公司标准
- [ ] 文档格式规范，图表清晰

## Related Assets (关联资产)

| Asset Type | Path | Description |
|------------|------|-------------|
| Agent | `../../agents/design-system.agent.md` | 系统设计Agent角色定义 |
| Prompt | `../../prompts/design-system.prompt.md` | 系统设计提示词模板 |
| Skill | `../../skills/design-system/SKILL.md` | 系统设计技能包 |
| Instruction | `../../instructions/design-system.instructions.md` | 系统设计技术指令 |

## Related Resources (相关资源)

- **Standards**: 
  - [ADR Template](../standards/adr-template.md) - 架构决策记录模板
  - [API Design Guidelines](../standards/api-design-guidelines.md) - API设计规范
- **Templates**: 
  - [System Design Document Template](../templates/system-design-doc.template.md) - 系统设计文档模板
  - [Architecture Diagram Template](../templates/architecture-diagram.template.md) - 架构图模板
- **Evaluations**: 
  - [Architecture Review Checklist](../evaluations/architecture-review-checklist.md) - 架构评审检查清单
  - [Design Quality Assessment](../evaluations/design-quality-assessment.md) - 设计质量评估表
