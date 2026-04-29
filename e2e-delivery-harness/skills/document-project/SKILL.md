# Skill: 项目文档 (Document Project)

## 概述

本 Skill 定义了项目文档编写的核心知识体系。

## 核心知识

### 文档编写方法

```python
class DocumentationSkill:
    """文档编写技能"""

    def __init__(self):
        self.doc_types = {
            "getting_started": {
                "focus": "快速上手",
                "length": "short",
                "examples": "high"
            },
            "user_guide": {
                "focus": "功能说明",
                "length": "medium",
                "examples": "medium"
            },
            "api_reference": {
                "focus": "接口定义",
                "length": "long",
                "examples": "high"
            },
            "deployment_guide": {
                "focus": "部署运维",
                "length": "medium",
                "examples": "medium"
            }
        }

    def create_api_doc(self, api_spec):
        """
        创建 API 文档
        """
        doc = {
            "overview": self.write_overview(api_spec),
            "authentication": self.write_auth(api_spec),
            "endpoints": self.write_endpoints(api_spec),
            "examples": self.write_examples(api_spec),
            "errors": self.write_errors(api_spec)
        }
        return doc

    def create_user_guide(self, features):
        """
        创建用户指南
        """
        doc = {
            "introduction": self.write_intro(features),
            "concepts": self.write_concepts(features),
            "tasks": self.write_tasks(features),
            "troubleshooting": self.write_troubleshooting(features)
        }
        return doc
```

## 关联资产

- **Scenario**: `../../scenarios/document-project/SCENARIO.md`
- **Instruction**: `../../instructions/document-project.instructions.md`
- **Prompt**: `../../prompts/document-project.prompt.md`
- **Agent**: `../../agents/technical-writer.agent.md`
