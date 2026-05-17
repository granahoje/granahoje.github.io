import os

langs = ['en', 'es', 'fr', 'ar', 'zh', 'ru', 'hi', 'ja', 'bn', 'pt-pt']

translations = {
    'en': {'privacy': 'Privacy Policy', 'terms': 'Terms of Service', 'disclaimer': 'Disclaimer', 'contact': 'Contact', 'back': 'Back to Home', 'last': 'Last updated'},
    'es': {'privacy': 'Política de Privacidad', 'terms': 'Términos de Servicio', 'disclaimer': 'Aviso Legal', 'contact': 'Contacto', 'back': 'Volver al Inicio', 'last': 'Última actualización'},
    'fr': {'privacy': 'Politique de Confidentialité', 'terms': 'Conditions d\'Utilisation', 'disclaimer': 'Avis Légal', 'contact': 'Contact', 'back': 'Retour à l\'Accueil', 'last': 'Dernière mise à jour'},
    'ar': {'privacy': 'سياسة الخصوصية', 'terms': 'شروط الخدمة', 'disclaimer': 'إخلاء المسؤولية', 'contact': 'اتصل بنا', 'back': 'العودة إلى الصفحة الرئيسية', 'last': 'آخر تحديث'},
    'zh': {'privacy': '隐私政策', 'terms': '服务条款', 'disclaimer': '免责声明', 'contact': '联系我们', 'back': '返回首页', 'last': '最后更新'},
    'ru': {'privacy': 'Политика конфиденциальности', 'terms': 'Условия использования', 'disclaimer': 'Отказ от ответственности', 'contact': 'Контакт', 'back': 'Вернуться на главную', 'last': 'Последнее обновление'},
    'hi': {'privacy': 'गोपनीयता नीति', 'terms': 'सेवा की शर्तें', 'disclaimer': 'अस्वीकरण', 'contact': 'संपर्क', 'back': 'होम पर वापस जाएं', 'last': 'अंतिम अपडेट'},
    'ja': {'privacy': 'プライバシーポリシー', 'terms': '利用規約', 'disclaimer': '免责事项', 'contact': 'お問い合わせ', 'back': 'ホームに戻る', 'last': '最終更新日'},
    'bn': {'privacy': 'গোপনীয়তা নীতি', 'terms': 'পরিষেবার শর্তাবলী', 'disclaimer': 'দায়মুক্তি', 'contact': 'যোগাযোগ', 'back': 'হোমে ফিরে যান', 'last': 'সর্বশেষ আপডেট'},
    'pt-pt': {'privacy': 'Política de Privacidade', 'terms': 'Termos de Serviço', 'disclaimer': 'Aviso Legal', 'contact': 'Contacto', 'back': 'Voltar ao Início', 'last': 'Última atualização'}
}

def create_page(lang, type_name):
    title = translations[lang][type_name]
    back_text = translations[lang]['back']
    last_text = translations[lang]['last']
    filename = f"{type_name.replace('_', '-')}.html"
    if type_name == 'privacy': filename = 'privacy-policy.html'
    if type_name == 'terms': filename = 'terms-of-service.html'
    
    content = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Grana Hoje</title>
    <link rel="stylesheet" href="/css/style.css">
    <link rel="canonical" href="https://granahoje.github.io/{lang}/{filename}">
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-706NN8PEE7"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', 'G-706NN8PEE7');
    </script>
</head>
<body>
    <div class="container">
        <a href="/{lang}/" class="back-link">← {back_text}</a>
        <h1>{title}</h1>
        <p class="last-updated">{last_text}: May 17, 2026</p>
        <p>Content for {title} in {lang} will be fully updated soon.</p>
    </div>
    <footer class="standard-footer">
        <div class="footer-container">
            <div class="footer-bottom">
                <p>&copy; 2026 Grana Hoje. All rights reserved.</p>
            </div>
        </div>
    </footer>
</body>
</html>"""
    
    with open(f"{lang}/{filename}", "w", encoding="utf-8") as f:
        f.write(content)

for lang in langs:
    if not os.path.exists(lang):
        os.makedirs(lang)
    create_page(lang, 'privacy')
    create_page(lang, 'terms')
    create_page(lang, 'disclaimer')
    create_page(lang, 'contact')
