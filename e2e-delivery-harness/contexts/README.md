# Contexts - 共享上下文

Contexts 是**跨阶段共享的上下文数据**定义，确保阶段间数据传递的一致性和可追溯性。

## 概述

Contexts 提供：

- **全局上下文**：贯穿全流程的共享数据
- **阶段上下文**：特定阶段的数据结构
- **数据模板**：标准化的数据结构定义
- **默认值**：合理的默认值设置

## 目录结构

```
contexts/
├── README.md                    # 本文档
├── global-context.md           # 全局上下文定义
├── project-context.template.md # 项目上下文模板
└── handover-context.template.md # 交接上下文模板
```

## 全局上下文

### 项目元数据

```yaml
project:
  name: string           # 项目名称
  code: string           # 项目代码
  version: string        # 当前版本
  stage: string          # 当前阶段
  owner: string          # 项目负责人
  
metadata:
  created_at: datetime   # 创建时间
  updated_at: datetime   # 更新时间
  created_by: string     # 创建人
  tags: [string]         # 项目标签
```

### 团队上下文

```yaml
team:
  name: string           # 团队名称
  members: [string]      # 团队成员
  lead: string           # 团队负责人
  
roles:
  - name: string         # 角色名称
    assignee: string     # 当前负责人
    capacity: number     # 工作容量
```

## 阶段上下文

### 需求阶段

```yaml
requirement_context:
  stakeholders: [object]   # 干系人列表
  requirements: [object]  # 需求列表
  use_cases: [object]     # 用例列表
  constraints: [string]   # 约束条件
```

### 设计阶段

```yaml
design_context:
  architecture: object    # 架构设计
  components: [object]    # 组件列表
  interfaces: [object]    # 接口列表
  tech_stack: [string]    # 技术栈
```

### 开发阶段

```yaml
development_context:
  codebase: object        # 代码库信息
  dependencies: [string]  # 依赖列表
  build_config: object    # 构建配置
  test_config: object     # 测试配置
```

### 测试阶段

```yaml
testing_context:
  test_cases: [object]     # 测试用例
  test_results: object    # 测试结果
  defects: [object]       # 缺陷列表
  coverage: object        # 覆盖率数据
```

### 部署阶段

```yaml
deployment_context:
  environments: [object]   # 环境列表
  configs: object         # 配置信息
  artifacts: [object]     # 部署产物
  rollback_plan: object   # 回滚方案
```

### 运维阶段

```yaml
monitoring_context:
  metrics: [object]       # 监控指标
  alerts: [object]        # 告警规则
  runbooks: [object]      # 运维手册
  incidents: [object]     # 故障记录
```

## Handover Context

阶段间交接时必须传递的上下文：

```yaml
handover:
  from_stage: string      # 源阶段
  to_stage: string        # 目标阶段
  timestamp: datetime     # 交接时间
  
  artifacts:
    - name: string        # 产物名称
      path: string        # 产物路径
      type: string        # 产物类型
      verified: boolean   # 是否已验证
      
  context:
    summary: string       # 阶段总结
    key_decisions: [string]  # 关键决策
    open_issues: [object]    # 未解决问题
    risks: [object]          # 已知风险
```

## 使用方式

### 1. 初始化项目上下文

```markdown
## 项目初始化

1. 创建项目上下文文件
2. 填充基础元数据
3. 设置团队成员
4. 定义初始阶段
```

### 2. 阶段间传递

```markdown
## 阶段交接

1. 生成 Handover Context
2. 填充产物清单
3. 更新全局上下文
4. 验证上下文完整性
```

### 3. 上下文继承

```markdown
## 上下文继承规则

- 全局上下文：所有阶段共享
- 阶段上下文：仅当前阶段使用
- 交接上下文：跨阶段传递
```

## 相关资产

- **Workflows**: [../workflows/](..//workflows/) - 工作流定义
- **Scenarios**: [../scenarios/](..//scenarios/) - 场景定义
