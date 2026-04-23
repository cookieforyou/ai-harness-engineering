# 命名规范 / Naming Convention

> **效力等级**: P0（强制）  
> **适用范围**: 本资产库全部目录与文件

---

## 1. 文件与目录命名

- 使用 **kebab-case**（短横线连接的小写字母）
- 仅允许使用：小写字母、数字、短横线 `-`、下划线 `_`（仅用于特定语义分隔）
- 禁止使用空格、中文、特殊符号

| 类型 | 正确 | 错误 |
| :--- | :--- | :--- |
| 目录 | `code-review/` | `codeReview/`, `代码审查/` |
| 文件 | `senior-engineer.role.md` | `SeniorEngineer.role.md`, ` senior engineer.role.md` |
| 配置文件 | `assets.lock` | `Assets.Lock`, `assets-lock` |

---

## 2. 变量与字段命名

- 使用 **snake_case**（下划线连接的小写字母）
- 布尔变量使用肯定语气：`is_valid`, `has_error`
- 集合变量使用复数：`findings`, `files`

| 正确 | 错误 |
| :--- | :--- |
| `pr_title` | `prTitle`, `pr-title` |
| `file_path` | `filePath`, `FilePath` |
| `is_action_required` | `actionRequired`, `isActionRequired` |

---

## 3. 常量命名

- 使用 **UPPER_SNAKE_CASE**

| 正确 | 错误 |
| :--- | :--- |
| `MAX_RETRY_COUNT` | `maxRetryCount`, `max_retry_count` |
| `DEFAULT_TIMEOUT_MS` | `defaultTimeout` |

---

## 4. ID 标识命名

全局唯一标识采用 `{module}-{name}-{version}` 格式：

| 模块 | ID 示例 |
| :--- | :--- |
| agents | `agent-senior-engineer-1.0.0` |
| skills | `skill-diff-parser-1.0.0` |
| scenarios | `scenario-code-review-1.0.0` |
| evaluations | `checkpoint-code-review-v1-1.0.0` |
| prompts | `prompt-code-review-v1-1.0.0` |

---

## 5. 版本号格式

- 严格遵循 SemVer: `MAJOR.MINOR.PATCH`
- 预发布版本: `1.0.0-alpha.1`
- 版本标签在文件名中体现时：`v1.md`, `v2.md`（简写）

---

## 6. 特殊文件命名

| 用途 | 文件名 | 说明 |
| :--- | :--- | :--- |
| 角色卡 | `{name}.role.md` | Agent 角色定义 |
| 运行配置 | `{name}.config.yaml` | Agent 运行参数 |
| 技能定义 | `{name}.yaml` | Skill 接口与实现描述 |
| 评估点 | `{name}.checkpoint.yaml` | 质量门禁定义 |
| 数据集 | `{name}.dataset.jsonl` | 评测数据集 |
| 场景编排 | `flow.yaml` | 场景内固定文件名 |
| 资产锁定 | `assets.lock` | 场景内固定文件名 |
