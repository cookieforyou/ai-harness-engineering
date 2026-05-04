---
name: incident-review
description: 故障复盘技能，提供故障分析和改进制定的方法论
type: skill
version: "1.1.0"
stage: monitoring
---

# Incident Review Skill

## Skill Overview

故障复盘是提升系统稳定性的重要手段。本技能提供故障分析的方法论、根因识别技术和改进制定流程。

## Prerequisites

1. 理解系统架构
2. 理解监控告警
3. 理解事件管理流程

## Knowledge Base

### 故障类型

| 类型 | 描述 | 示例 |
|------|------|------|
| 基础设施 | 云服务、网络、硬件 | 云厂商故障 |
| 应用 | 代码错误、配置错误 | NPE、OOM |
| 依赖 | 第三方服务、数据库 | 依赖服务故障 |
| 运维 | 部署变更、配置变更 | 发布导致故障 |

### 5 Why 分析法

通过连续追问"为什么"找出根本原因：

```
Why 1: 为什么系统宕机？
→ 因为数据库连接池耗尽

Why 2: 为什么连接池耗尽？
→ 因为有一个慢查询占用连接

Why 3: 为什么有慢查询？
→ 因为缺少索引

Why 4: 为什么缺少索引？
→ 因为上线前未做性能测试

Why 5: 为什么未做性能测试？
→ 因为没有性能测试流程

根本原因：缺乏性能测试流程
```

### Ishikawa 鱼骨图

从以下维度分析原因：
- 人（人员、技能）
- 机（设备、环境）
- 料（数据、材料）
- 法（方法、流程）
- 环（环境、依赖）

### 改进措施分类

| 类型 | 描述 | 示例 |
|------|------|------|
| 预防 | 防止故障发生 | 增加监控告警 |
| 检测 | 尽早发现问题 | 优化告警阈值 |
| 响应 | 快速恢复 | 完善应急预案 |
| 改进 | 持续优化 | 自动化流程 |

### MTTR 指标

| 指标 | 描述 | 目标 |
|------|------|------|
| MTTD | 平均检测时间 | < 5 分钟 |
| MTTR | 平均恢复时间 | < 30 分钟 |
| MTTF | 平均故障间隔 | 越长越好 |

## Procedures

### 复盘流程

1. 收集故障信息
2. 重构时间线
3. 分析直接原因
4. 识别根本原因
5. 评估影响
6. 制定改进措施
7. 编写复盘报告
8. 跟踪改进落地

### 根因分析步骤

1. 收集所有相关事实
2. 识别直接原因
3. 追问为什么
4. 确定根本原因
5. 验证根本原因

## Tools & Resources

- 日志分析工具
- 监控告警系统
- 事件管理平台
- 复盘报告模板

## Validation

### 复盘完整性检查

- [ ] 时间线完整
- [ ] 根因明确
- [ ] 影响评估充分
- [ ] 措施具体

### 改进措施检查

- [ ] 责任人明确
- [ ] 完成日期合理
- [ ] 可执行性强

## Examples

### Example：服务响应慢故障

**故障现象**：API 响应时间从 100ms 增加到 5s

**时间线**：
- T+0: 监控告警
- T+5: 定位到慢查询
- T+15: 找到问题 SQL
- T+30: 优化 SQL
- T+35: 恢复

**5 Why 分析**：
- Why: 响应慢 → 慢查询
- Why: 慢查询 → 缺少索引
- Why: 缺少索引 → 新功能未考虑
- Why: 未考虑 → 无性能测试流程
- Why: 无流程 → 未建立

**根本原因**：缺乏性能测试流程

**改进措施**：
1. 新增上线前性能测试流程
2. 增加慢查询监控
3. 建立 SQL 审核规范


## Core Knowledge

> Essential knowledge domain for review-incident execution.

### Domain Fundamentals
- [Core concept 1]
- [Core concept 2]
- [Core concept 3]

### Key Principles
1. [Principle 1]
2. [Principle 2]
3. [Principle 3]


## Best Practices

> Proven practices for review-incident excellence.

1. **Practice 1**: [Description and rationale]
2. **Practice 2**: [Description and rationale]
3. **Practice 3**: [Description and rationale]


## Common Pitfalls

> Frequent mistakes to avoid during review-incident execution.

### Pitfall 1: [Name]
**Risk**: [Description]
**Prevention**: [How to avoid]
**Impact**: [Consequences if not avoided]

### Pitfall 2: [Name]
**Risk**: [Description]
**Prevention**: [How to avoid]
**Impact**: [Consequences if not avoided]

### Pitfall 3: [Name]
**Risk**: [Description]
**Prevention**: [How to avoid]
**Impact**: [Consequences if not avoided]
