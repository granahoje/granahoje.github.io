// Investment Goal Simulator
document.addEventListener('DOMContentLoaded', function() {
    const app = document.getElementById('investment-goal-simulator-app');
    
    app.innerHTML = `
        <div class="calculator-form">
            <h3>💎 Simulador de Meta de Investimento</h3>
            
            <div class="input-group">
                <label for="goal-amount">Meta Financeira (R$):</label>
                <input type="number" id="goal-amount" placeholder="Ex: 100000" min="0" step="0.01">
            </div>
            
            <div class="input-group">
                <label for="initial-investment">Investimento Inicial (R$):</label>
                <input type="number" id="initial-investment" placeholder="Ex: 5000" min="0" step="0.01" value="0">
            </div>
            
            <div class="input-group">
                <label for="monthly-contribution">Aporte Mensal (R$):</label>
                <input type="number" id="monthly-contribution" placeholder="Ex: 500" min="0" step="0.01">
            </div>
            
            <div class="input-group">
                <label for="return-rate">Taxa de Retorno Anual (%):</label>
                <input type="number" id="return-rate" placeholder="Ex: 10" min="0" max="100" step="0.1" value="10">
            </div>
            
            <div class="input-group">
                <label for="time-horizon">Prazo:</label>
                <select id="time-horizon">
                    <option value="short">Curto Prazo (1-3 anos)</option>
                    <option value="medium">Médio Prazo (3-10 anos)</option>
                    <option value="long">Longo Prazo (10+ anos)</option>
                </select>
            </div>
            
            <button onclick="simulateInvestmentGoal()" class="btn-calculate">Simular Meta</button>
            
            <div id="result-investment" class="result-box" style="display:none;"></div>
        </div>
    `;
});

function simulateInvestmentGoal() {
    const goalAmount = parseFloat(document.getElementById('goal-amount').value);
    const initialInvestment = parseFloat(document.getElementById('initial-investment').value) || 0;
    const monthlyContribution = parseFloat(document.getElementById('monthly-contribution').value);
    const annualReturn = parseFloat(document.getElementById('return-rate').value) / 100;
    const timeHorizon = document.getElementById('time-horizon').value;
    
    if (!goalAmount || goalAmount <= 0 || !monthlyContribution || monthlyContribution <= 0) {
        alert('Por favor, preencha a meta e o aporte mensal');
        return;
    }
    
    const monthlyReturn = annualReturn / 12;
    let balance = initialInvestment;
    let months = 0;
    const maxMonths = 600; // 50 anos
    
    while (balance < goalAmount && months < maxMonths) {
        balance = balance * (1 + monthlyReturn) + monthlyContribution;
        months++;
    }
    
    const years = Math.floor(months / 12);
    const remainingMonths = months % 12;
    const totalContributed = initialInvestment + (monthlyContribution * months);
    const totalInterest = balance - totalContributed;
    
    let timeAdvice = '';
    if (timeHorizon === 'short' && years > 3) {
        timeAdvice = '<p class="alert">⚠️ Sua meta é de curto prazo, mas levará mais tempo. Considere aumentar os aportes.</p>';
    } else if (timeHorizon === 'medium' && (years < 3 || years > 10)) {
        timeAdvice = '<p class="alert">💡 Ajuste seus aportes para alinhar com o prazo de médio prazo.</p>';
    }
    
    const resultDiv = document.getElementById('result-investment');
    resultDiv.style.display = 'block';
    resultDiv.innerHTML = `
        <h4>📈 Simulação da Sua Meta</h4>
        <p><strong>Meta:</strong> ${formatCurrency(goalAmount)}</p>
        <p><strong>Tempo Necessário:</strong> ${years} anos e ${remainingMonths} meses</p>
        <p><strong>Total Investido:</strong> ${formatCurrency(totalContributed)}</p>
        <p><strong>Juros Ganhos:</strong> ${formatCurrency(totalInterest)}</p>
        <p><strong>Valor Final:</strong> ${formatCurrency(balance)}</p>
        ${timeAdvice}
        <p><em>🎯 Mantenha a disciplina e sua meta será alcançada!</em></p>
    `;
}