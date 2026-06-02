---
name: migrate-environment
description: "Domain skill for migrate-environment execution"
category: operations
type: skill
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['skill', 'knowledge']
---
# Skill: 环境迁移 (Environment Migration)

## Overview

本 Skill 定义了环境迁移的核心知识体系。

## Core Knowledge

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

## Associated Assets

- **Scenario**: `../../scenarios/migrate-environment/SCENARIO.md`
- **Instruction**: `../../instructions/migrate-environment.instructions.md`
- **Prompt**: `../../prompts/migrate-environment.prompt.md`
- **Agent**: `../../agents/migrate-environment.agent.md`


## Core Knowledge

> Essential knowledge domain for migrate-environment execution.

### Domain Fundamentals
- [Core concept 1]
- [Core concept 2]
- [Core concept 3]

### Key Principles
1. [Principle 1]
2. [Principle 2]
3. [Principle 3]


## Best Practices

> Proven practices for migrate-environment excellence.

1. **Practice 1**: [Description and rationale]
2. **Practice 2**: [Description and rationale]
3. **Practice 3**: [Description and rationale]


## Anti-patterns (反模式)

> 与 Common Pitfalls 同义，执行时合并检查。

## Common Pitfalls

> Frequent mistakes to avoid during migrate-environment execution.

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
