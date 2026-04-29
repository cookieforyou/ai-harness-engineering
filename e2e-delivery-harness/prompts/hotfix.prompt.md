# Prompt: 紧急修复场景执行 Prompt

## 概述

本 Prompt 用于指导 AI Agent 执行紧急缺陷修复工作。

## 变量定义 (Variables)

| 变量名 | 类型 | 必填 | 描述 | 示例 |
|--------|------|------|------|------|
| `issue_id` | string | 是 | 问题编号 | "BUG-001" |
| `issue_title` | string | 是 | 问题标题 | "支付失败" |
| `severity` | enum | 是 | 严重等级 | P0/P1/P2 |
| `affected_services` | string[] | 是 | 影响服务 | ["支付服务"] |
| `affected_users` | number | 是 | 影响用户数 | 1000 |
| `reporter` | string | 是 | 上报人 | "监控系统" |
| `detection_time` | datetime | 是 | 发现时间 | "2024-01-15 14:00" |
| `first_occurrence` | datetime | 否 | 首次出现 | "2024-01-15 13:30" |

## Chain of Thought

```
1. [THINK] 理解问题 → 影响范围和严重性？
2. [THINK] 定位根因 → 问题出在哪里？
3. [THINK] 设计修复 → 如何快速修复？
4. [EXECUTE] 执行修复 → 代码修改
5. [VALIDATE] 验证修复 → 测试确认
6. [OUTPUT] 输出报告 → 修复总结
```

## 错误处理 (Error Handling)

### EH-1: 根因不明

```
IF 30分钟内无法定位根因
THEN
  1. 收集更多信息
  2. 尝试临时止血方案
  3. 升级到专家团队
END
```

## Output Validation

### 验证清单

```markdown
## 自我验证报告

### V-001: 修复验证
- [ ] 问题已修复
- [ ] 无引入新问题
- [ ] 回归测试通过

### 验证结果
- 验证通过: [是/否]
```

## Handover 准备

```yaml
handover_to_support:
  deliverable: "紧急修复报告"
  status: "成功/失败"

  summary:
    issue_id: string
    duration: minutes
    root_cause: string
    fix_description: string
```

## Constraints

1. **快速响应**: 必须立即响应
2. **最小化修复**: 只修复必要部分
3. **可回滚**: 修复必须可回滚
