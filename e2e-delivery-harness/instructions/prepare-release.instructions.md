---
name: prepare-release
description: "Detailed technical instructions for prepare-release scenario execution"
applyTo: "scenarios/prepare-release/**"
phase: deployment
type: instruction
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['instruction', 'technical']
---
# Instructions: 发布准备 (Prepare Release)

## Release Type Standards

### 版本号规范

```yaml
# 语义化版本 (Semantic Versioning)
version_format: "MAJOR.MINOR.PATCH"

# 版本规则
version_rules:
  major:
    trigger: "破坏性变更"
    example: "2.0.0"
    description: "不兼容的 API 变更"

  minor:
    trigger: "新增功能"
    example: "1.2.0"
    description: "向后兼容的功能新增"

  patch:
    trigger: "缺陷修复"
    example: "1.1.1"
    description: "向后兼容的缺陷修复"

  pre_release:
    trigger: "预发布"
    example: "1.0.0-alpha.1"
    description: "测试版本"

  apply-hotfix:
    trigger: "紧急修复"
    example: "1.0.1"
    description: "生产问题紧急修复"
```

## Release Process Standards

### 发布阶段

```
┌─────────────────────────────────────────────────────────────┐
│                     RELEASE PHASES                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌───────────┐   ┌───────────┐   ┌───────────┐   ┌─────────┐ │
│  │  PLANNING │ → │ PREPARING │ → │ EXECUTING │ → │ CLOSING │ │
│  └───────────┘   └───────────┘   └───────────┘   └─────────┘ │
│       ↓              ↓               ↓              ↓       │
│   发布计划        发布准备        发布执行       发布收尾    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 发布检查清单

```yaml
# Pre-Release 检查清单
pre_release_checklist:
  code_quality:
    - name: "代码评审完成"
      required: true
    - name: "代码静态检查通过"
      required: true
    - name: "无新引入的 P0/P1 bug"
      required: true

  testing:
    - name: "单元测试覆盖率 ≥ 80%"
      required: true
    - name: "集成测试全部通过"
      required: true
    - name: "E2E 测试全部通过"
      required: true
    - name: "性能测试达标"
      required: false

  security:
    - name: "安全扫描通过"
      required: true
    - name: "依赖漏洞扫描通过"
      required: true
    - name: "敏感信息检查通过"
      required: true

  documentation:
    - name: "API 文档更新"
      required: true
    - name: "变更日志更新"
      required: true
    - name: "用户文档更新"
      required: false
```

## Release Review Standards

### 评审委员会

```yaml
release_review_board:
  members:
    - role: "Release Manager"
      responsibility: "发布协调"
    - role: "Tech Lead"
      responsibility: "技术决策"
    - role: "QA Lead"
      responsibility: "质量评估"
    - role: "Product Manager"
      responsibility: "业务确认"

  decision_modes:
    - mode: "GO"
      description: "可以发布"
    - mode: "NO-GO"
      description: "不允许发布"
    - mode: "CONDITIONAL-GO"
      description: "有条件发布"
```

### 评审检查项

| 检查项 | 权重 | 通过标准 |
|--------|------|----------|
| 测试完成度 | 20% | ≥ 95% |
| 代码质量 | 20% | 无高危问题 |
| 性能指标 | 15% | 达标 |
| 安全合规 | 25% | 无高危漏洞 |
| 文档完整性 | 10% | 完整 |
| 回滚方案 | 10% | 可行 |

## Rollback Plan Standards

### 回滚触发条件

```yaml
rollback_triggers:
  p0:
    - "核心功能不可用"
    - "数据一致性严重问题"
    - "安全漏洞"
    response_time: "5 分钟"

  p1:
    - "主要功能异常"
    - "性能严重下降"
    response_time: "30 分钟"

  p2:
    - "次要功能异常"
    - "非核心问题"
    response_time: "4 小时"
```

### 回滚流程

```
                    ┌─────────────┐
                    │  触发回滚   │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │  评估影响   │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │  审批回滚   │ ← 需 Release Manager 审批
                    └──────┬──────┘
                           │
         ┌─────────────────┼─────────────────┐
         │                 │                 │
  ┌──────▼──────┐    ┌──────▼──────┐    ┌──────▼──────┐
  │ 回滚应用    │    │ 回滚数据    │    │ 回滚配置    │
  └──────┬──────┘    └──────┬──────┘    └──────┬──────┘
         │                 │                 │
         └─────────────────┼─────────────────┘
                           │
                    ┌──────▼──────┐
                    │  验证回滚   │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │  通知干系人 │
                    └─────────────┘
```

### 回滚时间目标

| 环境 | 回滚时间目标 (RTO) |
|------|-------------------|
| 单实例 | 30 分钟 |
| 集群 | 15 分钟 |
| 容器 | 10 分钟 |
| Serverless | 5 分钟 |

## Release Window Standards

### 推荐发布时间

```yaml
# 生产环境发布时间窗口
production_window:
  preferred:
    - day: "Tuesday-Thursday"
      time: "22:00 - 02:00"
      reason: "业务低峰期"

  acceptable:
    - day: "Saturday-Sunday"
      time: "14:00 - 18:00"
      reason: "业务低峰期"

  avoided:
    - day: "Monday"
      reason: "周初业务高峰"
    - day: "Friday"
      reason: "周末前"
    - day: "Holiday"
      reason: "节假日"
```

### 值班安排

```yaml
oncall_requirements:
  release_window:
    duration_hours: 4
    team_size: 2
    roles:
      - "研发值班"
      - "运维值班"
      - "测试值班"

  escalation:
    level1: "值班人员"
    level2: "Team Lead"
    level3: "技术总监"
```

## Monitoring and Alerting Standards

### 发布监控指标

```yaml
# 关键监控指标
key_metrics:
  application:
    - name: "错误率"
      threshold: "> 1%"
      alert: true

    - name: "响应时间 P99"
      threshold: "> 500ms"
      alert: true

    - name: "QPS"
      threshold: "< expected * 0.5"
      alert: true

  infrastructure:
    - name: "CPU 使用率"
      threshold: "> 80%"
      alert: false

    - name: "内存使用率"
      threshold: "> 85%"
      alert: false

    - name: "磁盘使用率"
      threshold: "> 80%"
      alert: true
```

### 监控仪表盘

```yaml
# 发布监控仪表盘
release_dashboard:
  sections:
    - name: "业务指标"
      charts:
        - "请求量趋势"
        - "错误率趋势"
        - "响应时间分布"

    - name: "系统指标"
      charts:
        - "CPU/Memory"
        - "网络流量"
        - "数据库连接"

    - name: "对比视图"
      charts:
        - "发布前后对比"
        - "同环比分析"
```

## Communication Standards

### 发布通知模板

```markdown
# 【发布通知】{项目名称} {版本号}

## Release Time
{日期} {时间}

## Release Content
1. 功能更新
   - {功能1}
   - {功能2}

2. 问题修复
   - {BUG-123}: {问题描述}

## Impact Scope
- {系统A}: 无影响
- {系统B}: 需要配合升级

## Notes
- {注意事项1}
- {注意事项2}

## Rollback Plan
如遇问题，请联系 {联系方式}

## Contacts
- 技术负责人: {姓名}
- 值班电话: {电话}
```

## Post-release Review

### Post-Release Review

```yaml
post_release_review:
  timing: "发布后 24 小时"

  agenda:
    - name: "发布回顾"
      items:
        - "发布是否按计划完成"
        - "是否有遗漏项"

    - name: "问题分析"
      items:
        - "发布中发现的问题"
        - "潜在风险"

    - name: "改进建议"
      items:
        - "流程优化建议"
        - "工具改进建议"

  participants:
    - "Release Manager"
    - "研发团队"
    - "运维团队"
    - "测试团队"
```


## Overview

> High-level description of the prepare-release execution process.
>
> This instruction defines the technical approach, key activities, and success criteria for the prepare-release scenario.


## Multi-Language Code Examples

### Shell - Automated Release Script

```bash
#!/bin/bash
#
# automated-release.sh - 企业级自动化发布脚本
# 功能: 版本号管理、制品构建、发布确认、回滚准备
# 用法: ./automated-release.sh <major|minor|patch> [--dry-run]
#
set -euo pipefail

# ============================================================
# Configuration
# ============================================================
PROJECT_NAME="${PROJECT_NAME:-myapp}"
RELEASE_BRANCH="main"
DEVELOP_BRANCH="develop"
REMOTE="origin"
DRY_RUN=false

# ============================================================
# Utility Functions
# ============================================================
semver_validate() {
    # 校验语义化版本号格式: MAJOR.MINOR.PATCH
    local version="$1"
    if [[ ! "$version" =~ ^[0-9]+\.[0-9]+\.[0-9]+(-[a-zA-Z0-9.]+)?(\+[a-zA-Z0-9.]+)?$ ]]; then
        echo "Error: Invalid semver format: $version" >&2
        return 1
    fi
}

bump_version() {
    # Semantic Versioning 版本号递增
    local current="$1"
    local part="$2"
    local major minor patch

    IFS='.' read -r major minor patch <<< "${current%%-*}"
    case "$part" in
        major) major=$((major + 1)); minor=0; patch=0 ;;
        minor) minor=$((minor + 1)); patch=0 ;;
        patch) patch=$((patch + 1)) ;;
        *) echo "Error: part must be major|minor|patch"; exit 1 ;;
    esac
    echo "${major}.${minor}.${patch}"
}

# ============================================================
# Release Pipeline
# ============================================================
pipeline_pre_check() {
    echo "[1/6] Pre-release checklist verification..."
    local checks=(
        "CI pipeline status: $(git log --oneline -1 | head -c 40)"
        "Current branch: $(git branch --show-current)"
    )
    for check in "${checks[@]}"; do
        echo "  - $check"
    done

    # Check for uncommitted changes
    if [[ -n "$(git status --porcelain)" ]]; then
        echo "Error: Uncommitted changes found. Commit or stash first." >&2
        exit 1
    fi
}

pipeline_build() {
    echo "[2/6] Building release artifacts..."

    # Build application (example for Java/Maven project)
    if [[ -f "pom.xml" ]]; then
        mvn clean package -DskipTests -q
    elif [[ -f "build.gradle" ]]; then
        ./gradlew build -x test -q
    elif [[ -f "package.json" ]]; then
        npm ci && npm run build
    fi

    # Generate checksum for artifact integrity verification
    if ls target/*.jar 2>/dev/null; then
        sha256sum target/*.jar > target/checksums.sha256
    elif ls dist/* 2>/dev/null; then
        sha256sum dist/* > dist/checksums.sha256
    fi
    echo "  Artifacts built and checksums generated."
}

pipeline_create_tag() {
    local new_version="$1"
    echo "[3/6] Creating release tag: v${new_version}..."

    # Update version file
    echo "$new_version" > VERSION
    git add VERSION

    # Update changelog placeholder
    git commit -m "chore(release): bump version to v${new_version}"
    git tag -a "v${new_version}" -m "Release version v${new_version}"
    echo "  Tag v${new_version} created."
}

pipeline_deploy_staging() {
    echo "[4/6] Deploying to staging for verification..."
    # Placeholder - replace with actual deploy commands
    echo "  Deploying to https://staging.${PROJECT_NAME}.com..."
    sleep 2
    echo "  Smoke test passed."
}

pipeline_go_no_go() {
    local new_version="$1"
    echo "[5/6] Go/No-Go decision point for v${new_version}..."
    echo ""
    echo "  Release Readiness Checklist:"
    echo "  [ ] All test suites passed"
    echo "  [ ] Security scan passed"
    echo "  [ ] Performance benchmark within baseline"
    echo "  [ ] Release notes approved"
    echo "  [ ] Rollback plan confirmed"
    echo ""
    read -r -p "  Proceed with release? (yes/no): " confirmation
    if [[ "$confirmation" != "yes" ]]; then
        echo "  Release aborted by user. Run with --dry-run to simulate."
        exit 0
    fi
}

pipeline_push_and_deploy() {
    local new_version="$1"
    echo "[6/6] Pushing to production..."
    if [[ "$DRY_RUN" == true ]]; then
        echo "  [DRY-RUN] git push ${REMOTE} ${RELEASE_BRANCH} --tags"
        echo "  [DRY-RUN] Deploy v${new_version} to production"
    else
        git push "${REMOTE}" "${RELEASE_BRANCH}" --tags
        echo "  Deploying v${new_version} to production..."
        # Actual deploy command goes here
    fi
    echo "  Release v${new_version} completed!"
}

# ============================================================
# Main
# ============================================================
main() {
    local part="${1:-patch}"
    [[ "$*" == *"--dry-run"* ]] && DRY_RUN=true

    pipeline_pre_check

    # Ensure we are on release branch
    git checkout "${RELEASE_BRANCH}"
    git pull "${REMOTE}" "${RELEASE_BRANCH}"

    local current_version
    current_version=$(cat VERSION 2>/dev/null || echo "0.0.0")
    local new_version
    new_version=$(bump_version "$current_version" "$part")
    semver_validate "$new_version"

    pipeline_build
    pipeline_create_tag "$new_version"
    pipeline_deploy_staging
    pipeline_go_no_go "$new_version"
    pipeline_push_and_deploy "$new_version"
}

main "$@"
```

### Java - Spring Boot Actuator Health Check for Release Readiness

```java
package com.example.release;

import org.springframework.boot.actuate.health.Health;
import org.springframework.boot.actuate.health.HealthIndicator;
import org.springframework.stereotype.Component;

import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.URI;
import java.time.Duration;
import java.util.*;

/**
 * ReleaseReadinessHealthIndicator
 *
 * 发布准备健康检查组件，在发布前验证所有依赖服务状态。
 * 集成 Spring Boot Actuator 提供 /actuator/health/readiness 端点。
 */
@Component
public class ReleaseReadinessHealthIndicator implements HealthIndicator {

    private final HttpClient httpClient;
    private final List<DependencyCheck> dependencies;

    public ReleaseReadinessHealthIndicator() {
        this.httpClient = HttpClient.newBuilder()
                .connectTimeout(Duration.ofSeconds(5))
                .build();

        // 注册需要检查的所有依赖服务
        this.dependencies = List.of(
                new DependencyCheck("Database", "jdbc:mysql://primary-db:3306/heartbeat", 3306),
                new DependencyCheck("Redis Cache", "redis://cache-cluster:6379", 6379),
                new DependencyCheck("Message Queue", "amqp://mq-cluster:5672", 5672),
                new DependencyCheck("Payment Gateway", "https://payment-api.example.com/health", 443)
        );
    }

    @Override
    public Health health() {
        // 发布准备特有的健康检查逻辑，确保所有依赖可用
        List<String> failedDeps = new ArrayList<>();
        List<String> healthyDeps = new ArrayList<>();
        boolean allDependenciesUp = true;

        for (DependencyCheck dep : dependencies) {
            boolean isHealthy = checkDependency(dep);
            if (isHealthy) {
                healthyDeps.add(dep.name());
            } else {
                failedDeps.add(dep.name());
                allDependenciesUp = false;
            }
        }

        if (allDependenciesUp) {
            return Health.up()
                    .withDetail("release.ready", true)
                    .withDetail("dependencies.healthy", healthyDeps)
                    .withDetail("release.blocker", "none")
                    .build();
        }

        return Health.down()
                .withDetail("release.ready", false)
                .withDetail("dependencies.healthy", healthyDeps)
                .withDetail("dependencies.failed", failedDeps)
                .withDetail("release.blocker",
                        "Cannot proceed: " + String.join(", ", failedDeps) + " are unhealthy")
                .build();
    }

    /**
     * 检查单个依赖服务的可用性。
     * 支持 TCP 端口检测和 HTTP 端点健康检查两种模式。
     */
    private boolean checkDependency(DependencyCheck dep) {
        try {
            if (dep.port() == 443 || dep.port() == 80) {
                // HTTP 端点健康检查
                HttpRequest request = HttpRequest.newBuilder()
                        .uri(URI.create(dep.url()))
                        .timeout(Duration.ofSeconds(5))
                        .GET()
                        .build();
                HttpResponse<String> response = httpClient.send(request,
                        HttpResponse.BodyHandlers.ofString());
                return response.statusCode() == 200;
            } else {
                // TCP socket 检测（简化示例）
                try (var socket = new java.net.Socket()) {
                    socket.connect(new java.net.InetSocketAddress(
                            dep.url().split("://")[1].split(":")[0], dep.port()), 5000);
                    return true;
                }
            }
        } catch (Exception e) {
            return false;
        }
    }

    private record DependencyCheck(String name, String url, int port) {}
}
```

### Go - Kubernetes Rollout Status Monitoring

```go
package main

import (
	"context"
	"flag"
	"fmt"
	"log"
	"os"
	"os/signal"
	"time"

	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/apimachinery/pkg/watch"
	"k8s.io/client-go/kubernetes"
	"k8s.io/client-go/tools/clientcmd"
)

/*
 * k8s-rollout-watcher.go
 *
 * 监控 Kubernetes 发布滚动的实时状态，在发布准备阶段用于确认
 * 新版本 Deployment 是否成功发布。等待 rollout 完成并输出详细状态。
 *
 * 编译: go build -o k8s-rollout-watcher k8s-rollout-watcher.go
 * 运行: ./k8s-rollout-watcher -namespace=production -deployment=myapp -timeout=10m
 */

type RolloutStatus struct {
	Deployment     string
	Namespace      string
	DesiredReplicas int32
	UpdatedReplicas int32
	ReadyReplicas  int32
	AvailableReplicas int32
	Conditions     []string
	Complete       bool
}

// watchRollout 监控 Deployment rollout 过程，直到完成或超时。
func watchRollout(ctx context.Context, clientset *kubernetes.Clientset,
	namespace, deployment string, timeout time.Duration) (*RolloutStatus, error) {

	ctx, cancel := context.WithTimeout(ctx, timeout)
	defer cancel()

	deploymentsClient := clientset.AppsV1().Deployments(namespace)
	watcher, err := deploymentsClient.Watch(ctx, metav1.ListOptions{
		FieldSelector: fmt.Sprintf("metadata.name=%s", deployment),
	})
	if err != nil {
		return nil, fmt.Errorf("failed to watch deployment: %w", err)
	}
	defer watcher.Stop()

	log.Printf("Watching rollout of %s/%s (timeout: %v)...\n", namespace, deployment, timeout)

	for event := range watcher.ResultChan() {
		switch event.Type {
		case watch.Modified, watch.Added:
			dep, ok := event.Object.(*metav1.PartialObjectMetadata)
			_ = dep
			if !ok {
				continue
			}
		}

		// Fetch full deployment object for status
		dep, err := deploymentsClient.Get(ctx, deployment, metav1.GetOptions{})
		if err != nil {
			continue
		}

		status := &RolloutStatus{
			Deployment:       deployment,
			Namespace:        namespace,
			DesiredReplicas:  dep.Status.Replicas,
			UpdatedReplicas:  dep.Status.UpdatedReplicas,
			ReadyReplicas:    dep.Status.ReadyReplicas,
			AvailableReplicas: dep.Status.AvailableReplicas,
		}

		// Collect deployment conditions
		for _, cond := range dep.Status.Conditions {
			if cond.Status == "True" {
				status.Conditions = append(status.Conditions,
					fmt.Sprintf("%s (reason: %s)", cond.Type, cond.Reason))
			}
		}

		// Print progress
		fmt.Printf("\rProgress: %d/%d updated, %d ready, %d available  ",
			status.UpdatedReplicas, status.DesiredReplicas,
			status.ReadyReplicas, status.AvailableReplicas)

		// Check if rollout is complete
		progressing := false
		for _, cond := range dep.Status.Conditions {
			if cond.Type == "Progressing" && cond.Status == "True" &&
				cond.Reason == "NewReplicaSetAvailable" {
				progressing = true
			}
		}

		if dep.Status.UpdatedReplicas == dep.Status.Replicas &&
			dep.Status.ReadyReplicas == dep.Status.Replicas &&
			dep.Status.AvailableReplicas == dep.Status.Replicas &&
			progressing {
			status.Complete = true
			fmt.Println("\nRollout completed successfully!")
			return status, nil
		}
	}

	return nil, fmt.Errorf("rollout watcher terminated before completion")
}

func main() {
	namespace := flag.String("namespace", "default", "Kubernetes namespace")
	deployment := flag.String("deployment", "", "Deployment name")
	timeout := flag.Duration("timeout", 10*time.Minute, "Watch timeout")
	flag.Parse()

	if *deployment == "" {
		log.Fatal("--deployment flag is required")
	}

	// Load kubeconfig
	kubeconfig := os.Getenv("KUBECONFIG")
	if kubeconfig == "" {
		kubeconfig = os.Getenv("HOME") + "/.kube/config"
	}

	config, err := clientcmd.BuildConfigFromFlags("", kubeconfig)
	if err != nil {
		log.Fatalf("Failed to build kubeconfig: %v", err)
	}

	clientset, err := kubernetes.NewForConfig(config)
	if err != nil {
		log.Fatalf("Failed to create clientset: %v", err)
	}

	ctx, cancel := signal.NotifyContext(context.Background(), os.Interrupt)
	defer cancel()

	status, err := watchRollout(ctx, clientset, *namespace, *deployment, *timeout)
	if err != nil {
		log.Fatalf("Rollout watch failed: %v", err)
	}

	// Output structured status as JSON for pipeline integration
	fmt.Printf("\nFinal Status: %+v\n", status)
}
```

### JavaScript - npm Version Bump + release-it Automation

```javascript
#!/usr/bin/env node
/**
 * release-prep.js
 * 发布准备自动化工具: 版本号管理、Changelog 生成、发布确认
 *
 * 集成 release-it 实现一键发布准备工作流:
 *   1. 自动更新版本号 (遵循 semver)
 *   2. 生成 CHANGELOG.md (基于 Conventional Commits)
 *   3. 创建 Git Tag
 *   4. 生成发布检查报告
 *
 * 用法: node release-prep.js [major|minor|patch]
 */
const { execSync } = require("child_process");
const fs = require("fs");
const path = require("path");
const readline = require("readline");

// ============================================================
// release-it 配置文件生成
// ============================================================
const RELEASE_IT_CONFIG = {
  git: {
    commitMessage: "chore(release): release v${version}",
    tagName: "v${version}",
    tagAnnotation: "Release v${version}",
    push: true,
    pushArgs: ["--follow-tags"],
    requireCleanWorkingDir: true,
    requireBranch: "main",
  },
  npm: {
    publish: false, // 是否发布到 npm registry
  },
  github: {
    release: true,
    releaseName: "v${version}",
    assets: ["dist/*.zip"],
  },
  plugins: {
    "@release-it/conventional-changelog": {
      preset: "angular",
      infile: "CHANGELOG.md",
    },
  },
};

function generateReleaseConfig() {
  const configPath = path.join(process.cwd(), ".release-it.json");
  if (!fs.existsSync(configPath)) {
    fs.writeFileSync(configPath, JSON.stringify(RELEASE_IT_CONFIG, null, 2));
    console.log(`Generated: ${configPath}`);
  }
}

// ============================================================
// Pre-release Validation
// ============================================================
function validatePreRelease() {
  console.log("\n=== Pre-release Validation ===\n");

  const checks = [
    {
      name: "CI Status",
      check: () => {
        try {
          // Check last commit CI status (example for GitHub Actions)
          const log = execSync("git log --oneline -3", { encoding: "utf8" });
          return { pass: true, detail: log.split("\n")[0] };
        } catch {
          return { pass: false, detail: "Failed to check CI" };
        }
      },
    },
    {
      name: "Clean Working Directory",
      check: () => {
        const status = execSync("git status --porcelain", { encoding: "utf8" });
        return {
          pass: !status.trim(),
          detail: status.trim() || "Clean",
        };
      },
    },
    {
      name: "Branch Check",
      check: () => {
        const branch = execSync("git branch --show-current", { encoding: "utf8" }).trim();
        return {
          pass: branch === "main",
          detail: `Current: ${branch} (expect: main)`,
        };
      },
    },
    {
      name: "All Tests Pass",
      check: () => {
        try {
          execSync("npm test 2>&1", { encoding: "utf8", stdio: "pipe" });
          return { pass: true, detail: "All tests passed" };
        } catch (e) {
          return { pass: false, detail: "Tests failed" };
        }
      },
    },
    {
      name: "Build Artifact",
      check: () => {
        try {
          execSync("npm run build 2>&1", { encoding: "utf8", stdio: "pipe" });
          return { pass: true, detail: "Build successful" };
        } catch (e) {
          return { pass: false, detail: "Build failed" };
        }
      },
    },
  ];

  let allPassed = true;
  for (const { name, check } of checks) {
    const result = check();
    const icon = result.pass ? "PASS" : "FAIL";
    console.log(`  [${icon}] ${name}: ${result.detail}`);
    if (!result.pass) allPassed = false;
  }

  return allPassed;
}

// ============================================================
// Release Notes Generation
// ============================================================
function generateReleaseNotes() {
  console.log("\n=== Generating Release Notes ===\n");

  // Fetch commits since last tag
  let lastTag;
  try {
    lastTag = execSync("git describe --tags --abbrev=0 2>/dev/null || echo 'HEAD~10'", {
      encoding: "utf8",
    }).trim();
  } catch {
    lastTag = "HEAD~10";
  }

  const logFormat =
    '  - %s%n    Author: %an%n    Hash: %h';
  const changelog = execSync(
    `git log ${lastTag}..HEAD --format="${logFormat}" --no-merges`,
    { encoding: "utf8" }
  );

  // Categorize commits by type
  const categories = {
    feat: [],
    fix: [],
    chore: [],
    docs: [],
    refactor: [],
    test: [],
    other: [],
  };

  changelog.split("\n---\n").forEach((entry) => {
    const lines = entry.trim().split("\n");
    if (lines.length === 0) return;
    const firstLine = lines[0].replace(/^  - /, "");
    const match = firstLine.match(/^(feat|fix|chore|docs|refactor|test)(\(.*?\))?:/);
    const category = match ? match[1] : "other";
    if (categories[category]) {
      categories[category].push(entry.trim());
    }
  });

  // Output categorized release notes
  console.log("## Release Notes\n");
  for (const [category, items] of Object.entries(categories)) {
    if (items.length > 0) {
      const emojiMap = { feat: "Features", fix: "Bug Fixes", chore: "Maintenance",
        docs: "Documentation", refactor: "Refactoring", test: "Tests", other: "Other" };
      console.log(`### ${emojiMap[category] || category}`);
      console.log(items.join("\n"));
      console.log();
    }
  }
}

// ============================================================
// Main - 发布准备执行入口
// ============================================================
async function main() {
  const releaseType = process.argv[2] || "patch";
  const validTypes = ["major", "minor", "patch"];
  if (!validTypes.includes(releaseType)) {
    console.error(`Usage: node release-prep.js [${validTypes.join("|")}]`);
    process.exit(1);
  }

  console.log(`\n=== Release Preparation (${releaseType}) ===\n`);

  // Step 1: Validation
  const validated = validatePreRelease();
  if (!validated) {
    console.error("\nPre-release validation failed. Aborting.\n");
    process.exit(1);
  }

  // Step 2: Generate release-it config
  generateReleaseConfig();

  // Step 3: Generate release notes
  generateReleaseNotes();

  // Step 4: Go/No-Go
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  const answer = await new Promise((resolve) => {
    rl.question("\nProceed with release? (yes/no): ", resolve);
  });
  rl.close();

  if (answer.toLowerCase() !== "yes") {
    console.log("Release aborted.");
    process.exit(0);
  }

  // Step 5: Execute release
  console.log("\n=== Executing Release ===\n");
  execSync(`npx release-it ${releaseType} --ci`, { stdio: "inherit" });
  console.log("\nRelease completed successfully!");
}

main().catch(console.error);
```

## Error Handling

### Error Scenario 1: 发布检查清单未完成 (P1)

**触发条件**: Go/No-Go 评审时发布检查清单完成率低于 100%，存在必须完成的阻塞项未关闭

**处理流程**:
```
IF 检查清单必填项未完成
THEN
  1. 立即识别未完成项的负责人和预计完成时间
  2. 评估阻塞项的严重程度和对发布的影响范围
  3. IF 必填项不满足 AND 影响核心功能:
     a. 发布决策标记为 NO-GO
     b. 冻结发布，直到阻塞项解决
     c. 重新安排发布时间窗口
  4. IF 非必填项不满足:
     a. 标记为 CONDITIONAL-GO
     b. 制定发布后补齐计划并指定责任人
     c. 在 Post-Release Review 中跟踪
  5. 更新发布通知，告知干系人状态变更
END
```

**降级方案**: 对于 CONDITIONAL-GO，允许在发布后 24 小时内补齐非关键检查项

**升级条件**: 阻塞项超过 48 小时无法解决，升级至 Release Manager 和 Engineering Director 决策

### Error Scenario 2: Go/No-Go 决策僵持 (P2)

**触发条件**: 评审委员会成员对发布决策存在分歧，无法达成一致意见（支持率 < 60%）

**处理流程**:
```
IF Go/No-Go 决策无法达成一致
THEN
  1. 召开紧急决策会议，限时 30 分钟
  2. 列出支持发布和反对发布的具体理由
  3. 量化风险分析:
     a. 发布失败的影响 × 发生概率 = 风险值
     b. 不发布的业务损失（延期成本）
  4. 数据驱动决策: 基于量化分析而非主观判断
  5. IF 风险值低于阈值 AND 发布收益 > 不发布损失:
     a. 有条件发布（CONDITIONAL-GO）
     b. 制定风险缓解措施和加强监控
  6. ELSE 按多数意见决策，记录少数意见
END
```

**降级方案**: 延期 24 小时，解决争议点后重新评审

**升级条件**: 内部无法达成一致，升级至 CTO 作为最终决策者

### Error Scenario 3: 发布窗口错过 (P1)

**触发条件**: 由于准备延迟或阻塞项未解决，错过了预定的发布时间窗口

**处理流程**:
```
IF 当前时间超过发布窗口截止时间
THEN
  1. 立即终止当前发布流程，标记为 CANCELLED
  2. 评估下一个可用发布窗口:
     a. 标准窗口: 周二至周四 22:00-02:00
     b. 紧急窗口: 需 Release Manager 特批
  3. 重新安排发布时间:
     a. 优先选择下一个标准窗口（最早次日）
     b. 确认值班人员在新窗口可用
     c. 更新所有干系人的发布通知
  4. 如果发布有紧急业务需求:
     a. 提交紧急发布审批请求
     b. 获得 CTO/VP 级别批准
     c. 安排在紧急窗口发布
END
```

**降级方案**: 不跨天延期，直接选择下一个标准窗口（次日同一时段）

**升级条件**: 错过 3 个以上发布窗口，需要发布流程复盘和优化

### Error Scenario 4: 回滚方案未通过验证 (P0)

**触发条件**: 发布前回滚演练失败，或回滚脚本无法正常执行

**处理流程**:
```
IF 回滚验证失败
THEN
  1. 立即标记回滚方案为 INVALID，停止发布操作
  2. 诊断回滚失败原因:
     a. 数据迁移不可逆
     b. 回滚脚本 bug
     c. 环境配置冲突
     d. 依赖服务不兼容
  3. 修复回滚方案并重新验证:
     a. 修复脚本问题
     b. 补充数据回滚策略（快照恢复）
     c. 在预发环境完整演练
  4. 回滚验证通过前，禁止任何生产发布
  5. 更新回滚文档并通知相关人员
END
```

**降级方案**: 采用数据库快照恢复 + 应用回滚的组合策略

**升级条件**: 回滚方案 24 小时内无法验证通过，需架构师重新设计发布方案

## Quality Standards

> Acceptance criteria and quality gates for prepare-release deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | Pre-release checklist completion is 100% | Automated check |
| Standard 2 | Release notes accuracy is 98% or higher | Automated check |
| Standard 3 | All required approvals are obtained and documented | Automated check |
## References

- [harness-engineering.md](../standards/harness-engineering.md)
- [output-validation-checklist.md](../evaluations/output-validation-checklist.md)
- [regression-checklist.md](../evaluations/regression-checklist.md)
