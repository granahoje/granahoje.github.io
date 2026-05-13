#!/usr/bin/env python3
"""
Script para integrar somente o Adsterra autorizado em todas as páginas HTML do site.
Insere o script Adsterra antes do fechamento da tag </head>.
"""

import os
import re
from pathlib import Path

# Configuração única de monetização autorizada
ADSTERRA_SCRIPT = '''
<script src="https://pl29387236.profitablecpmratenetwork.com/5f/e8/01/5fe801f371dcdefd22e9b1fe08603d69.js"></script>
'''

def should_process_file(file_path):
    """Verifica se o arquivo deve ser processado."""
    # Ignorar arquivos em diretórios específicos
    ignore_dirs = ['__manus__', '.git', 'node_modules', '.github']
    
    for ignore_dir in ignore_dirs:
        if f'/{ignore_dir}/' in file_path or file_path.startswith(ignore_dir):
            return False
    
    # Processar apenas arquivos HTML
    return file_path.endswith('.html')

def has_monetization(content):
    """Verifica se o arquivo já possui integração de monetização."""
    return 'profitablecpmratenetwork.com' in content

def integrate_monetization(file_path):
    """Integra somente o Adsterra autorizado em um arquivo HTML."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pular se já possui integração
        if has_monetization(content):
            print(f"⏭️  SKIP (já integrado): {file_path}")
            return False
        
        # Verificar se tem </head>
        if '</head>' not in content:
            print(f"⚠️  SKIP (sem </head>): {file_path}")
            return False
        
        # Inserir antes de </head>
        new_content = content.replace('</head>', ADSTERRA_SCRIPT + '</head>', 1)
        
        # Salvar arquivo
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ INTEGRADO: {file_path}")
        return True
    
    except Exception as e:
        print(f"❌ ERRO em {file_path}: {e}")
        return False

def main():
    """Processa todos os arquivos HTML do repositório."""
    repo_path = Path('/home/ubuntu/granahoje.github.io')
    
    if not repo_path.exists():
        print("❌ Repositório não encontrado!")
        return
    
    html_files = list(repo_path.rglob('*.html'))
    print(f"📁 Encontrados {len(html_files)} arquivos HTML\n")
    
    processed = 0
    for html_file in sorted(html_files):
        relative_path = html_file.relative_to(repo_path)
        
        if should_process_file(str(relative_path)):
            if integrate_monetization(str(html_file)):
                processed += 1
    
    print(f"\n✨ Total de arquivos integrados: {processed}")

if __name__ == '__main__':
    main()
