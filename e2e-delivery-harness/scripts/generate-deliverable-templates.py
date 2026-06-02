#!/usr/bin/env python3
"""Generate minimal deliverable templates referenced across the harness."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "templates"

TEMPLATES = {
    "requirements-spec.template.md": "需求规格说明书",
    "stakeholder-analysis.template.md": "干系人分析",
    "business-process-diagram.template.md": "业务流程图",
    "system-design-doc.template.md": "系统设计文档",
    "architecture-diagram.template.md": "架构图",
    "architecture-doc.template.md": "架构设计文档",
    "service-boundary.template.md": "服务边界定义",
    "task-list.template.md": "任务清单",
    "dependency-graph.template.md": "依赖关系图",
    "pull-request.template.md": "Pull Request",
    "commit-message-convention.md": "Commit 消息规范",
    "api-doc.template.md": "API 文档",
    "test-case.template.md": "测试用例",
    "test-plan.template.md": "测试计划",
    "defect-report.template.md": "缺陷报告",
    "test-report.template.md": "测试报告",
    "deployment-plan.template.md": "部署计划",
    "rollback-plan.template.md": "回滚方案",
    "release-report.template.md": "发布报告",
    "post-mortem.template.md": "事故复盘",
    "runbook.template.md": "运维 Runbook",
    "incident-report.template.md": "故障报告",
    "inspection-report.template.md": "巡检报告",
    "hotfix-checklist.template.md": "热修复检查清单",
    "communication.template.md": "沟通通知",
    "er-diagram.template.md": "ER 图",
    "data-dictionary.template.md": "数据字典",
}

BODY = """---
name: {name}
type: deliverable-template
version: "1.0.0"
status: active
---

# {title} 模板

> 复制本模板到 `docs/` 对应路径，由 Agent 按 [standards/harness-engineering.md](../standards/harness-engineering.md) 填充。

## 元数据

- 项目: {{project_name}}
- 版本: {{version}}
- 作者: {{author}}
- 日期: {{ISO8601}}

## 正文

<!-- 按场景 Prompt 的 Output Format 章节结构填写 -->

## 验证

- [ ] 已通过 [evaluations/output-validation-checklist.md](../evaluations/output-validation-checklist.md)
"""


def main() -> None:
    ROOT.mkdir(parents=True, exist_ok=True)
    for filename, title in TEMPLATES.items():
        name = filename.replace(".template.md", "").replace(".md", "")
        path = ROOT / filename
        if not path.exists():
            path.write_text(
                BODY.format(name=name, title=title),
                encoding="utf-8",
            )
            print(f"created {filename}")
        else:
            print(f"skip {filename}")


if __name__ == "__main__":
    main()
