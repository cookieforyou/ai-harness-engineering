---
name: migrate-environment
description: "Detailed technical instructions for migrate-environment scenario execution"
applyTo: "scenarios/migrate-environment/**"
phase: operations
type: instruction
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['instruction', 'technical']
---
# Instructions: 环境迁移 (Migrate Environment)

## Migration Type Standards

### 迁移类型对比

| 类型 | 特点 | 停机时间 | 适用场景 |
|------|------|----------|----------|
| 全量迁移 | 一次性迁移 | 长 | 小数据量 |
| 增量迁移 | 分批次迁移 | 短 | 大数据量 |
| 蓝绿部署 | 双环境切换 | 极短 | 生产环境 |
| 滚动迁移 | 逐步迁移 | 无 | 高可用要求 |

## Data Migration Standards

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

## Rollback Standards

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

## Multi-Language Code Examples

### Terraform: 基础设施迁移脚本

```hcl
# main.tf — Terraform 基础设施迁移配置
terraform {
  required_version = ">= 1.6"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.23"
    }
  }

  # 使用 S3 后端存储状态文件（迁移前后需切换 backend）
  backend "s3" {
    bucket = "company-terraform-state"
    key    = "env/production/terraform.tfstate"
    region = "us-east-1"
    encrypt = true
    dynamodb_table = "terraform-locks"
  }
}

# 迁移源环境（旧）
module "source_env" {
  source = "./modules/environment"
  providers = {
    aws = aws.source
  }
  environment = var.source_environment
  vpc_cidr    = var.source_vpc_cidr
  instance_count = var.source_instance_count
}

# 迁移目标环境（新）
module "target_env" {
  source = "./modules/environment"
  providers = {
    aws = aws.target
  }
  environment = var.target_environment
  vpc_cidr    = var.target_vpc_cidr
  instance_count = var.target_instance_count

  # 从源环境导入数据
  source_db_snapshot = module.source_env.db_snapshot_id
  source_config_backup = module.source_env.config_backup_path
}

# 迁移验证
resource "null_resource" "migration_validation" {
  depends_on = [module.target_env]

  provisioner "local-exec" {
    command = <<EOT
      python3 scripts/validate-migration.py \
        --source ${var.source_environment} \
        --target ${var.target_environment} \
        --check-db true \
        --check-config true \
        --check-dns true
    EOT
  }
}
```

```bash
# Terraform 状态迁移脚本
#!/bin/bash
set -euo pipefail

ENVIRONMENT="${1:?Usage: $0 <environment>}"
NEW_REGION="${2:?Usage: $0 <env> <new-region>}"
BACKUP_FILE="terraform-state-backup-${ENVIRONMENT}-$(date +%Y%m%d-%H%M%S).json"

echo "=== Pre-migration Backup ==="
# 备份当前 Terraform 状态
terraform state pull > "${BACKUP_FILE}"
echo "State backed up to ${BACKUP_FILE}"

echo "=== Importing Existing Resources ==="
# 将现有资源导入 Terraform 管理
terraform import module.source_env.aws_instance.app i-1234567890abcdef0
terraform import module.source_env.aws_db_instance.main mydb-instance-id
terraform import module.source_env.aws_s3_bucket.data my-data-bucket

echo "=== State Migration ==="
# 切换 backend 配置到新环境
terraform init -migrate-state \
  -backend-config="bucket=company-terraform-state-new" \
  -backend-config="key=env/${ENVIRONMENT}/terraform.tfstate"

echo "=== Plan Verification ==="
# 验证迁移计划，确保无资源变更
terraform plan -detailed-exitcode
PLAN_EXIT=$?
if [ $PLAN_EXIT -eq 0 ]; then
    echo "SUCCESS: No diff — state migration verified"
elif [ $PLAN_EXIT -eq 2 ]; then
    echo "WARNING: State has changes — review plan output"
    terraform plan -out=tfplan
else
    echo "ERROR: Plan failed"
    exit 1
fi

echo "=== Migration Complete ==="
```

### Java: Spring Profile 切换与环境配置

```java
// ApplicationConfig.java — Spring 多环境配置（迁移用）
package com.company.migration;

import org.springframework.context.annotation.*;
import org.springframework.core.env.Environment;
import org.springframework.jdbc.datasource.DriverManagerDataSource;

import javax.sql.DataSource;

/**
 * Spring 多环境配置管理
 * 用于在环境迁移时平滑切换不同环境的配置
 */
@Configuration
@PropertySources({
    @PropertySource("classpath:application-${spring.profiles.active}.properties"),
    @PropertySource(value = "classpath:application-${spring.profiles.active}-secrets.properties",
                    ignoreResourceNotFound = true)
})
public class ApplicationConfig {

    private final Environment env;

    public ApplicationConfig(Environment env) {
        this.env = env;
    }

    @Bean
    @Profile("source-env")  // 旧环境配置
    public DataSource sourceDataSource() {
        DriverManagerDataSource ds = new DriverManagerDataSource();
        ds.setDriverClassName(env.getProperty("source.db.driver"));
        ds.setUrl(env.getProperty("source.db.url"));
        ds.setUsername(env.getProperty("source.db.username"));
        ds.setPassword(env.getProperty("source.db.password"));
        return ds;
    }

    @Bean
    @Profile("target-env")  // 新环境配置
    public DataSource targetDataSource() {
        DriverManagerDataSource ds = new DriverManagerDataSource();
        ds.setDriverClassName(env.getProperty("target.db.driver"));
        ds.setUrl(env.getProperty("target.db.url"));
        ds.setUsername(env.getProperty("target.db.username"));
        ds.setPassword(env.getProperty("target.db.password"));
        return ds;
    }

    @Bean
    @Profile("migration")  // 迁移过渡期配置（双写模式）
    public DataSource migrationDataSource() {
        // 路由数据源：主写目标库，从读源库
        RoutingDataSource rds = new RoutingDataSource();
        rds.setPrimaryDataSource(targetDataSource());
        rds.setSecondaryDataSource(sourceDataSource());
        rds.setReadOnlyMode(!env.getProperty("migration.cutover.completed", Boolean.class, false));
        return rds;
    }
}
```

```properties
# application-migration.properties — 迁移专用配置
# 数据库连接（双写模式）
migration.cutover.completed=false
migration.validation.interval.ms=5000

# 源环境
source.db.url=jdbc:mysql://old-db.company.com:3306/mydb
source.db.username=app_user_old

# 目标环境
target.db.url=jdbc:mysql://new-db.company.com:3306/mydb
target.db.username=app_user_new

# 功能开关
feature.use-new-cache=false
feature.use-new-queue=false

# 监控配置
migration.metrics.export=true
migration.alert.error-threshold=3
migration.alert.latency-threshold-ms=500
```

```bash
# Java 应用环境切换脚本
#!/bin/bash
# switch-env.sh — Spring 环境切换与验证
set -euo pipefail

APP_NAME="my-service"
OLD_ENV="source-env"
NEW_ENV="target-env"
MIGRATION_ENV="migration"

echo "=== Step 1: Start with migration profile (dual-write mode) ==="
java -jar ${APP_NAME}.jar \
  --spring.profiles.active=${MIGRATION_ENV} \
  --migration.cutover.completed=false

echo "=== Step 2: Verify dual-write consistency ==="
curl -s -f http://localhost:8080/actuator/health
python3 verify-data-consistency.py --source old-db --target new-db

echo "=== Step 3: Cutover to target environment ==="
curl -X POST http://localhost:8080/actuator/migration/cutover
java -jar ${APP_NAME}.jar \
  --spring.profiles.active=${NEW_ENV} \
  --migration.cutover.completed=true

echo "=== Step 4: Verify target environment ==="
curl -f http://localhost:8080/health
java -jar ${APP_NAME}.jar \
  -Dspring.profiles.active=${NEW_ENV} \
  -Dapp.version=$(git rev-parse HEAD)
```

### Go: Kubernetes ConfigMap 迁移

```go
// internal/migration/configmap.go — ConfigMap 迁移器
package migration

import (
	"context"
	"fmt"
	"log"
	"os"
	"path/filepath"
	"time"

	corev1 "k8s.io/api/core/v1"
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/client-go/kubernetes"
	"k8s.io/client-go/tools/clientcmd"
)

// ConfigMapMigrator 用于在 Kubernetes 集群间迁移 ConfigMap
type ConfigMapMigrator struct {
	sourceClient kubernetes.Interface
	targetClient kubernetes.Interface
	namespace    string
}

// NewConfigMapMigrator 创建迁移器实例
func NewConfigMapMigrator(sourceKubeConfig, targetKubeConfig, namespace string) (*ConfigMapMigrator, error) {
	sourceConfig, err := clientcmd.BuildConfigFromFlags("", sourceKubeConfig)
	if err != nil {
		return nil, fmt.Errorf("build source config: %w", err)
	}
	sourceClient, err := kubernetes.NewForConfig(sourceConfig)
	if err != nil {
		return nil, fmt.Errorf("create source client: %w", err)
	}

	targetConfig, err := clientcmd.BuildConfigFromFlags("", targetKubeConfig)
	if err != nil {
		return nil, fmt.Errorf("build target config: %w", err)
	}
	targetClient, err := kubernetes.NewForConfig(targetConfig)
	if err != nil {
		return nil, fmt.Errorf("create target client: %w", err)
	}

	return &ConfigMapMigrator{
		sourceClient: sourceClient,
		targetClient: targetClient,
		namespace:    namespace,
	}, nil
}

// MigrateConfigMap 迁移单个 ConfigMap
func (m *ConfigMapMigrator) MigrateConfigMap(ctx context.Context, name string) error {
	log.Printf("Migrating ConfigMap: %s/%s", m.namespace, name)

	// 从源集群读取
	cm, err := m.sourceClient.CoreV1().ConfigMaps(m.namespace).Get(ctx, name, metav1.GetOptions{})
	if err != nil {
		return fmt.Errorf("get source configmap: %w", err)
	}

	// 清理元数据（不迁移资源版本、UID 等）
	cleanCM := &corev1.ConfigMap{
		ObjectMeta: metav1.ObjectMeta{
			Name:        cm.Name,
			Labels:      cm.Labels,
			Annotations: cm.Annotations,
		},
		Data:       cm.Data,
		BinaryData: cm.BinaryData,
	}

	// 写入目标集群
	_, err = m.targetClient.CoreV1().ConfigMaps(m.namespace).Create(ctx, cleanCM, metav1.CreateOptions{})
	if err != nil {
		// 如果已存在则更新
		existing, getErr := m.targetClient.CoreV1().ConfigMaps(m.namespace).Get(ctx, name, metav1.GetOptions{})
		if getErr != nil {
			return fmt.Errorf("check target configmap: %w (create: %v)", getErr, err)
		}
		cleanCM.ResourceVersion = existing.ResourceVersion
		_, updateErr := m.targetClient.CoreV1().ConfigMaps(m.namespace).Update(ctx, cleanCM, metav1.UpdateOptions{})
		if updateErr != nil {
			return fmt.Errorf("update target configmap: %w", updateErr)
		}
	}

	log.Printf("ConfigMap migrated successfully: %s", name)
	return nil
}

// BatchMigrate 批量迁移所有 ConfigMap
func (m *ConfigMapMigrator) BatchMigrate(ctx context.Context, labelSelector string) (int, error) {
	list, err := m.sourceClient.CoreV1().ConfigMaps(m.namespace).List(ctx, metav1.ListOptions{
		LabelSelector: labelSelector,
	})
	if err != nil {
		return 0, fmt.Errorf("list source configmaps: %w", err)
	}

	migrated := 0
	for _, cm := range list.Items {
		if err := m.MigrateConfigMap(ctx, cm.Name); err != nil {
			log.Printf("ERROR migrating %s: %v", cm.Name, err)
			continue
		}
		migrated++
	}

	return migrated, nil
}
```

### JavaScript: 环境变量迁移工具

```javascript
#!/usr/bin/env node
/**
 * env-migrator.js — 环境变量迁移同步工具
 * 在源环境和目标环境之间同步环境变量配置
 */
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

class EnvironmentMigrator {
  constructor({ sourceEnv, targetEnv, configDir = './config' }) {
    this.sourceEnv = sourceEnv;
    this.targetEnv = targetEnv;
    this.configDir = configDir;
    this.diffLog = [];
  }

  /**
   * 加载环境变量文件
   */
  loadEnvFile(env) {
    const envPath = path.join(this.configDir, `.env.${env}`);
    if (!fs.existsSync(envPath)) {
      throw new Error(`Environment file not found: ${envPath}`);
    }

    const content = fs.readFileSync(envPath, 'utf-8');
    const vars = {};

    for (const line of content.split('\n')) {
      const trimmed = line.trim();
      if (!trimmed || trimmed.startsWith('#')) continue;

      const eqIndex = trimmed.indexOf('=');
      if (eqIndex === -1) continue;

      const key = trimmed.slice(0, eqIndex).trim();
      let value = trimmed.slice(eqIndex + 1).trim();

      // Remove surrounding quotes if present
      if ((value.startsWith('"') && value.endsWith('"')) ||
          (value.startsWith("'") && value.endsWith("'"))) {
        value = value.slice(1, -1);
      }

      vars[key] = value;
    }

    return vars;
  }

  /**
   * 对比两个环境的变量差异
   */
  diff(source, target) {
    const added = {};
    const removed = {};
    const changed = {};

    for (const [key, value] of Object.entries(source)) {
      if (!(key in target)) {
        removed[key] = value;
      } else if (target[key] !== value) {
        changed[key] = { from: value, to: target[key] };
      }
    }

    for (const [key, value] of Object.entries(target)) {
      if (!(key in source)) {
        added[key] = value;
      }
    }

    return { added, removed, changed };
  }

  /**
   * 同步环境变量
   */
  sync(dryRun = true) {
    console.log(`\n=== Environment Migration: ${this.sourceEnv} -> ${this.targetEnv} ===\n`);

    const sourceVars = this.loadEnvFile(this.sourceEnv);
    const targetVars = this.loadEnvFile(this.targetEnv);

    console.log(`Source (${this.sourceEnv}): ${Object.keys(sourceVars).length} variables`);
    console.log(`Target (${this.targetEnv}): ${Object.keys(targetVars).length} variables`);

    const diffResult = this.diff(sourceVars, targetVars);
    const totalChanges = Object.keys(diffResult.added).length +
                         Object.keys(diffResult.removed).length +
                         Object.keys(diffResult.changed).length;

    if (totalChanges === 0) {
      console.log('\nNo differences found — environments are in sync.');
      return;
    }

    console.log(`\nChanges detected: ${totalChanges}`);
    console.log(`  Added:   ${Object.keys(diffResult.added).length}`);
    console.log(`  Removed: ${Object.keys(diffResult.removed).length}`);
    console.log(`  Changed: ${Object.keys(diffResult.changed).length}`);

    if (Object.keys(diffResult.changed).length > 0) {
      console.log('\nChanged variables (sensitive values masked):');
      for (const [key, value] of Object.entries(diffResult.changed)) {
        const isSecret = key.toLowerCase().includes('secret') ||
                        key.toLowerCase().includes('token') ||
                        key.toLowerCase().includes('password');
        const oldVal = isSecret ? '***' : value.from;
        const newVal = isSecret ? '***' : value.to;
        console.log(`  ${key}: ${oldVal} -> ${newVal}`);
      }
    }

    if (dryRun) {
      console.log('\n[DRY RUN] No changes applied. Use --apply to execute.');
      return;
    }

    // 生成迁移脚本
    const migrationScript = this.generateMigrationScript(diffResult);
    const scriptPath = path.join(this.configDir, `migrate-${this.sourceEnv}-to-${this.targetEnv}.sh`);
    fs.writeFileSync(scriptPath, migrationScript, 'utf-8');
    fs.chmodSync(scriptPath, '755');

    console.log(`\nMigration script generated: ${scriptPath}`);
  }

  generateMigrationScript(diffResult) {
    const lines = [
      '#!/bin/bash',
      `# Auto-generated migration script: ${this.sourceEnv} -> ${this.targetEnv}`,
      `# Generated: ${new Date().toISOString()}`,
      '',
      'set -euo pipefail',
      '',
    ];

    for (const [key, value] of Object.entries(diffResult.added)) {
      lines.push(`export ${key}="${value.replace(/"/g, '\\"')}"`);
    }

    for (const [key] of Object.entries(diffResult.removed)) {
      lines.push(`unset ${key}`);
    }

    for (const [key, value] of Object.entries(diffResult.changed)) {
      lines.push(`export ${key}="${value.to.replace(/"/g, '\\"')}"`);
    }

    return lines.join('\n');
  }
}

// 命令行接口
if (require.main === module) {
  const args = process.argv.slice(2);
  const sourceEnv = args.find(a => a.startsWith('--source='))?.split('=')[1];
  const targetEnv = args.find(a => a.startsWith('--target='))?.split('=')[1];
  const apply = args.includes('--apply');
  const configDir = args.find(a => a.startsWith('--config='))?.split('=')[1] || './config';

  if (!sourceEnv || !targetEnv) {
    console.error('Usage: env-migrator.js --source=staging --target=production [--apply] [--config=./config]');
    process.exit(1);
  }

  const migrator = new EnvironmentMigrator({ sourceEnv, targetEnv, configDir });
  migrator.sync(!apply);
}
```

```bash
# 使用示例
node env-migrator.js --source=staging --target=production              # 对比差异（DRY RUN）
node env-migrator.js --source=staging --target=production --apply      # 执行迁移
node env-migrator.js --source=staging --target=production --apply --config=./deploy/config
```

## Error Handling

### Error Scenario 1: 迁移后环境不一致 (P1)

**触发条件**: 环境迁移完成后，目标环境与源环境的运行行为存在差异（功能、性能、配置）

**处理流程**:
```
IF 迁移完成后功能验证或监控告警显示环境差异
THEN
  1. 执行配置对比检查：
     - 环境变量：对比 source/target 的 .env 文件差异
     - 配置文件：diff config/application-source.yml config/application-target.yml
     - 基础设施：terraform plan 检查状态漂移
  2. 分析差异范围：
     - 数据库 schema 版本是否一致（Flyway/Liquibase 版本号对比）
     - 中间件版本是否匹配（Redis / Kafka / MySQL 版本）
     - 操作系统/Package 版本是否一致
  3. 生成差异清单并分类：
     - P0: 影响核心业务 → 立即修复
     - P1: 影响非核心功能 → 计划修复
     - P2: 配置风格差异 → 记录文档
  4. 修复配置差异后重新验证
  5. 更新配置基准线文档（Configuration Baseline）
END
```

**降级方案**: 将流量切回源环境，待目标环境修复后重新执行迁移

**升级条件**: 发现超过 10 项核心配置差异，或数据库 schema 不一致

### Error Scenario 2: DNS 传播延迟 (P2)

**触发条件**: 环境切换后，DNS 记录更新未在全球范围内生效，部分用户仍访问旧环境

**处理流程**:
```
IF 流量切换后 DNS 解析结果不一致（TTL 未过期）
THEN
  1. 检查 DNS TTL 配置：
     - 确认迁移前的 TTL 值（建议迁移前 48 小时将 TTL 降至 60s）
     - dig / nslookup 检查当前 DNS 记录
  2. 全球 DNS 传播状态检查：
     - 使用 whatsmyDNS / dnschecker 检查全球解析状态
     - 重点关注主要用户区域的 DNS 服务器
  3. 实施流量转发策略：
     - 在旧环境保留反向代理，将仍指向旧 IP 的请求重定向到新环境
     - 或使用 HTTP 301/302 重定向（短期）
  4. 监控 DNS 传播进度：
     - 每 15 分钟检查一次全球解析状态
     - 监控目标环境流量曲线（确认流量逐步达到预期）
  5. TTL 到期后确认 100% 流量到达新环境
  6. 恢复标准 TTL 值（建议 300s-3600s）
END
```

**降级方案**: 在旧环境保留完整的服务副本，通过 HTTP 重定向或反向代理实现无缝过渡

**升级条件**: DNS 传播超过 48 小时仍未完成，或 >5% 用户仍访问旧环境

### Error Scenario 3: SSL 证书过期 (P1)

**触发条件**: 新环境的 SSL/TLS 证书未提前配置或已过期，导致 HTTPS 访问失败

**处理流程**:
```
IF 迁移后监测到 SSL 握手失败或证书错误
THEN
  1. 检查目标环境的证书状态：
     - openssl s_client -connect new-env.company.com:443 -servername new-env.company.com
     - 确保证书链完整（中间证书未缺失）
     - 检查 SAN（Subject Alternative Names）是否包含所有域名
  2. 如证书过期或缺失：
     - 立即申请或续期证书（Let's Encrypt / 内部 CA / 商业 CA）
     - 确保证书私钥权限正确（600 权限）
  3. 安装证书到正确的存储位置：
     - K8s: kubectl create secret tls tls-cert --cert=fullchain.pem --key=privkey.pem
     - Nginx: 配置 ssl_certificate / ssl_certificate_key 指向正确路径
     - AWS ALB: 在 ACM 中上传/选择证书
  4. 验证证书安装正确：
     - SSL Labs 测试（面向公网）
     - 内部网络测试：openssl s_client 逐跳验证
  5. 清除用户端的证书缓存（建议设置 24h 观察期）
END
```

**降级方案**: 临时将流量切回使用有效证书的旧环境，或使用 HTTP 明文（仅内部网络，需 WAF 保护）

**升级条件**: 证书问题影响生产流量超过 30 分钟，或涉及 EV 证书审核


## Quality Standards

> Acceptance criteria and quality gates for migrate-environment deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | Migration success rate is 98% or higher | Automated check |
| Standard 2 | New environment performance is 95%+ of original | Automated check |
| Standard 3 | Environment cost is within 110% of original budget | Automated check |
## References

- [harness-engineering.md](../standards/harness-engineering.md)
- [output-validation-checklist.md](../evaluations/output-validation-checklist.md)
- [regression-checklist.md](../evaluations/regression-checklist.md)
