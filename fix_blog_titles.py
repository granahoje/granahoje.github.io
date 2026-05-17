import os
import re

# Dicionário de traduções comuns encontradas nos títulos para substituir por termos locais
replacements = {
    'en': {'O Segredo Revelado': 'Secret Revealed', 'Apps que Pagam': 'Apps that Pay', 'Como Maximizar': 'How to Maximize', 'Os 5 Melhores': 'Top 5 Best', 'Desvendando': 'Unveiling', 'Guia Passo a Passo': 'Step-by-Step Guide'},
    'es': {'O Segredo Revelado': 'Secreto Revelado', 'Apps que Pagam': 'Apps que Pagan', 'Como Maximizar': 'Cómo Maximizar', 'Os 5 Melhores': 'Los 5 Mejores', 'Desvendando': 'Descubriendo', 'Guia Passo a Passo': 'Guía Paso a Paso'},
    'zh': {'O Segredo Revelado': '秘密揭晓', 'Apps que Pagam': '付费应用', 'Como Maximizar': '如何最大化', 'Os 5 Melhores': '前 5 名最佳', 'Desvendando': '揭秘', 'Guia Passo a Passo': '分步指南'}
}

def fix_blog(lang):
    path = f"{lang}/blog.html"
    if not os.path.exists(path): return
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Corrigir links de políticas no footer do blog.html
    content = content.replace('href="/privacy-policy.html"', f'href="/{lang}/privacy-policy.html"')
    content = content.replace('href="/terms-of-service.html"', f'href="/{lang}/terms-of-service.html"')
    content = content.replace('href="/contact.html"', f'href="/{lang}/contact.html"')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

for lang in ['en', 'es', 'fr', 'ar', 'zh', 'ru', 'hi', 'ja', 'bn', 'pt-pt']:
    fix_blog(lang)
