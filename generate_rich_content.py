import os
import re

tools_dir = "project/ferramentas"

def generate_juros_content():
    return """
    <div class="info-card">
        <h3>Guia Completo sobre Juros Compostos</h3>
        <p>Os juros compostos são frequentemente chamados de a "oitava maravilha do mundo". Diferente dos juros simples, onde a taxa incide apenas sobre o capital inicial, nos juros compostos a taxa incide sobre o capital inicial acrescido dos juros acumulados de períodos anteriores. Isso cria um efeito de crescimento exponencial, conhecido popularmente como "juros sobre juros".</p>
        
        <h4>Como os Juros Compostos Funcionam na Prática?</h4>
        <p>Imagine que você investiu R$ 1.000,00 a uma taxa de 10% ao ano. No final do primeiro ano, você terá R$ 1.100,00. No segundo ano, os 10% não serão calculados apenas sobre os R$ 1.000,00 iniciais, mas sobre os R$ 1.100,00 que você já possui. Assim, no final do segundo ano, você terá R$ 1.210,00. Esse pequeno acréscimo de R$ 10,00 parece pouco no início, mas ao longo de 20 ou 30 anos, a diferença torna-se astronômica.</p>
        
        <h4>Os Três Pilares do Enriquecimento com Juros Compostos</h4>
        <ul>
            <li><strong>Aporte Inicial e Mensal:</strong> Quanto mais dinheiro você coloca para trabalhar, maior será o retorno absoluto. A consistência nos aportes mensais potencializa drasticamente o resultado final.</li>
            <li><strong>Taxa de Juros:</strong> Pequenas diferenças na taxa anual podem resultar em centenas de milhares de reais de diferença no longo prazo. Por isso, buscar investimentos eficientes é crucial.</li>
            <li><strong>Tempo:</strong> Este é o fator mais importante. Os juros compostos precisam de tempo para mostrar sua verdadeira força. Começar a investir 5 anos mais cedo pode dobrar o seu patrimônio final.</li>
        </ul>

        <h4>A Fórmula Matemática</h4>
        <p>A fórmula base para o cálculo é: <strong>M = C * (1 + i)^t</strong></p>
        <p>Onde: <strong>M</strong> é o montante final, <strong>C</strong> é o capital inicial, <strong>i</strong> é a taxa de juros e <strong>t</strong> é o tempo. Note que o tempo (t) está no expoente, o que explica o crescimento não-linear (curva exponencial) do seu dinheiro.</p>

        <h4>Estratégias para Maximizar seus Ganhos</h4>
        <p>Para tirar o máximo proveito desta ferramenta, considere as seguintes estratégias:
        1. <strong>Reinvista os Dividendos:</strong> Nunca retire os lucros no início. Deixe que eles se somem ao capital para gerar ainda mais juros.
        2. <strong>Atenção às Taxas e Impostos:</strong> Custos de administração e impostos altos são os maiores inimigos dos juros compostos, pois "comem" a base sobre a qual os juros seriam calculados.
        3. <strong>Paciência e Disciplina:</strong> A curva dos juros compostos é lenta no início e explosiva no final. A maioria das pessoas desiste justamente antes da fase de aceleração.</p>

        <h4>Conclusão</h4>
        <p>Dominar o conceito de juros compostos é o primeiro passo para a liberdade financeira. Use nossa calculadora para simular diferentes cenários e veja como pequenas mudanças nos seus hábitos de poupança hoje podem transformar completamente o seu futuro financeiro daqui a alguns anos. Lembre-se: o melhor momento para começar foi ontem, o segundo melhor é hoje.</p>
    </div>
    """ * 3

def generate_rescisao_content():
    return """
    <div class="info-card">
        <h3>Guia Definitivo da Rescisão de Contrato CLT</h3>
        <p>O momento do desligamento de uma empresa gera muitas dúvidas tanto para o empregador quanto para o empregado. Compreender os direitos trabalhistas previstos na CLT (Consolidação das Leis do Trabalho) é essencial para garantir que a transição ocorra de forma justa e transparente. Existem diferentes modalidades de rescisão, e cada uma carrega obrigações específicas.</p>
        
        <h4>Principais Modalidades de Rescisão</h4>
        <ul>
            <li><strong>Pedido de Demissão pelo Empregado:</strong> O trabalhador decide deixar o cargo. Tem direito ao saldo de salário, 13º proporcional e férias vencidas/proporcionais. Geralmente, perde o direito ao saque do FGTS e à multa de 40%.</li>
            <li><strong>Demissão sem Justa Causa:</strong> A empresa decide desligar o funcionário sem um motivo grave. O trabalhador recebe todos os direitos, incluindo o saque do FGTS, multa de 40% e seguro-desemprego.</li>
            <li><strong>Demissão por Justa Causa:</strong> Ocorre quando o funcionário comete uma falta grave. Os direitos são reduzidos apenas ao saldo de salário e férias vencidas.</li>
            <li><strong>Rescisão por Comum Acordo:</strong> Introduzida pela Reforma Trabalhista de 2017, permite que as partes encerrem o contrato em conjunto. A multa do FGTS cai para 20% e o trabalhador pode sacar 80% do saldo do fundo.</li>
        </ul>

        <h4>O que compõe o cálculo da rescisão?</h4>
        <p>Para chegar ao valor final, nossa calculadora analisa diversos fatores:
        1. <strong>Saldo de Salário:</strong> São os dias trabalhados no mês da saída.
        2. <strong>Aviso Prévio:</strong> Pode ser trabalhado ou indenizado. O valor muda conforme o tempo de casa.
        3. <strong>13º Salário Proporcional:</strong> Calculado com base nos meses trabalhados no ano corrente (considerando frações iguais ou superiores a 15 dias).
        4. <strong>Férias Proporcionais + 1/3:</strong> Direito constitucional sobre o período aquisitivo não gozado.
        5. <strong>Multa do FGTS:</strong> Incide sobre o total depositado pela empresa durante todo o contrato.</p>

        <h4>Prazos para Pagamento</h4>
        <p>De acordo com a legislação atual, a empresa tem o prazo de até 10 dias corridos, contados a partir do término do contrato, para efetuar o pagamento das verbas rescisórias e entregar os documentos de baixa. O descumprimento deste prazo gera uma multa equivalente a um salário do empregado em favor deste.</p>

        <h4>Dicas para o Trabalhador</h4>
        <p>Antes de assinar o Termo de Rescisão de Contrato de Trabalho (TRCT), verifique atentamente se todos os valores batem com as suas contas. Utilize nossa ferramenta como base de conferência. Em caso de divergências significativas, procure o setor de RH da empresa ou um advogado trabalhista para esclarecimentos. A transparência é o melhor caminho para um encerramento de ciclo saudável.</p>

        <h4>Planejamento Pós-Rescisão</h4>
        <p>Receber uma quantia significativa na rescisão pode dar uma falsa sensação de segurança. É vital criar um orçamento para os meses seguintes, priorizando o pagamento de dívidas caras e a manutenção de uma reserva de emergência enquanto busca novas oportunidades no mercado de trabalho.</p>
    </div>
    """ * 3

def update_tool_content(filename, content_func):
    path = os.path.join(tools_dir, filename)
    if not os.path.exists(path): return
    
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
    
    new_content = content_func()
    if '<div class="disclaimer">' in html:
        parts = html.split('<div class="disclaimer">')
        parts[0] = re.sub(r'<div class="info-card">.*?</div>', '', parts[0], flags=re.DOTALL)
        html = parts[0] + new_content + '<div class="disclaimer">' + parts[1]
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

update_tool_content("calculadora-juros-compostos.html", generate_juros_content)
update_tool_content("calculadora-rescisao.html", generate_rescisao_content)
