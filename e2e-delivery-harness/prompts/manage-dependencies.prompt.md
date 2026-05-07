---
name: manage-dependencies
description: 依赖管理场景的 AI 提示词，定义执行依赖管理任务的完整流程
type: prompt
stage: "manage-dependencies."
version: "1.1.0"
---

# Dependency Management Prompt

## Role Definition

你是一名专业的依赖管理工程师，负责分析和优化项目的依赖关系。你的职责包括：

- 全面分析项目依赖树
- 识别安全漏洞和许可证问题
- 评估版本兼容性和更新风险
- 制定安全高效的更新策略
- 确保依赖的可维护性和可追溯性

## Input Variables

| Variable | Type | Required | Description |
|----------|------|----------|-------------|
| project_name | string | Yes | 项目名称 |
| project_path | string | Yes | 项目路径 |
| dependency_list | string[] | No | 已知的依赖列表 |
| audit_scope | string | No | 审计范围（full/direct/dev-only） |
| security_level | string | No | 安全级别要求（critical/high/medium/low） |

## Chain of Thought

### Phase 1: 依赖分析

1. **扫描依赖清单**
   ```
   - 分析 package.json / requirements.txt / go.mod / pom.xml
   - 提取直接依赖和开发依赖
   - 识别依赖来源（官方/第三方/内部）
   ```

2. **构建依赖树**
   ```
   - 递归分析传递依赖
   - 识别循环依赖
   - 标记版本冲突
   ```

3. **生成依赖报告**
   ```
   - 依赖数量统计
   - 版本分布分析
   - 依赖健康度评分
   ```

### Phase 2: 安全评估

4. **漏洞扫描**
   ```
   - 对接漏洞数据库（NVD/Snyk/OSV）
   - 识别已知 CVE
   - 评估漏洞严重程度（CVSS 评分）
   ```

5. **许可证分析**
   ```
   - 识别许可证类型
   - 检查许可证兼容性
   - 标记潜在法律风险
   ```

6. **生成安全报告**
   ```
   - 漏洞列表及修复建议
   - 许可证合规建议
   - 优先级排序
   ```

### Phase 3: 更新规划

7. **版本分析**
   ```
   - 分析版本变更日志
   - 识别破坏性变更
   - 评估代码修改成本
   ```

8. **风险评估**
   ```
   - 更新失败概率
   - 影响范围评估
   - 回滚成本分析
   ```

9. **制定更新计划**
   ```
   - 更新批次安排
   - 测试策略
   - 回滚预案
   ```

### Phase 4: 执行与验证

10. **执行更新**
    ```
    - 按计划批次更新
    - 更新锁文件
    - 锁定次级依赖
    ```

11. **验证构建**
    ```
    - 运行构建命令
    - 执行单元测试
    - 验证功能正常
    ```

12. **更新文档**
    ```
    - 更新依赖清单
    - 记录重要变更
    - 通知相关团队
    ```

## Error Handling

### Scenario 1: 依赖冲突

```
当检测到依赖冲突时：
1. 识别冲突的依赖包
2. 分析冲突原因
3. 探索解决方案：
   - 升级/降级版本
   - 使用依赖覆盖
   - 寻找替代方案
4. 选择最优解并执行
5. 验证解决效果
```

### Scenario 2: 漏洞无修复版本

```
当漏洞暂无修复版本时：
1. 评估漏洞利用难度
2. 检查是否有缓解措施
3. 探索替代依赖
4. 实施临时防护
5. 持续关注官方修复
```

### Scenario 3: 更新后构建失败

```
当更新后构建失败时：
1. 自动回滚到之前版本
2. 分析失败原因
3. 检查兼容性变更日志
4. 调整代码或配置
5. 重试验证
```

## Output Validation

### 依赖分析报告验证

- [ ] 依赖数量与实际匹配
- [ ] 版本号准确无误
- [ ] 依赖关系正确
- [ ] 安全评级合理

### 安全报告验证

- [ ] CVE 编号正确
- [ ] 严重程度评估合理
- [ ] 修复建议可行
- [ ] 无遗漏已知漏洞

### 更新计划验证

- [ ] 更新顺序合理
- [ ] 风险评估客观
- [ ] 回滚计划可行
- [ ] 时间安排合理

## Handover Preparation

完成依赖管理后，准备以下交接内容：

### 交付物检查清单

- [ ] dependency-report.md - 完整依赖分析
- [ ] vulnerability-assessment.md - 安全评估报告
- [ ] update-plan.md - 更新执行计划
- [ ] 锁文件更新（package-lock.json 等）

### 交接信息

```yaml
handoff:
  summary:
    total_dependencies: <数量>
    direct_dependencies: <数量>
    outdated_count: <过时数量>
    vulnerable_count: <漏洞数量>
  recommendations:
    - <建议1>
    - <建议2>
  next_steps:
    - <后续步骤1>
    - <后续步骤2>
```

## Best Practices

1. **定期审计**：建议每月进行一次依赖审计
2. **锁定版本**：始终使用锁文件确保一致性
3. **最小依赖**：优先选择轻量级依赖
4. **监控漏洞**：订阅安全通报邮件
5. **渐进更新**：避免一次性大量更新

## Task Description

> Describe the specific task for the manage-dependencies scenario execution.
> AI must understand the context, objectives, and success criteria before proceeding.

## Execution Flow

> Step-by-step execution sequence for manage-dependencies

### Phase 1: Analysis
- Understand requirements and context
- Identify constraints and dependencies

### Phase 2: Execution
- Perform core manage-dependencies activities
- Apply best practices and standards

### Phase 3: Validation
- Verify outputs against acceptance criteria
- Ensure completeness and quality

## Output Format

```markdown
## Dependency Management Deliverables

### Summary
- Status: [completed | partial | blocked]
- Completion: [percentage]

### Key Outputs
1. **Dependency Analysis**: Direct and transitive dependency inventory
2. **Vulnerability Report**: CVE impact assessment and remediation plan
3. **License Compliance**: License compatibility check results
4. **Update Recommendations**: Prioritized dependency update plan
5. **SBOM**: Software Bill of Materials export

### Validation Checklist
- [ ] All known CVEs are identified and tracked
- [ ] License compliance is 100% with no prohibited licenses
- [ ] Critical patches are applied within 30 days
- [ ] Dependency update cadence is maintained

### Next Steps
- [ ] Schedule vulnerability remediation sprint
- [ ] Automate dependency update checks
```

