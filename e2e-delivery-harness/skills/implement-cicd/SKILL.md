---
name: implement-cicd
description: "Domain skill for implement-cicd execution"
category: deployment
type: skill
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-23
status: active
language: "zh-CN"
tags: ['skill', 'knowledge']
---
# Skill: CI/CD 实施 (CI/CD Implementation)

## Overview

本 Skill 定义了 CI/CD 实施的核心知识体系。

## Core Knowledge

### 持续集成 (CI)

```python
class CICDPipeline:
    """CI/CD 流水线"""

    def __init__(self):
        self.stages = []

    def add_stage(self, name, jobs):
        """添加阶段"""
        self.stages.append({
            'name': name,
            'jobs': jobs
        })

    def execute(self):
        """执行流水线"""
        for stage in self.stages:
            self._run_stage(stage)

    def _run_stage(self, stage):
        """运行阶段"""
        results = []
        for job in stage['jobs']:
            result = self._run_job(job)
            results.append(result)
            if not result.success and job.critical:
                raise PipelineError(f"Stage {stage['name']} failed")
        return results


class BuildStrategy:
    """构建策略"""

    @staticmethod
    def incremental_build():
        """增量构建"""
        # 只构建变更的模块
        changed_files = git.get_changed_files()
        affected_modules = deps.resolve_affected(changed_files)
        return affected_modules

    @staticmethod
    def parallel_build():
        """并行构建"""
        # 利用多核并行构建
        with Pool(processes=cpu_count()) as pool:
            results = pool.map(build_module, modules)
        return results
```

### 持续交付 (CD)

```python
class DeploymentStrategy:
    """部署策略"""

    # 滚动更新
    def rolling_update(self, old_replicas, new_image):
        """滚动更新"""
        replicas = old_replicas.copy()
        for i in range(len(replicas)):
            # 逐步替换
            replicas[i] = self._deploy_new(new_image)
            self._verify_health(replicas[i])
        return replicas

    # 蓝绿部署
    def blue_green_deploy(self, version):
        """蓝绿部署"""
        # 部署新版本到绿色环境
        green = self._deploy_environment('green', version)

        # 验证
        self._verify_health(green)

        # 流量切换
        self._switch_traffic('blue', 'green')

        # 保持旧版本用于回滚
        self._keep_old_version('blue', 'blue_version')

    # 金丝雀部署
    def canary_deploy(self, version, percentages):
        """金丝雀部署"""
        canary = self._deploy_canary(version)

        for weight in percentages:
            # 调整流量权重
            self._adjust_weight(canary, weight)

            # 观察分析
            metrics = self._analyze_metrics(canary)
            if metrics.error_rate > threshold:
                self._rollback_canary()
                return False

            time.sleep(observe_duration)

        # 全量切换
        self._full_rollout(canary)
        return True
```

### GitOps 实践

```python
class GitOpsWorkflow:
    """GitOps 工作流"""

    def sync_application(self, app_name):
        """同步应用"""
        # 1. 拉取最新配置
        desired_state = self._fetch_desired_state(app_name)

        # 2. 获取当前状态
        current_state = self._get_current_state(app_name)

        # 3. 对比差异
        diff = self._compute_diff(current_state, desired_state)

        # 4. 应用变更
        if diff:
            self._apply_changes(diff)

        # 5. 等待同步
        self._wait_for_sync(app_name)

    def rollback(self, app_name, revision):
        """回滚到指定版本"""
        # 1. 更新 Git 仓库
        self._update_git_ref(revision)

        # 2. ArgoCD 自动同步
        self.argocd.sync(app_name)

        # 3. 等待完成
        self._wait_for_sync(app_name)
```

### 流水线优化

```python
class PipelineOptimizer:
    """流水线优化"""

    @staticmethod
    def parallel_execution(stages):
        """并行执行优化"""
        # 识别可并行的阶段
        parallel_stages = [
            stage for stage in stages
            if not stage.has_dependencies()
        ]

        # 并行执行
        with ThreadPoolExecutor() as executor:
            futures = [
                executor.submit(stage.execute)
                for stage in parallel_stages
            ]
            results = [f.result() for f in futures]

        return results

    @staticmethod
    def cache_strategy():
        """缓存策略"""
        # 依赖缓存
        dependencies_cache = {
            'key': hash(lockfile),
            'path': cache_dir
        }

        # 构建缓存
        build_cache = {
            'key': f"{code_hash}-{dep_hash}",
            'path': build_cache_dir
        }

        return dependencies_cache, build_cache

    @staticmethod
    def test_optimization():
        """测试优化"""
        # 增量测试
        changed_tests = self._get_changed_tests()

        # 分片执行
        shards = self._split_tests(changed_tests, parallel_jobs)

        # 缓存测试结果
        cached_results = self._get_cached_results(shards)
```

### 质量门禁

```python
class QualityGate:
    """质量门禁"""

    def __init__(self):
        self.gates = []

    def add_gate(self, name, criteria, action):
        self.gates.append({
            'name': name,
            'criteria': criteria,
            'action': action
        })

    def evaluate(self, build_result):
        """评估质量门禁"""
        for gate in self.gates:
            result = gate['criteria'](build_result)
            if not result:
                gate['action']()
                raise QualityGateFailed(gate['name'])

        return True

    # 常用门禁
    @staticmethod
    def coverage_gate(threshold=80):
        def check(result):
            return result.coverage >= threshold
        return check

    @staticmethod
    def security_gate():
        def check(result):
            return result.security_issues.high == 0
        return check

    @staticmethod
    def test_pass_gate():
        def check(result):
            return result.test_failures == 0
        return check
```

### Pipeline Configuration Examples

#### Java: GitHub Actions (Maven)

```yaml
# GitHub Actions workflow for Java/Maven project
# File: .github/workflows/java-ci.yml
name: Java CI/CD

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        java: [17, 21]

    steps:
      - uses: actions/checkout@v4

      - name: Set up JDK ${{ matrix.java }}
        uses: actions/setup-java@v4
        with:
          java-version: ${{ matrix.java }}
          distribution: 'temurin'
          cache: maven

      - name: Build & Test
        run: mvn clean verify -B

      - name: Upload Test Results
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: test-results-java${{ matrix.java }}
          path: target/surefire-reports/

      - name: Dependency Check (OWASP)
        run: mvn org.owasp:dependency-check-maven:check -B
```

#### Java: Jenkinsfile (Declarative Pipeline)

```groovy
// Jenkinsfile - Declarative Pipeline for Java/Gradle project
pipeline {
    agent any

    tools {
        jdk 'JDK21'
        gradle '8.5'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build & Unit Test') {
            parallel {
                stage('Compile') {
                    steps { sh 'gradle compileJava' }
                }
                stage('Unit Test') {
                    steps { sh 'gradle test' }
                }
            }
        }

        stage('Quality Gate') {
            steps {
                sh 'gradle sonar'
                sh 'gradle check'
            }
        }

        stage('Integration Test') {
            steps {
                sh 'gradle integrationTest'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'gradle jibDockerBuild'
            }
        }

        stage('Deploy to Staging') {
            when { branch 'develop' }
            steps {
                sh 'kubectl set image deployment/myapp app=myapp:${BUILD_NUMBER} -n staging'
            }
        }
    }

    post {
        always {
            junit 'build/reports/**/*.xml'
            archiveArtifacts artifacts: 'build/libs/*.jar'
        }
        failure {
            slackSend(color: '#FF0000', message: "Pipeline failed: ${env.BUILD_URL}")
        }
    }
}
```

#### Go: GitHub Actions + Goreleaser

```yaml
# GitHub Actions workflow for Go project with Goreleaser
# File: .github/workflows/go-ci.yml
name: Go CI/CD

on:
  push:
    tags: ['v*']
    branches: [main]
  pull_request:
    branches: [main]

permissions:
  contents: write

jobs:
  lint-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Go
        uses: actions/setup-go@v5
        with:
          go-version: '1.22'
          cache: true

      - name: Lint
        uses: golangci/golangci-lint-action@v4
        with:
          version: latest

      - name: Test
        run: go test -v -race -coverprofile=coverage.txt ./...

      - name: Upload coverage
        uses: codecov/codecov-action@v4
        with:
          file: ./coverage.txt

  release:
    needs: lint-test
    if: startsWith(github.ref, 'refs/tags/v')
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Go
        uses: actions/setup-go@v5
        with:
          go-version: '1.22'

      - name: Run Goreleaser
        uses: goreleaser/goreleaser-action@v5
        with:
          distribution: goreleaser
          version: latest
          args: release --clean
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

```yaml
# .goreleaser.yaml
version: 2
before:
  hooks:
    - go mod tidy

builds:
  - env:
      - CGO_ENABLED=0
    goos:
      - linux
      - darwin
      - windows
    goarch:
      - amd64
      - arm64
    ldflags:
      - -s -w -X main.version={{.Version}}

archives:
  - format: tar.gz
    name_template: >-
      {{ .ProjectName }}_
      {{- title .Os }}_
      {{- if eq .Arch "amd64" }}x86_64
      {{- else }}{{ .Arch }}{{ end }}
    files:
      - README.md
      - LICENSE

dockers:
  - image_templates:
      - "ghcr.io/myorg/{{ .ProjectName }}:{{ .Version }}"
      - "ghcr.io/myorg/{{ .ProjectName }}:latest"
    use: buildx
    build_flag_templates:
      - "--platform=linux/amd64"

checksum:
  name_template: 'checksums.txt'

changelog:
  sort: asc
  filters:
    exclude:
      - '^docs:'
      - '^test:'
```

#### Node.js: GitHub Actions (npm/yarn)

```yaml
# GitHub Actions workflow for Node.js project
# File: .github/workflows/node-ci.yml
name: Node.js CI/CD

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [18, 20, 22]

    steps:
      - uses: actions/checkout@v4

      - name: Use Node.js ${{ matrix.node-version }}
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Lint
        run: npm run lint

      - name: Run tests with coverage
        run: npm run test:coverage

      - name: Upload coverage
        uses: codecov/codecov-action@v4
        with:
          flags: node-v${{ matrix.node-version }}

      - name: Build
        run: npm run build

      - name: Audit dependencies
        run: npm audit --audit-level=high

  docker-build:
    needs: build
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Login to GitHub Container Registry
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Build & Push Docker image
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: ghcr.io/myorg/myapp:latest,ghcr.io/myorg/myapp:${{ github.sha }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
```

#### Docker Multi-stage Build (Node.js)

```dockerfile
# Dockerfile - Multi-stage build for Node.js application
# Stage 1: Build
FROM node:20-alpine AS builder
WORKDIR /app

COPY package*.json ./
RUN npm ci --only=production

COPY . .
RUN npm run build

# Stage 2: Production image
FROM node:20-alpine
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./

USER appuser
EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD wget --no-verbose --tries=1 --spider http://localhost:3000/health || exit 1

CMD ["node", "dist/main.js"]
```

## Toolchain

### CI/CD 工具

| 类别 | 工具 |
|------|------|
| CI 服务 | GitHub Actions, GitLab CI, Jenkins |
| 构建 | Maven, Gradle, npm, yarn |
| 容器 | Docker, Buildah |
| 编排 | Kubernetes, Docker Swarm |
| GitOps | ArgoCD, Flux |
| 监控 | Prometheus, Grafana |

### 部署工具

| 工具 | 用途 |
|------|------|
| Helm | Kubernetes 应用管理 |
| Kustomize | Kubernetes 配置管理 |
| Terraform | 基础设施管理 |
| Ansible | 配置管理 |

## Associated Assets

- **Scenario**: `../../scenarios/implement-cicd/SCENARIO.md`
- **Instruction**: `../../instructions/implement-cicd.instructions.md`
- **Prompt**: `../../prompts/implement-cicd.prompt.md`
- **Agent**: `../../agents/implement-cicd.agent.md`


## Core Knowledge

> Essential knowledge domain for implement-cicd execution.

### Domain Fundamentals
- **持续集成 vs 持续交付 vs 持续部署**: CI 强调频繁集成并自动构建测试，CD 确保代码随时可发布到生产，持续部署是 CD 的自动化延伸。
- **Pipeline as Code**: 将流水线配置以代码形式管理（如 Jenkinsfile、GitHub Actions YAML），纳入版本控制，确保可追溯和可复现。
- **DORA 指标**: 四项核心指标衡量 DevOps 效能——部署频率、变更前置时间、变更失败率、故障恢复时间，指导持续改进。

### Key Principles
1. **主干开发 (Trunk-Based Development)**: 所有开发者向主干分支提交小批量变更，分支生命周期不超过一天，减少合并冲突和集成风险。
2. **构建一次部署多处**: 从 CI 产出的制品唯一且不可变，同一制品依次部署到开发、测试、预发布、生产环境，消除环境差异问题。
3. **失败快速反馈**: 流水线前置阶段（编译、单元测试）优先执行，失败立即阻断并通知提交者，缩短问题发现到修复的周期。


## Best Practices

> Proven practices for implement-cicd excellence.

1. **流水线阶段化**: 流水线按阶段组织（构建 -> 单元测试 -> 集成测试 -> 安全扫描 -> 部署），前序阶段失败则阻断后续执行，确保质量左移。
2. **并行化测试**: 将测试任务分片(Split)后并行执行，设立合理的分片粒度，显著缩短流水线执行时间。
3. **制品不可变**: 每个构建产出的制品包含唯一版本号并存储至制品仓库，一旦发布即不可修改，确保部署的可复现和可追溯。


## Anti-patterns (反模式)

> 与 Common Pitfalls 同义，执行时合并检查。

## Common Pitfalls

> Frequent mistakes to avoid during implement-cicd execution.

### Pitfall 1: 流水线配置过度复杂 (Over-Complicated Pipeline)
**Risk**: 流水线配置包含大量条件判断、动态步骤和脚本逻辑，难以维护和调试，故障频发。
**Prevention**: 遵循 KISS 原则，将复杂逻辑抽取为独立的脚本或工具，流水线仅编排而非实现业务逻辑。
**Impact**: 流水线本身频繁故障，成为交付瓶颈，开发人员信心下降，绕开流水线直接部署。

### Pitfall 2: 测试环境与生产环境不一致 (Environment Drift)
**Risk**: 测试环境和生产环境在 OS、依赖库、配置参数等方面存在差异，测试环境通过的变更到生产环境出现问题。
**Prevention**: 使用容器化技术和基础设施即代码(IaC)确保环境一致性，定期进行环境同步审计。
**Impact**: 生产环境出现测试环境未发现的故障，部署风险增加，变更加速受阻。

### Pitfall 3: 忽视流水线自身的版本管理 (Pipeline Version Neglect)
**Risk**: 流水线配置变更没有经过评审和测试，直接修改主分支配置导致流水线中断。
**Prevention**: 将流水线配置纳入版本控制，修改走 PR 评审流程，使用分支策略隔离变更影响。
**Impact**: 流水线突然中断，所有开发团队无法构建和部署，形成组织级的交付阻塞。
