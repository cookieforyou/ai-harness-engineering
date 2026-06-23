---
name: manage-dependencies
description: "依赖管理场景的技术指令，详细说明依赖管理的工具和方法"
applyTo: "scenarios/manage-dependencies/**"
phase: development
type: instruction
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['instruction', 'technical']
---
# Dependency Management Instructions

## Overview

本指令提供依赖管理的详细技术规范，包括工具选择、命令示例和最佳实践。

## Supported Package Managers

### Node.js / npm

```bash
# 查看依赖树
npm ls --depth=0        # 直接依赖
npm ls --all           # 完整依赖树
npm ls <package>       # 特定依赖

# 查看过时依赖
npm outdated

# 更新依赖
npm update             # 更新到 semver 允许范围
npm update <package>   # 更新特定依赖
npx npm-check-updates -u  # 交互式更新

# 安全审计
npm audit             # 漏洞扫描
npm audit fix         # 自动修复
npm audit --audit-level=high  # 仅显示高级别

# 许可证检查
npx license-checker --csv --out dependencies.csv
```

### Python / pip

```bash
# 导出依赖
pip freeze > requirements.txt
pipreqs . --force       # 基于代码分析

# 检查过时
pip list --outdated

# 安全检查
pip-audit
safety check

# 版本约束
pip install "requests>=2.28.0,<3.0.0"
```

### Go / go.mod

```bash
# 查看依赖
go list -m all          # 所有依赖
go list -m tree         # 依赖树

# 更新依赖
go get -u              # 更新所有
go get <package>@latest # 更新特定

# 清理依赖
go mod tidy
go mod verify

# 安全检查
gosec ./...
```

## Dependency Analysis

### 依赖健康度指标

| Metric | Good | Warning | Critical |
|--------|------|---------|----------|
| 依赖年龄 | < 6 months | 6-12 months | > 12 months |
| 更新频率 | Weekly/Monthly | Quarterly | Yearly+ |
| 社区规模 | > 1000 stars | 100-1000 | < 100 |
| 维护状态 | Active | Limited | Abandoned |

### 漏洞评估标准

- **Critical (9-10)**: 立即修复，RCE 或数据泄露风险
- **High (7-8.9)**: 1周内修复，权限提升或注入风险
- **Medium (4-6.9)**: 1月内修复，信息泄露风险
- **Low (0-3.9)**: 计划修复，较低风险

### 许可证兼容性矩阵

| License Type | Commercial Use | Modification | Distribution |
|--------------|---------------|-------------|--------------|
| MIT | Yes | Yes | Yes |
| Apache 2.0 | Yes | Yes | Yes |
| BSD 3-Clause | Yes | Yes | Yes |
| GPL 3.0 | Yes | Yes | Yes (copyleft) |
| AGPL 3.0 | Yes | Yes | Yes (strong copyleft) |
| Proprietary | Varies | No | No |

## Update Strategy

### 渐进式更新流程

```
1. 隔离环境测试
   └── 在 CI 隔离环境测试

2. 小批次更新
   └── 每次最多 5 个依赖

3. 回归测试
   └── 运行完整测试套件

4. 代码审查
   └── Review 变更内容

5. 合并部署
   └── 合并到主分支
```

### 批量更新策略

```yaml
# update-config.yaml
update_strategy:
  batch_size: 5
  interval_days: 7
  max_version_jump:
    major: 0  # 不允许主版本跳跃
    minor: 2  # 最多跳跃2个小版本
    patch: 5   # 最多跳跃5个补丁版本
  require_approval: true
  auto_rollback: true
```

## Lock File Management

### package-lock.json

```json
{
  "dependencies": {
    "lodash": {
      "version": "4.17.21",
      "resolved": "https://registry.npmjs.org/lodash/-/lodash-4.17.21.tgz",
      "integrity": "sha512-v2kDEe57lecTulaDIuNTPy3Ry4gLGJ6Z1O3vE1krgXZNrsQ+LFTGHVxVjcXPs17LhbZ3eBuzfnkkMOs1+pCjfyw==",
      "dev": false
    }
  }
}
```

### requirements.txt

```
# 固定版本
requests==2.28.0

# 范围版本（谨慎使用）
django>=3.2,<4.0

# 特定来源
git+https://github.com/user/repo.git@v1.2.3
-e git+https://github.com/user/repo.git#egg=mypackage
```

## Vulnerability Remediation

### 修复优先级

1. **立即处理**：Critical/High 漏洞且有可用修复
2. **计划处理**：High/Medium 漏洞需要代码修改
3. **监控观察**：无直接风险的漏洞
4. **接受风险**：无法修复且可接受的漏洞

### 缓解措施

```yaml
# security-config.yaml
mitigations:
  - type: WAF_RULE
    description: 阻止特定攻击向量
    expires: "2024-06-01"

  - type: NETWORK_ISOLATION
    description: 隔离受影响组件
    scope: internal_only

  - type: ADDITIONAL_MONITORING
    description: 加强日志和告警
    alert_threshold: 1/hour
```

## Rollback Procedures

### 自动回滚触发条件

- 构建失败
- 测试失败率 > 5%
- 安全扫描发现新漏洞
- 性能回归 > 20%

### 回滚命令

```bash
# npm
git checkout package-lock.json
npm ci

# pip
pip install -r requirements.lock

# go
git checkout go.sum
go mod download
```

## Best Practices

### Do's

1. 使用锁文件确保一致性
2. 定期更新依赖（至少每季度）
3. 关注安全通报
4. 最小化依赖数量
5. 优先选择活跃维护的库
6. 审核新增依赖
7. 记录重大依赖变更

### Don'ts

1. 不要忽略安全警告
2. 不要直接修改锁文件
3. 不要使用未知来源的包
4. 不要跳过测试直接部署
5. 不要忽略许可证要求
6. 不要使用已弃用的包
7. 不要忽略版本不兼容警告

## Multi-Language Code Examples

### Java: Maven/Gradle 依赖审计与 OWASP 插件

```xml
<!-- pom.xml — Maven OWASP Dependency Check 插件配置 -->
<project>
  <build>
    <plugins>
      <plugin>
        <groupId>org.owasp</groupId>
        <artifactId>dependency-check-maven</artifactId>
        <version>9.0.9</version>
        <configuration>
          <failBuildOnCVSS>7</failBuildOnCVSS>      <!-- CVSS >= 7时构建失败 -->
          <formats>
            <format>HTML</format>
            <format>JSON</format>
          </formats>
          <suppressionFiles>
            <suppressionFile>owasp-suppressions.xml</suppressionFile>
          </suppressionFiles>
        </configuration>
        <executions>
          <execution>
            <goals><goal>check</goal></goals>
          </execution>
        </executions>
      </plugin>
    </plugins>
  </build>
</project>
```

```bash
# Maven 依赖审计命令
mvn dependency:tree -Dverbose                           # 查看完整依赖树（含冲突信息）
mvn org.owasp:dependency-check-maven:check              # 执行 OWASP 安全扫描
mvn dependency-check:check -DfailBuildOnCVSS=9          # 仅 CVSS >= 9 时阻断构建

# Gradle 依赖审计命令
gradle dependencies --configuration compileClasspath    # 查看编译时依赖树
gradle dependencyCheckAnalyze                           # OWASP 安全检查
gradle dependencyUpdates                                # 检查可用更新
```

```kotlin
// build.gradle.kts — Gradle OWASP 插件与版本锁定
plugins {
    id("org.owasp.dependencycheck") version "9.0.9"
    id("com.github.ben-manes.versions") version "0.51.0"  // 版本检查
}

dependencyCheck {
    failBuildOnCVSS = 7.0f
    formats = listOf("HTML", "JSON")
    suppressionFile = "owasp-suppressions.xml"
    nvd {
        apiKey = System.getenv("NVD_API_KEY") ?: ""
        delay = 4000  // NVD API 请求间隔（毫秒），避免限流
    }
}

// 强制版本锁定 —— 解决传递依赖冲突
configurations.all {
    resolutionStrategy {
        failOnVersionConflict()
        force("com.fasterxml.jackson.core:jackson-databind:2.16.1")
        eachDependency {
            if (requested.group == "org.apache.logging.log4j") {
                useVersion("2.21.1")
            }
        }
    }
}
```

### Go: go mod tidy + govulncheck

```go
// go.mod — 依赖管理文件（自动生成后的示例）
module github.com/myorg/myservice

go 1.22

require (
    github.com/gin-gonic/gin v1.9.1
    github.com/go-sql-driver/mysql v1.7.1
    github.com/golang-jwt/jwt/v5 v5.2.0
    github.com/redis/go-redis/v9 v9.3.0
)

// exclude 指令排除存在已知漏洞的间接依赖版本
exclude golang.org/x/crypto v0.14.0

// replace 指令解决传递依赖冲突
replace github.com/ugorji/go => github.com/ugorji/go v1.2.12
```

```bash
# Go 依赖管理命令
go mod tidy              # 清理未使用的依赖并补充缺失的
go mod verify            # 验证依赖校验和是否匹配
go mod download          # 下载所有依赖到本地缓存

# 漏洞扫描工具链
go install golang.org/x/vuln/cmd/govulncheck@latest
govulncheck ./...        # 扫描项目所有包的安全漏洞

# 静态安全分析
go install github.com/securego/gosec/v2/cmd/gosec@latest
gosec -no-fail -fmt sarif -out results.sarif ./...

# 依赖树可视化
go graph                 # 输出 Mermaid 格式依赖图
```

### JavaScript: npm audit + yarn audit + Renovate 配置

```json
// renovate.json — Renovate 自动依赖更新配置
{
  "$schema": "https://docs.renovatebot.com/renovate-schema.json",
  "extends": [
    "config:base",
    ":separateMajorMinor",
    ":combinePatchMinorUpdates",
    "group:allNonMajor"
  ],
  "labels": ["dependencies", "auto-update"],
  "packageRules": [
    {
      "matchUpdateTypes": ["patch", "pin"],
      "automerge": true,
      "platformAutomerge": true
    },
    {
      "matchDepTypes": ["devDependencies"],
      "automerge": true
    },
    {
      "matchUpdateTypes": ["major"],
      "labels": ["dependencies", "major-update"],
      "reviewers": ["team:platform"]
    }
  ],
  "vulnerabilityAlerts": {
    "labels": ["security"],
    "enabled": true,
    "automerge": true
  },
  "schedule": ["before 9am on Monday"],
  "timezone": "Asia/Shanghai"
}
```

```bash
# npm 安全审计
npm audit                    # 查看所有安全漏洞
npm audit --json             # JSON 格式输出（用于 CI 解析）
npm audit --audit-level=high # 仅显示高危及以上
npm audit fix                # 自动修复（在 semver 范围内更新）
npm audit fix --force        # 强制修复（可能引入 breaking changes）

# yarn 安全审计
yarn audit                   # 扫描漏洞
yarn audit --groups dependencies  # 仅审计生产依赖
yarn upgrade-interactive     # 交互式选择更新版本
```

```javascript
// audit-ci.config.js — CI 安全审计配置
module.exports = {
  'critical': true,     // Critical 漏洞阻断构建
  'high': true,         // High 漏洞阻断构建
  'moderate': false,    // Moderate 仅警告
  'low': false,         // Low 仅警告

  // 白名单列表（已有缓解措施的漏洞）
  allowlist: [
    'GHSA-xxxx-xxxx-xxxx',
  ],

  // 报表输出
  'report-type': 'full',
  'output-format': {
    'type': 'json',
    'file': './reports/audit-report.json'
  }
};
```

```bash
# CI/CD 组合审计流水线
#!/bin/bash
set -euo pipefail

echo "=== Dependency Security Audit ==="
npm audit --audit-level=high || {
  npm audit --json > audit-report.json
  echo "High/Critical vulnerabilities found. See audit-report.json"
  exit 1
}

echo "=== License Compliance Check ==="
npx license-checker --csv --out license-report.csv --failOn 'GPL;AGPL'

echo "=== Snyk Deep Scan ==="
npx snyk test --json > snyk-report.json || true

echo "=== Audit Complete ==="
```

## Error Handling

### Error Scenario 1: 传递依赖冲突 (P1)

**触发条件**: Maven/Gradle 构建时出现 `DependencyResolutionException` 或 `ConflictException`，多个传递依赖引入同一库的不同版本

**处理流程**:
```
IF 构建日志显示传递依赖版本冲突
THEN
  1. 运行依赖分析命令输出完整依赖树
     - Maven: mvn dependency:tree -Dverbose
     - Gradle: gradle dependencies --configuration compileClasspath
     - Go: go list -m all
     - npm: npm ls --all
  2. 定位冲突来源：识别引入冲突版本的上游依赖路径
  3. 评估影响范围：确认冲突是否导致 ClassNotFoundException / NoSuchMethodError
  4. 制定解决策略：
     - Maven: 在 pom.xml 中使用 <dependencyManagement> 显式声明版本
     - Gradle: 在 resolutionStrategy 中使用 force() 锁定版本
     - Go: 使用 replace / exclude 指令
     - npm: 使用 overrides 字段强制版本
  5. 在隔离环境运行完整测试套件验证兼容性
  6. 通过 Code Review 后合并
END
```

**降级方案**: 回溯到上一个已知兼容的依赖版本组合，延后冲突依赖的升级计划

**升级条件**: 冲突涉及超过 5 个传递依赖，或影响核心功能模块的编译

### Error Scenario 2: Lock 文件合并冲突 (P1)

**触发条件**: Git 合并时 `package-lock.json` / `yarn.lock` / `go.sum` / `gradle.lockfile` 发生合并冲突

**处理流程**:
```
IF Git 报告 lock 文件冲突
THEN
  1. 接受双方更改（保留冲突标记），不手动编辑 lock 文件
  2. 根据包管理器执行重建命令：
     - npm: 删除 node_modules + package-lock.json → npm install 重新生成
     - yarn: git checkout --theirs yarn.lock → yarn install --frozen-lockfile
     - Go: git checkout HEAD -- go.sum → go mod tidy 重新生成
     - Gradle: gradle generateLockFiles 重新生成锁文件
  3. 对比重新生成的 lock 文件，确认合并后依赖版本正确
  4. 检查关键依赖版本未发生意外降级
  5. 运行完整 CI 测试流水线验证
  6. 提交重新生成的 lock 文件
END
```

**降级方案**: 分别从两个分支的 lock 文件构建，对比功能测试结果，再决定合并策略

**升级条件**: lock 文件冲突涉及超过 10 个依赖，或核心依赖版本被意外降级

### Error Scenario 3: 私有仓库认证失败 (P2)

**触发条件**: CI/CD 构建时从私有 NPM / Maven / Go 仓库拉取依赖返回 401/403 错误

**处理流程**:
```
IF 构建日志显示 401/403 认证错误
THEN
  1. 检查 CI 环境变量中的仓库认证凭据是否配置
     - npm: 确认 NPM_TOKEN 环境变量存在且格式正确
     - Maven: 检查 settings.xml 中 server 配置
     - Go: 检查 GOPROXY 和 GONOSUMCHECK 环境变量
  2. 验证凭据有效期：
     - npm token list 查看 token 是否过期
     - GitHub: gh auth status 检查认证状态
  3. 检查网络策略：
     - CI 运行环境 IP 是否在仓库访问白名单中
     - 防火墙规则是否阻止对仓库地址的访问
  4. 轮换凭据并更新 CI 环境变量
  5. 手动触发一次 CI 重跑验证修复
END
```

**降级方案**: 临时将私有依赖发布到公共 registry 的私有 scope，或使用本地缓存的 artifact

**升级条件**: 认证修复耗时超过 2 小时，阻塞多个团队的构建流水线


## Quality Standards

> Acceptance criteria and quality gates for manage-dependencies deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | All known CVEs are identified and tracked | Automated check |
| Standard 2 | License compliance is 100% with no prohibited licenses | Automated check |
| Standard 3 | Critical patches are applied within 30 days | Automated check |
## References

- [harness-engineering.md](../standards/harness-engineering.md)
- [output-validation-checklist.md](../evaluations/output-validation-checklist.md)
- [regression-checklist.md](../evaluations/regression-checklist.md)
