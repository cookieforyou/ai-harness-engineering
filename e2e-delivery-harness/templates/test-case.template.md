---
name: test-case
type: deliverable-template
version: "1.0.0"
status: active
---

# 测试用例 模板

> 复制本模板到 `docs/` 对应路径，由 Agent 按 [standards/harness-engineering.md](../standards/harness-engineering.md) 填充。

## 元数据

- 项目: {project_name}
- 版本: {version}
- 作者: {author}
- 日期: {ISO8601}

## 正文

## 测试用例概览

- **所属模块**: {module_name}
- **关联需求**: FR-{number}
- **测试类型**: {功能测试 / 集成测试 / 性能测试 / 安全测试}
- **测试版本**: {version}

## 测试用例列表

### TC-001: {测试用例标题}

**基本信息**:

| 字段 | 值 |
|------|----|
| 用例ID | TC-001 |
| 测试标题 | {test_title} |
| 测试优先级 | P0 / P1 / P2 / P3 |
| 所属模块 | {module_name} |
| 关联需求 | FR-{number} |
| 前置条件 | {preconditions} |
| 测试数据 | {test_data} |
| 自动化状态 | {已自动化 / 待自动化 / 手动} |

**测试步骤**:

| 步骤 | 操作描述 | 预期结果 | 实际结果 | 状态 |
|------|----------|----------|----------|------|
| 1 | {action_description} | {expected_result} | {actual_result} | PASS/FAIL/BLOCKED |
| 2 | {action_description} | {expected_result} | {actual_result} | PASS/FAIL/BLOCKED |
| 3 | {action_description} | {expected_result} | {actual_result} | PASS/FAIL/BLOCKED |

**后置条件**: {post_conditions}

---

### TC-002: {测试用例标题}

**基本信息**:

| 字段 | 值 |
|------|----|
| 用例ID | TC-002 |
| 测试标题 | {test_title} |
| 测试优先级 | P0 / P1 / P2 / P3 |
| 所属模块 | {module_name} |
| 关联需求 | FR-{number} |
| 前置条件 | {preconditions} |
| 测试数据 | {test_data} |
| 自动化状态 | {已自动化 / 待自动化 / 手动} |

**测试步骤**:

| 步骤 | 操作描述 | 预期结果 | 实际结果 | 状态 |
|------|----------|----------|----------|------|
| 1 | {action_description} | {expected_result} | {actual_result} | PASS/FAIL/BLOCKED |
| 2 | {action_description} | {expected_result} | {actual_result} | PASS/FAIL/BLOCKED |
| 3 | {action_description} | {expected_result} | {actual_result} | PASS/FAIL/BLOCKED |

## 需求-用例追溯矩阵

| 需求ID | 需求描述 | 覆盖用例 | 覆盖状态 |
|--------|----------|----------|----------|
| FR-001 | {description} | TC-001, TC-002 | 已覆盖 / 部分覆盖 / 未覆盖 |
| FR-002 | {description} | TC-003 | 已覆盖 / 部分覆盖 / 未覆盖 |

## 测试数据字典

| 数据项 | 类型 | 示例值 | 说明 |
|--------|------|--------|------|
| {data_field} | {type} | {example} | {description} |

## 验证

- [ ] 已通过 [evaluations/output-validation-checklist.md](../evaluations/output-validation-checklist.md)
