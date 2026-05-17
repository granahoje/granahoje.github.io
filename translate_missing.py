import os
import glob
from openai import OpenAI
import time

# Configurar cliente OpenAI
client = OpenAI()

def translate_html(html_content, target_lang):
    """Usa a API da OpenAI para traduzir o conteúdo HTML preservando a estrutura."""
    
    prompt = f"""
    Translate the following HTML content to {target_lang}.
    CRITICAL INSTRUCTIONS:
    1. DO NOT change ANY HTML tags, classes, IDs, or structure.
    2. ONLY translate the text content inside the tags.
    3. Keep all variables like {{...}} intact if they exist.
    4. For pt-pt, use European Portuguese.
    5. For bn, use Bengali.
    6. Translate the <title>, <meta name="description">, and <meta name="keywords"> content.
    7. DO NOT add markdown formatting like ```html around the output. Just return the raw HTML.
    
    HTML to translate:
    {html_content}
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You are a professional web content translator. You translate text while perfectly preserving HTML structure."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
        )
        result = response.choices[0].message.content.strip()
        
        # Remove possíveis marcações markdown se a IA ainda as adicionar
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

# Arquivos faltando em PT-PT
missing_pt_pt = [
    "apps-ganhar-dinheiro.html",
    "economia-verde-reciclagem-lucrativa.html",
    "investimentos-micro-franquias-digitais.html",
    "microtarefas-confiaveis.html",
    "monetizar-conhecimento-mentorias-online.html",
    "renda-extra-online.html",
    "renda-passiva-com-aluguel-de-equipamentos.html",
    "trabalho-remoto-assistente-virtual-2026.html"
]

# Arquivos faltando em BN
missing_bn = [
    "economia-verde-reciclagem-lucrativa.html",
    "investimentos-micro-franquias-digitais.html",
    "monetizar-conhecimento-mentorias-online.html",
    "renda-passiva-com-aluguel-de-equipamentos.html",
    "trabalho-remoto-assistente-virtual-2026.html"
]

def process_missing_files(missing_list, lang_code, lang_name):
    print(f"--- Processing missing files for {lang_code} ({lang_name}) ---")
    
    os.makedirs(f"/home/ubuntu/granahoje/{lang_code}/artigos", exist_ok=True)
    
    for filename in missing_list:
        source_path = f"/home/ubuntu/granahoje/en/artigos/{filename}"
        target_path = f"/home/ubuntu/granahoje/{lang_code}/artigos/{filename}"
        
        if not os.path.exists(source_path):
            print(f"Source file not found: {source_path}")
            continue
            
        if os.path.exists(target_path):
            print(f"Target already exists: {target_path}")
            continue
            
        print(f"Translating {filename} to {lang_code}...")
        
        with open(source_path, 'r', encoding='utf-8') as f:
            source_html = f.read()
            
        # O arquivo HTML inteiro pode ser muito grande para uma única chamada de API
        # Vamos tentar traduzir o arquivo inteiro primeiro, se falhar ou truncar, teríamos que dividir
        # Como gpt-4.1-mini tem bom contexto, deve funcionar para esses artigos
        
        translated_html = translate_html(source_html, lang_name)
        
        if translated_html:
            # Substituir caminhos específicos de idioma no HTML traduzido
            translated_html = translated_html.replace('href="/en/', f'href="/{lang_code}/')
            translated_html = translated_html.replace('value="en" selected="selected"', 'value="en"')
            translated_html = translated_html.replace(f'value="{lang_code}"', f'value="{lang_code}" selected="selected"')
            translated_html = translated_html.replace('lang="en"', f'lang="{lang_code}"')
            
            with open(target_path, 'w', encoding='utf-8') as f:
                f.write(translated_html)
            print(f"Successfully saved {target_path}")
        else:
            print(f"Failed to translate {filename}")
            
        # Pequena pausa para evitar rate limits
        time.sleep(2)

if __name__ == "__main__":
    process_missing_files(missing_pt_pt, "pt-pt", "European Portuguese")
    process_missing_files(missing_bn, "bn", "Bengali")
    print("Translation process completed!")
