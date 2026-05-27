#!/usr/bin/env python3
"""
Script para gerar RSS feed com URLs corretas dos produtos
Inclui todas as páginas de produtos com conteúdo completo
"""

import json
import os
from datetime import datetime
from urllib.parse import urljoin
import html

def load_products():
    """Carregar produtos do arquivo JSON"""
    try:
        with open('radar/data/products.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ Erro: arquivo products.json não encontrado")
        return {'products': [], 'categories': []}

def escape_xml(text):
    """Escapar caracteres especiais para XML"""
    if not text:
        return ""
    return html.escape(str(text))

def generate_rss():
    """Gerar RSS feed com URLs corretas"""
    data = load_products()
    products = data['products']
    
    base_url = "https://granahoje.github.io/radar"
    
    # Iniciar RSS
    rss = '<?xml version="1.0" encoding="UTF-8"?>\n'
    rss += '<rss xmlns:content="http://purl.org/rss/1.0/modules/content/" version="2.0">\n'
    rss += '  <channel>\n'
    rss += f'    <title>Radar Financeiro - Produtos Financeiros</title>\n'
    rss += f'    <link>{base_url}</link>\n'
    rss += f'    <description>Catálogo atualizado de produtos financeiros com análises profissionais e comparações</description>\n'
    rss += f'    <language>pt-br</language>\n'
    rss += f'    <lastBuildDate>{datetime.now().strftime("%a, %d %b %Y %H:%M:%S +0000")}</lastBuildDate>\n'
    rss += f'    <image>\n'
    rss += f'      <url>{base_url}/icon.png</url>\n'
    rss += f'      <title>Radar Financeiro</title>\n'
    rss += f'      <link>{base_url}</link>\n'
    rss += f'    </image>\n'
    
    print(f"📰 Gerando RSS Feed com {len(products)} produtos...")
    
    # Adicionar cada produto como item
    for product in products:
        product_url = urljoin(base_url, f"/produto/{product['id']}/")
        
        # Criar descrição resumida
        description = f"""<h3>{escape_xml(product['name'])}</h3>
<p><strong>Tipo:</strong> {escape_xml(product['type'])}</p>
<p><strong>Descrição:</strong> {escape_xml(product['description'])}</p>
<p><strong>Pontuação:</strong> {product['score']}%</p>
<p><strong>Avaliação:</strong> {product['rating']}⭐</p>

<h4>Prós:</h4>
<ul>
"""
        
        for pro in product.get('pros', [])[:5]:
            description += f"<li>{escape_xml(pro)}</li>\n"
        
        description += """</ul>

<h4>Contras:</h4>
<ul>
"""
        
        for con in product.get('cons', [])[:5]:
            description += f"<li>{escape_xml(con)}</li>\n"
        
        description += f"""</ul>

<p><a href="{escape_xml(product['affiliateLink'])}" target="_blank">Acessar Produto</a></p>
"""
        
        # Item RSS
        rss += f"""  <item>
    <title>{escape_xml(product['name'])} - {product['score']}%</title>
    <link>{product_url}</link>
    <guid>{escape_xml(product['id'])}</guid>
    <category>{escape_xml(product['type'])}</category>
    <pubDate>{datetime.now().strftime("%a, %d %b %Y %H:%M:%S +0000")}</pubDate>
    <description><![CDATA[{description}]]></description>
    <content:encoded><![CDATA[{description}]]></content:encoded>
  </item>
"""
    
    # Fechar RSS
    rss += '  </channel>\n'
    rss += '</rss>'
    
    # Salvar RSS
    rss_path = 'radar/feed.xml'
    with open(rss_path, 'w', encoding='utf-8') as f:
        f.write(rss)
    
    print(f"\n✅ RSS Feed gerado com sucesso!")
    print(f"📊 Total de itens: {len(products)}")
    print(f"📁 Arquivo: {rss_path}")
    print(f"🌐 URL pública: https://granahoje.github.io/radar/feed.xml")

if __name__ == '__main__':
    generate_rss()
