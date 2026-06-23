---
name: rollback-plan
type: deliverable-template
version: "1.0.0"
status: active
language: "zh-CN"
---

# 回滚方案 模板

> 复制本模板到 `docs/` 对应路径，由 Agent 按 [standards/harness-engineering.md](../standards/harness-engineering.md) 填充。

## 元数据

- 项目: {project_name}
- 版本: {version}
- 作者: {author}
- 日期: {ISO8601}

## 正文

## 回滚预案概览

- **发布版本**: {version}
- **当前版本**: {current_version}
- **回滚目标版本**: {rollback_target_version}
- **预案制定人**: {author}
- **最后更新**: {ISO8601}

## 触发条件

### 自动回滚触发

- [ ] 健康检查失败: {health_check_endpoint} 连续 {n} 次不可用
- [ ] 错误率超过阈值: 5xx 错误率 > {threshold}%
- [ ] 响应时间超过阈值: P95 响应时间 > {threshold}ms
- [ ] 关键业务指标异常: {metric_name} < {threshold}

### 手动回滚触发

- [ ] 发现 P0/P1 级别线上缺陷
- [ ] 功能不符合预期且影响用户体验
- [ ] 性能退化严重,影响系统可用性
- [ ] 数据一致性问题
- [ ] {其他手动触发条件}

## 回滚步骤

### 数据库回滚

```
1. 执行数据库回滚脚本: {rollback_script_path}
2. 验证数据一致性: {验证方法}
3. 确认回滚完成: {确认方法}
```

**数据库回滚预计耗时**: {estimated_time}

### 应用回滚

| 组件 | 回滚方式 | 操作步骤 | 预计耗时 |
|------|----------|----------|----------|
| {component} | {回滚到上一版本/指定版本} | {step_description} | {time} |
| {component} | {回滚到上一版本/指定版本} | {step_description} | {time} |
| {component} | {回滚到上一版本/指定版本} | {step_description} | {time} |

### 配置回滚

```
1. 恢复配置文件: {config_backup_path}
2. 重新加载配置: {reload_method}
3. 验证配置生效: {验证方法}
```

## 回滚验证

| 验证项目 | 验证方法 | 预期结果 | 负责人 |
|----------|----------|----------|--------|
| 服务状态 | 健康检查 | 所有服务正常 | {owner} |
| 功能验证 | 冒烟测试 | 核心功能正常 | {owner} |
| 数据验证 | 数据一致性检查 | 数据完整一致 | {owner} |
| 性能验证 | 性能基准测试 | 指标回归正常 | {owner} |

## 回滚后处理

- [ ] 通知干系人回滚完成
- [ ] 记录回滚原因和时间
- [ ] 标记当前发布版本为失败
- [ ] 安排问题根因分析
- [ ] 更新发布计划

## 沟通模板

**回滚通知**:
```
主题: [紧急] {项目名} v{version} 回滚通知
内容: {项目名} v{version} 于 {time} 触发回滚,
原因: {rollback_reason},
当前状态: {current_status},
后续安排: {follow_up_plan}
```

## 修订历史

| 版本 | 日期 | 作者 | 变更内容 | 评审人 |
|------|------|------|----------|--------|
| v1.0 | {ISO8601} | {author} | 初稿 | {reviewer} |

## 验证

- [ ] 已通过 [evaluations/output-validation-checklist.md](../evaluations/output-validation-checklist.md)
