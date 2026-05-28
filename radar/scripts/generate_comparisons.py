#!/usr/bin/env python3
import json
import os
from datetime import datetime

class ComparisonGenerator:
    def __init__(self):
        self.base_dir = '/home/ubuntu/granahoje.github.io/radar'
        self.data_file = os.path.join(self.base_dir, 'data/products.json')
        self.output_dir = os.path.join(self.base_dir, 'comparacao')
        os.makedirs(self.output_dir, exist_ok=True)

    def load_data(self):
        with open(self.data_file, 'r', encoding='utf-8') as f:
            return json.load(f)

    def generate_comparison_article(self, p1, p2):
        title = f"{p1['name']} vs {p2['name']}: Qual o melhor em {datetime.now().year}?"
        
        article = f"""## Introdução: O Grande Duelo
Escolher entre **{p1['name']}** e **{p2['name']}** é uma dúvida comum para muitos brasileiros. Ambos são excelentes produtos na categoria de {p1['type'].lower()}, mas possuem diferenças fundamentais que podem fazer um ser muito melhor que o outro para o seu perfil específico. Nesta análise profunda, comparamos taxas, benefícios, segurança e facilidade de uso para ajudar você a decidir.

## 1. Por que escolher {p1['name']}?
{p1['description']}

**Principais Benefícios de {p1['name']}:**
"""
        for pro in p1.get('pros', [])[:3]:
            article += f"- {pro}\n"

        article += f"""
## 2. Por que escolher {p2['name']}?
{p2['description']}

**Principais Benefícios de {p2['name']}:**
"""
        for pro in p2.get('pros', [])[:3]:
            article += f"- {pro}\n"

        article += f"""
## Veredito Final: Qual escolher?
Se você busca **{p1['pros'][0] if p1['pros'] else 'eficiência'}**, o **{p1['name']}** tende a ser a melhor escolha. Por outro lado, se sua prioridade é **{p2['pros'][0] if p2['pros'] else 'segurança'}**, o **{p2['name']}** pode ser mais adequado.

---

### 🚀 Comece agora:
- [Acessar site oficial de {p1['name']}]({p1['affiliateLink']})
- [Acessar site oficial de {p2['name']}]({p2['affiliateLink']})
"""
        return title, article

    def generate_html(self, title, article, p1, p2):
        # Conversão simples de Markdown para HTML
        content_html = article.replace('## ', '<h2>').replace('**', '<strong>').replace('</strong>', '**')
        content_html = content_html.replace('\n', '<br>')
        
        html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Radar Financeiro</title>
    <link rel="stylesheet" href="/radar/styles.css">
</head>
<body>
    <header>
        <div class="container">
            <div class="header-content">
                <div class="logo">📊 Radar Financeiro</div>
                <nav>
                    <a href="/radar/">Catálogo</a>
                    <a href="/radar/comparacao/">Comparar</a>
                    <a href="/radar/postagens.html">Postagens</a>
                </nav>
            </div>
        </div>
    </header>
    <div class="container" style="padding: 4rem 0;">
        <article class="article-container">
            <h1>{title}</h1>
            <p style="color: var(--text-tertiary); margin-bottom: 2rem;">Atualizado em: {datetime.now().strftime('%d/%m/%Y')}</p>
            
            <div class="article-content" style="background: var(--bg-card); padding: 2rem; border-radius: 1rem; border: 1px solid rgba(16, 185, 129, 0.1);">
                {content_html}
            </div>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem; margin-top: 3rem;">
                <div class="article-cta" style="padding: 2rem; background: rgba(16, 185, 129, 0.05); border-radius: 1rem; text-align: center; border: 2px dashed var(--primary);">
                    <h4>{p1['name']}</h4>
                    <p style="font-size: 0.9rem; margin-bottom: 1.5rem;">{p1['description'][:100]}...</p>
                    <a href="{p1['affiliateLink']}" class="btn btn-primary" target="_blank" rel="noopener noreferrer">Acessar Site Oficial</a>
                </div>
                <div class="article-cta" style="padding: 2rem; background: rgba(16, 185, 129, 0.05); border-radius: 1rem; text-align: center; border: 2px dashed var(--primary);">
                    <h4>{p2['name']}</h4>
                    <p style="font-size: 0.9rem; margin-bottom: 1.5rem;">{p2['description'][:100]}...</p>
                    <a href="{p2['affiliateLink']}" class="btn btn-primary" target="_blank" rel="noopener noreferrer">Acessar Site Oficial</a>
                </div>
            </div>
        </article>
    </div>
    <footer style="margin-top: 5rem; padding: 3rem 0; background: var(--bg-dark); text-align: center;">
        <p>&copy; 2026 Radar Financeiro. Todos os direitos reservados.</p>
    </footer>
</body>
</html>"""
        return html

    def run(self):
        data = self.load_data()
        products = data['products']
        
        by_cat = {}
        for p in products:
            cat = p['category']
            if cat not in by_cat: by_cat[cat] = []
            by_cat[cat].append(p)
            
        comparisons_count = 0
        for cat, items in by_cat.items():
            if len(items) >= 2:
                # Gerar duelos entre os produtos da categoria
                p1 = items[0]
                p2 = items[1]
                title, article = self.generate_comparison_article(p1, p2)
                html = self.generate_html(title, article, p1, p2)
                
                slug = f"{p1['id']}-vs-{p2['id']}"
                path = os.path.join(self.output_dir, slug)
                os.makedirs(path, exist_ok=True)
                with open(os.path.join(path, 'index.html'), 'w', encoding='utf-8') as f:
                    f.write(html)
                comparisons_count += 1
                
        print(f"✅ {comparisons_count} Duelos (X vs Y) gerados com sucesso!")

if __name__ == '__main__':
    ComparisonGenerator().run()
