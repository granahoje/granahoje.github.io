import os
from datetime import datetime

def generate_sitemap():
    base_url = "https://granahoje.github.io"
    artigos_dir = "artigos"
    
    # Páginas principais
    pages = [
        {"url": "/", "priority": "1.0", "changefreq": "daily"},
        {"url": "/blog.html", "priority": "0.8", "changefreq": "daily"},
        {"url": "/about.html", "priority": "0.5", "changefreq": "monthly"},
    ]
    
    # Adicionar artigos
    if os.path.exists(artigos_dir):
        for filename in os.listdir(artigos_dir):
            if filename.endswith(".html"):
                pages.append({
                    "url": f"/artigos/{filename}",
                    "priority": "0.7",
                    "changefreq": "weekly"
                })
    
    # Adicionar calculadoras na raiz
    for filename in os.listdir("."):
        if filename.startswith("calculadora-") and filename.endswith(".html"):
            pages.append({
                "url": f"/{filename}",
                "priority": "0.9",
                "changefreq": "monthly"
            })

    # Gerar XML
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    now = datetime.now().strftime("%Y-%m-%d")
    
    for page in pages:
        full_url = f"{base_url}{page['url']}"
        xml += f'  <url>\n'
        xml += f'    <loc>{full_url}</loc>\n'
        xml += f'    <lastmod>{now}</lastmod>\n'
        xml += f'    <changefreq>{page["changefreq"]}</changefreq>\n'
        xml += f'    <priority>{page["priority"]}</priority>\n'
        xml += f'  </url>\n'
        
    xml += '</urlset>'
    
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(xml)
    print("✅ sitemap.xml atualizado com sucesso!")

if __name__ == "__main__":
    generate_sitemap()
