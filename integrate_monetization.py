#!/usr/bin/env python3
"""
Script para integrar CPX Research e Monetag em todas as páginas HTML do site.
Insere o iframe do CPX Research e o script Monetag antes do fechamento da tag </body>.
"""

import os
import re
from pathlib import Path

# Configurações
CPX_IFRAME = '''
<!-- CPX Research Integration -->
<div style="margin: 20px; text-align: center;">
    <iframe width="100%" frameBorder="0" height="2000px" src="https://offers.cpx-research.com/index.php?app_id=32967&ext_user_id={unique_user_id}&secure_hash={secure_hash}&username={user_name}&email={user_email}&subid_1=&subid_2"></iframe>
</div>
'''

MONETAG_SCRIPT = '''
<!-- Monetag Integration -->
<script src="https://quge5.com/88/tag.min.js" data-zone="237206" async data-cfasync="false"></script>
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
    return 'cpx-research.com' in content or 'quge5.com' in content

def integrate_monetization(file_path):
    """Integra CPX Research e Monetag em um arquivo HTML."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pular se já possui integração
        if has_monetization(content):
            print(f"⏭️  SKIP (já integrado): {file_path}")
            return False
        
        # Verificar se tem </body>
        if '</body>' not in content:
            print(f"⚠️  SKIP (sem </body>): {file_path}")
            return False
        
        # Inserir antes de </body>
        insertion = MONETAG_SCRIPT + CPX_IFRAME
        new_content = content.replace('</body>', insertion + '</body>')
        
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
