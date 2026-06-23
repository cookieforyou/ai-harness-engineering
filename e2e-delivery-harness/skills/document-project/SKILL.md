---
name: document-project
description: "Domain skill for document-project execution"
category: development
type: skill
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-23
status: active
language: "zh-CN"
tags: ['skill', 'knowledge']
---
# Skill: 项目文档 (Document Project)

## Overview

本 Skill 定义了项目文档编写的核心知识体系，覆盖文档框架（Diátaxis、Arc42）、文档即代码（Docs-as-Code）、API 文档标准、Readme-driven Development 及文档自动化测试。适用于技术文档工程师、开发者及架构师创建高质量的项目文档。

## Core Knowledge

### 文档框架

#### Diátaxis 四象限框架

Diátaxis 按读者使用文档的目的分为四个象限，每种类型有明确的写作目标和风格：

| 象限 | 关注点 | 面向 | 风格 | 典型内容 |
|------|-------|------|------|---------|
| **教程 (Tutorial)** | 学习 | 新手 | 步骤式、引导 | Quick Start、教学指南 |
| **操作指南 (How-to)** | 任务 | 有经验的用户 | 步骤式、聚焦 | 部署指南、配置方法 |
| **参考 (Reference)** | 信息 | 所有用户 | 描述式、精确 | API 文档、配置项说明 |
| **解释 (Explanation)** | 理解 | 决策者 | 论述式、背景 | 架构说明、设计决策记录 |

**关键规则**: 不混用象限。教程中不插入 API 参考，参考文档中不写教学步骤。每个文档只服务一个象限的读者需求。

#### Arc42 架构文档模板

Arc42 是架构文档的标准模板，涵盖 12 个部分：

1. 简介与目标
2. 约束条件
3. 系统范围与上下文
4. 解决方案策略
5. 构建块视图（层级图）
6. 运行时视图（时序图）
7. 部署视图
8. 概念（跨领域）
9. 架构决策（ADR）
10. 质量需求
11. 技术风险
12. 术语表

### 文档即代码 (Docs-as-Code)

Docs-as-Code 的核心实践：

| 实践 | 说明 | 工具推荐 |
|------|------|---------|
| 版本管理 | 文档源文件纳入 Git 管理，与代码同仓库或独立仓库 | Git + GitHub/GitLab |
| 格式规范 | 使用纯文本标记语言，支持 Diff 和 Review | Markdown, AsciiDoc, reStructuredText |
| CI/CD | 自动构建、检查、发布文档 | GitHub Actions, GitLab CI, Netlify |
| 协作流程 | 文档走与代码相同的 Review 流程 | Pull Request + Reviewer |
| 自动化检查 | 链接检查、拼写检查、格式检查 | lychee, cspell, markdownlint |

### API 文档标准

#### OpenAPI / Swagger

- **OpenAPI 3.0+** 是 RESTful API 文档的事实标准
- 使用 yaml/json 定义 API 的端点、请求/响应模型、认证方式
- 可自动生成交互式文档（Swagger UI）和客户端 SDK
- 推荐流程：API 设计先行（Design-First），OpenAPI 规范作为唯一真相源

#### AsyncAPI

- 事件驱动/消息系统 API 文档标准（类比 OpenAPI 但面向异步）
- 支持 Kafka、RabbitMQ、MQTT 等消息协议
- 定义 Channel、Message、Schema、Bindings

### Readme-driven Development

一种"先写 README，再写实现"的开发方法论：

1. **Step 1**: 写 README 文档（描述用户如何使用该模块/服务）
2. **Step 2**: 获取反馈并迭代 README（确保 API 设计合理）
3. **Step 3**: 按 README 中的约定去实现

**优点**: 强迫作者在编码前思考用户使用场景，发现 API 设计缺陷时修改成本几乎为零。

### 文档自动化测试

| 检查类型 | 工具 | 检查内容 | CI 阶段 |
|---------|------|---------|---------|
| 链接检查 | lychee | 所有外部/内部链接是否 200 | PR 检查 |
| 拼写检查 | cspell | 英文拼写是否正确 | PR 检查 |
| 格式检查 | markdownlint | Markdown 格式规范 | PR 检查 |
| 代码验证 | 自定义脚本 | 文档中代码示例是否可以运行 | PR 检查 |
| Readability | textlint / Vale | 文档可读性评分 | 定时任务 |

### 文档编写方法

```python
class DocumentationSkill:
    """文档编写技能"""

    def __init__(self):
        self.doc_types = {
            "getting_started": {
                "focus": "快速上手",
                "length": "short",
                "examples": "high",
                "quadrant": "tutorial",
            },
            "user_guide": {
                "focus": "功能说明",
                "length": "medium",
                "examples": "medium",
                "quadrant": "how-to",
            },
            "api_reference": {
                "focus": "接口定义",
                "length": "long",
                "examples": "high",
                "quadrant": "reference",
            },
            "deployment_guide": {
                "focus": "部署运维",
                "length": "medium",
                "examples": "medium",
                "quadrant": "how-to",
            },
            "architecture_decision": {
                "focus": "设计决策记录",
                "length": "short",
                "examples": "low",
                "quadrant": "explanation",
            },
        }

    def create_api_doc(self, api_spec: dict) -> dict:
        """
        基于 OpenAPI 规范创建 API 文档

        Args:
            api_spec: OpenAPI 3.x 规范的 Python dict

        Returns:
            结构化的 API 文档字典
        """
        doc = {
            "overview": self._write_overview(api_spec),
            "authentication": self._write_auth(api_spec),
            "endpoints": self._write_endpoints(api_spec),
            "examples": self._write_examples(api_spec),
            "errors": self._write_errors(api_spec),
            "changelog": self._generate_changelog(api_spec),
        }
        return doc

    def create_user_guide(self, features: list[dict]) -> dict:
        """
        创建用户指南（How-to 象限）

        Args:
            features: 功能列表，每项含 name, description, steps, examples

        Returns:
            结构化的用户指南字典
        """
        doc = {
            "introduction": self._write_intro(features),
            "concepts": self._write_concepts(features),
            "tasks": self._write_tasks(features),
            "troubleshooting": self._write_troubleshooting(features),
        }
        return doc

    def validate_doc_links(self, doc_paths: list[str]) -> list[dict]:
        """
        验证文档中的链接有效性

        使用 lychee 进行链接检查，返回所有失效链接

        Args:
            doc_paths: 待检查的文档路径列表

        Returns:
            失效链接列表: [{file, url, status_code, error}]
        """
        import subprocess
        import json

        broken_links = []
        for path in doc_paths:
            result = subprocess.run(
                ["lychee", "--format", "json", path],
                capture_output=True, text=True, timeout=60
            )
            if result.returncode != 0:
                try:
                    results = json.loads(result.stdout)
                    for item in results:
                        if item.get("status") != 200:
                            broken_links.append({
                                "file": path,
                                "url": item.get("url"),
                                "status_code": item.get("status"),
                                "error": item.get("error_message", ""),
                            })
                except json.JSONDecodeError:
                    pass
        return broken_links

    def _write_overview(self, spec: dict) -> str:
        return spec.get("info", {}).get("description", "")

    def _write_auth(self, spec: dict) -> dict:
        security = spec.get("components", {}).get("securitySchemes", {})
        return {name: scheme.get("type") for name, scheme in security.items()}

    def _write_endpoints(self, spec: dict) -> list[dict]:
        endpoints = []
        for path, methods in spec.get("paths", {}).items():
            for method, details in methods.items():
                endpoints.append({
                    "path": path,
                    "method": method.upper(),
                    "summary": details.get("summary", ""),
                    "parameters": details.get("parameters", []),
                    "responses": details.get("responses", {}),
                })
        return endpoints

    def _write_examples(self, spec: dict) -> list[dict]:
        examples = []
        for path, methods in spec.get("paths", {}).items():
            for method, details in methods.items():
                if "examples" in details.get("requestBody", {}).get("content", {}).get("application/json", {}):
                    examples.append({
                        "endpoint": f"{method.upper()} {path}",
                        "request": details["requestBody"]["content"]["application/json"]["examples"],
                    })
        return examples

    def _write_errors(self, spec: dict) -> list[dict]:
        return [
            {"code": code, "description": detail.get("description", "")}
            for code, detail in spec.get("paths", {})
            .get("/errors", {})
            .get("get", {})
            .get("responses", {})
            .items()
        ]

    def _generate_changelog(self, spec: dict) -> list[dict]:
        return spec.get("info", {}).get("x-changelog", [])

    def _write_intro(self, features: list[dict]) -> str:
        return "This guide covers: " + ", ".join(f["name"] for f in features)

    def _write_concepts(self, features: list[dict]) -> list[str]:
        concepts = set()
        for f in features:
            if "concepts" in f:
                concepts.update(f["concepts"])
        return list(concepts)

    def _write_tasks(self, features: list[dict]) -> list[dict]:
        return [{"task": f["name"], "steps": f.get("steps", [])} for f in features]

    def _write_troubleshooting(self, features: list[dict]) -> list[dict]:
        issues = []
        for f in features:
            if "issues" in f:
                issues.extend(f["issues"])
        return issues
```

## Best Practices

1. **文档即代码 (Docs-as-Code)**：所有文档源文件纳入 Git 版本管理，使用 Markdown 格式，通过 CI 流水线自动构建和发布。文档评审走与代码相同的 PR 流程（≥1 人 Review），PR 标题添加 `[docs]` 前缀便于筛选。每次代码合并后自动触发文档构建和部署，确保文档与代码同步更新。使用 `.markdownlint.yaml` 统一团队文档格式规范，禁止手动修复格式问题（自动化修复）。

2. **Diátaxis 四象限框架**：按读者需求将文档分为 4 类——教程（面向学习）、操作指南（面向任务）、参考（面向信息）、解释（面向理解），不混用象限（如教程中不插入 API 参考）。仓库根目录按象限组织文档目录结构：`docs/tutorials/`、`docs/how-to/`、`docs/reference/`、`docs/explanation/`。每个文档的第一段明确声明其所属象限和目标读者。

3. **可执行示例优先**：所有代码示例必须是可运行的（含完整依赖声明），文档 CI 中自动执行示例代码并验证输出。禁止在文档中使用伪代码或未经验证的示例。示例代码使用独立的测试项目结构：`examples/` 目录下每个示例独立可运行，CI 中 `cd examples/ && make test` 验证所有示例。示例代码必须包含错误处理路径，展示常见错误的处理方法。

## Common Pitfalls

### Pitfall 1: 文档与代码不同步

- **Risk**：API 变更后文档未更新，读者按过时文档操作导致错误，反复报障。常见原因：只改代码不改文档、文档放在独立仓库难以跟踪对应关系、文档更新缺乏自动化验证。
- **Prevention**：将文档更新纳入 Definition of Done（DoD 必须包含"相关文档已更新"），API 变更时同步更新 OpenAPI/Swagger 规范文档。使用 CI 检查机制：代码变更涉及 API 时自动检查 OpenAPI 规范是否已更新。部署流水线中加入文档版本一致性检查，不一致时阻塞发布。
- **Impact**：开发者信任度下降，Onboarding 效率降低 ≥50%。新成员依赖过时文档学习导致理解偏差，增加沟通成本和返工量。最终团队放弃维护文档，形成"文档无用论"。

### Pitfall 2: 文档过多无导航

- **Risk**：文档量增长后缺乏结构化导航，读者无法快速定位所需内容。大量文档散落在仓库各处，没有清晰的入口和路径指引，新成员入职花费大量时间"考古"。
- **Prevention**：建立以 README 为入口的多级索引体系（README → 分类索引 → 具体文档），每层深度 ≤3 层。README 中必须包含"文档导航"章节，列出核心文档及其用途。使用 `mkdocs.yml` 或类似工具生成全局搜索索引，确保每个文档可在 2 次点击内到达。
- **Impact**：文档利用率低，重复提问增加。团队花费大量时间解答本已文档化的问题，知识传递效率下降。文档成为"写了没人看"的僵尸资产。

### Pitfall 3: 只写不维护

- **Risk**：初始创建大量文档雏形后长期不更新，内容腐化为"文档废墟"——过时的架构图、失效的链接、已废弃的功能说明。文档越旧越不可信，最终全部被视为不可靠。
- **Prevention**：每个文档声明 Owner 和 Review 周期（≥季度），使用文档新鲜度 Check（最后更新时间 ≤90 天）。建立文档健康仪表板：最后更新日期、访问频率、用户反馈评分。定期（每月）运行文档审计脚本，标记超过 90 天未更新的文档，通知 Owner 进行 Review。季度性"文档日"：团队集中清理和更新文档。
- **Impact**：新成员无法判断文档可信度，所有文档被默认为过时。知识流失加速，关键架构决策和操作流程只存在于少数人脑中，形成单点故障。

## 相关资产

- **标准**: `../../standards/document-standard.md`
- **标准**: `../../standards/requirement-standard.md`
- **评估**: `../../evaluations/documentation-quality.json`
- **评估**: `../../evaluations/api-spec-compliance.json`
