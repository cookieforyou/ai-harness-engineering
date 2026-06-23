---
name: git-workflow
type: standard
version: "2.0.0"
status: active
---

# Git 工作流

> 本规范定义 E2E Delivery Harness 中所有仓库的 Git 分支策略、提交约定、PR/MR 流程与发布标记。审查基准见 [harness-engineering.md](harness-engineering.md)。

## 1. 分支策略对比

### 1.1 Trunk-based Development (推荐)

**适用**: CI/CD 成熟、团队 < 20 人、微服务架构

```
main ──feat/A──────feat/B──────hotfix/C──→
        \          /            /
         f1..fn   f1..fn      h1..hn
```

- 分支存活时间 ≤ 2 天
- 每日至少一次合并到 trunk
- 使用 Feature Flags 控制未完成功能
- 每个 commit 可发布

### 1.2 GitFlow

**适用**: 版本发布周期明确、需要长期支持版本 (LTS)

```
master ──v1.0────v1.1────v2.0────v2.1──→
         \       /       \       /
develop──f1──f2─f3──release/v1.1─f4──→
         \
        feature/xxx
```

- `master`：生产发布历史，只接受 merge commit
- `develop`：日常开发集成分支
- `feature/xxx`：从 develop 创建，合并回 develop
- `release/x.y`：从 develop 创建，合并到 master + develop
- `hotfix/x.y.z`：从 master 创建，合并到 master + develop

### 1.3 选择决策

| 条件 | 推荐策略 | 说明 |
|------|----------|------|
| 每日发布多次 | Trunk-based | 高频发布无需长分支 |
| 定期固定版本 | GitFlow | 版本管理严格 |
| 团队 < 10 人 | Trunk-based | 协作简单 |
| 团队 10-50 人 | 改良 GitFlow | 轻量 GitFlow，feature 分支存活 ≤ 5 天 |
| 移动端/客户端 | GitFlow | 版本商店审核周期固定 |

## 2. 提交信息规范 (Commit Message Convention)

### 2.1 格式

```
<type>(<scope>): <subject>

<body>

<footer>
```

**type** (必填):
| 类型 | 含义 | 版本影响 |
|------|------|----------|
| `feat` | 新功能 | minor (MINOR) |
| `fix` | 缺陷修复 | patch (PATCH) |
| `refactor` | 重构，不涉及功能变更 | patch |
| `docs` | 文档变更 | patch |
| `style` | 格式调整（空格、缩进） | 不发布 |
| `test` | 测试相关 | 不发布 |
| `chore` | 构建/工具/依赖 | 不发布 |
| `perf` | 性能优化 | patch |
| `ci` | CI 配置变更 | 不发布 |
| `breaking` | 破坏性变更 | major (MAJOR) |

**scope** (可选): 影响模块 — `auth`, `payment`, `api`, `db` 等

**subject**: 不超过 72 字符，动词开头（现在时），首字母小写，末尾无句号

**body**: 说明 WHY（做了什么 + 为什么这样做），每行 ≤ 72 字符

**footer**: `BREAKING CHANGE: <description>` 或 `Closes #123, #456`

### 2.2 示例

```
feat(auth): add OAuth2.0 login with Google provider

Implement Google OAuth flow using OpenID Connect.
Token refresh is handled automatically every 45 minutes.

Closes #234
```

```
fix(payment): handle timeout on Stripe charge call

The Stripe charge API occasionally times out under load.
Added retry with exponential backoff, max 3 attempts.

Fixes #567
```

```
breaking!(api): change order response format

BREAKING CHANGE: The `order.items` field is now an object keyed by SKU
instead of an array. This affects all order retrieval endpoints.
```

### 2.3 禁止

- 单次提交包含多个不相关变更（拆分提交）
- 提交信息为 `fix bug`、`update`、`wip`、`asdf`
- 合并冲突未解决就提交

## 3. PR/MR 流程 (Pull/Merge Request Process)

### 3.1 PR 创建规范

- **标题**: 遵循 commit message 格式 (`<type>(<scope>): <subject>`)
- **描述模板**:
```markdown
## Description
（说明变更内容与动机）

## Type of Change
- [ ] feat: 新功能
- [ ] fix: 缺陷修复
- [ ] refactor: 重构
- [ ] docs: 文档
- [ ] test: 测试
- [ ] chores: 构建/工具

## Testing
（说明测试方式与结果）

## Checklist
- [ ] 单元测试通过
- [ ] 集成测试通过
- [ ] 代码审查完成
- [ ] 无新增 warning
- [ ] API 文档已更新（如适用）
```

### 3.2 PR 大小限制

| 指标 | 合理 | 警告 | 需拆分 |
|------|------|------|--------|
| 变更文件数 | ≤ 10 | 11-20 | > 20 |
| 总新增行数 | ≤ 300 | 301-1000 | > 1000 |
| 变更模块数 | ≤ 2 | 3 | > 3 |
| commit 数 | 1-5 | 6-10 | > 10（需 squash） |

### 3.3 合并策略

| 策略 | 时机 | 命令 |
|------|------|------|
| **Squash merge** | 功能分支合并到 main/develop | `git merge --squash` |
| **Merge commit** | release/hotfix 分支合并到 main | `git merge --no-ff` |
| **Rebase merge** | 个人分支同步上游变更 | `git rebase main` |

- 禁止直接在 main/master 上提交
- 禁止 force push 到共享分支（个人 feature 分支除外）
- PR 至少 1 个 Approve 才能合并（参见 [code-review-checklist.md](code-review-checklist.md)）

## 4. 发布标记 (Release Tagging)

### 4.1 版本规范 (SemVer)

```
v{MAJOR}.{MINOR}.{PATCH}-{pre-release}+{build}

示例: v2.1.3-rc.1+build.456
```

- **MAJOR**: 破坏性 API/DB 变更
- **MINOR**: 新功能，向后兼容
- **PATCH**: 缺陷修复，向后兼容
- **pre-release**: `alpha`, `beta`, `rc.N`
- **build**: CI build number 或 commit hash（可选）

### 4.2 标记规范

```
# 生产发布
git tag -a v2.1.3 -m "release: v2.1.3 - payment timeout fix"

# 预发布
git tag -a v2.2.0-rc.1 -m "release: v2.2.0-rc.1 - candidate for testing"
```

### 4.3 标记与分支对应

| 分支 | 标记类型 | 示例 |
|------|----------|------|
| master/main | 生产版本 | v1.0.0, v1.1.0 |
| release/* | RC 预发布 | v1.1.0-rc.1 |
| hotfix/* | 补丁版本 | v1.0.1 |
| feature/* | 不标记 | - |

## 5. HO-* 映射

- `HO-GIT-001` — 分支策略已定义并与项目匹配
- `HO-GIT-002` — commit message 格式合规
- `HO-GIT-003` — PR 大小在限制内
- `HO-GIT-004` — 版本标签格式正确

## 引用

- [asset-model.md](asset-model.md)
- [authoring-checklist.md](authoring-checklist.md)
- [code-review-checklist.md](code-review-checklist.md)
- [deployment-best-practices.md](deployment-best-practices.md)
