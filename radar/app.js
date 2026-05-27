// ============================================
// RADAR FINANCEIRO - APLICAÇÃO PRINCIPAL
// ============================================

class RadarFinanceiro {
  constructor() {
    this.products = [];
    this.categories = [];
    this.filteredProducts = [];
    this.currentCategory = null;
    this.searchQuery = '';
    this.sortBy = 'score';
    
    this.init();
  }

  async init() {
    try {
      // Carregar dados dos produtos
      const response = await fetch('/radar/data/products.json');
      const data = await response.json();
      
      this.products = data.products;
      this.categories = data.categories;
      
      this.setupEventListeners();
      this.renderCatalog();
      this.renderCategories();
    } catch (error) {
      console.error('Erro ao carregar dados:', error);
    }
  }

  setupEventListeners() {
    // Busca
    const searchInput = document.getElementById('search');
    if (searchInput) {
      searchInput.addEventListener('input', (e) => {
        this.searchQuery = e.target.value.toLowerCase();
        this.applyFilters();
      });
    }

    // Ordenação
    const sortSelect = document.getElementById('sort');
    if (sortSelect) {
      sortSelect.addEventListener('change', (e) => {
        this.sortBy = e.target.value;
        this.applyFilters();
      });
    }

    // Filtros de categoria
    document.addEventListener('click', (e) => {
      if (e.target.classList.contains('category-filter')) {
        const categoryId = e.target.dataset.category;
        this.currentCategory = this.currentCategory === categoryId ? null : categoryId;
        this.updateCategoryButtons();
        this.applyFilters();
      }
    });
  }

  renderCategories() {
    const container = document.getElementById('categories-container');
    if (!container) return;

    container.innerHTML = this.categories.map(cat => `
      <div class="category-card card">
        <div class="category-icon" style="font-size: 2.5rem; margin-bottom: 1rem;">
          ${cat.icon}
        </div>
        <h3 class="category-name">${cat.name}</h3>
        <p class="category-desc">${cat.description}</p>
        <button class="btn btn-primary category-filter" data-category="${cat.id}">
          Ver Produtos
        </button>
      </div>
    `).join('');
  }

  renderCatalog() {
    this.applyFilters();
    this.renderProducts();
  }

  applyFilters() {
    let filtered = [...this.products];

    // Filtro por categoria
    if (this.currentCategory) {
      filtered = filtered.filter(p => p.category === this.currentCategory);
    }

    // Filtro por busca
    if (this.searchQuery) {
      filtered = filtered.filter(p => 
        p.name.toLowerCase().includes(this.searchQuery) ||
        p.description.toLowerCase().includes(this.searchQuery) ||
        p.type.toLowerCase().includes(this.searchQuery)
      );
    }

    // Ordenação
    filtered.sort((a, b) => {
      switch (this.sortBy) {
        case 'score':
          return b.score - a.score;
        case 'rating':
          return b.rating - a.rating;
        case 'name':
          return a.name.localeCompare(b.name);
        default:
          return 0;
      }
    });

    this.filteredProducts = filtered;
  }

  renderProducts() {
    const container = document.getElementById('products-container');
    if (!container) return;

    if (this.filteredProducts.length === 0) {
      container.innerHTML = `
        <div style="grid-column: 1/-1; text-align: center; padding: 3rem;">
          <p style="font-size: 1.25rem; color: var(--text-secondary);">
            Nenhum produto encontrado
          </p>
        </div>
      `;
      return;
    }

    container.innerHTML = this.filteredProducts.map(product => `
      <div class="product-card fade-in">
        <div class="product-image">
          ${product.image ? `<img src="/radar/images/${product.image}" alt="${product.name}">` : '💰'}
        </div>
        <div class="product-content">
          <div class="product-header">
            <div class="product-name">${product.name}</div>
            <div class="product-type">${product.type}</div>
          </div>
          
          <p class="product-description">${product.description}</p>
          
          <div class="product-badges">
            ${product.badges.map(badge => `
              <span class="badge badge-primary">${badge}</span>
            `).join('')}
          </div>
          
          <div class="product-rating">
            <div class="rating">
              <span class="stars">${this.renderStars(product.rating)}</span>
              <span>${product.rating}</span>
            </div>
            <div class="product-score">${product.score}%</div>
          </div>
          
          <div class="product-footer">
            <a href="/radar/produto/${product.id}/" class="btn btn-outline">
              Ver Detalhes
            </a>
            <a href="${product.affiliateLink}" target="_blank" rel="noopener noreferrer" class="btn btn-primary">
              Acessar
            </a>
          </div>
        </div>
      </div>
    `).join('');
  }

  renderStars(rating) {
    const fullStars = Math.floor(rating);
    const hasHalf = rating % 1 !== 0;
    let stars = '';

    for (let i = 0; i < 5; i++) {
      if (i < fullStars) {
        stars += '<span class="star">★</span>';
      } else if (i === fullStars && hasHalf) {
        stars += '<span class="star">⭐</span>';
      } else {
        stars += '<span class="star empty">☆</span>';
      }
    }

    return stars;
  }

  updateCategoryButtons() {
    document.querySelectorAll('.category-filter').forEach(btn => {
      if (btn.dataset.category === this.currentCategory) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    });
  }

  // Método para obter produto por ID
  getProductById(id) {
    return this.products.find(p => p.id === id);
  }

  // Método para obter produtos da mesma categoria
  getProductsByCategory(categoryId) {
    return this.products.filter(p => p.category === categoryId);
  }

  // Método para gerar página de detalhes
  renderProductDetail(productId) {
    const product = this.getProductById(productId);
    if (!product) return null;

    const category = this.categories.find(c => c.id === product.category);
    const relatedProducts = this.getProductsByCategory(product.category)
      .filter(p => p.id !== productId)
      .slice(0, 3);

    return {
      product,
      category,
      relatedProducts
    };
  }

  // Método para gerar página de comparação
  renderComparison(categoryId) {
    const products = this.getProductsByCategory(categoryId);
    const category = this.categories.find(c => c.id === categoryId);

    return {
      category,
      products
    };
  }
}

// Inicializar aplicação quando DOM estiver pronto
document.addEventListener('DOMContentLoaded', () => {
  window.radar = new RadarFinanceiro();
});

// ============================================
// UTILITÁRIOS
// ============================================

// Função para gerar slug a partir de texto
function generateSlug(text) {
  return text
    .toLowerCase()
    .trim()
    .replace(/[^\w\s-]/g, '')
    .replace(/\s+/g, '-')
    .replace(/-+/g, '-');
}

// Função para formatar data
function formatDate(date) {
  const options = { year: 'numeric', month: 'long', day: 'numeric' };
  return new Date(date).toLocaleDateString('pt-BR', options);
}

// Função para copiar para clipboard
function copyToClipboard(text) {
  navigator.clipboard.writeText(text).then(() => {
    alert('Copiado para a área de transferência!');
  });
}

// Função para abrir modal
function openModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.style.display = 'flex';
  }
}

// Função para fechar modal
function closeModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.style.display = 'none';
  }
}

// Fechar modal ao clicar fora
document.addEventListener('click', (e) => {
  if (e.target.classList.contains('modal')) {
    e.target.style.display = 'none';
  }
});
