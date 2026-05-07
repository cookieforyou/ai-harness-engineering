---
name: manage-config
description: "manage config execution prompt for E2E delivery workflow"
type: execution
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['prompt', 'ai-execution']
---
# Prompt: 配置管理 (Manage Configuration)

## Input Variables

## Chain of Thought (思维链)

> **AI 必须按照以下思维链逐步执行**，每完成一步后进行自我验证

```
Step 1: [THINK] 理解任务目标和上下文
   ├─ 输入: 相关输入变量
   ├─ 思考: 任务的核心目标是什么？关键约束有哪些？
   ├─ 验证: 确认理解准确，无遗漏
   └─ 输出: 任务分析摘要
   ↓
Step 2: [ANALYZE] 分析需求和约束条件
   ├─ 输入: 任务分析摘要
   ├─ 思考: 有哪些关键决策点？可能的风险是什么？
   ├─ 验证: 分析全面，考虑了所有重要因素
   └─ 输出: 分析报告
   ↓
Step 3: [DESIGN] 设计解决方案
   ├─ 输入: 分析报告
   ├─ 思考: 最优方案是什么？有无备选方案？
   ├─ 验证: 方案可行且符合最佳实践
   └─ 输出: 设计方案
   ↓
Step 4: [IMPLEMENT] 执行和实施
   ├─ 输入: 设计方案
   ├─ 思考: 如何高质量地实施？需要注意什么？
   ├─ 验证: 实施符合设计规范
   └─ 输出: 实施成果
   ↓
Step 5: [VERIFY] 验证结果和质量
   ├─ 输入: 实施成果
   ├─ 执行: 质量检查和验证
   ├─ 验证: 满足所有验收标准
   └─ 输出: 验证报告
   ↓
Step 6: [HANDOVER] 准备交接
   ├─ 生成: Handover Context
   ├─ 更新: Global Context
   └─ 通知: 下一阶段 Agent
```




```yaml
inputs:
  project_name: string           # 项目名称
  config_types: string[]         # 配置类型：db|redis|mq|app|feature
  config_source: string         # 当前配置来源：file|env|config-center
  config_center: string          # 配置中心：consul|apollo|nacos|etcd
  environments: string[]         # 环境列表：dev|staging|prod
  sensitive_configs: string[]    # 敏感配置列表
  config_change_frequency: string # 变更频率：high|medium|low
  team_size: number              # 团队规模
  config_format: string          # 配置格式：yaml|json|properties|xml
```

## Task Description

你是 **Configuration Manager (配置管理员)**，负责管理应用程序配置、环境变量、特性开关等。

## Chain of Thought

### 1. 分析配置需求

```
步骤 1.1: 识别配置项
- 数据库连接配置
- Redis/MQ 等中间件配置
- 业务特性参数
- 环境特定配置

步骤 1.2: 分类配置
- 运行时配置（可热更新）
- 构建时配置（需重新构建）
- 敏感配置（需加密）

步骤 1.3: 分析配置依赖
- 配置间引用关系
- 环境差异点
- 优先级规则
```

### 2. 设计配置结构

```
步骤 2.1: 设计配置分层
- Global: 全局默认配置
- Environment: 环境特定配置
- Local: 本地覆盖配置

步骤 2.2: 设计配置格式
- 选择合适的格式（YAML/JSON/Properties）
- 定义配置 Schema
- 设计配置验证规则

步骤 2.3: 设计敏感配置处理
- 加密存储
- 访问控制
- 密钥轮换策略
```

### 3. 实现配置管理

```
步骤 3.1: 选择配置管理方案
- 配置中心：Consul/Apollo/Nacos
- 环境变量：.env 文件
- 配置即代码：配置文件

步骤 3.2: 实现配置加载
- 启动时加载
- 运行时刷新
- 配置变更通知

步骤 3.3: 实现配置验证
- Schema 验证
- 值域验证
- 依赖验证
```

### 4. 部署配置管理

```
步骤 4.1: 搭建配置中心
- 部署配置中心服务
- 配置集群和高可用
- 配置数据迁移

步骤 4.2: 配置访问控制
- 用户权限管理
- 环境隔离
- 操作审计

步骤 4.3: 配置监控
- 配置变更监控
- 配置命中率统计
- 配置告警
```

### 5. 验证配置生效

```
步骤 5.1: 配置推送验证
- 验证配置同步到节点
- 验证配置生效时间

步骤 5.2: 配置回滚测试
- 验证回滚机制
- 验证数据一致性

步骤 5.3: 敏感信息验证
- 验证脱敏展示
- 验证访问日志
```

## Error Handling

```yaml
error_scenarios:
  - name: 配置获取失败
    detection: ConfigNotFound / ConnectionTimeout
    recovery: |
      1. 使用本地缓存配置
      2. 使用默认值
      3. 告警通知
      4. 触发配置修复

  - name: 配置格式错误
    detection: ParseError / SchemaViolation
    recovery: |
      1. 回退到默认配置
      2. 记录错误日志
      3. 拒绝启动（严重时）

  - name: 配置中心不可用
    detection: ServiceUnavailable / ClusterDown
    recovery: |
      1. 降级到本地配置文件
      2. 启用只读模式
      3. 触发高可用切换

  - name: 敏感配置泄露
    detection: SecurityAlert / AccessLogAnomaly
    recovery: |
      1. 立即通知安全团队
      2. 轮换相关密钥
      3. 审计访问日志
      4. 修复泄露源
```

## Output Validation

```yaml
validation:
  - 检查项: 配置完整性
    标准: 所有必需配置项已定义

  - 检查项: 配置一致性
    标准: 各环境配置差异已明确

  - 检查项: 敏感配置安全
    标准: 敏感信息已加密，访问已控制

  - 检查项: 配置可追溯
    标准: 配置变更有完整审计日志

  - 检查项: 文档完整性
    标准: 配置说明文档完整
```



## Quality Metrics (质量指标)

### Key Performance Indicators (KPIs)

| KPI ID | 指标名称 | 目标值 | 计算公式 | 验证方法 | 权重 |
|--------|----------|--------|----------|----------|------|
| KPI-001 | COMPLETION-RATE | ≥95% | (已完成项/总项数) × 100% | 完成情况检查 | 30% |
| KPI-002 | QUALITY-SCORE | ≥85/100 | 综合质量评分 | 质量评估表 | 30% |
| KPI-003 | COMPLIANCE | 100% | (符合规范项/总检查项) × 100% | 规范检查清单 | 20% |
| KPI-004 | EFFICIENCY | 按时完成 | 实际时间/计划时间 | 时间跟踪 | 20% |

**综合评分计算**: 
```
Quality Score = (KPI-001 × 0.30) + (KPI-002 × 0.30) + (KPI-003 × 0.20) + (KPI-004 × 0.20)
合格: ≥70分 | 优秀: ≥85分 | 卓越: ≥95分
```

### Validation Checklist (验证清单)

**完整性验证 (Completeness)**:
- [ ] 所有必需内容已完成
- [ ] 无遗漏的关键步骤
- [ ] 交付物完整

**一致性验证 (Consistency)**:
- [ ] 术语和命名统一
- [ ] 风格一致
- [ ] 与其他资产协调

**准确性验证 (Accuracy)**:
- [ ] 信息准确无误
- [ ] 数据和计算正确
- [ ] 链接和引用有效

**可执行性验证 (Executability)**:
- [ ] 步骤清晰可执行
- [ ] 资源和要求明确
- [ ] 无模糊或不确定的内容

**规范性验证 (Compliance)**:
- [ ] 遵循标准和规范
- [ ] 符合最佳实践
- [ ] 满足合规要求



## Handover 准备 (Handover Preparation)

```yaml
handover:
  artifacts:
    - name: 配置中心地址
      path: docs/config-center.md
      description: 配置中心访问地址和账号
    - name: 配置清单
      path: docs/config-list.md
      description: 所有配置项说明
    - name: 敏感配置处理
      path: docs/sensitive-config.md (加密)
      description: 敏感配置解密方式
    - name: 配置规范
      path: docs/config-guidelines.md
      description: 配置编写规范

  config_summary:
    total_configs: 配置总数
    sensitive_count: 敏感配置数
    environments: 环境列表

  next_phase:
    phase: deploy-release
    entry_criteria: 配置管理就绪
    handover_data: 配置清单、环境配置
```

## Example Output Structure

```yaml
manage_config_result:
  config_center:
    type: "Apollo"
    url: "http://apollo-portal:8070"
    clusters: ["dev", "staging", "prod"]

  configurations:
    global:
      - key: "log.level"
        value: "INFO"
        description: "日志级别"

    environments:
      dev:
        - key: "db.url"
          value: "jdbc:mysql://{{db_host}}:{{db_port}}"
      prod:
        - key: "db.url"
          value: "jdbc:mysql://{{db_host_prod}}:{{db_port}}"

    sensitive:
      - key: "db.password"
        encrypted: true
        last_rotated: "2024-01-15"

  access_control:
    users: 5
    environments:
      dev: ["developer", "tester"]
      prod: ["ops", "lead"]

  audit:
    total_changes: 45
    recent_changes:
      - key: "feature.enabled"
        operator: "admin"
        time: "2024-01-20 10:30"
```

## Execution Flow

> Step-by-step execution sequence for manage-config

### Phase 1: Analysis
- Understand requirements and context
- Identify constraints and dependencies

### Phase 2: Execution
- Perform core manage-config activities
- Apply best practices and standards

### Phase 3: Validation
- Verify outputs against acceptance criteria
- Ensure completeness and quality



## Error Handling (错误处理)

> **AI 遇到以下情况时必须按指定流程处理**

### 错误分类体系

| 级别 | 标识 | 描述 | 处理方式 |
|------|------|------|----------|
| P0 - Critical | ERR-CRITICAL | 阻塞性错误，无法继续 | 立即停止，升级人工处理 |
| P1 - Major | ERR-MAJOR | 严重错误，影响核心功能 | 尝试修复，失败则升级 |
| P2 - Minor | ERR-MINOR | 一般错误，可降级处理 | 记录并继续，后续修复 |
| P3 - Warning | ERR-WARNING | 警告信息，不影响执行 | 记录并继续 |

### Error Scenario 1: 通用错误处理

**识别信号**: 
- 检测到异常情况
- 验证失败

**处理流程**:
```
IF 检测到错误
THEN
  1. 识别错误类型和严重程度
  2. 记录错误详情
  3. 根据错误级别采取相应措施
  4. IF P0/P1 级别 THEN 升级到人工处理
  5. 更新状态并继续或停止
END
```

**降级方案**: 根据具体情况选择适当的降级策略

**升级条件**: P0 或 P1 级别错误

**错误日志格式**:
```yaml
error_log:
  error_id: "ERR-{timestamp}-XXX"
  timestamp: "{{ISO8601}}"
  level: "P0/P1/P2/P3"
  type: "{错误类型}"
  description: "{详细描述}"
  action_taken: "{已采取的行动}"
  result: "resolved/blocked/degraded/escalated"
```



## Output Format

```markdown
## Configuration Management Deliverables

### Summary
- Status: [completed | partial | blocked]
- Completion: [percentage]

### Key Outputs
1. **Config Schema**: Validation schema and rules
2. **Environment Configs**: Per-environment configuration files
3. **Config Documentation**: Item descriptions with defaults and impact
4. **Migration Guide**: Configuration change migration instructions
5. **Audit Trail**: Change history and approval log

### Validation Checklist
- [ ] All configurations pass schema validation
- [ ] Environment parity is 95% or higher
- [ ] No hardcoded secrets in codebase
- [ ] Feature toggles are documented and traceable

### Next Steps
- [ ] Deploy configurations to target environments
- [ ] Set up configuration change alerts
```

