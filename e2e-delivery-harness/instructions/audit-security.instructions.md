---
name: audit-security
description: "安全审计执行指南，用于执行安全测试"
applyTo: "scenarios/audit-security/**"
phase: governance
type: instruction
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
language: "zh-CN"
tags: ['instruction', 'technical']
---
# Security Audit Instruction

## Objective

执行安全审计，发现安全漏洞和风险，确保系统符合安全要求。

## Prerequisites

1. 测试环境可用
2. 安全测试工具
3. 系统文档
4. 渗透测试授权

## Process Steps

### Step 1: 收集信息

1. 收集系统架构
2. 收集 API 文档
3. 收集认证机制
4. 识别资产清单

### Step 2: 识别攻击面

1. 识别入口点
2. 识别信任边界
3. 识别数据流
4. 识别关键资产

### Step 3: 执行安全测试

按照 OWASP Top 10 执行：

1. Broken Access Control
2. Cryptographic Failures
3. Injection
4. Insecure Design
5. Security Misconfiguration
6. Vulnerable Components
7. Auth Failures
8. Data Integrity Failures
9. Logging Failures
10. SSRF

### Step 4: 分析漏洞

1. 验证漏洞存在
2. 评估严重程度
3. 分析利用难度
4. 提出修复建议

### Step 5: 编写报告

1. 整理漏洞列表
2. 评估风险
3. 提出建议
4. 归档报告

## Quality Gates

### 准入检查

- [ ] 测试环境可用
- [ ] 测试工具就绪
- [ ] 审计范围已定

### 准出检查

- [ ] OWASP Top 10 已覆盖
- [ ] 漏洞列表完整
- [ ] 报告已归档

## Handoff Criteria

交接给开发前：

- [ ] 安全审计报告已完成
- [ ] 漏洞已确认
- [ ] 修复建议已提供


## Overview

> High-level description of the audit-security execution process.
>
> This instruction defines the technical approach, key activities, and success criteria for the audit-security scenario.


## Technical Specifications

> Detailed technical requirements and implementation guidelines for audit-security.

### Required Tools
- **OWASP ZAP / Burp Suite**: Web 应用动态安全扫描（DAST）
- **Trivy / Snyk / Dependabot**: 依赖项漏洞扫描（SCA）
- **SonarQube / Semgrep / CodeQL**: 静态应用安全测试（SAST）
- **Nmap / Masscan**: 网络端口扫描与服务发现
- **Lynis / CIS-CAT**: 系统基线合规扫描（CIS Benchmark）
- **Vault / AWS Secrets Manager**: 密钥检测与泄露扫描

### Environment Requirements
- 安全扫描工具版本保持最新（≤30 天延迟更新）
- 扫描目标环境有授权书（渗透测试授权、安全评估授权）
- 扫描结果存储加密（使用 KMS 加密的 S3/数据库）
- 隔离扫描网络（安全扫描流量不影响生产业务）

### Configuration Parameters
- `SCAN_SCHEDULE`: 扫描频率（SAST 每次 Push，DAST 每周，PenTest 每季度）
- `CRITICAL_VULN_SLA`: 严重漏洞修复 SLA（CVSS ≥9.0 → 24h，7.0-8.9 → 72h）
- `COMPLIANCE_FRAMEWORK`: 合规框架（SOC2 / ISO27001 / PCI-DSS / HIPAA）
- `SCAN_SCOPE`: 扫描范围（代码仓库、容器镜像、运行环境、网络拓扑）
- `ALERT_CHANNEL`: 漏洞告警通道（Critical → PagerDuty, High → Slack #security）


## Best Practices

> Industry-standard best practices for audit-security execution.

1. **Practice 1**: Conduct regular vulnerability assessments and penetration testing
2. **Practice 2**: Maintain compliance mapping against security frameworks
3. **Practice 3**: Document all findings with severity ratings and evidence


## Multi-Language Code Examples

This section provides production-ready security scanning configurations and automation scripts across multiple programming languages. Each example is designed for CI/CD integration with structured reporting for automated security auditing.

### Python (Bandit SAST + OWASP ZAP DAST Automation)

```python
#!/usr/bin/env python3
"""
Automated Security Scanning Pipeline
Integrates Bandit (SAST) and OWASP ZAP (DAST) for comprehensive analysis.
Uses: bandit (SAST) + OWASP ZAP API (DAST) + structured JSON reporting.
Usage: python security-scan.py --target-url https://staging.example.com
"""

import subprocess, json, sys, time, logging, os, argparse
from typing import Dict, List

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)


# === Phase 1: SAST with Bandit ===
def run_bandit_scan(target_dirs: List[str]) -> Dict:
    """
    Execute Bandit SAST scan to find common Python security issues:
    - Hardcoded passwords and secrets
    - SQL injection via raw query execution
    - Command injection via shell=True
    - Insecure deserialization (pickle, yaml.load)
    - Path traversal in file operations

    Bandit scoring: severity (low/medium/high) x confidence (low/medium/high)
    """
    logger.info("Starting Bandit SAST scan on: %s", ", ".join(target_dirs))
    os.makedirs("reports", exist_ok=True)

    cmd = [
        "bandit", "-r",
        "-ll",                          # Severity threshold >= low
        "-c", "bandit.yaml",            # Custom configuration
        "-f", "json",
        "-o", "reports/bandit-report.json",
    ] + target_dirs

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        report = json.loads(result.stdout) if result.stdout else {}
        high = report.get("high_severity", 0)
        medium = report.get("medium_severity", 0)
        low = report.get("low_severity", 0)
        logger.info("Bandit complete: H=%d M=%d L=%d", high, medium, low)
        return {
            "tool": "bandit", "status": "completed",
            "high": high, "medium": medium, "low": low,
            "report": "reports/bandit-report.json",
            "results": report.get("results", []),
        }
    except subprocess.TimeoutExpired:
        logger.error("Bandit timed out after 300s")
        return {"tool": "bandit", "status": "timeout"}
    except FileNotFoundError:
        logger.error("Bandit not found. Install: pip install bandit")
        return {"tool": "bandit", "status": "failed", "error": "Bandit not found"}


# === Phase 2: DAST with OWASP ZAP ===
def run_zap_scan(target_url: str, zap_url: str, api_key: str) -> Dict:
    """
    Execute OWASP ZAP active scan via REST API.
    Discovers and tests for: XSS, SQLi, CSRF, Path Traversal, Command Injection.
    Requires ZAP running in daemon mode: zap.sh -daemon -port 8080

    Scan workflow:
    1. Spider crawl to discover all endpoints
    2. Active scan to probe for vulnerabilities
    3. Collect and categorize alerts by risk level
    """
    import requests
    logger.info("Starting ZAP DAST scan on: %s", target_url)

    api_base = f"{zap_url}/JSON"
    headers = {"X-ZAP-API-Key": api_key} if api_key else {}

    try:
        # --- Step 1: Spider crawl ---
        logger.info("ZAP Step 1: Spider crawling...")
        r = requests.get(f"{api_base}/spider/action/scan/",
            params={"url": target_url, "maxChildren": 15},
            headers=headers, timeout=30)
        spider_id = r.json().get("scan")
        while True:
            status = requests.get(f"{api_base}/spider/view/status/",
                params={"scanId": spider_id}, headers=headers, timeout=10)
            if status.json().get("status") == "100":
                break
            time.sleep(5)

        # --- Step 2: Active scan ---
        logger.info("ZAP Step 2: Active vulnerability scan...")
        r = requests.get(f"{api_base}/ascan/action/scan/",
            params={"url": target_url, "recurse": True},
            headers=headers, timeout=30)
        scan_id = r.json().get("scan")

        start = time.time()
        while time.time() - start < 1800:  # 30 min timeout
            r = requests.get(f"{api_base}/ascan/view/status/",
                params={"scanId": scan_id}, headers=headers, timeout=10)
            pct = int(r.json().get("status", 0))
            if pct == 100:
                break
            time.sleep(10)

        # --- Step 3: Collect alerts ---
        alerts = requests.get(f"{api_base}/alert/view/alerts/",
            params={"baseurl": target_url},
            headers=headers, timeout=30).json().get("alerts", [])

        counts = {"high": 0, "medium": 0, "low": 0, "info": 0}
        for a in alerts:
            risk = a.get("risk", "").lower()
            if "high" in risk:      counts["high"] += 1
            elif "medium" in risk:  counts["medium"] += 1
            elif "low" in risk:     counts["low"] += 1
            else:                   counts["info"] += 1

        with open("reports/zap-report.json", "w") as f:
            json.dump({"alerts": alerts, "summary": counts}, f, indent=2)

        logger.info("ZAP complete: H=%d M=%d L=%d I=%d",
                     counts["high"], counts["medium"], counts["low"], counts["info"])
        return {"tool": "zap", "status": "completed", **counts,
                "report": "reports/zap-report.json"}

    except requests.exceptions.ConnectionError:
        logger.error("Cannot reach ZAP API at %s. Ensure ZAP is running.", zap_url)
        return {"tool": "zap", "status": "failed", "error": "ZAP unreachable"}
    except Exception as e:
        logger.error("ZAP scan failed: %s", str(e))
        return {"tool": "zap", "status": "failed", "error": str(e)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automated Security Scanner")
    parser.add_argument("--target-url", help="Target URL for ZAP DAST scan")
    parser.add_argument("--target-dirs", nargs="+", default=["src/", "app/"],
                        help="Source directories for Bandit scan")
    parser.add_argument("--sast-only", action="store_true", help="Run SAST only")
    args = parser.parse_args()

    results = {"sast": run_bandit_scan(args.target_dirs)}

    if not args.sast_only and args.target_url:
        results["dast"] = run_zap_scan(
            args.target_url,
            os.getenv("ZAP_API_URL", "http://localhost:8080"),
            os.getenv("ZAP_API_KEY", ""),
        )

    with open("reports/scan-summary.json", "w") as f:
        json.dump(results, f, indent=2)

    # Exit non-zero if high-severity findings exist
    high_total = results["sast"].get("high", 0) + \
                 results.get("dast", {}).get("high", 0)
    sys.exit(1 if high_total > 0 else 0)
```

### Java (SpotBugs + OWASP Dependency Check Maven Plugin)

```xml
<!-- pom.xml
  Maven build configuration for automated security scanning in Java projects.
  Combines SpotBugs (bytecode-level SAST) with OWASP Dependency Check (SCA).
-->
<project>
  <build>
    <plugins>
      <!-- ================================================================ -->
      <!-- SpotBugs Maven Plugin                                            -->
      <!-- Static analysis on compiled bytecode using FindSecBugs detectors -->
      <!-- ================================================================ -->
      <plugin>
        <groupId>com.github.spotbugs</groupId>
        <artifactId>spotbugs-maven-plugin</artifactId>
        <version>4.8.6</version>
        <configuration>
          <!-- Effort: Min/Default/Max (Max finds more but is slower) -->
          <effort>Max</effort>
          <!-- Threshold: Low/Medium/High -->
          <threshold>Medium</threshold>
          <!-- Fail build on any security bug pattern -->
          <failOnError>true</failOnError>
          <!-- Include only security-relevant detectors -->
          <includeFilterFile>spotbugs-security-include.xml</includeFilterFile>
          <!-- Exclude known false positives -->
          <excludeFilterFile>spotbugs-security-exclude.xml</excludeFilterFile>
          <plugins>
            <!-- FindSecBugs: 100+ security detectors for Java -->
            <plugin>
              <groupId>com.h3xstream.findsecbugs</groupId>
              <artifactId>findsecbugs-plugin</artifactId>
              <version>1.12.0</version>
            </plugin>
          </plugins>
        </configuration>
        <executions>
          <execution>
            <goals><goal>check</goal></goal>
            <phase>verify</phase>
          </execution>
        </executions>
      </plugin>

      <!-- ================================================================ -->
      <!-- OWASP Dependency Check Plugin                                    -->
      <!-- Scans project dependencies against NVD for known CVEs            -->
      <!-- ================================================================ -->
      <plugin>
        <groupId>org.owasp</groupId>
        <artifactId>dependency-check-maven</artifactId>
        <version>10.0.4</version>
        <configuration>
          <!-- Fail build on CVSS >= 7.0 (High severity) -->
          <failBuildOnCVSS>7</failBuildOnCVSS>
          <!-- Suppress known false positive CVEs -->
          <suppressionFiles>
            <suppressionFile>dependency-check-suppressions.xml</suppressionFile>
          </suppressionFiles>
          <!-- Generate both HTML report and JSON for CI parsing -->
          <formats>
            <format>HTML</format>
            <format>JSON</format>
          </formats>
          <!-- NVD API key (free: https://nvd.nist.gov/developers) -->
          <nvdApiKey>${env.NVD_API_KEY}</nvdApiKey>
          <!-- Don't fail build on NVD update errors (graceful degradation) -->
          <failOnError>false</failOnError>
        </configuration>
        <executions>
          <execution>
            <goals><goal>check</goal></goals>
            <phase>verify</phase>
          </execution>
        </executions>
      </plugin>
    </plugins>
  </build>
</project>
```

```bash
# === Java Security Scan Commands ===
# Run full security checks (bound to Maven verify phase)
mvn clean verify

# Run security checks only (skip unit tests for quick feedback)
mvn spotbugs:check dependency-check:check

# Update NVD cache manually (run weekly in CI pipeline)
mvn dependency-check:update-only

# Generate SpotBugs GUI report for manual review
mvn spotbugs:gui
```

### Go (gosec + govulncheck Integration)

```go
// cmd/security-scan/main.go
//
// Security scanning for Go projects combining:
//   gosec      - SAST scanning for insecure code patterns
//   govulncheck - Dependency vulnerability scanning against Go vuln DB
//
// Usage:
//   go run cmd/security-scan/main.go
//   go run cmd/security-scan/main.go --severity=high
package main

import (
	"encoding/json"
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
	"strings"
)

// ScanResult captures the outcome of a single security scan tool
type ScanResult struct {
	Tool   string `json:"tool"`
	Status string `json:"status"`
	Issues int    `json:"issues,omitempty"`
	Detail string `json:"detail,omitempty"`
	Error  string `json:"error,omitempty"`
}

// runGosec performs static analysis on Go source code.
//
// gosec detects:
//   - Hardcoded credentials (token, password, secret patterns)
//   - SQL injection via string concatenation
//   - Insecure cryptography (MD5, SHA1, RC4, DES)
//   - Unsafe file permissions (os.Chmod with 0777)
//   - Command injection (os/exec with shell)
//   - Integer overflow, race conditions, nil pointer dereference
func runGosec(severity string) ScanResult {
	fmt.Printf("[gosec] Starting SAST scan (severity >= %s)...\n", severity)

    	cmd := exec.Command("gosec",
		"-severity="+severity,       // low, medium, high
		"-confidence=medium",
		"-quiet",                      // Suppress progress in CI
		"-fmt=json",
		"-out=reports/gosec-report.json",
		"./...",
	)

	// gosec exits non-zero when issues are found (expected)
	output, err := cmd.CombinedOutput()
	if err != nil {
		var report struct {
			Stats struct {
				High   int `json:"high"`
				Medium int `json:"medium"`
				Low    int `json:"low"`
			} `json:"stats"`
		}
		if json.Unmarshal(output, &report) == nil {
			issues := report.Stats.High + report.Stats.Medium + report.Stats.Low
			fmt.Printf("[gosec] Found %d issues (H:%d M:%d L:%d)\n",
				issues, report.Stats.High, report.Stats.Medium, report.Stats.Low)
			return ScanResult{
				Tool: "gosec", Status: "completed", Issues: issues,
				Detail: fmt.Sprintf("H:%d M:%d L:%d",
					report.Stats.High, report.Stats.Medium, report.Stats.Low),
			}
		}
		return ScanResult{Tool: "gosec", Status: "failed", Error: string(output)}
	}
	return ScanResult{Tool: "gosec", Status: "completed", Issues: 0, Detail: "clean"}
}

// runGovulncheck scans Go module dependencies against the Go vulnerability
// database (https://vuln.go.dev). Uses source mode to only report vulns
// affecting code actually used by the project.
func runGovulncheck() ScanResult {
	fmt.Println("[govulncheck] Scanning dependencies for CVEs...")

	// -json: machine-readable output
	// ./...: scan all packages in the module
	cmd := exec.Command("govulncheck", "-json", "./...")
	output, err := cmd.Output()

	if err != nil {
		// govulncheck exits non-zero if vulnerabilities exist
		var result struct {
			Vulns []interface{} `json:"vulns"`
		}
		if json.Unmarshal(output, &result) == nil && len(result.Vulns) > 0 {
			fmt.Printf("[govulncheck] Found %d known vulnerabilities\n", len(result.Vulns))
			return ScanResult{Tool: "govulncheck", Status: "completed", Issues: len(result.Vulns)}
		}
		return ScanResult{Tool: "govulncheck", Status: "completed", Issues: 0}
	}

	var result struct {
		Vulns []interface{} `json:"vulns"`
	}
	json.Unmarshal(output, &result)
	return ScanResult{Tool: "govulncheck", Status: "completed", Issues: len(result.Vulns)}
}

func main() {
	_ = os.MkdirAll("reports", 0755)

	severity := "medium"
	if len(os.Args) > 1 && strings.HasPrefix(os.Args[1], "--severity=") {
		severity = strings.TrimPrefix(os.Args[1], "--severity=")
	}

	results := map[string]ScanResult{
		"gosec":       runGosec(severity),
		"govulncheck": runGovulncheck(),
	}

	report, _ := json.MarshalIndent(results, "", "  ")
	_ = os.WriteFile("reports/go-security-summary.json", report, 0644)
	fmt.Println("\n[summary] Results: reports/go-security-summary.json")

	for _, r := range results {
		if r.Status == "failed" {
			os.Exit(2)
		}
	}
}
```

```bash
# Install Go security tools
go install github.com/securego/gosec/v2/cmd/gosec@latest
go install golang.org/x/vuln/cmd/govulncheck@latest

# Run full Go security scan
go run cmd/security-scan/main.go

# Run individual tools
gosec -severity=high -quiet -fmt=text ./...
govulncheck ./...
```

### JavaScript (ESLint Security Plugin + npm audit + Snyk CLI)

```javascript
// scripts/security-scan.js
/**
 * Node.js Security Scanning Pipeline
 *
 * Three-layer security analysis for JavaScript/TypeScript projects:
 * 1. ESLint with eslint-plugin-security (SAST for code patterns)
 * 2. npm audit (dependency vulnerability against npm advisory DB)
 * 3. Snyk CLI (comprehensive scanning with policy engine)
 *
 * Usage: node scripts/security-scan.js
 */

const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const REPORTS = path.join(__dirname, '..', 'reports');
fs.mkdirSync(REPORTS, { recursive: true });

// --- ESLint Security Configuration ---
// Add this to .eslintrc.js for IDE integration:
const ESLINT_CONFIG = `
// .eslintrc.js - Security-focused ESLint configuration
module.exports = {
  plugins: ['security', 'no-secrets'],
  extends: [
    'plugin:security/recommended',    // OWASP Top 10 JS patterns
    'plugin:no-secrets/recommended',   // Detect hardcoded secrets/keys
  ],
  rules: {
    'security/detect-object-injection': 'error',
    'security/detect-non-literal-fs-filename': 'error',
    'security/detect-non-literal-regexp': 'error',
    'security/detect-unsafe-regex': 'error',
    'security/detect-eval-with-expression': 'error',
    'security/detect-no-csrf-before-method-override': 'error',
    'security/detect-pseudoRandomBytes': 'warn',
    'no-secrets/no-secrets': ['error', {
      tolerance: 3.0,  // Shannon entropy threshold
      additionalRegexes: {
        'AWS Access Key': 'AKIA[0-9A-Z]{16}',
        'GitHub Token': 'gh[pousr]_[A-Za-z0-9_]{36,}',
      },
    }],
  },
};
`;

/**
 * Phase 1: ESLint with security plugins
 * Scans code for: eval usage, insecure regex, path traversal, CSRF,
 * hardcoded secrets, prototype pollution, and more.
 */
function runESLintSecurity() {
  console.log('[eslint-security] Starting SAST scan...');
  try {
    execSync(
      'npx eslint . --ext .js,.ts,.jsx,.tsx ' +
      '--format json --output-file reports/eslint-report.json',
      { encoding: 'utf-8', timeout: 120000 }
    );
    const reportPath = path.join(REPORTS, 'eslint-report.json');
    if (fs.existsSync(reportPath)) {
      const report = JSON.parse(fs.readFileSync(reportPath, 'utf-8'));
      const errors = report.reduce((s, f) => s + f.errorCount, 0);
      const warnings = report.reduce((s, f) => s + f.warningCount, 0);
      console.log(`[eslint-security] ${errors} errors, ${warnings} warnings`);
      return { tool: 'eslint-security', errors, warnings };
    }
    return { tool: 'eslint-security', status: 'no-report' };
  } catch (err) {
    // ESLint errors on findings but still writes report
    if (fs.existsSync(path.join(REPORTS, 'eslint-report.json'))) {
      console.log('[eslint-security] Complete (issues found)');
      return { tool: 'eslint-security', status: 'completed' };
    }
    console.error('[eslint-security] Failed:', err.message);
    return { tool: 'eslint-security', status: 'failed', error: err.message };
  }
}

/**
 * Phase 2: npm audit
 * Scans node_modules against npm advisory database.
 * Fails only on high/critical vulnerabilities (--audit-level).
 */
function runNpmAudit() {
  console.log('[npm-audit] Scanning dependencies...');
  try {
    const output = execSync('npm audit --audit-level=moderate --json',
      { encoding: 'utf-8', timeout: 60000 });
    const result = JSON.parse(output);
    const vulns = Object.values(result.vulnerabilities || {});
    const critical = vulns.filter(v => v.severity === 'critical').length;
    const high = vulns.filter(v => v.severity === 'high').length;
    fs.writeFileSync(path.join(REPORTS, 'npm-audit-report.json'),
      JSON.stringify(result, null, 2));
    console.log(`[npm-audit] ${critical} critical, ${high} high, ${vulns.length} total`);
    return { tool: 'npm-audit', critical, high, total: vulns.length };
  } catch (err) {
    if (err.stdout) {
      try {
        const result = JSON.parse(err.stdout);
        const vulns = Object.keys(result.vulnerabilities || {}).length;
        console.log(`[npm-audit] ${vulns} vulnerabilities found`);
        return { tool: 'npm-audit', total: vulns };
      } catch (_) { /* ignore parse errors */ }
    }
    console.error('[npm-audit] Failed:', err.message);
    return { tool: 'npm-audit', status: 'failed', error: err.message };
  }
}

/**
 * Phase 3: Snyk CLI
 * Comprehensive scan: open source vulns, SAST, IaC, container.
 * Requires: SNYK_TOKEN environment variable (snyk auth)
 */
function runSnyk() {
  if (!process.env.SNYK_TOKEN) {
    console.warn('[snyk] SNYK_TOKEN not set; skipping');
    return { tool: 'snyk', status: 'skipped' };
  }
  console.log('[snyk] Running Snyk scan...');
  try {
    const output = execSync(
      'npx snyk test --all-projects --severity-threshold=medium --json',
      { encoding: 'utf-8', timeout: 300000 });
    fs.writeFileSync(path.join(REPORTS, 'snyk-report.json'), output);
    return { tool: 'snyk', status: 'completed' };
  } catch (err) {
    if (err.stdout) {
      fs.writeFileSync(path.join(REPORTS, 'snyk-report.json'), err.stdout);
      return { tool: 'snyk', status: 'completed' };
    }
    console.error('[snyk] Failed:', err.message);
    return { tool: 'snyk', status: 'failed', error: err.message };
  }
}

// --- Pipeline Orchestration ---
const results = {
  eslint: runESLintSecurity(),
  npmAudit: runNpmAudit(),
  snyk: runSnyk(),
};

fs.writeFileSync(path.join(REPORTS, 'security-summary.json'),
  JSON.stringify(results, null, 2));
console.log('\n[summary] Reports generated in reports/');
console.log(JSON.stringify(results, null, 2));

// Fail CI on critical/high findings
const hasCritical = results.npmAudit.critical > 0;
process.exit(hasCritical ? 1 : 0);
```

```bash
# === JavaScript Security Scan Commands ===
# Install dependencies
npm install --save-dev eslint eslint-plugin-security eslint-plugin-no-secrets
npm install -g snyk

# Run full pipeline
node scripts/security-scan.js

# Run individual scans
npx eslint . --ext .js,.ts --format stylish
npm audit --audit-level=high
snyk test --all-projects
```

### Shell (nmap + nikto Automated Penetration Testing)

```bash
#!/bin/bash
#===============================================================================
# Automated Penetration Testing Script
#
# Combines:
#   nmap  - Network discovery, port scanning, service/OS fingerprinting
#   nikto - Web server vulnerability scanner (60,000+ test patterns)
#
# Usage:
#   ./pentest-scan.sh <target-host> [options]
# Options:
#   -p <ports>     Port range (default: 1-10000)
#   -o <dir>       Output directory (default: reports/)
#   -a             Aggressive mode (intrusive tests enabled)
#   -q             Quiet mode (minimal output)
#
# Prerequisites: apt install nmap nikto (or brew install on macOS)
#===============================================================================

set -euo pipefail

TARGET="${1:?Usage: $0 <target-host>}"
PORT_RANGE="${2:-1-10000}"
OUTPUT_DIR="reports/$(date +%Y%m%d_%H%M%S)_${TARGET}"
AGGRESSIVE=false
QUIET=false

# Parse options
shift 2>/dev/null || true
while getopts "p:o:aq" opt; do
    case "$opt" in
        p) PORT_RANGE="$OPTARG" ;;
        o) OUTPUT_DIR="$OPTARG" ;;
        a) AGGRESSIVE=true ;;
        q) QUIET=true ;;
    esac
done

mkdir -p "$OUTPUT_DIR"

# Pre-flight: verify tools exist
for tool in nmap nikto; do
    if ! command -v "$tool" &>/dev/null; then
        echo "[FATAL] '$tool' not found. Install: apt install $tool"
        exit 2
    fi
done

echo "=============================================="
echo "  Penetration Test: $TARGET"
echo "  Port Range: $PORT_RANGE"
echo "  Started:    $(date)"
echo "=============================================="

#----------------------------------------------------------------------
# Phase 1: Host Discovery
#----------------------------------------------------------------------
echo "[Phase 1] Host discovery..."
nmap -sn "$TARGET" -oG "$OUTPUT_DIR/ping-sweep.gnmap" || \
    echo "[WARN] Host may not respond to ping; proceeding anyway"

#----------------------------------------------------------------------
# Phase 2: Port Scanning + Service Detection
#----------------------------------------------------------------------
echo "[Phase 2] Port scanning ($PORT_RANGE)..."
NMAP_ARGS=(
    -sS                    # TCP SYN scan (stealth)
    -sV                    # Service version detection
    -O                     # OS fingerprinting
    --version-intensity 5  # Aggressive version detection
    -p "$PORT_RANGE"       # Scan specified ports
    -T4                    # Timing: Aggressive
    --max-retries 3        # Limit retries for speed
    --open                 # Only show open ports
    -oA "$OUTPUT_DIR/nmap" # All output formats
)

if [ "$AGGRESSIVE" = true ]; then
    NMAP_ARGS+=(-sC --script=vuln)  # Default scripts + vuln detection
fi

nmap "${NMAP_ARGS[@]}" "$TARGET"

OPEN_PORTS=$(grep -oP '\d+/open/tcp' "$OUTPUT_DIR/nmap.gnmap" | \
             cut -d'/' -f1 | tr '\n' ',' | sed 's/,$//')
echo "[Phase 2] Open ports: $OPEN_PORTS"

#----------------------------------------------------------------------
# Phase 3: Web Vulnerability Scanning with Nikto
#----------------------------------------------------------------------
echo "[Phase 3] Web vulnerability scanning..."

HTTP_PORTS=$(grep -oP '\d+/open/tcp//http' "$OUTPUT_DIR/nmap.gnmap" 2>/dev/null | cut -d'/' -f1 || true)

if [ -z "$HTTP_PORTS" ]; then
    echo "[Phase 3] No HTTP services detected; skipping Nikto"
else
    for PORT in $HTTP_PORTS; do
        PROTOCOL="http"
        if [ "$PORT" = "443" ] || \
           grep -q "${PORT}/open/tcp//https" "$OUTPUT_DIR/nmap.gnmap" 2>/dev/null; then
            PROTOCOL="https"
        fi
        echo "[Phase 3] Scanning ${PROTOCOL}://${TARGET}:${PORT}..."

        NIKTO_ARGS=(
            -host "$TARGET"
            -port "$PORT"
            -output "$OUTPUT_DIR/nikto-${PORT}.html"
            -Format html
            -Tuning 123456789        # All test types
            -nointeractive
            -timeout 30
        )

        [ "$PROTOCOL" = "http" ] && NIKTO_ARGS+=(-nossl)

        if [ "$AGGRESSIVE" = true ]; then
            NIKTO_ARGS+=(-evasion 1 -mutate 2)
        fi

        nikto "${NIKTO_ARGS[@]}" 2>&1 | tee "$OUTPUT_DIR/nikto-${PORT}.log"
        VULNS=$(grep -c "OSVDB" "$OUTPUT_DIR/nikto-${PORT}.log" || echo 0)
        echo "[Phase 3] Nikto: $VULNS potential issues on port $PORT"
    done
fi

#----------------------------------------------------------------------
# Phase 4: Summary Report
#----------------------------------------------------------------------
echo "[Phase 4] Generating executive summary..."

cat > "$OUTPUT_DIR/executive-summary.md" << REPORT
# Penetration Test Report
- **Target**: $TARGET
- **Date**: $(date)
- **Ports**: $PORT_RANGE
- **Mode**: $([ "$AGGRESSIVE" = true ] && echo "Aggressive" || echo "Standard")

## Open Ports
\`\`\`
$(grep -E '^\d+/open' "$OUTPUT_DIR/nmap.nmap" 2>/dev/null || echo "None found")
\`\`\`

## Tool Results
- nmap: $OUTPUT_DIR/nmap.nmap
- nikto: $OUTPUT_DIR/nikto-*.log

*Detailed reports available in: $OUTPUT_DIR/*
REPORT

echo "=============================================="
echo "  Scan Complete!"
echo "  Reports: $OUTPUT_DIR/"
echo "=============================================="
```


## Error Handling

> 安全审计执行过程中的常见异常场景及对应的处理策略、降级方案和升级条件。

### Error Scenario 1: 扫描工具不可用/超时 (P1)

**触发条件**: 任一安全扫描工具（Bandit/SpotBugs/gosec/ESLint/ZAP/nmap/nikto）在启动时不可用（未安装、进程崩溃、许可证过期）或在规定超时时间内未完成扫描任务。

**处理流程**:
```
IF 工具启动失败 (exit code = 127 / FileNotFoundError)
THEN
  1. 检查工具是否已安装：which <tool> 或 command -v <tool>
  2. 如未安装，从官方源安装并重试（apt/brew/go install/npm install）
  3. 如已安装，检查运行日志定位具体失败原因（权限/PATH/依赖缺失）
  4. 记录工具不可用事件并通知安全工具链负责人
  5. 在扫描结果中标记该工具状态为 "SKIPPED-TOOL-UNAVAILABLE"
END

IF 扫描工具超时 (超过配置的时间阈值)
THEN
  1. 发送 SIGTERM 终止扫描进程，等待 30 秒后若未退出则发送 SIGKILL
  2. 分析超时原因：扫描范围过大 / 目标响应慢 / 网络延迟 / 工具 bug
  3. 缩小扫描范围后重试（如减少端口数量、限制扫描深度）
  4. 若重试仍超时，将扫描拆分为多个子任务分批执行
  5. 在报告中标明 "PARTIAL-RESULTS" 并附上已完成的扫描结果
END
```

**降级方案**: 对于不可用的 SAST 工具，切换至备用扫描工具（如 Bandit 不可用时使用 Semgrep 或 Pyre）；对于超时的 DAST 工具，分片执行扫描任务（按端点/路径拆分），将扫描间隔拉长至多个 CI 流水线周期完成；对于不可用的网络扫描工具，使用轻量级替代方案（如 masscan 替代 nmap 的端口扫描阶段）。

**升级条件**: 同一工具连续失败超过 3 次，或关键扫描工具（SAST/SCA）不可用超过 2 小时，影响发布流水线阻塞时，升级至安全工具链负责人和安全架构师；若扫描超时导致合规审计无法按时完成，升级至 CISO。

### Error Scenario 2: 大量误报导致分析效率下降 (P2)

**触发条件**: 安全扫描工具返回超过 100 条告警，或人工验证后确认误报率超过 60%（即 10 条告警中至少 6 条为误报），导致安全审计工程师需要花费大量时间筛选和验证真实漏洞。

**处理流程**:
```
IF 扫描报告告警总数 > 100 OR 误报率 > 60%
THEN
  1. 运行告警聚合脚本，按 CWE 分类和风险级别对告警分组
  2. 从上一轮审计结果中提取已确认的误报规则，自动滤除已知误报
  3. 调整扫描工具的配置参数以降低误报率：
     a. 提升严重级别阈值（如从 low→medium）
     b. 设置排除规则（如跳过测试目录、第三方代码）
     c. 启用误报抑制文件（如 spotbugs-security-exclude.xml）
  4. 使用机器学习分类器（如 Bandit 的 skip 注释 / 工具特定的 suppress 注解）
     将高频误报模式添加至自动排除列表
  5. 通知安全分析团队对新增告警规则进行人工验证和调优
END
```

**降级方案**: 在自动过滤阶段保留所有告警的原始记录，只调整展示优先级（高置信度的真实漏洞置顶展示）；对误报率 > 80% 的工具自动切换至低敏感度配置；对于已知误报模式，批量添加 suppress 注解并记录至误报管理数据库。

**升级条件**: 误报率 > 80% 且持续超过 3 个扫描周期，或由于大量误报导致一个及以上的真实高危漏洞被遗漏（由后续渗透测试或安全事件证实），升级至安全工具链架构师重新评估扫描策略和工具选型。

### Error Scenario 3: 发现正在被利用的 0day 漏洞 (P0)

**触发条件**: 在安全审计过程中，通过威胁情报源（如 Twitter 安全社区、NVD 预披露、厂商安全公告）或渗透测试手段发现系统所用组件存在正在野外被广泛利用的 0day 漏洞，且该漏洞影响当前版本的生产环境。

**处理流程**:
```
IF 确认存在正在被利用的 0day 漏洞且影响生产环境
THEN
  1. 立即启动安全应急响应流程（IRT），优先级 P0
  2. 评估影响范围：
     a. 识别受影响的所有服务、实例和部署环境
     b. 评估利用条件和可能造成的业务影响（数据泄露/服务中断/合规）
  3. 执行临时缓解措施（30 分钟内完成）：
     a. WAF 规则拦截利用流量
     b. 网络 ACL 限制受影响服务的来源 IP
     c. 禁用受影响的接口或功能特性
     d. 如有补丁，应用热修复（hotfix）到生产环境
  4. 通知干系人：
     a. 发送 P0 告警至 on-call 安全团队和运维团队
     b. 通知技术负责人和业务负责人
     c. 如涉及用户数据，通知隐私合规团队
  5. 持续监控利用尝试（查看 WAF 日志、IDS/IPS 告警）
  6. 在安全报告中记录 0day 漏洞详情、缓解措施和响应时间
END
```

**降级方案**: 如无法立即修复或缓解，采取网络隔离措施将受影响服务从生产网络中移除（或将流量路由至沙箱环境）；如果无法隔离，实施增强日志记录以备事后取证（确保日志包含 X-Forwarded-For、User-Agent 等关键字段）；对于无法修复的遗留系统，部署虚拟补丁（如 ModSecurity 规则）。

**升级条件**: 0day 漏洞导致用户数据泄露或服务中断，立即升级至 CISO、CTO 和法律合规团队，启动数据泄露通知流程；如涉及监管合规（PCI-DSS/SOC2/GDPR），同时通知相关监管机构和客户。创建安全事件工单，并在 24 小时内完成初步事后分析。

### Error Scenario 4: 合规标准变更导致审计范围调整 (P1)

**触发条件**: 在安全审计执行期间或两个审计周期之间，相关安全合规标准（如 PCI-DSS v4.0 → v4.1、SOC2 新增信任服务准则、GDPR 新增指南）发生变更，或企业新接入的第三方平台要求满足特定的安全基线，导致当前审计范围与最新合规要求不匹配。

**处理流程**:
```
IF 检测到合规标准版本变更或新增审计范围
THEN
  1. 从合规管理平台或安全公告获取最新的合规要求和变更差异对照表
  2. 对比新旧标准的控制项差异：
     a. 新增控制项及其安全要求
     b. 被废弃或修改的控制项
     c. 控制项严重级别变化
  3. 评估变化对当前审计计划的影响：
     a. 需要新增的审计检查和测试用例
     b. 需要修改的现有审计流程和工具配置
     c. 对审计工期和资源需求的影响
  4. 更新审计范围文档：
     a. 在审计追踪表中标注范围变更及变更时间
     b. 更新合规映射矩阵（Control mapping matrix）
     c. 调整扫描工具配置以覆盖新增控制项
  5. 补充执行新增或修改后的审计测试
  6. 在最终审计报告中注明合规变更和对应的范围调整
END
```

**降级方案**: 如在新标准生效日期前无法完成全部审计范围调整，优先覆盖与 P0/P1 漏洞相关的新增控制项，标记剩余控制项为 "SCOPE-PENDING" 并制定补审计划；使用自动化合规扫描工具（如 ScoutSuite、Prowler）快速覆盖基础控制项；向后兼容：新添加的控制项仍满足旧标准要求时，优先按旧标准完成审计，按新标准补充差距分析。

**升级条件**: 合规标准变更导致需要新增超过 30% 的审计测试用例，或变更涉及核心安全架构（加密算法更新/网络架构变更），或新标准要求的生产环境整改窗口短于 30 天，升级至安全架构师和合规负责人做影响评估和资源重分配决策。
## Quality Standards

> Acceptance criteria and quality gates for audit-security deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | All critical and high findings have remediation plans | Automated check |
| Standard 2 | Compliance coverage meets target framework requirements | Automated check |
| Standard 3 | Audit trail is complete and tamper-evident | Automated check |
## References

- [harness-engineering.md](../standards/harness-engineering.md)
- [output-validation-checklist.md](../evaluations/output-validation-checklist.md)
- [regression-checklist.md](../evaluations/regression-checklist.md)
