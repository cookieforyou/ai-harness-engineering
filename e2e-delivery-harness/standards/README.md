# Standards

Standards 是**规范性文件**，定义 Harness 中所有资产的惯例、模型和质量标准。

## 概述

Standards 提供：

- **Harness Engineering**：六层驾驭模型与五类资产合规清单（审查基准）
- **资产模型 (Asset Model)**：每种资产类型的结构和组件
- **生命周期 (Lifecycle)**：资产从创建到退役的阶段
- **命名规范 (Naming Conventions)**：文件和目录命名规则
- **质量评分 (Quality Rubric)**：评估输出质量的标准
- **编写检查清单 (Authoring Checklist)**：创建新资产的步骤
- **领域标准**：各场景 Related Resources 引用的专项规范（ADR、测试、部署、SRE 等）

## 文件结构

```
standards/
├── harness-engineering.md           # 审查与优化唯一基准
├── asset-model.md
├── lifecycle.md
├── naming-conventions.md
├── id-generation-quantification.md
├── smart-criteria.md
├── user-story-format.md
├── stakeholder-analysis-guide.md
├── output-quality-rubric.md
├── authoring-checklist.md
├── adr-template.md                  # 架构决策
├── api-design-guidelines.md
├── invest-principle.md
├── testing-best-practices.md
├── deployment-best-practices.md
├── incident-management.md
├── sre-best-practices.md
└── …（共 37 个文件，含 README）
```

## 维护

新增或修改标准后运行：

```bash
python3 scripts/harness-full-compliance.py
```

## 相关资产

- **Templates**: [../templates/](../templates/) - 资产与交付物模板
- **Evaluations**: [../evaluations/](../evaluations/) - 质量评估工具
