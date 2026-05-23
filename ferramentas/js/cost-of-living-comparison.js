// Cost of Living Comparison
document.addEventListener('DOMContentLoaded', function() {
    const app = document.getElementById('cost-of-living-comparison-app');
    
    // Dados aproximados de custo de vida em grandes cidades brasileiras
    const cities = {
        'São Paulo': { rent: 2500, food: 800, transport: 450, total: 3750 },
        'Rio de Janeiro': { rent: 2200, food: 750, transport: 400, total: 3350 },
        'Brasília': { rent: 2000, food: 700, transport: 350, total: 3050 },
        'Belo Horizonte': { rent: 1500, food: 600, transport: 300, total: 2400 },
        'Curitiba': { rent: 1600, food: 650, transport: 320, total: 2570 },
        'Porto Alegre': { rent: 1700, food: 680, transport: 340, total: 2720 },
        'Recife': { rent: 1400, food: 550, transport: 280, total: 2230 },
        'Salvador': { rent: 1500, food: 600, transport: 300, total: 2400 },
        'Fortaleza': { rent: 1300, food: 500, transport: 250, total: 2050 }
    };
    
    const cityOptions = Object.keys(cities).map(city => 
        `<option value="${city}">${city}</option>`
    ).join('');
    
    app.innerHTML = `
        <div class="calculator-form">
            <h3>🌍 Comparação de Custo de Vida</h3>
            
            <div class="input-group">
                <label for="city1">Cidade 1:</label>
                <select id="city1">
                    <option value="">Selecione...</option>
                    ${cityOptions}
                </select>
            </div>
            
            <div class="input-group">
                <label for="city2">Cidade 2:</label>
                <select id="city2">
                    <option value="">Selecione...</option>
                    ${cityOptions}
                </select>
            </div>
            
            <button onclick="compareCities()" class="btn-calculate">Comparar Cidades</button>
            
            <div id="result-comparison" class="result-box" style="display:none;"></div>
        </div>
    `;
    
    window.cities = cities; // Disponibilizar globalmente
});

function compareCities() {
    const city1Name = document.getElementById('city1').value;
    const city2Name = document.getElementById('city2').value;
    
    if (!city1Name || !city2Name) {
        alert('Por favor, selecione duas cidades');
        return;
    }
    
    if (city1Name === city2Name) {
        alert('Por favor, selecione cidades diferentes');
        return;
    }
    
    const city1 = window.cities[city1Name];
    const city2 = window.cities[city2Name];
    
    const difference = city2.total - city1.total;
    const percentDiff = ((difference / city1.total) * 100).toFixed(1);
    
    const resultDiv = document.getElementById('result-comparison');
    resultDiv.style.display = 'block';
    resultDiv.innerHTML = `
        <h4>📊 Comparação: ${city1Name} vs ${city2Name}</h4>
        
        <div class="comparison-table">
            <table style="width:100%; border-collapse: collapse;">
                <tr>
                    <th>Categoria</th>
                    <th>${city1Name}</th>
                    <th>${city2Name}</th>
                </tr>
                <tr>
                    <td>Aluguel</td>
                    <td>${formatCurrency(city1.rent)}</td>
                    <td>${formatCurrency(city2.rent)}</td>
                </tr>
                <tr>
                    <td>Alimentação</td>
                    <td>${formatCurrency(city1.food)}</td>
                    <td>${formatCurrency(city2.food)}</td>
                </tr>
                <tr>
                    <td>Transporte</td>
                    <td>${formatCurrency(city1.transport)}</td>
                    <td>${formatCurrency(city2.transport)}</td>
                </tr>
                <tr style="font-weight: bold; background: #f0f0f0;">
                    <td>Total Mensal</td>
                    <td>${formatCurrency(city1.total)}</td>
                    <td>${formatCurrency(city2.total)}</td>
                </tr>
            </table>
        </div>
        
        <p style="margin-top: 20px;"><strong>Diferença:</strong> ${formatCurrency(Math.abs(difference))} 
        ${difference > 0 ? `(${city2Name} é ${percentDiff}% mais cara)` : 
                           `(${city2Name} é ${Math.abs(percentDiff)}% mais barata)`}</p>
        
        <p><em>💡 Valores aproximados baseados em custos médios de 2026</em></p>
    `;
}