import os
import re
from pathlib import Path
from urllib.parse import urljoin, urlparse

root = Path('/home/ubuntu/granahoje.github.io')
broken_links = []
missing_files = []
checked = set()

def extract_links(html_content):
    """Extrai todos os links de um arquivo HTML"""
    href_pattern = r'href=["\']([^"\']+)["\']'
    src_pattern = r'src=["\']([^"\']+)["\']'
    
    hrefs = re.findall(href_pattern, html_content)
    srcs = re.findall(src_pattern, html_content)
    return hrefs + srcs

def check_link(link, base_path):
    """Verifica se um link é válido"""
    if link.startswith('http://') or link.startswith('https://') or link.startswith('//'):
        return True  # Links externos são considerados válidos
    
    if link.startswith('#'):
        return True  # Âncoras internas
    
    if link.startswith('mailto:') or link.startswith('tel:'):
        return True  # Links de email/telefone
    
    # Remover query strings e âncoras
    clean_link = link.split('?')[0].split('#')[0]
    
    # Resolver caminho relativo
    if clean_link.startswith('/'):
        file_path = root / clean_link.lstrip('/')
    else:
        file_path = (base_path.parent / clean_link).resolve()
    
    # Verificar se arquivo existe
    if not file_path.exists():
        return False
    
    return True

# Auditar todos os arquivos HTML
html_files = list(root.glob('**/*.html'))
print(f"Auditando {len(html_files)} arquivos HTML...")

for html_file in html_files:
    try:
        content = html_file.read_text(encoding='utf-8')
        links = extract_links(content)
        
        for link in links:
            if not check_link(link, html_file):
                broken_links.append({
                    'file': str(html_file.relative_to(root)),
                    'link': link
                })
    except Exception as e:
        print(f"Erro ao processar {html_file}: {e}")

# Relatório
print("\n=== RELATÓRIO DE AUDITORIA ===\n")
if broken_links:
    print(f"❌ {len(broken_links)} links quebrados encontrados:\n")
    for item in broken_links[:20]:  # Mostrar primeiros 20
        print(f"  📄 {item['file']}")
        print(f"     🔗 {item['link']}\n")
else:
    print("✅ Nenhum link quebrado encontrado!")

print(f"\n✅ Total de arquivos auditados: {len(html_files)}")
