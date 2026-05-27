#!/usr/bin/env python3
"""
Script para gerar sitemap.xml dinamicamente com URLs corretas
Inclui todas as páginas do Radar Financeiro com prioridades apropriadas
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
    """Gerar sitemap XML com URLs corretas"""
    data = load_products()
    products = data['products']
    categories = data['categories']
    
    base_url = "https://granahoje.github.io/radar"
    
    # Iniciar XML com namespace correto
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
    xml += '         xmlns:image="http://www.google.com/schemas/sitemap-image/1.1"\n'
    xml += '         xmlns:mobile="http://www.google.com/schemas/sitemap-mobile/1.0">\n'
    
    # URLs principais com prioridades altas
    main_urls = [
        ('/', 1.0, 'daily'),
        ('/comparacao/', 0.9, 'weekly'),
        ('/admin/', 0.3, 'monthly'),
        ('/feed.xml', 0.8, 'daily'),
    ]
    
    print(f"📊 Gerando Sitemap com {len(main_urls) + len(categories) + len(products)} URLs...")
    
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
    
    # URLs de categorias (se houver rota de categoria)
    for category in categories:
        # Nota: Ajuste conforme sua estrutura de roteamento
        url = urljoin(base_url, f"/categoria/{category['id']}/")
        lastmod = datetime.now().strftime('%Y-%m-%d')
        xml += f'''  <url>
    <loc>{url}</loc>
    <lastmod>{lastmod}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.75</priority>
  </url>
'''
    
    # URLs de produtos - CRÍTICO: Deve corresponder à estrutura real
    for product in products:
        # URL do produto (página estática HTML)
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
    
    total_urls = len(main_urls) + len(categories) + len(products)
    print(f"\n✅ Sitemap gerado com sucesso!")
    print(f"📊 Total de URLs: {total_urls}")
    print(f"   - Páginas principais: {len(main_urls)}")
    print(f"   - Categorias: {len(categories)}")
    print(f"   - Produtos: {len(products)}")
    print(f"📁 Arquivo: {sitemap_path}")
    print(f"🌐 URL pública: https://granahoje.github.io/radar/sitemap.xml")
    
    # Validar sitemap
    validate_sitemap(xml, products)

def validate_sitemap(xml_content, products):
    """Validar integridade do sitemap"""
    print("\n🔍 Validando Sitemap...")
    
    # Verificar que todas as URLs de produtos estão presentes
    for product in products:
        url = f"/produto/{product['id']}/"
        if url not in xml_content:
            print(f"  ⚠️  AVISO: URL do produto {product['id']} não encontrada no sitemap!")
        else:
            print(f"  ✓ {product['name']}: /produto/{product['id']}/")
    
    print("\n✅ Validação concluída!")

if __name__ == '__main__':
    generate_sitemap()
