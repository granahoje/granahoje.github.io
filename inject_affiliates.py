import json, random, re
from pathlib import Path
from bs4 import BeautifulSoup

root = Path('/home/ubuntu/granahoje.github.io')

with open(root / 'CAMPANHAS.json', 'r') as f:
    campanhas = json.load(f)

def get_cta(campanha):
    nome = campanha['nome']
    url = campanha['url']
    ctas = [
        f'<div class="affiliate-cta" style="margin: 20px 0; padding: 20px; background: rgba(34, 211, 189, 0.1); border-radius: 15px; border: 1px solid #22d3bd; text-align: center;">'
        f'<p style="margin-bottom: 10px; font-weight: 700;">💡 Dica do Grana Hoje:</p>'
        f'<p>Aproveite as melhores condições com o <strong>{nome}</strong>.</p>'
        f'<a href="{url}" target="_blank" rel="nofollow" style="display: inline-block; margin-top: 10px; padding: 10px 20px; background: #22d3bd; color: #09111f; text-decoration: none; border-radius: 8px; font-weight: 800;">Conhecer Agora →</a>'
        f'</div>',
        
        f'<div class="affiliate-cta" style="margin: 25px 0; padding: 15px; border-left: 4px solid #f59e0b; background: rgba(245, 158, 11, 0.05);">'
        f'<p><strong>Recomendação:</strong> Precisa de uma solução financeira? Confira o que o <strong>{nome}</strong> oferece para você.</p>'
        f'<a href="{url}" target="_blank" rel="nofollow" style="color: #f59e0b; font-weight: 800; text-decoration: none;">Ver detalhes da oferta →</a>'
        f'</div>'
    ]
    return random.choice(ctas)

def process_file(p):
    html = p.read_text(encoding='utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    
    # Identificar categoria do arquivo para link contextual
    cat = "Geral"
    if "juros-compostos" in p.name or "investimento" in p.name: cat = "Investimento"
    elif "salario" in p.name or "trabalhista" in p.name: cat = "Empréstimo"
    elif "moedas" in p.name or "cambio" in p.name: cat = "Câmbio"
    elif "reserva" in p.name: cat = "Dívidas"
    
    # Filtrar campanhas por categoria se possível, senão pegar aleatória
    matches = [c for c in campanhas if c['categoria'] == cat]
    if not matches: matches = campanhas
    
    selected = random.choice(matches)
    cta_html = get_cta(selected)
    
    # Inserir no final do conteúdo principal (antes do footer ou no final da div container)
    target = soup.find('main') or soup.find('article') or soup.find('div', class_='container')
    if target:
        # Evitar duplicatas se rodar de novo
        if not soup.find('div', class_='affiliate-cta'):
            target.append(BeautifulSoup(cta_html, 'html.parser'))
            p.write_text(str(soup), encoding='utf-8')
            return True
    return False

# 1. Aplicar em todas as calculadoras (ferramentas)
calcs = list(root.glob('calculadora-*.html')) + list(root.glob('conversor-*.html'))
count_calcs = 0
for c in calcs:
    if process_file(c): count_calcs += 1

# 2. Aplicar em alguns artigos de forma natural (ex: os 20 primeiros de cada idioma)
count_articles = 0
for lang_dir in [root] + [root / l for l in ['en', 'es', 'fr', 'ar', 'zh', 'ru', 'hi', 'ja', 'bn', 'pt-pt']]:
    artigos = list((lang_dir / 'artigos').glob('*.html'))[:5] # Limitar para manter natural
    for a in artigos:
        if process_file(a): count_articles += 1

print(f"Links inseridos em {count_calcs} ferramentas e {count_articles} artigos.")
