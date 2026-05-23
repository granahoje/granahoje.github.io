import os
import re

TOOLS = [
    ("Salary Split Calculator", "salary-split-calculator", "💰"),
    ("Emergency Fund Tracker", "emergency-fund-tracker", "🛡️"),
    ("Daily Expense Analyzer", "daily-expense-analyzer", "📊"),
    ("Inflation Impact Calculator", "inflation-impact-calculator", "📈"),
    ("Debt Payoff Strategy", "debt-payoff-strategy", "💸"),
    ("Subscription Cost Tracker", "subscription-cost-tracker", "📱"),
    ("Side Hustle Profit Calculator", "side-hustle-profit-calculator", "🚀"),
    ("Savings Challenge Generator", "savings-challenge-generator", "🎯"),
    ("Investment Goal Simulator", "investment-goal-simulator", "💎"),
    ("Cost of Living Comparison", "cost-of-living-comparison", "🌍")
]

path = "ferramentas.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Gerar cards
new_cards = ""
for title, folder, icon in TOOLS:
    new_cards += f'''
<a class="tool-card" href="/ferramentas/{folder}/">
    <div class="tool-icon">{icon}</div>
    <h3>{title}</h3>
    <p>Ferramenta premium para gestão financeira inteligente.</p>
    <span class="tool-link">Acessar Grátis →</span>
</a>'''

# Inserir no grid (procurando pelo final do grid ou um marcador)
if '<div class="tools-grid">' in content:
    content = content.replace('<div class="tools-grid">', f'<div class="tools-grid">{new_cards}')

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ ferramentas.html atualizado com as novas ferramentas premium!")
