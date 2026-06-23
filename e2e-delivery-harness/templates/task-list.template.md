---
name: task-list
type: deliverable-template
version: "1.0.0"
status: active
---

# 任务清单 模板

> 复制本模板到 `docs/` 对应路径，由 Agent 按 [standards/harness-engineering.md](../standards/harness-engineering.md) 填充。

## 元数据

- 项目: {project_name}
- 版本: {version}
- 作者: {author}
- 日期: {ISO8601}

## 正文

## 迭代信息

- **迭代名称**: {sprint_name}
- **迭代周期**: {start_date} ~ {end_date}
- **项目**: {project_name}
- **负责人**: {owner}
- **目标**: {sprint_goal}

## 任务清单

### {任务分组/模块名称}

| 任务ID | 任务名称 | 描述 | 预估工时(h) | 负责人 | 状态 | 优先级 | 依赖 |
|--------|----------|------|-------------|--------|------|--------|------|
| TASK-001 | {task_name} | {description} | {hours} | {assignee} | {To Do/In Progress/Done} | P0/P1/P2 | {dependencies} |
| TASK-002 | {task_name} | {description} | {hours} | {assignee} | {To Do/In Progress/Done} | P0/P1/P2 | {dependencies} |
| TASK-003 | {task_name} | {description} | {hours} | {assignee} | {To Do/In Progress/Done} | P0/P1/P2 | {dependencies} |

### {任务分组/模块名称}

| 任务ID | 任务名称 | 描述 | 预估工时(h) | 负责人 | 状态 | 优先级 | 依赖 |
|--------|----------|------|-------------|--------|------|--------|------|
| TASK-004 | {task_name} | {description} | {hours} | {assignee} | {To Do/In Progress/Done} | P0/P1/P2 | {dependencies} |

## 任务验收标准

### TASK-001: {任务名称}

- [ ] {验收标准 1}
- [ ] {验收标准 2}
- [ ] {验收标准 3}

### TASK-002: {任务名称}

- [ ] {验收标准 1}
- [ ] {验收标准 2}

## 完成定义 (DoD)

- [ ] **代码完成**: 所有代码已编写并提交
- [ ] **代码审查**: 已完成 Code Review 并解决所有意见
- [ ] **单元测试**: 单元测试覆盖率达到 {coverage_target}%
- [ ] **集成测试**: 集成测试通过
- [ ] **功能测试**: 功能测试通过
- [ ] **文档**: 相关文档已更新
- [ ] **性能测试**: 性能指标满足要求
- [ ] **安全审查**: 安全审查无高风险项
- [ ] **部署**: 已完成目标环境的部署

## 依赖管理

| 依赖ID | 依赖描述 | 阻塞任务 | 负责人 | 预计完成时间 | 状态 |
|--------|----------|----------|--------|--------------|------|
| DEP-001 | {description} | TASK-001 | {owner} | {date} | {status} |

## 风险评估

| 风险ID | 风险描述 | 概率 | 影响 | 缓解措施 |
|--------|----------|------|------|----------|
| RSK-001 | {description} | H/M/L | H/M/L | {mitigation} |

## 验证

- [ ] 已通过 [evaluations/output-validation-checklist.md](../evaluations/output-validation-checklist.md)
