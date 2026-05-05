---
name: implement-cicd
description: "Domain skill for implement-cicd execution"
type: skill
version: "1.1.0"
stage: "implement-cicd"
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
- **Agent**: `../../agents/cicd-engineer.agent.md`


## Core Knowledge

> Essential knowledge domain for implement-cicd execution.

### Domain Fundamentals
- [Core concept 1]
- [Core concept 2]
- [Core concept 3]

### Key Principles
1. [Principle 1]
2. [Principle 2]
3. [Principle 3]


## Best Practices

> Proven practices for implement-cicd excellence.

1. **Practice 1**: [Description and rationale]
2. **Practice 2**: [Description and rationale]
3. **Practice 3**: [Description and rationale]


## Common Pitfalls

> Frequent mistakes to avoid during implement-cicd execution.

### Pitfall 1: [Name]
**Risk**: [Description]
**Prevention**: [How to avoid]
**Impact**: [Consequences if not avoided]

### Pitfall 2: [Name]
**Risk**: [Description]
**Prevention**: [How to avoid]
**Impact**: [Consequences if not avoided]

### Pitfall 3: [Name]
**Risk**: [Description]
**Prevention**: [How to avoid]
**Impact**: [Consequences if not avoided]
