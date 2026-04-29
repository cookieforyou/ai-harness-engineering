# Instructions: 环境迁移 (Migrate Environment)

## 迁移类型规范

### 迁移类型对比

| 类型 | 特点 | 停机时间 | 适用场景 |
|------|------|----------|----------|
| 全量迁移 | 一次性迁移 | 长 | 小数据量 |
| 增量迁移 | 分批次迁移 | 短 | 大数据量 |
| 蓝绿部署 | 双环境切换 | 极短 | 生产环境 |
| 滚动迁移 | 逐步迁移 | 无 | 高可用要求 |

## 数据迁移规范

### 数据迁移策略

```yaml
migration_strategy:
  small_data:
    size: "< 1GB"
    method: "mysqldump/pg_dump"
    downtime: "< 1 hour"

  medium_data:
    size: "1GB - 100GB"
    method: "增量备份 + 同步"
    downtime: "< 30 minutes"

  large_data:
    size: "> 100GB"
    method: "CDC + 增量同步"
    downtime: "接近零"
```

## 回滚规范

### 回滚策略

```yaml
rollback:
  enabled: true
  trigger:
    - "功能验证失败"
    - "数据不一致"
    - "性能严重下降"

  steps:
    - "停止新环境"
    - "恢复数据"
    - "切换流量"
    - "验证旧环境"

  verification:
    - "健康检查"
    - "功能测试"
    - "数据验证"
```
