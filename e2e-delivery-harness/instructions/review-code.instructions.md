---
name: review-code
description: "代码审查执行指南，用于执行代码评审"
applyTo: "scenarios/review-code/**"
phase: testing
type: instruction
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
language: "zh-CN"
tags: ['instruction', 'technical']
---
# Code Review Instruction

## Objective

执行代码审查，发现质量问题，确保代码符合规范，减少缺陷进入测试阶段。

## Prerequisites

1. 待审查的代码已提交
2. PR 描述完整
3. 单元测试已通过

## Process Steps

### Step 1: 接收审查请求

1. 获取 PR 信息
2. 阅读 PR 描述
3. 理解变更目的
4. 检查分支信息

### Step 2: 理解代码变更

1. 查看变更文件列表
2. 阅读变更代码
3. 理解业务逻辑
4. 识别关键变更点

### Step 3: 执行代码审查

1. **规范检查**
   - 命名规范
   - 代码格式
   - 注释规范

2. **质量检查**
   - 代码复杂度
   - 耦合度
   - 错误处理

3. **安全检查**
   - SQL 注入
   - XSS
   - 权限控制

4. **测试检查**
   - 测试覆盖
   - 测试质量

### Step 4: 标注审查意见

1. 使用审查工具标注
2. 区分问题级别
3. 提供修改建议
4. 解释问题原因

### Step 5: 给出审查结论

1. 总结审查结果
2. 给出审查结论
3. 列出阻塞问题
4. 建议是否合并

## Quality Gates

### 准入检查

- [ ] PR 描述完整
- [ ] 代码已提交
- [ ] 测试已通过

### 准出检查

- [ ] 所有文件已审查
- [ ] 问题已标注
- [ ] 结论已给出

## Handoff Criteria

交接给开发者前：

- [ ] 审查报告已完成
- [ ] 问题已标注
- [ ] 结论已给出


## Overview

> High-level description of the review-code execution process.
>
> This instruction defines the technical approach, key activities, and success criteria for the review-code scenario.


## Technical Specifications

> Detailed technical requirements and implementation guidelines for review-code.

### Required Tools
- **SonarQube / CodeClimate / Codacy**: 代码质量平台（静态分析 + 质量门禁）
- **ESLint / Prettier / Stylelint**: JavaScript/TypeScript 代码规范与格式化
- **Checkstyle / SpotBugs / PMD**: Java 静态分析与代码规范
- **Pylint / Black / Mypy / Ruff**: Python 代码检查、格式化与类型检查
- **Reviewable / Gerrit / GitHub PR Review**: 代码评审协作平台
- **ArchUnit / dependency-cruiser**: 架构规范与依赖检查

### Environment Requirements
- 代码规范配置已标准化且纳入版本控制（.eslintrc / .pylintrc / checkstyle.xml）
- CI 流水线已集成自动化静态检查（PR 创建时自动触发，结果反馈至 PR Comment）
- 团队Code Review规范已发布（Review Checklist、Reviewer 指定规则）
- IDE 已配置实时 Linting（开发时即时反馈，减少Review往返）

### Configuration Parameters
- `MIN_REVIEWERS`: 最少审批人数（核心模块 ≥2，普通模块 ≥1）
- `REVIEW_TIMEOUT`: Review SLA（PR 提交后 4h 内有人开始 Review，24h 内完成）
- `QUALITY_GATE`: 质量门禁阈值（新增代码覆盖率 ≥80%，重复率 ≤3%，无 Blocker 问题）
- `MAX_PR_SIZE`: PR 最大变更行数（≤400 行，超过需拆分，便于高效 Review）
- `AUTO_MERGE_ENABLED`: 是否允许自动合并（仅当所有 Check 通过 + 所有 Reviewer 批准时）


## Best Practices

> Industry-standard best practices for review-code execution.

1. **Practice 1**: Review for logic correctness, security, and performance
2. **Practice 2**: Ensure code follows team style and architecture guidelines
3. **Practice 3**: Provide actionable feedback with examples


## Multi-Language Code Examples

### GitHub PR Review API - Automated Review Pipeline (Python)

```python
#!/usr/bin/env python3
"""
GitHub PR Review Automation - 代码审查流水线自动化

功能:
  - 自动获取待审查 PR 列表
  - 提交审查意见（逐行标注）
  - 审批或请求变更
  - 检查 Reviewer 分配状态

Requires: pip install PyGithub
"""
import os
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional

from github import Github, GithubException
from github.PullRequest import PullRequest
from github.PullRequestReview import PullRequestReview

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = os.getenv("GITHUB_REPO", "org/repo")


class PRReviewPipeline:
    """PR 审查自动化流水线 - 管理整个代码审查流程。"""

    def __init__(self, token: str, repo_name: str):
        self.gh = Github(token)
        self.repo = self.gh.get_repo(repo_name)

    def get_pending_reviews(self, reviewer: str) -> List[PullRequest]:
        """
        获取等待指定 Reviewer 审查的 PR 列表。
        用于审查工程师的工作队列管理，避免 PR 堆积超过 24 小时。
        """
        open_prs = self.repo.get_pulls(state="open", sort="created")
        pending = []
        for pr in open_prs:
            # 检查该 reviewer 是否被分配
            reviewers = [r.login for r in pr.get_review_requests()[0]]
            if reviewer in reviewers:
                # 检查是否已经有 Review 提交
                reviews = list(pr.get_reviews())
                reviewed_by = {r.user.login for r in reviews}
                if reviewer not in reviewed_by:
                    pending.append(pr)
        return pending

    def submit_review(self, pr_number: int, body: str,
                      event: str = "COMMENT",
                      comments: Optional[List[Dict]] = None) -> PullRequestReview:
        """
        提交代码审查结果。

        Args:
            pr_number: PR 编号
            body: 审查总结
            event: APPROVE / REQUEST_CHANGES / COMMENT
            comments: 逐行审查意见列表
                [{"path": "file.py", "position": 10, "body": "suggestion"}]
        """
        pr = self.repo.get_pull(pr_number)
        review = pr.create_review(
            body=body,
            event=event,
            comments=comments or [],
        )
        return review

    def check_review_requirements(self, pr_number: int) -> Dict:
        """
        检查 PR 的审查要求状态。
        返回: 所需审查人数、已完成人数、是否满足门禁
        """
        pr = self.repo.get_pull(pr_number)
        pr_details = pr.raw_data

        # 获取仓库分支保护规则
        branch = self.repo.get_branch(pr.base.ref)
        protection = branch.get_required_status_checks()

        return {
            "pr_number": pr_number,
            "required_reviewers": 1,  # 默认配置，可根据实际定义
            "completed_reviews": len(list(pr.get_reviews())),
            "status_checks_pass": all(
                s.conclusion == "success"
                for s in pr.get_combined_status().statuses
            ) if protection else True,
            "mergeable": pr.mergeable,
        }

    def assign_reviewers(self, pr_number: int,
                         reviewers: List[str]) -> None:
        """自动分配审查者。"""
        pr = self.repo.get_pull(pr_number)
        pr.add_to_assignees(*reviewers)
        pr.create_review_request(reviewers=reviewers)

    def generate_review_report(self, pr_number: int) -> dict:
        """
        生成 PR 审查报告，包含变更统计、审查意见汇总、质量评分。
        """
        pr = self.repo.get_pull(pr_number)
        files = pr.get_files()
        reviews = list(pr.get_reviews())

        file_stats = []
        total_additions = 0
        total_deletions = 0
        for f in files:
            file_stats.append({
                "filename": f.filename,
                "additions": f.additions,
                "deletions": f.deletions,
                "status": f.status,
            })
            total_additions += f.additions
            total_deletions += f.deletions

        review_summary = []
        for r in reviews:
            review_summary.append({
                "reviewer": r.user.login,
                "state": r.state,
                "submitted_at": r.submitted_at.isoformat(),
                "body": r.body[:200] if r.body else "",
            })

        score = self._calculate_quality_score(file_stats, review_summary)

        return {
            "pr_title": pr.title,
            "pr_number": pr_number,
            "changed_files": len(file_stats),
            "total_additions": total_additions,
            "total_deletions": total_deletions,
            "files": file_stats,
            "reviews": review_summary,
            "quality_score": score,
            "duration_hours": self._calculate_duration(pr),
        }

    def _calculate_quality_score(self, files: List[Dict],
                                 reviews: List[Dict]) -> int:
        """计算 PR 质量评分 (0-100)。"""
        score = 100
        # 文件变更太大扣分
        total_changes = sum(f["additions"] + f["deletions"] for f in files)
        if total_changes > 500:
            score -= 20
        elif total_changes > 200:
            score -= 10
        # 审查意见多表示问题多
        changes_requested = sum(1 for r in reviews if r["state"] == "CHANGES_REQUESTED")
        score -= changes_requested * 5
        return max(0, min(100, score))

    def _calculate_duration(self, pr: PullRequest) -> float:
        """计算 PR 从创建到当前的小时数。"""
        delta = datetime.now() - pr.created_at
        return round(delta.total_seconds() / 3600, 1)
```

### SonarQube Quality Gate Integration (Python)

```python
#!/usr/bin/env python3
"""
SonarQube 质量门禁集成 - 代码审查前的自动化质量检查

在人工审查前自动运行 SonarQube 扫描，阻止质量不达标的代码进入审查流程。
"""
import os
import json
import subprocess
import sys
from typing import Dict, List, Optional

import requests

SONAR_HOST_URL = os.getenv("SONAR_HOST_URL", "http://sonarqube:9000")
SONAR_TOKEN = os.getenv("SONAR_TOKEN")
SONAR_PROJECT_KEY = os.getenv("SONAR_PROJECT_KEY")


class SonarQubeQualityGate:
    """SonarQube 质量门禁检测器。"""

    def __init__(self, host_url: str, token: str, project_key: str):
        self.base_url = host_url.rstrip("/")
        self.auth = (token, "")
        self.project_key = project_key

    def run_scanner(self, branch: str = "main") -> bool:
        """
        运行 SonarQube Scanner 对指定分支进行代码质量分析。

        分析指标:
          - Bugs: 代码缺陷数量
          - Vulnerabilities: 安全漏洞数量
          - Code Smells: 代码异味数量
          - Coverage: 测试覆盖率
          - Duplications: 重复代码比例
          - Maintainability: 可维护性评分
        """
        print(f"Running SonarQube scan on branch: {branch}")
        result = subprocess.run(
            ["sonar-scanner",
             f"-Dsonar.host.url={self.base_url}",
             f"-Dsonar.token={self.auth[0]}",
             f"-Dsonar.projectKey={self.project_key}",
             f"-Dsonar.branch.name={branch}"],
            capture_output=True, text=True, check=False
        )
        if result.returncode != 0:
            print(f"SonarScanner error: {result.stderr}")
            return False
        print(f"SonarScanner completed with return code {result.returncode}")
        return True

    def get_quality_gate_status(self, branch: str = "main") -> Dict:
        """
        获取指定分支的质量门禁状态。

        返回值示例:
          {"status": "OK", "conditions": [...], "ignoredConditions": false}
        """
        resp = requests.get(
            f"{self.base_url}/api/qualitygates/project_status",
            params={"projectKey": self.project_key, "branch": branch},
            auth=self.auth,
            timeout=30,
        )
        resp.raise_for_status()
        return resp.json()

    def get_measures(self, branch: str = "main") -> Dict[str, float]:
        """
        获取项目的关键质量度量指标，用于自动评估代码质量。

        度量指标:
          - coverage: 测试覆盖率 (%)
          - bugs: 缺陷数
          - vulnerabilities: 漏洞数
          - code_smells: 代码异味
          - duplicated_lines_density: 重复率 (%)
          - sqale_index: 技术债务 (分钟)
        """
        metric_keys = (
            "coverage,bugs,vulnerabilities,code_smells,"
            "duplicated_lines_density,sqale_index,"
            "security_hotspots,ncloc"
        )
        resp = requests.get(
            f"{self.base_url}/api/measures/component",
            params={
                "component": self.project_key,
                "metricKeys": metric_keys,
                "branch": branch,
            },
            auth=self.auth,
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()

        measures = {}
        for measure in data.get("component", {}).get("measures", []):
            measures[measure["metric"]] = measure.get("value")
        return measures

    def generate_quality_report(self, branch: str = "main") -> Dict:
        """
        生成完整的代码质量报告，供审查工程师在 Review 前参考。

        报告包含:
          - 质量门禁状态
          - 代码度量指标
          - 安全热点
          - 推荐操作
        """
        gate_status = self.get_quality_gate_status(branch)
        measures = self.get_measures(branch)

        # 生成建议
        recommendations = []
        if not gate_status.get("projectStatus", {}).get("status") == "OK":
            recommendations.append("质量门禁未通过，建议修复所有 Blocker 和 Critical 问题后再审查")
        coverage = float(measures.get("coverage", 0) or 0)
        if coverage < 80:
            recommendations.append(f"测试覆盖率 {coverage}% 低于 80% 目标，要求补充测试")
        bugs = int(measures.get("bugs", 0) or 0)
        if bugs > 0:
            recommendations.append(f"发现 {bugs} 个代码缺陷，请在审查前修复")

        return {
            "quality_gate": gate_status["projectStatus"]["status"],
            "measures": measures,
            "recommendations": recommendations,
            "passed": gate_status["projectStatus"]["status"] == "OK",
        }
```

### Static Analysis Configuration Examples

#### Java - Checkstyle Configuration (checkstyle.xml)

```xml
<?xml version="1.0"?>
<!DOCTYPE module PUBLIC
  "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN"
  "https://checkstyle.org/dtds/configuration_1_3.dtd">
<!--
  Checkstyle 代码规范配置
  企业级 Java 代码审查标准，适用于所有服务端项目。
  重点: 命名规范、Javadoc 完整性、代码复杂度控制、异常处理规范。
-->
<module name="Checker">
    <property name="severity" value="error"/>
    <property name="charset" value="UTF-8"/>
    <property name="fileExtensions" value="java"/>

    <!-- 禁止 TAB 缩进 -->
    <module name="FileTabCharacter"/>

    <!-- 文件长度限制: 最大 1000 行 -->
    <module name="FileLength">
        <property name="max" value="1000"/>
    </module>

    <module name="TreeWalker">
        <!-- 命名规范 -->
        <module name="PackageName">
            <property name="format" value="^[a-z]+(\.[a-z][a-z0-9]*)*$"/>
        </module>
        <module name="TypeName"/>
        <module name="MethodName"/>
        <module name="ParameterName"/>
        <module name="ConstantName"/>

        <!-- 代码复杂度控制 -->
        <module name="CyclomaticComplexity">
            <property name="max" value="15"/>
        </module>
        <module name="NPathComplexity">
            <property name="max" value="200"/>
        </module>
        <module name="JavaNCSS">
            <property name="methodMaximum" value="50"/>
        </module>

        <!-- 异常处理规范 -->
        <module name="IllegalCatch">
            <property name="illegalClassNames"
                      value="java.lang.Exception, java.lang.Throwable, java.lang.RuntimeException"/>
        </module>
        <module name="ThrowsCount">
            <property name="max" value="3"/>
        </module>

        <!-- 导入规范 -->
        <module name="IllegalImport"/>
        <module name="UnusedImports"/>

        <!-- Javadoc 要求 -->
        <module name="JavadocMethod">
            <property name="accessModifiers" value="public"/>
        </module>
    </module>
</module>
```

#### JavaScript - ESLint Configuration (eslint.config.js)

```javascript
/**
 * ESLint 企业级配置 - ECMAScript 2022+
 *
 * 审查规范覆盖:
 *   - 代码质量 (错误预防)
 *   - 代码风格一致性
 *   - 安全最佳实践
 *   - 可维护性
 */
export default [
    {
        files: ["src/**/*.{js,jsx,ts,tsx}"],
        rules: {
            // ========== 错误预防 (Error Prevention) ==========
            // 禁止未使用的变量
            "no-unused-vars": ["error", { argsIgnorePattern: "^_" }],
            // 禁止使用 undefined 变量
            "no-undef": "error",
            // 强制使用 === 而不是 ==
            "eqeqeq": ["error", "always"],
            // 禁止 debugger 提交 (CI 中应设为 error)
            "no-debugger": "error",
            // 禁止 console.log (允许 console.error/warn)
            "no-console": ["error", { allow: ["warn", "error"] }],

            // ========== 代码复杂度 (Complexity) ==========
            // 圈复杂度最大 10
            "complexity": ["warn", { max: 10 }],
            // 函数最大行数
            "max-lines-per-function": ["warn", { max: 80 }],
            // 禁止过深的嵌套
            "max-depth": ["warn", { max: 4 }],

            // ========== 安全 (Security) ==========
            // 禁止 eval
            "no-eval": "error",
            // 禁止直接 new Function
            "no-new-func": "error",
            // 禁止使用不安全的正则
            "no-insecure-regex": "off",

            // ========== 可维护性 (Maintainability) ==========
            // 代码重复检测
            "no-duplicate-imports": "error",
            // 循环复杂度
            "max-params": ["warn", { max: 4 }],
            // 使用 const 而非 let (不可变优先)
            "prefer-const": "error",
        },
    },
];
```

#### Go - golangci-lint Configuration (.golangci.yml)

```yaml
# golangci-lint 企业级配置
# 运行: golangci-lint run ./...
#
# 审查检查器分类:
#   - Bug 检测: errcheck, govet, staticcheck
#   - 复杂度: gocyclo, gocognit
#   - 安全: gosec
#   - 风格: gofmt, goimports, revive

linters:
  enable:
    # ------- Bug 检测 (高优先级) -------
    - errcheck       # 检测未检查的错误
    - govet          # Go 官方 vet 工具
    - staticcheck    # 高级静态分析 (替代 golint)
    - ineffassign    # 检测无效赋值
    - typecheck      # 类型检查
    - unused         # 检测未使用的代码

    # ------- 代码复杂度 (中优先级) -------
    - gocyclo        # 圈复杂度 (推荐 ≤ 15)
    - gocognit       # 认知复杂度 (推荐 ≤ 20)

    # ------- 安全与正确性 (高优先级) -------
    - gosec          # 安全漏洞检查
    - bodyclose      # 确保 HTTP body 被关闭
    - noctx          # 检测缺少 context 的 HTTP 请求

    # ------- 代码风格 (低优先级) -------
    - gofmt          # 检查格式化
    - goimports      # 导入排序和分组
    - revive         # 增强版的 golint
    - misspell       # 拼写检查

  disable:
    - deadcode       # 已废弃
    - varcheck       # 已废弃
    - structcheck    # 已废弃

linters-settings:
  errcheck:
    check-type-assertions: true
    check-blank: true
    # 允许忽略的未检查错误模式
    exclude-functions:
      - "fmt.Fprintln"
      - "fmt.Fprintf"

  gocyclo:
    min-complexity: 15  # 圈复杂度阈值

  gocognit:
    min-complexity: 20  # 认知复杂度阈值

  gosec:
    severity: "high"
    confidence: "medium"
    excludes:
      - G204  # 允许 os/exec (已知风险已评估)

  revive:
    rules:
      - name: exported
        severity: warning
      - name: blank-imports
      - name: unused-parameter

issues:
  max-issues-per-linter: 0     # 无限制
  max-same-issues: 0           # 无限制

  # 排除规则: 测试文件和自动生成文件
  exclude-rules:
    - path: _test\.go
      linters:
        - gocyclo
        - errcheck
        - gosec
    - path: ".*_gen\\.go"
      linters:
        - all

run:
  timeout: 5m
  tests: true
  skip-dirs:
    - vendor
    - third_party
```

### CodeClimate Configuration (.codeclimate.yml)

```yaml
version: "2"
plugins:
  # -------- 静态分析插件 --------
  duplication:
    enabled: true
    config:
      languages:
        go:
          mass_threshold: 50
        java:
          mass_threshold: 50
        javascript:
          mass_threshold: 40
        python:
          mass_threshold: 30

  fixme:
    enabled: true
    config:
      strings:
        - TODO
        - FIXME
        - HACK
        - XXX

  # -------- 语言特定插件 --------
  # Java 静态分析
  checkstyle:
    enabled: true
    channel: "beta"
    config:
      file: "config/checkstyle.xml"

  # JavaScript 静态分析
  eslint:
    enabled: true
    channel: "eslint-9"
    config:
      config: ".eslintrc.js"
      extensions:
        - .js
        - .jsx
        - .ts
        - .tsx

  # Go 静态分析
  golint:
    enabled: true

  # -------- 安全相关 --------
  bundler-audit:
    enabled: false
  nodesecurity:
    enabled: true

ratings:
  paths:
    - "src/**/*.java"
    - "src/**/*.js"
    - "src/**/*.ts"
    - "src/**/*.go"
    - "src/**/*.py"
```

## Error Handling

### Error Scenario 1: 审查范围过大导致延迟 (P2)

**触发条件**: 单个 PR 变更文件超过 15 个或变更行数超过 500 行，预计审查时间超过 4 小时

**处理流程**:
```
IF PR 变更量 > 500 行 OR 变更文件 > 15 个
THEN
  1. 评估变更的风险等级:
     a. 低风险: 配置修改、测试、文档 → 可继续但要求分批
     b. 中风险: 业务逻辑变更 → 要求拆分为多个小 PR
     c. 高风险: 核心架构/安全变更 → 必须拆分并安排多人审查
  2. 与 PR 提交者沟通拆分计划:
     a. 将大型 PR 按逻辑模块拆分为 2-5 个小 PR
     b. 每个 PR 变更量控制在 200-300 行以内
     c. 确保拆分后的 PR 保持可独立审查和部署
  3. 如果无法拆分（紧急情况）:
     a. 指定 2 名以上审查工程师并行审查不同模块
     b. 使用 Code Review Checklist 确保覆盖所有关键点
     c. 延长审查时间箱至 8 小时
  4. 记录 Large PR 问题到 Retrospective
END
```

**降级方案**: 增量审查 - 先审查核心逻辑文件，再审查外围文件和测试

**升级条件**: 单个 PR 超过 1000 行且无法拆分，升级至 Tech Lead 评估架构设计问题

### Error Scenario 2: 自动化检查与人工审查冲突 (P2)

**触发条件**: 自动化工具（ESLint/Checkstyle/SonarQube）报告大量问题，但人工审查认为多为误报或风格偏好，双方结论不一致导致 PR 无法合并

**处理流程**:
```
IF 自动化工具报告 > 20 个问题 AND 提交者认为 > 30% 为误报
THEN
  1. 对每个自动化问题进行分类:
     a. 确认的 Bug/安全漏洞 → 必须修复
     b. 代码异味/可维护性 → 建议修复
     c. 风格偏好（TAB 缩进、命名风格）→ 由团队规范决定
     d. 确认的误报 → 在工具配置中排除
  2. 处理规则:
     a. 必须修复类: Blocker/Critical 级别，无争议
     b. 建议修复类: 审查工程师裁定，有争议升级讨论
     c. 风格类: 遵循团队现有规范，不引入新规则
     d. 误报: 更新工具配置文件（suppress/ignore）
  3. 持续改进:
     a. 如果某种误报频繁出现，调整规则配置
     b. 定期 (每月) 审查工具规则的有效性
     c. 更新团队编码规范文档
END
```

**降级方案**: 对于紧急 PR，允许部分建议类问题标记为 TODO 并创建技术债务

**升级条件**: 超过 50% 的自动化规则引发争议，需团队会议重新评审编码规范

### Error Scenario 3: 安全漏洞漏报 (P0)

**触发条件**: 代码审查完成后，在生产环境发现安全漏洞（SQL 注入、XSS、敏感信息泄露等），且该漏洞应能在审查阶段发现

**处理流程**:
```
IF 生产环境发现安全漏洞 AND 首次审查未检出
THEN
  1. 立即启动安全事件响应流程:
     a. 评估漏洞等级和实际影响范围
     b. 确认问题代码的提交时间和引入版本
     c. 评估是否有敏感数据泄露
  2. 紧急修复和回滚:
     a. 立即修复安全漏洞并走紧急发布通道
     b. 如果需要，回滚到安全版本
     c. 通知安全团队评估进一步的潜在影响
  3. 审查流程根因分析:
     a. 分析漏洞为何在审查阶段未被发现
     b. 检查是否有自动化检测规则缺失
     c. 评估是否存在审查人员对该领域不熟悉
  4. 改进措施:
     a. 在静态分析工具中补充缺失的安全规则
     b. 增加安全专项审查 Checklist（SAST/DAST）
     c. 安排相关领域的安全培训
     d. 对于高危模块，要求安全专家参与审查
END
```

**降级方案**: 如果漏洞无法立即修复，启用 WAF 临时规则阻断攻击路径

**升级条件**: 漏洞导致用户数据泄露或超过 RPO，启动全面安全事件响应

### Error Scenario 4: 审查者主观偏见导致代码质量波动 (P3)

**触发条件**: 同一提交者的代码在不同审查者之间获得差异显著的评价（一个 APPROVE 一个 REQUEST_CHANGES），或同一审查者对类似代码风格给出不一致的评价

**处理流程**:
```
IF 审查结论严重分歧 OR 审查一致性 < 70%
THEN
  1. 召集分歧双方进行 15 分钟对齐讨论:
     a. 双方各自解释审查标准和判断依据
     b. 确定分歧是技术层面的还是风格偏好
     c. 寻找共同认可的解决方案
  2. 引入第三位审查者做出中立判断:
     a. 选择 Senior Engineer 或 Tech Lead
     b. 第三方的决定作为最终裁决
     c. 记录裁决理由供后续参考
  3. 审查标准对齐:
     a. 使用统一的审查 Checklist
     b. 建立团队共享的代码规范和审查标准文档
     c. 定期举办审查标准对齐会议
END
```

**降级方案**: 如果 PR 不涉及核心功能，少数服从多数决策

**升级条件**: 同一模块反复出现审查分歧，需要 Tech Lead 进行团队培训和标准统一

## Quality Standards

> Acceptance criteria and quality gates for review-code deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | Defect detection rate is 85% or higher | Automated check |
| Standard 2 | Review turnaround time is 24 hours or less | Automated check |
| Standard 3 | Zero P0/P1 security vulnerabilities are missed | Automated check |
## References

- [harness-engineering.md](../standards/harness-engineering.md)
- [output-validation-checklist.md](../evaluations/output-validation-checklist.md)
- [regression-checklist.md](../evaluations/regression-checklist.md)
