import os
from pathlib import Path
from bs4 import BeautifulSoup
import re, json

root = Path('/home/ubuntu/granahoje.github.io')
langs = ['ar', 'bn', 'en', 'es', 'fr', 'hi', 'ja', 'pt-pt', 'ru', 'zh']

def audit_structure(soup):
    # Verifica elementos padrão esperados
    has_header = bool(soup.find('header'))
    has_nav = bool(soup.find('nav'))
    has_footer = bool(soup.find('footer'))
    has_ads = 'adsbygoogle' in str(soup)
    has_analytics = 'gtag' in str(soup)
    return {
        'header': has_header,
        'nav': has_nav,
        'footer': has_footer,
        'ads': has_ads,
        'analytics': has_analytics
    }

def get_word_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    for tag in soup(['script','style','nav','footer','header','noscript']):
        tag.decompose()
    text = soup.get_text(' ', strip=True)
    words = re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ0-9]+(?:[-'][A-Za-zÀ-ÖØ-öø-ÿ0-9]+)?", text)
    return len(words)

results = {
    'languages': {},
    'standardization': [],
    'short_articles': []
}

# 1. Auditoria de Idiomas
for lang in langs:
    lang_dir = root / lang
    if lang_dir.exists():
        files = list(lang_dir.glob('**/*.html'))
        results['languages'][lang] = {
            'count': len(files),
            'has_artigos_folder': (lang_dir / 'artigos').exists()
        }
    else:
        results['languages'][lang] = 'MISSING'

# 2. Auditoria de Artigos (PT-BR e outros)
all_html = list(root.glob('**/*.html'))
for p in all_html:
    if any(part in {'.git', 'node_modules'} for part in p.parts): continue
    
    try:
        html = p.read_text(encoding='utf-8', errors='ignore')
        soup = BeautifulSoup(html, 'html.parser')
        
        # Só auditar artigos (pasta artigos ou arquivos específicos de conteúdo)
        is_article = 'artigos/' in str(p) or p.name in ['artigo-ganhar-dinheiro-online.html', 'artigo-seguranca-online.html']
        
        if is_article:
            words = get_word_count(html)
            struct = audit_structure(soup)
            
            entry = {
                'file': str(p.relative_to(root)),
                'words': words,
                'structure': struct
            }
            
            if words < 800:
                results['short_articles'].append(entry)
            
            # Verificar padronização (se falta algo básico)
            if not all(struct.values()):
                results['standardization'].append(entry)
                
    except Exception as e:
        print(f"Error processing {p}: {e}")

# 3. Localizar AEET
aeet_matches = []
for p in root.glob('**/*'):
    if p.is_file() and p.suffix in ['.html', '.md', '.txt']:
        if 'AEET' in p.read_text(errors='ignore'):
            aeet_matches.append(str(p.relative_to(root)))
results['aeet_matches'] = aeet_matches

with open('/home/ubuntu/granahoje.github.io/audit_v2_results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print("Auditoria V2 concluída. Resultados em audit_v2_results.json")
