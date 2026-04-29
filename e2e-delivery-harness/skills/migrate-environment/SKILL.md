# Skill: 环境迁移 (Environment Migration)

## 概述

本 Skill 定义了环境迁移的核心知识体系。

## 核心知识

### 迁移方法

```python
class EnvironmentMigration:
    """环境迁移"""

    def __init__(self, source, target):
        self.source = source
        self.target = target

    def full_migration(self):
        """全量迁移"""
        # 1. 备份
        self.backup()
        # 2. 迁移数据
        self.migrate_data()
        # 3. 迁移配置
        self.migrate_config()
        # 4. 验证
        self.verify()

    def incremental_migration(self):
        """增量迁移"""
        # 1. 基线迁移
        self.baseline_migration()
        # 2. 增量同步
        self.incremental_sync()
        # 3. 切换
        self.switch()

    def blue_green_migration(self):
        """蓝绿迁移"""
        # 1. 部署新环境
        self.deploy_target()
        # 2. 流量切换
        self.switch_traffic()
        # 3. 保留旧环境
        self.keep_old_env()
```

## 关联资产

- **Scenario**: `../../scenarios/migrate-environment/SCENARIO.md`
- **Instruction**: `../../instructions/migrate-environment.instructions.md`
- **Prompt**: `../../prompts/migrate-environment.prompt.md`
- **Agent**: `../../agents/devops-engineer.agent.md`
