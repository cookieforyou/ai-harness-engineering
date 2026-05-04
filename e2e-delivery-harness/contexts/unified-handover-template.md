# Unified Handover Context Template (统一交接上下文模板)

## 概述

本文档定义了 E2E 交付全流程中各阶段交接的标准化模板，确保阶段间信息传递的完整性和一致性。

## 交接时机

```
┌─────────────────────────────────────────────────────────┐
│  Stage 1: 需求分析                                       │
│  └── Handover ──→ Stage 2: 系统设计                      │
│                                                              │
│  Stage 2: 系统设计                                          │
│  └── Handover ──→ Stage 3: 任务分解                        │
│                                                              │
│  Stage 3: 任务分解                                          │
│  └── Handover ──→ Stage 4: 开发实现                         │
│                                                              │
│  Stage 4: 开发实现                                           │
│  └── Handover ──→ Stage 5: 测试验证                          │
│                                                              │
│  Stage 5: 测试验证                                           │
│  └── Handover ──→ Stage 6: 部署发布                         │
│                                                              │
│  Stage 6: 部署发布                                           │
│  └── Handover ──→ Stage 7: 监控运维                         │
└─────────────────────────────────────────────────────────┘
```

## 统一交接模板

### 标准 Handover 格式

```yaml
handover_context:
  # ========== 基础信息 ==========
  handover_id: "HANDOVER-{STAGE_FROM}-{STAGE_TO}-{NNN}"
  timestamp: "{YYYY-MM-DD HH:MM:SS}"
  version: "{版本号}"
  
  # ========== 交接方信息 ==========
  from:
    stage: "{阶段名称}"
    owner: "{负责人姓名}"
    agent: "{使用的Agent}"
    completion_rate: "{完成百分比}"
  
  # ========== 接收方信息 ==========
  to:
    stage: "{目标阶段名称}"
    expected_owner: "{期望负责人}"
  
  # ========== 交付物清单 ==========
  deliverables:
    - id: "{交付物ID}"
      name: "{交付物名称}"
      path: "{文件路径}"
      status: "COMPLETED|IN_PROGRESS|BLOCKED"
      quality_check: "PASS|FAIL|PENDING"
      notes: "{备注}"
  
  # ========== 关键数据传递 ==========
  data_transfer:
    # 关键输入参数
    inputs:
      - key: "{参数名}"
        value: "{参数值}"
        source: "{来源}"
    
    # 关键输出结果
    outputs:
      - key: "{结果名}"
        value: "{结果值}"
        impact: "{影响说明}"
    
    # 上下文继承
    context_inherited:
      - context_key: "{上下文键}"
        inherited_from: "{来源阶段}"
        usage: "{使用说明}"
  
  # ========== 状态摘要 ==========
  summary:
    total_items: N                    # 总项数
    completed: N                      # 已完成
    in_progress: N                    # 进行中
    blocked: N                        # 阻塞
    completion_rate: "{百分比}"
  
  # ========== 未解决问题 ==========
  open_issues:
    blocking:
      - id: "{问题ID}"
        title: "{问题标题}"
        severity: "BLOCKER|MAJOR|MINOR"
        owner: "{负责人}"
        due_date: "{截止日期}"
        blocking_reason: "{阻塞原因}"
    
    non_blocking:
      - id: "{问题ID}"
        title: "{问题标题}"
        severity: "MAJOR|MINOR|COMMENT"
        owner: "{负责人}"
        notes: "{说明}"
  
  # ========== 风险传递 ==========
  risks_transferred:
    - risk_id: "{风险ID}"
      title: "{风险标题}"
      likelihood: "HIGH|MEDIUM|LOW"
      impact: "HIGH|MEDIUM|LOW"
      mitigation: "{缓解措施}"
      status: "OPEN|MITIGATED|CLOSED"
  
  # ========== 下一步行动 ==========
  next_actions:
    - action: "{行动描述}"
      owner: "{负责人}"
      due_date: "{截止日期}"
      priority: "P0|P1|P2"
      dependencies: "{依赖项}"
  
  # ========== 确认签字 ==========
  sign_off:
    from_owner: "{交接方签字} / {日期}"
    to_owner: "{接收方签字} / {日期}"
    reviewer: "{评审签字} / {日期}"
    notes: "{签字备注}"
```

## 分阶段 Handover 模板

### H1: 需求 → 设计

```yaml
handover_requirement_to_design:
  handover_id: "HANDOVER-REQ-DES-001"
  
  deliverables:
    - id: "REQ-001"
      name: "需求规格说明书"
      path: "/requirements/spec.md"
      status: "COMPLETED"
    
    - id: "REQ-TEST-001"
      name: "验收标准清单"
      path: "/requirements/acceptance-criteria.md"
      status: "COMPLETED"
    
    - id: "REQ-STAKE-001"
      name: "干系人清单"
      path: "/requirements/stakeholders.md"
      status: "COMPLETED"
  
  design_inputs:
    business_goals: "{业务目标描述}"
    success_metrics: "{成功指标}"
    constraints: "{约束条件}"
    assumptions: "{假设条件}"
  
  key_requirements:
    - id: "REQ-001"
      title: "{需求标题}"
      priority: "P0"
      complexity: "HIGH|MEDIUM|LOW"
      design_impact: "{设计影响说明}"
```

### H2: 设计 → 任务分解

```yaml
handover_design_to_task:
  handover_id: "HANDOVER-DES-TASK-001"
  
  deliverables:
    - id: "DES-001"
      name: "架构设计文档"
      path: "/design/architecture.md"
      status: "COMPLETED"
    
    - id: "DES-API-001"
      name: "接口定义"
      path: "/design/api-spec.md"
      status: "COMPLETED"
    
    - id: "DES-DB-001"
      name: "数据模型"
      path: "/design/data-model.md"
      status: "COMPLETED"
  
  task_inputs:
    architecture_overview: "{架构概览}"
    tech_stack: "{技术栈}"
    module_boundaries: "{模块边界}"
    interface_contracts: "{接口契约}"
```

### H3: 任务分解 → 开发

```yaml
handover_task_to_development:
  handover_id: "HANDOVER-TASK-DEV-001"
  
  deliverables:
    - id: "TASK-LIST-001"
      name: "任务分解清单"
      path: "/tasks/task-list.md"
      status: "COMPLETED"
    
    - id: "SPRINT-PLAN-001"
      name: "迭代计划"
      path: "/tasks/sprint-plan.md"
      status: "COMPLETED"
  
  development_inputs:
    sprint_scope: "{Sprint范围}"
    team_capacity: "{团队产能}"
    dependencies: "{任务依赖}"
    priorities: "{优先级排序}"
```

### H4: 开发 → 测试

```yaml
handover_development_to_test:
  handover_id: "HANDOVER-DEV-TEST-001"
  
  deliverables:
    - id: "CODE-001"
      name: "源代码"
      path: "/src"
      status: "COMPLETED"
      quality_checks:
        coverage: "≥80%"
        linting: "PASS"
        security: "PASS"
    
    - id: "TEST-UNIT-001"
      name: "单元测试"
      path: "/tests/unit"
      status: "COMPLETED"
    
    - id: "DEV-DOC-001"
      name: "开发文档"
      path: "/docs/dev-guide.md"
      status: "COMPLETED"
  
  test_inputs:
    build_artifacts: "{构建产物路径}"
    test_data: "{测试数据}"
    known_issues: "{已知问题}"
```

### H5: 测试 → 部署

```yaml
handover_test_to_deploy:
  handover_id: "HANDOVER-TEST-DEPLOY-001"
  
  deliverables:
    - id: "TEST-REPORT-001"
      name: "测试报告"
      path: "/reports/test-report.md"
      status: "COMPLETED"
    
    - id: "TEST-CASES-001"
      name: "测试用例"
      path: "/tests/test-cases.md"
      status: "COMPLETED"
    
    - id: "BUG-LIST-001"
      name: "缺陷清单"
      path: "/reports/bug-list.md"
      status: "COMPLETED"
  
  test_summary:
    total_cases: N
    passed: N
    failed: N
    pass_rate: "{百分比}"
    blocking_bugs: N
  
  deploy_inputs:
    build_package: "{部署包路径}"
    environment: "{目标环境}"
    rollback_version: "{回滚版本}"
```

### H6: 部署 → 监控

```yaml
handover_deploy_to_monitor:
  handover_id: "HANDOVER-DEPLOY-MON-001"
  
  deliverables:
    - id: "DEPLOY-REPORT-001"
      name: "部署报告"
      path: "/reports/deploy-report.md"
      status: "COMPLETED"
    
    - id: "CONFIG-001"
      name: "配置清单"
      path: "/config/production.md"
      status: "COMPLETED"
  
  monitor_inputs:
    deployed_version: "{部署版本}"
    health_endpoints: "{健康检查端点}"
    metrics_to_watch: "{关键指标}"
    alert_thresholds: "{告警阈值}"
    runbook: "{运维手册路径}"
```

---

## Handover 检查清单

### 交接前检查

```markdown
## Handover 前检查

### 交付物检查
- [ ] 所有交付物已完成
- [ ] 质量检查已通过
- [ ] 文档已归档

### 数据完整性
- [ ] 输入数据已传递
- [ ] 输出数据已记录
- [ ] 上下文已继承

### 问题跟踪
- [ ] 阻塞问题已记录
- [ ] 非阻塞问题已记录
- [ ] 风险已传递

### 确认签字
- [ ] 交接方已签字
- [ ] 接收方已确认
```

### 接收后检查

```markdown
## Handover 接收检查

### 完整性检查
- [ ] 交付物清单已接收
- [ ] 数据传递已确认
- [ ] 问题列表已了解

### 理解确认
- [ ] 关键需求已理解
- [ ] 技术约束已了解
- [ ] 风险已识别

### 计划确认
- [ ] 下一步行动已明确
- [ ] 责任人已确认
- [ ] 截止日期已确认

### 签字确认
- [ ] 已签字接收
```

---

## Associated Assets

| 资产类型 | 文件路径 |
|----------|----------|
| 交接模板 | `contexts/handover-context.template.md` |
| 全局上下文 | `contexts/global-context.md` |
| 输出验证 | `evaluations/output-validation-checklist.md` |
| ID 生成规范 | `standards/id-generation-quantification.md` |
