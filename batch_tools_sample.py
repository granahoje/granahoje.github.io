import os

template = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Grana Hoje</title>
    <style>
        :root {{ --primary:#22d3bd; --bg:#09111f; --bg-soft:#0f1b2d; --text:#f8fafc; --muted:#a8b3c7; }}
        body {{ font-family:'Plus Jakarta Sans',sans-serif; background:var(--bg); color:var(--text); line-height:1.6; margin:0; }}
        .container {{ width:min(100%, 800px); margin:0 auto; padding:40px 20px; }}
        .calc-card {{ background:var(--bg-soft); padding:40px; border-radius:25px; border:1px solid rgba(34,211,189,0.2); box-shadow:0 20px 40px rgba(0,0,0,0.3); }}
        .header {{ text-align:center; margin-bottom:40px; }}
        .header h1 {{ color:var(--primary); font-size:2rem; font-weight:900; margin-bottom:10px; }}
        .header p {{ color:var(--muted); }}
        .input-group {{ margin-bottom:25px; }}
        label {{ display:block; margin-bottom:10px; font-weight:700; color:var(--muted); font-size:0.9rem; text-transform:uppercase; }}
        input {{ width:100%; padding:15px; background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); border-radius:12px; color:#fff; font-size:1.1rem; outline:none; transition:0.3s; }}
        input:focus {{ border-color:var(--primary); background:rgba(255,255,255,0.08); }}
        .btn-calc {{ width:100%; padding:18px; background:var(--primary); color:var(--bg); border:none; border-radius:12px; font-weight:900; font-size:1.1rem; cursor:pointer; transition:0.3s; }}
        .btn-calc:hover {{ transform:translateY(-3px); box-shadow:0 15px 30px rgba(34,211,189,0.3); }}
        .result-box {{ margin-top:40px; padding:30px; background:rgba(34,211,189,0.1); border-radius:20px; text-align:center; display:none; border:1px solid rgba(34,211,189,0.2); }}
        .result-title {{ color:var(--muted); font-size:1rem; margin-bottom:10px; }}
        .result-value {{ font-size:2.5rem; font-weight:900; color:var(--primary); display:block; }}
        .explanation {{ margin-top:40px; color:var(--muted); font-size:0.95rem; }}
        .explanation h2 {{ color:#fff; font-size:1.3rem; margin-bottom:15px; }}
    </style>
</head>
<body>
    <header style="background:rgba(9,17,31,0.8); backdrop-filter:blur(15px); border-bottom:1px solid rgba(255,255,255,0.05); padding:15px 0; position:sticky; top:0; z-index:100;">
        <div style="width:min(100%, 1200px); margin:0 auto; padding:0 20px; display:flex; justify-content:space-between; align-items:center;">
            <a href="/" style="color:var(--primary); text-decoration:none; font-weight:800; font-size:1.3rem;">GRANA HOJE</a>
            <a href="/blog.html" style="color:#fff; text-decoration:none; font-weight:700;">Blog</a>
        </div>
    </header>
    <main class="container">
        <div class="calc-card">
            <div class="header">
                <span style="font-size:3.5rem; display:block; margin-bottom:15px;">{icon}</span>
                <h1>{title}</h1>
                <p>{description}</p>
            </div>
            {inputs}
            <button class="btn-calc" onclick="calcular()">Calcular Agora</button>
            <div class="result-box" id="resultBox">
                <p class="result-title">Resultado Estimado:</p>
                <span class="result-value" id="resultValue">---</span>
                <p id="resultDetail" style="margin-top:15px; color:var(--primary); font-weight:700;"></p>
            </div>
            <div class="explanation">
                <h2>Como funciona esta ferramenta?</h2>
                <p>{explanation}</p>
            </div>
        </div>
    </main>
    <script>
        function calcular() {{
            {logic}
            document.getElementById('resultBox').style.display = 'block';
        }}
    </script>
</body>
</html>
"""

tools = [
    {
        "filename": "comparador-cdb-poupanca.html",
        "icon": "🏦",
        "title": "CDB vs Poupança",
        "description": "Descubra qual investimento rende mais para o seu dinheiro hoje.",
        "inputs": """
            <div class="input-group">
                <label>Valor a Investir (R$)</label>
                <input type="number" id="valor" placeholder="1000">
            </div>
            <div class="input-group">
                <label>Taxa do CDB (% do CDI)</label>
                <input type="number" id="cdi_perc" placeholder="100">
            </div>
            <div class="input-group">
                <label>Prazo (Meses)</label>
                <input type="number" id="meses" placeholder="12">
            </div>
        """,
        "logic": """
            const v = parseFloat(document.getElementById('valor').value);
            const cdi = 0.1125; // CDI Atual 11.25%
            const cdb_taxa = (parseFloat(document.getElementById('cdi_perc').value) / 100) * cdi;
            const t = parseFloat(document.getElementById('meses').value);
            
            const rend_poup = v * (Math.pow(1 + 0.005, t) - 1);
            const rend_cdb_bruto = v * (Math.pow(1 + (cdb_taxa/12), t) - 1);
            let ir = 0.225;
            if(t > 24) ir = 0.15;
            else if(t > 12) ir = 0.175;
            else if(t > 6) ir = 0.20;
            
            const rend_cdb_liquido = rend_cdb_bruto * (1 - ir);
            const diff = rend_cdb_liquido - rend_poup;
            
            document.getElementById('resultValue').innerText = rend_cdb_liquido.toLocaleString('pt-BR', {style:'currency', currency:'BRL'});
            document.getElementById('resultDetail').innerText = diff > 0 ? `O CDB rende R$ ${diff.toFixed(2)} a mais que a poupança.` : `Neste caso, a poupança é competitiva.`;
        """,
        "explanation": "Esta calculadora utiliza a taxa SELIC/CDI atual para projetar o rendimento de um CDB pós-fixado, descontando o Imposto de Renda regressivo e comparando com o rendimento fixo da poupança (0,5% ao mês + TR)."
    },
    {
        "filename": "calculadora-ponto-equilibrio.html",
        "icon": "⚖️",
        "title": "Ponto de Equilíbrio",
        "description": "Saiba quanto sua empresa precisa vender para não ter prejuízo.",
        "inputs": """
            <div class="input-group">
                <label>Custos Fixos Totais (R$)</label>
                <input type="number" id="fixos" placeholder="5000">
            </div>
            <div class="input-group">
                <label>Preço de Venda Unitário (R$)</label>
                <input type="number" id="preco" placeholder="100">
            </div>
            <div class="input-group">
                <label>Custo Variável Unitário (R$)</label>
                <input type="number" id="variavel" placeholder="60">
            </div>
        """,
        "logic": """
            const f = parseFloat(document.getElementById('fixos').value);
            const p = parseFloat(document.getElementById('preco').value);
            const v = parseFloat(document.getElementById('variavel').value);
            
            const margem = p - v;
            if(margem <= 0) {
                alert("O preço de venda deve ser maior que o custo variável!");
                return;
            }
            const pe = f / margem;
            
            document.getElementById('resultValue').innerText = Math.ceil(pe) + " Unidades";
            document.getElementById('resultDetail').innerText = `Você precisa vender ${Math.ceil(pe)} unidades para cobrir seus custos fixos de R$ ${f.toFixed(2)}.`;
        """,
        "explanation": "O Ponto de Equilíbrio (Break-even Point) é o volume de vendas necessário para que a receita total seja igual aos custos totais. É o momento em que a empresa começa a ter lucro."
    }
]

for tool in tools:
    path = os.path.join('/home/ubuntu/granahoje.github.io', tool['filename'])
    with open(path, 'w', encoding='utf-8') as f:
        f.write(template.format(**tool))
    print(f"Criada: {tool['filename']}")
