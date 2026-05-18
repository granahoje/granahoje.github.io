import os
from openai import OpenAI
import time

client = OpenAI()

def translate_html(html_content, target_lang):
    prompt = f"""
    Translate the following HTML content to {target_lang}.
    CRITICAL INSTRUCTIONS:
    1. DO NOT change ANY HTML tags, classes, IDs, or structure.
    2. ONLY translate the text content inside the tags.
    3. For pt-pt, use European Portuguese.
    4. For bn, use Bengali.
    5. Translate the <title>, <meta name="description">, and <meta name="keywords"> content.
    6. Return ONLY the raw HTML.
    
    HTML to translate:
    {html_content}
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You are a professional web content translator."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
        )
        result = response.choices[0].message.content.strip()
        if result.startswith("```html"): result = result[7:]
        if result.startswith("```"): result = result[3:]
        if result.endswith("```"): result = result[:-3]
        return result.strip()
    except Exception as e:
        print(f"Error: {e}")
        return None

languages = [
    ("en", "English"),
    ("es", "Spanish"),
    ("fr", "French"),
    ("ar", "Arabic"),
    ("zh", "Chinese"),
    ("ru", "Russian"),
    ("hi", "Hindi"),
    ("ja", "Japanese"),
    ("pt-pt", "European Portuguese"),
    ("bn", "Bengali")
]

filename = "micro-saas-sem-codigo.html"
source_path = f"/home/ubuntu/granahoje_site/artigos/{filename}"

with open(source_path, 'r', encoding='utf-8') as f:
    source_html = f.read()

for lang_code, lang_name in languages:
    print(f"Translating to {lang_name}...")
    target_dir = f"/home/ubuntu/granahoje_site/{lang_code}/artigos"
    os.makedirs(target_dir, exist_ok=True)
    target_path = os.path.join(target_dir, filename)
    
    translated = translate_html(source_html, lang_name)
    if translated:
        # Ajustar links e seletores de idioma
        translated = translated.replace('lang="pt-BR"', f'lang="{lang_code}"')
        translated = translated.replace('selected>🇧🇷 PT-BR', '>')
        translated = translated.replace(f'value="{lang_code}">', f'value="{lang_code}" selected>')
        
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(translated)
        print(f"Saved: {target_path}")
    else:
        print(f"Failed: {lang_name}")
    time.sleep(1)
