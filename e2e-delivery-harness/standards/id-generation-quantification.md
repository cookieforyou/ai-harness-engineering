---
name: id-generation-quantification
description: "ID 生成与量化标准，定义资产库中所有 ID 的前缀规范、格式规则、分配规则及各阶段的量化指标标准"
type: standard
version: "2.0.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-23
status: active
tags: ['standard', 'id-generation', 'quantification', 'quality-gates']
---

# ID Generation & Quantification Standards (ID生成与量化标准)

## 概述

本文档定义了 E2E Delivery Harness 资产库中所有 ID 的生成规则和量化标准，确保编号体系的一致性和可追溯性。

## ID 编号体系

### ID 前缀规范

| 前缀 | 用途 | 适用范围 | 示例 |
|------|------|----------|------|
| `REQ` | 需求项 | 需求规格说明书 | `REQ-001` |
| `DES` | 设计项 | 架构设计文档 | `DES-001` |
| `TASK` | 任务项 | 任务分解清单 | `TASK-001` |
| `TC` | 测试用例 | 测试用例库 | `TC-001` |
| `BUG` | 缺陷 | 缺陷跟踪系统 | `BUG-001` |
| `RISK` | 风险项 | 风险登记表 | `RISK-001` |
| `IMPROVE` | 改进项 | 改进措施跟踪 | `IMPROVE-001` |
| `DC` | 决策点 | 决策检查点 | `DC-001` |
| `V` | 验证项 | 验证清单 | `V-001` |
| `EH` | 错误处理 | 错误处理策略 | `EH-001` |
| `Q` | 质量门禁 | Quality Gates | `Q-001` |
| `MET` | 指标项 | 量化指标定义 | `MET-001` |
| `INC` | 故障项 | 故障记录 | `INC-001` |
| `CHG` | 变更项 | 变更记录 | `CHG-001` |

### ID 格式

```regex
^{PREFIX}-{NNN}$$
```

- `PREFIX`: 大写前缀 (2-7个字符)
- `-`: 分隔符
- `NNN`: 3位数字序号 (001-999)

### ID 分配规则

1. **连续性**: ID 必须连续分配，不能跳号
2. **唯一性**: 同一类型 ID 在同一文档内必须唯一
3. **可追溯性**: ID 一旦分配不可更改，废弃时保留空号

---

## 量化标准

### 需求分析阶段

| 指标 | 标准 | 测量方法 |
|------|------|----------|
| `REQ-COVER` 需求覆盖率 | ≥ 95% | 核心流程覆盖数/总流程数 |
| `REQ-TEST` 验收标准可测试率 | 100% | 每条标准可验证 |
| `REQ-PRIORITY` 优先级覆盖率 | 100% | 每个需求有优先级 |
| `REQ-STAKEHOLDER` 干系人覆盖率 | ≥ 90% | 关键干系人已识别 |

### 系统设计阶段

| 指标 | 标准 | 测量方法 |
|------|------|----------|
| `DES-COVER` 设计覆盖率 | 100% | 设计可追溯到需求 |
| `DES-INTERFACE` 接口定义完整率 | 100% | 所有接口已定义 |
| `DES-RISK` 风险识别率 | ≥ 90% | 主要风险已识别 |
| `DES-EXTEND` 扩展性评分 | ≥ 3/5 | 架构评审得分 |

### 任务分解阶段

| 指标 | 标准 | 测量方法 |
|------|------|----------|
| `TASK-GRANULARITY` 粒度达标率 | ≥ 90% | 90%任务在1-3天 |
| `TASK-DEPENDENCY` 依赖完整率 | 100% | 无循环依赖 |
| `TASK-ESTIMATE` 估算准确率 | ±20% | 与实际工时对比 |
| `TASK-PRIORITY` 优先级覆盖率 | 100% | 每任务有优先级 |

### 开发实现阶段

| 指标 | 标准 | 测量方法 |
|------|------|----------|
| `DEV-COVERAGE` 单元测试覆盖率 | ≥ 80% | 行覆盖率 |
| `DEV-COMPLIANCE` 代码规范符合率 | 100% | Linting 通过率 |
| `DEV-SECURITY` 安全问题数 | 0 Critical/High | SAST 扫描 |
| `DEV-DOC` 文档完整率 | ≥ 90% | 关键代码有注释 |

### 测试验证阶段

| 指标 | 标准 | 测量方法 |
|------|------|----------|
| `TEST-COVER` 用例执行率 | ≥ 95% | 已执行/总数 |
| `TEST-PASS` 用例通过率 | ≥ 90% | 通过/已执行 |
| `TEST-BLOCK` 阻塞缺陷率 | 0% | 阻塞发布缺陷数 |
| `TEST-REGRESSION` 回归覆盖率 | ≥ 80% | 变更影响覆盖 |

### 部署发布阶段

| 指标 | 标准 | 测量方法 |
|------|------|----------|
| `DEPLOY-SUCCESS` 部署成功率 | ≥ 99% | 成功次数/总次数 |
| `DEPLOY-TIME` 部署耗时 | ≤ 30min | 单次部署时长 |
| `DEPLOY-ROLLBACK` 回滚次数 | ≤ 5% | 回滚次数/部署次数 |
| `DEPLOY-VALIDATE` 验证通过率 | 100% | 检查项通过/总项 |

### 监控运维阶段

| 指标 | 标准 | 测量方法 |
|------|------|----------|
| `MON-COVER` 监控覆盖率 | 100% | 黄金指标覆盖 |
| `MON-ALERT` 告警准确率 | ≥ 90% | 真实告警/总告警 |
| `MON-SLO` SLO 达成率 | ≥ 99.5% | 实际可用性 |
| `MON-MTTR` MTTR | ≤ 30min | 平均恢复时间 |

---

## 质量门禁 (Quality Gates) 标准

### QG-1: 需求评审通过

```yaml
gate: QG-1
name: 需求评审通过
stage: requirement-analysis
criteria:
  - REQ-COVER ≥ 95%
  - REQ-TEST = 100%
  - 评审签字完成
```

### QG-2: 设计评审通过

```yaml
gate: QG-2
name: 设计评审通过
stage: system-design
criteria:
  - DES-COVER = 100%
  - DES-INTERFACE = 100%
  - 技术评审通过
```

### QG-3: 开发提测

```yaml
gate: QG-3
name: 开发提测
stage: development
criteria:
  - DEV-COVERAGE ≥ 80%
  - DEV-COMPLIANCE = 100%
  - 无 Critical/High 安全问题
```

### QG-4: 测试通过

```yaml
gate: QG-4
name: 测试通过
stage: testing
criteria:
  - TEST-COVER ≥ 95%
  - TEST-PASS ≥ 90%
  - TEST-BLOCK = 0
```

### QG-5: 部署就绪

```yaml
gate: QG-5
name: 部署就绪
stage: deployment
criteria:
  - 测试报告已签发
  - 回滚方案已就绪
  - 监控已配置
```

### QG-6: 上线确认

```yaml
gate: QG-6
name: 上线确认
stage: deployment
criteria:
  - 健康检查 100% 通过
  - 错误率 < 0.1%
  - 响应时间 < SLA
```

---

## 相关资产

- [naming-conventions.md](../standards/naming-conventions.md)
- [output-quality-rubric.md](../standards/output-quality-rubric.md)
- [harness-engineering.md](../harness-engineering.md)
- [lifecycle.md](../standards/lifecycle.md)
- [asset-model.md](../standards/asset-model.md)
