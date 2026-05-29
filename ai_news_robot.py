import os
import requests
import json
import re
import random
from datetime import datetime
from xml.etree import ElementTree as ET
from openai import OpenAI

# Configurações
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
NEWS_FEEDS = [
    "https://news.google.com/rss/search?q=finanças+pessoais+investimentos+renda+extra&hl=pt-BR&gl=BR&ceid=BR:pt-419",
    "https://www.infomoney.com.br/feed/",
    "https://exame.com/feed/"
]

# Lista de Afiliados
AFFILIATES = [
    {"name": "Picpay-Abertura de Conta PJ", "url": "https://apretailer.com.br/click/6a16869a2bfa81783858cd52/188415/359067/subaccount"},
    {"name": "Santander", "url": "https://apretailer.com.br/click/6a16869a2bfa8178566a06a2/188413/359067/subaccount"},
    {"name": "BTG Pactual", "url": "https://apretailer.com.br/click/6a16869a2bfa81793e50f472/188400/359067/subaccount"},
    {"name": "Pagbank Maquininha", "url": "https://apretailer.com.br/click/6a16869a2bfa81782b6be242/186226/359067/subaccount"},
    {"name": "Banco BV – Empréstimo com Garantia Veicular", "url": "https://apretailer.com.br/click/6a0bab802bfa817b7f1a79b2/188286/358980/subaccount"},
    {"name": "Velotax", "url": "https://apretailer.com.br/click/6a0bab802bfa817b783708b2/188130/358980/subaccount"},
    {"name": "Bybit", "url": "https://apretailer.com.br/click/6a16869a2bfa8178f62a16f2/188136/359067/subaccount"},
    {"name": "HIPER CASH", "url": "https://apretailer.com.br/click/6a16869a2bfa8178cb6134b2/182687/359067/subaccount"},
    {"name": "Remessa Online", "url": "https://apretailer.com.br/click/6a16869b2bfa8178cb6134b3/187944/359067/subaccount"},
    {"name": "Juca - Antecipação de FGTS", "url": "https://apretailer.com.br/click/6a16869a2bfa81789e2c3462/187799/359067/subaccount"},
    {"name": "Santander PJ - Abertura de conta", "url": "https://apretailer.com.br/click/6a16869b2bfa81789e2c3464/187773/359067/subaccount"},
    {"name": "Cartão Carrefour", "url": "https://apretailer.com.br/click/6a16869a2bfa8178d8192fa2/188544/359067/subaccount"},
    {"name": "Cartão Atacadão", "url": "https://apretailer.com.br/click/6a16869b2bfa817868268623/188543/359067/subaccount"},
    {"name": "Crypto.com", "url": "https://apretailer.com.br/click/6a16869a2bfa8179143c12b2/187745/359067/subaccount"},
    {"name": "Quita Boletos", "url": "https://apretailer.com.br/click/6a16869a2bfa817908298d82/188352/359067/subaccount"},
    {"name": "Santander Acordos", "url": "https://apretailer.com.br/click/6a16869a2bfa817868268622/187700/359067/subaccount"},
    {"name": "Acordo Certo", "url": "https://apretailer.com.br/click/6a16869a2bfa817115280f72/187558/359067/subaccount"},
    {"name": "CASATRADE", "url": "https://apretailer.com.br/click/6a0bab802bfa817bc269d5c2/186975/358980/subaccount"},
    {"name": "Credspot - FGTS", "url": "https://apretailer.com.br/click/6a0bab802bfa817bbc03aef2/186580/358980/subaccount"},
    {"name": "Consigmais - SIAPE", "url": "https://apretailer.com.br/click/6a0bab802bfa817bce432822/186657/358980/subaccount"},
    {"name": "Olymp Trade FTD Bitcoin", "url": "https://apretailer.com.br/click/6a0bab802bfa817bd42023d4/178147/358980/subaccount"},
    {"name": "PicPay - Abertura de contas", "url": "https://apretailer.com.br/click/6a0bab802bfa8139b3579842/186179/358980/subaccount"},
    {"name": "MINUTO SEGUROS", "url": "https://apretailer.com.br/click/6a0bab802bfa8144cc0ad9b2/183524/358980/subaccount"},
    {"name": "Ourocard", "url": "https://apretailer.com.br/click/6a0bab802bfa81391c4d5ee2/185834/358980/subaccount"},
    {"name": "Consigmais - FGTS", "url": "https://apretailer.com.br/click/6a0bab802bfa817be02f00a2/184986/358980/subaccount"},
    {"name": "Consigmais - INSS", "url": "https://apretailer.com.br/click/6a16869a2bfa81788059e072/184987/359067/subaccount"},
    {"name": "Acordo Certo - Negociação de Dívidas", "url": "https://apretailer.com.br/click/6a0bab802bfa81398f1142c2/182268/358980/subaccount"},
    {"name": "BomPraCrédito - Empréstimo Pessoal", "url": "https://apretailer.com.br/click/6a16869a2bfa8178b15f7aa6/185636/359067/subaccount"},
    {"name": "Nexo - Plataforma de ativos digitais", "url": "https://apretailer.com.br/click/6a0bab802bfa81394d4c4542/184515/358980/subaccount"},
    {"name": "Juros Baixos - Empréstimos", "url": "https://apretailer.com.br/click/6a16869a2bfa8178622cf8c2/183012/359067/subaccount"},
    {"name": "Juros Baixos - Empréstimo pessoal", "url": "https://apretailer.com.br/click/6a0bab802bfa81394742c132/179945/358980/subaccount"},
    {"name": "SuperSim - Empréstimo Pessoal", "url": "https://apretailer.com.br/click/6a0bab802bfa8139047c0492/177702/358980/subaccount"},
    {"name": "UP.P Empréstimos", "url": "https://apretailer.com.br/click/6a0bab802bfa8139352802e2/179925/358980/subaccount"}
]

client = OpenAI(api_key=OPENAI_API_KEY)

def fetch_latest_news():
    print("🔍 Buscando notícias online...")
    news_items = []
    for url in NEWS_FEEDS:
        try:
            resp = requests.get(url, timeout=15)
            if resp.status_code == 200:
                root = ET.fromstring(resp.content)
                for item in root.findall(".//item")[:5]:
                    title = item.find("title").text
                    link = item.find("link").text
                    news_items.append({"title": title, "link": link})
        except Exception as e:
            print(f"Erro ao buscar {url}: {e}")
    return news_items

def generate_article(news_context):
    print("🤖 Gerando artigo com IA (EEAT, 800+ palavras)...")
    
    prompt = f"""
    Você é um especialista em finanças e SEO. Crie um artigo de blog em Português do Brasil baseado nesta notícia recente: "{news_context['title']}".
    
    REQUISITOS OBRIGATÓRIOS:
    1. Mínimo de 800 palavras.
    2. Foco em EEAT (Experiência, Especialidade, Autoridade e Confiança).
    3. Estilo de escrita humano, envolvente e prático.
    4. Formato: Markdown (com Frontmatter do Jekyll).
    5. Estrutura: Introdução impactante, subtítulos H2 e H3, listas, dicas práticas e conclusão forte.
    6. SEO: Use palavras-chave naturalmente, crie um título chamativo e uma meta description.
    7. NÃO use frases clichês de IA (ex: "No mundo dinâmico de hoje").
    8. Insira o marcador [AFFILIATE_TOP] logo após o primeiro parágrafo.
    9. Insira o marcador [AFFILIATE_MIDDLE] exatamente no meio do artigo (após um subtítulo H2).
    
    Retorne o conteúdo no formato:
    ---
    layout: post
    title: "Título SEO"
    date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} -0300
    categories: [finanças, renda-extra]
    description: "Meta descrição aqui"
    ---
    # Título do Post
    Conteúdo aqui...
    """
    
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    content = response.choices[0].message.content
    
    # Selecionar 2 afiliados aleatórios para este post
    af1, af2 = random.sample(AFFILIATES, 2)
    
    top_html = f'<div class="cta-top" style="margin:20px 0;padding:25px;background:linear-gradient(135deg, #f0fff4 0%, #dcfce7 100%);border-radius:15px;border:2px solid #22c55e;text-align:center;box-shadow:0 4px 12px rgba(0,0,0,0.05);"><h4 style="margin:0 0 10px;color:#15803d;">🚀 Oportunidade Selecionada</h4><p style="margin:0 0 15px;color:#166534;">{af1["name"]}: Uma das melhores opções para o seu perfil financeiro hoje.</p><a href="{af1["url"]}" target="_blank" style="display:inline-block;padding:12px 25px;background:#22c55e;color:white;font-weight:900;text-decoration:none;border-radius:8px;transition:all 0.3s;">ACESSAR AGORA &rarr;</a></div>'
    
    mid_html = f'<div class="cta-mid" style="margin:30px 0;padding:25px;background:linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%);border-radius:15px;border:2px solid #f59e0b;text-align:center;box-shadow:0 4px 12px rgba(0,0,0,0.05);"><h4 style="margin:0 0 10px;color:#b45309;">💡 Recomendação do Especialista</h4><p style="margin:0 0 15px;color:#92400e;">{af2["name"]}: Potencialize seus resultados com esta ferramenta testada.</p><a href="{af2["url"]}" target="_blank" style="display:inline-block;padding:12px 25px;background:#f59e0b;color:white;font-weight:900;text-decoration:none;border-radius:8px;transition:all 0.3s;">CONFERIR DETALHES &rarr;</a></div>'
    
    content = content.replace("[AFFILIATE_TOP]", top_html)
    content = content.replace("[AFFILIATE_MIDDLE]", mid_html)
    
    return content

def save_post(content):
    title_match = re.search(r'title: "(.*?)"', content)
    title = title_match.group(1) if title_match else "novo-post"
    slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"_posts/{date_str}-{slug}.md"
    
    os.makedirs("_posts", exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Post salvo: {filename}")
    return filename

def main():
    if not OPENAI_API_KEY:
        print("❌ Erro: OPENAI_API_KEY não configurada.")
        return
        
    news = fetch_latest_news()
    if not news:
        print("❌ Nenhuma notícia encontrada.")
        return
        
    selected = random.choice(news)
    
    article_content = generate_article(selected)
    save_post(article_content)
    
    if os.path.exists("convert_md_to_html.py"):
        print("🔄 Convertendo Markdown para HTML...")
        os.system("python3 convert_md_to_html.py")
        
    if os.path.exists("rebuild_blog.py"):
        print("📊 Atualizando blog.html...")
        os.system("python3 rebuild_blog.py")

if __name__ == "__main__":
    main()
