import os
import re

credibility_html = """    <!-- Mensagem de Credibilidade -->
    <div style="margin: 15px 20px; padding: 12px; background: rgba(0, 209, 178, 0.1); border: 1px solid rgba(0, 209, 178, 0.2); border-radius: 15px; text-align: center;">
        <p style="font-size: 0.75rem; color: #00d1b2; font-weight: 600; margin: 0;">
            🔒 <span id="credibilityText">Nossos patrocinadores garantem seus pagamentos. Ao navegar e interagir, você ajuda a manter nossa comunidade ativa e lucrativa!</span>
        </p>
    </div>
"""

def apply_to_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Pular se já possui a mensagem
    if 'Nossos patrocinadores garantem seus pagamentos' in content:
        return False

    # Estratégia 1: Após </header>
    if '</header>' in content:
        new_content = content.replace('</header>', '</header>\n' + credibility_html, 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True

    # Estratégia 2: Após <body>
    if '<body' in content:
        match = re.search(r'(<body[^>]*>)', content)
        if match:
            insert_pos = match.end()
            new_content = content[:insert_pos] + '\n' + credibility_html + content[insert_pos:]
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True

    # Estratégia 3: Após <main> ou primeira <section>
    if '<main' in content or '<section' in content:
        pattern = r'(<main[^>]*>|<section[^>]*>)'
        match = re.search(pattern, content)
        if match:
            insert_pos = match.end()
            new_content = content[:insert_pos] + '\n' + credibility_html + content[insert_pos:]
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True

    return False

def main():
    count = 0
    for root, dirs, files in os.walk('.'):
        # Pular diretórios irrelevantes
        if '.git' in root or '__manus__' in root or '.nvm' in root:
            continue
            
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                if apply_to_file(filepath):
                    print(f"✓ {filepath}")
                    count += 1
    
    print(f"\nTotal de arquivos atualizados: {count}")

if __name__ == "__main__":
    main()
