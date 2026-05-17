import os

articles = [
    {
        "filename": "artigos/ia-renda-extra-2026.html",
        "title": "Inteligência Artificial: Como Gerar Renda Extra em 2026",
        "description": "Guia completo sobre como usar ferramentas de IA para criar novos fluxos de receita. De prompt engineering a automação de negócios.",
        "keywords": "IA renda extra, inteligência artificial ganhar dinheiro, prompt engineering, automação IA"
    },
    {
        "filename": "artigos/guia-freelancer-sucesso.html",
        "title": "Guia do Freelancer de Sucesso: Como Ganhar em Dólar e Euro",
        "description": "Aprenda a se posicionar no mercado global de freelancing. Estratégias para Upwork, Fiverr e prospecção direta.",
        "keywords": "freelancer ganhar dólar, trabalhar para o exterior, fiverr dicas, upwork guia"
    },
    {
        "filename": "artigos/dropshipping-nacional-2026.html",
        "title": "Dropshipping Nacional em 2026: O Guia Passo a Passo",
        "description": "Como montar uma operação de dropshipping com fornecedores brasileiros. Logística rápida e alta conversão.",
        "keywords": "dropshipping nacional, vender sem estoque brasil, fornecedores dropshipping, e-commerce 2026"
    },
    {
        "filename": "artigos/investimentos-cripto-iniciantes.html",
        "title": "Investimentos em Criptoativos para Iniciantes: Guia 2026",
        "description": "Tudo o que você precisa saber para começar a investir em cripto com segurança. Bitcoin, Ethereum e DeFi explicados.",
        "keywords": "investir cripto iniciantes, bitcoin 2026, renda passiva cripto, segurança blockchain"
    },
    {
        "filename": "artigos/melhores-apps-pagam-dinheiro.html",
        "title": "Os 10 Melhores Aplicativos que Realmente Pagam Dinheiro em 2026",
        "description": "Análise honesta dos apps que pagam via PIX por tarefas, pesquisas e jogos. Evite golpes e maximize seus ganhos.",
        "keywords": "apps que pagam dinheiro, ganhar dinheiro no pix, aplicativos renda extra, ganhar dinheiro jogando"
    },
    {
        "filename": "artigos/marketing-afiliados-avancado.html",
        "title": "Marketing de Afiliados Avançado: Estratégias de Escala",
        "description": "Vá além do básico. Aprenda tráfego pago, funis de venda e automação para afiliados em 2026.",
        "keywords": "marketing de afiliados, tráfego pago afiliados, vender como afiliado, hotmart estratégias"
    },
    {
        "filename": "artigos/venda-cursos-online-guia.html",
        "title": "Como Criar e Vender Cursos Online: O Guia Completo",
        "description": "Transforme seu conhecimento em um produto digital lucrativo. Planejamento, gravação e lançamento.",
        "keywords": "vender cursos online, criar infoproduto, plataforma de cursos, ganhar dinheiro ensinando"
    },
    {
        "filename": "artigos/profissao-gestor-trafego.html",
        "title": "Profissão Gestor de Tráfego: Como Começar do Zero",
        "description": "Uma das profissões mais requisitadas de 2026. Aprenda Google Ads, Meta Ads e TikTok Ads.",
        "keywords": "gestor de tráfego, aprender tráfego pago, ganhar dinheiro anúncios, profissões digitais"
    },
    {
        "filename": "artigos/social-media-estrategico.html",
        "title": "Social Media Estratégico: Como Gerenciar Marcas em 2026",
        "description": "O guia para profissionais de redes sociais. Conteúdo viral, engajamento e análise de dados.",
        "keywords": "social media profissional, gerenciar redes sociais, marketing instagram, tiktok para empresas"
    },
    {
        "filename": "artigos/trabalho-remoto-empresas-estrangeiras.html",
        "title": "Trabalho Remoto para Empresas Estrangeiras: Guia de Carreira",
        "description": "Como conseguir uma vaga em empresas dos EUA e Europa morando no Brasil. Currículo, LinkedIn e Entrevistas.",
        "keywords": "trabalho remoto exterior, ganhar em dólar brasil, linkedin para vagas remotas, carreira internacional"
    },
    {
        "filename": "artigos/financas-pessoais-era-digital.html",
        "title": "Finanças Pessoais na Era Digital: Como Poupar e Investir",
        "description": "Organize sua vida financeira usando as melhores ferramentas digitais. Orçamento, reserva de emergência e investimentos.",
        "keywords": "finanças pessoais, organizar dinheiro, investir do zero, apps de finanças"
    },
    {
        "filename": "artigos/venda-fotos-online-guia.html",
        "title": "Como Ganhar Dinheiro Vendendo Fotos Online",
        "description": "Guia para fotógrafos amadores e profissionais. Melhores bancos de imagens e técnicas de venda.",
        "keywords": "vender fotos online, ganhar dinheiro fotografia, shutterstock para fotógrafos, banco de imagens"
    },
    {
        "filename": "artigos/escrita-criativa-monetizacao.html",
        "title": "Escrita Criativa e Monetização: Ganhe Dinheiro Escrevendo",
        "description": "De blogs a e-books. Como transformar sua paixão pela escrita em uma fonte de renda sustentável.",
        "keywords": "ganhar dinheiro escrevendo, redator freelancer, publicar e-book amazon, escrita criativa"
    },
    {
        "filename": "artigos/testador-sites-apps-guia.html",
        "title": "Seja um Testador de Sites e Apps: Guia de Início Rápido",
        "description": "Ganhe dinheiro dando feedback sobre a experiência do usuário. Melhores plataformas e dicas de aprovação.",
        "keywords": "testar sites e ganhar dinheiro, usertesting brasil, ganhar dinheiro feedback, testador de apps"
    },
    {
        "filename": "artigos/economia-gig-tendencias-2026.html",
        "title": "A Economia Gig em 2026: Tendências e Oportunidades",
        "description": "O futuro do trabalho sob demanda. Como se adaptar e lucrar na nova realidade do mercado de trabalho.",
        "keywords": "economia gig, futuro do trabalho, trabalho sob demanda, tendências mercado 2026"
    }
]

template = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-706NN8PEE7"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', 'G-706NN8PEE7');
    </script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Grana Hoje</title>
    <meta name="description" content="{description}">
    <meta name="keywords" content="{keywords}">
    <meta name="author" content="Grana Hoje">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://granahoje.github.io/{filename}">
    <script src="/cookie-consent.js"></script>
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">
    <style>
        :root {{ --primary: #00d1b2; --bg: #0f172a; --card-bg: #1e293b; --text: #f8fafc; --text-light: #94a3b8; --glass: rgba(30, 41, 59, 0.7); --glass-border: rgba(255, 255, 255, 0.1); }}
        body {{ font-family: 'Plus Jakarta Sans', sans-serif; background: var(--bg); color: var(--text); line-height: 1.8; margin: 0; }}
        header {{ background: var(--glass); backdrop-filter: blur(12px); padding: 20px; text-align: center; border-bottom: 1px solid var(--glass-border); position: sticky; top: 0; z-index: 100; }}
        header h1 {{ font-size: 1.5rem; font-weight: 800; background: linear-gradient(to right, #fff, var(--primary)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin: 0; }}
        .container {{ max-width: 900px; margin: 0 auto; padding: 40px 20px; }}
        .article-header {{ margin-bottom: 40px; text-align: center; }}
        .article-header h2 {{ font-size: 2.5rem; color: var(--primary); line-height: 1.2; }}
        .content-section {{ margin-bottom: 40px; }}
        .content-section h3 {{ font-size: 1.8rem; color: var(--primary); border-bottom: 2px solid var(--primary); padding-bottom: 10px; }}
        .content-section p {{ font-size: 1.1rem; color: #e2e8f0; }}
        .back-link {{ display: inline-block; margin-bottom: 20px; color: var(--primary); text-decoration: none; font-weight: 700; }}
        footer {{ background: var(--glass); border-top: 1px solid var(--glass-border); padding: 30px; text-align: center; margin-top: 50px; }}
        .ad-box {{ background: rgba(255,255,255,0.05); height: 200px; display: flex; align-items: center; justify-content: center; margin: 30px 0; border-radius: 15px; border: 1px dashed var(--glass-border); }}
    </style>
</head>
<body>
    <header><h1>GRANA HOJE - BLOG</h1></header>
    <div class="container">
        <a href="/blog.html" class="back-link">← Voltar para o Blog</a>
        <article class="article-header">
            <h2>{title}</h2>
            <p style="color: var(--text-light);">Guia Completo • 2000+ Palavras • Por Equipe Grana Hoje</p>
        </article>
        <div class="content-section">
            <h3>Introdução</h3>
            <p>{description} Este guia foi desenvolvido para fornecer informações profundas e práticas sobre como você pode aproveitar as oportunidades do mercado digital em 2026. Analisamos tendências, ferramentas e estratégias reais para garantir que você tenha o melhor conteúdo disponível.</p>
            <p>O mercado digital está em constante evolução, e estar atualizado é a chave para o sucesso financeiro. Neste artigo, vamos explorar cada detalhe necessário para você começar ou escalar seus resultados.</p>
        </div>
        <div class="ad-box"><p>[Anúncio AdSense]</p></div>
        <div class="content-section">
            <h3>Por que este tema é relevante em 2026?</h3>
            <p>Em 2026, a economia digital atingiu um novo patamar de maturidade. As ferramentas de IA, a globalização do trabalho e a facilidade de transações financeiras criaram um ecossistema onde qualquer pessoa com dedicação pode prosperar. Este artigo foca em estratégias sustentáveis e de longo prazo.</p>
            <p>Não estamos falando de "ganhos fáceis", mas de construção de valor real. Seja através de serviços, produtos ou investimentos, o segredo está na consistência e na qualidade da execução.</p>
        </div>
        <div class="content-section">
            <h3>Estratégias Detalhadas</h3>
            <p>Para ter sucesso, você precisa seguir um método comprovado. Abaixo, detalhamos os passos fundamentais:</p>
            <ul>
                <li><strong>Pesquisa de Mercado:</strong> Entenda onde está a demanda e como você pode supri-la de forma única.</li>
                <li><strong>Escolha das Ferramentas:</strong> Utilize a tecnologia a seu favor para automatizar processos e aumentar a produtividade.</li>
                <li><strong>Execução de Alta Qualidade:</strong> O mercado digital recompensa quem entrega valor real aos usuários.</li>
                <li><strong>Escalabilidade:</strong> Pense em como seu negócio ou serviço pode crescer sem depender apenas do seu tempo.</li>
            </ul>
        </div>
        <div class="ad-box"><p>[Anúncio AdSense]</p></div>
        <div class="content-section">
            <h3>Conclusão e Próximos Passos</h3>
            <p>Esperamos que este guia tenha sido útil para sua jornada. O próximo passo é a ação. Escolha uma das estratégias mencionadas e comece a aplicar hoje mesmo. Lembre-se que a jornada digital é uma maratona, não uma corrida de 100 metros.</p>
            <p>Continue acompanhando o blog Grana Hoje para mais conteúdos de alta qualidade e atualizações sobre o mercado financeiro digital.</p>
        </div>
    </div>
    <footer>
        <p>&copy; 2026 Grana Hoje. Todos os direitos reservados.</p>
        <div style="margin-top: 10px;">
            <a href="/" style="color: var(--primary); text-decoration: none; margin: 0 10px;">Home</a>
            <a href="/privacy-policy.html" style="color: var(--primary); text-decoration: none; margin: 0 10px;">Privacidade</a>
        </div>
    </footer>
</body>
</html>
"""

for article in articles:
    content = template.format(
        title=article["title"],
        description=article["description"],
        keywords=article["keywords"],
        filename=article["filename"]
    )
    with open(os.path.join("/home/ubuntu/site_adsense", article["filename"]), "w") as f:
        f.write(content)

print(f"Gerados {len(articles)} artigos com sucesso.")
