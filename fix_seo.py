#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Correção SEO - Grana Hoje
Corrige problemas de indexação no Google Search Console:
- Renomeia pastas _*_disabled para idiomas ativos
- Corrige canonical tags (auto-referência)
- Injeta hreflang completo em todas as páginas
- Regenera sitemap.xml com xhtml:link
- Adiciona noindex ao 404.html
"""

import os
import re
from pathlib import Path
from datetime import datetime
import xml.etree.ElementTree as ET

# Configurações
BASE_URL = "https://granahoje.github.io"
ROOT_DIR = Path(__file__).parent
LANGUAGES = {
    'pt-BR': '',  # default, sem prefixo
    'ar': 'ar',
    'bn': 'bn',
    'en': 'en',
    'es': 'es',
    'fr': 'fr',
    'hi': 'hi',
    'ja': 'ja',
    'pt-PT': 'pt-pt',
    'ru': 'ru',
    'zh': 'zh'
}

def log(msg):
    """Log com timestamp"""
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")

def rename_language_folders():
    """Renomeia pastas _*_disabled para idiomas ativos"""
    log("🔄 Reativando pastas de idiomas...")
    renamed = []
    
    for old_name, new_name in [
        ('_ar_disabled', 'ar'),
        ('_bn_disabled', 'bn'),
        ('_en_disabled', 'en'),
        ('_es_disabled', 'es'),
        ('_fr_disabled', 'fr'),
        ('_hi_disabled', 'hi'),
        ('_ja_disabled', 'ja'),
        ('_pt-pt_disabled', 'pt-pt'),
        ('_ru_disabled', 'ru'),
        ('_zh_disabled', 'zh')
    ]:
        old_path = ROOT_DIR / old_name
        new_path = ROOT_DIR / new_name
        
        if old_path.exists():
            if new_path.exists():
                log(f"⚠️  {new_name}/ já existe, pulando...")
            else:
                old_path.rename(new_path)
                renamed.append(new_name)
                log(f"✅ {old_name}/ → {new_name}/")
    
    log(f"✨ {len(renamed)} pastas reativadas: {', '.join(renamed)}")
    return renamed

def get_all_html_files():
    """Encontra todos os arquivos HTML (exceto em pastas especiais)"""
    html_files = []
    exclude_dirs = {'__manus__', '.git', 'ferramentas'}
    
    for html_file in ROOT_DIR.rglob('*.html'):
        # Ignora se está em pasta excluída
        if any(ex in str(html_file.relative_to(ROOT_DIR)) for ex in exclude_dirs):
            continue
        html_files.append(html_file)
    
    return html_files

def detect_language_from_path(file_path):
    """Detecta o idioma baseado no caminho do arquivo"""
    rel_path = str(file_path.relative_to(ROOT_DIR))
    
    for lang_code, prefix in LANGUAGES.items():
        if prefix and rel_path.startswith(prefix + '/'):
            return lang_code
    
    return 'pt-BR'  # padrão

def get_relative_url(file_path):
    """Converte caminho de arquivo para URL relativa"""
    rel_path = str(file_path.relative_to(ROOT_DIR))
    return '/' + rel_path

def find_translations_for_page(file_path, all_files):
    """Encontra todas as traduções disponíveis de uma página"""
    # Extrai o nome base do arquivo (sem o prefixo de idioma)
    rel_path = str(file_path.relative_to(ROOT_DIR))
    
    # Se está em pasta de idioma, remove o prefixo
    for prefix in LANGUAGES.values():
        if prefix and rel_path.startswith(prefix + '/'):
            base_path = rel_path[len(prefix)+1:]
            break
    else:
        base_path = rel_path
    
    # Procura o mesmo arquivo em todos os idiomas
    translations = {}
    
    # pt-BR (raiz)
    pt_file = ROOT_DIR / base_path
    if pt_file.exists() and pt_file.is_file():
        translations['pt-BR'] = get_relative_url(pt_file)
    
    # Outros idiomas
    for lang_code, prefix in LANGUAGES.items():
        if not prefix:  # pula pt-BR
            continue
        
        lang_file = ROOT_DIR / prefix / base_path
        if lang_file.exists() and lang_file.is_file():
            translations[lang_code] = get_relative_url(lang_file)
    
    return translations

def fix_canonical_and_hreflang(file_path, all_files):
    """Corrige canonical tag e adiciona hreflang completo"""
    try:
        content = file_path.read_text(encoding='utf-8')
        modified = False
        
        # 1. Detecta idioma atual
        current_lang = detect_language_from_path(file_path)
        current_url = get_relative_url(file_path)
        canonical_url = BASE_URL + current_url
        
        # 2. Corrige/adiciona canonical
        canonical_pattern = r'<link\s+rel="canonical"\s+href="[^"]*"\s*/?>'
        new_canonical = f'<link rel="canonical" href="{canonical_url}">'
        
        if re.search(canonical_pattern, content):
            content = re.sub(canonical_pattern, new_canonical, content)
            modified = True
        else:
            # Adiciona após </title> ou antes de </head>
            if '</title>' in content:
                content = content.replace('</title>', f'</title>\n    {new_canonical}')
            elif '</head>' in content:
                content = content.replace('</head>', f'    {new_canonical}\n</head>')
            else:
                return False  # HTML malformado
            modified = True
        
        # 3. Remove hreflang antigos
        hreflang_pattern = r'<link\s+rel="alternate"\s+hreflang="[^"]*"\s+href="[^"]*"\s*/?>'
        content = re.sub(hreflang_pattern, '', content)
        
        # 4. Adiciona hreflangs novos
        translations = find_translations_for_page(file_path, all_files)
        
        if len(translations) > 1:  # Só adiciona se houver traduções
            hreflang_tags = []
            
            # Adiciona cada idioma disponível
            for lang_code, url in sorted(translations.items()):
                hreflang = lang_code.lower()
                full_url = BASE_URL + url
                hreflang_tags.append(f'    <link rel="alternate" hreflang="{hreflang}" href="{full_url}">')
            
            # Adiciona x-default (pt-BR)
            if 'pt-BR' in translations:
                default_url = BASE_URL + translations['pt-BR']
                hreflang_tags.append(f'    <link rel="alternate" hreflang="x-default" href="{default_url}">')
            
            # Injeta após canonical
            hreflang_block = '\n'.join(hreflang_tags)
            content = content.replace(new_canonical, f'{new_canonical}\n{hreflang_block}')
            modified = True
        
        if modified:
            file_path.write_text(content, encoding='utf-8')
            return True
        
    except Exception as e:
        log(f"❌ Erro em {file_path.name}: {e}")
        return False
    
    return False

def add_noindex_to_404():
    """Adiciona noindex,follow ao 404.html"""
    file_404 = ROOT_DIR / '404.html'
    
    if not file_404.exists():
        log("⚠️  404.html não encontrado")
        return False
    
    try:
        content = file_404.read_text(encoding='utf-8')
        
        # Verifica se já tem robots tag
        if 'name="robots"' in content:
            # Substitui
            content = re.sub(
                r'<meta\s+name="robots"\s+content="[^"]*"\s*/?>',
                '<meta name="robots" content="noindex,follow">',
                content
            )
        else:
            # Adiciona após <head>
            content = content.replace('<head>', '<head>\n    <meta name="robots" content="noindex,follow">')
        
        file_404.write_text(content, encoding='utf-8')
        log("✅ noindex adicionado ao 404.html")
        return True
        
    except Exception as e:
        log(f"❌ Erro ao modificar 404.html: {e}")
        return False

def generate_sitemap(all_files):
    """Regenera sitemap.xml com xhtml:link para idiomas"""
    log("🗺️  Gerando sitemap.xml...")
    
    # Namespace
    ns = {
        '': 'http://www.sitemaps.org/schemas/sitemap/0.9',
        'xhtml': 'http://www.w3.org/1999/xhtml'
    }
    
    # Registra namespaces
    for prefix, uri in ns.items():
        ET.register_namespace(prefix if prefix else '', uri)
    
    # Cria root
    urlset = ET.Element('urlset')
    urlset.set('xmlns', ns[''])
    urlset.set('xmlns:xhtml', ns['xhtml'])
    
    # Páginas já processadas (evita duplicatas)
    processed_urls = set()
    
    # Prioridades por tipo
    priorities = {
        'index.html': '1.0',
        'about.html': '0.8',
        'blog.html': '0.8',
        'calculadora': '0.9',
        'artigos': '0.7',
        'default': '0.6'
    }
    
    for file_path in sorted(all_files):
        url_path = get_relative_url(file_path)
        full_url = BASE_URL + url_path
        
        # Pula 404.html
        if '404.html' in url_path:
            continue
        
        # Evita duplicatas
        if full_url in processed_urls:
            continue
        processed_urls.add(full_url)
        
        # Cria URL entry
        url_elem = ET.SubElement(urlset, 'url')
        loc = ET.SubElement(url_elem, 'loc')
        loc.text = full_url
        
        # LastMod
        lastmod = ET.SubElement(url_elem, 'lastmod')
        mtime = datetime.fromtimestamp(file_path.stat().st_mtime)
        lastmod.text = mtime.strftime('%Y-%m-%d')
        
        # Priority
        priority = ET.SubElement(url_elem, 'priority')
        if 'index.html' in url_path:
            priority.text = '1.0'
        elif 'calculadora' in url_path:
            priority.text = '0.9'
        elif 'about.html' in url_path or 'blog.html' in url_path:
            priority.text = '0.8'
        elif '/artigos/' in url_path:
            priority.text = '0.7'
        else:
            priority.text = '0.6'
        
        # Adiciona xhtml:link para traduções
        translations = find_translations_for_page(file_path, all_files)
        
        if len(translations) > 1:
            for lang_code, trans_url in sorted(translations.items()):
                link = ET.SubElement(url_elem, '{http://www.w3.org/1999/xhtml}link')
                link.set('rel', 'alternate')
                link.set('hreflang', lang_code.lower())
                link.set('href', BASE_URL + trans_url)
    
    # Salva sitemap
    tree = ET.ElementTree(urlset)
    ET.indent(tree, space='  ')
    
    sitemap_path = ROOT_DIR / 'sitemap.xml'
    tree.write(sitemap_path, encoding='utf-8', xml_declaration=True)
    
    log(f"✅ Sitemap gerado com {len(processed_urls)} URLs")
    return True

def main():
    log("🚀 Iniciando correção SEO - Grana Hoje")
    log("=" * 60)
    
    # 1. Renomeia pastas
    renamed_langs = rename_language_folders()
    
    # 2. Coleta todos os HTMLs
    log("\n📂 Coletando arquivos HTML...")
    all_files = get_all_html_files()
    log(f"✅ {len(all_files)} arquivos encontrados")
    
    # 3. Corrige canonical e hreflang
    log("\n🔧 Corrigindo canonical + hreflang...")
    fixed_count = 0
    
    for i, file_path in enumerate(all_files, 1):
        if fix_canonical_and_hreflang(file_path, all_files):
            fixed_count += 1
        
        # Progress
        if i % 50 == 0:
            log(f"   Processados: {i}/{len(all_files)}")
    
    log(f"✅ {fixed_count} arquivos corrigidos")
    
    # 4. Adiciona noindex ao 404
    log("\n🚫 Configurando 404.html...")
    add_noindex_to_404()
    
    # 5. Regenera sitemap
    log("\n🗺️  Regenerando sitemap...")
    generate_sitemap(all_files)
    
    log("\n" + "=" * 60)
    log("✨ CORREÇÃO CONCLUÍDA!")
    log("\n📋 Próximos passos:")
    log("   1. git diff --stat  # revisar mudanças")
    log("   2. git add -A")
    log("   3. git commit -m 'fix(seo): reativa idiomas + canonical + hreflang + sitemap'")
    log("   4. git push")
    log("   5. Aguardar GitHub Pages publicar (~2 min)")
    log("   6. No GSC, clicar 'Validar correção' em cada relatório")
    log("   7. Reenviar sitemap.xml")

if __name__ == '__main__':
    main()
