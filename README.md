# 0xHardfork's Blog

这是使用 Jekyll 搭建的个人技术博客，托管在 GitHub Pages 上。

## 🚀 快速开始

### 前置要求

- Ruby 2.7 或更高版本
- Bundler

### 安装

1. 克隆仓库：
```bash
git clone https://github.com/0xHardfork/0xHardfork.github.io.git
cd 0xHardfork.github.io
```

2. 安装依赖：
```bash
bundle install
```

### 本地预览

运行本地开发服务器：

```bash
bundle exec jekyll serve
```

或者使用实时重载：

```bash
bundle exec jekyll serve --livereload
```

访问 `http://localhost:4000` 查看网站。

## 📝 写作

### 创建新文章

在 `_posts` 目录下创建新的 Markdown 文件，文件名格式为：

```
YYYY-MM-DD-title.md
```

例如：`2026-01-12-my-first-post.md`

### 文章模板

每篇文章需要包含 YAML Front Matter：

```markdown
---
layout: post
title: "你的文章标题"
date: 2026-01-12 20:00:00 +0900
categories: 分类名称
tags: [标签1, 标签2, 标签3]
---

在这里写文章内容...
```

### Markdown 功能

支持所有标准 Markdown 语法，包括：

- **代码高亮**：使用三个反引号 + 语言名称
- **表格**：使用管道符和连字符
- **列表**：有序和无序列表
- **引用**：使用 `>` 符号
- **链接和图片**：标准 Markdown 语法

## 📁 目录结构

```
.
├── _config.yml          # Jekyll 配置文件
├── _posts/              # 博客文章目录
│   └── YYYY-MM-DD-title.md
├── _site/               # 生成的静态网站（自动生成，已忽略）
├── about.md             # 关于页面
├── index.md             # 首页
├── Gemfile              # Ruby 依赖管理
└── README.md            # 本文件
```

## 🎨 自定义

### 修改配置

编辑 `_config.yml` 文件来自定义网站设置：

- `title`: 网站标题
- `description`: 网站描述
- `author`: 作者信息
- `url`: 网站 URL

### 更换主题

默认使用 `minima` 主题。要更换主题，请：

1. 在 `Gemfile` 中添加新主题
2. 在 `_config.yml` 中修改 `theme` 设置
3. 运行 `bundle install`

## 🚢 部署

### GitHub Pages

1. 将代码推送到 GitHub：
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

2. 在 GitHub 仓库设置中：
   - 进入 Settings > Pages
   - Source 选择 `main` 分支
   - 点击 Save

3. GitHub 会自动构建并部署网站到 `https://0xhardfork.github.io`

### 本地构建

生成静态网站文件：

```bash
bundle exec jekyll build
```

生成的文件会在 `_site` 目录中。

## 📚 资源

- [Jekyll 文档](https://jekyllrb.com/docs/)
- [GitHub Pages 文档](https://docs.github.com/en/pages)
- [Markdown 指南](https://www.markdownguide.org/)
- [Liquid 模板语法](https://shopify.github.io/liquid/)

## 📄 许可

MIT License

## 👤 作者

**0xHardfork**

- GitHub: [@0xHardfork](https://github.com/0xHardfork)

---

Happy blogging! 🎉
