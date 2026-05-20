import os
import re

tools_dir = "project/ferramentas"

content_map = {
    "calculadora-rescisao.html": {
        "title": "Calculadora de Rescisão CLT",
        "subtitle": "Calcule seus direitos trabalhistas de forma rápida e precisa.",
        "guide": "Entenda como funciona o cálculo da sua rescisão de contrato de trabalho. Nossa ferramenta considera saldo de salário, aviso prévio, férias e 13º salário proporcional.",
        "importance": "Saber o valor exato da sua rescisão é fundamental para garantir que seus direitos sejam respeitados e para planejar seu orçamento durante a transição de carreira.",
        "faq": "Como é calculado o aviso prévio? O aviso prévio pode ser trabalhado ou indenizado, e seu valor corresponde a um mês de salário mais 3 dias por cada ano trabalhado na empresa."
    },
    "calculadora-financiamento.html": {
        "title": "Calculadora de Financiamento",
        "subtitle": "Simule as parcelas do seu financiamento imobiliário ou de veículos.",
        "guide": "Compare diferentes taxas de juros e prazos para encontrar a melhor opção de financiamento para o seu bolso.",
        "importance": "O financiamento é um compromisso de longo prazo. Simular antes de contratar ajuda a evitar dívidas impagáveis e a economizar milhares de reais em juros.",
        "faq": "O que é o sistema SAC e PRICE? O SAC tem parcelas decrescentes, enquanto o PRICE mantém as parcelas fixas durante todo o contrato."
    }
}

def fix_tool(file_path, data):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Substituir o conteúdo repetitivo
    repetitive_pattern = r"<p>Conteúdo educativo profundo.*?</p>"
    content = re.sub(repetitive_pattern, f"<p>{data['guide']}</p>", content, flags=re.DOTALL)
    
    # Se houver mais de uma seção com o texto repetitivo, substituir as outras também
    content = re.sub(repetitive_pattern, f"<p>{data['importance']}</p>", content, flags=re.DOTALL)
    content = re.sub(repetitive_pattern, f"<p>{data['faq']}</p>", content, flags=re.DOTALL)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

for filename, data in content_map.items():
    path = os.path.join(tools_dir, filename)
    if os.path.exists(path):
        fix_tool(path, data)
