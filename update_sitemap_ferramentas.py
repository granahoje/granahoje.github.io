import os

TOOLS = [
    "salary-split-calculator",
    "emergency-fund-tracker",
    "daily-expense-analyzer",
    "inflation-impact-calculator",
    "debt-payoff-strategy",
    "subscription-cost-tracker",
    "side-hustle-profit-calculator",
    "savings-challenge-generator",
    "investment-goal-simulator",
    "cost-of-living-comparison"
]

LANGUAGES = ["en", "es", "fr", "de", "it", "ja", "ko", "zh", "ru", "ar"]

path = "ferramentas/sitemap-ferramentas.xml"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

new_urls = ""
for tool in TOOLS:
    # URL principal (PT)
    new_urls += f'''
<url>
<loc>https://granahoje.github.io/ferramentas/{tool}/</loc>
<changefreq>weekly</changefreq>
<priority>0.8</priority>
</url>'''
    # URLs em outros idiomas
    for lang in LANGUAGES:
        new_urls += f'''
<url>
<loc>https://granahoje.github.io/ferramentas/lang/{lang}/{tool}/</loc>
<changefreq>weekly</changefreq>
<priority>0.7</priority>
</url>'''

# Inserir antes do fechamento do urlset
content = content.replace('</urlset>', f'{new_urls}\n</urlset>')

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ sitemap-ferramentas.xml atualizado!")
