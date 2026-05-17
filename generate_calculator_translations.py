#!/usr/bin/env python3
"""
Script para gerar versões traduzidas da calculadora de juros compostos
em todos os idiomas suportados do site.
"""

import os
from openai import OpenAI

client = OpenAI()

# Configuração de idiomas
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
}

def translate_html(html_content, target_lang, lang_code):
    """Traduz o conteúdo HTML preservando a estrutura."""
    
    prompt = f"""
    Translate the following HTML content to {target_lang}.
    CRITICAL INSTRUCTIONS:
    1. DO NOT change ANY HTML tags, classes, IDs, or structure.
    2. ONLY translate the text content inside the tags.
    3. Keep all JavaScript code unchanged.
    4. Keep all variable names and function names unchanged.
    5. Translate the <title>, <meta name="description">, and <meta name="keywords"> content.
    6. DO NOT add markdown formatting around the output. Just return the raw HTML.
    7. Update the lang attribute to "{lang_code}"
    8. Update the canonical href to include the language path: /en/calculadora-juros-compostos.html -> /{lang_code}/calculadora-juros-compostos.html
    
    HTML to translate:
    {html_content}
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You are a professional web content translator. You translate text while perfectly preserving HTML structure and JavaScript code."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
        )
        result = response.choices[0].message.content.strip()
        
        # Remove possíveis marcações markdown
        if result.startswith("```html"):
            result = result[7:]
        if result.startswith("```"):
            result = result[3:]
        if result.endswith("```"):
            result = result[:-3]
            
        return result.strip()
    except Exception as e:
        print(f"Error during translation: {e}")
        return None

def main():
    """Processa todos os idiomas e gera as versões traduzidas."""
    
    # Ler arquivo base em inglês
    base_file = "/home/ubuntu/granahoje.github.io/en/calculadora-juros-compostos.html"
    
    if not os.path.exists(base_file):
        print(f"❌ Base file not found: {base_file}")
        return
    
    with open(base_file, 'r', encoding='utf-8') as f:
        base_html = f.read()
    
    print(f"📁 Base file loaded: {base_file}\n")
    
    for lang_code, lang_info in LANGUAGES.items():
        lang_name = lang_info['name']
        lang_path = lang_info['path']
        
        # Criar diretório se não existir
        os.makedirs(f"/home/ubuntu/granahoje.github.io/{lang_path}", exist_ok=True)
        
        target_file = f"/home/ubuntu/granahoje.github.io/{lang_path}/calculadora-juros-compostos.html"
        
        print(f"🌍 Translating to {lang_name} ({lang_code})...")
        
        translated_html = translate_html(base_html, lang_name, lang_code)
        
        if translated_html:
            # Garantir que o atributo lang está correto
            translated_html = translated_html.replace('lang="en"', f'lang="{lang_code}"')
            
            # Atualizar canonical URL
            translated_html = translated_html.replace(
                'href="https://granahoje.github.io/en/calculadora-juros-compostos.html"',
                f'href="https://granahoje.github.io/{lang_path}/calculadora-juros-compostos.html"'
            )
            
            # Atualizar links de navegação
            translated_html = translated_html.replace('href="/en/', f'href="/{lang_path}/')
            
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(translated_html)
            
            print(f"✅ Saved: {target_file}")
        else:
            print(f"❌ Failed to translate to {lang_name}")
        
        print()

if __name__ == "__main__":
    main()
    print("✨ Translation process completed!")
