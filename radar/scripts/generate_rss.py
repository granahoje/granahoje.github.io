#!/usr/bin/env python3
"""
Gerador de RSS Feed para o Radar Financeiro
Permite que agregadores e plataformas consumam o conteúdo automaticamente
"""

import json
import os
from datetime import datetime

def generate_rss_feed():
    """Gerar feed RSS com todos os produtos"""
    
    # Carregar produtos
    try:
        with open('radar/data/products.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("❌ Erro: arquivo products.json não encontrado")
        return False
    
    products = data['products']
    base_url = "https://granahoje.github.io/radar"
    
    # Cabeçalho RSS
    rss_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<rss version="2.0" xmlns:content="http://purl.org/rss/1.0/modules/content/">',
        '  <channel>',
        '    <title>Radar Financeiro - Produtos Financeiros</title>',
        f'    <link>{base_url}</link>',
        '    <description>Catálogo atualizado de produtos financeiros com análises e comparações</description>',
        '    <language>pt-br</language>',
        f'    <lastBuildDate>{datetime.now().strftime("%a, %d %b %Y %H:%M:%S +0000")}</lastBuildDate>',
        '    <image>',
        f'      <url>{base_url}/icon.png</url>',
        '      <title>Radar Financeiro</title>',
        f'      <link>{base_url}</link>',
        '    </image>',
    ]
    
    # Adicionar cada produto como item RSS
    for product in sorted(products, key=lambda x: x['score'], reverse=True)[:50]:
        category = product.get('category', 'geral')
        product_url = f"{base_url}/produto/{product['id']}/"
        
        # Criar lista de prós
        pros_html = '\n'.join([f'        <li>{pro}</li>' for pro in product.get('pros', [])])
        
        # Criar lista de contras
        cons_html = '\n'.join([f'        <li>{con}</li>' for con in product.get('cons', [])])
        
        # Criar descrição HTML
        description = f"""<![CDATA[
        <h3>{product['name']}</h3>
        <p><strong>Tipo:</strong> {product['type']}</p>
        <p><strong>Descrição:</strong> {product['description']}</p>
        <p><strong>Pontuação:</strong> {product['score']}%</p>
        <p><strong>Avaliação:</strong> {product['rating']}⭐</p>
        
        <h4>Prós:</h4>
        <ul>
{pros_html}
        </ul>
        
        <h4>Contras:</h4>
        <ul>
{cons_html}
        </ul>
        
        <p><a href="{product['affiliateLink']}" target="_blank">Acessar Produto</a></p>
        ]]>"""
        
        # Item do feed
        item_lines = [
            '    <item>',
            f'      <title>{product["name"]} - {product["score"]}%</title>',
            f'      <link>{product_url}</link>',
            f'      <guid>{product["id"]}</guid>',
            f'      <category>{product["type"]}</category>',
            f'      <pubDate>{datetime.now().strftime("%a, %d %b %Y %H:%M:%S +0000")}</pubDate>',
            f'      <description>{description}</description>',
            f'      <content:encoded>{description}</content:encoded>',
            '    </item>',
        ]
        
        rss_lines.extend(item_lines)
    
    # Fechar RSS
    rss_lines.extend([
        '  </channel>',
        '</rss>',
    ])
    
    # Juntar e salvar
    rss = '\n'.join(rss_lines)
    
    os.makedirs('radar', exist_ok=True)
    with open('radar/feed.xml', 'w', encoding='utf-8') as f:
        f.write(rss)
    
    print("✅ RSS Feed gerado com sucesso!")
    print(f"📁 Arquivo: radar/feed.xml")
    print(f"📊 Total de produtos: {len(products)}")
    print(f"🔗 URL: https://granahoje.github.io/radar/feed.xml")
    
    return True

if __name__ == '__main__':
    generate_rss_feed()
