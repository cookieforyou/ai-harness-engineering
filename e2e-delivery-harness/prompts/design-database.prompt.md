---
name: design-database
description: "数据库设计提示词，用于设计数据库架构、表结构、索引策略和分库分表方案"
type: prompt
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: [prompt, database, schema]
---
# Design Database Prompt

## Purpose

本提示词指导AI执行数据库设计任务，设计数据库架构、表结构、索引策略、分库分表方案等。

### Key Objectives

- **规范化的数据建模**: 达到第三范式（3NF），确保数据一致性
- **高效的索引设计**: 覆盖高频查询，提升查询性能
- **可扩展的Schema设计**: 支持数据量增长，预留扩展空间
- **完整的数据字典**: 所有表和字段有清晰注释和约束定义

## Input Variables (变量定义)

> **AI 在执行前必须确认以下变量已填充**，如未填充则请求用户提供

| Variable | Type | Required | Default | Description | Validation |
|----------|------|----------|---------|-------------|------------|
| `project_name` | string | true | - | 项目名称 | 非空字符串 |
| `domain_model` | string | true | - | 领域模型或ER图描述 | 包含实体和关系 |
| `database_type` | enum | true | - | 数据库类型 | mysql/postgresql/mongodb/tidb |
| `data_volume` | object | true | - | 数据量预估 | 含当前量和增长率 |
| `read_write_ratio` | string | false | "7:3" | 读写比例 | 格式：读:写 |
| `consistency_level` | enum | false | strong | 一致性级别 | strong/eventual |
| `availability_target` | number | false | 99.9 | 可用性目标(%) | 99-99.999之间 |
| `compliance_reqs` | array | false | [] | 合规要求 | GDPR/PII等 |
| `existing_schema` | string | false | - | 现有Schema（如有） | SQL或描述 |

### 示例: 变量的正确格式

```yaml
# 示例: 完整的数据库设计输入
project_name: "电商平台系统"
domain_model: |
  核心实体：
  - User（用户）：id, username, email, phone, created_at
  - Product（商品）：id, name, price, stock, category_id
  - Order（订单）：id, user_id, total_amount, status, created_at
  - OrderItem（订单项）：id, order_id, product_id, quantity, price
  
  关系：
  - User 1:N Order
  - Order 1:N OrderItem
  - Product 1:N OrderItem
  - Category 1:N Product

database_type: "mysql"
data_volume:
  current_gb: 10
  growth_rate_percent: 10
  one_year_gb: 20
  peak_rows_per_table:
    users: 1000000
    orders: 5000000
    products: 100000
    
read_write_ratio: "8:2"
consistency_level: "strong"
availability_target: 99.99
compliance_reqs:
  - "GDPR: 用户数据可删除权"
  - "PII: 手机号、邮箱需加密存储"
```

## Chain of Thought (思维链)

> **AI 必须按照以下思维链逐步执行**，每完成一步后进行自我验证

```
[THINK] Step 1: 理解业务需求和数据特征
   ├─ 输入: domain_model, database_type, data_volume
   ├─ 思考: 核心实体有哪些？数据访问模式是OLTP还是OLAP？
   ├─ 验证: 与领域模型对照，确认实体边界清晰
   └─ 输出: 业务需求分析摘要
   ↓
[ANALYZE] Step 2: 分析数据需求和约束
   ├─ 输入: read_write_ratio, consistency_level, compliance_reqs
   ├─ 思考: 一致性要求是什么？是否有合规约束？数据类型如何选择？
   ├─ 验证: 评估字符集、时区处理、敏感字段加密需求
   └─ 输出: 数据约束分析报告
   ↓
[DESIGN] Step 3: 设计概念模型和逻辑模型
   ├─ 输入: 业务需求分析、数据约束分析
   ├─ 思考: 实体间关系如何建模？是否达到3NF？需要反范式化吗？
   ├─ 验证: ER图完整性检查，主键和外键定义清晰
   └─ 输出: ER图和表结构初稿
   ↓
[EVALUATE] Step 4: 设计物理模型和优化策略
   ├─ 输入: ER图和表结构初稿
   ├─ 思考: 索引策略如何设计？是否需要分区或分片？
   ├─ 验证: 执行计划分析，检查全表扫描风险
   └─ 输出: 索引设计和优化方案
   ↓
[DOCUMENT] Step 5: 输出数据库设计文档
   ├─ 生成DDL脚本（CREATE TABLE语句）
   ├─ 编写数据字典（表结构、字段说明、约束）
   ├─ 绘制ER图（概念模型、逻辑模型）
   └─ 输出: 完整的数据库设计文档
   ↓
[VALIDATE] Step 6: 评审确认并准备交接
   ├─ 组织数据库设计评审会议，收集DBA反馈
   ├─ 根据反馈修订设计方案
   ├─ 获得DBA签字确认
   └─ 生成交接上下文，准备移交开发阶段
```

## Error Handling (错误处理)

> **AI 在执行过程中遇到以下情况时的处理策略**

### Error Scenario 1: 数据不一致问题

**识别信号**: 
- 外键约束冲突或违反
- 重复数据出现
- 脏读、不可重复读、幻读现象

**处理流程**:
```
IF 检测到数据不一致
THEN
  1. 分析不一致的根本原因（并发写入、事务隔离级别、应用层逻辑错误）
  2. IF 并发问题 THEN 调整事务隔离级别或使用乐观锁/悲观锁
  3. IF 应用层错误 THEN 修复业务逻辑，添加数据校验
  4. 执行数据清洗，修复已存在的不一致数据
  5. 添加约束和触发器，防止未来出现类似问题
  6. 更新设计规范文档
END
```

**降级方案**: 暂时接受轻微不一致，通过定时任务进行数据对账和修复

**升级条件**: 经过2次调整后仍然存在严重数据不一致，需要DBA介入进行架构级调整

---

### Error Scenario 2: 查询性能不达标

**识别信号**: 
- 慢查询日志中出现大量超时查询（>1秒）
- EXPLAIN显示全表扫描或临时表
- CPU或IO使用率持续高负载

**处理流程**:
```
IF 检测到查询性能不达标
THEN
  1. 使用EXPLAIN分析慢查询的执行计划
  2. 识别性能瓶颈：全表扫描、未使用索引、JOIN过多、子查询嵌套
  3. IF 缺少索引 THEN 添加合适的索引（优先联合索引）
  4. IF SQL复杂 THEN 重构SQL，减少JOIN或拆分为多次查询
  5. IF 数据量大 THEN 考虑分区、分片或引入缓存层
  6. 重新测试查询性能，验证优化效果
  7. 更新索引设计文档
END
```

**降级方案**: 对非核心查询降低性能要求，或引入读写分离减轻主库压力

**升级条件**: 经过多轮优化仍无法满足P99延迟目标，需要重新评估架构设计（如引入搜索引擎、列式存储）

---

### Error Scenario 3: 容量预估不足导致扩容困难

**识别信号**: 
- 磁盘使用率超过80%
- 单表行数超过1000万，性能明显下降
- 备份时间过长影响业务

**处理流程**:
```
IF 检测到容量预警
THEN
  1. 评估当前数据量和增长速度
  2. IF 单表过大 THEN 实施水平分表（按时间范围或哈希）
  3. IF 单库过大 THEN 实施垂直分库（按业务域）或水平分库
  4. 制定数据归档策略，将冷数据迁移到廉价存储
  5. 执行在线迁移，确保业务不中断
  6. 更新容量规划文档
END
```

**降级方案**: 临时增加存储空间，同时启动分库分表方案设计

**升级条件**: 无法在线扩容，需要停机维护，需协调业务窗口期

## Output Validation (输出验证)

> **重要**: 在生成最终输出前，必须完成以下验证步骤

### Validation Checklist

**V-001: Schema Completeness (Schema完整性)**
- [ ] ER图包含所有核心实体和关系
- [ ] DDL脚本可执行，无语法错误
- [ ] 数据字典覆盖所有表和字段
- [ ] 索引设计文档完整

**V-002: Normalization Compliance (规范化合规)**
- [ ] 所有表达到第三范式（3NF）
- [ ] 无重复列或派生列（除非反范式化优化）
- [ ] 每个非主键列完全依赖于主键

**V-003: Index Coverage (索引覆盖)**
- [ ] 高频查询有索引覆盖（≥90%）
- [ ] 索引数量合理（≤5个/表）
- [ ] 联合索引遵循最左前缀原则
- [ ] 无冗余索引

**V-004: Performance Feasibility (性能可行性)**
- [ ] P99查询延迟<500ms（基准测试）
- [ ] 无N+1查询问题
- [ ] JOIN表数量合理（≤5个）
- [ ] 大字段（TEXT/BLOB）单独存储

**V-005: Compliance & Standards (规范性和标准)**
- [ ] 命名规范统一（表名、字段名、索引名）
- [ ] 敏感字段加密存储
- [ ] 审计字段齐全（created_at, updated_at, deleted_at）
- [ ] 符合GDPR等合规要求

### Validation Failure Handling

```
IF any validation check fails
THEN
  1. Identify specific failed items
  2. Attempt to fix based on available information
  3. IF cannot fix THEN mark as [NEEDS REVIEW] with explanation
  4. Generate validation report with pass/fail status
  5. Highlight critical issues requiring immediate attention
END
```

## Output Format (输出格式)

> AI必须按照以下结构生成数据库设计文档

```markdown
# Database Design Document

## 1. Executive Summary
- Project Name: {project_name}
- Database Type: {mysql/postgresql/mongodb/tidb}
- Version: 1.0
- Date: {current_date}

## 2. Business Requirements Analysis

### 2.1 Core Entities
{列出核心业务实体及其属性}

### 2.2 Data Characteristics
| Characteristic | Value |
|----------------|-------|
| Current Volume | {GB} |
| Growth Rate | {%/year} |
| Read/Write Ratio | {ratio} |
| Consistency Level | {strong/eventual} |

## 3. Conceptual Model (ER Diagram)

### 3.1 Entity List
| Entity | Primary Key | Description |
|--------|-------------|-------------|
| {entity-1} | {pk} | {description} |

### 3.2 Relationships
| Relationship | Type | Description |
|--------------|------|-------------|
| User → Order | 1:N | 一个用户可以有多个订单 |

### 3.3 ER Diagram
{ER图说明或Mermaid代码}

## 4. Logical Model (Table Structure)

### 4.1 Table Definitions

#### Table: {table_name}
**Description**: {表描述}

| Column | Type | Nullable | Default | Constraint | Comment |
|--------|------|----------|---------|------------|---------|
| id | BIGINT | NO | AUTO_INCREMENT | PRIMARY KEY | 主键ID |
| username | VARCHAR(50) | NO | - | UNIQUE | 用户名 |
| email | VARCHAR(100) | NO | - | UNIQUE | 邮箱 |
| created_at | DATETIME | NO | CURRENT_TIMESTAMP | - | 创建时间 |
| updated_at | DATETIME | NO | CURRENT_TIMESTAMP ON UPDATE | - | 更新时间 |

**Indexes**:
- PRIMARY KEY (id)
- UNIQUE KEY uk_username (username)
- UNIQUE KEY uk_email (email)
- KEY idx_created_at (created_at)

**Foreign Keys**:
- N/A (或列出外键)

### 4.2 All Tables
{重复上述结构，列出所有表}

## 5. Physical Model

### 5.1 Database Configuration
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Character Set | utf8mb4 | 支持emoji和多语言 |
| Collation | utf8mb4_unicode_ci | Unicode排序 |
| Storage Engine | InnoDB | 支持事务和外键 |
| Row Format | DYNAMIC | 支持大字段高效存储 |

### 5.2 Partitioning Strategy
{如果需要分区，描述分区策略}

### 5.3 Sharding Strategy
{如果需要分库分表，描述分片策略}

## 6. Indexing Strategy

### 6.1 Index Design Principles
- 高频查询字段必须有索引
- 联合索引遵循最左前缀原则
- 避免过度索引（≤5个/表）
- 定期审查无用索引

### 6.2 Index List by Table
| Table | Index Name | Columns | Type | Purpose |
|-------|------------|---------|------|---------|
| users | uk_username | username | UNIQUE | 唯一性约束 |
| orders | idx_user_status | user_id, status | NORMAL | 用户订单查询 |

## 7. Data Dictionary

### 7.1 Table: {table_name}
| Column | Type | Length | Nullable | Default | Constraint | Description |
|--------|------|--------|----------|---------|------------|-------------|
| id | BIGINT | - | NO | AUTO_INCREMENT | PK | 主键ID |

### 7.2 All Tables
{重复上述结构，列出所有表的详细数据字典}

## 8. DDL Scripts

```sql
-- Create Database
CREATE DATABASE IF NOT EXISTS `{project_name}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE `{project_name}`;

-- Create Tables
CREATE TABLE `users` (
  `id` BIGINT NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `username` VARCHAR(50) NOT NULL COMMENT '用户名',
  `email` VARCHAR(100) NOT NULL COMMENT '邮箱',
  `phone` VARCHAR(20) DEFAULT NULL COMMENT '手机号',
  `password_hash` VARCHAR(255) NOT NULL COMMENT '密码哈希',
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `deleted_at` DATETIME DEFAULT NULL COMMENT '删除时间（软删除）',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_username` (`username`),
  UNIQUE KEY `uk_email` (`email`),
  KEY `idx_created_at` (`created_at`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='用户表';

-- Repeat for all tables
```

## 9. Performance Optimization

### 9.1 Query Patterns
| Query Pattern | Frequency | Expected Latency | Index Used |
|---------------|-----------|------------------|------------|
| SELECT * FROM users WHERE username = ? | High | <50ms | uk_username |

### 9.2 Optimization Recommendations
- 建议1：对于订单查询，使用联合索引(user_id, status, created_at)
- 建议2：对于历史订单，考虑按月分区
- 建议3：引入Redis缓存热点数据

## 10. Security & Compliance

### 10.1 Sensitive Data Handling
| Field | Encryption Method | Rationale |
|-------|-------------------|-----------|
| password | bcrypt hashing | 不可逆加密 |
| phone | AES-256 encryption | PII数据保护 |
| email | AES-256 encryption | PII数据保护 |

### 10.2 Compliance Requirements
- GDPR: 用户数据可删除（实现软删除）
- PII: 敏感字段加密存储
- Audit: 所有表包含审计字段

## 11. Capacity Planning

### 11.1 Growth Projection
| Year | Estimated Size (GB) | Estimated Rows (Millions) |
|------|---------------------|---------------------------|
| Year 1 | {size} | {rows} |
| Year 2 | {size} | {rows} |
| Year 3 | {size} | {rows} |

### 11.2 Scaling Strategy
- 当单表超过1000万行时，实施水平分表
- 当单库超过500GB时，实施垂直分库
- 冷数据归档到对象存储

## 12. Validation Summary

- Schema Review Status: {passed/pending}
- Performance Benchmark: {results}
- DBA Sign-off: {yes/no}
```

## Handover Context (交接上下文)

> 完成数据库设计后，生成以下交接信息给开发阶段

```yaml
handover:
  header:
    from_stage: "database-design"
    to_stage: "development"
    handover_id: "HO-{{timestamp}}-DB"
    timestamp: "{{ISO8601}}"
    prepared_by: "Database Architect Agent"
    
  summary:
    status: "completed/partial/blocked"
    completion_percentage: {{0-100}}
    quality_score: {{0-100}}
    database_type: "mysql/postgresql/mongodb"
    total_tables: {{count}}
    estimated_size_gb: {{size}}
    
  artifacts:
    delivered:
      - name: "Database Design Document"
        path: "docs/database/design.md"
        version: "1.0"
        sections:
          - Business Requirements Analysis
          - Conceptual Model (ER Diagram)
          - Logical Model (Table Structure)
          - Physical Model
          - Indexing Strategy
          - Data Dictionary
          - DDL Scripts
          - Performance Optimization
          - Security & Compliance
          - Capacity Planning
          
  metrics:
    total_tables: {{count}}
    total_indexes: {{count}}
    foreign_keys: {{count}}
    unique_constraints: {{count}}
    normalization_level: "3NF"
    
  key_decisions:
    - id: "DC-001"
      description: "Database type selection - MySQL chosen for ACID compliance"
      rationale: "Strong consistency required for financial transactions"
      
    - id: "DC-002"
      description: "Primary key strategy - Auto Increment for single-node"
      rationale: "Simpler and faster than distributed ID for current scale"
      
  open_issues:
    blocking: []
    non_blocking:
      - id: "ISSUE-001"
        description: "Some query patterns need optimization during implementation"
        impact: "May require index adjustments"
        owner: "Backend Developer"
        
  risks:
    - id: "RISK-001"
      description: "Data volume may grow faster than projected"
      probability: "medium"
      impact: "high"
      mitigation: "Monitor growth rate monthly, prepare sharding plan"
      
  recommendations:
    - "Use ORM framework for easier schema management"
    - "Implement database migration scripts (Flyway/Liquibase)"
    - "Set up monitoring for slow queries and deadlocks"
    - "Regular backup and test restore procedures"
    
  next_steps:
    - "Execute DDL scripts in development environment"
    - "Implement data access layer (DAO/Repository)"
    - "Write unit tests for database operations"
    - "Set up CI/CD pipeline for schema migrations"
```

## Related Assets (关联资产)

| Asset Type | Path | Description |
|------------|------|-------------|
| Scenario | `../scenarios/design-database/SCENARIO.md` | 数据库设计场景定义 |
| Agent | `../agents/design-database.agent.md` | 数据库设计Agent角色 |
| Skill | `../skills/design-database/SKILL.md` | 数据库设计技能包 |
| Instruction | `../instructions/design-database.instructions.md` | 数据库设计技术指令 |

## Related Resources (相关资源)

- **Standards**: 
  - [Database Naming Convention](../standards/database-naming-convention.md) - 数据库命名规范
  - [Normalization Guidelines](../standards/normalization-guidelines.md) - 数据库规范化指南
- **Templates**: 
  - [ER Diagram Template](../templates/er-diagram.template.md) - ER图模板
  - [Data Dictionary Template](../templates/data-dictionary.template.md) - 数据字典模板
- **Evaluations**: 
  - [Schema Review Checklist](../evaluations/schema-review-checklist.md) - Schema评审检查清单
  - [Query Performance Benchmark](../evaluations/query-performance-benchmark.md) - 查询性能基准测试

## Handover Preparation (交接准备)

使用 [contexts/unified-handover-template.md](../contexts/unified-handover-template.md)。

```yaml
handover:
  header:
    from_stage: "system-design"
    to_stage: "implement-feature"
    handover_id: "HO-{ISO8601}-{sequence}"
    timestamp: "{ISO8601}"
    prepared_by: "design-database"
  summary:
    status: completed|partial|blocked
    quality_score: {0-100}
  artifacts:
    delivered: []
  decisions: []
  open_issues:
    blocking: []
    non_blocking: []
  risks: []
  quality_metrics:
    kpi_results: []
  recommendations: []
```
