---
name: architecture-diagram
type: deliverable-template
version: "1.0.0"
status: active
---

# 架构图 模板

> 复制本模板到 `docs/` 对应路径，由 Agent 按 [standards/harness-engineering.md](../standards/harness-engineering.md) 填充。

## 元数据

- 项目: {project_name}
- 版本: {version}
- 作者: {author}
- 日期: {ISO8601}

## 正文

## 图表清单

| 图表名称 | 图表类型 | 文件格式 | 对应架构文档章节 |
|----------|----------|----------|------------------|
| {diagram_name} | {C4-Context / Component / Deployment / Sequence / ER} | .puml/.drawio/.png | {section_ref} |

## C4 上下文图

### 图表描述

{描述系统上下文图展示的范围和关键元素}

### PlantUML 示例

```
@startuml
!include <C4/C4_Context>
Person(user, "用户", "系统的终端用户")
System(system, "系统名称", "系统的业务功能")
System_Ext(external, "外部系统", "外部依赖系统")

Rel(user, system, "使用")
Rel(system, external, "调用")
@enduml
```

### 关键元素

| 元素 | 类型 | 描述 |
|------|------|------|
| {element} | Person/System/System_Ext | {description} |

## C4 容器图

### PlantUML 示例

```
@startuml
!include <C4/C4_Container>
Person(user, "用户", "用户")
System_Boundary(system, "系统") {
    Container(web, "Web App", "React", "提供前端界面")
    Container(api, "API Server", "Spring Boot", "提供 RESTful API")
}
Rel(user, web, "使用", "HTTPS")
Rel(web, api, "调用", "REST")
@enduml
```

## C4 组件图

### PlantUML 示例 (关键组件)

```
@startuml
!include <C4/C4_Component>
Container_Boundary(api, "API Server") {
    Component(controller, "Controller", "处理 HTTP 请求")
    Component(service, "Service", "业务逻辑层")
    Component(repository, "Repository", "数据访问层")
}
Rel(controller, service, "调用")
Rel(service, repository, "调用")
@enduml
```

## 部署图

### 部署架构描述

{描述部署拓扑结构}

### PlantUML 示例

```
@startuml
node "负载均衡" {
    [Nginx]
}
node "应用服务器" {
    [App Instance 1]
    [App Instance 2]
}
node "数据库" {
    [PostgreSQL]
}
Nginx --> App Instance 1
Nginx --> App Instance 2
App Instance 1 --> PostgreSQL
App Instance 2 --> PostgreSQL
@enduml
```

## 时序图

### 关键流程时序

```
@startuml
actor 用户
participant "前端" as UI
participant "API" as API
participant "Service" as SVC
participant "DB" as DB

用户 -> UI: 发起请求
UI -> API: HTTP 请求
API -> SVC: 业务处理
SVC -> DB: 数据查询
DB --> SVC: 返回数据
SVC --> API: 处理结果
API --> UI: HTTP 响应
UI --> 用户: 展示结果
@enduml
```

## 图例和符号标准

### 符号约定

| 符号 | 含义 | 使用场景 |
|------|------|----------|
| {symbol} | {meaning} | {scenario} |
| 实线箭头 | 同步调用 | REST API 调用 |
| 虚线箭头 | 异步/事件 | 消息队列事件 |
| 方框 | 系统/容器/组件 | C4 模型元素 |
| 圆形 | 角色/人员 | 外部用户 |

## 修订历史

| 版本 | 日期 | 作者 | 变更内容 | 评审人 |
|------|------|------|----------|--------|
| v1.0 | {ISO8601} | {author} | 初稿 | {reviewer} |

## 验证

- [ ] 已通过 [evaluations/output-validation-checklist.md](../evaluations/output-validation-checklist.md)
