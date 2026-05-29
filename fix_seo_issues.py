import os
import re

def fix_sitemap():
    with open('sitemap.xml', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Substituir URLs de idioma que terminam em /index.html por / (com barra final)
    # Ex: https://granahoje.github.io/ja/index.html -> https://granahoje.github.io/ja/
    new_content = re.sub(r'https://granahoje.github.io/([a-z]{2}(-[a-z]{2})?)/index\.html', r'https://granahoje.github.io/\1/', content)
    
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Sitemap.xml corrigido.")

def fix_canonical_and_hreflang(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Corrigir canonical: remover index.html se for uma página de idioma
    # Ex: <link rel="canonical" href="https://granahoje.github.io/ja/index.html"> -> .../ja/
    content = re.sub(r'<link rel="canonical" href="https://granahoje\.github\.io/([a-z]{2}(-[a-z]{2})?)/index\.html">', 
                     r'<link rel="canonical" href="https://granahoje.github.io/\1/">', content)
    
    # 2. Corrigir hreflangs: remover index.html
    content = re.sub(r'hreflang="([a-z]{2}(-[a-z]{2})?)" href="https://granahoje\.github\.io/\1/index\.html"', 
                     r'hreflang="\1" href="https://granahoje.github.io/\1/"', content)

    # 3. Caso especial pt-br: se hreflang="pt-br" apontar para /index.html, mudar para a raiz /
    content = re.sub(r'hreflang="pt-br" href="https://granahoje\.github\.io/index\.html"', 
                     r'hreflang="pt-br" href="https://granahoje.github.io/"', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def process_html_files():
    for root, dirs, files in os.walk('.'):
        if '.git' in root: continue
        for file in files:
            if file.endswith('.html'):
                fix_canonical_and_hreflang(os.path.join(root, file))
    print("Arquivos HTML corrigidos.")

if __name__ == "__main__":
    fix_sitemap()
    process_html_files()
