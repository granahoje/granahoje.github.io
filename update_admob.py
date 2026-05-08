import os

publisher_id = "ca-pub-4896859041377751"
ad_script = f'<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={publisher_id}" crossorigin="anonymous"></script>'
meta_tag = f'<meta name="google-adsense-account" content="{publisher_id}">'

def update_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already updated
    if publisher_id in content:
        print(f"Skipping {file_path}, already updated.")
        return

    # Insert ad script before gtag
    if 'src="https://www.googletagmanager.com/gtag/js' in content:
        content = content.replace(
            '<script async src="https://www.googletagmanager.com/gtag/js',
            f'{ad_script}\n    <script async src="https://www.googletagmanager.com/gtag/js'
        )
    
    # Insert meta tag before Meta Tags Essenciais
    if '<!-- Meta Tags Essenciais -->' in content:
        content = content.replace(
            '<!-- Meta Tags Essenciais -->',
            f'<!-- Google AdMob App ID -->\n    {meta_tag}\n    \n    <!-- Meta Tags Essenciais -->'
        )
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {file_path}")

# Walk through directories
for root, dirs, files in os.walk('.'):
    for file in files:
        if file == "index.html":
            update_html(os.path.join(root, file))
