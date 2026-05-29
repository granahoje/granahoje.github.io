import os
import re
from pathlib import Path
from bs4 import BeautifulSoup

root = Path('.')
index_file = root / 'index.html'
artigos_dir = root / 'artigos'

def get_latest_articles(count=3):
    articles = []
    # Pegar arquivos HTML na pasta artigos, ordenados por data de modificação (mais recentes primeiro)
    files = sorted(artigos_dir.glob('*.html'), key=os.path.getmtime, reverse=True)
    
    for p in files:
        if len(articles) >= count:
            break
        try:
            html = p.read_text(encoding='utf-8')
            soup = BeautifulSoup(html, 'html.parser')
            title = soup.title.string.replace(' - Grana Hoje', '') if soup.title else p.stem.replace('-', ' ').title()
            
            desc_meta = soup.find('meta', attrs={'name': 'description'})
            desc = desc_meta.get('content', '') if desc_meta else "Confira as últimas novidades financeiras no Grana Hoje."
            if len(desc) > 120: desc = desc[:117] + "..."

            articles.append({
                "title": title,
                "url": f"/artigos/{p.name}",
                "desc": desc
            })
        except:
            continue
    return articles

def update_index():
    articles = get_latest_articles(3)
    if not articles:
        return

    news_html = ""
    for art in articles:
        news_html += f"""
            <a href="{art['url']}" class="calc-card" style="text-decoration: none; display: block; background: var(--card); padding: 25px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.05); transition: all 0.3s;">
                <span style="font-size: 0.8rem; color: var(--primary); font-weight: 800; text-transform: uppercase; letter-spacing: 1px; display: block; margin-bottom: 10px;">Novo Artigo</span>
                <h3 style="font-size: 1.2rem; margin-bottom: 10px; color: #fff;">{art['title']}</h3>
                <p style="font-size: 0.9rem; color: var(--muted); margin-bottom: 15px;">{art['desc']}</p>
                <span style="color: var(--primary); font-weight: 700; font-size: 0.9rem;">Ler Agora →</span>
            </a>"""

    index_content = index_file.read_text(encoding='utf-8')
    pattern = re.compile(r'(<!-- NOVIDADES_ROBO_START -->.*?<div id="latestNews" class="news-grid".*?>).*?(</div>.*?<!-- NOVIDADES_ROBO_END -->)', re.DOTALL)
    
    if pattern.search(index_content):
        new_index_content = pattern.sub(rf'\1{news_html}\2', index_content)
        index_file.write_text(new_index_content, encoding='utf-8')
        print("✅ index.html atualizado com as últimas novidades.")
    else:
        print("❌ Marcadores de novidades não encontrados no index.html")

if __name__ == "__main__":
    update_index()
