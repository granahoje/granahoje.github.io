// ============================================
// PÁGINA DE COMPARAÇÃO - RADAR FINANCEIRO
// ============================================

class ComparisonPage {
  constructor() {
    this.products = [];
    this.categories = [];
    this.selectedCategory = null;
    
    this.init();
  }

  async init() {
    try {
      const response = await fetch('/radar/data/products.json');
      const data = await response.json();
      
      this.products = data.products;
      this.categories = data.categories;
      
      this.renderCategoryButtons();
      
      // Selecionar primeira categoria por padrão
      if (this.categories.length > 0) {
        this.selectCategory(this.categories[0].id);
      }
    } catch (error) {
      console.error('Erro ao carregar dados:', error);
    }
  }

  renderCategoryButtons() {
    const container = document.getElementById('category-buttons');
    container.innerHTML = this.categories.map(cat => `
      <button 
        class="filter-btn category-btn" 
        data-category="${cat.id}"
        onclick="comparisonPage.selectCategory('${cat.id}')"
      >
        ${cat.icon} ${cat.name}
      </button>
    `).join('');
  }

  selectCategory(categoryId) {
    this.selectedCategory = categoryId;
    
    // Atualizar botões ativos
    document.querySelectorAll('.category-btn').forEach(btn => {
      if (btn.dataset.category === categoryId) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    });

    this.renderComparison();
  }

  renderComparison() {
    const categoryProducts = this.products.filter(p => p.category === this.selectedCategory);
    
    if (categoryProducts.length === 0) {
      document.getElementById('comparison-table').innerHTML = `
        <p style="text-align: center; padding: 2rem; color: var(--text-secondary);">
          Nenhum produto nesta categoria
        </p>
      `;
      return;
    }

    this.renderComparisonHeader(categoryProducts);
    this.renderComparisonBody(categoryProducts);
  }

  renderComparisonHeader(products) {
    const header = document.getElementById('comparison-header');
    header.innerHTML = `
      <th style="position: sticky; left: 0; background: rgba(16, 185, 129, 0.1);">Características</th>
      ${products.map(p => `
        <th style="text-align: center;">
          <div style="font-weight: 700; color: var(--primary);">${p.name}</div>
          <div style="font-size: 0.875rem; color: var(--text-secondary);">${p.type}</div>
        </th>
      `).join('')}
    `;
  }

  renderComparisonBody(products) {
    const body = document.getElementById('comparison-body');
    
    const characteristics = [
      { label: 'Pontuação', key: 'score', format: (v) => `${v}%` },
      { label: 'Avaliação', key: 'rating', format: (v) => `⭐ ${v}` },
      { label: 'Badges', key: 'badges', format: (v) => v.join(', ') || '-' },
      { label: 'Prós', key: 'pros', format: (v) => v.join(', ') || '-' },
      { label: 'Contras', key: 'cons', format: (v) => v.join(', ') || '-' },
    ];

    body.innerHTML = characteristics.map(char => `
      <tr>
        <td style="font-weight: 600; position: sticky; left: 0; background: rgba(16, 185, 129, 0.05);">
          ${char.label}
        </td>
        ${products.map(p => `
          <td style="text-align: center;">
            ${char.format(p[char.key])}
          </td>
        `).join('')}
      </tr>
    `).join('');

    // Adicionar linha de ação
    const actionRow = document.createElement('tr');
    actionRow.innerHTML = `
      <td style="font-weight: 600; position: sticky; left: 0; background: rgba(16, 185, 129, 0.05);">
        Ação
      </td>
      ${products.map(p => `
        <td style="text-align: center;">
          <a href="${p.affiliateLink}" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-small">
            Acessar
          </a>
        </td>
      `).join('')}
    `;
    body.appendChild(actionRow);
  }
}

// Inicializar página de comparação
let comparisonPage;
document.addEventListener('DOMContentLoaded', () => {
  comparisonPage = new ComparisonPage();
});
