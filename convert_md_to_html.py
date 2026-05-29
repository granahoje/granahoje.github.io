import os
import markdown
import re

posts_dir = '_posts'
output_dir = 'artigos'
template_path = 'artigos/7-apps-pagam-pix-instantaneo.html'

os.makedirs(output_dir, exist_ok=True)

with open(template_path, 'r', encoding='utf-8') as f:
    template_content = f.read()

def convert_posts():
    for filename in os.listdir(posts_dir):
        if filename.endswith('.md'):
            filepath = os.path.join(posts_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                full_content = f.read()
            
            # Separar frontmatter do conteúdo
            parts = re.split(r'---', full_content)
            if len(parts) >= 3:
                md_content = parts[2].strip()
                frontmatter = parts[1]
            else:
                md_content = full_content
                frontmatter = ""
            
            # Converter Markdown para HTML
            html_body = markdown.markdown(md_content)
            
            # Extrair título
            title_match = re.search(r'title: "(.*?)"', frontmatter)
            title = title_match.group(1) if title_match else "Grana Hoje"
            
            # Nome do arquivo de saída
            output_filename = filename[11:].replace('.md', '.html') if len(filename) > 11 else filename.replace('.md', '.html')
            output_path = os.path.join(output_dir, output_filename)
            
            final_html = template_content
            final_html = re.sub(r'<title>.*?</title>', f'<title>{title} - Grana Hoje</title>', final_html)
            final_html = re.sub(r'<h2>.*?</h2>', f'<h2>{title}</h2>', final_html)
            
            start_marker = '<div class="content-section">'
            end_marker = '</div>'
            start_index = final_html.find(start_marker)
            if start_index != -1:
                content_start = start_index + len(start_marker)
                # Encontrar o fechamento da div de conteúdo principal
                # Para ser mais robusto, vamos procurar o próximo </div> após o início
                content_end = final_html.find(end_marker, content_start)
                if content_end != -1:
                    final_html = final_html[:content_start] + "\n" + html_body + "\n" + final_html[content_end:]
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(final_html)
            print(f"Convertido: {filename} -> {output_filename}")

if __name__ == "__main__":
    convert_posts()
