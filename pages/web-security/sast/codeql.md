---
layout: default
title: CodeQL
---

# CodeQL

## 简介

CodeQL是GitHub开发的代码查询语言，用于发现代码中的安全漏洞。

## 核心概念

### 1. 代码数据库

将代码转换为可查询的数据库：
```bash
codeql database create mydb --language=javascript
```

### 2. 查询语言

使用类似SQL的语法查询代码：
```ql
import javascript

from Function f
where f.getName() = "eval"
select f, "Found dangerous eval function"
```

### 3. 查询库

预定义的安全查询集合。

## 实战示例

### 检测SQL注入

```ql
/**
 * @name SQL injection
 * @kind path-problem
 */
import javascript
import DataFlow::PathGraph

class SqlInjectionConfig extends TaintTracking::Configuration {
  SqlInjectionConfig() { this = "SqlInjectionConfig" }
  
  override predicate isSource(DataFlow::Node source) {
    source instanceof RemoteFlowSource
  }
  
  override predicate isSink(DataFlow::Node sink) {
    exists(DatabaseQuery query |
      sink = query.getQuery()
    )
  }
}

from SqlInjectionConfig cfg, DataFlow::PathNode source, DataFlow::PathNode sink
where cfg.hasFlowPath(source, sink)
select sink.getNode(), source, sink, "SQL injection vulnerability"
```

## CI/CD集成

```yaml
name: CodeQL Analysis
on: [push, pull_request]
jobs:
  analyze:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: github/codeql-action/init@v2
      - uses: github/codeql-action/analyze@v2
```

## 学习资源

- [CodeQL官方文档](https://codeql.github.com/docs/)
- [CodeQL查询库](https://github.com/github/codeql)

---

[← 返回SAST](./) | [← 返回Web安全](..) | [← 返回首页](/)
