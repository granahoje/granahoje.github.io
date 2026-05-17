import os
import re

languages = {
    "pt-br": "",
    "ar": "ar/",
    "bn": "bn/",
    "en": "en/",
    "es": "es/",
    "fr": "fr/",
    "hi": "hi/",
    "ja": "ja/",
    "pt-pt": "pt-pt/",
    "ru": "ru/",
    "zh": "zh/"
}

base_url = "https://granahoje.github.io/"

def get_hreflang_tags(page_name):
    tags = []
    for lang, path in languages.items():
        url = f"{base_url}{path}{page_name}"
        tags.append(f'    <link rel="alternate" hreflang="{lang}" href="{url}" />')
    tags.append(f'    <link rel="alternate" hreflang="x-default" href="{base_url}{page_name}" />')
    return "\n".join(tags)

pages_to_fix = ["index.html", "blog.html"]

for lang_code, lang_path in languages.items():
    for page in pages_to_fix:
        file_path = os.path.join(lang_path, page) if lang_path else page
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 1. Corrigir Canonical
            new_canonical = f"{base_url}{lang_path}{page}"
            content = re.sub(r'<link rel="canonical" href="[^"]+">', f'<link rel="canonical" href="{new_canonical}">', content)
            content = re.sub(r'<link href="[^"]+" rel="canonical"/>', f'<link rel="canonical" href="{new_canonical}">', content)

            # 2. Injetar Hreflang (antes do </head>)
            hreflang_tags = get_hreflang_tags(page)
            if '<link rel="alternate"' not in content:
                content = content.replace('</head>', f'{hreflang_tags}\n</head>')
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed: {file_path}")
