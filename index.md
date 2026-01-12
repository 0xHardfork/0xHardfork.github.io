---
layout: default
title: 0xHardfork - Security Research
---

<div class="terminal-header">
  <span class="terminal-prompt">root@0xhardfork:~#</span> <span class="terminal-cursor">█</span>
</div>

# 0xHardfork Security Lab

> **[CLASSIFIED]** Advanced Security Research & Code Analysis

<div class="ascii-scroll-container">
<div class="ascii-scroll-content">

```
 ___        _   _               _ __           _    
/ _ \__  __| | | | __ _ _ __ __| |/ _| ___  _ __| | __
| | | \ \/ /| |_| |/ _` | '__/ _` | |_ / _ \| '__| |/ /
| |_| |>  < |  _  | (_| | | | (_| |  _| (_) | |  |   < 
\___//_/\_\|_| |_|\__,_|_|  \__,_|_|  \___/|_|  |_|\_\
```

</div>
</div>

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
      <a href="/{{ category.path }}/" class="btn-enter">[ENTER] →</a>
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

<div class="social-links">
  {% if site.social.github %}
  <a href="{{ site.social.github }}" target="_blank" rel="noopener noreferrer" class="social-link" title="GitHub">
    <svg width="24" height="24" viewBox="0 0 16 16" fill="currentColor">
      <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/>
    </svg>
    GitHub
  </a>
  {% endif %}
  
  {% if site.social.x %}
  <a href="{{ site.social.x }}" target="_blank" rel="noopener noreferrer" class="social-link" title="X (Twitter)">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
      <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
    </svg>
    X
  </a>
  {% endif %}
  
  {% if site.social.email %}
  <a href="{{ site.social.email }}" class="social-link" title="Email">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
      <path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/>
    </svg>
    Email
  </a>
  {% endif %}
</div>

<script>
// Collapsible tree functionality
(function() {
    function initCollapsibleTree() {
        const parentItems = document.querySelectorAll('.topic-list .has-children .parent-item');
        
        parentItems.forEach(function(item) {
            // Remove old listeners by cloning
            const newItem = item.cloneNode(true);
            item.parentNode.replaceChild(newItem, item);
            
            newItem.addEventListener('click', function(e) {
                // Don't prevent default if clicking on a link
                const target = e.target;
                if (target.tagName === 'A' && target.classList.contains('parent-link')) {
                    return; // Allow link to work normally
                }
                
                e.preventDefault();
                const parent = this.parentElement;
                const nestedList = parent.querySelector('.nested-list');
                const icon = this.querySelector('.toggle-icon');
                
                if (nestedList) {
                    if (nestedList.style.display === 'block') {
                        nestedList.style.display = 'none';
                        icon.textContent = '▸';
                        parent.classList.remove('expanded');
                    } else {
                        nestedList.style.display = 'block';
                        icon.textContent = '▾';
                        parent.classList.add('expanded');
                    }
                }
            });
        });
    }
    
    // Initialize on page load
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initCollapsibleTree);
    } else {
        initCollapsibleTree();
    }
})();
</script>
