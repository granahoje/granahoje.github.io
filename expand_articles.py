import os, json, re
from pathlib import Path
from bs4 import BeautifulSoup
from openai import OpenAI

client = OpenAI()
root = Path('/home/ubuntu/granahoje.github.io')

def get_content(soup):
    # Tenta encontrar a div de conteúdo principal
    main = soup.find('main') or soup.find('article') or soup.find('div', class_='container')
    if not main:
        return None
    return main

def expand_text(title, current_text, lang='pt-BR'):
    prompt = f"""
    Você é um redator especialista em SEO e finanças.
    O artigo atual sobre "{title}" está muito curto. 
    Expanda o conteúdo para que ele tenha mais de 1000 palavras, mantendo o tom profissional e educativo.
    Use subtítulos (H2, H3), listas e parágrafos bem estruturados.
    Idioma: {lang}
    
    Conteúdo atual para referência:
    {current_text[:1000]}
    
    Retorne APENAS o HTML interno do conteúdo expandido (sem <html> ou <body>).
    """
    
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def process_file(file_path):
    print(f"Processando: {file_path}")
    html = file_path.read_text(encoding='utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    
    title = soup.title.string if soup.title else file_path.stem
    content_div = get_content(soup)
    
    if not content_div:
        print(f"Erro: Conteúdo não encontrado em {file_path}")
        return

    current_text = content_div.get_text()
    words = len(re.findall(r'\w+', current_text))
    
    if words < 800:
        print(f"Expandindo {file_path} ({words} palavras)...")
        lang = 'pt-BR'
        if any(l in str(file_path) for l in ['/en/', '/es/', '/fr/', '/ar/', '/zh/', '/ru/', '/hi/', '/ja/', '/bn/', '/pt-pt/']):
            for l in ['en', 'es', 'fr', 'ar', 'zh', 'ru', 'hi', 'ja', 'bn', 'pt-pt']:
                if f'/{l}/' in str(file_path):
                    lang = l
                    break
        
        new_content_html = expand_text(title, current_text, lang)
        # Limpar blocos de código se a IA retornar
        new_content_html = re.sub(r'^```html\n|```$', '', new_content_html, flags=re.MULTILINE)
        
        # Substituir o conteúdo preservando a estrutura externa (header/footer)
        content_div.clear()
        content_div.append(BeautifulSoup(new_content_html, 'html.parser'))
        
        # Garantir padronização básica se faltar
        if not soup.find('header'):
            # Poderia injetar um header padrão aqui
            pass
            
        file_path.write_text(str(soup), encoding='utf-8')
        return True
    return False

# Para teste, processar os primeiros 5 curtos de PT-BR
with open('/home/ubuntu/granahoje.github.io/audit_v2_results.json', 'r') as f:
    audit = json.load(f)

count = 0
for art in audit['short_articles']:
    fpath = root / art['file']
    if 'artigos/' in str(fpath) and count < 10: # Limitar para não gastar tokens demais de uma vez
        if process_file(fpath):
            count += 1

print(f"Total de {count} artigos expandidos.")
