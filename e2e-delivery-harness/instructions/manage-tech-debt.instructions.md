---
name: manage-tech-debt
description: "技术债务管理场景的技术指令"
applyTo: "scenarios/manage-tech-debt/**"
phase: development
type: instruction
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
language: "zh-CN"
tags: ['instruction', 'technical']
---
# Technical Debt Management Instructions

## Overview

This instruction establishes the technical standards and governance framework for identifying, tracking, and strategically managing technical debt across the software delivery lifecycle. It covers debt quantification methodologies, prioritization frameworks balancing business impact against remediation cost, refactoring strategies that minimize delivery risk, and investment proposals for leadership alignment. The instruction ensures technical debt remains visible and actively managed rather than accumulating silently, with measurable paydown targets and trend tracking.


## Debt Quantification Framework

### Code Quality Metrics

| Metric | Good | Warning | Critical |
|--------|------|---------|----------|
| Cyclomatic Complexity | < 10 | 10-20 | > 20 |
| Lines of Code (per function) | < 20 | 20-50 | > 50 |
| Code Duplication | < 3% | 3-10% | > 10% |
| Comment Ratio | 20-30% | 10-20% | < 10% |
| Method Length | < 10 | 10-20 | > 20 |

### Technical Debt Ratio (TDR)

```
TDR = (Cost to Fix / Cost to Rebuild) × 100%

Excellent:  < 5%
Good:       5-10%
Acceptable: 10-15%
High:       15-25%
Critical:   > 25%
```

### Interest Rate Model

| Debt Type | Interest Rate | Impact |
|-----------|---------------|--------|
| 代码债务 | 5%/月 | 开发效率下降 |
| 架构债务 | 10%/月 | 扩展成本增加 |
| 测试债务 | 8%/月 | Bug 修复时间增加 |
| 文档债务 | 3%/月 | 新人上手时间增加 |

## Analysis Tools

### Static Code Analysis

```bash
# SonarQube
sonar-scanner -Dsonar.projectKey=myproject

# ESLint (JavaScript/TypeScript)
eslint src/ --format json > eslint-report.json

# Pylint (Python)
pylint src/ --output-format=json > pylint-report.json

# Checkstyle (Java)
mvn checkstyle:checkstyle
```

### Code Complexity Analysis

```bash
# Radon (Python)
radon cc -a -b src/

# ESComplex (JavaScript)
escomplex -t

# SonarQube Code Complexity
sonar.issues.sort=COMPLEXITY
```

### Dependency Analysis

```bash
# Dependabot (GitHub)
# .github/dependabot.yml

# npm audit
npm audit --json > audit-report.json

# Snyk
snyk test --json > snyk-report.json
```

## Refactoring Patterns

### 1. Extract Method

**Before:**
```python
def process_order(order):
    # Validate order
    if not order.items:
        raise ValueError("Empty order")
    if order.total < 0:
        raise ValueError("Invalid total")
    
    # Calculate discount
    if order.customer.tier == "premium":
        discount = order.total * 0.2
    else:
        discount = order.total * 0.1
    
    # Apply discount
    order.total = order.total - discount
    
    # Save order
    db.save(order)
    
    # Send notification
    email.send(order.customer, "Order confirmed")
```

**After:**
```python
def process_order(order):
    validate_order(order)
    apply_discount(order)
    save_and_notify(order)

def validate_order(order):
    if not order.items:
        raise ValueError("Empty order")
    if order.total < 0:
        raise ValueError("Invalid total")

def apply_discount(order):
    rate = 0.2 if order.customer.tier == "premium" else 0.1
    discount = order.total * rate
    order.total = order.total - discount
```

### 2. Replace Conditional with Polymorphism

**Before:**
```python
def calculate_shipping(order):
    if order.country == "US":
        return order.weight * 0.5
    elif order.country == "UK":
        return order.weight * 0.7
    elif order.country == "CN":
        return order.weight * 0.8
    else:
        return order.weight * 1.0
```

**After:**
```python
class ShippingStrategy:
    def calculate(self, order):
        raise NotImplementedError

class USShipping(ShippingStrategy):
    def calculate(self, order):
        return order.weight * 0.5

class UKShipping(ShippingStrategy):
    def calculate(self, order):
        return order.weight * 0.7

class ShippingFactory:
    @staticmethod
    def get_strategy(country):
        strategies = {
            "US": USShipping(),
            "UK": UKShipping(),
        }
        return strategies.get(country, DefaultShipping())
```

### 3. Introduce Null Object

**Before:**
```python
def get_customer_name(customer):
    if customer is None:
        return "Guest"
    return customer.name
```

**After:**
```python
class NullCustomer:
    name = "Guest"
    
def get_customer_name(customer):
    return (customer or NullCustomer()).name
```

## Debt Repayment Strategies

### Strategy 1: Boy Scout Rule

> "Leave the code cleaner than you found it"

```yaml
implementation:
  rule: "每次提交必须修复至少一个问题"
  scope:
    - 代码异味
    - 命名不规范
    - 缺少注释
    - 小规模重构
  validation: "所有测试必须通过"
```

### Strategy 2: dedicated Debt Sprints

```yaml
planning:
  frequency: "每季度一次"
  duration: "1-2 周"
  team_size: "2-4 人"
  focus: "高优先级债务"
  goals:
    - 债务清单减少 30%
    - 关键指标改善
    - 文档更新
```

### Strategy 3: Investment Time

```yaml
allocation:
  principle: "20% 时间用于技术改进"
  breakdown:
    - 10%: 债务偿还
    - 5%: 工具改进
    - 5%: 学习研究
  tracking: "在 Sprint 中明确任务"
```

## Prevention Mechanisms

### CI/CD Quality Gates

```yaml
quality_gates:
  - name: "Code Coverage"
    threshold: 80%
    fail_on_decrease: true
    
  - name: "Code Smells"
    max_per_file: 5
    max_per_function: 1
    
  - name: "Technical Debt Ratio"
    max: 5%
    
  - name: "Critical Issues"
    count: 0
```

### Code Review Checklist

```markdown
## Technical Debt Review Checklist

### 代码质量
- [ ] 函数长度 < 50 行
- [ ] 圈复杂度 < 10
- [ ] 无重复代码
- [ ] 命名规范清晰

### 架构
- [ ] 无循环依赖
- [ ] 符合 SOLID 原则
- [ ] 适当的抽象层级

### 测试
- [ ] 测试覆盖 > 80%
- [ ] 无脆弱测试
- [ ] 测试命名规范

### 文档
- [ ] 复杂逻辑有注释
- [ ] 公共 API 有文档
- [ ] 更新相关文档
```

## Metrics Dashboard

### Key Metrics

| Metric | Baseline | Target | Frequency |
|--------|----------|--------|-----------|
| TDR | 15% | < 5% | Monthly |
| Code Coverage | 65% | > 80% | Sprint |
| Avg. Function Length | 35 | < 20 | Weekly |
| Debt Items Open | 150 | < 50 | Monthly |
| Debt Interest Rate | 8% | < 3% | Quarterly |

### Tracking Tools

- SonarQube Dashboard
- Jira Debt Tickets
- Custom Dashboard (Grafana)
- Tech Radar

## Multi-Language Code Examples

### Java: SonarQube API 调用与静态分析集成

```java
// SonarQubeClient.java — SonarQube API 客户端（用于自动化债务分析）
package com.company.tdq;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.time.Duration;
import java.util.*;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

/**
 * SonarQube API 客户端
 * 用于在 CI/CD 流水线中查询项目技术债务指标并生成报告
 */
public class SonarQubeClient {
    private static final ObjectMapper MAPPER = new ObjectMapper();
    private final HttpClient httpClient;
    private final String apiBaseUrl;
    private final String authToken;

    public SonarQubeClient(String baseUrl, String authToken) {
        this.apiBaseUrl = baseUrl.endsWith("/") ? baseUrl + "api" : baseUrl + "/api";
        this.authToken = authToken;
        this.httpClient = HttpClient.newBuilder()
                .connectTimeout(Duration.ofSeconds(10))
                .build();
    }

    /** 查询项目技术债务指标 */
    public TechnicalDebtMetrics getProjectMetrics(String projectKey) throws Exception {
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(apiBaseUrl + "/measures/component?component=" + projectKey
                        + "&metricKeys=code_smells,sqale_index,sqale_debt_ratio,"
                        + "duplicated_lines_density,coverage,complexity,ncloc"))
                .header("Authorization", "Basic " + Base64.getEncoder()
                        .encodeToString((authToken + ":").getBytes()))
                .GET()
                .build();

        HttpResponse<String> response = httpClient.send(request,
                HttpResponse.BodyHandlers.ofString());

        if (response.statusCode() != 200) {
            throw new RuntimeException("SonarQube API error: " + response.body());
        }

        return parseMetrics(projectKey, response.body());
    }

    private TechnicalDebtMetrics parseMetrics(String projectKey, String json) throws Exception {
        JsonNode root = MAPPER.readTree(json);
        JsonNode measures = root.path("component").path("measures");

        TechnicalDebtMetrics metrics = new TechnicalDebtMetrics();
        metrics.projectKey = projectKey;

        for (JsonNode m : measures) {
            String metric = m.path("metric").asText();
            String value = m.path("value").asText();
            switch (metric) {
                case "code_smells" -> metrics.codeSmells = Integer.parseInt(value);
                case "sqale_index" -> metrics.sqaleIndexMinutes = Long.parseLong(value);
                case "sqale_debt_ratio" -> metrics.debtRatio = Double.parseDouble(value);
                case "duplicated_lines_density" -> metrics.duplicationRate = Double.parseDouble(value);
                case "coverage" -> metrics.coverage = Double.parseDouble(value);
                case "complexity" -> metrics.complexity = Integer.parseInt(value);
                case "ncloc" -> metrics.linesOfCode = Integer.parseInt(value);
            }
        }

        // 计算技术债务等级
        if (metrics.debtRatio < 5) metrics.grade = "A (Excellent)";
        else if (metrics.debtRatio < 10) metrics.grade = "B (Good)";
        else if (metrics.debtRatio < 20) metrics.grade = "C (Acceptable)";
        else if (metrics.debtRatio < 50) metrics.grade = "D (High)";
        else metrics.grade = "F (Critical)";

        return metrics;
    }

    /** 根据质量门禁判断是否通过 */
    public boolean passesQualityGate(String projectKey) throws Exception {
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(apiBaseUrl + "/qualitygates/project_status?projectKey=" + projectKey))
                .header("Authorization", "Basic " + Base64.getEncoder()
                        .encodeToString((authToken + ":").getBytes()))
                .GET()
                .build();

        HttpResponse<String> response = httpClient.send(request,
                HttpResponse.BodyHandlers.ofString());
        JsonNode root = MAPPER.readTree(response.body());
        return "OK".equals(root.path("projectStatus").path("status").asText());
    }

    // 内部数据类
    static class TechnicalDebtMetrics {
        String projectKey;
        int codeSmells;
        long sqaleIndexMinutes;
        double debtRatio;       // 技术债务比率（%）
        double duplicationRate; // 代码重复率（%）
        double coverage;        // 测试覆盖率（%）
        int complexity;         // 总圈复杂度
        int linesOfCode;        // 代码行数
        String grade;           // 等级：A-F

        @Override
        public String toString() {
            return String.format("""
                    === Technical Debt Report: %s ===
                    Lines of Code:      %d
                    Code Smells:        %d
                    Debt Ratio:         %.1f%%
                    Grade:              %s
                    Duplication Rate:   %.1f%%
                    Coverage:           %.1f%%
                    Complexity:         %d
                    Estimated Effort:   %d hours
                    """,
                    projectKey, linesOfCode, codeSmells, debtRatio, grade,
                    duplicationRate, coverage, complexity, sqaleIndexMinutes / 60);
        }
    }
}
```

```xml
<!-- pom.xml — 静态分析工具集成配置 -->
<project>
  <build>
    <plugins>
      <!-- SonarQube 扫描 -->
      <plugin>
        <groupId>org.sonarsource.scanner.maven</groupId>
        <artifactId>sonar-maven-plugin</artifactId>
        <version>3.10.0.2594</version>
      </plugin>
      <!-- Checkstyle 代码规范 -->
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-checkstyle-plugin</artifactId>
        <version>3.3.1</version>
        <configuration>
          <configLocation>checkstyle.xml</configLocation>
          <failOnViolation>true</failOnViolation>
          <maxAllowedViolations>10</maxAllowedViolations>
        </configuration>
      </plugin>
    </plugins>
  </build>
</project>
```

### Python: 技术债务量化脚本与 SonarQube API 调用

```python
#!/usr/bin/env python3
"""
技术债务量化分析脚本
从 SonarQube 获取指标，计算债务优先级，生成团队看板数据
"""
import os
import json
import logging
from datetime import datetime, timedelta
from typing import Optional

import requests
import pandas as pd
from dataclasses import dataclass, asdict

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)


@dataclass
class DebtItem:
    """单个技术债务项"""
    key: str
    component: str
    message: str
    severity: str         # BLOCKER / CRITICAL / MAJOR / MINOR / INFO
    debt: str             # 修复预估时间，如 "1h"
    type: str             # BUG / VULNERABILITY / CODE_SMELL
    creation_date: str
    update_date: str
    project: str


class TechDebtAnalyzer:
    """技术债务分析器 — 集成 SonarQube API 与本地静态分析"""

    def __init__(self, sonar_url: str, sonar_token: str):
        self.sonar_url = sonar_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Basic {sonar_token}"})

    def get_issues(self, project_key: str,
                   severities: Optional[list] = None,
                   types: Optional[list] = None,
                   page_size: int = 500) -> list[DebtItem]:
        """获取项目所有技术债务 issues"""
        params = {
            "componentKeys": project_key,
            "ps": page_size,
            "additionalFields": "_all",
        }
        if severities:
            params["severities"] = ",".join(severities)
        if types:
            params["types"] = ",".join(types)

        all_issues = []
        page = 1

        while True:
            params["p"] = page
            resp = self.session.get(
                f"{self.sonar_url}/api/issues/search",
                params=params,
                timeout=30,
            )
            resp.raise_for_status()
            data = resp.json()

            for issue in data.get("issues", []):
                all_issues.append(DebtItem(
                    key=issue["key"],
                    component=issue["component"],
                    message=issue["message"],
                    severity=issue.get("severity", "MAJOR"),
                    debt=issue.get("debt", "0min"),
                    type=issue.get("type", "CODE_SMELL"),
                    creation_date=issue.get("creationDate", ""),
                    update_date=issue.get("updateDate", ""),
                    project=project_key,
                ))

            if len(data.get("issues", [])) < page_size:
                break
            page += 1

        return all_issues

    def calculate_priority_score(self, items: list[DebtItem]) -> float:
        """
        计算综合债务优先级分数

        权重公式：
        Score = (BLOCKER*10 + CRITICAL*5 + MAJOR*2 + MINOR*0.5) + 时间衰减因子
        """
        severity_weights = {
            "BLOCKER": 10, "CRITICAL": 5,
            "MAJOR": 2, "MINOR": 0.5, "INFO": 0.1,
        }

        base_score = sum(severity_weights.get(item.severity, 0) for item in items)

        # 时间衰减因子：3个月前的债务权重降低
        three_months_ago = datetime.now() - timedelta(days=90)
        stale_count = sum(
            1 for item in items
            if item.update_date and item.update_date[:10] < three_months_ago.strftime("%Y-%m-%d")
        )
        stale_penalty = stale_count * -0.5

        return base_score + stale_penalty

    def generate_report(self, project_key: str) -> dict:
        """生成完整的债务分析报告"""
        logger.info(f"Analyzing tech debt for project: {project_key}")

        # 获取所有 issues
        all_issues = self.get_issues(project_key)
        logger.info(f"Total issues found: {len(all_issues)}")

        # 按严重级别分类
        by_severity = {}
        for issue in all_issues:
            by_severity.setdefault(issue.severity, []).append(issue)

        # 按类型分类
        by_type = {}
        for issue in all_issues:
            by_type.setdefault(issue.type, []).append(issue)

        report = {
            "project": project_key,
            "analyzed_at": datetime.now().isoformat(),
            "summary": {
                "total_items": len(all_issues),
                "blocker": len(by_severity.get("BLOCKER", [])),
                "critical": len(by_severity.get("CRITICAL", [])),
                "major": len(by_severity.get("MAJOR", [])),
                "minor": len(by_severity.get("MINOR", [])),
                "bugs": len(by_type.get("BUG", [])),
                "vulnerabilities": len(by_type.get("VULNERABILITY", [])),
                "code_smells": len(by_type.get("CODE_SMELL", [])),
            },
            "priority_score": self.calculate_priority_score(all_issues),
            "recommendations": [],
        }

        # 生成建议
        if report["summary"]["blocker"] > 0:
            report["recommendations"].append(
                "IMMEDIATE: Blockers detected — schedule emergency refactoring"
            )
        if report["summary"]["critical"] > 10:
            report["recommendations"].append(
                "HIGH: Critical items exceed threshold — plan for next sprint"
            )
        if report["priority_score"] > 100:
            report["recommendations"].append(
                "ALERT: Overall debt score is high — consider a dedicated debt sprint"
            )

        return report


# 命令行入口
if __name__ == "__main__":
    analyzer = TechDebtAnalyzer(
        sonar_url=os.getenv("SONAR_URL", "http://localhost:9000"),
        sonar_token=os.getenv("SONAR_TOKEN", ""),
    )
    project = os.getenv("SONAR_PROJECT", "my-project")
    report = analyzer.generate_report(project)

    print(json.dumps(report, indent=2, ensure_ascii=False))

    # 输出 CSV 用于导入 Jira/Trello
    all_items = analyzer.get_issues(project)
    df = pd.DataFrame([asdict(item) for item in all_items])
    df.to_csv(f"tech-debt-{project}.csv", index=False)
    logger.info(f"Report saved to tech-debt-{project}.csv")
```

### 静态分析工具配置

```yaml
# .github/workflows/static-analysis.yml — GitHub Actions 静态分析流水线
name: Static Code Analysis
on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  analysis:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up JDK 17
        uses: actions/setup-java@v4
        with:
          java-version: '17'

      - name: SonarQube Scan
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
        run: |
          mvn sonar:sonar \
            -Dsonar.host.url=${{ vars.SONAR_HOST }} \
            -Dsonar.qualitygate.wait=true

      - name: Checkstyle Analysis
        run: mvn checkstyle:checkstyle

      - name: Debt Threshold Check
        run: |
          # Ensure debt ratio stays below 10%
          python scripts/check-debt-threshold.py --max-ratio 10
```

### Go: 债务量化 CLI 工具

```go
// cmd/debt/main.go — 技术债务 CLI 量化工具
package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"log"
	"net/http"
	"os"
	"time"
)

// DebtMetrics 对应 SonarQube API 返回的技术债务指标
type DebtMetrics struct {
	Project    string  `json:"project"`
	DebtRatio  float64 `json:"debt_ratio"`
	CodeSmells int     `json:"code_smells"`
	Coverage   float64 `json:"coverage"`
	Grade      string  `json:"grade"`
}

// fetchFromSonar 调用 SonarQube API 获取指标
func fetchFromSonar(baseURL, projectKey, token string) (*DebtMetrics, error) {
	url := fmt.Sprintf("%s/api/measures/component?component=%s&metricKeys=code_smells,sqale_debt_ratio,coverage",
		baseURL, projectKey)

	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		return nil, fmt.Errorf("create request: %w", err)
	}
	req.Header.Set("Authorization", "Basic "+token)

	client := &http.Client{Timeout: 10 * time.Second}
	resp, err := client.Do(req)
	if err != nil {
		return nil, fmt.Errorf("api call: %w", err)
	}
	defer resp.Body.Close()

	var result struct {
		Component struct {
			Measures []struct {
				Metric string `json:"metric"`
				Value  string `json:"value"`
			} `json:"measures"`
		} `json:"component"`
	}
	if err := json.NewDecoder(resp.Body).Decode(&result); err != nil {
		return nil, fmt.Errorf("decode response: %w", err)
	}

	metrics := &DebtMetrics{Project: projectKey}
	for _, m := range result.Component.Measures {
		switch m.Metric {
		case "code_smells":
			fmt.Sscanf(m.Value, "%d", &metrics.CodeSmells)
		case "sqale_debt_ratio":
			fmt.Sscanf(m.Value, "%f", &metrics.DebtRatio)
		case "coverage":
			fmt.Sscanf(m.Value, "%f", &metrics.Coverage)
		}
	}

	// 计算等级
	switch {
	case metrics.DebtRatio < 5:
		metrics.Grade = "A"
	case metrics.DebtRatio < 10:
		metrics.Grade = "B"
	case metrics.DebtRatio < 20:
		metrics.Grade = "C"
	case metrics.DebtRatio < 50:
		metrics.Grade = "D"
	default:
		metrics.Grade = "F"
	}

	return metrics, nil
}

func main() {
	var sonarURL, project, token, format string
	flag.StringVar(&sonarURL, "url", "http://localhost:9000", "SonarQube base URL")
	flag.StringVar(&project, "project", "", "Project key")
	flag.StringVar(&token, "token", "", "Auth token")
	flag.StringVar(&format, "format", "text", "Output format (text/json)")
	flag.Parse()

	if project == "" || token == "" {
		log.Fatal("--project and --token are required")
	}

	metrics, err := fetchFromSonar(sonarURL, project, token)
	if err != nil {
		log.Fatalf("Failed to fetch metrics: %v", err)
	}

	switch format {
	case "json":
		enc := json.NewEncoder(os.Stdout)
		enc.SetIndent("", "  ")
		enc.Encode(metrics)
	default:
		fmt.Printf("Technical Debt Report: %s\n", metrics.Project)
		fmt.Printf("  Grade:         %s\n", metrics.Grade)
		fmt.Printf("  Debt Ratio:    %.1f%%\n", metrics.DebtRatio)
		fmt.Printf("  Code Smells:   %d\n", metrics.CodeSmells)
		fmt.Printf("  Coverage:      %.1f%%\n", metrics.Coverage)
	}
}
```

## Error Handling

### Error Scenario 1: 静态分析误报处理 (P2)

**触发条件**: SonarQube / ESLint / Pylint 静态分析工具报告了不准确的问题（false positive）

**处理流程**:
```
IF 经人工审查确认为误报
THEN
  1. 在静态分析工具中添加误报豁免：
     - SonarQube: 标记 issue 为 "Won't Fix" 并添加注释说明原因
     - ESLint: /* eslint-disable-next-line <rule> — 原因说明 */
     - Pylint: # pylint: disable=<code>  # 原因说明
  2. 在项目级配置中添加全局豁免规则（如适用）：
     - SonarQube: sonar.issue.ignore.multicriteria
     - ESLint: .eslintrc.js 中的 rules 配置
     - Checkstyle: suppressions.xml
  3. 添加代码注释说明为什么忽略该规则
  4. 在技术债务跟踪工具中记录豁免项及到期复查日期
  5. 定期复查所有豁免项（建议每季度），确认条件未变化
END
```

**降级方案**: 暂时提高质量门禁阈值，允许少量误报通过，确保 CI/CD 流水线不阻塞

**升级条件**: 误报影响超过 10% 的代码库，或误报数量超过 50 个

### Error Scenario 2: 债务偿还引入功能回归 (P0)

**触发条件**: 重构/清理技术债务后，已有功能出现行为异常或测试失败

**处理流程**:
```
IF 债务偿还 MR 引入回归
THEN
  1. 立即暂停 MR 合并，标记为 DO NOT MERGE
  2. 分析回归范围：
     - 缩小到具体哪个重构操作引入了回归
     - 对比重构前后的代码差异
  3. 评估影响严重程度：
     - 影响核心功能 → 立即回滚整个 MR
     - 影响边缘功能 → 修复问题后推进 MR
  4. 制定修复方案：
     - 回滚有问题的重构，保持其他重构不变
     - 或修复回归问题后补充更多边界测试
  5. 补充缺失的测试用例，防止同类回归
  6. 重新运行完整回归测试套件，确认全部通过
END
```

**降级方案**: 回滚整个债务偿还 MR，将其拆分为更小的、可独立验证的变更分批提交

**升级条件**: 回归问题影响生产环境或核心业务流程

### Error Scenario 3: 团队债务意识不足 (P2)

**触发条件**: 技术债务持续增加但团队未识别或未跟踪，债务指标持续恶化

**处理流程**:
```
IF 连续两个 Sprint 债务比率上升（超过 15%）
THEN
  1. 在 CI 流水线中强制执行质量门禁：
     - 新增代码的覆盖率下降 > 1% → 构建警告
     - 新增代码异味 > 3 个/文件 → 构建失败
     - 技术债务比率 > 15% → 构建失败
  2. 将债务指标纳入 Sprint Review 的必要展示项
  3. 在 Code Review 检查清单中增加债务相关检查项
  4. 为每个功能需求分配 20% 的债务偿还容量（Sprint 承诺）
  5. 设置债务指标告警：
     - SonarQube Webhook → Slack 通知
     - 每周自动生成债务趋势报告
  6. 每季度安排一次债务 Sprint，专门偿还高优先级债务
END
```

**降级方案**: 由架构师每周人工审查新增债务并分配到对应团队

**升级条件**: 债务比率连续两个季度上升，影响交付速度超过 30%


## Quality Standards

> Acceptance criteria and quality gates for manage-tech-debt deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | All known debt is registered and visible | Automated check |
| Standard 2 | Debt paydown rate is 10% or higher per quarter | Automated check |
| Standard 3 | Debt impact on delivery decreases 15% year-over-year | Automated check |
## References

- [harness-engineering.md](../standards/harness-engineering.md)
- [output-validation-checklist.md](../evaluations/output-validation-checklist.md)
- [regression-checklist.md](../evaluations/regression-checklist.md)
