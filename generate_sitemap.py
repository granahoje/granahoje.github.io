#!/usr/bin/env python3
"""
Script para gerar sitemap.xml atualizado com todas as páginas do site,
incluindo as novas calculadoras em todos os idiomas.
"""

import os
from datetime import datetime
from pathlib import Path

def generate_sitemap():
    """Gera o sitemap.xml com todas as páginas."""
    
    base_url = "https://granahoje.github.io"
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Idiomas suportados
    languages = ['', 'en', 'es', 'fr', 'pt-pt', 'ar', 'zh', 'ru', 'hi', 'ja', 'bn']
    
    # Páginas principais
    main_pages = [
        'index.html',
        'blog.html',
        'about.html',
        'contact.html',
        'privacy-policy.html',
        'terms-of-service.html',
        'disclaimer.html',
        'faq.html',
        'calculadora-juros-compostos.html',
    ]
    
    # Coletar todos os artigos
    articles_dir = Path('/home/ubuntu/granahoje.github.io/artigos')
    articles = []
    if articles_dir.exists():
        articles = [f.name for f in articles_dir.glob('*.html')]
    
    # Gerar XML
    xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    # Adicionar páginas principais para cada idioma
    for lang in languages:
        lang_prefix = f"/{lang}" if lang else ""
        
        for page in main_pages:
            url = f"{base_url}{lang_prefix}/{page}" if lang_prefix else f"{base_url}/{page}"
            xml_content += f'  <url>\n'
            xml_content += f'    <loc>{url}</loc>\n'
            xml_content += f'    <lastmod>{today}</lastmod>\n'
            xml_content += f'    <priority>0.8</priority>\n'
            xml_content += f'  </url>\n'
    
    # Adicionar artigos para cada idioma
    for lang in languages:
        lang_prefix = f"/{lang}" if lang else ""
        
        for article in articles:
            url = f"{base_url}{lang_prefix}/artigos/{article}"
            xml_content += f'  <url>\n'
            xml_content += f'    <loc>{url}</loc>\n'
            xml_content += f'    <lastmod>{today}</lastmod>\n'
            xml_content += f'    <priority>0.7</priority>\n'
            xml_content += f'  </url>\n'
    
    xml_content += '</urlset>\n'
    
    # Salvar sitemap
    with open('/home/ubuntu/granahoje.github.io/sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(xml_content)
    
    print(f"✅ Sitemap gerado com sucesso!")
    print(f"📊 Total de URLs: {xml_content.count('<loc>')}")

if __name__ == "__main__":
    generate_sitemap()
