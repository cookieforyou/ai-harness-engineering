# templates / 项目模板

本目录提供可快速启动的脚手架与模板，帮助团队以标准化方式新建 Agent、场景或项目。

---

## 模板清单

| 模板 | 用途 | 初始化命令 |
| :--- | :--- | :--- |
| `project-scaffold/` | 新项目接入 AI Harness 资产库 | 复制后按 README 配置 |
| `scenario-skeleton/` | 新建端到端场景的最小结构 | 复制到 `scenarios/{name}/` |
| `agent-template/` | 新建 Agent 的最小结构 | 复制到 `agents/` |
| `skill-skeleton.yaml` | 新建技能的接口定义模板 | 复制到 `skills/{name}.yaml` |

---

## 使用原则

- **复制即运行**: 模板复制后应能直接通过检查清单的基础项
- **最小可行**: 不包含未使用的示例代码，避免污染
- **自说明**: 模板内包含注释或配套 README，引导用户填空

---

## 新增模板

如果你有重复 3 次以上的初始化需求，请将其固化为模板：
1. 提炼最小可运行结构
2. 替换具体业务内容为占位符（如 `{{PROJECT_NAME}}`）
3. 编写 `README.md` 说明使用步骤
4. 在 `templates/README.md` 中登记
