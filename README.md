# 0xHardfork Security Lab

> 🔐 Advanced Security Research • Code Analysis • Exploit Development

A dark hacker-themed Jekyll GitHub Pages site for documenting security research and technical knowledge.

## 📚 Content Structure

```
pages/
├── cloud-security/          # 云安全
│   └── container-security/  # 容器安全
│       └── docker.md       # Docker安全
└── web-security/           # Web安全
    ├── iast.md            # 交互式应用安全测试
    ├── sast/              # 静态应用安全测试
    │   ├── codeql.md      # CodeQL
    │   └── llm-sast.md    # 大模型SAST
    └── sac.md             # 软件成分分析
```

## 🎨 Theme Features

- **Dark Hacker Aesthetic**: Pure black background with neon green accents
- **CRT Scanline Effects**: Retro terminal-style visual effects
- **Card-based Navigation**: First-level categories displayed as interactive cards
- **Multi-level Directory Support**: Hierarchical documentation structure
- **Glowing Text Effects**: Animated neon text shadows
- **Responsive Design**: Works on desktop and mobile

## 🚀 Local Preview

```bash
bundle install
bundle exec jekyll serve
```

Visit `http://localhost:4000`

## 📝 Adding Content

**🎯 NEW: 动态目录加载！**

查看 **[USAGE.md](USAGE.md)** 了解如何快速添加新分类和页面。

### 快速添加新分类

1. **编辑 `_data/categories.yml`** - 添加分类配置（5行代码）
2. **创建目录** - `mkdir -p pages/your-category`  
3. **添加内容** - 创建markdown文件
4. **推送代码** - 首页自动生成新卡片！

详细说明见 [USAGE.md](USAGE.md)。

### Create a new page

1. Create a markdown file in the appropriate directory under `pages/`
2. Add YAML front matter:
   ```yaml
   ---
   layout: default
   title: Your Page Title
   ---
   ```
3. Write your content in Markdown
4. Update parent index files to link to your new page

### Directory Structure

- Each directory should have an `index.md` file
- Use relative links for navigation
- Include breadcrumb links (← Back to...)

## 🛠️ Customization

### Modify Theme Colors

Edit `_sass/jekyll-theme-hacker.scss`:
- `$body-background`: Background color
- `$body-foreground`: Text color
- `$header`: Header/title color

### Add New Categories

1. Create a new directory under `pages/`
2. Add an `index.md` file
3. Update `index.md` in the root to include the new category card

## 📄 License

MIT License - See [LICENSE](LICENSE) file

## 💻 Tech Stack

- Jekyll 3.9+
- GitHub Pages
- SCSS/CSS3
- Markdown

---

**Maintained by 0xHardfork** | Last update: 2026-01-12
