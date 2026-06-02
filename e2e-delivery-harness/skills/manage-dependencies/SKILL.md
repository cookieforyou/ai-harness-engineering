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
