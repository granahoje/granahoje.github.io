import os
import requests
import json
import re
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

# Links de Afiliado (Serão preenchidos quando o usuário enviar)
AFFILIATE_TOP = "" 
AFFILIATE_MIDDLE = ""

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
    
    # Inserir placeholders para afiliados no prompt
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
    
    # Substituir placeholders pelos links reais (se existirem)
    top_html = f'<div class="cta-top" style="margin:20px 0;padding:20px;background:#f0fff4;border-radius:10px;border:1px solid #22c55e;text-align:center;"><a href="{AFFILIATE_TOP}" style="font-weight:bold;color:#15803d;text-decoration:none;">🚀 Dica de Hoje: Aproveite esta oportunidade de Renda Extra &rarr;</a></div>' if AFFILIATE_TOP else ""
    mid_html = f'<div class="cta-mid" style="margin:20px 0;padding:20px;background:#fffbeb;border-radius:10px;border:1px solid #f59e0b;text-align:center;"><a href="{AFFILIATE_MIDDLE}" style="font-weight:bold;color:#b45309;text-decoration:none;">💡 Recomendação Especial: Comece a investir com segurança &rarr;</a></div>' if AFFILIATE_MIDDLE else ""
    
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
        
    import random
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
