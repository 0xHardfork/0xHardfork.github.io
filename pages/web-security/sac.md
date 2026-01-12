---
layout: default
title: SAC - 软件成分分析
---

# SAC - 软件成分分析

## 什么是SCA?

SCA (Software Composition Analysis) 用于识别和管理开源组件及其依赖项中的安全风险。

## 为什么需要SCA?

现代应用中，开源组件占比通常超过80%：

```
现代应用 = 自研代码(20%) + 开源组件(80%)
```

## 主要功能

### 1. 依赖发现

识别项目中的所有依赖：
```bash
npm audit
pip-audit
```

### 2. 漏洞检测

检查已知CVE漏洞：
```json
{
  "name": "lodash",
  "version": "4.17.15",
  "vulnerabilities": [
    {
      "cve": "CVE-2020-8203",
      "severity": "high",
      "description": "Prototype Pollution"
    }
  ]
}
```

### 3. 许可证合规

检查开源许可证兼容性。

### 4. 版本管理

推荐安全的版本更新。

## 主流工具

| 工具 | 特点 | 开源 |
|------|------|------|
| Snyk | 开发者友好 | ❌ |
| Black Duck | 企业级 | ❌ |
| OWASP Dependency-Check | 社区活跃 | ✅ |
| Trivy | 容器扫描 | ✅ |

## 实践示例

### package.json扫描

```bash
# 使用npm audit
npm audit --json > audit-report.json

# 自动修复
npm audit fix
```

### 集成到CI/CD

```yaml
name: SCA Scan
on: [push, pull_request]
jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run Trivy
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: 'fs'
          scan-ref: '.'
```

## 最佳实践

1. ✅ **定期扫描** - 自动化SCA扫描
2. ✅ **及时更新** - 修复高危漏洞
3. ✅ **锁定版本** - 使用lock文件
4. ✅ **许可证审查** - 避免法律风险
5. ✅ **最小依赖** - 减少攻击面

---

[← 返回Web安全](./) | [← 返回首页](/)
