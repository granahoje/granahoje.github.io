import os, re
from pathlib import Path
from bs4 import BeautifulSoup

root = Path('/home/ubuntu/granahoje.github.io')
artigos_dir = root / 'artigos'
blog_file = root / 'blog.html'

def get_article_data(p):
    try:
        html = p.read_text(encoding='utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.title.string if soup.title else p.stem.replace('-', ' ').title()
        
        # Tentar pegar uma descrição ou o primeiro parágrafo
        desc_meta = soup.find('meta', attrs={'name': 'description'})
        if desc_meta:
            desc = desc_meta.get('content', '')
        else:
            first_p = soup.find('p')
            desc = first_p.get_text()[:150] + '...' if first_p else "Leia mais sobre este assunto no Grana Hoje."
            
        return {
            "title": title,
            "url": f"/artigos/{p.name}",
            "desc": desc,
            "meta": "Artigo • 2026"
        }
    except:
        return None

def rebuild():
    artigos = []
    for p in sorted(artigos_dir.glob('*.html'), reverse=True):
        data = get_article_data(p)
        if data: artigos.append(data)
    
    print(f"Encontrados {len(artigos)} artigos.")
    
    blog_html = blog_file.read_text(encoding='utf-8')
    
    # Gerar o HTML dos cards
    cards_html = ""
    for art in artigos:
        cards_html += f"""
        <article class="post-card">
            <div class="article-meta">{art['meta']}</div>
            <h3>{art['title']}</h3>
            <p>{art['desc']}</p>
            <a class="read-more" href="{art['url']}">Ler Artigo Completo</a>
        </article>"""
    
    # Substituir o conteúdo da grid no blog.html
    # Usando regex para encontrar a seção articles-grid
    pattern = re.compile(r'(<section class="articles-grid" id="articlesGrid">).*?(</section>)', re.DOTALL)
    new_blog_html = pattern.sub(rf'\1{cards_html}\2', blog_html)
    
    blog_file.write_text(new_blog_html, encoding='utf-8')
    print("blog.html atualizado com sucesso.")

rebuild()
