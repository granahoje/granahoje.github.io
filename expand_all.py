import os, json, re, time
from pathlib import Path
from bs4 import BeautifulSoup
from openai import OpenAI

client = OpenAI()
root = Path('/home/ubuntu/granahoje.github.io')

def get_content(soup):
    return soup.find('main') or soup.find('article') or soup.find('div', class_='container')

def expand_text(title, current_text, lang='pt-BR'):
    prompt = f"Expand this article titled '{title}' to over 1000 words in {lang}. Focus on financial education, SEO optimization, and professional tone. Use H2/H3 tags. Return ONLY the HTML content. Current text: {current_text[:500]}"
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except:
        return None

def process():
    with open('/home/ubuntu/granahoje.github.io/audit_v2_results.json', 'r') as f:
        audit = json.load(f)
    
    short_list = [a for a in audit['short_articles'] if 'artigos/' in a['file']]
    print(f"Total para expandir: {len(short_list)}")
    
    for i, art in enumerate(short_list):
        fpath = root / art['file']
        if not fpath.exists(): continue
        
        print(f"[{i+1}/{len(short_list)}] Expandindo {art['file']}...")
        html = fpath.read_text(encoding='utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        content_div = get_content(soup)
        
        if content_div:
            lang = 'pt-BR'
            for l in ['en', 'es', 'fr', 'ar', 'zh', 'ru', 'hi', 'ja', 'bn', 'pt-pt']:
                if f'/{l}/' in str(fpath): lang = l; break
            
            new_html = expand_text(soup.title.string if soup.title else fpath.stem, content_div.get_text(), lang)
            if new_html:
                new_html = re.sub(r'^```html\n|```$', '', new_html, flags=re.MULTILINE)
                content_div.clear()
                content_div.append(BeautifulSoup(new_html, 'html.parser'))
                fpath.write_text(str(soup), encoding='utf-8')
                time.sleep(1) # Evitar rate limit

process()
