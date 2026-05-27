#!/usr/bin/env python3
"""
Script para gerar sitemap.xml dinamicamente
Inclui todas as páginas do Radar Financeiro
"""

import json
import os
from datetime import datetime
from urllib.parse import urljoin

def load_products():
    """Carregar produtos do arquivo JSON"""
    try:
        with open('radar/data/products.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ Erro: arquivo products.json não encontrado")
        return {'products': [], 'categories': []}

def generate_sitemap():
    """Gerar sitemap XML"""
    data = load_products()
    products = data['products']
    categories = data['categories']
    
    base_url = "https://granahoje.github.io/radar"
    
    # Iniciar XML
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    # URLs principais
    main_urls = [
        ('/', 1.0, 'daily'),
        ('/comparacao/', 0.9, 'weekly'),
        ('/admin/', 0.5, 'monthly'),
    ]
    
    for path, priority, changefreq in main_urls:
        url = urljoin(base_url, path)
        lastmod = datetime.now().strftime('%Y-%m-%d')
        xml += f'''  <url>
    <loc>{url}</loc>
    <lastmod>{lastmod}</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
  </url>
'''
    
    # URLs de categorias
    for category in categories:
        url = urljoin(base_url, f"/categoria/{category['id']}/")
        lastmod = datetime.now().strftime('%Y-%m-%d')
        xml += f'''  <url>
    <loc>{url}</loc>
    <lastmod>{lastmod}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
'''
    
    # URLs de produtos
    for product in products:
        url = urljoin(base_url, f"/produto/{product['id']}/")
        lastmod = datetime.now().strftime('%Y-%m-%d')
        xml += f'''  <url>
    <loc>{url}</loc>
    <lastmod>{lastmod}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.7</priority>
  </url>
'''
    
    # Fechar XML
    xml += '</urlset>'
    
    # Salvar sitemap
    sitemap_path = 'radar/sitemap.xml'
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(xml)
    
    print(f"✅ Sitemap gerado com sucesso!")
    print(f"📊 Total de URLs: {len(main_urls) + len(categories) + len(products)}")
    print(f"📁 Arquivo: {sitemap_path}")

if __name__ == '__main__':
    generate_sitemap()
