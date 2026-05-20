import os
import re

tools_dir = "project/ferramentas"
css_path = "../css/ferramentas.css"

def update_tool(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Remover o bloco <style> antigo
    content = re.sub(r"<style>.*?</style>", f'<link rel="stylesheet" href="{css_path}">', content, flags=re.DOTALL)

    # Melhorar a estrutura do body
    # Envolver o conteúdo principal em divs com as novas classes
    if '<div class="container">' in content:
        # Se já tem container, vamos tentar ajustar a estrutura interna
        content = content.replace('<main>', '<main class="container">')
        content = content.replace('<h1 class="page-title">', '<header class="page-header"><h1 class="page-title">')
        content = content.replace('</h1>', '</h1>')
        content = content.replace('<p class="page-subtitle">', '<p class="page-subtitle">')
        # Fechar o header da página se necessário
        if '</p>' in content and 'page-subtitle' in content:
            content = content.replace('</p>\n    <div class="calculator-grid">', '</p></header>\n    <div class="calculator-container">\n    <div class="calculator-grid">')
            content = content.replace('</div>\n    </main>', '</div>\n    </div>\n    </main>')

    # Ajustar as seções de informação para info-card
    content = content.replace('<div class="info-section">', '<div class="info-card">')
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

for filename in os.listdir(tools_dir):
    if filename.endswith(".html"):
        update_tool(os.path.join(tools_dir, filename))
