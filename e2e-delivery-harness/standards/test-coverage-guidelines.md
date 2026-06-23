---
name: test-coverage-guidelines
description: "测试覆盖率指南标准，定义 Line/Branch/Function/Mutation 覆盖率类型、各模块目标覆盖率、覆盖率报告格式以及 JaCoCo/Coverage.py/Istanbul 工具配置"
type: standard
version: "1.1.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-23
status: active
tags: ['standard', 'testing', 'coverage', 'quality', 'jacoco', 'istanbul']
---

# 测试覆盖率指南标准

## Overview

**Purpose**: Define standardized test coverage targets, measurement types, tooling configuration, and reporting requirements for all projects within the E2E Delivery Harness. This standard ensures consistent quality measurement across the entire codebase and establishes a common vocabulary for coverage-related discussions in code reviews, CI/CD pipelines, and release decisions.

**Scope**: All codebases, modules, and services within the E2E Delivery Harness project, including Java (JVM), Python, and JavaScript/TypeScript components. This standard applies to both new development and existing legacy code undergoing modification.

**Audience**: All developers, QA engineers, CI/CD pipeline maintainers, and technical leads responsible for code quality and release management.

## 覆盖率类型定义

| 类型 | 定义 | 重要性 | 说明 |
|------|------|--------|------|
| Line Coverage | 代码行被执行的比例 | 基础指标 | 反映代码被执行的范围，但无法保证逻辑的完整测试。易受表面覆盖影响，需结合其他指标使用 |
| Branch Coverage | 条件分支（if/switch/三元表达式）被覆盖的比例 | 重要 | 比 Line Coverage 更严格，要求每个布尔分支（true/false）都被测试覆盖。推荐作为主要的质量门禁指标 |
| Function Coverage | 函数/方法被调用的比例 | 基础指标 | 确保所有公开和私有函数都有测试调用。对于检测死代码和未使用的接口尤其有效 |
| Mutation Coverage | 代码变异（更改运算符、反转条件等）后被测试捕获的比率 | 高级指标 | 衡量测试质量而非数量。变异未被杀死 = 测试存在缺口。越高代表测试越有效，能真实反映测试的缺陷检测能力 |

## 各模块目标覆盖率

覆盖率目标按模块类型分级设定。所有目标为最低要求（minimum targets），团队应在实际可行的情况下设定更高目标。新增代码必须比遗留代码执行更严格的标准。

| 模块类型 | 定义 | Line | Branch | Function | Mutation |
|---------|------|------|--------|----------|----------|
| 核心模块 | 核心业务逻辑、支付处理、安全认证、数据处理管道 | >=90% | >=85% | >=95% | >=70% |
| 一般模块 | API层、服务层、通用工具类、中间件 | >=80% | >=75% | >=90% | >=60% |
| 工具/配置 | 工具函数、配置管理、脚本、构建辅助 | >=60% | >=50% | >=80% | N/A |
| 新增代码 | 新提交代码（diff覆盖，PR增量） | >=90% | >=85% | >=95% | - |

**例外处理原则**：
- 对于无法避免的低覆盖率模块，需由技术负责人（Tech Lead）书面豁免并记录原因，豁免有效期为一个季度。
- UI 组件可适当降低 Branch Coverage 要求至 >=60%，但必须保证用户交互路径的完整覆盖。
- 第三方集成代码（Adapter/Proxy 模式）可视集成复杂度降低 5-10% 阈值，但需额外进行集成测试。

## 覆盖率报告格式要求

覆盖率报告必须满足以下格式和存档要求，以确保人类可读性与 CI 自动化解析能力兼备：

1. **统一报告格式**：HTML 报告（人类可读）+ XML 报告（CI 解析）。HTML 报告应包含可视化摘要（图表/着色），XML 报告需遵循 JaCoCo/cobertura/Cobertura 或 lcov 标准 schema。
2. **报告内容**：
   - 整体覆盖率摘要（Line / Branch / Function / Mutation）
   - 按模块、包、或源代码目录的详细覆盖率分解
   - 覆盖率趋势图（可选，推荐在独立 dashboard 中呈现历史走势）
3. **CI 集成**：每次 CI 运行必须生成覆盖率报告并归档为构建产物（artifact），保留周期不少于 30 天。
4. **PR 门禁**：Pull Request 合并前覆盖率不得下降超过 1%（绝对值）。当新增代码覆盖率低于目标值时，PR 将被标记为 Failed。
5. **报告存储路径**：
   - 本地构建：`build/reports/coverage/`（Java/Maven），`coverage/`（Python/JavaScript）
   - CI 构建物：归档至 CI artifact，命名格式 `{project}-{branch}-{build}-coverage`
   - 历史存档：推荐通过 SonarQube 或 Codecov/Coveralls 平台集中管理

## 工具配置指南

### JaCoCo (Java/JVM)

适用于 Maven 项目的推荐配置。`excludes` 用于剔除自动生成类和配置入口，`rules` 定义 CI 门禁的最低通过阈值。

```xml
<plugin>
  <groupId>org.jacoco</groupId>
  <artifactId>jacoco-maven-plugin</artifactId>
  <version>0.8.11</version>
  <executions>
    <execution>
      <id>default-prepare-agent</id>
      <goals><goal>prepare-agent</goal></goals>
    </execution>
    <execution>
      <id>default-report</id>
      <phase>verify</phase>
      <goals><goal>report</goal></goals>
    </execution>
    <execution>
      <id>default-check</id>
      <phase>verify</phase>
      <goals><goal>check</goal></goals>
      <configuration>
        <rules>
          <rule><element>BUNDLE</element><limits>
            <limit><counter>LINE</counter>
                  <value>COVEREDRATIO</value>
                  <minimum>0.80</minimum></limit>
            <limit><counter>BRANCH</counter>
                  <value>COVEREDRATIO</value>
                  <minimum>0.75</minimum></limit>
          </limits></rule>
        </rules>
        <excludes>
          <exclude>**/*Config.*</exclude>
          <exclude>**/*Application.*</exclude>
          <exclude>**/dto/**</exclude>
          <exclude>**/model/**</exclude>
        </excludes>
      </configuration>
    </execution>
  </executions>
</plugin>
```

### Coverage.py (Python)

适用于 pytest + coverage 组合。`source` 限定被测模块范围，`omit` 排除测试代码和框架代码，`fail_under` 设 CI 硬门禁。

```ini
[run]
source = myproject
omit = */tests/*,*/migrations/*,*/setup.py,conftest.py
branch = true

[report]
show_missing = true
fail_under = 80
exclude_lines =
    pragma: no cover
    def __repr__
    def __str__
    raise NotImplementedError
    if __name__ == .__main__.:
```

### Istanbul / NYC (JavaScript / TypeScript)

适用于 Jest / Mocha 配合 nyc 的 JavaScript/TypeScript 项目。`check-coverage` 启用门禁检查。

```json
{
  "nyc": {
    "check-coverage": true,
    "lines": 80,
    "branches": 75,
    "functions": 90,
    "statements": 80,
    "include": ["src/**/*.ts", "src/**/*.js"],
    "exclude": [
      "**/*.test.*",
      "**/node_modules/**",
      "**/dist/**",
      "**/coverage/**"
    ],
    "reporter": ["html", "text", "lcov"],
    "all": true
  }
}
```

## 覆盖率管理最佳实践

1. **不唯数字论**：不要为覆盖率数字而测试。避免表面覆盖（测试执行了代码但无断言）、避免过度 Mock 导致覆盖率虚高。优先关注 Mutation Coverage，它比 Line Coverage 更能反映测试有效性。
2. **优先测试核心逻辑**：将测试资源集中在核心业务逻辑、复杂分支、异步流程和安全关键路径上。简单 Getter/Setter 和配置类可策略性排除。
3. **排除策略**：在覆盖率报告中策略性地排除自动生成代码、配置类、DTO、Plain 数据模型等非逻辑性代码。排除列表应在团队内评审并归档。
4. **趋势追踪**：定期（每月）审查覆盖率趋势。覆盖率长期稳定或上升是健康的信号；突然下降应触发根因分析。推荐使用 SonarQube / Codecov 等平台持续追踪。
5. **CI 集成**：将覆盖率门禁加入 CI Pipeline 的 verify/check 阶段。门禁失败不应阻断本地开发，但必须阻断合并到主干的 PR。
6. **review 同步**：代码审查时将覆盖率变化纳入检查项。Reviewer 应确认新增代码的测试覆盖了正反两个分支。

## 覆盖率反模式

以下反模式描述了常见的覆盖率质量陷阱及其正确做法。开发人员在编写测试和审查 PR 时应主动识别并避免这些模式。

| 反模式 | 表现 | 正确做法 |
|--------|------|---------|
| 表面覆盖 | 测试执行了代码但无断言或断言不足，导致 Branch Coverage 远低于 Line Coverage | 每个测试方法至少有一个明确断言，使用参数化测试覆盖多种输入组合 |
| 过度 Mock | Mock 所有外部依赖导致覆盖率虚高，但实际集成路径未得到验证 | 适当引入集成测试验证真实交互；对边界条件使用 Mock，对核心流程使用真实依赖或 TestContainer |
| 忽略分支 | 只测 Happy Path，Exception / Error / Null / Edge Case 分支均未覆盖 | 使用分支覆盖分析结果逐步补齐缺失分支，优先补充异常路径和边界值 |
| 数字游戏 | 追求 100% Line Coverage 而忽视测试有效性，包含大量无意义测试 | 关注 Mutation Coverage 和测试有效性，以质量和缺陷检出率为第一优先级 |
| 一次性覆盖 | 测试仅为满足 CI 门禁而写，后续重构时测试失效即删除 | 测试即文档。为行为而非实现编写测试，重构时测试应保持有效 |

## Examples

### Good: 高质量的覆盖率报告示例

项目 `payment-service` 的核心模块达到 Line 94%、Branch 88%、Mutation 72%。团队使用参数化测试覆盖了 12 种支付场景的 all 分支，包括成功、余额不足、超时、风控拦截等异常路径。代码变更后 Mutation Coverage 稳定在 70% 以上，表明测试能有效检测逻辑错误。PR 覆盖率 diff 仅下降 0.3%，顺利通过门禁。

### Bad: 虚高的覆盖率报告示例

项目 `user-service` 的 Line Coverage 达 92%，但 Branch Coverage 仅 41%，Mutation Coverage 为 23%。分析发现大部分测试仅调用函数并检查非空返回值，未验证 if/else 分支和异常处理逻辑。新增代码中一个 null 指针判空分支未被覆盖，在预发布环境触发 P0 事故。该项目的测试覆盖率数字虚高，真实测试质量远低于预期。

### Remediation: 低质量覆盖率的修复路径

针对 `user-service` 的问题，团队采取了以下措施：1) 将 Branch Coverage 门禁从 40% 提升至 75%；2) 使用 JaCoCo Branch Coverage 报告识别未覆盖分支；3) 为每个条件分支补充边界值测试用例；4) 引入 Pitest（Mutation Testing）并将 Mutation Coverage 纳入门禁。两个月后 Branch Coverage 提升至 81%，Mutation Coverage 达到 58%。

## Compliance Checklist

- [ ] 核心模块是否达到 Line >=90%、Branch >=85%？
- [ ] 新增代码覆盖率是否 >=90%（diff 覆盖）？
- [ ] CI 流水线是否配置了覆盖率 gate（fail build when below target）？
- [ ] PR 合并前是否确认覆盖率未下降超过 1%（绝对值）？
- [ ] 是否排除了自动生成代码和配置类（策略性排除，有记录）？
- [ ] 覆盖率报告是否包含 HTML 和 XML 两种格式（或等效的 lcov / cobertura 格式）？
- [ ] 是否有针对分支覆盖率的专项测试（Branch Coverage 专项补充）？
- [ ] 是否定期（每月）审查覆盖率趋势并归档趋势报告？

## Related Standards

- [testing-best-practices.md](testing-best-practices.md)
- [test-data-management.md](test-data-management.md)
- [harness-engineering.md](harness-engineering.md)
- [output-quality-rubric.md](output-quality-rubric.md)
- [code-review-checklist.md](code-review-checklist.md)
