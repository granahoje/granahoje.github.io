import os
from pathlib import Path
from datetime import datetime

root = Path('/home/ubuntu/granahoje.github.io')
base_url = 'https://granahoje.github.io'

def generate_sitemap():
    files = list(root.glob('**/*.html'))
    sitemap_content = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]
    
    today = datetime.now().strftime('%Y-%m-%d')
    
    for f in sorted(files):
        if any(part in {'.git', 'node_modules'} for part in f.parts): continue
        
        rel_path = f.relative_to(root)
        url = f"{base_url}/{rel_path}"
        
        # Otimizar prioridades
        priority = "0.6"
        if f.name == 'index.html': priority = "1.0"
        elif f.parent == root: priority = "0.8"
        elif 'artigos/' in str(rel_path): priority = "0.7"
        
        sitemap_content.append(f"  <url>")
        sitemap_content.append(f"    <loc>{url}</loc>")
        sitemap_content.append(f"    <lastmod>{today}</lastmod>")
        sitemap_content.append(f"    <priority>{priority}</priority>")
        sitemap_content.append(f"  </url>")
        
    sitemap_content.append('</urlset>')
    
    (root / 'sitemap.xml').write_text('\n'.join(sitemap_content), encoding='utf-8')
    print("Sitemap.xml atualizado com sucesso.")

generate_sitemap()
