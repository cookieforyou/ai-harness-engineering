---
name: deploy-release
description: "Technical instructions for deployment and release execution"
applyTo: "scenarios/deploy-release/**"
phase: deployment
type: instruction
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: [instruction, technical, deployment]
---
# Deploy Release Instructions

## Purpose

本文档定义了部署发布阶段的标准操作流程、质量检查标准和工作产出规范。部署发布是将测试通过的软件安全、可靠地部署到目标环境的过程，需要确保服务连续性、数据完整性和系统稳定性。

### Business Value

- **保证服务连续性**: 通过零停机或最短停机时间的部署策略，确保用户服务不中断
- **降低部署风险**: 完善的回滚机制和灰度发布策略，快速应对异常情况
- **提升部署效率**: 自动化部署流程和标准化操作，减少人工干预和错误
- **增强可追溯性**: 完整的部署记录和监控数据，便于问题定位和事后分析
- **支持业务敏捷**: 快速可靠的部署能力，加速产品迭代和功能上线

## Investigation Flow

### 流程概览

```
发布确认 → 环境准备 → 部署执行 → 验证检查 → 监控配置 → Handover交接
```

---

### Step 1: 发布确认和计划制定

**目的**: 确认发布范围、获得授权、制定详细计划

**输入**:
- 测试报告 (verify-test 场景输出)
- 发布版本号 (release_version)
- 发布范围说明 (release_scope)
- 目标环境 (target_environment)

**操作**:

1. **检查前置条件**
   - 确认测试报告已通过，无P0/P1级别缺陷
   - 确认发布已获得产品经理和技术负责人批准（签字或邮件确认）
   - 确认回滚方案已准备并测试验证
   - 确认发布时间窗口合适（低峰期或维护窗口）

2. **确认发布范围**
   - 记录版本号（语义化版本格式，如v1.2.3）
   - 整理变更清单：
     - 新功能列表
     - Bug修复列表
     - 性能优化项
     - 配置变更项
   - 明确目标环境（prod/staging/dev）
   - 确定发布时间（具体日期和时间）

3. **选择部署策略**
   - **蓝绿部署**: 零停机，适合关键业务，需要双倍资源
   - **滚动部署**: 逐步替换实例，资源利用率高，有短暂降级
   - **灰度发布**: 小流量验证，风险最低，适合大规模系统
   - **直接部署**: 快速但风险高，仅用于非关键环境
   - 选择标准：
     - 业务连续性要求（是否允许停机）
     - 风险等级（新功能稳定性、历史部署成功率）
     - 基础设施支持（是否有足够资源）
     - 停机容忍度（业务方可接受的最长停机时间）

4. **制定详细计划**
   - 部署步骤分解：
     - 每步操作描述
     - 预计执行时间
     - 责任人
     - 验证点
   - 回滚触发条件：
     - 错误率 > 0.1% 持续5分钟
     - P95响应时间 > SLA阈值（如500ms）
     - 健康检查失败
     - 核心功能不可用
   - 沟通计划：
     - 通知对象（产品、运营、客服、管理层）
     - 通知渠道（Slack、邮件、电话）
     - 通知时机（部署前24小时、部署前1小时、部署开始、部署完成）

**输出**: 
- 发布确认清单
- 部署计划文档

---

### Step 2: 环境检查和资源准备

**目的**: 确保目标环境就绪，资源配置充足

**输入**:
- 部署计划文档
- 部署配置 (deployment_config)
- 目标环境信息

**操作**:

1. **环境检查**
   - 服务器状态检查：
     - CPU使用率（应 < 70%）
     - 内存使用率（应 < 80%）
     - 磁盘空间（应有足够空间存放新版本和日志）
     - 磁盘IOPS（应满足应用需求）
   - 网络连通性检查：
     - 内网连通性（应用服务器之间）
     - 外网连通性（第三方API调用）
     - DNS解析（域名解析正确）
     - 防火墙规则（端口开放、IP白名单）
   - 依赖服务健康状态检查：
     - 数据库（连接正常、主从同步正常）
     - 缓存（Redis/Memcached连接正常）
     - 消息队列（Kafka/RabbitMQ连接正常）
     - 第三方API（支付网关、短信服务等）

2. **资源评估**
   - 计算资源评估：
     - CPU核心数是否充足
     - 内存容量是否充足
     - 是否需要临时扩容（部署期间增加实例数）
   - 存储资源评估：
     - 磁盘空间是否充足（应用、日志、临时文件）
     - IOPS是否满足需求（数据库、文件读写）
   - 网络带宽评估：
     - 入口带宽是否充足（用户请求）
     - 出口带宽是否充足（API响应、文件下载）

3. **配置准备**
   - 环境变量配置：
     - 数据库连接字符串
     - API密钥和令牌
     - 功能开关（Feature Flags）
     - 日志级别
   - 配置文件更新：
     - application.yml / application.properties
     - nginx.conf / apache.conf
     - docker-compose.yml / kubernetes manifests
   - 敏感信息处理：
     - 使用Vault或Secrets Manager管理敏感信息
     - 避免在代码或配置文件中硬编码密码
   - 配置差异对比：
     - 对比当前版本和新版本的配置变更
     - 确认配置变更符合预期

4. **备份准备**
   - 数据库备份：
     - 执行全量备份或增量备份
     - 记录备份时间和位置
     - 验证备份可用性（测试恢复流程）
   - 配置文件备份：
     - 备份当前版本的配置文件
     - 记录配置文件的SHA256校验和
   - 应用备份：
     - 保留上一版本的制品（Docker镜像、JAR包等）
     - 记录版本号和校验和

**输出**: 
- 环境准备报告
- 备份记录

---

### Step 3: 部署执行和实时监控

**目的**: 按计划执行部署，实时监控状态，及时处理异常

**输入**:
- 部署计划文档
- 部署脚本
- 部署包 (release_package)

**操作**:

1. **执行前最后检查**
   - 确认人员就位：
     - 开发工程师（负责代码问题）
     - 运维工程师（负责基础设施问题）
     - DBA（负责数据库问题）
   - 确认通知已发送：
     - 产品经理
     - 运营团队
     - 客服团队
     - 管理层
   - 确认回滚方案就绪：
     - 回滚脚本已准备
     - 回滚数据已备份
     - 回滚流程已演练
   - 确认监控告警已启用：
     - Prometheus/Grafana监控正常
     - AlertManager告警规则已加载
     - 通知渠道（Slack、邮件、短信）正常

2. **按步骤执行部署**
   - 上传部署包：
     - 上传到目标服务器或容器仓库
     - 验证文件完整性（MD5/SHA256校验）
   - 执行部署脚本：
     - 停止旧版本服务（优雅停机，等待请求处理完成）
     - 启动新版本服务
     - 等待服务启动完成
   - 健康检查：
     - 检查存活探针（Liveness Probe）
     - 检查就绪探针（Readiness Probe）
     - 检查启动探针（Startup Probe，如配置）
   - 执行冒烟测试：
     - 验证核心功能是否正常
     - 验证API接口是否可用
     - 验证用户界面是否可访问

3. **实时监控状态**
   - 监控服务状态：
     - 实例数是否符合预期
     - 重启次数（异常重启可能表示问题）
     - 健康状态（Healthy/Unhealthy）
   - 监控资源使用：
     - CPU使用率（应 < 80%）
     - 内存使用率（应 < 90%）
     - 磁盘IO（读写延迟、IOPS）
     - 网络流量（入站/出站带宽）
   - 监控应用指标：
     - 响应时间（平均、P50、P95、P99）
     - 吞吐量（请求数/秒）
     - 错误率（错误请求数/总请求数）
   - 监控日志输出：
     - 错误日志（ERROR级别）
     - 异常堆栈（Exception Stack Trace）
     - 警告日志（WARN级别，可能预示问题）

4. **异常处理**
   - 如检测到异常，立即分析原因：
     - 查看日志定位问题
     - 检查监控指标趋势
     - 联系相关工程师协助
   - IF 可快速修复（<5分钟）THEN：
     - 尝试修复并重试部署
     - 最多重试2次
   - ELSE：
     - 立即执行回滚
     - 恢复到上一稳定版本
     - 验证回滚后系统正常
   - 记录详细的异常信息和处理过程

**输出**: 
- 部署执行日志
- 实时监控快照

---

### Step 4: 部署后验证

**目的**: 全面验证部署结果，确保功能和性能符合预期

**输入**:
- 部署执行日志
- 健康检查URL (health_check_url)
- 冒烟测试用例 (smoke_tests)

**操作**:

1. **功能验证**
   - 执行冒烟测试：
     - 验证核心业务流程（如用户登录、下单、支付）
     - 验证关键API接口（返回正确的数据和状态码）
     - 验证用户界面（页面加载正常、交互流畅）
   - 执行回归测试：
     - 运行自动化回归测试套件
     - 确保未引入回归问题
     - 重点关注受变更影响的模块
   - 验证用户界面和交互：
     - UI测试（页面布局、样式、响应式设计）
     - 端到端测试（完整用户旅程）
     - 跨浏览器测试（Chrome、Firefox、Safari、Edge）
   - 验证API接口：
     - 接口契约测试（请求/响应格式符合规范）
     - 集成测试（与依赖服务的交互）
     - 性能测试（API响应时间、吞吐量）

2. **性能验证**
   - 对比部署前后的性能基线：
     - 响应时间（应在基线±10%范围内）
     - 吞吐量（不应显著下降）
     - 错误率（应 < 0.1%）
   - 执行压力测试：
     - 模拟高并发场景
     - 观察系统表现（响应时间、错误率、资源使用）
     - 识别性能瓶颈
   - 检查资源使用：
     - CPU使用率是否正常
     - 内存使用是否正常（无内存泄漏）
     - 磁盘IO是否正常
   - 识别性能瓶颈：
     - 应用层瓶颈（代码效率、算法复杂度）
     - 数据库瓶颈（慢查询、索引缺失）
     - 网络瓶颈（带宽限制、延迟高）
     - 缓存瓶颈（缓存命中率低）

3. **集成验证**
   - 验证与依赖服务的集成：
     - 数据库连接和操作正常
     - 缓存读写正常
     - 消息队列生产和消费正常
   - 验证与第三方服务的集成：
     - 支付网关调用正常
     - 短信服务发送正常
     - 邮件服务发送正常
   - 验证数据流：
     - 数据采集正常
     - 数据处理正常
     - 数据存储正常

4. **数据验证**
   - 验证数据完整性：
     - 无数据丢失或损坏
     - 数据迁移成功（如执行了数据库迁移）
   - 验证数据一致性：
     - 主从同步正常（数据库主从复制）
     - 缓存一致性（缓存与数据库数据一致）
   - 验证数据库迁移：
     - 表结构变更成功
     - 数据迁移成功
     - 索引创建成功
   - 验证关键业务数据：
     - 订单数据完整
     - 用户数据完整
     - 库存数据准确

**输出**: 
- 部署验证报告

---

### Step 5: 监控配置和告警设置

**目的**: 配置完善的监控和告警，确保持续监控系统状态

**输入**:
- 部署验证报告
- 监控系统配置模板

**操作**:

1. **监控指标配置**
   - 基础设施监控：
     - CPU使用率（%）
     - 内存使用率（%）
     - 磁盘使用率（%）
     - 网络流量（入站/出站，Mbps）
     - 磁盘IOPS（读写操作数/秒）
   - 应用性能监控：
     - 响应时间（平均、P50、P95、P99，ms）
     - 吞吐量（请求数/秒）
     - 错误率（错误请求数/总请求数，%）
     - 活跃连接数
     - JVM GC次数和时间（Java应用）
   - 业务指标监控：
     - 订单量（订单数/分钟）
     - 用户活跃度（在线用户数、DAU、MAU）
     - 转化率（注册转化率、购买转化率）
     - 收入（GMV、ARPU）
   - 自定义指标：
     - 业务特定的关键指标
     - 新功能的使用情况

2. **告警规则设置**
   - 错误率告警：
     - 条件：错误率 > 0.1% 持续5分钟
     - 级别：P1
     - 通知：Slack + 邮件
   - 响应时间告警：
     - 条件：P95响应时间 > SLA阈值（如500ms）持续5分钟
     - 级别：P1
     - 通知：Slack + 邮件
   - 资源使用告警：
     - 条件：CPU > 80% 或 内存 > 90% 持续10分钟
     - 级别：P2
     - 通知：邮件
   - 服务可用性告警：
     - 条件：健康检查失败
     - 级别：P0
     - 通知：电话 + Slack + 邮件
   - 业务指标告警：
     - 条件：订单量下降 > 20% 持续15分钟
     - 级别：P1
     - 通知：Slack + 邮件

3. **告警通知配置**
   - 通知渠道：
     - Slack（实时通知，适合P0/P1）
     - 邮件（详细报告，适合所有级别）
     - 短信/电话（紧急情况，适合P0）
   - 通知对象：
     - on-call工程师（第一响应人）
     - 技术负责人（升级联系人）
     - 值班经理（业务影响评估）
   - 告警分级：
     - P0：立即电话通知，5分钟内响应
     - P1：Slack + 邮件，15分钟内响应
     - P2：邮件，1小时内响应
     - P3：邮件，下一个工作日处理
   - 告警抑制：
     - 避免告警风暴（同一问题重复告警）
     - 设置静默期（维护窗口期间暂停告警）
     - 告警聚合（相关问题合并为一条告警）

4. **监控面板创建**
   - 创建部署专用监控面板：
     - 使用Grafana、Datadog等工具
     - 展示关键指标趋势
     - 设置自动刷新（每30秒或1分钟）
   - 展示内容：
     - 响应时间趋势图
     - 错误率趋势图
     - 资源使用趋势图（CPU、内存）
     - 业务指标趋势图（订单量、用户数）
   - 分享监控面板：
     - 生成共享链接
     - 发送给相关干系人
     - 添加到团队Wiki

**输出**: 
- 监控配置文件
- 监控面板链接

---

### Step 6: Handover Context生成和交接

**目的**: 生成完整的Handover Context，便于运维监控阶段顺利接手

**输入**:
- 所有交付物（部署日志、验证报告、监控配置等）

**操作**:

1. **收集所有交付物**
   - 部署执行日志 (logs/deployment-log.md)
   - 部署验证报告 (reports/verification-report.md)
   - 监控配置文件 (monitoring/alerts.yaml)
   - 发布总结报告 (docs/release-report.md)
   - 回滚方案文档 (docs/rollback-plan.md)

2. **填写Handover Context模板**
   ```yaml
   handover:
     header:
       from_stage: "deployment"
       to_stage: "monitoring-operations"
       handover_id: "HO-{{timestamp}}-{{sequence}}"
       timestamp: "{{ISO8601}}"
       prepared_by: "{{agent.name}}"
       
     summary:
       status: "success/partial/failed_rolled_back"
       completion_percentage: {{0-100}}
       quality_score: {{0-100}}
       deployment_duration: "{{duration}}"
       downtime: "{{duration_or_zero}}"
       deployment_strategy: "blue-green/rolling/canary/direct"
       
     artifacts:
       delivered:
         - name: "Release Package"
           path: "registry/releases/{version}"
           version: "{release_version}"
           checksum: "{{SHA256}}"
         # ... 其他交付物
         
     decisions:
       - id: "DC-002"
         description: "部署策略选择"
         rationale: "选择蓝绿部署以最小化停机时间"
         
     open_issues:
       blocking: []
       non_blocking:
         - id: "ISSUE-001"
           description: "非核心功能X存在小问题，计划下版本修复"
           
     risks:
       - id: "RISK-001"
         description: "新版本依赖的中间件版本较新，需密切监控"
         probability: "low"
         impact: "medium"
         mitigation: "已在测试环境充分验证，生产环境加强监控"
         
     recommendations:
       - "前24小时密切监控错误率和响应时间"
       - "关注数据库性能，必要时优化慢查询"
       
     quality_metrics:
       kpi_results:
         - kpi_id: "KPI-001"
           name: "DEPLOY-SUCCESS-RATE"
           value: 100
           target: 99
           unit: "%"
           status: "pass"
       overall_score: 100
       grade: "excellent"
       
     next_steps:
       immediate:
         - "Monitor Operate Agent开始持续监控（至少24小时）"
       short_term:
         - "24小时后编写部署回顾报告"
       long_term:
         - "分析部署数据，识别改进机会"
   ```

3. **更新Global Context**
   - 发布状态（success/partial/failed_rolled_back）
   - 监控重点（需要特别关注的指标和问题）
   - 应急联系人（技术负责人、DBA、运维值班）

4. **通知Monitor Operate Agent**
   - 发送Handover Context
   - 确认接收并开始持续监控
   - 约定监控周期（至少24小时）

**输出**: 
- Handover Context（YAML格式）
- Global Context更新记录

## What To Check

### 必检项 (Mandatory Checks)

| 检查项 | 标准 | 检查方法 | 通过条件 |
|--------|------|----------|----------|
| 回滚方案 | 有可执行的回滚方案且已测试 | 回滚演练记录检查 | 演练成功，回滚时间≤15分钟 |
| 测试报告 | 测试通过，无P0/P1缺陷 | 测试报告审查 | 测试通过率≥90%，无阻塞缺陷 |
| 发布授权 | 获得产品经理和技术负责人批准 | 审批记录检查 | 有签字或邮件确认 |
| 环境就绪 | 目标环境检查全部通过 | 环境检查报告 | 所有检查项通过 |
| 监控配置 | 监控告警已配置并测试 | 监控系统检查 | 告警规则已加载，通知渠道正常 |
| 备份完成 | 关键数据已备份且可用 | 备份验证 | 备份文件存在，测试恢复成功 |

### 建议检查项 (Recommended Checks)

| 检查项 | 标准 | 检查方法 | 通过条件 |
|--------|------|----------|----------|
| 资源充足 | 部署资源充足或有扩容计划 | 资源评估报告 | 资源使用率 < 80% 或有扩容方案 |
| 时间合理 | 部署时间窗口合理 | 发布计划检查 | 在低峰期或维护窗口 |
| 通知到位 | 相关人员已通知 | 通知记录检查 | 100% 通知对象已收到通知 |
| 文档完整 | 部署文档完整 | 文档清单检查 | 所有必需文档已准备 |

## Quality Criteria

### 质量维度

| 维度 | 要求 | 权重 | 评分标准 |
|------|------|------|----------|
| 部署安全 | 过程安全可控，无数据丢失 | 30% | 100%安全: 30分; 有小问题: 20分; 有严重问题: 0分 |
| 回滚能力 | 可快速回滚（≤15分钟） | 25% | ≤15min: 25分; 15-30min: 15分; >30min: 0分 |
| 验证完整 | 验证覆盖全面，无遗漏 | 25% | 100%覆盖: 25分; 90-99%: 20分; <90%: 0分 |
| 文档完整 | 文档归档完整，可追溯 | 20% | 100%完整: 20分; 90-99%: 15分; <90%: 0分 |

### 质量等级

| 等级 | 分数范围 | 说明 |
|------|----------|------|
| 卓越 (Excellent) | 95-100分 | 所有KPIs超标，部署质量极高 |
| 优秀 (Good) | 85-94分 | 所有KPIs达标，部署质量良好 |
| 合格 (Fair) | 70-84分 | 基本KPIs达标，存在改进空间 |
| 不合格 (Poor) | <70分 | 关键KPIs未达标，需要返工 |

## Output Specification

### 产出清单

| 产出 | 格式 | 必填 | 描述 | 位置 |
|------|------|------|------|------|
| 部署执行日志 | Markdown/YAML | 是 | 每步执行结果、时间戳、状态 | logs/deployment-log.md |
| 健康检查结果 | Table/JSON | 是 | 所有端点的检查结果 | reports/health-check-results.json |
| 部署验证报告 | Markdown | 是 | 功能、性能、集成、数据验证结果 | reports/verification-report.md |
| 监控配置文件 | YAML/JSON | 是 | 告警规则和监控面板配置 | monitoring/alerts.yaml |
| 发布总结报告 | Markdown | 是 | 部署总结、质量评估、建议 | docs/release-report.md |
| Handover Context | YAML | 是 | 交接给下一阶段的完整上下文 | contexts/handover-{timestamp}.yaml |

### 输出格式要求

#### 部署执行日志格式
```markdown
## Deployment Execution Log

### Step 1: Upload Deployment Package
- **Start Time**: {timestamp}
- **End Time**: {timestamp}
- **Status**: Success/Failed
- **Details**: 
  - Package: {package_name}
  - Checksum: {SHA256}
  - Upload Location: {path}
- **Logs**: 
  ```
  {log_snippet}
  ```

### Step 2: Stop Old Version
...

### Step 3: Start New Version
...

### Step 4: Health Check
...
```

#### 部署验证报告格式
```markdown
# Deployment Verification Report

## 1. Functional Verification
- Smoke Tests: {passed}/{total}
- Regression Tests: {passed}/{total}
- UI Tests: {passed}/{total}
- API Tests: {passed}/{total}

## 2. Performance Verification
- Response Time: {avg_ms} (baseline: {baseline_ms})
- Throughput: {req_per_sec} (baseline: {baseline_req_per_sec})
- Error Rate: {percentage}% (baseline: {baseline_percentage}%)

## 3. Integration Verification
- Database: Pass/Fail
- Cache: Pass/Fail
- Message Queue: Pass/Fail
- Third-party APIs: Pass/Fail

## 4. Data Verification
- Data Integrity: Pass/Fail
- Data Consistency: Pass/Fail
- Migration Success: Pass/Fail

## 5. Conclusion
- Overall Status: Pass/Fail
- Issues Found: {list}
- Recommendations: {list}
```

## Related Assets (关联资产)

| Asset Type | Path | Description |
|------------|------|-------------|
| Scenario | `../../scenarios/deploy-release/SCENARIO.md` | 部署发布场景定义 |
| Agent | `../../agents/deploy-release.agent.md` | 部署发布Agent角色定义 |
| Prompt | `../../prompts/deploy-release.prompt.md` | 部署发布提示词模板 |
| Skill | `../../skills/deploy-release/SKILL.md` | 部署发布技能包 |

## Related Resources (相关资源)

- **Standards**: 
  - [Deployment Best Practices](../standards/deployment-best-practices.md) - 部署最佳实践指南
  - [Rollback Strategy](../standards/rollback-strategy.md) - 回滚策略标准
  - [Health Check Guidelines](../standards/health-check-guidelines.md) - 健康检查指南
  - [Monitoring Standards](../standards/monitoring-standards.md) - 监控配置标准
- **Templates**: 
  - [Deployment Plan Template](../templates/deployment-plan.template.md) - 部署计划模板
  - [Rollback Plan Template](../templates/rollback-plan.template.md) - 回滚方案模板
  - [Release Report Template](../templates/release-report.template.md) - 发布报告模板
  - [Post-Mortem Template](../templates/post-mortem.template.md) - 事故复盘模板
- **Evaluations**: 
  - [Deployment Quality Checklist](../evaluations/deployment-quality-checklist.md) - 部署质量检查清单
  - [Rollback Drill Report](../evaluations/rollback-drill-report.md) - 回滚演练报告
  - [Performance Baseline](../evaluations/performance-baseline.md) - 性能基线报告
