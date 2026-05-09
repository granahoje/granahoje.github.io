#!/usr/bin/env python3
import re
from pathlib import Path

ROOT = Path('/home/ubuntu/granahoje.github.io')

def fix_html(path):
    content = path.read_text(encoding='utf-8')
    
    # Se o script anterior removeu o fechamento de h2 ou a tag section
    if '<h2 class="section-title" id="tasksTitle">' in content and '<section class="task-list"' not in content:
        # Procurar onde o bloco de tarefas começa logo após o h2
        content = content.replace('<h2 class="section-title" id="tasksTitle">', '<h2 class="section-title" id="tasksTitle">✨ Missões Lucrativas</h2>\n        <section class="task-list" role="region" aria-label="Lista de tarefas disponíveis">')
        
        # Procurar onde o bloco de tarefas termina antes do visitor-counter
        if '<div class="visitor-counter"' in content and '</section>' not in content:
             content = content.replace('<div class="visitor-counter"', '</section>\n\n        <div class="visitor-counter"')

    # Garantir que o prefixo CPX esteja nas traduções se não estiver
    if '"surveyName": "CPX:' not in content:
        content = re.sub(r'("surveyName":\s*")([^"]+)', r'\1CPX: \2', content)
    if '"simulatorName": "CPX:' not in content:
        content = re.sub(r'("simulatorName":\s*")([^"]+)', r'\1CPX: \2', content)

    path.write_text(content, encoding='utf-8')

for path in ROOT.glob('**/index.html'):
    fix_html(path)
print("Estrutura corrigida.")
