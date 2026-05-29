import os
import re
from pathlib import Path
from bs4 import BeautifulSoup
from datetime import datetime

root = Path('.')
index_file = root / 'index.html'
artigos_dir = root / 'artigos'

def get_latest_articles(count=3):
    articles = []
    files = sorted(artigos_dir.glob('*.html'), key=os.path.getmtime, reverse=True)
    
    for p in files:
        if len(articles) >= count:
            break
        try:
            mtime = os.path.getmtime(p)
            dt_str = datetime.fromtimestamp(mtime).strftime("%d/%m/%Y às %H:%M")
            
            html = p.read_text(encoding='utf-8')
            soup = BeautifulSoup(html, 'html.parser')
            title = soup.title.string.replace(' - Grana Hoje', '') if soup.title else p.stem.replace('-', ' ').title()
            
            desc_meta = soup.find('meta', attrs={'name': 'description'})
            desc = desc_meta.get('content', '') if desc_meta else "Confira as últimas novidades financeiras no Grana Hoje."
            if len(desc) > 120: desc = desc[:117] + "..."

            articles.append({
                "title": title,
                "url": f"/artigos/{p.name}",
                "desc": desc,
                "date": dt_str
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
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                    <span style="font-size: 0.75rem; color: var(--primary); font-weight: 800; text-transform: uppercase; letter-spacing: 1px;">Novo Artigo</span>
                    <span style="font-size: 0.7rem; color: var(--muted);">{art['date']}</span>
                </div>
                <h3 style="font-size: 1.2rem; margin-bottom: 10px; color: #fff;">{art['title']}</h3>
                <p style="font-size: 0.9rem; color: var(--muted); margin-bottom: 15px;">{art['desc']}</p>
                <span style="color: var(--primary); font-weight: 700; font-size: 0.9rem;">Ler Agora →</span>
            </a>"""

    index_content = index_file.read_text(encoding='utf-8')
    pattern = re.compile(r'(<!-- NOVIDADES_ROBO_START -->.*?<div id="latestNews" class="news-grid".*?>).*?(</div>.*?<!-- NOVIDADES_ROBO_END -->)', re.DOTALL)
    
    if pattern.search(index_content):
        new_index_content = pattern.sub(rf'\1{news_html}\2', index_content)
        index_file.write_text(new_index_content, encoding='utf-8')
        print("✅ index.html atualizado com data e hora.")
    else:
        print("❌ Marcadores não encontrados.")

if __name__ == "__main__":
    update_index()
