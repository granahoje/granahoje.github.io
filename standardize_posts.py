import os
import re

# Configurações
BASE_DIR = "."
ARTIGOS_DIR = "artigos"
CSS_FILE = "css/style.css"
FOOTER_FILE = "footer-standard.html"

# Carregar o footer padrão
with open(FOOTER_FILE, 'r', encoding='utf-8') as f:
    FOOTER_CONTENT = f.read()

# Estilo CSS padrão (baseado no que vimos)
STANDARD_HEAD = """<head>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4896859041377751" crossorigin="anonymous"></script>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-706NN8PEE7"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-706NN8PEE7');
    </script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/css/style.css">
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
"""

STANDARD_HEADER = """
<header>
    <div class="logo">GRANA HOJE</div>
    <nav>
        <a href="/">Home</a>
        <a href="/blog.html">Blog</a>
        <a href="/sobre.html">Sobre</a>
        <a href="/contato.html">Contato</a>
    </nav>
</header>
"""

def standardize_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extrair título e descrição
    title_match = re.search(r'<title>(.*?)</title>', content)
    desc_match = re.search(r'<meta name="description" content="(.*?)">', content)
    
    title = title_match.group(1) if title_match else "Grana Hoje"
    description = desc_match.group(1) if desc_match else ""

    # Extrair o conteúdo principal (dentro de .container ou body)
    # Tenta pegar o que está dentro da div container se existir
    container_match = re.search(r'<div class="container">(.*?)</div>\s*<footer>', content, re.DOTALL)
    if not container_match:
        container_match = re.search(r'<body>(.*?)<footer>', content, re.DOTALL)
    
    main_content = container_match.group(1) if container_match else ""
    
    # Limpar o conteúdo principal de headers e links de volta antigos
    main_content = re.sub(r'<header>.*?</header>', '', main_content, flags=re.DOTALL)
    main_content = re.sub(r'<a class="back".*?</a>', '', main_content)
    
    # Montar o novo HTML
    new_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
{STANDARD_HEAD}
    <title>{title}</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="https://granahoje.github.io/{file_path}">
</head>
<body>
{STANDARD_HEADER}
<div class="container">
    <a href="/blog.html" class="back-link">← Voltar para o Blog</a>
    {main_content}
</div>
{FOOTER_CONTENT}
</body>
</html>"""
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f"Padronizado: {file_path}")

# Lista das 10 postagens (baseado nos arquivos mais recentes e no contexto)
posts_to_fix = [
    "artigos/pix-infinito-app-50-reais-cadastro.html",
    "artigos/profissao-gestor-trafego.html",
    "artigos/psicologia-do-dinheiro-mentalidade-riqueza.html",
    "artigos/renda-extra-online.html",
    "artigos/renda-passiva-com-aluguel-de-equipamentos.html",
    "artigos/segredo-milionarios-pix-apps-pouco-conhecidos.html",
    "artigos/seguranca-automacao-residencial-voz.html",
    "artigos/social-fi-renda-extra.html",
    "artigos/social-media-estrategico.html",
    "artigos/testador-sites-apps-guia.html",
    "artigos/trabalho-remoto-assistente-virtual-2026.html",
    "artigos/trabalho-remoto-empresas-estrangeiras.html",
    "artigos/venda-cursos-online-guia.html",
    "artigos/venda-digital-assets-ia.html",
    "artigos/venda-fotos-online-guia.html"
]

for post in posts_to_fix:
    if os.path.exists(post):
        standardize_html(post)

# Padronizar a calculadora também
calc_path = "ferramentas/salary-split-calculator/index.html"
if os.path.exists(calc_path):
    standardize_html(calc_path)

