import json, random, re
from pathlib import Path
from bs4 import BeautifulSoup

root = Path('/home/ubuntu/granahoje.github.io')

with open(root / 'CAMPANHAS.json', 'r') as f:
    campanhas = json.load(f)

def get_premium_cta(campanha):
    nome = campanha['nome']
    url = campanha['url']
    
    templates = [
        # Premium Card 1 - Destaque com Gradiente
        f'''<div class="premium-affiliate-cta" style="
            margin: 40px 0;
            padding: 35px;
            background: linear-gradient(135deg, rgba(34, 211, 189, 0.15) 0%, rgba(16, 185, 129, 0.1) 100%);
            border: 2px solid rgba(34, 211, 189, 0.4);
            border-radius: 20px;
            box-shadow: 0 15px 40px rgba(34, 211, 189, 0.15), inset 0 1px 0 rgba(255,255,255,0.1);
            position: relative;
            overflow: hidden;
        ">
            <div style="position: absolute; top: -50px; right: -50px; width: 150px; height: 150px; background: radial-gradient(circle, rgba(34, 211, 189, 0.2), transparent); border-radius: 50%;"></div>
            <div style="position: relative; z-index: 1;">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                    <span style="font-size: 2.5rem;">⭐</span>
                    <h3 style="margin: 0; color: #22d3bd; font-size: 1.5rem; font-weight: 900;">Recomendação Premium</h3>
                </div>
                <p style="color: #b6c2d2; font-size: 1.05rem; line-height: 1.6; margin-bottom: 25px; font-weight: 500;">
                    Nossos especialistas testaram e aprovaram o <strong style="color: #fff;">{nome}</strong>. 
                    Oferece as melhores condições do mercado para sua situação financeira.
                </p>
                <a href="{url}" target="_blank" rel="nofollow" style="
                    display: inline-block;
                    padding: 16px 35px;
                    background: linear-gradient(135deg, #22d3bd 0%, #10b981 100%);
                    color: #09111f;
                    text-decoration: none;
                    border-radius: 12px;
                    font-weight: 900;
                    font-size: 1.05rem;
                    transition: all 0.3s;
                    box-shadow: 0 10px 25px rgba(34, 211, 189, 0.3);
                    border: none;
                    cursor: pointer;
                ">
                    🚀 Acessar {nome} Agora
                </a>
            </div>
        </div>''',

        # Premium Card 2 - Spotlight
        f'''<div class="premium-affiliate-cta" style="
            margin: 40px 0;
            padding: 40px;
            background: linear-gradient(to bottom, rgba(34, 211, 189, 0.1), rgba(15, 27, 45, 0.95));
            border: 2px solid #22d3bd;
            border-radius: 20px;
            box-shadow: 0 0 30px rgba(34, 211, 189, 0.25), inset 0 1px 0 rgba(255,255,255,0.1);
        ">
            <div style="text-align: center;">
                <div style="display: inline-block; padding: 12px 24px; background: rgba(34, 211, 189, 0.2); border-radius: 999px; margin-bottom: 20px; border: 1px solid rgba(34, 211, 189, 0.3);">
                    <span style="color: #22d3bd; font-weight: 800; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px;">Oferta Especial</span>
                </div>
                <h3 style="margin: 0 0 15px; color: #fff; font-size: 1.6rem; font-weight: 900;">{nome}</h3>
                <p style="color: #b6c2d2; font-size: 1.05rem; line-height: 1.7; margin-bottom: 30px; max-width: 600px; margin-left: auto; margin-right: auto;">
                    Aproveite as melhores condições e comece sua jornada financeira com segurança e confiança.
                </p>
                <a href="{url}" target="_blank" rel="nofollow" style="
                    display: inline-block;
                    padding: 18px 45px;
                    background: linear-gradient(135deg, #22d3bd 0%, #10b981 100%);
                    color: #09111f;
                    text-decoration: none;
                    border-radius: 12px;
                    font-weight: 900;
                    font-size: 1.1rem;
                    transition: all 0.3s;
                    box-shadow: 0 15px 35px rgba(34, 211, 189, 0.4);
                    border: none;
                    cursor: pointer;
                ">
                    ✨ Conhecer {nome}
                </a>
            </div>
        </div>''',

        # Premium Card 3 - Side by Side
        f'''<div class="premium-affiliate-cta" style="
            margin: 40px 0;
            padding: 35px;
            background: linear-gradient(90deg, rgba(34, 211, 189, 0.08) 0%, rgba(16, 185, 129, 0.05) 100%);
            border-left: 5px solid #22d3bd;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            display: flex;
            align-items: center;
            gap: 30px;
        ">
            <div style="font-size: 3rem; flex-shrink: 0;">💎</div>
            <div style="flex-grow: 1;">
                <h4 style="margin: 0 0 10px; color: #22d3bd; font-size: 1.3rem; font-weight: 900;">Parceiro Recomendado</h4>
                <p style="margin: 0 0 15px; color: #b6c2d2; font-size: 1rem; line-height: 1.6;">
                    <strong style="color: #fff;">{nome}</strong> é uma das melhores opções do mercado. Testado e aprovado por nossos especialistas.
                </p>
                <a href="{url}" target="_blank" rel="nofollow" style="
                    display: inline-block;
                    padding: 12px 30px;
                    background: linear-gradient(135deg, #22d3bd 0%, #10b981 100%);
                    color: #09111f;
                    text-decoration: none;
                    border-radius: 10px;
                    font-weight: 900;
                    font-size: 0.95rem;
                    transition: all 0.3s;
                    box-shadow: 0 8px 20px rgba(34, 211, 189, 0.3);
                    border: none;
                    cursor: pointer;
                ">
                    Acessar Agora →
                </a>
            </div>
        </div>''',

        # Premium Card 4 - Minimal Premium
        f'''<div class="premium-affiliate-cta" style="
            margin: 40px 0;
            padding: 30px;
            background: rgba(34, 211, 189, 0.05);
            border: 2px dashed rgba(34, 211, 189, 0.3);
            border-radius: 15px;
            text-align: center;
        ">
            <p style="margin: 0 0 20px; color: #22d3bd; font-weight: 800; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px;">
                ✅ Verificado e Recomendado
            </p>
            <h4 style="margin: 0 0 15px; color: #fff; font-size: 1.4rem; font-weight: 900;">{nome}</h4>
            <p style="margin: 0 0 25px; color: #b6c2d2; font-size: 1rem;">
                Confira esta oportunidade especial que nossos leitores aprovam.
            </p>
            <a href="{url}" target="_blank" rel="nofollow" style="
                display: inline-block;
                padding: 14px 40px;
                background: linear-gradient(135deg, #22d3bd 0%, #10b981 100%);
                color: #09111f;
                text-decoration: none;
                border-radius: 10px;
                font-weight: 900;
                font-size: 1rem;
                transition: all 0.3s;
                box-shadow: 0 10px 25px rgba(34, 211, 189, 0.3);
                border: none;
                cursor: pointer;
            ">
                Começar Agora
            </a>
        </div>'''
    ]
    return random.choice(templates)

def process_file(p):
    try:
        html = p.read_text(encoding='utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        
        # Remover CTAs antigos
        for old in soup.find_all(['div', 'blockquote'], class_=['affiliate-cta', 'natural-cta', 'tool-tip', 'premium-affiliate-cta']):
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
        cta_html = get_premium_cta(selected)
        
        target = soup.find('main') or soup.find('article') or soup.find('div', class_='container')
        if target:
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

print(f"Links premium redesenhados em {count} páginas.")
