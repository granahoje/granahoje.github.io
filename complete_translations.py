
import os
import re
from openai import OpenAI

client = OpenAI()

LANGUAGES = {
    'en': 'English',
    'es': 'Spanish',
    'fr': 'French',
    'ar': 'Arabic',
    'zh': 'Simplified Chinese',
    'ru': 'Russian',
    'hi': 'Hindi',
    'ja': 'Japanese',
    'bn': 'Bengali',
    'pt-pt': 'European Portuguese'
}

# Lista de ferramentas que identifiquei como incompletas
TOOLS = [
    'calculadora-valor-presente.html',
    'calculadora-rebalanceamento.html',
    'calculadora-ganho-capital.html',
    'calculadora-inflacao.html',
    'calculadora-previdencia-privada.html',
    'calculadora-taxa-real.html',
    'calculadora-valor-futuro.html',
    'calculadora-alocacao-carteira.html',
    'calculadora-independencia-financeira.html'
]

def translate_html(html_content, target_lang_name, target_lang_code, filename):
    print(f"    Translating to {target_lang_name}...")
    prompt = f"""
    Translate the following financial tool HTML from Portuguese to {target_lang_name}.
    
    CRITICAL RULES:
    1. DO NOT change any HTML tags, classes, IDs, or structure.
    2. ONLY translate the visible text content, titles, placeholders, and labels.
    3. Keep all JavaScript code and logic EXACTLY as it is.
    4. Update the <html lang="..."> attribute to "{target_lang_code}".
    5. If there is a canonical link or language selector, update the paths to include /{target_lang_code}/.
    6. Maintain the professional, human, and educational tone (EEAT).
    7. Return ONLY the raw HTML code. No markdown blocks.
    
    HTML to translate:
    {html_content}
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You are a professional web developer and translator specializing in financial content and SEO."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )
        translated = response.choices[0].message.content.strip()
        # Clean up potential markdown wrapping
        translated = re.sub(r'^```html\s*', '', translated)
        translated = re.sub(r'\s*```$', '', translated)
        return translated
    except Exception as e:
        print(f"    Error translating to {target_lang_code}: {e}")
        return None

def main():
    base_dir = "/home/ubuntu/granahoje.github.io"
    
    for tool in TOOLS:
        source_path = os.path.join(base_dir, tool)
        if not os.path.exists(source_path):
            print(f"Skipping {tool}: Source file not found.")
            continue
            
        print(f"Processing {tool}...")
        with open(source_path, 'r', encoding='utf-8') as f:
            source_html = f.read()
            
        for lang_code, lang_name in LANGUAGES.items():
            target_dir = os.path.join(base_dir, lang_code)
            os.makedirs(target_dir, exist_ok=True)
            target_path = os.path.join(target_dir, tool)
            
            if os.path.exists(target_path):
                # print(f"  - {lang_code}/{tool} already exists. Skipping.")
                continue
                
            translated_html = translate_html(source_html, lang_name, lang_code, tool)
            if translated_html:
                with open(target_path, 'w', encoding='utf-8') as f:
                    f.write(translated_html)
                print(f"  ✅ Saved {lang_code}/{tool}")

if __name__ == "__main__":
    main()
