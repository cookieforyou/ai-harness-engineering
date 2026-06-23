---
name: pull-request
type: deliverable-template
version: "1.0.0"
status: active
---

# Pull Request 模板

> 复制本模板到 `docs/` 对应路径，由 Agent 按 [standards/harness-engineering.md](../standards/harness-engineering.md) 填充。

## 元数据

- 项目: {project_name}
- 版本: {version}
- 作者: {author}
- 日期: {ISO8601}

## 正文

## 描述

### 变更摘要

{用清晰简洁的语言描述此 PR 的变更内容}

### 相关需求/工单

- **需求**: FR-{number} / TASK-{number}
- **缺陷修复**: BUG-{number} / INC-{number}
- **关联 Issue**: #{issue_number}

### 背景与动机

{描述此变更的背景、业务动机或 Bug 场景}

## 变更类型

- [ ] **功能新增** (Feature)
- [ ] **缺陷修复** (Bugfix)
- [ ] **性能优化** (Performance)
- [ ] **重构** (Refactor)
- [ ] **文档更新** (Documentation)
- [ ] **测试** (Test)
- [ ] **构建/CI** (Build/CI)
- [ ] **其他** (Other): {描述}

## 变更范围

### 影响的服务/模块

- [ ] {service/module_name}: {变更描述}
- [ ] {service/module_name}: {变更描述}

### API 变更

- [ ] 新增 API: {endpoint}
- [ ] 修改 API: {endpoint} - {变更描述}
- [ ] 废弃 API: {endpoint}
- [ ] 无 API 变更

### 数据库变更

- [ ] 新增表/集合: {table_name}
- [ ] 修改表结构: {table_name} - {变更描述}
- [ ] 数据迁移: {migration_description}
- [ ] 无数据库变更

## 测试验证

### 测试范围

- [ ] 单元测试 - {覆盖率}%
- [ ] 集成测试 - {测试场景描述}
- [ ] 功能测试 - {测试方法}
- [ ] 端到端测试 - {测试描述}
- [ ] 性能测试 - {基准测试结果}

### 测试结果

| 测试类型 | 执行数 | 通过 | 失败 | 跳过 |
|----------|--------|------|------|------|
| Unit | {total} | {pass} | {fail} | {skip} |
| Integration | {total} | {pass} | {fail} | {skip} |
| E2E | {total} | {pass} | {fail} | {skip} |

## 检查清单

- [ ] 代码遵循项目编码规范
- [ ] 已添加/更新必要的测试
- [ ] 已添加/更新必要的文档
- [ ] 代码无明显的性能问题
- [ ] 所有测试通过
- [ ] 已处理边界情况和异常场景
- [ ] 日志记录充分且不包含敏感信息
- [ ] 无已知安全漏洞

## 截图/录屏 (UI 变更时必填)

| 变更前 | 变更后 |
|--------|--------|
| {before_screenshot} | {after_screenshot} |

## Reviewer Notes

{对 Reviewer 的特别说明,如:重点关注区域、已知限制、待办事项等}

## 验证

- [ ] 已通过 [evaluations/output-validation-checklist.md](../evaluations/output-validation-checklist.md)
