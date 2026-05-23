// Emergency Fund Tracker
document.addEventListener('DOMContentLoaded', function() {
    const app = document.getElementById('emergency-fund-tracker-app');
    
    app.innerHTML = `
        <div class="calculator-form">
            <h3>🛡️ Rastreador de Reserva de Emergência</h3>
            
            <div class="input-group">
                <label for="monthly-expenses">Gastos Mensais (R$):</label>
                <input type="number" id="monthly-expenses" placeholder="Ex: 2500" min="0" step="0.01">
            </div>
            
            <div class="input-group">
                <label for="current-fund">Reserva Atual (R$):</label>
                <input type="number" id="current-fund" placeholder="Ex: 5000" min="0" step="0.01">
            </div>
            
            <div class="input-group">
                <label for="target-months">Meta de Meses:</label>
                <select id="target-months">
                    <option value="3">3 meses (mínimo)</option>
                    <option value="6" selected>6 meses (recomendado)</option>
                    <option value="12">12 meses (ideal)</option>
                </select>
            </div>
            
            <button onclick="trackEmergencyFund()" class="btn-calculate">Analisar Reserva</button>
            
            <div id="result-emergency" class="result-box" style="display:none;"></div>
        </div>
    `;
});

function trackEmergencyFund() {
    const monthlyExpenses = parseFloat(document.getElementById('monthly-expenses').value);
    const currentFund = parseFloat(document.getElementById('current-fund').value);
    const targetMonths = parseInt(document.getElementById('target-months').value);
    
    if (!monthlyExpenses || monthlyExpenses <= 0) {
        alert('Por favor, insira seus gastos mensais');
        return;
    }
    
    const targetAmount = monthlyExpenses * targetMonths;
    const remaining = targetAmount - currentFund;
    const percentComplete = (currentFund / targetAmount) * 100;
    const monthsCovered = currentFund / monthlyExpenses;
    
    const resultDiv = document.getElementById('result-emergency');
    resultDiv.style.display = 'block';
    resultDiv.innerHTML = `
        <h4>📊 Status da sua Reserva de Emergência</h4>
        <div class="progress-bar">
            <div class="progress-fill" style="width: ${Math.min(percentComplete, 100)}%"></div>
        </div>
        <p><strong>Progresso:</strong> ${percentComplete.toFixed(1)}% completo</p>
        <p><strong>Meta:</strong> ${formatCurrency(targetAmount)} (${targetMonths} meses)</p>
        <p><strong>Reserva Atual:</strong> ${formatCurrency(currentFund)}</p>
        <p><strong>Meses Cobertos:</strong> ${monthsCovered.toFixed(1)} meses</p>
        ${remaining > 0 ? `
            <p class="alert"><strong>Falta:</strong> ${formatCurrency(remaining)}</p>
        ` : `
            <p class="success">✅ Parabéns! Sua reserva está completa!</p>
        `}
    `;
}