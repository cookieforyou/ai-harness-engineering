---
name: database-naming-convention
description: "数据库命名规范标准，定义表名、列名、索引、约束、视图和存储过程的命名规则，涵盖 MySQL/PostgreSQL/Oracle 的差异处理"
type: standard
version: "1.1.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-23
status: active
language: "zh-CN"
tags: ['standard', 'database', 'naming', 'convention']
---

# 数据库命名规范标准

## Overview

数据库命名规范是本项目所有数据库对象命名的统一标准，适用于 MySQL、PostgreSQL 和 Oracle 三种主流关系型数据库。本规范旨在通过一致的命名约定提升数据库对象的可读性、可维护性和可移植性，降低团队成员在数据库设计、开发和审查过程中的认知负荷。

**适用范围**：本项目涉及的所有数据库对象，包括但不限于表（Table）、列（Column）、索引（Index）、约束（Constraint）、视图（View）、物化视图（Materialized View）、存储过程（Stored Procedure）、函数（Function）和触发器（Trigger）。

---

## Core Content

### 1. 通用命名原则

所有数据库对象命名必须遵循以下核心原则：

- **大小写**：强制使用小写字母加下划线分隔（`snake_case`）。MySQL、PostgreSQL 和 Oracle 均支持此格式，且可避免跨数据库迁移时的引号转义问题。
- **自描述性**：名称应能清晰表达对象的业务含义，避免含义模糊或过于通用的命名（如 `data1`、`tmp`）。
- **避免冗余**：名称中不重复包含数据库名、模式名等上下文信息。
- **保留字禁令**：禁止使用数据库保留字（Reserved Words）作为任何对象名。附表列出了常见保留字及其替代方案。
- **长度限制**：表名 ≤ 30 字符，列名 ≤ 30 字符，索引名 ≤ 30 字符，约束名 ≤ 30 字符。此限制主要出于 Oracle 兼容性考虑。
- **字符集**：仅使用 `a-z`、`0-9` 和下划线 `_`。禁止使用数字开头，禁止连续下划线。

**附表：常见保留字与替代命名**

| 保留字 | 替代方案 | 说明 |
|--------|----------|------|
| `user` | `usr_account` | 用户表 |
| `order` | `ord_order` | 订单表 |
| `status` | `entity_status` | 状态列 |
| `group` | `usr_group` | 用户组 |
| `level` | `usr_level` | 用户等级 |
| `type` | `entity_type` | 类型列 |
| `count` | `entity_count` | 计数列 |
| `value` | `attr_value` | 属性值 |
| `key` | `access_key` | 访问密钥 |
| `date` | `event_date` | 日期列 |
| `time` | `event_time` | 时间列 |
| `desc` | `description` | 描述列 |

### 2. 表命名规则

所有表名必须采用单数形式，并遵循统一的格式规范。

- **格式**：`{模块前缀}_{业务名称}`。模块前缀使用 3-4 个字母的缩写，确保在整个项目范围内唯一且具有辨识度。
  - 示例：`usr_account`（用户模块-账户表）、`ord_order`（订单模块-订单表）、`prd_product`（产品模块-产品表）。

- **单数形式**：表名使用单数而非复数。例如 `usr_account` 而非 `usr_accounts`，`ord_order_item` 而非 `ord_order_items`。

- **关联表**：表示多对多关系的关联表命名格式为 `{表A}_{表B}_map`。表名按字母顺序排列（考虑业务主次可调整）。例如 `user_role_map`（用户与角色关联）、`order_product_map`（订单与产品关联）。

- **临时表**：格式为 `tmp_{目的}_{YYYYMMDD}`。临时表使用后应及时清理，生命周期不应超过 24 小时。例如 `tmp_cleanup_20260601`、`tmp_import_batch_20260623`。

- **归档表**：格式为 `arc_{原表名}_{YYYYMMDD}`。归档表应与原始表保持相同的表结构。例如 `arc_ord_order_20260601`、`arc_usr_account_20260601`。

- **系统表/字典表**：格式为 `sys_{字典名称}`。例如 `sys_config`（系统配置）、`sys_dict_item`（字典条目）。

### 3. 列命名规则

列命名应清晰反映其数据类型和业务含义，通过前缀或后缀传递类型信息。

- **主键列**：统一使用 `id` 作为单表主键列名。对于复合主键或需要显式关联的场景，使用 `{表名}_id`。数据类型统一为 `BIGINT UNSIGNED`（自增）或 `CHAR(36)`（UUID v4）。

- **外键列**：格式为 `{关联表名}_id`。外键列名应与关联表的主键列名对齐，便于通过名称直接理解关联关系。例如 `user_id`（关联 `usr_account.id`）、`order_id`（关联 `ord_order.id`）、`product_id`（关联 `prd_product.id`）。

- **布尔列**：使用 `is_`、`has_`、`can_` 前缀，明确表示该列为布尔（Boolean）类型。例如 `is_active`、`is_deleted`、`has_approval`、`has_attachment`、`can_override`。

- **日期时间列**：使用 `{事件}_at` 格式，数据类型为 `DATETIME`（或 `TIMESTAMP`）。例如 `created_at`、`updated_at`、`deleted_at`、`approved_at`、`shipped_at`、`expired_at`。

- **日期列（不含时间）**：使用 `{事件}_date` 格式，数据类型为 `DATE`。例如 `birth_date`、`start_date`、`end_date`。

- **枚举/状态列**：使用 `{实体}_status` 格式，数据类型为 `VARCHAR` 或 `TINYINT`（通过代码表映射）。例如 `order_status`、`account_status`、`shipment_status`。

- **计数列**：使用 `{实体}_count` 格式，数据类型为 `INT` 或 `BIGINT`。例如 `item_count`、`login_count`、`retry_count`。

- **金额列**：使用 `{名称}_amount` 格式，统一使用最小单位整数存储（如分为单位），数据类型为 `BIGINT`。例如 `total_amount`、`discount_amount`、`tax_amount`。需要保留精度的场景使用 `DECIMAL(18,2)`。

- **JSON/文本列**：使用 `{名称}_json` 或 `{名称}_text` 后缀。例如 `ext_json`、`remark_text`。

### 4. 索引命名规则

索引名称必须包含索引类型前缀，通过名称即可判断索引的特性和作用。

- **主键索引**：`pk_{表名}`。每个表有且只有一个主键索引。例如 `pk_usr_account`、`pk_ord_order`。

- **唯一索引**：`uk_{表名}_{列名}`。唯一约束对应的索引使用此命名。联合唯一索引需将所有列名列出。例如 `uk_user_email`（用户表邮箱唯一）、`uk_user_phone`、`uk_order_order_no`（订单编号唯一）。

- **普通索引**：`idx_{表名}_{列名}`。单列索引直接包含列名。例如 `idx_order_status`、`idx_order_created_at`。

- **联合索引**：`idx_{表名}_{列1}_{列2}`。列名按索引定义中的顺序排列，遵循最左前缀原则。例如 `idx_order_user_status`（复合索引 `(user_id, status)`）、`idx_order_status_created`（复合索引 `(status, created_at)`）。

- **全文索引**：`ft_{表名}_{列名}`。例如 `ft_product_name`、`ft_article_content`。

- **空间索引**：`sp_{表名}_{列名}`。例如 `sp_store_location`。

### 5. 约束命名规则

约束名称应清晰标识约束类型和作用的列，便于错误诊断和运维管理。

- **主键约束（PRIMARY KEY）**：同名于主键索引，格式为 `pk_{表名}`。例如 `pk_usr_account`、`pk_ord_order`。

- **唯一约束（UNIQUE）**：同名于唯一索引，格式为 `uk_{表名}_{列名}`。例如 `uk_user_email`、`uk_user_phone`。

- **外键约束（FOREIGN KEY）**：格式为 `fk_{子表}_{父表}`。外键约束名应清晰表达引用关系。例如 `fk_order_user`（订单表引用用户表）、`fk_order_item_order`（订单项表引用订单表）。

- **CHECK 约束**：格式为 `ck_{表名}_{列名}`。例如 `ck_user_age`（年龄范围检查）、`ck_order_amount_positive`（金额正数检查）、`ck_account_status_value`（状态值域检查）。

- **默认值约束（DEFAULT）**：不强制命名规范，由数据库自动生成；如需显式命名，格式为 `df_{表名}_{列名}`。

### 6. 视图命名规则

视图和物化视图的命名应清晰区分，并包含业务用途描述。

- **普通视图**：格式为 `v_{业务描述}`。视图名应概括视图的业务含义或用途。例如 `v_active_user_summary`、`v_order_monthly_report`、`v_user_permission`。

- **物化视图**：格式为 `mv_{业务描述}`。物化视图与普通视图通过前缀 `mv_` 区分。例如 `mv_daily_sales`、`mv_user_login_stats`、`mv_product_inventory_snapshot`。

### 7. 存储过程、函数与触发器命名规则

数据库可编程对象的命名应包含对象类型标识，以便从名称直接判断对象类型。

- **存储过程（Stored Procedure）**：格式为 `sp_{模块}_{动作}`。例如 `sp_order_create`、`sp_order_cancel`、`sp_user_register`、`sp_report_generate_daily`。

- **函数（Function）**：格式为 `fn_{描述}`。函数名以动词开头描述其功能。例如 `fn_calc_tax`、`fn_generate_order_no`、`fn_get_user_full_name`、`fn_encrypt_password`。

- **触发器（Trigger）**：格式为 `trg_{表名}_{事件}`。事件标识插入 `ins`、更新 `upd`、删除 `del`。例如 `trg_user_before_insert`、`trg_order_after_update`、`trg_account_after_delete`。

### 8. 各数据库引擎差异处理

尽管本规范力求统一，各数据库引擎仍存在语法和功能层面的差异，需注意以下处理方式：

- **MySQL**：
  - 保留字转义应使用反引号（backtick `` ` ``），但本规范要求尽量避免使用保留字，减少转义需求。
  - 存储引擎推荐统一使用 `InnoDB`，以支持事务和外键约束。
  - 字符集推荐使用 `utf8mb4`，排序规则使用 `utf8mb4_unicode_ci`。
  - 索引长度受列前缀限制，`VARCHAR` 列索引需注意前缀长度。

- **PostgreSQL**：
  - 保留字转义使用双引号（`"`），但不推荐使用；建议始终坚持小写 `snake_case`，无需引号。
  - PostgreSQL 默认将未加引号的对象名转换为小写，因此小写命名可直接使用。
  - 使用 `SERIAL` 或 `IDENTITY` 实现自增主键，而非 MySQL 的 `AUTO_INCREMENT`。
  - 序列（Sequence）命名：`seq_{表名}_{列名}`，例如 `seq_usr_account_id`。

- **Oracle**：
  - 30 字符长度限制仍然适用，所有命名必须严格遵守此上限。
  - Oracle 默认将未加引号的对象名转换为大写，但建议在 DDL 中使用小写命名以保持跨数据库一致性。
  - 使用 `SEQUENCE` 实现自增，序列命名格式为 `seq_{表名}_{列名}`。
  - 不支持 `AUTO_INCREMENT` 和 `IDENTITY`（12c+ 支持 Identity Columns，但仍建议使用 Sequence）。
  - 分区表命名：`{表名}_{分区键}`，如 `ord_order_202606`。

---

## Examples

以下示例展示符合规范和违反规范的命名对比，帮助理解规范的具体应用。

### 表命名

| 符合规范（Good） | 违反规范（Bad） | 原因 |
|------------------|-----------------|------|
| `usr_account` | `t_user_account_list` | Bad 使用冗余前缀 `t_`、复数形式 `users`、无业务含义后缀 `list` |
| `ord_order` | `order_table` | Bad `order` 为保留字，`_table` 后缀冗余 |
| `user_role_map` | `user_to_role_mapping` | Bad 关联表应使用 `_map` 后缀而非 `_to_mapping` |

### 列命名

| 符合规范（Good） | 违反规范（Bad） | 原因 |
|------------------|-----------------|------|
| `is_active` | `active_flag` / `active` | Bad 缺少布尔前缀 `is_`，未明确表达数据类型 |
| `created_at` | `create_time` / `crt_dt` | Bad 日期列应使用 `_at` 后缀，缩写不统一 |
| `usr_account_id` | `user_id` / `uid` | Bad 外键应使用完整的 `{表名}_id` 格式，`uid` 含义模糊 |

### 索引命名

| 符合规范（Good） | 违反规范（Bad） | 原因 |
|------------------|-----------------|------|
| `uk_user_email` | `unique_email_idx` | Bad 唯一索引应使用 `uk_` 前缀而非 `unique_` |
| `idx_order_status_created` | `index1` / `order_status_index` | Bad `index1` 无描述性，缺少 `idx_` 前缀 |

### 存储过程命名

| 符合规范（Good） | 违反规范（Bad） | 原因 |
|------------------|-----------------|------|
| `sp_order_create` | `create_order_proc` | Bad 缺少 `sp_` 前缀，后缀 `_proc` 不是标准标识 |
| `fn_calc_tax` | `get_tax_value_func` | Bad 函数应使用 `fn_` 前缀 |

---

## Compliance Checklist

使用以下检查清单验证数据库设计是否遵循本规范：

- [ ] 所有对象名是否使用小写 snake_case？
- [ ] 表名是否使用单数形式并含模块前缀？
- [ ] 列名是否遵循类型前缀约定（布尔 `is_*`，日期 `*_at`）？
- [ ] 主键列命名为 `id`、外键列命名为 `{表名}_id`？
- [ ] 索引命名是否包含类型前缀（`pk_`/`uk_`/`idx_`/`ft_`）？
- [ ] 约束命名是否包含类型前缀（`pk_`/`uk_`/`fk_`/`ck_`）？
- [ ] 是否避免了所有数据库保留字（参考保留字附表中的替代命名）？
- [ ] 所有对象名长度是否在 30 字符以内（Oracle 兼容）？

---

## Related Standards

- [normalization-guidelines.md](normalization-guidelines.md)
- [harness-engineering.md](harness-engineering.md)
- [asset-model.md](asset-model.md)
