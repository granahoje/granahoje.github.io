import json, random, re
from pathlib import Path
from bs4 import BeautifulSoup

root = Path('/home/ubuntu/granahoje.github.io')

with open(root / 'CAMPANHAS.json', 'r') as f:
    campanhas = json.load(f)

def get_natural_cta(campanha):
    nome = campanha['nome']
    url = campanha['url']
    
    templates = [
        f'<div class="natural-cta" style="margin: 30px 0; padding: 25px; background: #1a263e; border-radius: 20px; border: 1px solid rgba(0, 209, 178, 0.3); box-shadow: 0 10px 30px rgba(0,0,0,0.1);">'
        f'<h4 style="color: #00d1b2; margin-top: 0; margin-bottom: 12px; font-size: 1.2rem;">🚀 Potencialize seus Resultados</h4>'
        f'<p style="color: #b6c2d2; font-size: 1rem; line-height: 1.5; margin-bottom: 18px;">Para complementar sua estratégia financeira, recomendamos conhecer o <strong>{nome}</strong>. É uma das ferramentas mais seguras que testamos este ano.</p>'
        f'<a href="{url}" target="_blank" rel="nofollow" style="display: inline-block; padding: 12px 24px; background: linear-gradient(135deg, #00d1b2, #00a98f); color: #0f172a; text-decoration: none; border-radius: 12px; font-weight: 800; transition: 0.3s;">Acessar {nome} →</a>'
        f'</div>',
        
        f'<blockquote style="margin: 35px 0; padding: 20px 30px; border-left: 5px solid #00d1b2; background: rgba(0, 209, 178, 0.05); font-style: normal; border-radius: 0 15px 15px 0;">'
        f'<p style="margin-bottom: 15px; color: #f8fafc; font-weight: 600;">Nota do Editor:</p>'
        f'<p style="color: #b6c2d2;">Muitos leitores nos perguntam sobre as melhores opções para este perfil. Atualmente, o <strong>{nome}</strong> oferece as condições mais competitivas do mercado.</p>'
        f'<a href="{url}" target="_blank" rel="nofollow" style="color: #00d1b2; font-weight: 700; text-decoration: underline;">Clique aqui para conferir a oferta oficial</a>'
        f'</blockquote>',
        
        f'<div class="tool-tip" style="margin: 30px 0; padding: 20px; background: rgba(245, 158, 11, 0.1); border-radius: 15px; border: 1px dashed #f59e0b; display: flex; align-items: center; gap: 20px;">'
        f'<div style="font-size: 2rem;">💡</div>'
        f'<div>'
        f'<p style="margin: 0; color: #f8fafc; font-weight: 700;">Dica Prática:</p>'
        f'<p style="margin: 5px 0 0; color: #b6c2d2;">Você pode acelerar seus objetivos financeiros utilizando o <strong>{nome}</strong>. <a href="{url}" target="_blank" rel="nofollow" style="color: #f59e0b; text-decoration: none; font-weight: 700;">Saiba mais aqui.</a></p>'
        f'</div>'
        f'</div>'
    ]
    return random.choice(templates)

def process_file(p):
    try:
        html = p.read_text(encoding='utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        
        # Remover CTAs antigos se existirem
        for old in soup.find_all(['div', 'blockquote'], class_=['affiliate-cta', 'natural-cta', 'tool-tip']):
            old.decompose()
            
        cat = "Geral"
        if "juros-compostos" in p.name or "investimento" in p.name: cat = "Investimento"
        elif "salario" in p.name or "trabalhista" in p.name or "emprestimo" in p.name: cat = "Empréstimo"
        elif "moedas" in p.name or "cambio" in p.name: cat = "Câmbio"
        elif "reserva" in p.name or "divida" in p.name: cat = "Dívidas"
        elif "fgts" in p.name: cat = "FGTS"
        elif "cripto" in p.name or "bitcoin" in p.name: cat = "Cripto"
        
        matches = [c for c in campanhas if c['categoria'] == cat]
        if not matches: matches = campanhas
        
        selected = random.choice(matches)
        cta_html = get_natural_cta(selected)
        
        target = soup.find('main') or soup.find('article') or soup.find('div', class_='container')
        if target:
            # Em artigos, tentar inserir no meio do texto
            paragraphs = target.find_all('p')
            if len(paragraphs) > 4:
                paragraphs[len(paragraphs)//2].insert_after(BeautifulSoup(cta_html, 'html.parser'))
            else:
                target.append(BeautifulSoup(cta_html, 'html.parser'))
            
            p.write_text(str(soup), encoding='utf-8')
            return True
    except Exception as e:
        print(f"Erro em {p}: {e}")
    return False

# Aplicar em ferramentas e artigos
count = 0
for p in list(root.glob('*.html')) + list(root.glob('**/artigos/*.html')):
    if p.name in ['index.html', 'blog.html', 'about.html', 'contact.html', 'privacy-policy.html', 'terms-of-service.html']:
        continue
    if process_file(p):
        count += 1

print(f"Links naturais inseridos em {count} páginas.")
