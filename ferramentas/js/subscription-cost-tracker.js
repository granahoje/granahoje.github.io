// Subscription Cost Tracker
let subscriptions = [];

document.addEventListener('DOMContentLoaded', function() {
    const app = document.getElementById('subscription-cost-tracker-app');
    
    app.innerHTML = `
        <div class="calculator-form">
            <h3>📱 Rastreador de Assinaturas</h3>
            
            <div class="input-group">
                <label for="sub-name">Nome da Assinatura:</label>
                <input type="text" id="sub-name" placeholder="Ex: Netflix">
            </div>
            
            <div class="input-group">
                <label for="sub-cost">Custo Mensal (R$):</label>
                <input type="number" id="sub-cost" placeholder="Ex: 39.90" min="0" step="0.01">
            </div>
            
            <button onclick="addSubscription()" class="btn-calculate">Adicionar Assinatura</button>
            <button onclick="analyzeSubs()" class="btn-secondary">Analisar Gastos</button>
            <button onclick="clearSubs()" class="btn-danger">Limpar Todas</button>
            
            <div id="subs-list" style="margin-top: 20px;"></div>
            <div id="result-subs" class="result-box" style="display:none;"></div>
        </div>
    `;
});

function addSubscription() {
    const name = document.getElementById('sub-name').value;
    const cost = parseFloat(document.getElementById('sub-cost').value);
    
    if (!name || !cost || cost <= 0) {
        alert('Por favor, preencha todos os campos');
        return;
    }
    
    subscriptions.push({ name, cost });
    
    document.getElementById('sub-name').value = '';
    document.getElementById('sub-cost').value = '';
    
    updateSubsList();
}

function updateSubsList() {
    const listDiv = document.getElementById('subs-list');
    if (subscriptions.length === 0) {
        listDiv.innerHTML = '<p>Nenhuma assinatura adicionada.</p>';
        return;
    }
    
    listDiv.innerHTML = '<h4>Suas Assinaturas:</h4>' + subscriptions.map((sub, idx) => `
        <div class="expense-item">
            ${sub.name} - ${formatCurrency(sub.cost)}/mês
            <button onclick="removeSub(${idx})" style="margin-left: 10px; font-size: 12px;">❌</button>
        </div>
    `).join('');
}

function removeSub(idx) {
    subscriptions.splice(idx, 1);
    updateSubsList();
}

function analyzeSubs() {
    if (subscriptions.length === 0) {
        alert('Adicione pelo menos uma assinatura primeiro');
        return;
    }
    
    const monthlyTotal = subscriptions.reduce((sum, sub) => sum + sub.cost, 0);
    const yearlyTotal = monthlyTotal * 12;
    const potentialSavings = yearlyTotal * 0.40; // 40% de economia
    
    const resultDiv = document.getElementById('result-subs');
    resultDiv.style.display = 'block';
    resultDiv.innerHTML = `
        <h4>📊 Análise de Assinaturas</h4>
        <p><strong>Total Mensal:</strong> ${formatCurrency(monthlyTotal)}</p>
        <p><strong>Total Anual:</strong> ${formatCurrency(yearlyTotal)}</p>
        <p><strong>Número de Assinaturas:</strong> ${subscriptions.length}</p>
        <p><strong>Custo Médio:</strong> ${formatCurrency(monthlyTotal / subscriptions.length)}/assinatura</p>
        <p class="alert">💡 <strong>Dica:</strong> Cancelando assinaturas pouco usadas, você pode economizar até ${formatCurrency(potentialSavings)} por ano!</p>
    `;
}

function clearSubs() {
    if (confirm('Deseja limpar todas as assinaturas?')) {
        subscriptions = [];
        updateSubsList();
        document.getElementById('result-subs').style.display = 'none';
    }
}