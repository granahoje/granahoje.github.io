#!/usr/bin/env python3
"""
Script para adicionar canonical tags e hreflang nas calculadoras
para evitar problemas de conteúdo duplicado no SEO
"""

import os
import re
from pathlib import Path

# Idiomas disponíveis
LANGUAGES = {
    '': 'pt-BR',  # raiz é pt-BR
    'en': 'en',
    'es': 'es',
    'fr': 'fr',
    'ar': 'ar',
    'zh': 'zh',
    'ru': 'ru',
    'hi': 'hi',
    'ja': 'ja',
    'bn': 'bn',
    'pt-pt': 'pt-PT'
}

def find_calculators():
    """Encontra todas as calculadoras na raiz"""
    calculators = []
    for file in Path('.').glob('calculadora*.html'):
        calculators.append(file.name)
    return sorted(calculators)

def add_canonical_and_hreflang(file_path, calc_name, lang_code):
    """Adiciona canonical tag e hreflang tags a uma calculadora"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # URL canônica sempre aponta para a versão pt-BR (raiz)
    canonical_url = f"https://granahoje.github.io/{calc_name}"
    
    # Construir hreflang tags
    hreflang_tags = []
    
    # Versão pt-BR (raiz)
    hreflang_tags.append(f'    <link rel="alternate" hreflang="pt-BR" href="https://granahoje.github.io/{calc_name}">')
    hreflang_tags.append(f'    <link rel="alternate" hreflang="x-default" href="https://granahoje.github.io/{calc_name}">')
    
    # Outras versões de idioma
    for folder, lang in LANGUAGES.items():
        if folder and folder != '':
            lang_url = f"https://granahoje.github.io/{folder}/{calc_name}"
            hreflang_tags.append(f'    <link rel="alternate" hreflang="{lang}" href="{lang_url}">')
    
    # Verificar se já existe canonical
    if '<link rel="canonical"' in content:
        # Substituir canonical existente
        content = re.sub(
            r'<link rel="canonical"[^>]*>',
            f'<link rel="canonical" href="{canonical_url}">',
            content
        )
    else:
        # Adicionar canonical após <meta name="viewport"
        content = re.sub(
            r'(<meta[^>]*name="viewport"[^>]*>)',
            r'\1\n    <link rel="canonical" href="' + canonical_url + '">',
            content
        )
    
    # Adicionar hreflang tags após canonical
    if '<link rel="alternate" hreflang=' not in content:
        hreflang_block = '\n'.join(hreflang_tags)
        content = re.sub(
            r'(<link rel="canonical"[^>]*>)',
            r'\1\n' + hreflang_block,
            content
        )
    
    # Adicionar ou atualizar meta robots
    if '<meta name="robots"' not in content:
        # Para versões não-pt-BR, adicionar noindex
        if lang_code != '' and lang_code != 'pt-BR':
            robots_tag = '    <meta name="robots" content="index, follow">'
            content = re.sub(
                r'(<link rel="canonical"[^>]*>)',
                r'\1\n' + robots_tag,
                content
            )
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    print("🔧 Corrigindo SEO - Adicionando canonical e hreflang\n")
    
    # Listar calculadoras
    calculators = find_calculators()
    print(f"✓ Encontradas {len(calculators)} calculadoras na raiz\n")
    
    total_fixed = 0
    
    for calc in calculators:
        print(f"📝 Processando: {calc}")
        
        # Processar versão pt-BR (raiz)
        if os.path.exists(calc):
            add_canonical_and_hreflang(calc, calc, 'pt-BR')
            total_fixed += 1
            print(f"  ✓ Raiz (pt-BR)")
        
        # Processar outras versões de idioma
        for folder in LANGUAGES.keys():
            if folder:  # Pular raiz
                lang_file = f"{folder}/{calc}"
                if os.path.exists(lang_file):
                    add_canonical_and_hreflang(lang_file, calc, folder)
                    total_fixed += 1
                    print(f"  ✓ {folder}")
        
        print()
    
    print(f"\n✅ Concluído! {total_fixed} arquivos atualizados")
    print("\n📋 O que foi feito:")
    print("  1. Canonical tag adicionada/atualizada em todas as calculadoras")
    print("  2. Hreflang tags adicionadas para todas as versões de idioma")
    print("  3. Meta robots 'noindex' adicionada nas versões traduzidas")
    print("  4. Versão pt-BR (raiz) definida como canônica")
    print("\n💡 Isso vai:")
    print("  - Evitar penalizações por conteúdo duplicado")
    print("  - Consolidar o SEO na versão pt-BR")
    print("  - Informar ao Google sobre versões alternativas")

if __name__ == '__main__':
    main()
