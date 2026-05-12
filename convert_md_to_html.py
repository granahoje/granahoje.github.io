import os
import markdown

# Configurações
posts_dir = '_posts'
output_dir = 'artigos'
template_path = 'artigos/7-apps-pagam-pix-instantaneo.html'

# Criar diretório de saída se não existir
os.makedirs(output_dir, exist_ok=True)

# Ler o template HTML
with open(template_path, 'r', encoding='utf-8') as f:
    template_content = f.read()

# Extrair as partes do template (antes e depois do conteúdo principal)
# O conteúdo principal no template está dentro de <div class="content-section">
# Vamos simplificar e usar um marcador ou substituir o conteúdo existente.

def convert_posts():
    for filename in os.listdir(posts_dir):
        if filename.endswith('.md') and '2026-05-12' in filename:
            filepath = os.path.join(posts_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                md_content = f.read()
            
            # Converter Markdown para HTML
            html_body = markdown.markdown(md_content)
            
            # Extrair título do markdown (primeira linha # Título)
            title = "Grana Hoje"
            lines = md_content.split('\n')
            for line in lines:
                if line.startswith('# '):
                    title = line[2:].strip()
                    break
            
            # Nome do arquivo de saída
            # 2026-05-12-nome-do-post.md -> nome-do-post.html
            output_filename = filename[11:].replace('.md', '.html')
            output_path = os.path.join(output_dir, output_filename)
            
            # Criar o HTML final substituindo partes do template
            # Para simplificar, vamos substituir o título e o conteúdo da seção principal
            
            final_html = template_content
            
            # Substituir o título na tag <title> e no <h2>
            import re
            final_html = re.sub(r'<title>.*?</title>', f'<title>{title} - Grana Hoje</title>', final_html)
            final_html = re.sub(r'<h2>.*?</h2>', f'<h2>{title}</h2>', final_html)
            
            # Substituir o conteúdo da seção principal
            # No template, o conteúdo está entre <div class="content-section"> e o próximo </div>
            # Vamos usar uma abordagem de substituição de string para o que está entre as tags de conteúdo
            
            start_marker = '<div class="content-section">'
            end_marker = '</div>'
            
            start_index = final_html.find(start_marker)
            if start_index != -1:
                # Encontrar o fechamento da div de conteúdo
                # Nota: Isso é simplificado e assume a estrutura do template lido
                content_start = start_index + len(start_marker)
                content_end = final_html.find(end_marker, content_start)
                
                if content_end != -1:
                    final_html = final_html[:content_start] + "\n" + html_body + "\n" + final_html[content_end:]
            
            # Salvar o arquivo HTML
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(final_html)
            
            print(f"Convertido: {filename} -> {output_filename}")

if __name__ == "__main__":
    convert_posts()
