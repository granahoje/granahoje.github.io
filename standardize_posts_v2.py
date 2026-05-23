import os
import re

# Configurações
BASE_DIR = "."
CSS_FILE = "css/style.css"
FOOTER_FILE = "footer-standard.html"
BASE_URL = "https://granahoje.github.io/"

languages = {
    "pt-br": "artigos/",
    "ar": "ar/artigos/",
    "bn": "bn/artigos/",
    "en": "en/artigos/",
    "es": "es/artigos/",
    "fr": "fr/artigos/",
    "hi": "hi/artigos/",
    "ja": "ja/artigos/",
    "pt-pt": "pt-pt/artigos/",
    "ru": "ru/artigos/",
    "zh": "zh/artigos/"
}

# Carregar o footer padrão
with open(FOOTER_FILE, 'r', encoding='utf-8') as f:
    FOOTER_CONTENT = f.read()

STANDARD_HEAD_START = """<head>
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

def get_hreflang_tags(filename):
    tags = []
    for lang, folder in languages.items():
        url = f"{BASE_URL}{folder}{filename}"
        tags.append(f'    <link rel="alternate" hreflang="{lang}" href="{url}" />')
    tags.append(f'    <link rel="alternate" hreflang="x-default" href="{BASE_URL}artigos/{filename}" />')
    return "\n".join(tags)

def standardize_html(file_path, is_article=True):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    filename = os.path.basename(file_path)
    title_match = re.search(r'<title>(.*?)</title>', content)
    desc_match = re.search(r'<meta name="description" content="(.*?)">', content)
    
    title = title_match.group(1) if title_match else "Grana Hoje"
    description = desc_match.group(1) if desc_match else ""

    # Tenta extrair o conteúdo principal
    container_match = re.search(r'<div class="container">(.*?)</div>\s*(?:<footer|</body>)', content, re.DOTALL)
    if not container_match:
        container_match = re.search(r'<body>(.*?)<footer>', content, re.DOTALL)
    
    main_content = container_match.group(1) if container_match else ""
    main_content = re.sub(r'<header>.*?</header>', '', main_content, flags=re.DOTALL)
    main_content = re.sub(r'<a class="back".*?</a>', '', main_content)
    main_content = re.sub(r'<a href="/blog.html" class="back-link">.*?</a>', '', main_content)

    hreflangs = get_hreflang_tags(filename) if is_article else ""
    canonical = f"{BASE_URL}{file_path.replace('./', '')}"

    new_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
{STANDARD_HEAD_START}
    <title>{title}</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="{canonical}">
{hreflangs}
</head>
<body>
{STANDARD_HEADER}
<div class="container">
    <a href="/blog.html" class="back-link">← Voltar para o Blog</a>
    {main_content.strip()}
</div>
{FOOTER_CONTENT}
</body>
</html>"""
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f"Padronizado: {file_path}")

# Artigos em português
articles = [f for f in os.listdir("artigos") if f.endswith(".html")]
for art in articles:
    standardize_html(os.path.join("artigos", art))

# Calculadora
calc_path = "ferramentas/salary-split-calculator/index.html"
if os.path.exists(calc_path):
    standardize_html(calc_path, is_article=False)

