import os

BASE_DIR = os.path.expanduser("~/granahoje.github.io")

IDIOMAS = [
    ("", "🇧🇷 PT-BR"), ("en", "🇺🇸 EN"), ("es", "🇪🇸 ES"),
    ("fr", "🇫🇷 FR"), ("ar", "🇸🇦 AR"), ("zh", "🇨🇳 ZH"),
    ("ru", "🇷🇺 RU"), ("hi", "🇮🇳 HI"), ("ja", "🇯🇵 JA"),
    ("bn", "🇧🇩 BN"), ("pt-pt", "🇵🇹 PT-PT")
]

def seletor_idiomas(arquivo):
    opts = ""
    for val, label in IDIOMAS:
        opts += f'<option value="{val}">{label}</option>\n'
    return f'''<select class="language-selector" onchange="window.location.href='/'+this.value+'/{arquivo}'" aria-label="Idioma" style="background:rgba(255,255,255,.05); border:1px solid rgba(255,255,255,.08); color:#f8fafc; padding:10px; border-radius:12px; font-weight:600; cursor:pointer; font-size:0.9rem; outline:none;">
<option value="">🌐 Idioma</option>
{opts}</select>'''

def header(arquivo):
    return f'''<header>
<div class="container header-inner">
<a class="logo" href="/">GRANA HOJE</a>
<nav class="nav-links">
{seletor_idiomas(arquivo)}
<a href="/blog.html">Blog</a>
<a href="/about.html">Sobre</a>
<a href="/contact.html">Contato</a>
</nav>
</div>
</header>'''

def afiliado(emoji, nome, descricao, link, botao):
    return f'''<div class="premium-affiliate-cta" style="margin:40px 0;padding:30px;background:linear-gradient(90deg,rgba(34,211,189,0.08) 0%,rgba(16,185,129,0.05) 100%);border-left:5px solid #22d3bd;border-radius:15px;box-shadow:0 10px 30px rgba(0,0,0,0.2);display:flex;align-items:center;gap:30px;">
<div style="font-size:3rem;flex-shrink:0;">{emoji}</div>
<div style="flex-grow:1;">
<h4 style="margin:0 0 10px;color:#22d3bd;font-size:1.3rem;font-weight:900;">Parceiro Recomendado</h4>
<p style="margin:0 0 15px;color:#b6c2d2;font-size:1rem;line-height:1.6;"><strong style="color:#fff;">{nome}</strong> {descricao}</p>
<a href="{link}" rel="nofollow" target="_blank" style="display:inline-block;padding:12px 30px;background:linear-gradient(135deg,#22d3bd 0%,#10b981 100%);color:#09111f;text-decoration:none;border-radius:10px;font-weight:900;font-size:0.95rem;box-shadow:0 8px 20px rgba(34,211,189,0.3);">{botao}</a>
</div>
</div>'''

def artigo_link():
    return '''<div style="margin:30px 0;padding:25px;background:rgba(34,211,189,0.05);border:1px solid rgba(34,211,189,0.2);border-radius:15px;text-align:center;">
<p style="color:var(--muted);margin-bottom:15px;font-size:0.95rem;">📚 Quer aprender mais?</p>
<a href="/blog.html" style="display:inline-block;padding:12px 30px;background:var(--primary);color:var(--bg);text-decoration:none;border-radius:10px;font-weight:900;box-shadow:0 4px 12px rgba(34,211,189,0.3);">Ler Artigo Completo →</a>
</div>'''

def base_html(titulo, meta_desc, arquivo, subtitulo, calculator_html, script_js, aff_html, info_html):
    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>{titulo} - Grana Hoje</title>
<meta name="description" content="{meta_desc}"/>
<link rel="stylesheet" href="/css/ferramentas.css">
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
main{{padding-top:20px;}}
.page-header{{padding:30px 0 20px;margin-bottom:0;}}
.page-title{{font-size:clamp(1.8rem,6vw,2.5rem);margin-bottom:12px;}}
.page-subtitle{{font-size:1rem;margin-bottom:0;}}
.calculator-container{{margin-top:30px;margin-bottom:40px;}}
.form-group-row{{display:grid;grid-template-columns:1fr 1fr;gap:16px;}}
@media(max-width:600px){{.form-group-row{{grid-template-columns:1fr;}}.page-title{{font-size:1.5rem;}}}}
</style>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4896859041377751" crossorigin="anonymous"></script>
</head>
<body>
{header(arquivo)}
<main class="container">
<header class="page-header">
<a href="/blog.html" class="back-link">
<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
Voltar para o Blog
</a>
<h1 class="page-title">{titulo}</h1>
<p class="page-subtitle">{subtitulo}</p>
</header>
<section class="calculator-container">
<div class="calculator-card">
{calculator_html}
</div>
{aff_html}
{artigo_link()}
<section class="info-content">
<div class="info-card">
{info_html}
</div>
</section>
</section>
</main>
<footer><div class="container"><p>© 2026 Grana Hoje. Educação financeira para todos.</p></div></footer>
<script>
function fmt(v){{return new Intl.NumberFormat('pt-BR',{{style:'currency',currency:'BRL'}}).format(v);}}
{script_js}
</script>
</body>
</html>'''

# ============================================================
# 1. CALCULADORA DE FGTS
# ============================================================
fgts_calc = '''
<div class="form-group-row">
<div class="form-group">
<label for="salario">Salário Bruto (R$)</label>
<input id="salario" type="number" min="0" step="0.01" placeholder="3000" value="3000"/>
</div>
<div class="form-group">
<label for="anos-fgts">Anos Trabalhados</label>
<input id="anos-fgts" type="number" min="0" step="1" placeholder="5" value="5"/>
</div>
</div>
<div class="form-group-row">
<div class="form-group">
<label for="meses-fgts">Meses Adicionais</label>
<input id="meses-fgts" type="number" min="0" max="11" step="1" placeholder="3" value="3"/>
</div>
<div class="form-group">
<label for="rendimento">Rendimento Médio FGTS (% ao ano)</label>
<input id="rendimento" type="number" min="0" step="0.01" placeholder="3" value="3"/>
</div>
</div>
<button class="btn-calculate" onclick="calcFGTS()" type="button">Calcular Saldo FGTS</button>
<div class="result-box" id="result-fgts">
<span class="result-label">Saldo Estimado do FGTS</span>
<span class="result-value" id="value-fgts">R$ 0,00</span>
<div id="det-fgts" style="margin-top:16px;text-align:left;font-size:0.9rem;color:var(--muted);"></div>
</div>'''

fgts_js = '''
function calcFGTS(){
  const sal = parseFloat(document.getElementById('salario').value)||0;
  const anos = parseInt(document.getElementById('anos-fgts').value)||0;
  const meses = parseInt(document.getElementById('meses-fgts').value)||0;
  const rend = parseFloat(document.getElementById('rendimento').value)/100||0.03;
  if(sal<=0){alert('Informe um salário válido.');return;}
  const totalMeses = anos*12 + meses;
  const deposMensal = sal*0.08;
  let saldo = 0;
  const taxaMensal = Math.pow(1+rend,1/12)-1;
  for(let i=0;i<totalMeses;i++){saldo=(saldo+deposMensal)*(1+taxaMensal);}
  document.getElementById('value-fgts').textContent = fmt(saldo);
  document.getElementById('result-fgts').classList.add('active');
  let h='<div style="border-top:1px solid rgba(255,255,255,0.1);padding-top:12px;">';
  h+=`<p><strong>Depósito Mensal (8%):</strong> ${fmt(deposMensal)}</p>`;
  h+=`<p><strong>Total Depositado:</strong> ${fmt(deposMensal*totalMeses)}</p>`;
  h+=`<p style="color:var(--primary);font-weight:700;"><strong>Saldo com Rendimento:</strong> ${fmt(saldo)}</p>`;
  h+=`<p style="color:var(--accent);"><strong>Rendimento Total:</strong> ${fmt(saldo-deposMensal*totalMeses)}</p>`;
  h+='</div>';
  document.getElementById('det-fgts').innerHTML=h;
}
window.addEventListener('load',calcFGTS);'''

fgts_info = '''<h3>FGTS: O Que É e Como Funciona na Prática</h3>
<p>O Fundo de Garantia do Tempo de Serviço, o famoso FGTS, é um dos direitos trabalhistas mais importantes do Brasil e, ao mesmo tempo, um dos menos compreendidos. Todo trabalhador com carteira assinada tem 8% do seu salário bruto depositado mensalmente pelo empregador em uma conta vinculada na Caixa Econômica Federal. Esse dinheiro é seu, mas com acesso restrito a situações específicas previstas em lei.</p>
<p>A grande questão que muitos trabalhadores se fazem é: quanto tenho guardado e quando posso usar? A resposta depende do tempo de serviço, do seu salário e dos rendimentos acumulados. Nossa calculadora te dá uma estimativa realista baseada nesses fatores, ajudando você a planejar o uso futuro do seu fundo.</p>
<h4>Quando Você Pode Sacar o FGTS?</h4>
<p>O saque do FGTS é permitido em diversas situações: demissão sem justa causa, aposentadoria, compra da casa própria, doenças graves como câncer e HIV, desastres naturais, e o chamado saque-aniversário. Cada modalidade tem suas regras e limitações. A demissão sem justa causa é o caso mais comum, e nela você tem direito ao saldo total mais a multa de 40% sobre o valor do fundo.</p>
<p>O saque-aniversário, criado em 2020, permite retirar uma parte do saldo todo ano no mês do seu aniversário. É uma opção interessante para quem precisa de liquidez, mas tem um custo: ao aderir, você abre mão da multa de 40% em caso de demissão sem justa causa. Analise bem antes de optar por essa modalidade.</p>
<h4>FGTS como Estratégia Financeira</h4>
<p>Muitos brasileiros encaram o FGTS apenas como uma reserva para emergências trabalhistas. Mas ele pode ser muito mais do que isso. O fundo pode ser usado como entrada na compra de um imóvel pelo programa Casa Verde e Amarela, reduzindo significativamente o valor financiado e, consequentemente, os juros pagos ao longo dos anos. Essa é uma das formas mais inteligentes de utilizar o benefício.</p>
<p>Outra estratégia é usar o FGTS para amortizar o saldo devedor de um financiamento imobiliário já existente. Dependendo das condições do seu contrato, isso pode reduzir o prazo ou o valor das parcelas, gerando uma economia expressiva em juros. Consulte seu banco ou a Caixa para entender as opções disponíveis no seu caso específico.</p>
<h4>Antecipação do FGTS: Vale a Pena?</h4>
<p>O mercado financeiro oferece produtos de antecipação do FGTS, especialmente do saque-aniversário. Bancos e fintechs permitem que você receba antecipadamente os valores futuros do seu fundo, cobrando juros sobre o montante. As taxas geralmente são menores que as do crédito pessoal tradicional, tornando essa uma opção razoável para quem precisa de crédito de emergência.</p>
<p>No entanto, ao antecipar o FGTS, você compromete uma renda futura garantida. Se surgir uma oportunidade melhor de uso do fundo, como a compra de um imóvel, você poderá estar com o saldo já comprometido. Pense bem antes de tomar essa decisão e use nossa calculadora para entender o impacto no seu planejamento de longo prazo.</p>
<h4>Conclusão</h4>
<p>O FGTS é uma reserva valiosa que todo trabalhador brasileiro acumula ao longo da carreira. Entendê-lo é o primeiro passo para usá-lo estrategicamente. Seja para a compra da casa própria, para uma reserva de emergência em caso de demissão, ou para amortização de dívidas, o fundo pode ser um aliado poderoso na sua jornada financeira. Use nossa ferramenta regularmente para acompanhar a evolução do seu saldo estimado e planejar o futuro com mais segurança.</p>'''

# ============================================================
# 2. CALCULADORA DE RENDA EXTRA
# ============================================================
renda_calc = '''
<div class="form-group">
<label for="renda-atual">Renda Mensal Atual (R$)</label>
<input id="renda-atual" type="number" min="0" step="0.01" placeholder="3000" value="3000"/>
</div>
<div class="form-group-row">
<div class="form-group">
<label for="meta-renda">Meta de Renda Extra (R$/mês)</label>
<input id="meta-renda" type="number" min="0" step="0.01" placeholder="1000" value="1000"/>
</div>
<div class="form-group">
<label for="horas-disp">Horas Disponíveis por Semana</label>
<input id="horas-disp" type="number" min="1" max="60" step="1" placeholder="10" value="10"/>
</div>
</div>
<div class="form-group">
<label for="valor-hora">Valor da Sua Hora de Trabalho (R$)</label>
<input id="valor-hora" type="number" min="0" step="0.01" placeholder="30" value="30"/>
</div>
<button class="btn-calculate" onclick="calcRenda()" type="button">Calcular Potencial de Renda Extra</button>
<div class="result-box" id="result-renda">
<span class="result-label">Renda Extra Mensal Potencial</span>
<span class="result-value" id="value-renda">R$ 0,00</span>
<div id="det-renda" style="margin-top:16px;text-align:left;font-size:0.9rem;color:var(--muted);"></div>
</div>'''

renda_js = '''
function calcRenda(){
  const atual = parseFloat(document.getElementById('renda-atual').value)||0;
  const meta = parseFloat(document.getElementById('meta-renda').value)||0;
  const horas = parseFloat(document.getElementById('horas-disp').value)||0;
  const valorHora = parseFloat(document.getElementById('valor-hora').value)||0;
  if(horas<=0||valorHora<=0){alert('Preencha todos os campos.');return;}
  const horasMes = horas*4.33;
  const rendaMes = horasMes*valorHora;
  const novaRenda = atual+rendaMes;
  const aumento = ((rendaMes/atual)*100).toFixed(1);
  document.getElementById('value-renda').textContent = fmt(rendaMes);
  document.getElementById('result-renda').classList.add('active');
  let h='<div style="border-top:1px solid rgba(255,255,255,0.1);padding-top:12px;">';
  h+=`<p><strong>Horas por Mês:</strong> ${horasMes.toFixed(0)}h</p>`;
  h+=`<p><strong>Renda Extra Mensal:</strong> ${fmt(rendaMes)}</p>`;
  h+=`<p><strong>Renda Total com Extra:</strong> ${fmt(novaRenda)}</p>`;
  h+=`<p style="color:var(--primary);font-weight:700;"><strong>Aumento na Renda:</strong> +${aumento}%</p>`;
  if(meta>0){
    const status = rendaMes>=meta ? '✅ Meta atingida!' : `⚠️ Faltam ${fmt(meta-rendaMes)} para a meta`;
    h+=`<p style="color:var(--accent);margin-top:8px;"><strong>${status}</strong></p>`;
  }
  h+='</div>';
  document.getElementById('det-renda').innerHTML=h;
}
window.addEventListener('load',calcRenda);'''

renda_info = '''<h3>Renda Extra em 2026: Como Transformar Tempo em Dinheiro</h3>
<p>Vivemos em uma era de oportunidades sem precedentes para quem quer aumentar sua renda. A economia digital derrubou barreiras que antes impediam pessoas comuns de oferecer seus talentos para o mundo. Hoje, com um smartphone e habilidades que você já tem, é possível gerar uma renda extra significativa sem sair de casa. A questão não é mais se é possível, mas sim como fazer de forma estratégica e sustentável.</p>
<p>A calculadora acima foi desenvolvida para te ajudar a visualizar o potencial real de uma renda extra baseada no seu tempo disponível e no valor da sua hora. Muitas pessoas subestimam o que podem gerar com apenas algumas horas semanais. Dez horas por semana a R$ 50,00 a hora representam R$ 2.165,00 mensais a mais no seu bolso. Isso pode mudar completamente sua situação financeira.</p>
<h4>As Melhores Fontes de Renda Extra em 2026</h4>
<p>O mercado de trabalho freelancer cresceu exponencialmente. Plataformas como Workana, 99Freelas e Upwork conectam profissionais brasileiros a clientes no mundo inteiro. Redação, design, programação, consultoria, tradução — se você tem uma habilidade, há alguém disposto a pagar por ela. O segredo é começar com projetos menores para construir reputação e ir aumentando as tarifas conforme o portfólio cresce.</p>
<p>Outra fonte poderosa é a criação de conteúdo digital. Cursos online, e-books, templates e mentorias são produtos que você cria uma vez e vende infinitas vezes. O mercado de educação digital no Brasil movimenta bilhões por ano, e a demanda por conhecimento prático e acessível nunca foi tão alta. Se você domina algum assunto, pode monetizá-lo com investimento mínimo.</p>
<h4>Como Precificar Seu Tempo Corretamente</h4>
<p>Um dos maiores erros de quem começa a trabalhar por conta é cobrar pouco demais. Muitos profissionais calculam seu valor hora dividindo o salário mensal por 220 horas e usam isso como referência. Mas esse raciocínio ignora fatores cruciais: impostos, tempo de prospecção de clientes, períodos sem trabalho e o valor do seu conhecimento especializado.</p>
<p>Uma regra mais realista: multiplique o valor hora CLT por 2,5 a 3 vezes para chegar a um preço freelancer justo. Isso cobre os custos extras de trabalhar por conta própria e garante que você não saia no prejuízo. Lembre-se: como autônomo, você assume riscos que o empregador assumia antes. Esse risco tem um custo que precisa estar no seu preço.</p>
<h4>Investindo a Renda Extra de Forma Inteligente</h4>
<p>De nada adianta gerar mais dinheiro se ele vai escorrer pelos dedos. A renda extra deve ter um destino claro desde o primeiro real. Sugerimos dividir em três partes: um terço para quitar dívidas ou criar reserva de emergência, um terço para investimentos de longo prazo, e um terço para reinvestir no próprio negócio paralelo, seja em cursos, equipamentos ou marketing.</p>
<p>Essa disciplina de alocar a renda extra antes de gastá-la é o que separa quem realmente transforma a situação financeira de quem simplesmente aumenta o padrão de consumo. O objetivo da renda extra não é consumir mais agora, mas construir liberdade financeira para o futuro.</p>
<h4>Conclusão</h4>
<p>A renda extra não é um luxo reservado a poucos privilegiados. É uma estratégia acessível a qualquer pessoa disposta a dedicar algumas horas semanais e aprender novas habilidades. Use nossa calculadora para definir sua meta, escolha a fonte de renda que melhor se encaixa no seu perfil e comece hoje. O melhor momento para começar era ontem; o segundo melhor momento é agora.</p>'''

# ============================================================
# 3. CALCULADORA DE CUSTO DE CARRO
# ============================================================
carro_calc = '''
<div class="form-group-row">
<div class="form-group">
<label for="parcela-carro">Parcela Mensal (R$)</label>
<input id="parcela-carro" type="number" min="0" step="0.01" placeholder="1200" value="1200"/>
</div>
<div class="form-group">
<label for="seguro-carro">Seguro Mensal (R$)</label>
<input id="seguro-carro" type="number" min="0" step="0.01" placeholder="250" value="250"/>
</div>
</div>
<div class="form-group-row">
<div class="form-group">
<label for="combustivel">Combustível/Mês (R$)</label>
<input id="combustivel" type="number" min="0" step="0.01" placeholder="400" value="400"/>
</div>
<div class="form-group">
<label for="ipva">IPVA Anual (R$)</label>
<input id="ipva" type="number" min="0" step="0.01" placeholder="1800" value="1800"/>
</div>
</div>
<div class="form-group-row">
<div class="form-group">
<label for="manutencao">Manutenção/Mês (R$)</label>
<input id="manutencao" type="number" min="0" step="0.01" placeholder="150" value="150"/>
</div>
<div class="form-group">
<label for="estacionamento">Estacionamento/Mês (R$)</label>
<input id="estacionamento" type="number" min="0" step="0.01" placeholder="100" value="100"/>
</div>
</div>
<button class="btn-calculate" onclick="calcCarro()" type="button">Calcular Custo Total</button>
<div class="result-box" id="result-carro">
<span class="result-label">Custo Total Mensal do Carro</span>
<span class="result-value" id="value-carro">R$ 0,00</span>
<div id="det-carro" style="margin-top:16px;text-align:left;font-size:0.9rem;color:var(--muted);"></div>
</div>'''

carro_js = '''
function calcCarro(){
  const parcela = parseFloat(document.getElementById('parcela-carro').value)||0;
  const seguro = parseFloat(document.getElementById('seguro-carro').value)||0;
  const comb = parseFloat(document.getElementById('combustivel').value)||0;
  const ipva = parseFloat(document.getElementById('ipva').value)||0;
  const manut = parseFloat(document.getElementById('manutencao').value)||0;
  const estac = parseFloat(document.getElementById('estacionamento').value)||0;
  const ipvaMes = ipva/12;
  const total = parcela+seguro+comb+ipvaMes+manut+estac;
  const anual = total*12;
  document.getElementById('value-carro').textContent = fmt(total);
  document.getElementById('result-carro').classList.add('active');
  let h='<div style="border-top:1px solid rgba(255,255,255,0.1);padding-top:12px;">';
  h+=`<p><strong>Financiamento:</strong> ${fmt(parcela)}/mês</p>`;
  h+=`<p><strong>Seguro:</strong> ${fmt(seguro)}/mês</p>`;
  h+=`<p><strong>Combustível:</strong> ${fmt(comb)}/mês</p>`;
  h+=`<p><strong>IPVA (mensal):</strong> ${fmt(ipvaMes)}/mês</p>`;
  h+=`<p><strong>Manutenção:</strong> ${fmt(manut)}/mês</p>`;
  h+=`<p><strong>Estacionamento:</strong> ${fmt(estac)}/mês</p>`;
  h+=`<p style="color:var(--accent);font-weight:700;margin-top:8px;"><strong>Total Mensal:</strong> ${fmt(total)}</p>`;
  h+=`<p style="color:var(--primary);font-weight:700;"><strong>Total Anual:</strong> ${fmt(anual)}</p>`;
  h+='</div>';
  document.getElementById('det-carro').innerHTML=h;
}
window.addEventListener('load',calcCarro);'''

carro_info = '''<h3>O Custo Real do Carro: O Que Ninguém Te Conta na Concessionária</h3>
<p>Comprar um carro é um dos maiores sonhos dos brasileiros e, ao mesmo tempo, uma das decisões financeiras mais complexas que uma pessoa pode tomar. A concessionária te mostra a parcela, o vendedor te seduz com o test drive, mas ninguém senta ao seu lado para calcular o custo total de ser proprietário de um veículo. É exatamente isso que nossa calculadora faz: revelar a realidade completa por trás do sonho.</p>
<p>Muita gente fica chocada quando soma todos os custos do carro pela primeira vez. Uma parcela de R$ 1.200,00 parece gerenciável, mas quando você adiciona seguro, combustível, IPVA, manutenção e estacionamento, o valor total frequentemente dobra ou triplica. Um carro que parecia caber no orçamento de repente consome 40% da renda familiar.</p>
<h4>Os Custos Invisíveis do Automóvel</h4>
<p>A parcela do financiamento é o custo mais visível, mas está longe de ser o único. O seguro de um carro novo pode custar de R$ 200,00 a R$ 800,00 por mês dependendo do modelo, perfil do motorista e cidade. O IPVA varia de estado para estado, mas representa em média 2% a 4% do valor do veículo por ano. Uma revisão básica pode custar R$ 500,00 a R$ 1.500,00. Pneus novos, R$ 800,00 a R$ 2.000,00 o jogo. Esses valores, diluídos mensalmente, pesam mais do que parece.</p>
<p>E tem o combustível. Com os preços atuais da gasolina no Brasil, um motorista que roda 1.500 km por mês com um carro que faz 12 km/l gasta aproximadamente R$ 450,00 a R$ 500,00 apenas em combustível. Some isso à depreciação do veículo, que pode ser de 15% a 25% no primeiro ano, e o custo real do carro se torna ainda mais impressionante.</p>
<h4>Carro Próprio vs Transporte por Aplicativo</h4>
<p>Uma comparação que cada vez mais brasileiros estão fazendo é entre ter carro próprio e usar aplicativos de transporte como principal meio de locomoção. Para quem não usa o carro diariamente ou mora em cidade com boa cobertura de aplicativos, pode ser financeiramente vantajoso abrir mão do veículo próprio.</p>
<p>Faça as contas: se seu carro custa R$ 2.500,00 por mês no total, você poderia usar esse dinheiro para pagar em torno de 80 a 100 corridas de aplicativo. Se você faz menos de 60 corridas por mês, o aplicativo pode ser mais barato. Mas se você tem família grande, mora longe do trabalho ou mora em cidade sem boa cobertura, o carro próprio ainda faz mais sentido.</p>
<h4>Como Reduzir os Custos do Seu Carro</h4>
<p>Se você já tem o carro, há estratégias para reduzir os custos. Compare seguros anualmente, pois as cotações variam muito entre seguradoras. Mantenha a revisão em dia para evitar problemas maiores e mais caros. Dirija de forma econômica, evitando acelerações bruscas que aumentam o consumo. Considere instalar GNV se rodar muito, pois a economia pode compensar o investimento em menos de dois anos.</p>
<h4>Conclusão</h4>
<p>O carro é um bem que tem custo emocional e prático inegável. Mas a decisão de comprar, manter ou trocar de veículo deve ser baseada em números reais, não em emoção. Use nossa calculadora regularmente para entender quanto seu carro realmente custa e se ele está dentro do que seu orçamento pode suportar com saúde. A regra geral é que o total de custos do automóvel não deve ultrapassar 15% da renda familiar. Se estiver acima disso, é hora de repensar.</p>'''

# ============================================================
# 4. CALCULADORA DE SEGURO DE VIDA
# ============================================================
seguro_calc = '''
<div class="form-group-row">
<div class="form-group">
<label for="renda-seguro">Renda Mensal Familiar (R$)</label>
<input id="renda-seguro" type="number" min="0" step="0.01" placeholder="5000" value="5000"/>
</div>
<div class="form-group">
<label for="dependentes">Número de Dependentes</label>
<input id="dependentes" type="number" min="0" max="10" step="1" placeholder="2" value="2"/>
</div>
</div>
<div class="form-group-row">
<div class="form-group">
<label for="dividas">Total de Dívidas (R$)</label>
<input id="dividas" type="number" min="0" step="0.01" placeholder="50000" value="50000"/>
</div>
<div class="form-group">
<label for="anos-cobertura">Anos de Cobertura Desejados</label>
<input id="anos-cobertura" type="number" min="1" max="30" step="1" placeholder="10" value="10"/>
</div>
</div>
<button class="btn-calculate" onclick="calcSeguro()" type="button">Calcular Cobertura Ideal</button>
<div class="result-box" id="result-seguro">
<span class="result-label">Cobertura Recomendada</span>
<span class="result-value" id="value-seguro">R$ 0,00</span>
<div id="det-seguro" style="margin-top:16px;text-align:left;font-size:0.9rem;color:var(--muted);"></div>
</div>'''

seguro_js = '''
function calcSeguro(){
  const renda = parseFloat(document.getElementById('renda-seguro').value)||0;
  const dep = parseInt(document.getElementById('dependentes').value)||0;
  const dividas = parseFloat(document.getElementById('dividas').value)||0;
  const anos = parseInt(document.getElementById('anos-cobertura').value)||10;
  if(renda<=0){alert('Informe a renda familiar.');return;}
  const rendaAnual = renda*12;
  const coberturaRenda = rendaAnual*anos;
  const fatorDep = 1+(dep*0.1);
  const coberturaNecessaria = (coberturaRenda*fatorDep)+dividas;
  const estimMensal = coberturaNecessaria*0.0003;
  document.getElementById('value-seguro').textContent = fmt(coberturaNecessaria);
  document.getElementById('result-seguro').classList.add('active');
  let h='<div style="border-top:1px solid rgba(255,255,255,0.1);padding-top:12px;">';
  h+=`<p><strong>Cobertura de Renda (${anos} anos):</strong> ${fmt(coberturaRenda)}</p>`;
  h+=`<p><strong>Cobertura para Dívidas:</strong> ${fmt(dividas)}</p>`;
  h+=`<p><strong>Fator Dependentes (${dep}):</strong> +${(dep*10)}%</p>`;
  h+=`<p style="color:var(--primary);font-weight:700;margin-top:8px;"><strong>Cobertura Total Recomendada:</strong> ${fmt(coberturaNecessaria)}</p>`;
  h+=`<p style="color:var(--accent);"><strong>Prêmio Estimado/Mês:</strong> ${fmt(estimMensal)}</p>`;
  h+='</div>';
  document.getElementById('det-seguro').innerHTML=h;
}
window.addEventListener('load',calcSeguro);'''

seguro_info = '''<h3>Seguro de Vida: O Investimento que Protege Quem Você Ama</h3>
<p>Falar sobre seguro de vida é falar sobre algo que a maioria das pessoas prefere evitar: a própria mortalidade. Mas ignorar essa realidade pode deixar as pessoas que você mais ama em uma situação financeira devastadora. O seguro de vida não é um gasto; é uma declaração de amor e responsabilidade. É garantir que, mesmo na sua ausência, sua família terá condições de manter o padrão de vida, quitar dívidas e construir o futuro que vocês planejaram juntos.</p>
<p>No Brasil, a penetração do seguro de vida ainda é baixa comparada a países desenvolvidos. Muitos brasileiros acreditam que é caro, complicado ou desnecessário. Mas a realidade é que os planos básicos de seguro de vida têm preços acessíveis, especialmente para pessoas mais jovens, e podem oferecer coberturas de centenas de milhares de reais por valores mensais modestos.</p>
<h4>Quanto de Cobertura Você Realmente Precisa?</h4>
<p>A nossa calculadora usa uma metodologia amplamente adotada por planejadores financeiros: soma a renda que você precisaria repor pelos anos que seus dependentes precisariam de suporte, mais as dívidas existentes, ajustada pelo número de dependentes. É uma estimativa conservadora, mas realista, que garante que sua família não passará aperto financeiro em um momento já tão difícil emocionalmente.</p>
<p>Uma regra prática usada por muitos especialistas é ter uma cobertura equivalente a 10 vezes a renda anual bruta. Se você ganha R$ 5.000,00 por mês, sua cobertura ideal seria em torno de R$ 600.000,00. Pode parecer um número alto, mas quando você divide o prêmio mensal correspondente pela proteção oferecida, o custo-benefício é extraordinário.</p>
<h4>Tipos de Seguro de Vida no Brasil</h4>
<p>O mercado brasileiro oferece basicamente dois tipos principais: o seguro de vida temporário e o seguro de vida inteiro. O temporário é contratado por um período específico, geralmente de 10 a 30 anos, e é mais barato. É ideal para quem tem filhos pequenos ou dívidas de longo prazo como financiamento imobiliário. O seguro de vida inteiro tem cobertura vitalícia e geralmente inclui uma componente de acúmulo de valor, mas é significativamente mais caro.</p>
<p>Além da cobertura por morte, muitos seguros oferecem coberturas adicionais como invalidez permanente, doenças graves e diária por internação hospitalar. Essas coberturas complementares podem fazer uma enorme diferença em situações de doença grave, onde você ainda está vivo mas incapacitado de trabalhar. Avalie quais coberturas fazem sentido para o seu perfil e momento de vida.</p>
<h4>Como Escolher a Seguradora Certa</h4>
<p>Não escolha um seguro de vida apenas pelo preço. A solidez financeira da seguradora é fundamental, pois você quer ter certeza de que ela estará lá para pagar quando necessário. Verifique a classificação da empresa nos órgãos reguladores, leia as condições gerais do contrato com atenção e compare pelo menos três cotações antes de decidir. Nosso parceiro recomendado nesta página oferece cotações personalizadas com atendimento especializado.</p>
<h4>Conclusão</h4>
<p>O seguro de vida é um dos pilares de uma estratégia financeira sólida, especialmente para quem tem dependentes. Use nossa calculadora para entender qual cobertura faz sentido para você, compare opções no mercado e tome uma decisão informada. Proteger sua família é proteger tudo que você construiu. Não deixe para amanhã uma decisão que pode mudar o futuro de quem você ama.</p>'''

# ============================================================
# GERAR OS ARQUIVOS
# ============================================================
calculadoras = [
    {
        "arquivo": "calculadora-fgts.html",
        "titulo": "Calculadora de FGTS",
        "meta": "Calcule seu saldo do FGTS, simule rendimentos e saiba quanto você tem direito a receber.",
        "subtitulo": "Simule seu saldo, rendimentos e descubra quando e como usar seu FGTS.",
        "calc": fgts_calc,
        "js": fgts_js,
        "aff": afiliado("🏦", "Credspot", "é especialista em antecipação de FGTS com taxas competitivas. Simule gratuitamente e receba seu dinheiro rapidamente.", "https://apretailer.com.br/click/6a0bab802bfa817b98549fd2/187799/358980/subaccount", "Simular Antecipação →"),
        "info": fgts_info,
        "card_icon": "💰",
        "card_desc": "Simule seu saldo, rendimentos e saiba como usar seu FGTS estrategicamente."
    },
    {
        "arquivo": "calculadora-renda-extra.html",
        "titulo": "Calculadora de Renda Extra",
        "meta": "Calcule seu potencial de renda extra com base no seu tempo disponível e valor hora.",
        "subtitulo": "Descubra quanto você pode ganhar a mais por mês com seu tempo disponível.",
        "calc": renda_calc,
        "js": renda_js,
        "aff": afiliado("📈", "CasaTrade", "oferece uma plataforma completa para quem quer investir a renda extra e fazer o dinheiro trabalhar por você.", "https://apretailer.com.br/click/6a0bab802bfa817bc269d5c2/186975/358980/subaccount", "Conhecer a Plataforma →"),
        "info": renda_info,
        "card_icon": "💡",
        "card_desc": "Descubra quanto você pode ganhar a mais por mês com seu tempo disponível."
    },
    {
        "arquivo": "calculadora-custo-carro.html",
        "titulo": "Calculadora de Custo do Carro",
        "meta": "Calcule o custo real mensal do seu carro incluindo parcela, seguro, combustível, IPVA e manutenção.",
        "subtitulo": "Descubra quanto seu carro realmente custa por mês considerando todos os gastos.",
        "calc": carro_calc,
        "js": carro_js,
        "aff": afiliado("🚗", "Minuto Seguros", "compara seguros de carro de diversas seguradoras para você encontrar a melhor proteção pelo melhor preço.", "https://apretailer.com.br/click/6a0bab802bfa8144cc0ad9b2/183524/358980/subaccount", "Comparar Seguros →"),
        "info": carro_info,
        "card_icon": "🚗",
        "card_desc": "Descubra o custo real do seu carro somando parcela, seguro, combustível e IPVA."
    },
    {
        "arquivo": "calculadora-seguro-vida.html",
        "titulo": "Calculadora de Seguro de Vida",
        "meta": "Calcule a cobertura ideal de seguro de vida para proteger sua família financeiramente.",
        "subtitulo": "Descubra qual cobertura de seguro de vida é ideal para proteger sua família.",
        "calc": seguro_calc,
        "js": seguro_js,
        "aff": afiliado("🛡️", "Minuto Seguros", "compara planos de seguro de vida de diversas seguradoras para você encontrar a melhor proteção pelo menor preço.", "https://apretailer.com.br/click/6a0bab802bfa8144cc0ad9b2/183524/358980/subaccount", "Comparar Planos →"),
        "info": seguro_info,
        "card_icon": "🛡️",
        "card_desc": "Calcule a cobertura ideal de seguro de vida para proteger sua família."
    }
]

# Gerar HTMLs
for c in calculadoras:
    html = base_html(
        c["titulo"], c["meta"], c["arquivo"], c["subtitulo"],
        c["calc"], c["js"], c["aff"], c["info"]
    )
    path = os.path.join(BASE_DIR, c["arquivo"])
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ {c['arquivo']}")

# Atualizar ferramentas.html
ferr_path = os.path.join(BASE_DIR, "ferramentas.html")
ferr = open(ferr_path, encoding="utf-8").read()

cards = ""
for c in calculadoras:
    nome = c["arquivo"].replace(".html","")
    cards += f'''
<a class="tool-card" href="/{c['arquivo']}">
<div class="tool-icon">{c["card_icon"]}</div>
<h3>{c["titulo"]}</h3>
<p>{c["card_desc"]}</p>
<span class="tool-link">Acessar Calculadora →</span>
</a>'''

ferr_new = ferr.replace('</div>\n</main>', cards + '\n</div>\n</main>')
with open(ferr_path, "w", encoding="utf-8") as f:
    f.write(ferr_new)
print("✅ ferramentas.html atualizado!")
print("\n🎉 Tudo pronto! Agora rode:")
print("git add -A && git commit -m 'Adiciona 4 novas calculadoras financeiras' && git push origin main")


