import os
import re

languages = {
    "pt-br": "artigos/",
    "ar": "ar/artigos/",
    "bn": "bn/artigos/",
    "en": "en/artigos/",
    "es": "es/artigos/",
    "fr": "fr/artigos/",
    "hi": "hi/artigos/",
    "ja": "ja/artigos/",
    "pt-pt": "pt-pt/artigos/",
    "ru": "ru/artigos/",
    "zh": "zh/artigos/"
}

base_url = "https://granahoje.github.io/"

def get_hreflang_tags(article_filename):
    tags = []
    for lang, folder in languages.items():
        url = f"{base_url}{folder}{article_filename}"
        tags.append(f'    <link rel="alternate" hreflang="{lang}" href="{url}" />')
    # x-default aponta para a versão em português (raiz/artigos/)
    tags.append(f'    <link rel="alternate" hreflang="x-default" href="{base_url}artigos/{article_filename}" />')
    return "\n".join(tags)

# Coletar todos os nomes de arquivos de artigos baseados na pasta principal 'artigos/'
base_articles_dir = "artigos"
if os.path.exists(base_articles_dir):
    article_files = [f for f in os.listdir(base_articles_dir) if f.endswith(".html")]
    
    for article in article_files:
        for lang_code, lang_folder in languages.items():
            file_path = os.path.join(lang_folder, article)
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 1. Corrigir Canonical
                new_canonical = f"{base_url}{lang_folder}{article}"
                content = re.sub(r'<link rel="canonical" href="[^"]+">', f'<link rel="canonical" href="{new_canonical}">', content)
                content = re.sub(r'<link href="[^"]+" rel="canonical"/>', f'<link rel="canonical" href="{new_canonical}">', content)

                # 2. Injetar Hreflang (se não existir)
                if '<link rel="alternate"' not in content:
                    hreflang_tags = get_hreflang_tags(article)
                    content = content.replace('</head>', f'{hreflang_tags}\n</head>')
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
        print(f"Processed article across all languages: {article}")
else:
    print("Diretório 'artigos/' não encontrado.")
