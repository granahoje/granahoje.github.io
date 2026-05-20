
import os
from bs4 import BeautifulSoup

def get_calculator_info(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        title_tag = soup.find('title')
        title = title_tag.text.replace(' - Grana Hoje', '').strip() if title_tag else 'Calculadora'
        
        # Try to find a subtitle or description paragraph
        description_tag = soup.find('p', class_='page-subtitle')
        if not description_tag:
            description_tag = soup.find('meta', attrs={'name': 'description'})
            if description_tag:
                description = description_tag['content'].strip()
            else:
                description = 'Ferramenta financeira gratuita.'
        else:
            description = description_tag.text.strip()
            
        # Extract icon from the first tool-card if available, otherwise use a default
        icon = '📊'
        tool_card_icon = soup.find('div', class_='tool-icon')
        if tool_card_icon:
            icon = tool_card_icon.text.strip()
        elif 'juros-compostos' in file_path: icon = '📈'
        elif 'reserva-emergencia' in file_path: icon = '🛡️'
        elif 'financiamento' in file_path: icon = '🏠'
        elif 'cdb-poupanca' in file_path: icon = '⚖️'
        elif 'desconto' in file_path: icon = '🏷️'
        elif 'dividend-yield' in file_path: icon = '💎'
        elif 'ponto-equilibrio' in file_path: icon = '🎯'
        elif 'roi' in file_path: icon = '📊'
        elif 'salario-liquido' in file_path: icon = '💰'
        elif 'juros-simples' in file_path: icon = '📈'
        elif 'rescisao' in file_path: icon = '📄'
        elif 'inflacao' in file_path: icon = '💸'
        elif 'ganho-capital' in file_path: icon = '💰'
        elif 'rebalanceamento' in file_path: icon = '🔄'
        elif 'valor-futuro' in file_path: icon = '🔮'
        elif 'valor-presente' in file_path: icon = '⏳'
        elif 'alocacao-carteira' in file_path: icon = '💼'
        elif 'independencia-financeira' in file_path: icon = '🏖️'
        elif 'preco-medio' in file_path: icon = '📉'
        elif 'tesouro-direto' in file_path: icon = '🏛️'
        elif 'investimento-mensal' in file_path: icon = '🗓️'
        elif 'taxa-real' in file_path: icon = '📊'


    return {
        'href': os.path.basename(file_path),
        'icon': icon,
        'title': title,
        'description': description
    }

def main():
    base_dir = "/home/ubuntu/granahoje.github.io"
    ferramentas_html_path = os.path.join(base_dir, "ferramentas.html")
    
    calculator_files = sorted([f for f in os.listdir(base_dir) if f.startswith('calculadora-') and f.endswith('.html')])
    
    all_calculators_info = []
    for calc_file in calculator_files:
        info = get_calculator_info(os.path.join(base_dir, calc_file))
        all_calculators_info.append(info)
        
    # Generate new tools-grid HTML
    new_tools_grid_content = []
    for calc in all_calculators_info:
        new_tools_grid_content.append(f"""
            <a href="/{calc['href']}" class="tool-card">
                <div class="tool-icon">{calc['icon']}</div>
                <h3>{calc['title']}</h3>
                <p>{calc['description']}</p>
                <span class="tool-link">Acessar Calculadora →</span>
            </a>""")
            
    new_tools_grid_html = "\n".join(new_tools_grid_content)
    
    with open(ferramentas_html_path, 'r', encoding='utf-8') as f:
        ferramentas_html = f.read()
        
    # Find and replace the tools-grid div content
    soup = BeautifulSoup(ferramentas_html, 'html.parser')
    tools_grid_div = soup.find('div', class_='tools-grid')
    
    if tools_grid_div:
        tools_grid_div.clear()
        tools_grid_div.append(BeautifulSoup(new_tools_grid_html, 'html.parser'))
        
        updated_html = str(soup)
        with open(ferramentas_html_path, 'w', encoding='utf-8') as f:
            f.write(updated_html)
        print("ferramentas.html updated successfully!")
    else:
        print("Error: .tools-grid div not found in ferramentas.html")

if __name__ == "__main__":
    main()
