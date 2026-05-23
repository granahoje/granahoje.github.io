// Side Hustle Profit Calculator
document.addEventListener('DOMContentLoaded', function() {
    const app = document.getElementById('side-hustle-profit-calculator-app');
    
    app.innerHTML = `
        <div class="calculator-form">
            <h3>🚀 Calculadora de Lucro de Freela/Bico</h3>
            
            <div class="input-group">
                <label for="revenue">Receita Mensal (R$):</label>
                <input type="number" id="revenue" placeholder="Ex: 1500" min="0" step="0.01">
            </div>
            
            <div class="input-group">
                <label for="costs">Custos Mensais (R$):</label>
                <input type="number" id="costs" placeholder="Ex: 300" min="0" step="0.01">
            </div>
            
            <div class="input-group">
                <label for="hours">Horas Trabalhadas/Mês:</label>
                <input type="number" id="hours" placeholder="Ex: 40" min="0" step="1">
            </div>
            
            <div class="input-group">
                <label for="tax-rate">Impostos (%):</label>
                <input type="number" id="tax-rate" placeholder="Ex: 6" min="0" max="100" step="0.1" value="6">
            </div>
            
            <button onclick="calculateSideHustleProfit()" class="btn-calculate">Calcular Lucro Real</button>
            
            <div id="result-hustle" class="result-box" style="display:none;"></div>
        </div>
    `;
});

function calculateSideHustleProfit() {
    const revenue = parseFloat(document.getElementById('revenue').value);
    const costs = parseFloat(document.getElementById('costs').value);
    const hours = parseFloat(document.getElementById('hours').value);
    const taxRate = parseFloat(document.getElementById('tax-rate').value) / 100;
    
    if (!revenue || revenue <= 0 || !hours || hours <= 0) {
        alert('Por favor, preencha pelo menos receita e horas trabalhadas');
        return;
    }
    
    const taxes = revenue * taxRate;
    const netProfit = revenue - costs - taxes;
    const hourlyRate = netProfit / hours;
    const profitMargin = (netProfit / revenue) * 100;
    
    const resultDiv = document.getElementById('result-hustle');
    resultDiv.style.display = 'block';
    resultDiv.innerHTML = `
        <h4>💰 Seu Lucro Real</h4>
        <p><strong>Receita Mensal:</strong> ${formatCurrency(revenue)}</p>
        <p><strong>Custos:</strong> -${formatCurrency(costs)}</p>
        <p><strong>Impostos (${formatPercent(taxRate * 100)}):</strong> -${formatCurrency(taxes)}</p>
        <p class="success"><strong>Lucro Líquido:</strong> ${formatCurrency(netProfit)}</p>
        <p><strong>Valor/Hora:</strong> ${formatCurrency(hourlyRate)}</p>
        <p><strong>Margem de Lucro:</strong> ${profitMargin.toFixed(1)}%</p>
        ${netProfit < 0 ? '<p class="alert">⚠️ Você está tendo prejuízo! Revise seus custos.</p>' : ''}
    `;
}