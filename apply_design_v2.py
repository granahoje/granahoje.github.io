import os
import re

tools_dir = "project/ferramentas"
css_path = "../css/ferramentas.css"

def update_tool(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Atualizar CSS
    content = re.sub(r"<style>.*?</style>", f'<link rel="stylesheet" href="{css_path}">', content, flags=re.DOTALL)
    
    # 2. Corrigir estrutura do Main e Header da Página
    # Procurar o título H1 e o subtítulo P para criar o page-header
    header_pattern = re.compile(r'<h1 class="page-title">(.*?)</h1>\s*<p class="page-subtitle">(.*?)</p>', re.DOTALL)
    if header_pattern.search(content):
        content = header_pattern.sub(r'<header class="page-header">\n    <h1 class="page-title">\1</h1>\n    <p class="page-subtitle">\2</p>\n</header>', content)
    
    # 3. Envolver a calculadora em um calculator-container
    if '<div class="calculator-grid">' in content and '<div class="calculator-container">' not in content:
        content = content.replace('<div class="calculator-grid">', '<div class="calculator-container">\n    <div class="calculator-grid">')
        # Fechar o container após a grid (isso é um pouco mais complexo, vamos tentar basear no fechamento da grid)
        # Como as grids costumam terminar antes das info-sections
        content = content.replace('<!-- Espaço de Anúncios -->', '</div>\n    </div>\n    <!-- Espaço de Anúncios -->')

    # 4. Ajustar Info Sections para Info Cards
    content = content.replace('<div class="info-section">', '<div class="info-card">')
    
    # 5. Garantir que o main tenha a classe container para centralizar
    content = content.replace('<main>', '<main class="container">')

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

for filename in os.listdir(tools_dir):
    if filename.endswith(".html"):
        update_tool(os.path.join(tools_dir, filename))
