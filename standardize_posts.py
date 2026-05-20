import os
from pathlib import Path
from bs4 import BeautifulSoup

root = Path('/home/ubuntu/granahoje.github.io')

# Cabeçalho padrão para artigos
HEADER_HTML = """
<header style="background: rgba(15,23,42,.88); backdrop-filter: blur(14px); border-bottom: 1px solid rgba(255,255,255,.11); padding: 15px 20px; display: flex; justify-content: space-between; align-items: center; position: sticky; top: 0; z-index: 100;">
    <a href="/" style="text-decoration: none; font-size: 1.2rem; font-weight: 800; color: #00d1b2;">GRANA HOJE</a>
    <nav style="display: flex; gap: 20px;">
        <a href="/blog.html" style="color: #fff; text-decoration: none; font-weight: 700;">Blog</a>
        <a href="/about.html" style="color: #fff; text-decoration: none; font-weight: 700;">Sobre</a>
    </nav>
</header>
"""

FOOTER_HTML = """
<footer style="border-top: 1px solid rgba(255,255,255,.11); background: rgba(15,23,42,.8); text-align: center; padding: 40px 20px; color: #b6c2d2; margin-top: 50px;">
    <div style="display: flex; justify-content: center; gap: 20px; margin-bottom: 20px;">
        <a href="/about.html" style="color: #00d1b2; text-decoration: none;">Sobre</a>
        <a href="/blog.html" style="color: #00d1b2; text-decoration: none;">Blog</a>
        <a href="/privacy-policy.html" style="color: #00d1b2; text-decoration: none;">Privacidade</a>
    </div>
    <p>© 2026 Grana Hoje. Todos os direitos reservados.</p>
</footer>
"""

def standardize_file(p):
    try:
        html = p.read_text(encoding='utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        
        # Remover headers e footers antigos se existirem
        for old in soup.find_all(['header', 'footer']):
            old.decompose()
            
        # Inserir novo header no início do body
        if soup.body:
            soup.body.insert(0, BeautifulSoup(HEADER_HTML, 'html.parser'))
            soup.body.append(BeautifulSoup(FOOTER_HTML, 'html.parser'))
            
            # Garantir fonte e estilo básico se faltar
            if not soup.find('style'):
                style = soup.new_tag('style')
                style.string = "body { font-family: 'Plus Jakarta Sans', sans-serif; background: #0f172a; color: #f8fafc; margin: 0; line-height: 1.6; } .container { max-width: 800px; margin: 0 auto; padding: 40px 20px; }"
                soup.head.append(style)
                
            p.write_text(str(soup), encoding='utf-8')
            return True
    except Exception as e:
        print(f"Erro em {p}: {e}")
    return False

# Aplicar aos artigos de todos os idiomas
count = 0
for p in root.glob('**/artigos/*.html'):
    if standardize_file(p):
        count += 1

print(f"Padronização concluída em {count} arquivos.")
