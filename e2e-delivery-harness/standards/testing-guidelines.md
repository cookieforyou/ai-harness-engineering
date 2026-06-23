---
name: testing-guidelines
description: "测试指南标准，定义测试金字塔策略、各层测试类型与覆盖率目标、测试数据管理与质量门禁规范"
type: standard
version: "2.0.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-23
status: active
tags: ['standard', 'testing', 'quality', 'test-automation', 'coverage']
---

# 测试指南

> 本规范定义 E2E Delivery Harness 中所有场景的质量验证策略，涵盖测试金字塔、各层覆盖要求与数据管理原则。审查基准见 [harness-engineering.md](../harness-engineering.md)。

## 1. 测试金字塔 (Test Pyramid)

本库遵循 **分层递进** 的测试策略，各层投入比例应与金字塔结构一致：

```
           ╱╲
          ╱ E2E ╲          ← 5-10% 投入
         ╱────────╲
        ╱ Integration ╲    ← 15-25% 投入
       ╱────────────────╲
      ╱   Unit / Component ╲  ← 60-70% 投入
     ╱────────────────────────╲
    ╱         Static + Lint        ╲
```

每一层的结果作为下一层的准入条件。上层失败不会跳过下层，但下层失败应阻止上层执行。

## 2. 测试类型与定义

### 2.1 静态分析 (Static Analysis)

| 类型 | 工具示例 | 检查项 | 通过标准 |
|------|----------|--------|----------|
| **Lint** | ESLint, Pylint, Checkstyle | 代码格式、语法错误 | 零 error, warning ≤ 5 |
| **类型检查** | TypeScript, mypy, Pyright | 类型一致性 | 零 error |
| **安全扫描** | Semgrep, Snyk, Bandit | OWASP Top 10、CVE | 零 high/critical |
| **依赖审计** | npm audit, pip-audit, Dependabot | 已知漏洞依赖 | 零 critical, ≤2 high |

### 2.2 单元测试 (Unit Tests)

- **范围**: 单个函数/方法/组件，隔离所有外部依赖
- **框架**: Jest (TS/JS), Pytest (Python), JUnit (Java), Go testing
- **Mock 原则**: Mock 外部 I/O（网络、DB、文件系统）；不 Mock 纯函数
- **通过标准**:
  - 覆盖率 ≥ 85%（branch coverage ≥ 75%）
  - 新增代码覆盖率 ≥ 90%
  - 测试无 Flaky（连续 3 次运行结果一致）
- **禁止**: 测试中网络调用、数据库写入、文件系统写入

### 2.3 集成测试 (Integration Tests)

- **范围**: 跨模块/服务交互，包含真实数据库、缓存、消息队列
- **框架**: Supertest (HTTP), Testcontainers (容器化依赖), WireMock (桩服务)
- **策略**:
  - 每个集成点至少一个正向 + 一个异常场景
  - 数据库迁移前后各执行一次全量集成测试
  - 外部依赖使用 Testcontainers 或真实桩，禁止 Mock 整个依赖
- **通过标准**:
  - 覆盖率 ≥ 60%
  - 所有关键路径集成点已验证
  - 数据一致性场景通过（CRUD + 事务回滚）

### 2.4 端到端测试 (E2E Tests)

- **范围**: 从用户操作到系统响应的完整业务链路
- **框架**: Playwright (Web), REST Assured (API), Cypress
- **策略**:
  - 覆盖核心用户旅程（Happy Path + 主要异常路径）
  - 数据隔离：测试前初始化 fixture，测试后清理
  - Page Object 模式封装 UI 操作层
- **通过标准**:
  - 全部核心场景通过（P0 级别场景 100%）
  - E2E 失败自动截图 + 录制（用于调试）
  - 无条件重试：每个场景最多重试 1 次（失败后立即重试）

### 2.5 性能测试 (Performance Tests)

- **负载测试**: 模拟平均 TPS × 2～5 持续 30 分钟
- **压力测试**: 逐步增加负载至系统瓶颈
- **峰值测试**: 模拟历史峰值 TPS × 1.5 运行 15 分钟
- **持久测试**: 中负载持续运行 ≥ 8 小时监测内存泄漏
- **通过标准**:
  - P99 延迟 ≤ SLO 阈值
  - 错误率 < 0.1%
  - 无内存泄漏（内存曲线平稳）

### 2.6 安全测试 (Security Tests)

- SAST: 静态安全分析（Semgrep, SonarQube）
- DAST: 动态安全扫描（OWASP ZAP, Burp Suite）
- 容器扫描: Trivy, Grype（CVE 扫描镜像层）
- 依赖扫描: Snyk, WhiteSource

## 3. 各层覆盖率目标 (Coverage Targets per Layer)

| 层 | 最低覆盖率 | 目标覆盖率 | 测量工具 |
|----|-----------|-----------|----------|
| Lint | N/A | 零 warning | ESLint/Pylint 等 |
| Unit (Branch) | 70% | ≥ 80% | Istanbul, Coverage.py, JaCoCo |
| Unit (Line) | 80% | ≥ 90% | 同上 |
| Integration | 50% | ≥ 70% | 同上 + 定制 |
| E2E (场景) | 80% P0 场景 | 100% P0 + 70% P1 | Playwright trace |
| Performance | N/A | SLO 达标 | K6, Grafana K6, Locust |

> 覆盖率不达标 → 禁止晋升到下一环境。参见 [deployment-best-practices.md](../standards/deployment-best-practices.md) 环境晋升流程。

## 4. 测试数据管理原则 (Test Data Management)

### 4.1 数据分类

| 类别 | 定义 | 示例 | 存储位置 |
|------|------|------|----------|
| **Static Fixtures** | 不变的基础数据 | 用户角色码表、配置字典 | 代码仓库 `test/fixtures/` |
| **Dynamic Fixtures** | 测试前创建，测试后销毁 | 订单、用户账户 | 测试容器或独立 schema |
| **Anonymous Data** | 脱敏后的真实数据 | 去标识化的用户资料 | 独立匿名数据库 |
| **Synthetic Data** | 模拟生成的业务数据 | 随机满足规则的订单 | 运行时生成 |

### 4.2 数据隔离

- 单元测试: 不依赖任何外部数据存储
- 集成测试: 每个测试用例独立 schema 或独立数据库
- E2E 测试: 独立测试租户 (tenant) 或唯一标识前缀
- 并行测试: 数据键值包含 `${worker_id}_${timestamp}` 避免冲突

### 4.3 数据清理策略

- **始终清理**: 集成测试、E2E 测试在 teardown 阶段清理数据
- **清理失败标记**: 清理失败时标记为 leak 但不阻塞 CI（避免测试中断）
- **定期全量清理**: 测试数据库每天凌晨执行全量清理 (TRUNCATE ALL)

## 5. 测试门禁 (Quality Gates) 与 CI 集成

```
[Commit] → Static Analysis → Unit Tests → Integration Tests
    ↓                                                   ↓
 [Fail: Block PR]                              [Fail: Block Merge]
    ↓                                                   ↓
 E2E Tests → Performance Tests → Security Scan → [Release Artifact]
    ↓              ↓                  ↓                     ↓
 [Block Staging] [Block Canary]  [Block Prod]        [Sign & Push]
```

每个 Quality Gate 的输出可作为 handover HO-* 字段：
- `HO-TEST-1` — 单元测试覆盖率报告
- `HO-TEST-2` — 集成测试通过率
- `HO-TEST-3` — E2E 场景通过清单
- `HO-TEST-4` — 性能测试报告
- `HO-TEST-5` — 安全扫描结果

## 6. Flaky 测试管理 (Flaky Test Management)

- **识别**: 同一 PR 中测试结果在重试后从 Fail → Pass 则标记为 Flaky
- **隔离**: Flaky 测试自动移至独立 suite 并降级为警告
- **跟踪**: 每周报告 Flaky 测试列表，指定责任人修复
- **SLA**: Flaky 测试在标记后 7 天内必须修复或删除
- **禁止**: 屏蔽 (skip/ignore) flaky 测试而不创建跟踪 issue

## 7. 测试环境规范

| 属性 | 要求 |
|------|------|
| CI 执行超时 | 单元测试 ≤ 10min，集成测试 ≤ 30min，E2E ≤ 60min |
| 并行度 | 集成测试 worker ≤ 4，E2E 浏览器实例 ≤ 3 |
| 资源限制 | 每个 worker 内存 ≤ 1GB，CPU ≤ 1core |
| 幂等性 | 所有测试可重复执行任意次数结果一致 |
| 随机性 | 禁用非确定性逻辑（时间用 fixed mock，UUID 用序列） |

## 相关资产

- [asset-model.md](../standards/asset-model.md)
- [authoring-checklist.md](../standards/authoring-checklist.md)
- [deployment-best-practices.md](../standards/deployment-best-practices.md)
- [code-review-checklist.md](../standards/code-review-checklist.md)
