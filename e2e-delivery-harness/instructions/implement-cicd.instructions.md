---
name: implement-cicd
description: "Detailed technical instructions for implement-cicd scenario execution"
applyTo: "scenarios/implement-cicd/**"
phase: deployment
type: instruction
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
language: "zh-CN"
tags: ['instruction', 'technical']
---
# Instructions: CI/CD 实施 (Implement CI/CD)

## CI/CD 平台选型

### 主流平台对比

| 平台 | 特点 | 适用场景 |
|------|------|----------|
| GitHub Actions | 集成度高、免费额度大 | GitHub 项目 |
| GitLab CI | 完整的 DevOps 平台 | GitLab 项目 |
| Jenkins | 插件丰富、高度可定制 | 企业项目 |
| ArgoCD | GitOps 原生、Kubernetes | K8s 部署 |
| Spinnaker | 多云支持、复杂部署 | 大型企业 |

### GitHub Actions 规范

```yaml
# 基础结构
workflow_structure:
  name: "工作流名称"
  on: "触发条件"
  jobs:
    job_id:
      runs-on: "运行环境"
      steps:
        - uses: "复用 Actions"
        - run: "执行命令"
```

### GitLab CI 规范

```yaml
# 基础结构
stages:
  - build
  - test
  - deploy

variables:
  IMAGE_TAG: $CI_COMMIT_SHORT_SHA

build:
  stage: build
  script:
    - docker build -t app:$IMAGE_TAG .
```

## Pipeline Design Standards

### 流水线阶段

```
┌─────────────────────────────────────────────────────────────┐
│                    CI/CD PIPELINE STAGES                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐    │
│  │  BUILD  │ → │  TEST   │ → │  SCAN   │ → │ DEPLOY  │    │
│  └─────────┘   └─────────┘   └─────────┘   └─────────┘    │
│       ↓             ↓             ↓             ↓           │
│   代码编译      单元测试      安全扫描      部署环境        │
│   依赖安装      集成测试      代码检查      验证测试        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 阶段定义

```yaml
pipeline_stages:
  build:
    purpose: "构建产物"
    jobs:
      - compile
      - package
      - build_image

  test:
    purpose: "质量验证"
    jobs:
      - unit_test
      - integration_test
      - e2e_test
      - coverage

  security:
    purpose: "安全扫描"
    jobs:
      - dependency_scan
      - code_scan
      - image_scan

  deploy:
    purpose: "部署发布"
    jobs:
      - deploy_dev
      - deploy_staging
      - deploy_prod
```

## Build Configuration Standards

### Docker 构建优化

```dockerfile
# 多阶段构建
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
RUN npm run build

FROM node:18-alpine AS runner
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
EXPOSE 3000
CMD ["node", "dist/index.js"]

# 构建优化
# 1. 使用 .dockerignore
# 2. 利用构建缓存
# 3. 多阶段构建减小镜像
```

### 构建缓存配置

```yaml
# GitHub Actions 缓存
- uses: actions/cache@v3
  with:
    path: |
      ~/.npm
      ~/.m2
      ~/.gradle
    key: ${{ runner.os }}-build-${{ hashFiles('**/package-lock.json') }}

# GitLab CI 缓存
cache:
  key: ${CI_COMMIT_REF_SLUG}
  paths:
    - node_modules/
    - .gradle/
```

## Test Configuration Standards

### 测试金字塔

```yaml
test_strategy:
  unit_test:
    coverage_target: "≥ 80%"
    execution: "每次提交"
    parallel: true

  integration_test:
    coverage_target: "核心路径"
    execution: "每次 PR"
    dependencies: ["数据库", "缓存"]

  e2e_test:
    coverage_target: "关键用户路径"
    execution: "每日构建"
    environment: "测试环境"
```

### Test Report配置

```yaml
# JUnit XML 报告
test_reports:
  format: "JUnit XML"
  paths:
    - "**/test-results/*.xml"
    - "**/reports/junit/*.xml"

# 覆盖率报告
coverage_reports:
  format: ["Cobertura", "JaCoCo"]
  thresholds:
    line: 80
    branch: 70
```

## Deployment Strategy Standards

### 部署类型对比

| 策略 | 特点 | 适用场景 |
|------|------|----------|
| 蓝绿部署 | 两套环境，快速切换 | 有状态服务 |
| 金丝雀部署 | 渐进式放量 | 重大变更 |
| 滚动更新 | 逐步替换 | 无状态服务 |
| 功能开关 | 代码即上线 | A/B 测试 |

### 蓝绿部署

```yaml
# Kubernetes 蓝绿部署
blue_green:
  blue:
    replicas: 3
    label: "version: blue"
    traffic_weight: 100

  green:
    replicas: 3
    label: "version: green"
    traffic_weight: 0

  switch:
    method: "Service Selector 切换"
    duration: "秒级"

  rollback:
    method: "Selector 切回"
    duration: "秒级"
```

### 金丝雀部署

```yaml
# Argo Rollouts 金丝雀
canary:
  steps:
    - setWeight: 5      # 5% 流量
    - pause: {}         # 等待人工审批
    - setWeight: 20     # 20% 流量
    - pause: {duration: 10}
    - setWeight: 50     # 50% 流量
    - pause: {duration: 10}
    - setWeight: 100    # 100% 流量

  analysis:
    success_delay: 5m
    failure_threshold: 3
    templates:
      - templateName: "success-rate"
      - templateName: "latency"
```

## Security Configuration Standards

### 密钥管理

```yaml
# 不提交密钥
secret_management:
  tools:
    - "GitHub Secrets"
    - "GitLab CI Variables"
    - "Vault"
    - "AWS Secrets Manager"

  practices:
    - "永远不提交密钥到代码"
    - "使用环境变量注入"
    - "定期轮换密钥"
    - "最小权限原则"
```

### 安全扫描配置

```yaml
security_scans:
  dependency_scan:
    tool: "Snyk / Dependabot"
    frequency: "daily"
    action: "auto_fix"

  code_scan:
    tool: "SonarQube"
    quality_gate: "PASS"
    blocker_issues: 0

  image_scan:
    tool: "Trivy / Clair"
    severity: "HIGH/CRITICAL"
    action: "block_deploy"
```

## Monitoring and Alerting Standards

### 流水线监控

```yaml
pipeline_monitoring:
  metrics:
    - name: "pipeline_duration"
      labels: ["stage", "branch"]

    - name: "pipeline_success_rate"
      labels: ["repository"]

    - name: "deployment_frequency"
      labels: ["environment"]

    - name: "lead_time"
      labels: ["repository"]

  alerts:
    - name: "pipeline_failed"
      condition: "status == 'failed'"
      channel: "slack"

    - name: "deployment_failed"
      condition: "status == 'failed'"
      channel: "pagerduty"
```

## GitOps 规范

### ArgoCD 配置

```yaml
# Application 定义
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: myapp
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/org/repo
    targetRevision: HEAD
    path: k8s/overlays/prod
  destination:
    server: https://kubernetes.default.svc
    namespace: myapp
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
      - CreateNamespace=true
```

### GitOps 流程

```
┌──────────────────────────────────────────────────────────────┐
│                      GITOPS FLOW                            │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  Developer → Git → CI Pipeline → Container Registry        │
│                                    ↓                         │
│                              Git Repository                   │
│                                    ↓                         │
│                              ArgoCD                          │
│                                    ↓                         │
│                              Kubernetes                      │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```


## Overview

> High-level description of the implement-cicd execution process.
>
> This instruction defines the technical approach, key activities, and success criteria for the implement-cicd scenario.


## Technical Specifications

> Detailed technical requirements and implementation guidelines for implement-cicd.

### Required Tools
- **GitHub Actions / GitLab CI / Jenkins**: CI/CD 流水线引擎
- **Docker / BuildKit / Kaniko**: 容器镜像构建
- **Helm / Kustomize**: Kubernetes 部署编排
- **ArgoCD / Flux**: GitOps 持续交付
- **SonarQube / CodeClimate**: 代码质量门禁
- **Trivy / Grype / Snyk**: 容器镜像安全扫描

### Environment Requirements
- CI Runner 可访问源代码仓库（GitHub / GitLab / Bitbucket）
- 镜像仓库已配置且可推送（Docker Hub / Harbor / ECR / ACR）
- 目标 Kubernetes 集群可达（kubectl context 已配置）
- Secrets 已注入 CI 环境（不要硬编码，使用 GitHub Secrets / Vault）

### Configuration Parameters
- `CI_TRIGGER`: 触发条件（push to main → deploy-staging, tag v* → deploy-prod）
- `BUILD_TIMEOUT`: 构建超时时间（默认 30min，大型 Monorepo 可延长至 60min）
- `PARALLEL_JOBS`: 并行 Job 数量上限（≤ Runner 资源限制）
- `ARTIFACT_RETENTION`: 构建产物保留天数（≥30 天）
- `ENVIRONMENT_PROTECTION`: 生产环境部署是否需要人工审批（must be true）


## Multi-Language Code Examples

This section provides production-grade CI/CD pipeline configurations across five major platforms and languages, covering build, test, security scan, artifact publishing, and deployment stages.

### GitHub Actions (YAML)

```yaml
# .github/workflows/ci-cd.yml
# Full multi-stage CI/CD workflow: build, test, security scan, image push, and deploy.
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]
  release:
    types: [published]

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}
  NODE_VERSION: "20"

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

jobs:
  # ──────────────────────────── BUILD ────────────────────────────
  build:
    name: Build and Test
    runs-on: ubuntu-latest
    timeout-minutes: 15
    outputs:
      version: ${{ steps.version.outputs.version }}

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: "npm"

      - name: Install dependencies
        run: npm ci --frozen-lockfile

      - name: Lint code
        run: npm run lint

      - name: Run unit tests with coverage
        run: npm run test:coverage

      - name: Upload coverage report
        uses: actions/upload-artifact@v4
        with:
          name: coverage-report
          path: coverage/

      - name: Build project
        run: npm run build

      - name: Determine version
        id: version
        run: |
          if [[ "${{ github.event_name }}" == "release" ]]; then
            echo "version=${{ github.event.release.tag_name }}" >> "$GITHUB_OUTPUT"
          else
            echo "version=$(node -p "require('./package.json').version")-$(git rev-parse --short HEAD)" >> "$GITHUB_OUTPUT"
          fi

      - name: Upload build artifacts
        uses: actions/upload-artifact@v4
        with:
          name: build-output
          path: dist/

  # ──────────────────────────── SECURITY SCAN ────────────────────
  security-scan:
    name: Security Scan
    runs-on: ubuntu-latest
    needs: [build]
    timeout-minutes: 10

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Run Trivy vulnerability scanner on filesystem
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: "fs"
          scan-ref: "."
          format: "sarif"
          output: "trivy-results.sarif"
          severity: "HIGH,CRITICAL"
          exit-code: 1

      - name: Upload Trivy results to GitHub Security tab
        uses: github/codeql-action/upload-sarif@v3
        with:
          sarif_file: "trivy-results.sarif"

      - name: Run CodeQL analysis
        uses: github/codeql-action/init@v3
        with:
          languages: javascript

      - name: Perform CodeQL analysis
        uses: github/codeql-action/analyze@v3

  # ──────────────────────────── DOCKER BUILD & PUSH ─────────────
  docker:
    name: Build and Push Docker Image
    runs-on: ubuntu-latest
    needs: [security-scan]
    if: github.event_name != 'pull_request'
    timeout-minutes: 10
    permissions:
      contents: read
      packages: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Log in to Container Registry
        uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Extract Docker metadata
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          tags: |
            type=semver,pattern={{version}}
            type=sha,prefix={{branch}}-
            type=ref,event=branch

      - name: Build and push Docker image
        uses: docker/build-push-action@v5
        with:
          context: .
          file: ./Dockerfile
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max

  # ──────────────────────────── DEPLOY ──────────────────────────
  deploy:
    name: Deploy to Production
    runs-on: ubuntu-latest
    needs: [docker]
    if: github.event_name == 'release'
    timeout-minutes: 20
    environment: production

    steps:
      - name: Checkout deployment manifests
        uses: actions/checkout@v4

      - name: Configure kubectl
        uses: azure/setup-kubectl@v4
        with:
          version: "latest"

      - name: Set Kubernetes context
        run: |
          echo "${{ secrets.KUBE_CONFIG }}" | base64 -d > kubeconfig.yaml
          export KUBECONFIG=kubeconfig.yaml

      - name: Deploy to Kubernetes
        run: |
          kubectl set image deployment/myapp \
            myapp=${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ needs.build.outputs.version }} \
            --record

      - name: Verify deployment rollout
        run: |
          kubectl rollout status deployment/myapp --timeout=300s

      - name: Run post-deployment smoke tests
        run: |
          curl --fail --retry 3 https://api.ecommerce.example.com/health
```

### GitLab CI (YAML)

```yaml
# .gitlab-ci.yml
# Full GitLab CI pipeline with multi-stage build, test, security scanning, and deployment.

stages:
  - lint
  - build
  - test
  - security
  - package
  - deploy

variables:
  DOCKER_DRIVER: overlay2
  DOCKER_TLS_CERTDIR: ""
  IMAGE_TAG: $CI_COMMIT_SHORT_SHA
  IMAGE_FULL: $CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA

# ─── Global cache ───
cache:
  key: ${CI_COMMIT_REF_SLUG}
  paths:
    - node_modules/
    - .npm/

# ─── Lint ───
lint:
  stage: lint
  image: node:20-alpine
  script:
    - npm ci --frozen-lockfile
    - npm run lint
  only:
    - merge_requests
    - main

# ─── Build ───
build:
  stage: build
  image: node:20-alpine
  script:
    - npm ci --frozen-lockfile
    - npm run build
  artifacts:
    paths:
      - dist/
    expire_in: 1 hour
  only:
    - main
    - tags

# ─── Test ───
test:
  stage: test
  image: node:20-alpine
  script:
    - npm ci --frozen-lockfile
    - npm run test:coverage
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage/cobertura-coverage.xml
    paths:
      - coverage/
  coverage: '/All files[^|]*\|[^|]*\s+([\d\.]+)/'
  only:
    - merge_requests
    - main

integration-test:
  stage: test
  image: node:20-alpine
  services:
    - name: postgres:16-alpine
      alias: postgres
      variables:
        POSTGRES_DB: test
        POSTGRES_USER: test
        POSTGRES_PASSWORD: test
    - name: redis:7-alpine
      alias: redis
  script:
    - npm ci --frozen-lockfile
    - npm run test:integration
  variables:
    DATABASE_URL: "postgresql://test:test@postgres:5432/test"
    REDIS_URL: "redis://redis:6379"
  only:
    - main

# ─── Security Scan ───
security-scan:
  stage: security
  image: node:20-alpine
  script:
    - npm ci --frozen-lockfile
    - npm audit --audit-level=high
  allow_failure: true
  only:
    - main

dependency-scan:
  stage: security
  image:
    name: aquasec/trivy:latest
    entrypoint: [""]
  script:
    - trivy fs --exit-code 1 --severity HIGH,CRITICAL --no-progress .
  only:
    - main

# ─── Package ───
docker-build:
  stage: package
  image: docker:latest
  services:
    - docker:dind
  script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
    - docker build -t $IMAGE_FULL .
    - docker push $IMAGE_FULL
  only:
    - tags

# ─── Deploy ───
.deploy-template: &deploy-template
  stage: deploy
  image: alpine/k8s:latest
  script:
    - apk add --no-cache curl
    - kubectl config use-context $KUBE_CONTEXT
    - kubectl set image deployment/myapp myapp=$IMAGE_FULL
    - kubectl rollout status deployment/myapp --timeout=300s
    - curl --fail --retry 3 $HEALTH_ENDPOINT

deploy-staging:
  <<: *deploy-template
  variables:
    KUBE_CONTEXT: staging
    HEALTH_ENDPOINT: "https://staging.ecommerce.example.com/health"
  only:
    - main
  environment:
    name: staging

deploy-production:
  <<: *deploy-template
  variables:
    KUBE_CONTEXT: production
    HEALTH_ENDPOINT: "https://api.ecommerce.example.com/health"
  only:
    - tags
  environment:
    name: production
  when: manual
```

### Java / Maven + Jenkins Declarative Pipeline

```groovy
// Jenkinsfile
// Declarative Jenkins pipeline for Java/Maven projects with
// parallel stages, artifact archiving, security scanning, and deployment.

pipeline {
    agent {
        kubernetes {
            label 'maven-pod'
            defaultContainer 'jnlp'
            yaml '''
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: maven
    image: maven:3.9-eclipse-temurin-21
    command: ["cat"]
    tty: true
  - name: docker
    image: docker:24
    command: ["cat"]
    tty: true
    volumeMounts:
    - name: docker-sock
      mountPath: /var/run/docker.sock
  volumes:
  - name: docker-sock
    hostPath:
      path: /var/run/docker.sock
'''
        }
    }

    environment {
        REGISTRY = 'ghcr.io'
        IMAGE_NAME = "${REGISTRY}/${JENKINS_GITHUB_ORG}/myapp"
        SONAR_HOST_URL = 'https://sonarqube.example.com'
    }

    options {
        timeout(time: 30, unit: 'MINUTES')
        buildDiscarder(logRotator(numToKeepStr: '10'))
        ansiColor('xterm')
        disableConcurrentBuilds()
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
                    steps {
                        container('maven') {
                            sh 'mvn clean compile -DskipTests'
                        }
                    }
                }
                stage('Unit Test') {
                    steps {
                        container('maven') {
                            sh 'mvn test'
                        }
                    }
                    post {
                        always {
                            junit 'target/surefire-reports/*.xml'
                        }
                    }
                }
                stage('Lint') {
                    steps {
                        container('maven') {
                            sh 'mvn checkstyle:checkstyle pmd:pmd'
                        }
                    }
                    post {
                        always {
                            checkstyle pattern: 'target/checkstyle-result.xml'
                            pmd pattern: 'target/pmd.xml'
                        }
                    }
                }
            }
        }

        stage('Integration Test') {
            steps {
                container('maven') {
                    sh 'mvn verify -Pintegration-test'
                }
            }
            post {
                always {
                    junit 'target/failsafe-reports/*.xml'
                }
            }
        }

        stage('Quality Gate') {
            steps {
                container('maven') {
                    withSonarQubeEnv('SonarQube') {
                        sh 'mvn sonar:sonar -Dsonar.host.url=${SONAR_HOST_URL}'
                    }
                }
                // Wait for SonarQube quality gate result
                timeout(time: 5, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }

        stage('Security Scan') {
            steps {
                container('docker') {
                    sh 'docker run --rm -v $PWD:/app aquasec/trivy fs --exit-code 1 --severity HIGH,CRITICAL /app'
                }
            }
        }

        stage('Package & Publish') {
            when {
                branch 'main'
            }
            steps {
                container('maven') {
                    sh 'mvn package -DskipTests'
                    sh """
                        mvn deploy \
                          -DaltDeploymentRepository=github::default::https://maven.pkg.github.com/${JENKINS_GITHUB_ORG}/myapp \
                          -Dregistry=https://maven.pkg.github.com \
                          -Dtoken=${GITHUB_TOKEN}
                    """
                }
                container('docker') {
                    sh """
                        docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} .
                        docker push ${IMAGE_NAME}:${BUILD_NUMBER}
                    """
                }
            }
        }
    }

    post {
        failure {
            emailext(
                subject: "Pipeline FAILED: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: "Pipeline failed. Check ${env.BUILD_URL} for details.",
                to: 'team@ecommerce.example.com'
            )
        }
        always {
            archiveArtifacts artifacts: 'target/*.jar', fingerprint: true
            cleanWs()
        }
    }
}
```

### Go Release with GoReleaser

```yaml
# .goreleaser.yaml
# GoReleaser configuration for multi-platform binary releases,
# Homebrew formula publishing, and Docker image distribution.

version: 2

project_name: platform-cli

before:
  hooks:
    - go mod tidy
    - go generate ./...

builds:
  - id: platform-cli
    main: ./cmd/platform
    binary: platform
    ldflags:
      - -s -w
      - -X main.version={{.Version}}
      - -X main.commit={{.Commit}}
      - -X main.date={{.Date}}
    env:
      - CGO_ENABLED=0
    goos:
      - linux
      - darwin
      - windows
    goarch:
      - amd64
      - arm64
    ignore:
      - goos: windows
        goarch: arm64
    mod_timestamp: "{{ .CommitTimestamp }}"

archives:
  - id: binary
    formats: [tar.gz]
    name_template: >-
      {{ .ProjectName }}_{{ .Version }}_
      {{- if eq .Os "darwin" }}macOS
      {{- else }}{{ .Os }}{{ end }}_
      {{- if eq .Arch "amd64" }}x86_64
      {{- else }}{{ .Arch }}{{ end }}
    files:
      - LICENSE
      - README.md
    format_overrides:
      - goos: windows
        formats: [zip]

checksum:
  name_template: "checksums.txt"
  algorithm: sha256

snapshot:
  name_template: "{{ .Version }}-SNAPSHOT-{{ .ShortCommit }}"

changelog:
  sort: asc
  filters:
    exclude:
      - "^docs:"
      - "^test:"
      - "^ci:"
      - Merge pull request
      - Merge branch

# ─── Homebrew Formula ───
brews:
  - name: platform-cli
    repository:
      owner: ecommerce-org
      name: homebrew-tap
    homepage: "https://github.com/ecommerce-org/platform-cli"
    description: "CLI tool for E-Commerce Platform operations"
    license: "Apache-2.0"
    install: |
      bin.install "platform"

# ─── Docker Images ───
dockers:
  - image_templates:
      - "ghcr.io/ecommerce-org/platform-cli:{{ .Version }}"
      - "ghcr.io/ecommerce-org/platform-cli:latest"
    dockerfile: Dockerfile.goreleaser
    build_flag_templates:
      - "--pull"
      - "--label=org.opencontainers.image.created={{.Date}}"
      - "--label=org.opencontainers.image.title={{.ProjectName}}"
      - "--label=org.opencontainers.image.revision={{.FullCommit}}"
      - "--label=org.opencontainers.image.version={{.Version}}"

# ─── SBOM ───
sboms:
  - artifacts: archive
  - artifacts: binary

# ─── Release ───
release:
  github:
    owner: ecommerce-org
    name: platform-cli
  draft: true
  replace_existing_draft: true

# ─── Announce ───
announce:
  slack:
    enabled: true
    message_template: "New release: {{ .ProjectName }} {{ .Version }} is available!"
    channel: "#releases"
```

### JavaScript / npm Publish Workflow

```yaml
# .github/workflows/npm-publish.yml
# GitHub Actions workflow for automated npm package publishing
# with package verification, provenance, and release management.

name: Publish npm Package

on:
  release:
    types: [published]
  workflow_dispatch:
    inputs:
      dist-tag:
        description: "npm dist-tag (latest, next, beta)"
        required: true
        default: "latest"
        type: choice
        options:
          - latest
          - next
          - beta

env:
  NODE_VERSION: "20"

jobs:
  # ─── Verify Package ───
  verify:
    name: Verify Package Integrity
    runs-on: ubuntu-latest
    timeout-minutes: 10

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          registry-url: "https://registry.npmjs.org"
          cache: "npm"

      - run: npm ci --frozen-lockfile

      - name: Lint package
        run: npm run lint

      - name: Run tests
        run: npm run test:coverage

      - name: Build package
        run: npm run build

      - name: Check package size
        run: |
          PKG_SIZE=$(du -sk dist/ | cut -f1)
          echo "Package size: ${PKG_SIZE}KB"
          if [ "$PKG_SIZE" -gt 10240 ]; then
            echo "❌ Package exceeds 10MB limit"
            exit 1
          fi

      - name: Verify package exports
        run: node -e "const pkg = require('./package.json'); Object.keys(pkg.exports || {}).forEach(e => console.log('export:', e))"

  # ─── Publish ───
  publish:
    name: Publish to npm
    runs-on: ubuntu-latest
    needs: [verify]
    timeout-minutes: 10
    permissions:
      contents: read
      id-token: write  # Required for npm provenance

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          registry-url: "https://registry.npmjs.org"

      - run: npm ci --frozen-lockfile
      - run: npm run build

      - name: Determine dist-tag
        id: tag
        run: |
          if [[ "${{ github.event_name }}" == "release" ]]; then
            # Detect pre-release from tag name
            if [[ "${{ github.event.release.tag_name }}" =~ -(alpha|beta|rc) ]]; then
              echo "dist-tag=next" >> "$GITHUB_OUTPUT"
            else
              echo "dist-tag=latest" >> "$GITHUB_OUTPUT"
            fi
          else
            echo "dist-tag=${{ inputs.dist-tag }}" >> "$GITHUB_OUTPUT"
          fi

      - name: Publish to npm
        run: npm publish --provenance --tag ${{ steps.tag.outputs.dist-tag }}
        env:
          NODE_AUTH_TOKEN: ${{ secrets.NPM_TOKEN }}

      - name: Create GitHub Release asset
        run: |
          npm pack
          gh release upload ${{ github.event.release.tag_name }} *.tgz
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

  # ─── Post-Publish Health Check ───
  verify-publish:
    name: Verify Published Package
    runs-on: ubuntu-latest
    needs: [publish]
    timeout-minutes: 5

    steps:
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}

      - name: Install freshly published package
        run: |
          sleep 15  # Wait for npm propagation
          npm install ${{ github.event.repository.name }}@${{ github.event.release.tag_name }}
          node -e "require('${{ github.event.repository.name }}')"
          echo "✅ Package installed and loaded successfully"
```

## Best Practices

> Industry-standard best practices for implement-cicd execution.

1. **Practice 1**: Define pipeline stages with clear quality gates
2. **Practice 2**: Automate build, test, and deployment with artifact versioning
3. **Practice 3**: Integrate security scanning into the pipeline


## Error Handling

> CI/CD 流水线的异常处理规范与降级策略，涵盖构建失败、制品冲突、密钥泄露等关键场景。

### Error Scenario 1: 流水线构建失败 (P1)

**触发条件**: 代码推送或 PR 合并后，CI/CD 流水线在构建、测试或扫描阶段失败，阻断后续部署流程，影响开发交付节奏。

**处理流程**:
```
IF pipeline 状态为 "failed" 且失败阶段非手工终止
THEN
  1. 立即读取 CI 平台（GitHub Actions / GitLab CI / Jenkins）输出的错误日志摘要
  2. 按失败类型分流诊断：
     - 编译错误 → 检查依赖版本、语法变更、环境差异
     - 测试失败 → 查看 JUnit 报告中的失败用例及断言栈
     - 安全扫描阻断 → 审查 Trivy/Snyk 报告中的高危漏洞
  3. 在失败阶段自动触发重试机制（最多重试 2 次），排除临时环境问题
  4. 若重试后仍失败，自动创建故障 Issue 并标记优先级
  5. 通知流水线责任人，附带失败摘要日志、关联 Commit 及建议排查方向
END
```

**降级方案**: 若构建失败为外部依赖（npm registry 不可用、Docker Hub 限流）导致，自动切换至镜像源或私有缓存仓库重试；若为代码缺陷，阻断合并并回退至上一稳定构建版本。

**升级条件**: 同一流水线连续失败 3 次以上，或主分支构建失败超过 30 分钟未修复，或失败导致生产环境紧急修复流程阻塞。

### Error Scenario 2: 制品发布冲突 (P1)

**触发条件**: 多个并行流水线或开发者同时向同一制品仓库推送相同版本的构建产物（如 Docker 镜像 Tag 冲突、npm 包版本重复、Maven 制品坐标冲突），导致版本覆盖或发布失败。

**处理流程**:
```
IF 制品推送失败 (status: 409 Conflict / 403 Forbidden)
THEN
  1. 解析制品仓库返回的冲突错误消息，提取制品名称和版本号
  2. 查询制品仓库版本历史，确认冲突来源：
     - 同一版本被不同构建同时推送 → 保留先推送的版本
     - 版本号未随代码变更递增 → 阻断并提示版本规范
  3. 在流水线中注入版本号唯一性预检步骤（先检查制品库是否已存在目标版本）
  4. 强制使用不可变 Tag 策略（如 Git SHA 或 Build ID 作为镜像 Tag）
  5. 启用发布事务锁，同一时刻仅允许一个流水线执行发布操作
END
```

**降级方案**: 冲突发生时自动为制品追加时间戳后缀（`-YYYYMMDDHHMMSS`）生成唯一版本号，确保后续部署可正常拉取；同时记录冲突事件至审计日志。

**升级条件**: 冲突导致生产发布延迟超过 1 小时，或同一制品出现 3 次以上版本冲突，或冲突涉及安全补丁版本的紧急发布。

### Error Scenario 3: 环境变量泄露 (P0)

**触发条件**: CI/CD 流水线日志、构建产物或 Artifact 中意外暴露了敏感信息（API 密钥、数据库连接串、云服务凭证、私钥），可能因日志打印、Debug 输出或错误的配置文件包含导致。

**处理流程**:
```
IF 在日志/制品中检测到疑似敏感信息模式（AK、SK、token、password、secret）
THEN
  1. 立即触发流水线停止，阻止后续阶段运行，防止进一步扩散
  2. 使用 Git Secrets Scanner 扫描全量流水线日志、构建产物和 Artifact
  3. 自动移除/清除已暴露的 Artifact，删除包含敏感信息的日志行
  4. 轮换所有可能暴露的密钥：
     - 在密钥管理平台（Vault / AWS Secrets Manager）中立即吊销
     - 生成新密钥并更新到 CI 环境变量中
  5. 通知安全团队进行事件定级与影响面评估
END
```

**降级方案**: 若泄露发生在第三方平台日志（如 GitHub Actions 公开日志），立即将流水线切换至私有 Runner 并启用日志脱敏插件（`actions/detect-secrets` + `actions/gitleaks`）；重启构建使用临时占位密钥运行紧急修复。

**升级条件**: 凭证出现在公开可访问的流水线日志或镜像层中（任何外部可访问即视为 P0 安全事件），或泄露涉及生产环境数据库/云服务根凭证，或同一团队月内再次发生同类泄露事件。


## Quality Standards

> Acceptance criteria and quality gates for implement-cicd deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | Lead time from commit to production is under 1 day | Automated check |
| Standard 2 | Deployment frequency is at least once per day | Automated check |
| Standard 3 | Mean time to recovery (MTTR) is under 1 hour | Automated check |
## References

- [harness-engineering.md](../standards/harness-engineering.md)
- [output-validation-checklist.md](../evaluations/output-validation-checklist.md)
- [regression-checklist.md](../evaluations/regression-checklist.md)
