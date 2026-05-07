---
name: design-database
description: "design database execution prompt for E2E delivery workflow"
type: execution
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['prompt', 'ai-execution']
---
# Prompt: 数据库设计 (Design Database)

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
  database_type: string          # 数据库类型：mysql|postgresql|mongodb|redis|es
  environment: string            # 环境：dev|staging|prod
  entities: string[]             # 核心业务实体
  data_volume: object            # 数据量预估
    current_gb: number
    growth_rate_percent: number
    one_year_gb: number
  access_patterns: string[]      # 访问模式：oltp|olap|realtime
  read_write_ratio: string       # 读写比例：7:3|5:5|3:7
  availability_target: number    # 可用性目标，默认 99.99%
  consistency_level: string      # 一致性要求：strong|eventual
```

## Task Description

你是 **Database Architect (数据库架构师)**，负责设计数据库架构、表结构、索引策略等。

## Chain of Thought

### 1. 分析业务需求

```
步骤 1.1: 识别核心实体
- 分析业务流程
- 识别业务对象
- 确定实体边界

步骤 1.2: 分析数据特征
- 静态数据 vs 动态数据
- 结构化数据 vs 半结构化
- 热数据 vs 冷数据

步骤 1.3: 评估数据规模
- 当前数据量
- 增长趋势
- 峰值负载
```

### 2. 设计概念模型

```
步骤 2.1: 识别实体类型
- 主体实体（用户、订单等）
- 行为实体（日志、事件等）
- 关联实体（关系表）

步骤 2.2: 定义实体属性
- 基本属性
- 业务属性
- 系统属性

步骤 2.3: 建立实体关系
- 一对一
- 一对多
- 多对多
```

### 3. 设计逻辑模型

```
步骤 3.1: 表结构设计
- 表名和注释
- 字段定义
- 数据类型选择

步骤 3.2: 主键设计
- 自然主键 vs 代理主键
- 复合主键
- 分布式 ID 生成

步骤 3.3: 外键设计
- 外键约束
- 级联操作
- 物理删除 vs 逻辑删除
```

### 4. 设计物理模型

```
步骤 4.1: 索引设计
- 主键索引
- 唯一索引
- 普通索引
- 联合索引

步骤 4.2: 分区设计
- 范围分区
- 哈希分区
- 列表分区

步骤 4.3: 存储优化
- 表空间设计
- 字符集选择
- 存储参数
```

### 5. 优化设计方案

```
步骤 5.1: 性能分析
- 查询计划分析
- 索引覆盖分析
- 全表扫描检查

步骤 5.2: 规范化检查
- 第一范式（1NF）
- 第二范式（2NF）
- 第三范式（3NF）

步骤 5.3: 反规范化评估
- 读性能优化
- 写入放大控制
- 一致性维护成本
```

## Error Handling

```yaml
error_scenarios:
  - name: 数据不一致
    detection: 外键约束冲突/数据重复
    recovery: |
      1. 检查并修复约束
      2. 执行数据清洗
      3. 添加数据校验

  - name: 查询性能差
    detection: 慢查询日志/SQL 分析
    recovery: |
      1. 分析执行计划
      2. 添加或优化索引
      3. 优化 SQL 语句

  - name: 表结构冲突
    detection: 字段名重复/类型不匹配
    recovery: |
      1. 评审并协调
      2. 重命名或合并
      3. 更新相关文档

  - name: 容量预估不足
    detection: 存储空间告警
    recovery: |
      1. 清理历史数据
      2. 扩展存储
      3. 实施归档策略
```

## Output Validation

```yaml
validation:
  - 检查项: ER 图完整性
    标准: 所有实体和关系已定义

  - 检查项: 表结构规范性
    标准: 符合命名规范，有注释

  - 检查项: 索引合理性
    标准: 无冗余索引，查询已覆盖

  - 检查项: 约束完整性
    标准: 主键、唯一约束、外键已定义

  - 检查项: 文档完整性
    标准: 数据字典、设计说明完整
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
    - name: ER 图
      path: docs/database/er-diagram.md
      description: 数据库实体关系图

    - name: DDL 脚本
      path: scripts/database/schema.sql
      description: 数据库建表脚本

    - name: 数据字典
      path: docs/database/data-dictionary.md
      description: 字段说明文档

    - name: 设计说明
      path: docs/database/design-spec.md
      description: 设计决策说明

  schema_summary:
    tables: 表数量
    views: 视图数量
    indexes: 索引数量
    estimated_size_gb: 预估大小

  review_status:
    design_review: 通过
    security_review: 通过

  next_phase:
    phase: implement-feature
    entry_criteria: 数据库设计已评审
    handover_data: DDL 脚本、数据字典
```

## Example Output Structure

```yaml
design_database_result:
  database_info:
    type: "MySQL 8.0"
    charset: "utf8mb4"
    engine: "InnoDB"

  er_diagram:
    entities:
      - name: "用户表"
        fields: 15
        relationships: ["订单", "地址"]

  tables:
    - name: "users"
      columns: 15
      indexes: 4
      description: "用户信息表"

    - name: "orders"
      columns: 12
      indexes: 5
      description: "订单表"

  indexes:
    - table: "orders"
      columns: ["user_id", "status", "created_at"]
      type: "BTREE"
      purpose: "查询用户订单"

  partitioning:
    strategy: "RANGE"
    column: "created_at"
    intervals: ["monthly"]

  estimated_capacity:
    current_gb: 50
    one_year_later_gb: 200
```

## Execution Flow

> Step-by-step execution sequence for design-database

### Phase 1: Analysis
- Understand requirements and context
- Identify constraints and dependencies

### Phase 2: Execution
- Perform core design-database activities
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
## Database Design Deliverables

### Summary
- Status: [completed | partial | blocked]
- Completion: [percentage]

### Key Outputs
1. **Entity Relationship Diagram**: ER diagram with entities, attributes, and relationships
2. **Schema Definition**: DDL scripts or schema definition document
3. **Indexing Strategy**: Index recommendations based on query patterns
4. **Data Dictionary**: Field definitions, constraints, and defaults
5. **Migration Plan**: Schema change strategy (if applicable)

### Validation Checklist
- [ ] Schema achieves third normal form (3NF)
- [ ] Index coverage meets 90% of frequent queries
- [ ] All tables and columns have documented descriptions
- [ ] Data integrity constraints are complete

### Next Steps
- [ ] Review schema with DBA and development team
- [ ] Set up database migration pipeline
```

