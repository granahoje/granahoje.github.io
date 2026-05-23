// Savings Challenge Generator
document.addEventListener('DOMContentLoaded', function() {
    const app = document.getElementById('savings-challenge-generator-app');
    
    app.innerHTML = `
        <div class="calculator-form">
            <h3>🎯 Gerador de Desafio de Poupança</h3>
            
            <div class="input-group">
                <label for="challenge-type">Tipo de Desafio:</label>
                <select id="challenge-type">
                    <option value="52weeks">Desafio 52 Semanas</option>
                    <option value="365days">Desafio 365 Dias</option>
                    <option value="custom">Personalizado</option>
                </select>
            </div>
            
            <div class="input-group" id="custom-goal-group" style="display:none;">
                <label for="custom-goal">Meta de Economia (R$):</label>
                <input type="number" id="custom-goal" placeholder="Ex: 5000" min="0" step="0.01">
            </div>
            
            <div class="input-group" id="custom-weeks-group" style="display:none;">
                <label for="custom-weeks">Número de Semanas:</label>
                <input type="number" id="custom-weeks" placeholder="Ex: 26" min="1" max="52">
            </div>
            
            <button onclick="generateChallenge()" class="btn-calculate">Gerar Desafio</button>
            
            <div id="result-challenge" class="result-box" style="display:none;"></div>
        </div>
    `;
    
    document.getElementById('challenge-type').addEventListener('change', function() {
        const isCustom = this.value === 'custom';
        document.getElementById('custom-goal-group').style.display = isCustom ? 'block' : 'none';
        document.getElementById('custom-weeks-group').style.display = isCustom ? 'block' : 'none';
    });
});

function generateChallenge() {
    const type = document.getElementById('challenge-type').value;
    let result = '';
    
    if (type === '52weeks') {
        const total = (52 * 53) / 2; // soma de 1 a 52
        result = `
            <h4>🎯 Desafio 52 Semanas</h4>
            <p>Na semana 1, economize R$ 1,00. Na semana 2, R$ 2,00, e assim por diante...</p>
            <p><strong>Total ao Final:</strong> ${formatCurrency(total)}</p>
            <p><strong>Última Semana:</strong> R$ 52,00</p>
            <p><em>💡 Dica: Você pode inverter e começar com R$ 52 e terminar com R$ 1!</em></p>
        `;
    } else if (type === '365days') {
        const total = (365 * 366) / 2; // soma de 1 a 365
        result = `
            <h4>🎯 Desafio 365 Dias</h4>
            <p>Dia 1: economize R$ 1,00. Dia 2: R$ 2,00, e assim por diante...</p>
            <p><strong>Total ao Final do Ano:</strong> ${formatCurrency(total)}</p>
            <p><strong>Último Dia:</strong> R$ 365,00</p>
            <p><em>⚠️ Desafio avançado! Organize-se para os últimos meses.</em></p>
        `;
    } else {
        const goal = parseFloat(document.getElementById('custom-goal').value);
        const weeks = parseInt(document.getElementById('custom-weeks').value);
        
        if (!goal || !weeks) {
            alert('Preencha a meta e número de semanas');
            return;
        }
        
        const weeklyAmount = goal / weeks;
        result = `
            <h4>🎯 Seu Desafio Personalizado</h4>
            <p><strong>Meta:</strong> ${formatCurrency(goal)}</p>
            <p><strong>Duração:</strong> ${weeks} semanas</p>
            <p><strong>Economize por Semana:</strong> ${formatCurrency(weeklyAmount)}</p>
            <p><em>👍 Mantenha a consistência e você alcançará sua meta!</em></p>
        `;
    }
    
    const resultDiv = document.getElementById('result-challenge');
    resultDiv.style.display = 'block';
    resultDiv.innerHTML = result;
}