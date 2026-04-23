---
name: handover-context
type: template
version: "1.0"
description: 阶段间交接上下文模板
scope: inter-stage
---

# Handover Context Template - 交接上下文模板

## 使用说明

每次阶段间交接时，生成并填充此模板，确保信息的完整传递。

---

## 交接基本信息

```yaml
handover:
  id: ""                      # 交接单编号 (如: HO-RA-SD-001)
  from_stage: ""              # 源阶段
  to_stage: ""                # 目标阶段
  timestamp: ""                # 交接时间 (ISO 8601)
  
  initiator:
    name: ""                  # 交接发起人
    role: ""                   # 角色
    signature: ""              # 签字确认
    
  recipient:
    name: ""                  # 交接接收人
    role: ""                   # 角色
    signature: ""              # 签字确认
```

---

## 阶段总结

### 完成情况

```yaml
completion:
  status: "completed"          # completed/partial/incomplete
  summary: ""                  # 阶段总结
  
  metrics:
    planned_items: 0           # 计划项数
    completed_items: 0         # 完成项数
    deliverables_count: 0      # 交付物数量
    
  quality_gates:
    - gate: ""                 # 门禁名称
      status: "passed"        # passed/failed/pending
      verified_by: ""          # 验证人
```

### 关键产出

```yaml
deliverables:
  - name: ""                  # 交付物名称
    path: ""                  # 文件路径
    type: "document"          # document/code/config/data
    version: ""               # 版本号
    size: ""                  # 文件大小
    hash: ""                  # 文件哈希
    verified: true            # 已验证
    notes: ""                 # 备注
```

---

## 上下文传递

### 全局上下文更新

```yaml
context_updates:
  project:
    stage: ""                 # 更新为下一阶段
    updated_at: ""            # 更新时间
    
  metrics:
    stage_completed: 0        # 已完成阶段数
    total_stages: 7          # 总阶段数
    progress_percent: 0       # 进度百分比
```

### 阶段特定数据

```yaml
stage_data:
  # 根据阶段填充相应数据
  # 见各阶段的 Context 定义
```

---

## 关键决策记录

```yaml
decisions:
  - id: ""                    # 决策编号
    date: ""                  # 决策日期
    topic: ""                 # 决策主题
    decision: ""              # 决策内容
    rationale: ""             # 决策依据
    made_by: ""               # 决策人
    impact: ""                # 影响范围
    
  risks_accepted:
    - risk: ""                # 风险描述
      mitigation: ""          # 缓解措施
      accepted_by: ""         # 接受人
```

---

## 未解决问题

```yaml
open_issues:
  - id: ""                    # 问题编号
    title: ""                 # 问题标题
    description: ""           # 问题描述
    priority: "medium"        # high/medium/low
    owner: ""                 # 负责人
    due_date: ""              # 计划解决日期
    blocking: true            # 是否阻塞后续
    
  dependencies:
    - issue_id: ""           # 依赖的问题
      dependency_type: ""     # depends_on/blocks/is_blocked_by
      
  assumptions:
    - ""                      # 基于的假设
```

---

## 风险传递

```yaml
risks:
  identified:
    - id: ""                  # 风险编号
      description: ""         # 风险描述
      probability: "medium"   # high/medium/low
      impact: "medium"       # high/medium/low
      mitigation: ""          # 缓解措施
      contingency: ""         # 应急预案
      
  escalated:
    - ""                      # 升级的风险
```

---

## 建议与备注

```yaml
recommendations:
  - ""                        # 建议内容
  
notes:
  - ""                        # 其他备注
  
next_steps:
  - ""                        # 建议的后续步骤
```

---

## 交接清单

### 发起人确认

- [ ] 所有交付物已准备完毕
- [ ] 交付物已验证正确性
- [ ] 交接文档已填写完整
- [ ] 已通知接收人

### 接收人确认

- [ ] 已收到所有交付物
- [ ] 已验证交付物完整性
- [ ] 已理解交接内容
- [ ] 无阻塞性问题

### 签名

| 角色 | 姓名 | 签名 | 日期 |
|------|------|------|------|
| 发起人 | | | |
| 接收人 | | | |
| 见证人 | | | |

---

## 使用示例

### 需求分析 → 系统设计 交接

```yaml
handover:
  id: "HO-RA-SD-001"
  from_stage: "requirement-analysis"
  to_stage: "system-design"
  timestamp: "2024-01-15T10:30:00Z"
  
  initiator:
    name: "张三"
    role: "需求分析师"
    
  recipient:
    name: "李四"
    role: "系统设计师"

deliverables:
  - name: "需求规格说明书"
    path: "artifacts/requirements-spec-v1.2.md"
    type: "document"
    verified: true
    
decisions:
  - id: "DEC-001"
    topic: "技术选型"
    decision: "采用微服务架构"
    rationale: "支持高并发和快速迭代"
    made_by: "技术负责人"

open_issues:
  - id: "ISSUE-001"
    title: "第三方支付接口对接"
    priority: "high"
    blocking: true
```
