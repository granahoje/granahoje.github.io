// Debt Payoff Strategy
document.addEventListener('DOMContentLoaded', function() {
    const app = document.getElementById('debt-payoff-strategy-app');
    
    app.innerHTML = `
        <div class="calculator-form">
            <h3>💸 Estratégia de Quitação de Dívidas</h3>
            
            <div class="input-group">
                <label for="debt1-name">Dívida 1:</label>
                <input type="text" id="debt1-name" placeholder="Ex: Cartão de Crédito" value="Cartão de Crédito">
            </div>
            <div class="input-group">
                <label>Saldo (R$):</label>
                <input type="number" id="debt1-balance" placeholder="1500" min="0" step="0.01">
            </div>
            <div class="input-group">
                <label>Taxa de Juros Mensal (%):</label>
                <input type="number" id="debt1-rate" placeholder="3.5" min="0" step="0.01">
            </div>
            
            <div class="input-group">
                <label for="debt2-name">Dívida 2:</label>
                <input type="text" id="debt2-name" placeholder="Ex: Empréstimo Pessoal" value="Empréstimo">
            </div>
            <div class="input-group">
                <label>Saldo (R$):</label>
                <input type="number" id="debt2-balance" placeholder="5000" min="0" step="0.01">
            </div>
            <div class="input-group">
                <label>Taxa de Juros Mensal (%):</label>
                <input type="number" id="debt2-rate" placeholder="2.0" min="0" step="0.01">
            </div>
            
            <div class="input-group">
                <label for="monthly-payment">Pagamento Mensal Disponível (R$):</label>
                <input type="number" id="monthly-payment" placeholder="500" min="0" step="0.01">
            </div>
            
            <button onclick="compareStrategies()" class="btn-calculate">Comparar Estratégias</button>
            
            <div id="result-debt" class="result-box" style="display:none;"></div>
        </div>
    `;
});

function compareStrategies() {
    const debt1 = {
        name: document.getElementById('debt1-name').value,
        balance: parseFloat(document.getElementById('debt1-balance').value),
        rate: parseFloat(document.getElementById('debt1-rate').value) / 100
    };
    
    const debt2 = {
        name: document.getElementById('debt2-name').value,
        balance: parseFloat(document.getElementById('debt2-balance').value),
        rate: parseFloat(document.getElementById('debt2-rate').value) / 100
    };
    
    const monthlyPayment = parseFloat(document.getElementById('monthly-payment').value);
    
    if (!debt1.balance || !debt2.balance || !monthlyPayment) {
        alert('Por favor, preencha todos os campos');
        return;
    }
    
    // Bola de Neve: menor saldo primeiro
    const snowball = debt1.balance < debt2.balance ? [debt1, debt2] : [debt2, debt1];
    
    // Avalanche: maior taxa primeiro
    const avalanche = debt1.rate > debt2.rate ? [debt1, debt2] : [debt2, debt1];
    
    const resultDiv = document.getElementById('result-debt');
    resultDiv.style.display = 'block';
    resultDiv.innerHTML = `
        <h4>🎯 Estratégias de Quitação</h4>
        
        <div class="strategy-box">
            <h5>⛄ Método Bola de Neve (Psicológico)</h5>
            <p>Prioriza a dívida menor para vitórias rápidas</p>
            <p>1º: ${snowball[0].name} - ${formatCurrency(snowball[0].balance)}</p>
            <p>2º: ${snowball[1].name} - ${formatCurrency(snowball[1].balance)}</p>
            <p><em>👍 Melhor para motivação e disciplina</em></p>
        </div>
        
        <div class="strategy-box">
            <h5>🏔️ Método Avalanche (Financeiro)</h5>
            <p>Prioriza a maior taxa de juros</p>
            <p>1º: ${avalanche[0].name} - ${formatPercent(avalanche[0].rate * 100)} juros</p>
            <p>2º: ${avalanche[1].name} - ${formatPercent(avalanche[1].rate * 100)} juros</p>
            <p><em>💰 Economiza mais dinheiro no longo prazo</em></p>
        </div>
        
        <p><strong>Total de Dívidas:</strong> ${formatCurrency(debt1.balance + debt2.balance)}</p>
        <p><strong>Pagamento Mensal:</strong> ${formatCurrency(monthlyPayment)}</p>
    `;
}