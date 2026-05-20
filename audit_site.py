from pathlib import Path
from bs4 import BeautifulSoup
import re, json
root = Path('/home/ubuntu/granahoje.github.io')

def visible_text(html):
    soup = BeautifulSoup(html, 'html.parser')
    for tag in soup(['script','style','nav','footer','header','noscript']):
        tag.decompose()
    return soup.get_text(' ', strip=True)

articles = []
for p in sorted((root/'artigos').glob('*.html')):
    html = p.read_text(encoding='utf-8', errors='ignore')
    text = visible_text(html)
    words = re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ0-9]+(?:[-'][A-Za-zÀ-ÖØ-öø-ÿ0-9]+)?", text)
    title = BeautifulSoup(html, 'html.parser').find(['h1','title'])
    articles.append({'file': str(p.relative_to(root)), 'words': len(words), 'title': title.get_text(' ', strip=True) if title else ''})

short = [a for a in articles if a['words'] < 800]
print('TOTAL_ARTIGOS', len(articles))
print('CURTOS', len(short))
for a in short:
    print(f"SHORT {a['words']:4d} {a['file']} | {a['title'][:90]}")
print('\nOCORRENCIAS_7+_FERRAMENTAS')
for p in root.glob('**/*.html'):
    if any(part in {'.git','node_modules'} for part in p.parts): continue
    txt = p.read_text(encoding='utf-8', errors='ignore')
    if '7+' in txt or 'Calculadoras Gratuitas' in txt:
        print(str(p.relative_to(root)))
print('\nBUSCADOR')
for p in root.glob('**/*'):
    if p.is_file() and p.suffix.lower() in {'.html','.js','.css'}:
        txt = p.read_text(encoding='utf-8', errors='ignore')
        if re.search(r'busca|search|pesquis', txt, re.I):
            print(str(p.relative_to(root)))
print('\nSITEMAP')
for name in ['sitemap.xml','robots.txt','aeet.html','AEET.html']:
    p=root/name
    print(name, p.exists(), p.stat().st_size if p.exists() else '')
Path('/home/ubuntu/granahoje.github.io/audit_results.json').write_text(json.dumps({'articles':articles,'short':short}, ensure_ascii=False, indent=2), encoding='utf-8')
