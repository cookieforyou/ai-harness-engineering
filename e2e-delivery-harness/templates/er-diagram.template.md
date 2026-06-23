---
name: er-diagram
type: deliverable-template
version: "1.0.0"
status: active
---

# ER 图 模板

> 复制本模板到 `docs/` 对应路径，由 Agent 按 [standards/harness-engineering.md](../standards/harness-engineering.md) 填充。

## 元数据

- 项目: {project_name}
- 版本: {version}
- 作者: {author}
- 日期: {ISO8601}

## 正文

## ER 图概览

- **数据域**: {data_domain}
- **模型版本**: {version}
- **创建人**: {author}
- **最后更新**: {ISO8601}

## 实体清单

### {实体名称}

**描述**: {实体的业务含义}

**属性定义**:

| 属性名 | 数据类型 | 长度 | 主键 | 外键 | 必填 | 唯一 | 默认值 | 描述 |
|--------|----------|------|------|------|------|------|--------|------|
| id | BIGINT | 20 | PK | - | Y | Y | - | 主键ID |
| {field} | {type} | {length} | - | - | Y/N | Y/N | {default} | {description} |
| {field} | {type} | {length} | - | {参考表.字段} | Y/N | Y/N | {default} | {description} |

**约束**:
- {constraint_description}
- {constraint_description}

---

### {实体名称}

**描述**: {实体的业务含义}

**属性定义**:

| 属性名 | 数据类型 | 长度 | 主键 | 外键 | 必填 | 唯一 | 默认值 | 描述 |
|--------|----------|------|------|------|------|------|--------|------|
| {field} | {type} | {length} | PK/FK | - | Y/N | Y/N | {default} | {description} |
| {field} | {type} | {length} | - | - | Y/N | Y/N | {default} | {description} |

## 关系定义

| 实体A | 关系 | 实体B | 关系类型 | 描述 |
|-------|------|-------|----------|------|
| {entity} | {拥有/属于/关联} | {entity} | 1:1 / 1:N / M:N | {description} |
| {entity} | {拥有/属于/关联} | {entity} | 1:1 / 1:N / M:N | {description} |
| {entity} | {拥有/属于/关联} | {entity} | 1:1 / 1:N / M:N | {description} |

### 关系详情

**{Entity A} -- ({关系类型}) -- {Entity B}**:
- **外键**: {Entity B}.{field} → {Entity A}.{field}
- **级联策略**: {CASCADE/SET NULL/RESTRICT}
- **基数说明**: {如:一个用户可以有多个订单,一个订单属于一个用户}

## 标记法说明

### Crow's Foot 标记法

```
○----- 0 或 1 (Optional)
|----- 恰好 1 (Mandatory one)
◀▶---- 多 (Many)
--|---- 恰好 1 (One)
```

### 关系基数示例

| 标记 | 含义 |
|------|------|
| ||----o| | 一对零或一 |
| ||----|| | 一对一 (强制) |
| ||----<| | 一对多 (强制) |
| o-----o| | 零或一对零或一 |

## 完整关系图 (PlantUML)

```
@startuml
' 推荐使用 PlantUML 绘制 ER 图

entity "Entity1" as e1 {
  + id: BIGINT [PK]
  --
  name: VARCHAR(100)
  created_at: TIMESTAMP
}

entity "Entity2" as e2 {
  + id: BIGINT [PK]
  --
  e1_id: BIGINT [FK]
  description: TEXT
  --
  * e1_id -> e1.id
}

e1 ||--o{ e2 : has
@enduml
```

## 修订历史

| 版本 | 日期 | 作者 | 变更内容 | 评审人 |
|------|------|------|----------|--------|
| v1.0 | {ISO8601} | {author} | 初稿 | {reviewer} |

## 验证

- [ ] 已通过 [evaluations/output-validation-checklist.md](../evaluations/output-validation-checklist.md)
