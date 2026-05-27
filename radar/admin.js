// ============================================
// PAINEL ADMINISTRATIVO - RADAR FINANCEIRO
// ============================================

const ADMIN_PASSWORD = 'radar2024'; // Alterar em produção
const STORAGE_KEY = 'radar_admin_session';
const PRODUCTS_STORAGE = 'radar_products_data';

class AdminPanel {
  constructor() {
    this.isAuthenticated = false;
    this.products = [];
    this.categories = [];
    
    this.checkAuthentication();
  }

  checkAuthentication() {
    const session = sessionStorage.getItem(STORAGE_KEY);
    if (session === 'authenticated') {
      this.isAuthenticated = true;
      this.showAdminPanel();
      this.loadData();
    } else {
      this.showLoginForm();
    }
  }

  showLoginForm() {
    document.getElementById('login-section').classList.remove('hidden');
    document.getElementById('admin-section').classList.add('hidden');
  }

  showAdminPanel() {
    document.getElementById('login-section').classList.add('hidden');
    document.getElementById('admin-section').classList.remove('hidden');
  }

  loadData() {
    // Carregar dados do localStorage ou arquivo JSON
    const savedProducts = localStorage.getItem(PRODUCTS_STORAGE);
    if (savedProducts) {
      this.products = JSON.parse(savedProducts);
    } else {
      this.loadProductsFromJSON();
    }

    this.loadCategories();
    this.updateDashboard();
    this.renderProductsTable();
    this.populateCategorySelect();
  }

  async loadProductsFromJSON() {
    try {
      const response = await fetch('/radar/data/products.json');
      const data = await response.json();
      this.products = data.products;
      this.categories = data.categories;
      localStorage.setItem(PRODUCTS_STORAGE, JSON.stringify(this.products));
    } catch (error) {
      console.error('Erro ao carregar produtos:', error);
      this.showAlert('Erro ao carregar dados dos produtos', 'error');
    }
  }

  loadCategories() {
    try {
      const response = fetch('/radar/data/products.json')
        .then(r => r.json())
        .then(data => {
          this.categories = data.categories;
        });
    } catch (error) {
      console.error('Erro ao carregar categorias:', error);
    }
  }

  updateDashboard() {
    document.getElementById('total-products').textContent = this.products.length;
    document.getElementById('total-categories').textContent = this.categories.length;
    
    const avgRating = (this.products.reduce((sum, p) => sum + p.rating, 0) / this.products.length).toFixed(1);
    document.getElementById('avg-rating').textContent = avgRating;
    
    const lastUpdate = localStorage.getItem('radar_last_update') || 'Nunca';
    document.getElementById('last-update').textContent = lastUpdate;
  }

  renderProductsTable() {
    const tbody = document.getElementById('products-table');
    tbody.innerHTML = this.products.map((product, index) => `
      <tr>
        <td><strong>${product.name}</strong></td>
        <td>${product.category}</td>
        <td><span style="color: var(--primary); font-weight: 700;">${product.score}%</span></td>
        <td><a href="${product.affiliateLink}" target="_blank" style="color: var(--primary);">Ver Link</a></td>
        <td>
          <div class="action-buttons">
            <button class="btn btn-secondary btn-small" onclick="editProduct(${index})">✏️ Editar</button>
            <button class="btn btn-danger btn-small" onclick="deleteProduct(${index})">🗑️ Deletar</button>
          </div>
        </td>
      </tr>
    `).join('');
  }

  populateCategorySelect() {
    const select = document.getElementById('product-category');
    select.innerHTML = '<option value="">Selecione uma categoria</option>' + 
      this.categories.map(cat => `<option value="${cat.id}">${cat.name}</option>`).join('');
  }

  addProduct(productData) {
    const newProduct = {
      id: `product-${Date.now()}`,
      ...productData,
      score: parseInt(productData.score),
      rating: parseFloat(productData.rating),
      badges: [],
      pros: [],
      cons: [],
      features: [],
      image: null
    };

    this.products.push(newProduct);
    this.saveProducts();
    this.renderProductsTable();
    this.updateDashboard();
    this.showAlert('Produto adicionado com sucesso!', 'success');
    document.getElementById('product-form').reset();
  }

  deleteProduct(index) {
    if (confirm('Tem certeza que deseja deletar este produto?')) {
      this.products.splice(index, 1);
      this.saveProducts();
      this.renderProductsTable();
      this.updateDashboard();
      this.showAlert('Produto deletado com sucesso!', 'success');
    }
  }

  saveProducts() {
    localStorage.setItem(PRODUCTS_STORAGE, JSON.stringify(this.products));
    localStorage.setItem('radar_last_update', new Date().toLocaleString('pt-BR'));
  }

  showAlert(message, type) {
    const container = document.getElementById('alert-container');
    const alert = document.createElement('div');
    alert.className = `alert alert-${type}`;
    alert.textContent = message;
    container.appendChild(alert);

    setTimeout(() => {
      alert.remove();
    }, 5000);
  }
}

// ============================================
// EVENT HANDLERS
// ============================================

let adminPanel;

function handleLogin(event) {
  event.preventDefault();
  const password = document.getElementById('password').value;

  if (password === ADMIN_PASSWORD) {
    sessionStorage.setItem(STORAGE_KEY, 'authenticated');
    adminPanel = new AdminPanel();
  } else {
    alert('Senha incorreta!');
    document.getElementById('password').value = '';
  }
}

function logout() {
  sessionStorage.removeItem(STORAGE_KEY);
  location.reload();
}

function handleAddProduct(event) {
  event.preventDefault();
  
  const productData = {
    name: document.getElementById('product-name').value,
    category: document.getElementById('product-category').value,
    type: document.getElementById('product-type').value,
    description: document.getElementById('product-description').value,
    affiliateLink: document.getElementById('product-link').value,
    score: document.getElementById('product-score').value,
    rating: document.getElementById('product-rating').value
  };

  adminPanel.addProduct(productData);
}

function editProduct(index) {
  alert('Funcionalidade de edição em desenvolvimento');
}

function deleteProduct(index) {
  adminPanel.deleteProduct(index);
}

function generateAllDescriptions() {
  adminPanel.showAlert('Gerando descrições com IA... (Requer API Key configurada)', 'success');
  // Implementar chamada para API de IA
}

function updateRankings() {
  adminPanel.products.forEach(product => {
    product.score = Math.floor(Math.random() * 30) + 70; // Simular atualização
  });
  adminPanel.saveProducts();
  adminPanel.renderProductsTable();
  adminPanel.updateDashboard();
  adminPanel.showAlert('Rankings atualizados com sucesso!', 'success');
}

function generateImages() {
  adminPanel.showAlert('Gerando imagens com IA... (Requer API Key configurada)', 'success');
  // Implementar chamada para API de geração de imagens
}

function saveOpenAIKey() {
  const key = document.getElementById('openai-key').value;
  if (key) {
    localStorage.setItem('openai_api_key', key);
    adminPanel.showAlert('Chave de API salva com sucesso!', 'success');
  }
}

function saveUpdateFrequency() {
  const frequency = document.getElementById('update-frequency').value;
  localStorage.setItem('update_frequency', frequency);
  adminPanel.showAlert('Frequência de atualização salva!', 'success');
}

// Inicializar painel quando DOM estiver pronto
document.addEventListener('DOMContentLoaded', () => {
  adminPanel = new AdminPanel();
});
