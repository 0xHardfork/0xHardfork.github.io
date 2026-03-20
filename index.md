---
layout: default
title: 0xHardfork - Security Research
---

<div class="terminal-header">
  <span class="terminal-prompt">root@0xhardfork:~#</span>
  <input type="text" id="terminal-input" class="terminal-input" placeholder="Type 'help' or search articles..." autocomplete="off">
  <span class="terminal-cursor" id="terminal-cursor">█</span>
  <div id="autocomplete-menu" class="autocomplete-menu"></div>
</div>

<!-- Matrix Easter Egg Canvas -->
<canvas id="matrix-canvas" class="matrix-canvas"></canvas>


# 0xHardfork Security Lab

> **[CLASSIFIED]** Advanced Security Research & Code Analysis

<div class="ascii-scroll-container">
<div class="ascii-scroll-content">
<pre><code> ___        _   _               _ __           _    
/ _ \__  __| | | | __ _ _ __ __| |/ _| ___  _ __| | __
| | | \ \/ /| |_| |/ _` | '__/ _` | |_ / _ \| '__| |/ /
| |_| |>  < |  _  | (_| | | | (_| |  _| (_) | |  |   < 
\___//_/\_\|_| |_|\__,_|_|  \__,_|_|  \___/|_|  |_|\_\
</code></pre>
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

<script>
// Article Search and Terminal Interaction
(function() {
    const articles = [
        {% for page in site.pages %}{% if page.title %}{title: {{ page.title | jsonify }}, url: {{ page.url | jsonify }}, path: {{ page.path | jsonify }}},{% endif %}{% endfor %}
    ].filter(a => {
        // Exclude 404 pages, README, and other special pages
        const excludePaths = ['404.html', '404.md', 'README.md', 'USAGE.md'];
        const excludeTitles = ['404', 'Page Not Found'];
        return a.title && 
               !excludePaths.some(p => a.path.includes(p)) &&
               !excludeTitles.some(t => a.title.includes(t));
    });
    
    console.log('Total articles loaded:', articles.length);
    console.log('Sample articles:', articles.slice(0, 3));
    
    const terminalInput = document.getElementById('terminal-input');
    const autocompleteMenu = document.getElementById('autocomplete-menu');
    const terminalCursor = document.getElementById('terminal-cursor');
    let selectedIndex = -1, filteredArticles = [];
    
    // Update cursor position to follow input
    function updateCursorPosition() {
        if (!terminalInput || !terminalCursor) return;
        
        const prompt = document.querySelector('.terminal-prompt');
        const promptWidth = prompt ? prompt.offsetWidth+20 : 200;
        const inputValue = terminalInput.value;
        
        // Create temporary span to measure text width
        const tempSpan = document.createElement('span');
        tempSpan.style.font = window.getComputedStyle(terminalInput).font;
        tempSpan.style.visibility = 'hidden';
        tempSpan.style.position = 'absolute';
        tempSpan.textContent = inputValue;
        document.body.appendChild(tempSpan);
        const textWidth = tempSpan.offsetWidth;
        document.body.removeChild(tempSpan);
        
        // Position cursor after prompt + input text
        terminalCursor.style.left = (promptWidth + textWidth + 10) + 'px';
        terminalCursor.style.display = 'inline';
    }
    
    function searchArticles(query) {
        if (!query) return [];
        query = query.toLowerCase();
        const results = articles.filter(a => a.title.toLowerCase().includes(query) || a.path.toLowerCase().includes(query));
        console.log('Search query:', query, 'Results:', results.length);
        return results;
    }
    
    function showAutocomplete(results) {
        if (results.length === 0) { autocompleteMenu.classList.remove('show'); return; }
        autocompleteMenu.innerHTML = results.map((a, i) => `<div class="autocomplete-item" data-index="${i}"><div class="article-title">${a.title}</div><div class="article-path">${a.path}</div></div>`).join('');
        autocompleteMenu.classList.add('show');
        selectedIndex = -1;
    }
    
    function handleCommand(cmd) {
        cmd = cmd.trim().toLowerCase();
        if (cmd === 'run') { startMatrixRain(); terminalInput.value = ''; autocompleteMenu.classList.remove('show'); updateCursorPosition(); }
        else if (cmd === 'help') { alert('Commands:\n- Type to search articles\n- "run" - Matrix Easter Egg\n- "clear" - Clear input'); terminalInput.value = ''; updateCursorPosition(); }
        else if (cmd === 'clear') { terminalInput.value = ''; autocompleteMenu.classList.remove('show'); updateCursorPosition(); }
    }
    
    terminalInput.addEventListener('input', e => { 
        filteredArticles = searchArticles(e.target.value); 
        showAutocomplete(filteredArticles); 
        updateCursorPosition();
    });
    
    terminalInput.addEventListener('keydown', e => {
        const items = autocompleteMenu.querySelectorAll('.autocomplete-item');
        if (e.key === 'ArrowDown') { e.preventDefault(); selectedIndex = Math.min(selectedIndex + 1, items.length - 1); updateSelection(items); }
        else if (e.key === 'ArrowUp') { e.preventDefault(); selectedIndex = Math.max(selectedIndex - 1, -1); updateSelection(items); }
        else if (e.key === 'Enter') { e.preventDefault(); if (selectedIndex >= 0 && filteredArticles[selectedIndex]) window.location.href = filteredArticles[selectedIndex].url; else handleCommand(terminalInput.value); }
        else if (e.key === 'Escape') { autocompleteMenu.classList.remove('show'); selectedIndex = -1; }
    });
    
    function updateSelection(items) { items.forEach((item, i) => { item.classList.toggle('selected', i === selectedIndex); if (i === selectedIndex) item.scrollIntoView({ block: 'nearest' }); }); }
    autocompleteMenu.addEventListener('click', e => { const item = e.target.closest('.autocomplete-item'); if (item && filteredArticles[item.dataset.index]) window.location.href = filteredArticles[item.dataset.index].url; });
    document.addEventListener('click', e => { if (!e.target.closest('.terminal-header')) autocompleteMenu.classList.remove('show'); });
    
    // Initial cursor state
    updateCursorPosition();
})();

function startMatrixRain() {
    const canvas = document.getElementById('matrix-canvas'), ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth; canvas.height = window.innerHeight; canvas.classList.add('active');
    const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$%^&*()_+-=[]{}|;:,.<>?/~'.split('');
    const fontSize = 16, columns = canvas.width / fontSize, drops = Array(Math.floor(columns)).fill(0).map(() => Math.random() * -100);
    
    function draw() {
        ctx.fillStyle = 'rgba(0, 0, 0, 0.05)'; ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = '#0F0'; ctx.font = fontSize + 'px monospace';
        drops.forEach((drop, i) => {
            ctx.fillText(chars[Math.floor(Math.random() * chars.length)], i * fontSize, drop * fontSize);
            if (drop * fontSize > canvas.height && Math.random() > 0.975) drops[i] = 0;
            drops[i]++;
        });
    }
    
    const interval = setInterval(draw, 33);
    function closeMatrix(e) { if (e.type === 'click' || e.key === 'Escape') { canvas.classList.remove('active'); clearInterval(interval); document.removeEventListener('keydown', closeMatrix); canvas.removeEventListener('click', closeMatrix); } }
    document.addEventListener('keydown', closeMatrix); canvas.addEventListener('click', closeMatrix);
}
</script>
