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
                    title_el = item.find("title")
                    link_el = item.find("link")
                    if title_el is not None and link_el is not None:
                        title = title_el.text
                        link = link_el.text
                        if title and link:
                            news_items.append({"title": title, "link": link})
        except Exception as e:
            print(f"Erro ao buscar {url}: {e}")
    return news_items

def generate_article(news_context):
    print("🤖 Gerando artigo com IA (EEAT, 1000+ palavras)...")

    prompt = f"""
Você é um jornalista especialista em finanças pessoais, com mais de 10 anos de experiência.
Crie um artigo de blog completo em Português do Brasil, baseado nesta notícia recente: "{news_context['title']}".

REQUISITOS OBRIGATÓRIOS:
1. Mínimo de 1000 palavras com conteúdo original e de alta qualidade.
2. Siga os princípios de EEAT do Google: demonstre Experiência, Especialidade, Autoridade e Confiança.
3. Escreva de forma humana, clara e envolvente — como um especialista real explicando para um amigo.
4. Formato: Markdown com Frontmatter do Jekyll.
5. Estrutura obrigatória:
   - Introdução contextualizada (2-3 parágrafos)
   - Pelo menos 4 subtítulos H2 com conteúdo substancial
   - Subtítulos H3 dentro de seções maiores
   - Listas com pelo menos 5 itens quando aplicável
   - Dicas práticas e acionáveis
   - Conclusão com chamada para reflexão
6. SEO: título descritivo e honesto (sem clickbait), meta description de 150-160 caracteres.
7. NÃO use: frases clichês de IA, promessas exageradas, linguagem sensacionalista.
8. NÃO inclua links externos de afiliados ou promoções comerciais.
9. Cite fontes quando mencionar dados ou estatísticas.
10. Adicione uma seção "Perguntas Frequentes" (FAQ) com pelo menos 3 perguntas e respostas.

Retorne APENAS o conteúdo no formato abaixo, sem texto adicional:
---
layout: post
title: "Título descritivo e informativo aqui"
date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} -0300
categories: [finanças, educação-financeira]
description: "Meta descrição informativa de 150-160 caracteres aqui"
author: "Equipe Grana Hoje"
---

Conteúdo completo do artigo aqui...
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=3000,
        temperature=0.7
    )
    content = response.choices[0].message.content

    # Remover qualquer marcador de afiliado que possa ter sobrado
    content = re.sub(r'\[AFFILIATE_TOP\]', '', content)
    content = re.sub(r'\[AFFILIATE_MIDDLE\]', '', content)
    content = re.sub(r'apretailer\.com\.br[^\s"\'<>]*', '', content)

    return content

def save_post(content):
    title_match = re.search(r'title: "(.*?)"', content)
    title = title_match.group(1) if title_match else "novo-post"
    slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
    # Limitar tamanho do slug
    slug = slug[:80]
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
    print(f"📰 Notícia selecionada: {selected['title']}")

    article_content = generate_article(selected)
    save_post(article_content)

    if os.path.exists("convert_md_to_html.py"):
        print("🔄 Convertendo Markdown para HTML...")
        os.system("python3 convert_md_to_html.py")

    if os.path.exists("rebuild_blog.py"):
        print("📊 Atualizando blog.html...")
        os.system("python3 rebuild_blog.py")

    if os.path.exists("update_index_news.py"):
        print("🏠 Atualizando página inicial...")
        os.system("python3 update_index_news.py")

    if os.path.exists("generate_main_sitemap.py"):
        print("🗺️ Atualizando sitemap...")
        os.system("python3 generate_main_sitemap.py")

    print("✅ Robô finalizado com sucesso!")

if __name__ == "__main__":
    main()
