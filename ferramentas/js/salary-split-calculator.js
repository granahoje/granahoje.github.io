// Salary Split Calculator
document.addEventListener('DOMContentLoaded', function() {
    const app = document.getElementById('salary-split-calculator-app');
    
    app.innerHTML = `
        <div class="calculator-form">
            <h3>💰 Divisão Estratégica do Salário (Regra 50/30/20)</h3>
            
            <div class="input-group">
                <label for="salary">Seu Salário Mensal (R$):</label>
                <input type="number" id="salary" placeholder="Ex: 3000" min="0" step="0.01">
            </div>
            
            <button onclick="calculateSalarySplit()" class="btn-calculate">Calcular Divisão</button>
            
            <div id="result-split" class="result-box" style="display:none;"></div>
        </div>
    `;
});

function calculateSalarySplit() {
    const salary = parseFloat(document.getElementById('salary').value);
    
    if (!salary || salary <= 0) {
        alert('Por favor, insira um salário válido');
        return;
    }
    
    const necessities = salary * 0.50; // 50% Necessidades
    const wants = salary * 0.30; // 30% Desejos
    const savings = salary * 0.20; // 20% Investimentos
    
    const resultDiv = document.getElementById('result-split');
    resultDiv.style.display = 'block';
    resultDiv.innerHTML = `
        <h4>📊 Sua Divisão Ideal:</h4>
        <div class="split-item">
            <strong>🏠 Necessidades (50%):</strong> ${formatCurrency(necessities)}<br>
            <small>Aluguel, contas, alimentação, transporte</small>
        </div>
        <div class="split-item">
            <strong>🎯 Desejos (30%):</strong> ${formatCurrency(wants)}<br>
            <small>Lazer, hobbies, streaming, restaurantes</small>
        </div>
        <div class="split-item">
            <strong>💎 Investimentos (20%):</strong> ${formatCurrency(savings)}<br>
            <small>Poupança, investimentos, reserva de emergência</small>
        </div>
        <div class="total-split">
            <strong>Total:</strong> ${formatCurrency(salary)}
        </div>
    `;
}