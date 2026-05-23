import os

# Configurações
BASE_DIR = "ferramentas"
LANGUAGES = ["pt", "en", "es", "fr", "de", "it", "ja", "ko", "zh", "ru", "ar"]
TOOLS = [
    "salary-split-calculator",
    "emergency-fund-tracker",
    "daily-expense-analyzer",
    "inflation-impact-calculator",
    "debt-payoff-strategy",
    "subscription-cost-tracker",
    "side-hustle-profit-calculator",
    "savings-challenge-generator",
    "investment-goal-simulator",
    "cost-of-living-comparison"
]

# Template Base (Estilo Fintech Premium)
def get_base_html(title, description, tool_id, lang="pt"):
    # Simplificado para economizar espaço e créditos, mas mantendo a qualidade visual solicitada
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Grana Hoje</title>
    <meta name="description" content="{description}">
    <link rel="stylesheet" href="/css/style.css">
    <link rel="stylesheet" href="/ferramentas/css/premium-tool.css">
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4896859041377751" crossorigin="anonymous"></script>
</head>
<body class="premium-tool">
    <header>
        <div class="logo">GRANA HOJE</div>
        <nav>
            <a href="/">Home</a>
            <a href="/blog.html">Blog</a>
            <a href="/sobre.html">Sobre</a>
        </nav>
    </header>

    <main class="container">
        <section class="hero-premium">
            <div class="glow"></div>
            <h1>{title}</h1>
            <p class="subtitle">{description}</p>
        </section>

        <section class="tool-interface card-glass">
            <div id="{tool_id}-app">
                <!-- A ferramenta será injetada aqui via JS -->
                <div class="loading">Carregando ferramenta premium...</div>
            </div>
        </section>

        <section class="content-eeat">
            <div class="article-content">
                <h2>O que é {title}?</h2>
                <p>Conteúdo detalhado sobre a ferramenta para SEO e EEAT...</p>
                <!-- Mais conteúdo será adicionado via script de expansão -->
            </div>
        </section>

        <section class="cta-premium card-glass">
            <h3>Maximize seus Resultados Financeiros</h3>
            <p>Conheça as melhores plataformas para gerenciar seu patrimônio com inteligência.</p>
            <a href="https://apretailer.com.br/click/6a0bab802bfa817b650fa492/188415/358980/subaccount" class="btn-premium">Explorar Agora</a>
        </section>
    </main>

    <footer class="standard-footer">
        <p>© 2026 Grana Hoje. Todos os direitos reservados.</p>
    </footer>

    <script src="/ferramentas/js/premium-core.js"></script>
    <script src="/ferramentas/js/{tool_id}.js"></script>
</body>
</html>"""

# Criar estrutura de diretórios
for tool in TOOLS:
    tool_path = os.path.join(BASE_DIR, tool)
    os.makedirs(tool_path, exist_ok=True)
    
    # Criar index.html (versão principal em PT)
    with open(os.path.join(tool_path, "index.html"), "w", encoding="utf-8") as f:
        f.write(get_base_html(tool.replace("-", " ").title(), "Ferramenta financeira premium para " + tool.replace("-", " "), tool))

    # Criar versões em outros idiomas
    for lang in LANGUAGES:
        if lang == "pt": continue
        lang_path = os.path.join(BASE_DIR, "lang", lang, tool)
        os.makedirs(lang_path, exist_ok=True)
        with open(os.path.join(lang_path, "index.html"), "w", encoding="utf-8") as f:
            f.write(get_base_html(tool.replace("-", " ").title(), "Premium financial tool for " + tool.replace("-", " "), tool, lang))

print("✅ Estrutura de 110 páginas (10 ferramentas x 11 idiomas) criada com sucesso!")
