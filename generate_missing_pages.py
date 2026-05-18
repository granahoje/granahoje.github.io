#!/usr/bin/env python3
"""
Script para gerar páginas faltantes com tradução via OpenAI.
Gera:
1. conversor-moedas.html para es, fr, ar
2. calculadora-juros-compostos.html para ja
3. calculadora-desconto, investimento-mensal, reserva-emergencia, roi, conversor-moedas para pt-pt
4. about.html para todos os 10 idiomas
5. faq.html para todos os 10 idiomas
"""

import os
import re
from openai import OpenAI

client = OpenAI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LANGUAGES = {
    'en': {'name': 'English', 'lang_attr': 'en', 'locale': 'en_US'},
    'es': {'name': 'Spanish', 'lang_attr': 'es', 'locale': 'es_ES'},
    'fr': {'name': 'French', 'lang_attr': 'fr', 'locale': 'fr_FR'},
    'hi': {'name': 'Hindi', 'lang_attr': 'hi', 'locale': 'hi_IN'},
    'ja': {'name': 'Japanese', 'lang_attr': 'ja', 'locale': 'ja_JP'},
    'zh': {'name': 'Chinese (Simplified)', 'lang_attr': 'zh', 'locale': 'zh_CN'},
    'ru': {'name': 'Russian', 'lang_attr': 'ru', 'locale': 'ru_RU'},
    'ar': {'name': 'Arabic', 'lang_attr': 'ar', 'locale': 'ar_SA'},
    'bn': {'name': 'Bengali', 'lang_attr': 'bn', 'locale': 'bn_BD'},
    'pt-pt': {'name': 'Portuguese (Portugal)', 'lang_attr': 'pt-PT', 'locale': 'pt_PT'},
}

ADSENSE_ID = "ca-pub-4896859041377751"
GA_ID = "G-706NN8PEE7"
BASE_URL = "https://granahoje.github.io"

HREFLANG_CALCULATORS = {
    'conversor-moedas.html': {
        'pt-br': '/conversor-moedas.html',
        'en': '/en/conversor-moedas.html',
        'es': '/es/conversor-moedas.html',
        'fr': '/fr/conversor-moedas.html',
        'hi': '/hi/conversor-moedas.html',
        'ja': '/ja/conversor-moedas.html',
        'zh': '/zh/conversor-moedas.html',
        'ru': '/ru/conversor-moedas.html',
        'ar': '/ar/conversor-moedas.html',
        'bn': '/bn/conversor-moedas.html',
        'pt-pt': '/pt-pt/conversor-moedas.html',
    },
    'calculadora-juros-compostos.html': {
        'pt-br': '/calculadora-juros-compostos.html',
        'en': '/en/calculadora-juros-compostos.html',
        'es': '/es/calculadora-juros-compostos.html',
        'fr': '/fr/calculadora-juros-compostos.html',
        'hi': '/hi/calculadora-juros-compostos.html',
        'ja': '/ja/calculadora-juros-compostos.html',
        'zh': '/zh/calculadora-juros-compostos.html',
        'ru': '/ru/calculadora-juros-compostos.html',
        'ar': '/ar/calculadora-juros-compostos.html',
        'bn': '/bn/calculadora-juros-compostos.html',
        'pt-pt': '/pt-pt/calculadora-juros-compostos.html',
    },
    'calculadora-desconto.html': {
        'pt-br': '/calculadora-desconto.html',
        'en': '/en/calculadora-desconto.html',
        'es': '/es/calculadora-desconto.html',
        'fr': '/fr/calculadora-desconto.html',
        'hi': '/hi/calculadora-desconto.html',
        'ja': '/ja/calculadora-desconto.html',
        'zh': '/zh/calculadora-desconto.html',
        'ru': '/ru/calculadora-desconto.html',
        'ar': '/ar/calculadora-desconto.html',
        'bn': '/bn/calculadora-desconto.html',
        'pt-pt': '/pt-pt/calculadora-desconto.html',
    },
    'calculadora-investimento-mensal.html': {
        'pt-br': '/calculadora-investimento-mensal.html',
        'en': '/en/calculadora-investimento-mensal.html',
        'es': '/es/calculadora-investimento-mensal.html',
        'fr': '/fr/calculadora-investimento-mensal.html',
        'hi': '/hi/calculadora-investimento-mensal.html',
        'ja': '/ja/calculadora-investimento-mensal.html',
        'zh': '/zh/calculadora-investimento-mensal.html',
        'ru': '/ru/calculadora-investimento-mensal.html',
        'ar': '/ar/calculadora-investimento-mensal.html',
        'bn': '/bn/calculadora-investimento-mensal.html',
        'pt-pt': '/pt-pt/calculadora-investimento-mensal.html',
    },
    'calculadora-reserva-emergencia.html': {
        'pt-br': '/calculadora-reserva-emergencia.html',
        'en': '/en/calculadora-reserva-emergencia.html',
        'es': '/es/calculadora-reserva-emergencia.html',
        'fr': '/fr/calculadora-reserva-emergencia.html',
        'hi': '/hi/calculadora-reserva-emergencia.html',
        'ja': '/ja/calculadora-reserva-emergencia.html',
        'zh': '/zh/calculadora-reserva-emergencia.html',
        'ru': '/ru/calculadora-reserva-emergencia.html',
        'ar': '/ar/calculadora-reserva-emergencia.html',
        'bn': '/bn/calculadora-reserva-emergencia.html',
        'pt-pt': '/pt-pt/calculadora-reserva-emergencia.html',
    },
    'calculadora-roi.html': {
        'pt-br': '/calculadora-roi.html',
        'en': '/en/calculadora-roi.html',
        'es': '/es/calculadora-roi.html',
        'fr': '/fr/calculadora-roi.html',
        'hi': '/hi/calculadora-roi.html',
        'ja': '/ja/calculadora-roi.html',
        'zh': '/zh/calculadora-roi.html',
        'ru': '/ru/calculadora-roi.html',
        'ar': '/ar/calculadora-roi.html',
        'bn': '/bn/calculadora-roi.html',
        'pt-pt': '/pt-pt/calculadora-roi.html',
    },
    'about.html': {
        'pt-br': '/about.html',
        'en': '/en/about.html',
        'es': '/es/about.html',
        'fr': '/fr/about.html',
        'hi': '/hi/about.html',
        'ja': '/ja/about.html',
        'zh': '/zh/about.html',
        'ru': '/ru/about.html',
        'ar': '/ar/about.html',
        'bn': '/bn/about.html',
        'pt-pt': '/pt-pt/about.html',
    },
    'faq.html': {
        'pt-br': '/faq.html',
        'en': '/en/faq.html',
        'es': '/es/faq.html',
        'fr': '/fr/faq.html',
        'hi': '/hi/faq.html',
        'ja': '/ja/faq.html',
        'zh': '/zh/faq.html',
        'ru': '/ru/faq.html',
        'ar': '/ar/faq.html',
        'bn': '/bn/faq.html',
        'pt-pt': '/pt-pt/faq.html',
    },
}

def build_hreflang_tags(filename, current_lang):
    """Gera as tags hreflang para uma página."""
    hreflang_map = HREFLANG_CALCULATORS.get(filename, {})
    tags = []
    for lang_code, path in hreflang_map.items():
        tags.append(f'    <link rel="alternate" hreflang="{lang_code}" href="{BASE_URL}{path}" />')
    tags.append(f'    <link rel="alternate" hreflang="x-default" href="{BASE_URL}{hreflang_map.get("en", hreflang_map.get("pt-br", "/"))}" />')
    return '\n'.join(tags)

def translate_html_content(source_html, target_lang_name, target_lang_code, filename):
    """Usa OpenAI para traduzir o conteúdo HTML visível."""
    prompt = f"""You are an expert HTML translator. Translate the visible text content of this HTML page to {target_lang_name}.

Rules:
1. Translate ONLY the visible text content (titles, labels, descriptions, button text, paragraphs, etc.)
2. Keep ALL HTML tags, attributes, CSS, JavaScript code EXACTLY as-is
3. Keep financial terms like BRL, USD, EUR, PIX, etc. unchanged
4. Keep the page structure, IDs, classes unchanged
5. For the lang attribute in <html>, use: {target_lang_code}
6. Make the translation natural and culturally appropriate for {target_lang_name} speakers
7. For Arabic (ar), ensure RTL text is natural
8. Keep numbers and formulas unchanged
9. Return ONLY the translated HTML, no explanations

Source HTML:
{source_html}"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=8000,
        temperature=0.3
    )
    return response.choices[0].message.content.strip()

def fix_canonical_and_hreflang(html_content, lang_code, filename):
    """Corrige canonical URL e adiciona/atualiza hreflang tags."""
    if lang_code == 'pt-br':
        canonical_url = f"{BASE_URL}/{filename}"
    else:
        canonical_url = f"{BASE_URL}/{lang_code}/{filename}"
    
    # Fix canonical
    html_content = re.sub(
        r'<link rel="canonical"[^>]+>',
        f'<link rel="canonical" href="{canonical_url}">',
        html_content
    )
    
    # Add hreflang tags before </head>
    hreflang_tags = build_hreflang_tags(filename, lang_code)
    
    # Remove existing hreflang tags
    html_content = re.sub(r'\s*<link rel="alternate" hreflang="[^"]*"[^>]*/>\n?', '', html_content)
    
    # Insert before </head>
    html_content = html_content.replace('</head>', f'{hreflang_tags}\n</head>', 1)
    
    return html_content

def fix_nav_links(html_content, lang_code):
    """Corrige links de navegação para o idioma correto."""
    if lang_code == 'pt-br':
        prefix = ''
    else:
        prefix = f'/{lang_code}'
    
    # Fix common nav links
    nav_replacements = [
        (r'href="/blog\.html"', f'href="{prefix}/blog.html"'),
        (r'href="/about\.html"', f'href="{prefix}/about.html"'),
        (r'href="/contact\.html"', f'href="{prefix}/contact.html"'),
        (r'href="/en/blog\.html"', f'href="{prefix}/blog.html"'),
        (r'href="/en/about\.html"', f'href="{prefix}/about.html"'),
        (r'href="/en/contact\.html"', f'href="{prefix}/contact.html"'),
    ]
    
    for pattern, replacement in nav_replacements:
        html_content = re.sub(pattern, replacement, html_content)
    
    return html_content

def read_source_file(filename, preferred_lang='en'):
    """Lê o arquivo fonte para usar como base de tradução."""
    # Try preferred lang first
    path = os.path.join(BASE_DIR, preferred_lang, filename)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    
    # Try root
    path = os.path.join(BASE_DIR, filename)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    
    return None

def generate_page(lang_code, filename, source_html=None):
    """Gera uma página traduzida."""
    lang_info = LANGUAGES[lang_code]
    lang_name = lang_info['name']
    lang_attr = lang_info['lang_attr']
    
    output_path = os.path.join(BASE_DIR, lang_code, filename)
    
    if os.path.exists(output_path):
        print(f"  SKIP: {lang_code}/{filename} já existe")
        return False
    
    if source_html is None:
        print(f"  ERROR: Sem fonte para {filename}")
        return False
    
    print(f"  Traduzindo {filename} para {lang_name}...")
    
    try:
        translated = translate_html_content(source_html, lang_name, lang_attr, filename)
        
        # Fix lang attribute
        translated = re.sub(r'<html lang="[^"]*">', f'<html lang="{lang_attr}">', translated)
        
        # Fix canonical and hreflang
        translated = fix_canonical_and_hreflang(translated, lang_code, filename)
        
        # Fix nav links
        translated = fix_nav_links(translated, lang_code)
        
        # Ensure AdSense is present
        if ADSENSE_ID not in translated and 'pagead2' not in translated:
            adsense_script = f'<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE_ID}" crossorigin="anonymous"></script>\n'
            translated = translated.replace('<head>', '<head>\n' + adsense_script, 1)
        
        # Write file
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(translated)
        
        print(f"  OK: {lang_code}/{filename}")
        return True
    except Exception as e:
        print(f"  ERROR: {lang_code}/{filename}: {e}")
        return False

def main():
    print("=== Gerando páginas faltantes ===\n")
    
    # 1. Calculadoras faltantes
    missing_calculators = [
        ('es', 'conversor-moedas.html'),
        ('fr', 'conversor-moedas.html'),
        ('ar', 'conversor-moedas.html'),
        ('ja', 'calculadora-juros-compostos.html'),
        ('pt-pt', 'calculadora-desconto.html'),
        ('pt-pt', 'calculadora-investimento-mensal.html'),
        ('pt-pt', 'calculadora-reserva-emergencia.html'),
        ('pt-pt', 'calculadora-roi.html'),
        ('pt-pt', 'conversor-moedas.html'),
    ]
    
    print("--- Calculadoras faltantes ---")
    for lang_code, filename in missing_calculators:
        source = read_source_file(filename, 'en')
        generate_page(lang_code, filename, source)
    
    # 2. about.html para todos os idiomas
    print("\n--- about.html para todos os idiomas ---")
    about_source = read_source_file('about.html', 'root')
    if about_source is None:
        with open(os.path.join(BASE_DIR, 'about.html'), 'r', encoding='utf-8') as f:
            about_source = f.read()
    
    for lang_code in LANGUAGES.keys():
        generate_page(lang_code, 'about.html', about_source)
    
    # 3. faq.html para todos os idiomas
    print("\n--- faq.html para todos os idiomas ---")
    faq_source = None
    with open(os.path.join(BASE_DIR, 'faq.html'), 'r', encoding='utf-8') as f:
        faq_source = f.read()
    
    for lang_code in LANGUAGES.keys():
        generate_page(lang_code, 'faq.html', faq_source)
    
    print("\n=== Concluído! ===")

if __name__ == '__main__':
    main()
