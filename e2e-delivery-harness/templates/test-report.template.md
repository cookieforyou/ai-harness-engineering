---
name: test-report
type: deliverable-template
version: "1.0.0"
status: active
language: "zh-CN"
---

# 测试报告 模板

> 复制本模板到 `docs/` 对应路径，由 Agent 按 [standards/harness-engineering.md](../standards/harness-engineering.md) 填充。

## 元数据

- 项目: {project_name}
- 版本: {version}
- 作者: {author}
- 日期: {ISO8601}

## 正文

## 执行摘要

- **测试版本**: {version}
- **测试环境**: {environment}
- **测试周期**: {start_date} ~ {end_date}
- **测试负责人**: {owner}

## 执行统计

### 总体统计

| 指标 | 数量 | 占比 |
|------|------|------|
| 总用例数 | {total} | 100% |
| 通过 | {pass} | {pass_percentage}% |
| 失败 | {fail} | {fail_percentage}% |
| 阻塞 | {blocked} | {blocked_percentage}% |
| 未执行 | {not_executed} | {not_executed_percentage}% |

### 按模块统计

| 模块 | 总用例 | 通过 | 失败 | 阻塞 | 通过率 |
|------|--------|------|------|------|--------|
| {module} | {total} | {pass} | {fail} | {blocked} | {rate}% |
| {module} | {total} | {pass} | {fail} | {blocked} | {rate}% |

### 按优先级统计

| 优先级 | 总用例 | 通过 | 失败 | 阻塞 | 通过率 |
|--------|--------|------|------|------|--------|
| P0 | {total} | {pass} | {fail} | {blocked} | {rate}% |
| P1 | {total} | {pass} | {fail} | {blocked} | {rate}% |
| P2 | {total} | {pass} | {fail} | {blocked} | {rate}% |
| P3 | {total} | {pass} | {fail} | {blocked} | {rate}% |

## 缺陷分析

### 缺陷汇总

| 严重级别 | 总数 | 已修复 | 待修复 | 关闭 |
|----------|------|--------|--------|------|
| P0 - Critical | {total} | {fixed} | {pending} | {closed} |
| P1 - Major | {total} | {fixed} | {pending} | {closed} |
| P2 - Minor | {total} | {fixed} | {pending} | {closed} |
| P3 - Trivial | {total} | {fixed} | {pending} | {closed} |

### 缺陷趋势

{缺陷趋势分析描述}

## 覆盖率分析

| 覆盖类型 | 目标值 | 实际值 | 状态 |
|----------|--------|--------|------|
| 需求覆盖率 | {target}% | {actual}% | PASS/FAIL |
| 代码行覆盖率 | {target}% | {actual}% | PASS/FAIL |
| 分支覆盖率 | {target}% | {actual}% | PASS/FAIL |

## 质量评估

### 主要发现

1. {质量发现 1}
2. {质量发现 2}
3. {质量发现 3}

### 风险评估

| 风险 | 等级 | 说明 |
|------|------|------|
| {risk} | H/M/L | {description} |

## 发布建议

- [ ] **推荐发布**: 质量达标,无阻塞性问题
- [ ] **有条件发布**: {发布条件}
- [ ] **不推荐发布**: {理由}

## 修订历史

| 版本 | 日期 | 作者 | 变更内容 | 评审人 |
|------|------|------|----------|--------|
| v1.0 | {ISO8601} | {author} | 初稿 | {reviewer} |

## 验证

- [ ] 已通过 [evaluations/output-validation-checklist.md](../evaluations/output-validation-checklist.md)
