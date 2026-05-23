// Premium Core - Sistema base para todas as ferramentas premium
document.addEventListener('DOMContentLoaded', function() {
    console.log('Premium Core carregado');
});

// Funções utilitárias comuns
function formatCurrency(value) {
    return new Intl.NumberFormat('pt-BR', {
        style: 'currency',
        currency: 'BRL'
    }).format(value);
}

function formatPercent(value) {
    return new Intl.NumberFormat('pt-BR', {
        style: 'percent',
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
    }).format(value / 100);
}

function parseNumber(value) {
    if (typeof value === 'string') {
        value = value.replace(/\./g, '').replace(',', '.');
    }
    return parseFloat(value) || 0;
}
