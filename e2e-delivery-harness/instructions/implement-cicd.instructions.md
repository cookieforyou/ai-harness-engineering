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

## 流水线设计规范

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

## 构建配置规范

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

## 测试配置规范

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

### 测试报告配置

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

## 部署策略规范

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

## 安全配置规范

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

## 监控告警规范

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
