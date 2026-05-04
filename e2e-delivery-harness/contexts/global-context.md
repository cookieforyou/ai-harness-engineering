---
name: global-context
type: context
version: "1.0"
description: 贯穿全流程的全局上下文定义
scope: all-stages
---

# Global Context - 全局上下文

## 项目元数据

```yaml
project:
  name: ""                    # 项目名称
  code: ""                    # 项目代码 (如: PRJ-001)
  version: "1.1.0"            # 当前版本
  stage: "init"               # 当前阶段
  owner: ""                   # 项目负责人
  description: ""             # 项目描述

metadata:
  created_at: ""              # 创建时间 (ISO 8601)
  updated_at: ""              # 更新时间 (ISO 8601)
  created_by: ""              # 创建人
  tags: []                    # 项目标签
  
status:
  overall: "in_progress"      # 整体状态: init/in_progress/paused/completed
  quality: "pending"          # 质量状态: pending/approved/rejected
  risk_level: "medium"        # 风险等级: low/medium/high/critical
```

## 团队上下文

```yaml
team:
  name: ""                    # 团队名称
  members: []                 # 团队成员列表
  lead: ""                    # 团队负责人
  communication_channel: ""    # 沟通渠道
  
roles:
  product_owner: ""            # 产品负责人
  tech_lead: ""               # 技术负责人
  quality_lead: ""            # 质量负责人
  devops_lead: ""             # 运维负责人
```

## 时间线上下文

```yaml
timeline:
  start_date: ""              # 计划开始日期
  end_date: ""                # 计划结束日期
  current_iteration: 1        # 当前迭代
  total_iterations: 1        # 总迭代数
  
milestones:
  - name: ""                  # 里程碑名称
    date: ""                  # 计划日期
    status: "pending"          # 状态
    deliverables: []          # 交付物
```

## 技术上下文

```yaml
tech_stack:
  languages: []                # 编程语言
  frameworks: []               # 框架
  databases: []                # 数据库
  infrastructure: []           # 基础设施
  tools: []                    # 工具链

codebase:
  repo_url: ""                # 代码仓库地址
  branch_strategy: ""          # 分支策略
  ci_cd_pipeline: ""          # CI/CD 配置
```

## 环境上下文

```yaml
environments:
  development:
    url: ""                   # 开发环境地址
    status: "active"          # 状态
  staging:
    url: ""                   # 预发环境地址
    status: "pending"          # 状态
  production:
    url: ""                   # 生产环境地址
    status: "pending"         # 状态
```

## 质量标准上下文

```yaml
quality_standards:
  code_coverage_min: 70       # 最低代码覆盖率
  test_pass_rate_min: 95      # 最低测试通过率
  doc_completeness: "required" # 文档完整性要求
  security_scan: "required"    # 安全扫描要求

review_requirements:
  code_review: true           # 需要代码审查
  design_review: true          # 需要设计审查
  test_review: true           # 需要测试审查
```

## 约束上下文

```yaml
constraints:
  budget: null                # 预算限制
  timeline: null              # 时间限制
  resources: null             # 资源限制
  tech_limitations: []        # 技术限制

assumptions:
  - ""                        # 假设条件
```

## 相关上下文

- [Project Context Template](./project-context.template.md) - 项目上下文模板
- [Handover Context Template](./handover-context.template.md) - 交接上下文模板
