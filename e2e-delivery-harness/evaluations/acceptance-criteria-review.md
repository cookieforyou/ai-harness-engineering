# Acceptance Criteria Review (验收标准审查)

审查每条 AC-*（Given-When-Then）是否满足 Harness **Goal + Feedback** 层要求。

## 审查表

| AC ID | Given 可验证? | When 可执行? | Then 可观测? | 无主观词? | 结果 |
|-------|---------------|--------------|--------------|-----------|------|
| AC-001 | | | | | PASS/FAIL |

## 规则

1. **Then** 必须包含可检查产物（状态码、字段、指标、文件）
2. 禁止单独使用：快速、友好、稳定、高效（须量化）
3. 每条 REQ 至少一条 AC；P0 需求 AC 覆盖率 100%

## 与测试衔接

通过的 AC 应映射到 TC-*（见 verify-test 场景）。
