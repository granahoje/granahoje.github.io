// Daily Expense Analyzer
let expenses = [];

document.addEventListener('DOMContentLoaded', function() {
    const app = document.getElementById('daily-expense-analyzer-app');
    
    app.innerHTML = `
        <div class="calculator-form">
            <h3>📊 Analisador de Gastos Diários</h3>
            
            <div class="input-group">
                <label for="expense-desc">Descrição do Gasto:</label>
                <input type="text" id="expense-desc" placeholder="Ex: Almoço">
            </div>
            
            <div class="input-group">
                <label for="expense-amount">Valor (R$):</label>
                <input type="number" id="expense-amount" placeholder="Ex: 25.00" min="0" step="0.01">
            </div>
            
            <div class="input-group">
                <label for="expense-category">Categoria:</label>
                <select id="expense-category">
                    <option value="Alimentação">🍔 Alimentação</option>
                    <option value="Transporte">🚗 Transporte</option>
                    <option value="Lazer">🎮 Lazer</option>
                    <option value="Saúde">💊 Saúde</option>
                    <option value="Moradia">🏠 Moradia</option>
                    <option value="Outros">📦 Outros</option>
                </select>
            </div>
            
            <button onclick="addExpense()" class="btn-calculate">Adicionar Gasto</button>
            <button onclick="analyzeExpenses()" class="btn-secondary">Analisar</button>
            <button onclick="clearExpenses()" class="btn-danger">Limpar Tudo</button>
            
            <div id="expenses-list" style="margin-top: 20px;"></div>
            <div id="result-analysis" class="result-box" style="display:none;"></div>
        </div>
    `;
});

function addExpense() {
    const desc = document.getElementById('expense-desc').value;
    const amount = parseFloat(document.getElementById('expense-amount').value);
    const category = document.getElementById('expense-category').value;
    
    if (!desc || !amount || amount <= 0) {
        alert('Por favor, preencha todos os campos');
        return;
    }
    
    expenses.push({ desc, amount, category });
    
    document.getElementById('expense-desc').value = '';
    document.getElementById('expense-amount').value = '';
    
    updateExpensesList();
}

function updateExpensesList() {
    const listDiv = document.getElementById('expenses-list');
    if (expenses.length === 0) {
        listDiv.innerHTML = '<p>Nenhum gasto adicionado ainda.</p>';
        return;
    }
    
    listDiv.innerHTML = '<h4>Gastos Adicionados:</h4>' + expenses.map((exp, idx) => `
        <div class="expense-item">
            ${exp.desc} - ${formatCurrency(exp.amount)} (${exp.category})
            <button onclick="removeExpense(${idx})" style="margin-left: 10px; font-size: 12px;">❌</button>
        </div>
    `).join('');
}

function removeExpense(idx) {
    expenses.splice(idx, 1);
    updateExpensesList();
}

function analyzeExpenses() {
    if (expenses.length === 0) {
        alert('Adicione pelo menos um gasto primeiro');
        return;
    }
    
    const total = expenses.reduce((sum, exp) => sum + exp.amount, 0);
    const byCategory = {};
    
    expenses.forEach(exp => {
        byCategory[exp.category] = (byCategory[exp.category] || 0) + exp.amount;
    });
    
    const resultDiv = document.getElementById('result-analysis');
    resultDiv.style.display = 'block';
    resultDiv.innerHTML = `
        <h4>📈 Análise dos Seus Gastos</h4>
        <p><strong>Total Gasto:</strong> ${formatCurrency(total)}</p>
        <p><strong>Número de Gastos:</strong> ${expenses.length}</p>
        <p><strong>Gasto Médio:</strong> ${formatCurrency(total / expenses.length)}</p>
        <h5>Por Categoria:</h5>
        ${Object.entries(byCategory).map(([cat, val]) => `
            <p>${cat}: ${formatCurrency(val)} (${((val/total)*100).toFixed(1)}%)</p>
        `).join('')}
    `;
}

function clearExpenses() {
    if (confirm('Deseja limpar todos os gastos?')) {
        expenses = [];
        updateExpensesList();
        document.getElementById('result-analysis').style.display = 'none';
    }
}