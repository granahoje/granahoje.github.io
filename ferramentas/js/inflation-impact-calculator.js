// Inflation Impact Calculator
document.addEventListener('DOMContentLoaded', function() {
    const app = document.getElementById('inflation-impact-calculator-app');
    
    app.innerHTML = `
        <div class="calculator-form">
            <h3>📉 Calculadora de Impacto da Inflação</h3>
            
            <div class="input-group">
                <label for="initial-amount">Valor Inicial (R$):</label>
                <input type="number" id="initial-amount" placeholder="Ex: 10000" min="0" step="0.01">
            </div>
            
            <div class="input-group">
                <label for="inflation-rate">Taxa de Inflação Anual (%):</label>
                <input type="number" id="inflation-rate" placeholder="Ex: 4.5" min="0" step="0.01" value="4.5">
            </div>
            
            <div class="input-group">
                <label for="years">Período (anos):</label>
                <input type="number" id="years" placeholder="Ex: 5" min="1" max="50" value="5">
            </div>
            
            <button onclick="calculateInflationImpact()" class="btn-calculate">Calcular Impacto</button>
            
            <div id="result-inflation" class="result-box" style="display:none;"></div>
        </div>
    `;
});

function calculateInflationImpact() {
    const initialAmount = parseFloat(document.getElementById('initial-amount').value);
    const inflationRate = parseFloat(document.getElementById('inflation-rate').value) / 100;
    const years = parseInt(document.getElementById('years').value);
    
    if (!initialAmount || initialAmount <= 0 || !years || years <= 0) {
        alert('Por favor, preencha todos os campos corretamente');
        return;
    }
    
    const futureValue = initialAmount / Math.pow(1 + inflationRate, years);
    const loss = initialAmount - futureValue;
    const lossPercent = (loss / initialAmount) * 100;
    
    const resultDiv = document.getElementById('result-inflation');
    resultDiv.style.display = 'block';
    resultDiv.innerHTML = `
        <h4>📉 Impacto da Inflação no Seu Patrimônio</h4>
        <p><strong>Valor Hoje:</strong> ${formatCurrency(initialAmount)}</p>
        <p><strong>Poder de Compra em ${years} anos:</strong> ${formatCurrency(futureValue)}</p>
        <p class="alert"><strong>Perda de Valor:</strong> ${formatCurrency(loss)} (-${lossPercent.toFixed(2)}%)</p>
        <p><em>Seu dinheiro perderá ${formatPercent(lossPercent)} do seu valor em ${years} anos com inflação de ${formatPercent(inflationRate * 100)} ao ano.</em></p>
    `;
}