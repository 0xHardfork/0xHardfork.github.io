---
layout: default
title: 0xHardfork - Security Research
---

<div class="terminal-header">
  <span class="terminal-prompt">root@0xhardfork:~#</span> <span class="terminal-cursor">█</span>
</div>

# 0xHardfork Security Lab

> **[CLASSIFIED]** Advanced Security Research & Code Analysis

```
 ___        _   _               _ __           _    
/ _ \__  __| | | | __ _ _ __ __| |/ _| ___  _ __| | __
| | | \ \/ /| |_| |/ _` | '__/ _` | |_ / _ \| '__| |/ /
| |_| |>  < |  _  | (_| | | | (_| |  _| (_) | |  |   < 
\___//_/\_\|_| |_|\__,_|_|  \__,_|_|  \___/|_|  |_|\_\
```

<div class="category-grid">
{% for category in site.data.categories %}
  <div class="category-card {{ category.id }}">
    <div class="card-header">
      <span class="card-icon">{{ category.icon }}</span>
      <h2>{{ category.name }}</h2>
    </div>
    <div class="card-content">
      <p>{{ category.description }}</p>
      {% include category-tree.html category=category %}
    </div>
    <div class="card-footer">
      <a href="{{ category.path | prepend: '/' | relative_url }}" class="btn-enter">[ENTER] →</a>
    </div>
  </div>
{% endfor %}
</div>

<div class="status-bar">
  <span class="status-item">STATUS: <span class="status-active">● ACTIVE</span></span>
  <span class="status-item">THREAT LEVEL: <span class="threat-low">LOW</span></span>
  <span class="status-item">UPTIME: 99.9%</span>
</div>

---

<p class="footer-note">
  <span class="blink">▮</span> System initialized | Last update: {{ site.time | date: "%Y-%m-%d" }} | Maintained by 0xHardfork
</p>
