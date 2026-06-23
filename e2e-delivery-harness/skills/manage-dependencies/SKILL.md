---
name: manage-dependencies
description: "Domain skill for manage-dependencies execution"
category: development
type: skill
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
language: "zh-CN"
tags: ['skill', 'knowledge']
---
# Dependency Management Skill

## Core Knowledge

### 1. Package Manager Fundamentals

#### npm (Node.js)
- **Lock File**: package-lock.json
- **Manifest**: package.json
- **Commands**:
  - `npm install` - 安装依赖
  - `npm update` - 更新依赖
  - `npm audit` - 安全审计
  - `npm ls` - 列出依赖

#### pip (Python)
- **Lock File**: requirements.lock / Pipfile.lock
- **Manifest**: requirements.txt / Pipfile
- **Commands**:
  - `pip freeze` - 导出依赖
  - `pip install -r requirements.txt` - 安装
  - `pip-audit` - 安全审计

#### go mod (Go)
- **Lock File**: go.sum
- **Manifest**: go.mod
- **Commands**:
  - `go mod tidy` - 整理依赖
  - `go get` - 获取依赖
  - `go mod verify` - 验证依赖

### 2. Semantic Versioning (SemVer)

```
MAJOR.MINOR.PATCH
1.2.3
│   │   │
│   │   └── Patch: bug 修复，兼容更新
│   └───── Minor: 新功能，向后兼容
└───────── Major: 破坏性变更
```

- **^1.2.3**: 允许 Minor 和 Patch 更新
- **~1.2.3**: 仅允许 Patch 更新
- **1.2.3**: 精确版本

### 3. Security Vulnerability Databases

| Database | URL | API |
|----------|-----|-----|
| NVD | nvd.nist.gov | REST API |
| OSV | osv.dev | API |
| Snyk | snyk.io | API |
| GitHub Advisory | github.com/advisories | GraphQL |

### 4. License Categories

#### Permissive (可商用)
- MIT, Apache 2.0, BSD 2/3-Clause, ISC

#### Copyleft (需开源)
- GPL 2.0/3.0, LGPL, AGPL

#### Proprietary (专有)
- 需要商业许可

## Best Practices

### 1. 依赖选择原则
- 优先选择活跃维护的包
- 优先选择 Stars 多的包
- 优先选择文档完善的包
- 优先选择依赖较少的包
- 优先选择类型安全的包（TypeScript）

### 2. 版本控制策略
- 生产依赖锁定精确版本
- 开发依赖可使用范围版本
- CI 环境必须使用锁文件
- 定期检查依赖时效性

### 3. 安全审计流程
```
1. 定期运行 npm audit / pip-audit
2. 设置安全告警阈值
3. 订阅安全通报
4. 定期更新依赖
5. 使用 WAF/IDS 缓解已知风险
```

### 4. 依赖优化技巧
- 使用 `npm prune` 清理未使用依赖
- 使用 `npm dedupe` 去重传递依赖
- 使用 `bundle analyzer` 可视化依赖大小
- 考虑使用替代轻量级库

## Common Issues & Solutions

### Issue 1: 依赖循环
```
A -> B -> C -> A
Solution: 重构代码结构，打破循环依赖
```

### Issue 2: 版本冲突
```
A requires lodash@^4.0.0
B requires lodash@^4.17.0
Solution: 升级到兼容版本或使用 npm overrides
```

### Issue 3: 幽灵依赖
```
项目中使用了但 package.json 未声明
Solution: 使用 npm ls 检查，确保 package.json 准确
```

### Issue 4: 依赖过多
```
Solution:
1. 分析未使用依赖
2. 寻找多功能替代品
3. 考虑内置实现
4. 使用 tree-shaking
```

## Toolchain Reference

### Analysis Tools
- `npm-compare-versions`: 版本比较
- `license-checker`: 许可证检查
- `depcheck`: 未使用依赖检测
- `bundlesize`: 依赖大小监控

### Security Tools
- `npm audit`: npm 内置审计
- `snyk`: 高级安全分析
- `Socket`: npm 安全平台
- `WhiteSource`: 企业级安全

### Update Tools
- `npm-check-updates`: 检查更新
- `greenkeeper`: 自动更新 PR
- `renovate`: 依赖更新机器人
- `dependabot`: GitHub 原生更新


## Anti-patterns (反模式)

> 与 Common Pitfalls 同义，执行时合并检查。

## Common Pitfalls

> Frequent mistakes to avoid during manage-dependencies execution.

### Pitfall 1: 忽视传递依赖的漏洞
**Risk**: 只关注直接声明的依赖版本和安全告警，忽略传递依赖(即依赖的依赖)中存在的已知漏洞(CVE)。攻击者可以通过利用传递依赖中的低关注度漏洞间接攻破应用。很多大型安全事件(如event-stream、lodash原型链污染)均通过传递依赖链传播。
**Prevention**: 使用 `npm audit --recursive`、`pip-audit`、`Trivy`、`Snyk` 等工具对完整依赖树进行安全扫描；配置CI门禁——传递依赖中存在高危及以上漏洞时阻止构建；订阅OSV(Open Source Vulnerabilities)数据库获取实时漏洞通知。
**Impact**: 看似安全的直接依赖通过传递依赖链引入漏洞，安全团队无法全面掌握攻击面；漏洞被利用后可能导致数据泄露、服务入侵或供应链攻击溯源困难。

### Pitfall 2: 盲目升级大版本
**Risk**: 在不阅读Changelog、不评估Breaking Changes的前提下直接将依赖升级到最新Major版本。Major版本升级通常包含不兼容的API变更、行为变化和移除的废弃功能，直接升级可能导致应用运行时崩溃或逻辑错误。
**Prevention**: Major版本升级前必须阅读完整的Changelog和Migration Guide；先在独立分支上升级并运行完整的回归测试套件；采用渐进式升级策略——先升级到最新Minor版本，再处理Major变更；使用Renovate/Dependabot自动创建版本升级PR并附加Changelog摘要。
**Impact**: 生产环境出现难以排查的运行时异常；已废弃API的移除导致应用崩溃；新版本行为变化导致业务逻辑偏差而未触发显式错误。

### Pitfall 3: 不读Changelog直接升级
**Risk**: 即使是Minor或Patch版本升级，也可能包含行为变更(如安全加固导致的兼容性问题、默认配置调整、废弃警告)。仅查看版本号而不阅读Changelog就升级，可能忽略重要的变更通知和迁移建议。
**Prevention**: 在升级PR描述中要求包含Changelog的核心变更摘要，由审查者确认无影响后才能合入；对关键依赖的升级设置观察期——先在预发环境运行24小时后无异常再推送到生产。
**Impact**: 未预见的副作用的修复成本高于升级本身带来的收益；多次忽视Changelog导致依赖维护者停止发布详细变更记录，形成恶性循环。
