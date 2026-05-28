#!/usr/bin/env python3
import json
import os
from datetime import datetime

def generate_posts_index():
    products_file = 'radar/data/products.json'
    output_file = 'radar/postagens.html'
    
    with open(products_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        products = data['products']
        categories = {c['id']: c['name'] for c in data.get('categories', [])}

    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Índice de Postagens | Radar Financeiro</title>
    <link rel="stylesheet" href="/radar/styles.css">
    <style>
        .posts-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1.5rem;
            margin-top: 2rem;
        }}
        .post-item {{
            background: var(--bg-card);
            border: 1px solid rgba(16, 185, 129, 0.1);
            border-radius: 0.5rem;
            padding: 1.5rem;
            transition: var(--transition);
        }}
        .post-item:hover {{
            border-color: var(--primary);
            transform: translateY(-5px);
        }}
        .post-category {{
            font-size: 0.8rem;
            color: var(--primary);
            text-transform: uppercase;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }}
        .post-title {{
            font-size: 1.2rem;
            margin-bottom: 1rem;
            color: var(--text-primary);
        }}
    </style>
</head>
<body>
    <header>
        <div class="container">
            <div class="header-content">
                <div class="logo">📊 Radar Financeiro</div>
                <nav>
                    <a href="/radar/">Catálogo</a>
                    <a href="/radar/comparacao/">Comparar</a>
                    <a href="/radar/postagens.html" class="active">Postagens</a>
                </nav>
            </div>
        </div>
    </header>

    <section class="hero" style="padding: 4rem 0;">
        <div class="container">
            <h1>Índice de Postagens</h1>
            <p>Explore todos os nossos artigos e análises financeiras detalhadas.</p>
        </div>
    </section>

    <div class="container" style="padding: 4rem 0;">
        <div class="posts-grid">
"""

    for product in products:
        cat_name = categories.get(product['category'], 'Geral')
        html += f"""
            <div class="post-item">
                <div class="post-category">{cat_name}</div>
                <div class="post-title">{product['name']}</div>
                <a href="/radar/produto/{product['id']}/" class="btn btn-outline btn-small">Ler Artigo</a>
            </div>"""

    html += """
        </div>
    </div>

    <footer>
        <div class="container">
            <div class="footer-bottom">
                <p>&copy; 2026 Radar Financeiro. Todos os direitos reservados.</p>
            </div>
        </div>
    </footer>
</body>
</html>"""

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ Índice de postagens gerado em {output_file}")

if __name__ == '__main__':
    generate_posts_index()
