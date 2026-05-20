import os
import json
from pathlib import Path

# Dicionário de traduções para os 10 idiomas
translations = {
    "pt-br": {
        "header_title": "GRANA HOJE",
        "blog": "Blog",
        "result": "Resultado Estimado:",
        "calculate": "Calcular Agora",
        "how_works": "Como funciona esta ferramenta?",
        "financing": "Simulador de Financiamento Imobiliário",
        "financing_desc": "Compare SAC vs PRICE e veja qual é melhor para você.",
        "financing_inputs": [
            ("Valor do Imóvel (R$)", "imovel"),
            ("Entrada (R$)", "entrada"),
            ("Taxa de Juros (% a.a.)", "taxa"),
            ("Prazo (Anos)", "anos")
        ],
        "financing_explain": "O SAC (Sistema de Amortização Constante) tem parcelas decrescentes. O PRICE tem parcelas fixas. Esta ferramenta calcula ambos para você comparar.",
        
        "rescisao": "Calculadora de Rescisão (CLT)",
        "rescisao_desc": "Saiba quanto você deve receber ao ser demitido.",
        "rescisao_inputs": [
            ("Salário Mensal (R$)", "salario"),
            ("Tempo de Serviço (Anos)", "anos"),
            ("Tem Justa Causa?", "justa_causa")
        ],
        "rescisao_explain": "Calcula aviso prévio, 13º proporcional, FGTS + multa de 40%, férias proporcionais e saldo de salário.",
        
        "independencia": "Independência Financeira (Regra 4%)",
        "independencia_desc": "Quanto você precisa poupar para nunca mais trabalhar.",
        "independencia_inputs": [
            ("Gasto Mensal (R$)", "gasto"),
            ("Retorno Anual Esperado (%)", "retorno")
        ],
        "independencia_explain": "A Regra dos 4% diz que você pode sacar 4% do seu patrimônio anualmente sem correr risco de falência.",
        
        "satoshi": "Conversor Satoshi para Real",
        "satoshi_desc": "Converta Satoshis (menor unidade do Bitcoin) para reais.",
        "satoshi_inputs": [
            ("Quantidade de Satoshis", "satoshi"),
            ("Preço do Bitcoin (R$)", "preco_btc")
        ],
        "satoshi_explain": "1 Bitcoin = 100.000.000 Satoshis. Esta ferramenta converte pequenas quantidades para reais.",
        
        "orcamento": "Simulador de Orçamento (50/30/20)",
        "orcamento_desc": "Distribua sua renda de forma inteligente: 50% necessidades, 30% desejos, 20% poupança.",
        "orcamento_inputs": [
            ("Renda Mensal (R$)", "renda")
        ],
        "orcamento_explain": "A regra 50/30/20 é um método simples de orçamento que ajuda a manter o controle financeiro."
    },
    "en": {
        "header_title": "GRANA TODAY",
        "blog": "Blog",
        "result": "Estimated Result:",
        "calculate": "Calculate Now",
        "how_works": "How does this tool work?",
        "financing": "Real Estate Financing Simulator",
        "financing_desc": "Compare SAC vs PRICE and see which is best for you.",
        "financing_inputs": [
            ("Property Value (R$)", "imovel"),
            ("Down Payment (R$)", "entrada"),
            ("Interest Rate (% p.a.)", "taxa"),
            ("Term (Years)", "anos")
        ],
        "financing_explain": "SAC (Constant Amortization System) has decreasing installments. PRICE has fixed installments. This tool calculates both for comparison.",
        
        "rescisao": "Termination Calculator (CLT)",
        "rescisao_desc": "Find out how much you should receive if dismissed.",
        "rescisao_inputs": [
            ("Monthly Salary (R$)", "salario"),
            ("Years of Service", "anos"),
            ("Just Cause?", "justa_causa")
        ],
        "rescisao_explain": "Calculates notice period, proportional 13th salary, FGTS + 40% fine, proportional vacation and balance.",
        
        "independencia": "Financial Independence (4% Rule)",
        "independencia_desc": "How much do you need to save to never work again.",
        "independencia_inputs": [
            ("Monthly Expenses (R$)", "gasto"),
            ("Expected Annual Return (%)", "retorno")
        ],
        "independencia_explain": "The 4% Rule states you can withdraw 4% of your assets annually without bankruptcy risk.",
        
        "satoshi": "Satoshi to Real Converter",
        "satoshi_desc": "Convert Satoshis (smallest Bitcoin unit) to reais.",
        "satoshi_inputs": [
            ("Satoshi Amount", "satoshi"),
            ("Bitcoin Price (R$)", "preco_btc")
        ],
        "satoshi_explain": "1 Bitcoin = 100,000,000 Satoshis. This tool converts small amounts to reais.",
        
        "orcamento": "Budget Simulator (50/30/20)",
        "orcamento_desc": "Distribute your income wisely: 50% needs, 30% wants, 20% savings.",
        "orcamento_inputs": [
            ("Monthly Income (R$)", "renda")
        ],
        "orcamento_explain": "The 50/30/20 rule is a simple budgeting method to maintain financial control."
    },
    "es": {
        "header_title": "GRANA HOY",
        "blog": "Blog",
        "result": "Resultado Estimado:",
        "calculate": "Calcular Ahora",
        "how_works": "¿Cómo funciona esta herramienta?",
        "financing": "Simulador de Financiamiento Inmobiliario",
        "financing_desc": "Compara SAC vs PRICE y ve cuál es mejor para ti.",
        "financing_inputs": [
            ("Valor de la Propiedad (R$)", "imovel"),
            ("Entrada (R$)", "entrada"),
            ("Tasa de Interés (% a.a.)", "taxa"),
            ("Plazo (Años)", "anos")
        ],
        "financing_explain": "SAC tiene cuotas decrecientes. PRICE tiene cuotas fijas. Esta herramienta calcula ambas para comparación.",
        
        "rescisao": "Calculadora de Rescisión (CLT)",
        "rescisao_desc": "Descubre cuánto deberías recibir si eres despedido.",
        "rescisao_inputs": [
            ("Salario Mensual (R$)", "salario"),
            ("Años de Servicio", "anos"),
            ("¿Causa Justa?", "justa_causa")
        ],
        "rescisao_explain": "Calcula aviso previo, 13º proporcional, FGTS + multa del 40%, vacaciones proporcionles y saldo.",
        
        "independencia": "Independencia Financiera (Regla 4%)",
        "independencia_desc": "Cuánto necesitas ahorrar para nunca volver a trabajar.",
        "independencia_inputs": [
            ("Gastos Mensuales (R$)", "gasto"),
            ("Retorno Anual Esperado (%)", "retorno")
        ],
        "independencia_explain": "La Regla del 4% dice que puedes retirar el 4% de tu patrimonio anualmente sin riesgo de quiebra.",
        
        "satoshi": "Conversor Satoshi a Real",
        "satoshi_desc": "Convierte Satoshis (unidad más pequeña de Bitcoin) a reales.",
        "satoshi_inputs": [
            ("Cantidad de Satoshis", "satoshi"),
            ("Precio del Bitcoin (R$)", "preco_btc")
        ],
        "satoshi_explain": "1 Bitcoin = 100.000.000 Satoshis. Esta herramienta convierte pequeñas cantidades a reales.",
        
        "orcamento": "Simulador de Presupuesto (50/30/20)",
        "orcamento_desc": "Distribuye tu ingreso inteligentemente: 50% necesidades, 30% deseos, 20% ahorros.",
        "orcamento_inputs": [
            ("Ingreso Mensual (R$)", "renda")
        ],
        "orcamento_explain": "La regla 50/30/20 es un método simple de presupuesto para mantener el control financiero."
    },
    "fr": {
        "header_title": "GRANA AUJOURD'HUI",
        "blog": "Blog",
        "result": "Résultat Estimé:",
        "calculate": "Calculer Maintenant",
        "how_works": "Comment fonctionne cet outil?",
        "financing": "Simulateur de Financement Immobilier",
        "financing_desc": "Comparez SAC vs PRICE et voyez lequel est le mieux pour vous.",
        "financing_inputs": [
            ("Valeur de la Propriété (R$)", "imovel"),
            ("Apport (R$)", "entrada"),
            ("Taux d'Intérêt (% p.a.)", "taxa"),
            ("Durée (Années)", "anos")
        ],
        "financing_explain": "SAC a des versements décroissants. PRICE a des versements fixes. Cet outil calcule les deux pour la comparaison.",
        
        "rescisao": "Calculatrice de Résiliation (CLT)",
        "rescisao_desc": "Découvrez combien vous devriez recevoir si vous êtes licencié.",
        "rescisao_inputs": [
            ("Salaire Mensuel (R$)", "salario"),
            ("Années de Service", "anos"),
            ("Cause Juste?", "justa_causa")
        ],
        "rescisao_explain": "Calcule le préavis, le 13e proportionnel, FGTS + amende de 40%, congés proportionnels et solde.",
        
        "independencia": "Indépendance Financière (Règle 4%)",
        "independencia_desc": "Combien devez-vous économiser pour ne jamais travailler à nouveau.",
        "independencia_inputs": [
            ("Dépenses Mensuelles (R$)", "gasto"),
            ("Rendement Annuel Attendu (%)", "retorno")
        ],
        "independencia_explain": "La Règle des 4% stipule que vous pouvez retirer 4% de votre patrimoine annuellement sans risque de faillite.",
        
        "satoshi": "Convertisseur Satoshi en Real",
        "satoshi_desc": "Convertissez les Satoshis (plus petite unité de Bitcoin) en reals.",
        "satoshi_inputs": [
            ("Quantité de Satoshis", "satoshi"),
            ("Prix du Bitcoin (R$)", "preco_btc")
        ],
        "satoshi_explain": "1 Bitcoin = 100 000 000 Satoshis. Cet outil convertit de petites quantités en reals.",
        
        "orcamento": "Simulateur de Budget (50/30/20)",
        "orcamento_desc": "Distribuez votre revenu intelligemment: 50% besoins, 30% envies, 20% épargne.",
        "orcamento_inputs": [
            ("Revenu Mensuel (R$)", "renda")
        ],
        "orcamento_explain": "La règle 50/30/20 est une méthode simple de budgétisation pour maintenir le contrôle financier."
    },
    "ar": {
        "header_title": "جرانا اليوم",
        "blog": "مدونة",
        "result": "النتيجة المقدرة:",
        "calculate": "احسب الآن",
        "how_works": "كيف تعمل هذه الأداة؟",
        "financing": "محاكي التمويل العقاري",
        "financing_desc": "قارن بين SAC و PRICE واكتشف أيهما أفضل لك.",
        "financing_inputs": [
            ("قيمة العقار (R$)", "imovel"),
            ("الدفعة الأولى (R$)", "entrada"),
            ("سعر الفائدة (% سنويًا)", "taxa"),
            ("المدة (سنوات)", "anos")
        ],
        "financing_explain": "SAC له أقساط متناقصة. PRICE له أقساط ثابتة. تحسب هذه الأداة كليهما للمقارنة.",
        
        "rescisao": "حاسبة الفسخ (CLT)",
        "rescisao_desc": "اكتشف كم يجب أن تتلقى إذا تم فصلك.",
        "rescisao_inputs": [
            ("الراتب الشهري (R$)", "salario"),
            ("سنوات الخدمة", "anos"),
            ("سبب عادل؟", "justa_causa")
        ],
        "rescisao_explain": "يحسب الإشعار المسبق والراتب الثالث عشر والـ FGTS وغرامة 40% والإجازة النسبية والرصيد.",
        
        "independencia": "الاستقلال المالي (قاعدة 4%)",
        "independencia_desc": "كم تحتاج لتوفير لعدم العمل مرة أخرى.",
        "independencia_inputs": [
            ("النفقات الشهرية (R$)", "gasto"),
            ("العائد السنوي المتوقع (%)", "retorno")
        ],
        "independencia_explain": "تنص قاعدة 4% على أنه يمكنك سحب 4% من أصولك سنويًا دون خطر الإفلاس.",
        
        "satoshi": "محول ساتوشي إلى ريال",
        "satoshi_desc": "حول ساتوشي (أصغر وحدة بيتكوين) إلى ريال.",
        "satoshi_inputs": [
            ("كمية ساتوشي", "satoshi"),
            ("سعر البيتكوين (R$)", "preco_btc")
        ],
        "satoshi_explain": "1 بيتكوين = 100,000,000 ساتوشي. تحول هذه الأداة كميات صغيرة إلى ريال.",
        
        "orcamento": "محاكي الميزانية (50/30/20)",
        "orcamento_desc": "وزع دخلك بذكاء: 50% احتياجات، 30% رغبات، 20% توفير.",
        "orcamento_inputs": [
            ("الدخل الشهري (R$)", "renda")
        ],
        "orcamento_explain": "قاعدة 50/30/20 هي طريقة بسيطة للميزانية للحفاظ على السيطرة المالية."
    },
    "zh": {
        "header_title": "今日格拉纳",
        "blog": "博客",
        "result": "估计结果：",
        "calculate": "现在计算",
        "how_works": "此工具如何工作？",
        "financing": "房地产融资模拟器",
        "financing_desc": "比较SAC与PRICE，看哪个最适合您。",
        "financing_inputs": [
            ("房产价值 (R$)", "imovel"),
            ("首付 (R$)", "entrada"),
            ("利率 (% 年)", "taxa"),
            ("期限 (年)", "anos")
        ],
        "financing_explain": "SAC有递减分期付款。PRICE有固定分期付款。此工具计算两者以供比较。",
        
        "rescisao": "解除计算器 (CLT)",
        "rescisao_desc": "如果被解雇，您应该收到多少。",
        "rescisao_inputs": [
            ("月薪 (R$)", "salario"),
            ("服务年限", "anos"),
            ("正当理由？", "justa_causa")
        ],
        "rescisao_explain": "计算预告期、第13个月工资、FGTS + 40%罚款、按比例休假和余额。",
        
        "independencia": "财务独立（4%规则）",
        "independencia_desc": "您需要节省多少才能永远不再工作。",
        "independencia_inputs": [
            ("月支出 (R$)", "gasto"),
            ("预期年回报率 (%)", "retorno")
        ],
        "independencia_explain": "4%规则规定您可以每年提取资产的4%而不会破产风险。",
        
        "satoshi": "聪到雷亚尔转换器",
        "satoshi_desc": "将聪（比特币最小单位）转换为雷亚尔。",
        "satoshi_inputs": [
            ("聪数量", "satoshi"),
            ("比特币价格 (R$)", "preco_btc")
        ],
        "satoshi_explain": "1比特币 = 100,000,000聪。此工具将小额转换为雷亚尔。",
        
        "orcamento": "预算模拟器 (50/30/20)",
        "orcamento_desc": "明智地分配您的收入：50%需求、30%欲望、20%储蓄。",
        "orcamento_inputs": [
            ("月收入 (R$)", "renda")
        ],
        "orcamento_explain": "50/30/20规则是一种简单的预算方法，用于保持财务控制。"
    },
    "ru": {
        "header_title": "ГРАНА СЕГОДНЯ",
        "blog": "Блог",
        "result": "Ожидаемый результат:",
        "calculate": "Рассчитать сейчас",
        "how_works": "Как работает этот инструмент?",
        "financing": "Симулятор ипотечного финансирования",
        "financing_desc": "Сравните SAC и PRICE и выберите лучший вариант для вас.",
        "financing_inputs": [
            ("Стоимость имущества (R$)", "imovel"),
            ("Первоначальный взнос (R$)", "entrada"),
            ("Процентная ставка (% годовых)", "taxa"),
            ("Срок (лет)", "anos")
        ],
        "financing_explain": "SAC имеет убывающие платежи. PRICE имеет фиксированные платежи. Этот инструмент рассчитывает оба варианта для сравнения.",
        
        "rescisao": "Калькулятор расторжения (CLT)",
        "rescisao_desc": "Узнайте, сколько вы должны получить при увольнении.",
        "rescisao_inputs": [
            ("Ежемесячная зарплата (R$)", "salario"),
            ("Стаж работы", "anos"),
            ("Уважительная причина?", "justa_causa")
        ],
        "rescisao_explain": "Рассчитывает уведомление, 13-й месячный оклад, FGTS + штраф 40%, пропорциональный отпуск и остаток.",
        
        "independencia": "Финансовая независимость (правило 4%)",
        "independencia_desc": "Сколько вам нужно накопить, чтобы больше никогда не работать.",
        "independencia_inputs": [
            ("Ежемесячные расходы (R$)", "gasto"),
            ("Ожидаемая годовая доходность (%)", "retorno")
        ],
        "independencia_explain": "Правило 4% гласит, что вы можете ежегодно снимать 4% своих активов без риска банкротства.",
        
        "satoshi": "Конвертер Сатоши в реал",
        "satoshi_desc": "Конвертируйте Сатоши (наименьшую единицу биткойна) в реалы.",
        "satoshi_inputs": [
            ("Количество Сатоши", "satoshi"),
            ("Цена биткойна (R$)", "preco_btc")
        ],
        "satoshi_explain": "1 биткойн = 100 000 000 Сатоши. Этот инструмент конвертирует небольшие суммы в реалы.",
        
        "orcamento": "Симулятор бюджета (50/30/20)",
        "orcamento_desc": "Распределите свой доход разумно: 50% потребности, 30% желания, 20% сбережения.",
        "orcamento_inputs": [
            ("Ежемесячный доход (R$)", "renda")
        ],
        "orcamento_explain": "Правило 50/30/20 - это простой метод составления бюджета для сохранения финансового контроля."
    },
    "hi": {
        "header_title": "आज ग्राना",
        "blog": "ब्लॉग",
        "result": "अनुमानित परिणाम:",
        "calculate": "अभी गणना करें",
        "how_works": "यह उपकरण कैसे काम करता है?",
        "financing": "रियल एस्टेट वित्तपोषण सिम्युलेटर",
        "financing_desc": "SAC बनाम PRICE की तुलना करें और देखें कि आपके लिए कौन सा बेहतर है।",
        "financing_inputs": [
            ("संपत्ति मूल्य (R$)", "imovel"),
            ("डाउन पेमेंट (R$)", "entrada"),
            ("ब्याज दर (% प्रति वर्ष)", "taxa"),
            ("अवधि (वर्ष)", "anos")
        ],
        "financing_explain": "SAC में घटती किस्तें हैं। PRICE में निश्चित किस्तें हैं। यह उपकरण तुलना के लिए दोनों की गणना करता है।",
        
        "rescisao": "समाप्ति कैलकुलेटर (CLT)",
        "rescisao_desc": "पता करें कि यदि आप बर्खास्त हों तो आपको कितना मिलना चाहिए।",
        "rescisao_inputs": [
            ("मासिक वेतन (R$)", "salario"),
            ("सेवा के वर्ष", "anos"),
            ("न्यायसंगत कारण?", "justa_causa")
        ],
        "rescisao_explain": "नोटिस अवधि, आनुपातिक 13वां वेतन, FGTS + 40% जुर्माना, आनुपातिक छुट्टी और शेष की गणना करता है।",
        
        "independencia": "वित्तीय स्वतंत्रता (4% नियम)",
        "independencia_desc": "आपको कभी फिर से काम न करने के लिए कितना बचाना होगा।",
        "independencia_inputs": [
            ("मासिक व्यय (R$)", "gasto"),
            ("अपेक्षित वार्षिक रिटर्न (%)", "retorno")
        ],
        "independencia_explain": "4% नियम कहता है कि आप दिवालिएपन के जोखिम के बिना अपनी संपत्ति का 4% वार्षिक निकाल सकते हैं।",
        
        "satoshi": "सातोशी से रीयल कनवर्टर",
        "satoshi_desc": "सातोशी (बिटकॉइन की सबसे छोटी इकाई) को रीयल में परिवर्तित करें।",
        "satoshi_inputs": [
            ("सातोशी की मात्रा", "satoshi"),
            ("बिटकॉइन की कीमत (R$)", "preco_btc")
        ],
        "satoshi_explain": "1 बिटकॉइन = 100,000,000 सातोशी। यह उपकरण छोटी मात्रा को रीयल में परिवर्तित करता है।",
        
        "orcamento": "बजट सिम्युलेटर (50/30/20)",
        "orcamento_desc": "अपनी आय को बुद्धिमानी से वितरित करें: 50% जरूरतें, 30% चाहतें, 20% बचत।",
        "orcamento_inputs": [
            ("मासिक आय (R$)", "renda")
        ],
        "orcamento_explain": "50/30/20 नियम वित्तीय नियंत्रण बनाए रखने के लिए बजट का एक सरल तरीका है।"
    },
    "ja": {
        "header_title": "グラナ・トゥデイ",
        "blog": "ブログ",
        "result": "推定結果:",
        "calculate": "今すぐ計算",
        "how_works": "このツールはどのように機能しますか？",
        "financing": "不動産融資シミュレーター",
        "financing_desc": "SACとPRICEを比較して、どちらがあなたに最適かを確認してください。",
        "financing_inputs": [
            ("物件価値 (R$)", "imovel"),
            ("頭金 (R$)", "entrada"),
            ("金利 (% 年)", "taxa"),
            ("期間 (年)", "anos")
        ],
        "financing_explain": "SACは減少する分割払いです。PRICEは固定分割払いです。このツールは両方を計算して比較します。",
        
        "rescisao": "解除計算機 (CLT)",
        "rescisao_desc": "解雇された場合に受け取るべき金額を確認してください。",
        "rescisao_inputs": [
            ("月給 (R$)", "salario"),
            ("勤続年数", "anos"),
            ("正当な理由？", "justa_causa")
        ],
        "rescisao_explain": "予告期間、13ヶ月目の給与、FGTS + 40%罰金、按分休暇および残高を計算します。",
        
        "independencia": "経済的自由（4%ルール）",
        "independencia_desc": "二度と働かないために必要な貯蓄額を確認してください。",
        "independencia_inputs": [
            ("月間支出 (R$)", "gasto"),
            ("予想年間収益率 (%)", "retorno")
        ],
        "independencia_explain": "4%ルールは、破産のリスクなしに毎年資産の4%を引き出せることを述べています。",
        
        "satoshi": "サトシからレアルへのコンバーター",
        "satoshi_desc": "サトシ（ビットコインの最小単位）をレアルに変換します。",
        "satoshi_inputs": [
            ("サトシの量", "satoshi"),
            ("ビットコイン価格 (R$)", "preco_btc")
        ],
        "satoshi_explain": "1ビットコイン = 100,000,000サトシ。このツールは少量をレアルに変換します。",
        
        "orcamento": "予算シミュレーター (50/30/20)",
        "orcamento_desc": "収入を賢く配分します：50%必需品、30%欲望、20%貯蓄。",
        "orcamento_inputs": [
            ("月収 (R$)", "renda")
        ],
        "orcamento_explain": "50/30/20ルールは、財務管理を維持するための単純な予算方法です。"
    },
    "bn": {
        "header_title": "গ্রানা আজ",
        "blog": "ব্লগ",
        "result": "অনুমানিত ফলাফল:",
        "calculate": "এখনই গণনা করুন",
        "how_works": "এই সরঞ্জামটি কীভাবে কাজ করে?",
        "financing": "রিয়েল এস্টেট ফিনান্সিং সিমুলেটর",
        "financing_desc": "SAC বনাম PRICE তুলনা করুন এবং আপনার জন্য কোনটি সেরা তা দেখুন।",
        "financing_inputs": [
            ("সম্পত্তির মূল্য (R$)", "imovel"),
            ("ডাউন পেমেন্ট (R$)", "entrada"),
            ("সুদের হার (% বার্ষিক)", "taxa"),
            ("মেয়াদ (বছর)", "anos")
        ],
        "financing_explain": "SAC এর হ্রাসমান কিস্তি আছে। PRICE এর স্থির কিস্তি আছে। এই সরঞ্জামটি তুলনার জন্য উভয়ই গণনা করে।",
        
        "rescisao": "সমাপ্তি ক্যালকুলেটর (CLT)",
        "rescisao_desc": "আপনি যদি বরখাস্ত হন তবে আপনি কত পাবেন তা জানুন।",
        "rescisao_inputs": [
            ("মাসিক বেতন (R$)", "salario"),
            ("সেবার বছর", "anos"),
            ("ন্যায্য কারণ?", "justa_causa")
        ],
        "rescisao_explain": "নোটিস পিরিয়ড, আনুপাতিক 13তম বেতন, FGTS + 40% জরিমানা, আনুপাতিক ছুটি এবং ব্যালেন্স গণনা করে।",
        
        "independencia": "আর্থিক স্বাধীনতা (4% নিয়ম)",
        "independencia_desc": "আপনাকে কখনও আবার কাজ না করতে কত সঞ্চয় করতে হবে তা জানুন।",
        "independencia_inputs": [
            ("মাসিক খরচ (R$)", "gasto"),
            ("প্রত্যাশিত বার্ষিক রিটার্ন (%)", "retorno")
        ],
        "independencia_explain": "4% নিয়ম বলে যে আপনি দেউলিয়া ঝুঁকি ছাড়াই বার্ষিক আপনার সম্পদের 4% উত্তোলন করতে পারেন।",
        
        "satoshi": "সাতোশি থেকে রিয়েল কনভার্টার",
        "satoshi_desc": "সাতোশি (বিটকয়েনের ক্ষুদ্রতম ইউনিট) কে রিয়েলে রূপান্তরিত করুন।",
        "satoshi_inputs": [
            ("সাতোশির পরিমাণ", "satoshi"),
            ("বিটকয়েনের মূল্য (R$)", "preco_btc")
        ],
        "satoshi_explain": "1 বিটকয়েন = 100,000,000 সাতোশি। এই সরঞ্জামটি ছোট পরিমাণকে রিয়েলে রূপান্তরিত করে।",
        
        "orcamento": "বাজেট সিমুলেটর (50/30/20)",
        "orcamento_desc": "আপনার আয় বুদ্ধিমানের সাথে বিতরণ করুন: 50% প্রয়োজন, 30% চাহিদা, 20% সঞ্চয়।",
        "orcamento_inputs": [
            ("মাসিক আয় (R$)", "renda")
        ],
        "orcamento_explain": "50/30/20 নিয়ম আর্থিক নিয়ন্ত্রণ বজায় রাখার জন্য একটি সহজ বাজেটিং পদ্ধতি।"
    },
    "pt-pt": {
        "header_title": "GRANA HOJE",
        "blog": "Blogue",
        "result": "Resultado Estimado:",
        "calculate": "Calcular Agora",
        "how_works": "Como funciona esta ferramenta?",
        "financing": "Simulador de Financiamento Imobiliário",
        "financing_desc": "Compare SAC vs PRICE e veja qual é melhor para si.",
        "financing_inputs": [
            ("Valor do Imóvel (R$)", "imovel"),
            ("Entrada (R$)", "entrada"),
            ("Taxa de Juros (% a.a.)", "taxa"),
            ("Prazo (Anos)", "anos")
        ],
        "financing_explain": "O SAC (Sistema de Amortização Constante) tem prestações decrescentes. O PRICE tem prestações fixas. Esta ferramenta calcula ambos para si comparar.",
        
        "rescisao": "Calculadora de Rescisão (CLT)",
        "rescisao_desc": "Saiba quanto deve receber se for despedido.",
        "rescisao_inputs": [
            ("Salário Mensal (R$)", "salario"),
            ("Tempo de Serviço (Anos)", "anos"),
            ("Tem Justa Causa?", "justa_causa")
        ],
        "rescisao_explain": "Calcula aviso prévio, 13º proporcional, FGTS + multa de 40%, férias proporcionais e saldo de salário.",
        
        "independencia": "Independência Financeira (Regra 4%)",
        "independencia_desc": "Quanto precisa poupar para nunca mais trabalhar.",
        "independencia_inputs": [
            ("Gasto Mensal (R$)", "gasto"),
            ("Retorno Anual Esperado (%)", "retorno")
        ],
        "independencia_explain": "A Regra dos 4% diz que pode sacar 4% do seu património anualmente sem risco de insolvência.",
        
        "satoshi": "Conversor Satoshi para Real",
        "satoshi_desc": "Converta Satoshis (menor unidade do Bitcoin) para reais.",
        "satoshi_inputs": [
            ("Quantidade de Satoshis", "satoshi"),
            ("Preço do Bitcoin (R$)", "preco_btc")
        ],
        "satoshi_explain": "1 Bitcoin = 100.000.000 Satoshis. Esta ferramenta converte pequenas quantidades para reais.",
        
        "orcamento": "Simulador de Orçamento (50/30/20)",
        "orcamento_desc": "Distribua o seu rendimento de forma inteligente: 50% necessidades, 30% desejos, 20% poupança.",
        "orcamento_inputs": [
            ("Rendimento Mensal (R$)", "renda")
        ],
        "orcamento_explain": "A regra 50/30/20 é um método simples de orçamento que ajuda a manter o controlo financeiro."
    }
}

print(json.dumps(translations, ensure_ascii=False, indent=2))
print(f"\nTotal de idiomas: {len(translations)}")
