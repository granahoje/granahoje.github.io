#!/usr/bin/env python3
import os
from openai import OpenAI

client = OpenAI()

LANGUAGES = {
    'es': {'name': 'Spanish', 'path': 'es'},
    'fr': {'name': 'French', 'path': 'fr'},
    'pt-pt': {'name': 'European Portuguese', 'path': 'pt-pt'},
    'ar': {'name': 'Arabic', 'path': 'ar'},
    'zh': {'name': 'Simplified Chinese', 'path': 'zh'},
    'ru': {'name': 'Russian', 'path': 'ru'},
    'hi': {'name': 'Hindi', 'path': 'hi'},
    'ja': {'name': 'Japanese', 'path': 'ja'},
    'bn': {'name': 'Bengali', 'path': 'bn'},
    'en': {'name': 'English', 'path': 'en'},
}

CALCULATORS = [
    ('calculadora-salario-liquido.html', 'Calculadora de Salário Líquido'),
    ('conversor-moedas.html', 'Conversor de Moedas')
]

def translate_html(html_content, target_lang, lang_code, calc_name):
    prompt = f"""
    Translate this {calc_name} HTML to {target_lang}.
    CRITICAL:
    1. DO NOT change HTML tags, classes, IDs, or structure
    2. ONLY translate text content inside tags
    3. Keep all JavaScript code unchanged
    4. Update lang attribute to "{lang_code}"
    5. Update canonical href to /{lang_code}/{calc_name}
    6. Return ONLY raw HTML, no markdown
    
    HTML:
    {html_content}
    """
    
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a professional HTML translator. Preserve all HTML structure and code."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
    )
    result = response.choices[0].message.content.strip()
    if result.startswith("```html"): result = result[7:]
    if result.startswith("```"): result = result[3:]
    if result.endswith("```"): result = result[:-3]
    return result.strip()

for calc_file, calc_name in CALCULATORS:
    base_file = f"/home/ubuntu/granahoje.github.io/{calc_file}"
    
    if not os.path.exists(base_file):
        print(f"❌ {calc_file} not found")
        continue
    
    with open(base_file, 'r', encoding='utf-8') as f:
        base_html = f.read()
    
    print(f"\n📁 Traduzindo {calc_name}...")
    
    for lang_code, lang_info in LANGUAGES.items():
        if lang_code == 'pt-br': continue
        
        lang_name = lang_info['name']
        lang_path = lang_info['path']
        os.makedirs(f"/home/ubuntu/granahoje.github.io/{lang_path}", exist_ok=True)
        
        target_file = f"/home/ubuntu/granahoje.github.io/{lang_path}/{calc_file}"
        
        print(f"  🌍 {lang_name}...", end=" ", flush=True)
        
        translated = translate_html(base_html, lang_name, lang_code, calc_name)
        translated = translated.replace('lang="pt-BR"', f'lang="{lang_code}"')
        translated = translated.replace(f'href="https://granahoje.github.io/{calc_file}"', f'href="https://granahoje.github.io/{lang_path}/{calc_file}"')
        
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(translated)
        
        print("✅")

print("\n✨ Tradução concluída!")
