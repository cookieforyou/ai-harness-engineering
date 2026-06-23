---
name: migrate-environment
description: "Domain skill for migrate-environment execution"
category: operations
type: skill
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-23
status: active
language: "zh-CN"
tags: ['skill', 'knowledge']
---
# Skill: 环境迁移 (Environment Migration)

## Overview

本 Skill 定义了环境迁移的核心知识体系，涵盖迁移策略选择、数据一致性校验、阶段化迁移流程、自动化回滚机制等关键领域，为从开发环境到生产环境的全链路迁移提供标准化方法论。

## Core Knowledge

### 迁移策略对比

环境迁移根据业务容忍度选择不同策略，核心维度是对比**风险**、**成本**和**迁移时间**三者的trade-off。

| 策略 | 风险等级 | 实施成本 | 迁移时间 | 适用场景 |
|------|---------|---------|---------|---------|
| **Rehost (Lift-and-Shift)** | 中 | 低 | 短 | 快速上云，无架构改造 |
| **Replatform** | 中低 | 中 | 中 | 小幅优化，如迁移至托管数据库 |
| **Refactor** | 低 | 高 | 长 | 微服务拆分、架构现代化 |
| **Blue-Green 部署** | 极低 | 中高 | 中 | 关键业务，零停机要求 |
| **Canary 发布** | 极低 | 中 | 中 | 渐进式流量切换，灰度验证 |
| **Rolling 更新** | 低 | 低 | 中 | 无状态服务平缓升级 |

### 迁移阶段 (Phased Migration)

```
Assessment  →  Planning  →  Preparation  →  Execution  →  Verification  →  Cutover  →  Decommission
     ↑              ↑             ↑               ↑              ↑             ↑             ↑
  评估现状       制定计划     环境准备       执行迁移       一致性验证     流量切换     源环境下线
```

- **Assessment**: 评估源环境配置、依赖关系、数据量、网络拓扑
- **Planning**: 制定迁移计划、回滚策略、资源预算、时间窗口
- **Preparation**: 搭建目标环境、配置网络、打通数据通道
- **Execution**: 执行数据迁移、配置同步、服务部署
- **Verification**: 数据一致性校验、功能测试、性能对比
- **Cutover**: DNS切换、流量转发、全面验证
- **Decommission**: 源环境保留观察期（≥7天）后下线

### 数据一致性验证方法

数据一致性是迁移成功的核心判定标准，推荐采用双校验机制：

1. **行数比对**: 逐表比对源和目标环境的记录数，差异率要求 **<0.01%**（≥99.99% 匹配）
2. **Checksum 校验**: 对抽样数据计算 MD5/SHA256 哈希值，抽样量 ≥1000 行或全量（小表），确保数据完整性
3. **增量对账 (Reconciliation)**: 持续同步期间，对比增量数据的变更日志，确保无数据丢失

### 回滚策略

迁移必须预设自动化回滚触发条件，满足任一条件即自动触发回滚：

- **错误率 > 1%**: 迁移后服务的HTTP 5xx错误率超过基线的1%
- **延迟 > 200% 基线**: P95延迟超过迁移前基线的2倍
- **数据不一致被检测**: 行数比对差异 ≥0.01% 或 Checksum 校验不通过
- **回滚时间目标 ≤15分钟**: 一键回滚脚本覆盖DNS切换、数据库回滚、配置还原
- **源环境保留 ≥7天**: 迁移完成后源环境保留不少于7天，供数据追查和紧急回滚

### EnvironmentMigrator 类

```python
import enum
from typing import Dict, List, Optional, Tuple


class MigrationStrategy(enum.Enum):
    REHOST = "rehost"
    REPLATFORM = "replatform"
    REFACTOR = "refactor"
    BLUE_GREEN = "blue_green"
    CANARY = "canary"
    ROLLING = "rolling"


class MigrationPhase(enum.Enum):
    ASSESSMENT = "assessment"
    PLANNING = "planning"
    PREPARATION = "preparation"
    EXECUTION = "execution"
    VERIFICATION = "verification"
    CUTOVER = "cutover"
    DECOMMISSION = "decommission"


class EnvironmentMigrator:
    """环境迁移执行器，支持多策略选择、预检、切换和回滚"""

    def __init__(self, source: str, target: str, strategy: MigrationStrategy):
        self.source = source
        self.target = target
        self.strategy = strategy
        self.current_phase: Optional[MigrationPhase] = None
        self.error_rate_baseline: float = 0.0
        self.latency_baseline: float = 0.0

    def select_strategy(self, risk_tolerance: float, budget: float) -> MigrationStrategy:
        """根据风险容忍度和预算选择最优迁移策略"""
        strategy_scores = {
            MigrationStrategy.REHOST: {"risk": 0.7, "cost": 0.3, "speed": 0.9},
            MigrationStrategy.REPLATFORM: {"risk": 0.5, "cost": 0.5, "speed": 0.6},
            MigrationStrategy.REFACTOR: {"risk": 0.2, "cost": 0.9, "speed": 0.3},
            MigrationStrategy.BLUE_GREEN: {"risk": 0.1, "cost": 0.7, "speed": 0.5},
            MigrationStrategy.CANARY: {"risk": 0.1, "cost": 0.6, "speed": 0.5},
            MigrationStrategy.ROLLING: {"risk": 0.3, "cost": 0.4, "speed": 0.7},
        }
        # 根据风险容忍度加权选择
        sorted_strategies = sorted(
            strategy_scores.items(),
            key=lambda x: (
                x[1]["risk"] * (1 - risk_tolerance) +
                x[1]["cost"] * (1 - min(budget, 1.0)) +
                x[1]["speed"]
            ),
            reverse=True,
        )
        return sorted_strategies[0][0]

    def pre_flight_check(self) -> Dict[str, bool]:
        """执行迁移前预检，返回所有检查项的状态"""
        checks = {
            "source_accessible": self._check_connectivity(self.source),
            "target_ready": self._check_connectivity(self.target),
            "backup_completed": self._backup_source(),
            "disk_space_sufficient": self._check_disk_space(),
            "network_bandwidth_adequate": self._check_bandwidth(),
            "rollback_script_ready": self._verify_rollback_script(),
            "maintenance_window_confirmed": self._confirm_maintenance_window(),
        }
        failed = [k for k, v in checks.items() if not v]
        if failed:
            raise RuntimeError(f"Pre-flight checks failed: {', '.join(failed)}")
        return checks

    def cutover(self, strategy: str = "dns") -> bool:
        """执行流量切换，支持DNS切换/负载均衡权重调整/反向代理更新"""
        if strategy == "dns":
            return self._dns_switch()
        elif strategy == "weight":
            return self._traffic_weight_adjust()
        elif strategy == "proxy":
            return self._reverse_proxy_update()
        else:
            raise ValueError(f"Unknown cutover strategy: {strategy}")

    def rollback(self, trigger_reason: str) -> bool:
        """自动化回滚：DNS回切、数据库回滚、配置还原"""
        steps = [
            ("DNS回切", self._dns_rollback()),
            ("数据库回滚", self._database_rollback()),
            ("配置还原", self._config_restore()),
            ("流量切换回源", self._traffic_restore()),
        ]
        for step_name, success in steps:
            if not success:
                raise RuntimeError(f"Rollback failed at step: {step_name}")
        self._log_rollback_event(trigger_reason)
        return True

    def _check_connectivity(self, endpoint: str) -> bool:
        """检查端点可达性"""
        import subprocess
        return subprocess.call(["ping", "-c", "1", "-W", "2", endpoint]) == 0

    def _backup_source(self) -> bool:
        """备份源环境"""
        return True  # placeholder

    def _check_disk_space(self) -> bool:
        """检查磁盘空间"""
        return True  # placeholder

    def _check_bandwidth(self) -> bool:
        """检查网络带宽"""
        return True  # placeholder

    def _verify_rollback_script(self) -> bool:
        """验证回滚脚本可用性"""
        return True  # placeholder

    def _confirm_maintenance_window(self) -> bool:
        """确认维护窗口"""
        return True  # placeholder

    def _dns_switch(self) -> bool:
        """DNS切换"""
        return True  # placeholder

    def _traffic_weight_adjust(self) -> bool:
        """流量权重调整"""
        return True  # placeholder

    def _reverse_proxy_update(self) -> bool:
        """反向代理更新"""
        return True  # placeholder

    def _dns_rollback(self) -> bool:
        """DNS回滚"""
        return True  # placeholder

    def _database_rollback(self) -> bool:
        """数据库回滚"""
        return True  # placeholder

    def _config_restore(self) -> bool:
        """配置还原"""
        return True  # placeholder

    def _traffic_restore(self) -> bool:
        """流量恢复"""
        return True  # placeholder

    def _log_rollback_event(self, reason: str) -> None:
        """记录回滚事件"""
        import logging
        logging.warning(f"Rollback triggered due to: {reason}")
```

### 传统迁移方法

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

## Best Practices

> 环境迁移的行业最佳实践，确保迁移过程安全、可靠、可追溯。

1. **分阶段灰度迁移**：先迁移非关键环境（Dev → Staging），再迁移类生产环境（Pre-Prod），最后迁移生产环境。每阶段间设置 ≥24 小时的验证窗口和冒烟测试期，确保异常可被及时发现并阻断，避免级联故障扩散至生产环境

2. **基础设施即代码 (IaC) 先行**：迁移前将源环境的所有基础设施定义为 Terraform / CloudFormation 代码（覆盖率 ≥95%）。目标环境通过 IaC 一键重建，确保环境一致性，消除手动配置漂移带来的 "works on my machine" 问题。配置变更必须经过 Code Review 和版本管理

3. **数据一致性双校验**：迁移完成后执行行数比对（差异 < 0.01%）和抽样 Checksum 校验（≥1000 行随机抽样，MD5/SHA256），两个校验均通过后方可执行流量切换。任一校验不通过则自动阻断并触发回滚流程

## Common Pitfalls

> 环境迁移中常见错误及其防范措施。

### Pitfall 1: 直接全量迁移生产环境

**Risk**: 未经预生产验证直接迁移生产，配置差异或数据不兼容导致全站宕机。跳过 Staging/Pre-Prod 验证环节会遗漏大量环境特有的兼容性问题。

**Prevention**: 严格执行 Dev → Staging → Pre-Prod → Prod 四阶段迁移，每阶段有明确的 Go / No-Go 门禁检查清单（至少包含：功能测试通过率 ≥99%、性能指标不劣化、数据一致性校验通过）。

**Impact**: P0 级生产事故，回滚时间可能超过数小时，同时影响所有在线用户，造成严重业务损失和声誉损害。

### Pitfall 2: 忽略数据一致性校验

**Risk**: 仅依靠迁移工具的 "成功" 状态判断迁移完成，实际存在数据丢失、字段截断或字符编码损坏未被发现。更隐蔽的问题是浮点精度差异和时区处理不一致导致的数据偏差。

**Prevention**: 实施自动化数据一致性校验（行数 + Checksum），写入迁移 Runbook 的验证步骤，将校验结果纳入迁移报告。对关键业务表（如订单表、用户表）增加字段级逐行比对。

**Impact**: 数据不一致可能在数天后才被发现，此时增量数据已双向覆盖，修复成本极高，业务损失不可逆。

### Pitfall 3: 无回滚预案

**Risk**: 迁移失败后无自动化回滚手段，依赖手动重建环境耗时数小时。在迁移窗口即将关闭时，团队在压力下可能选择 "向前修复" 而非回滚，进一步恶化故障。

**Prevention**: 保留源环境 ≥7 天，实现一键回滚脚本（含 DNS 切换、数据库回滚、配置还原），回滚时间目标 ≤15 分钟。每季度执行一次回滚演练，确保脚本可靠性。

**Impact**: 业务中断时间远超 SLA（通常从数小时延长至数十小时），可能导致违反合规要求并触发罚款条款。

## 相关资产

以下标准和评估清单与本技能直接相关，执行环境迁移时应一并参考：

- [回滚策略标准](../../standards/rollback-strategy.md) — 标准化回滚分级和回滚流程定义
- [部署最佳实践](../../standards/deployment-best-practices.md) — Blue-Green/Canary/Rolling 部署策略详解
- [部署质量检查清单](../../evaluations/deployment-quality-checklist.md) — 部署完成后逐项验证质量门禁
- [回滚演练报告模板](../../evaluations/rollback-drill-report.md) — 回滚演练记录和复盘模板
