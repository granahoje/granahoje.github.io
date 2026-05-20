import os

IDIOMAS = ['en','es','fr','ar','zh','hi','ja','ru','pt-pt','bn','pt-br']

POSTS = {
  'mineracao-dados-mobile-etica': {
    'en': ('Mobile Data Mining 2026 - Grana Hoje','Mobile Data Mining: Ethics, Privacy and Financial Impact in 2026','Every tap on your smartphone generates valuable data.'),
    'es': ('Minería de Datos Móvil 2026 - Grana Hoje','Minería de Datos Móvil: Ética, Privacidad e Impacto Financiero en 2026','Cada toque en tu smartphone genera datos valiosos.'),
    'fr': ('Exploration Données Mobile 2026 - Grana Hoje','Exploration de Données Mobile: Éthique, Confidentialité et Impact Financier en 2026','Chaque touche sur votre smartphone génère des données précieuses.'),
    'ar': ('تعدين البيانات المحمول 2026 - Grana Hoje','تعدين البيانات عبر الهاتف المحمول: الأخلاقيات والخصوصية والتأثير المالي في 2026','كل نقرة على شاشة هاتفك الذكي تولد بيانات قيمة.'),
    'zh': ('移动数据挖掘 2026 - Grana Hoje','移动数据挖掘：2026年伦理、隐私与财务影响','您智能手机上的每一次点击都会产生有价值的数据。'),
    'hi': ('मोबाइल डेटा माइनिंग 2026 - Grana Hoje','मोबाइल डेटा माइनिंग: 2026 में नैतिकता, गोपनीयता और वित्तीय प्रभाव','आपके स्मार्टफोन पर हर टच मूल्यवान डेटा उत्पन्न करता है।'),
    'ja': ('モバイルデータマイニング 2026 - Grana Hoje','モバイルデータマイニング：2026年の倫理、プライバシーと財務への影響','スマートフォンの画面をタップするたびに貴重なデータが生成されます。'),
    'ru': ('Мобильный майнинг данных 2026 - Grana Hoje','Мобильный майнинг данных: этика, конфиденциальность и финансовое влияние в 2026 году','Каждое касание экрана вашего смартфона генерирует ценные данные.'),
    'pt-pt': ('Mineração de Dados Mobile 2026 - Grana Hoje','Mineração de Dados Mobile: Ética, Privacidade e Impacto nas Suas Finanças em 2026','Cada toque no ecrã do seu smartphone gera dados valiosos.'),
    'bn': ('মোবাইল ডেটা মাইনিং 2026 - Grana Hoje','মোবাইল ডেটা মাইনিং: ২০২৬ সালে নৈতিকতা, গোপনীয়তা এবং আর্থিক প্রভাব','আপনার স্মার্টফোনের প্রতিটি স্পর্শ মূল্যবান ডেটা তৈরি করে।'),
    'pt-br': ('Mineração de Dados Mobile 2026 - Grana Hoje','Mineração de Dados Mobile: Ética, Privacidade e Impacto nas Suas Finanças em 2026','Cada toque na tela do seu smartphone gera dados valiosos.'),
  },
  'venda-digital-assets-ia': {
    'en': ('Selling Digital Assets with AI 2026 - Grana Hoje','Selling Digital Assets with AI: Build a Passive Income Machine in 2026','AI-powered digital assets represent one of the greatest income opportunities of our era.'),
    'es': ('Venta de Activos Digitales con IA 2026 - Grana Hoje','Venta de Activos Digitales con IA: Crea una Máquina de Ingresos Pasivos en 2026','Los activos digitales con IA representan una de las mayores oportunidades de ingresos de nuestra era.'),
    'fr': ('Vente Actifs Numériques IA 2026 - Grana Hoje','Vente d Actifs Numériques avec IA: Créez une Machine à Revenus Passifs en 2026','Les actifs numériques avec IA représentent une des plus grandes opportunités de revenus de notre époque.'),
    'ar': ('بيع الأصول الرقمية بالذكاء الاصطناعي 2026 - Grana Hoje','بيع الأصول الرقمية بالذكاء الاصطناعي: أنشئ آلة دخل سلبي في 2026','الأصول الرقمية بالذكاء الاصطناعي تمثل واحدة من أكبر فرص توليد الدخل في عصرنا.'),
    'zh': ('用AI销售数字资产 2026 - Grana Hoje','用AI销售数字资产：在2026年创建被动收入机器','AI驱动的数字资产代表了我们时代最大的收入机会之一。'),
    'hi': ('AI से डिजिटल एसेट्स बेचना 2026 - Grana Hoje','AI के साथ डिजिटल एसेट्स बेचना: 2026 में पैसिव इनकम मशीन बनाएं','AI-संचालित डिजिटल एसेट्स हमारे युग के सबसे बड़े आय अवसरों में से एक हैं।'),
    'ja': ('AIでデジタルアセット販売 2026 - Grana Hoje','AIでデジタルアセットを販売する：2026年に不労所得マシンを構築する','AIを活用したデジタルアセットは私たちの時代で最大の収入機会の一つです。'),
    'ru': ('Продажа цифровых активов с ИИ 2026 - Grana Hoje','Продажа цифровых активов с ИИ: создайте машину пассивного дохода в 2026 году','Цифровые активы с ИИ представляют одну из величайших возможностей получения дохода нашей эпохи.'),
    'pt-pt': ('Venda de Ativos Digitais com IA 2026 - Grana Hoje','Venda de Ativos Digitais com IA: Crie uma Máquina de Rendimento Passivo em 2026','Os ativos digitais com IA representam uma das maiores oportunidades de rendimento da nossa época.'),
    'bn': ('AI দিয়ে ডিজিটাল অ্যাসেট বিক্রি 2026 - Grana Hoje','AI দিয়ে ডিজিটাল অ্যাসেট বিক্রি: ২০২৬ সালে প্যাসিভ ইনকাম মেশিন তৈরি করুন','AI-চালিত ডিজিটাল অ্যাসেট আমাদের যুগের সবচেয়ে বড় আয়ের সুযোগগুলির মধ্যে একটি।'),
    'pt-br': ('Venda de Digital Assets com IA 2026 - Grana Hoje','Venda de Digital Assets com IA: Crie uma Máquina de Renda Passiva em 2026','A venda de digital assets com IA representa uma das maiores oportunidades de geração de renda da nossa era.'),
  }
}

for slug, idiomas in POSTS.items():
  for lang, (title, h1, intro) in idiomas.items():
    os.makedirs(lang, exist_ok=True)
    path = f'{lang}/{slug}.html'
    html = f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>
body{{font-family:sans-serif;max-width:800px;margin:2rem auto;padding:0 1rem;color:#333}}
h1{{color:#16213e;border-bottom:3px solid #e94560;padding-bottom:.5rem}}
.intro{{background:#f8f9fa;border-left:4px solid #e94560;padding:1rem;margin:1rem 0}}
footer{{margin-top:3rem;padding-top:1rem;border-top:1px solid #eee;color:#888;font-size:.85rem}}
a{{color:#e94560}}
</style>
</head>
<body>
<p><a href="https://granahoje.github.io/">← Grana Hoje</a></p>
<h1>{h1}</h1>
<div class="intro"><p>{intro}</p></div>
<p>Continue reading at <a href="https://granahoje.github.io/artigos/{slug}.html">Grana Hoje</a>.</p>
<footer>© 2026 Grana Hoje</footer>
</body>
</html>'''
    with open(path, 'w', encoding='utf-8') as f:
      f.write(html)
    print(f'OK: {path}')

print('Concluido!')
