# 场景：自动化代码审查 / Automated Code Review

## 业务背景

在软件交付流程中，代码审查（Code Review）是保障质量的关键环节。本场景通过 AI Agent 自动化执行初轮审查，识别安全、逻辑、性能、可维护性问题，生成结构化报告，并通过质量门禁决定是否需要人工深度介入。

## 预期输入

```json
{
  "pr_id": "PR-2048",
  "repo": "org/service-a",
  "diff": "unified diff string...",
  "context": "Java Spring Boot 微服务，使用 PostgreSQL"
}
```

## 预期输出

```json
{
  "status": "success | partial | failure",
  "report_url": "...",
  "summary": "发现 2 处 high，1 处 medium",
  "action_required": true,
  "human_escalation": false
}
```

## 流程概览

1. **Diff 解析** — 将统一 Diff 拆分为按文件组织的结构化数据
2. **安全扫描** — 并行执行密钥泄露检测与漏洞模式匹配
3. **深度审查** — 资深工程师 Agent 对代码逻辑、性能、可维护性进行综合评审
4. **报告合并** — 合并安全扫描与深度审查结果，去重并排序
5. **质量门禁** — 运行评估脚本，判断是否通过
6. **通知与归档** — 通过或人工升级

## 成功标准

- 安全漏洞检出率 >= 95%（基于 evaluations/code-review-dataset.jsonl）
- 误报率 <= 15%
- 平均响应延迟 <= 60s（单文件 <200 行）
- Critical 级别问题 100% 触发人工介入

## 依赖资产

- Agent: `agents/senior-engineer`
- Skills: `skills/diff-parser`, `skills/security-audit`, `skills/report-merger`
- Prompts: `prompts/code-review/v1.md`
- Instructions: `instructions/system/code-review-system.md`, `instructions/safety/*`
- Evaluations: `evaluations/code-review-checkpoint.yaml`

## 版本历史

| 版本 | 日期 | 变更 |
| :--- | :--- | :--- |
| 1.0.0 | 2026-04 | 初版，覆盖基础审查流程 |
