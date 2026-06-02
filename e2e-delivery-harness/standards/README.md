# Standards

Standards 是**规范性文件**，定义 Harness 中所有资产的惯例、模型和质量标准。

## 概述

Standards 提供：

- **资产模型 (Asset Model)**：每种资产类型的结构和组件
- **生命周期 (Lifecycle)**：资产从创建到退役的阶段
- **命名规范 (Naming Conventions)**：文件和目录命名规则
- **质量评分 (Quality Rubric)**：评估输出质量的标准
- **编写检查清单 (Authoring Checklist)**：创建新资产的步骤

## 文件结构

```
standards/
├── harness-engineering.md      # Harness 六层模型与合规清单（审查基准）
├── asset-model.md              # 资产模型定义
├── lifecycle.md                # 生命周期规范
├── naming-conventions.md       # 命名规范
├── id-generation-quantification.md  # ID 与量化门禁
├── smart-criteria.md           # SMART 与需求编写
├── user-story-format.md        # 用户故事与 AC
├── stakeholder-analysis-guide.md   # 干系人分析
├── output-quality-rubric.md    # 输出质量标准
└── authoring-checklist.md      # 编写检查清单
```

## 资产模型 (asset-model.md)

定义每种资产类型的结构和组件：

- **Agent**：角色定义结构
- **Skill**：能力模块结构
- **Instruction**：执行指南结构
- **Prompt**：提示词模板结构
- **Scenario**：场景包结构
- **Standard**：规范性文件结构
- **Template**：模板结构
- **Evaluation**：评估工具结构

## 生命周期 (lifecycle.md)

定义资产经历的阶段：

1. **草稿 (Draft)**：初始创建
2. **评审 (Review)**：同行评审和反馈
3. **验证 (Validation)**：按质量标准测试
4. **批准 (Approval)**：干系人签字
5. **发布 (Published)**：可供使用
6. **弃用 (Deprecated)**：正在淘汰
7. **退役 (Retired)**：不再可用

## 命名规范 (naming-conventions.md)

一致的命名规则：

- 按资产类型划分的文件命名模式
- 目录命名惯例
- YAML front matter 字段命名
- 标签命名标准
- 版本号方案

## 输出质量评分 (output-quality-rubric.md)

评估输出的标准：

- **完整性 (Completeness)**：所有必需章节是否存在？
- **正确性 (Correctness)**：内容是否准确？
- **一致性 (Consistency)**：是否遵循惯例？
- **清晰度 (Clarity)**：是否易于理解？
- **可用性 (Usability)**：是否实用？

## 编写检查清单 (authoring-checklist.md)

创建新资产的步骤：

1. 定义目的和范围
2. 遵循资产模型模板
3. 包含必需的 YAML front matter
4. 添加适当的章节内容
5. 按质量评分验证
6. 审查一致性
7. 提交审批

## 使用场景

参考 Standards 的时机：

- 创建新资产时
- 审查现有资产时
- 验证资产质量时
- 解决命名或格式问题时

## 相关资产

- **Templates**: [../templates/](..//templates/) - 资产模板
- **Evaluations**: [../evaluations/](..//evaluations/) - 质量评估工具
