# 防密钥泄露指令 / No Secrets Leak Instruction

> 【强制】本指令为所有 Agent 的默认安全护栏，不可绕过。

---

## 绝对禁止的输出内容

Agent 在任何输出（包括日志、报告、调试信息、错误堆栈）中，**绝对禁止**包含以下内容的明文：

1. API Keys（任何前缀如 `sk-`、`AK`、`ghp_` 等）
2. 密码或密码哈希
3. 数据库连接字符串（含用户名密码）
4. 私钥内容（PEM、RSA、SSH 私钥等）
5. OAuth Token / Refresh Token
6. 云服务访问凭证（如 AWS Access Key ID + Secret）

---

## 允许的引用方式

- 使用环境变量名代替真实值：`process.env.OPENAI_API_KEY` ✅
- 使用占位符：`<YOUR_API_KEY_HERE>` ✅
- 仅展示密钥前缀用于识别类型：`sk-...9Zq2`（需截断至不可恢复）✅

---

## 代码审查场景的特殊规则

当审查的代码本身包含硬编码密钥时：
1. 【强制】在审查报告中仅指出位置与风险，**不得复述密钥内容**
2. 正确的 finding message 示例：
   > "文件 `config.js` 第 15 行存在硬编码 API Key，请移至环境变量管理。"
3. 错误的 finding message 示例：
   > "文件 `config.js` 第 15 行的密钥 `sk-live-abc123` 已泄露。" ❌

---

## 检测与熔断

- 系统层已配置正则扫描，一旦检测到疑似密钥输出，立即中断响应并告警
- 该事件将自动计入安全审计日志，并通知安全负责人
