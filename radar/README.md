# 📊 Radar Financeiro

Plataforma automatizada de comparação e análise de produtos financeiros com geração automática de conteúdo via IA.

## 🚀 Funcionalidades

- ✅ **Catálogo Completo**: Empréstimos, cartões, contas PJ, criptomoedas, seguros
- ✅ **Rankings Automáticos**: Pontuação, badges (Melhor Taxa, Mais Popular, Recomendado)
- ✅ **Geração de Conteúdo via IA**: Descrições, análises, prós/contras automáticos
- ✅ **Página de Comparação**: Lado a lado entre produtos da mesma categoria
- ✅ **Filtros e Busca**: Por categoria, tipo e características
- ✅ **Painel Administrativo**: Gerenciar produtos, editar links, atualizar conteúdo
- ✅ **SEO Otimizado**: Meta tags dinâmicas, sitemap.xml, URLs amigáveis
- ✅ **Geração de Imagens**: Ilustrações automáticas para cada produto
- ✅ **Atualização Automática**: GitHub Actions com cron job periódico
- ✅ **Design Dark Profissional**: Verde-esmeralda e azul-marinho

## 📁 Estrutura do Projeto

```
radar/
├── data/
│   └── products.json          # Catálogo de produtos
├── scripts/
│   ├── generate_content.py    # Gerar conteúdo com IA
│   ├── generate_images.py     # Gerar imagens com IA
│   └── generate_sitemap.py    # Gerar sitemap.xml
├── admin/
│   └── index.html             # Painel administrativo
├── comparacao/
│   ├── index.html             # Página de comparação
│   └── comparacao.js          # Lógica de comparação
├── images/                    # Imagens dos produtos
├── index.html                 # Página principal
├── styles.css                 # Estilos (dark theme)
├── app.js                     # Lógica principal
└── admin.js                   # Lógica do painel admin
```

## 🔧 Configuração

### 1. Clonar o Repositório

```bash
git clone https://github.com/granahoje/granahoje.github.io.git
cd granahoje.github.io
```

### 2. Adicionar Secrets do GitHub

Para usar as funcionalidades de IA, configure os secrets no repositório:

1. Vá para **Settings → Secrets and variables → Actions**
2. Adicione `OPENAI_API_KEY` com sua chave da OpenAI

### 3. Executar Localmente

```bash
# Iniciar um servidor local
python -m http.server 8000

# Acessar em http://localhost:8000/radar/
```

## 📝 Gerenciar Produtos

### Adicionar Produto Manualmente

1. Abra `/radar/data/products.json`
2. Adicione um novo objeto ao array `products`:

```json
{
  "id": "novo-produto",
  "name": "Nome do Produto",
  "category": "emprestimos",
  "type": "Tipo",
  "description": "Descrição",
  "affiliateLink": "https://seu-link-afiliado.com",
  "rating": 4.5,
  "score": 90,
  "badges": ["Recomendado"],
  "pros": ["Pró 1", "Pró 2"],
  "cons": ["Contra 1"],
  "features": ["feature1"],
  "image": "produto.png"
}
```

### Usar Painel Administrativo

1. Acesse `/radar/admin/`
2. Senha padrão: `radar2024` (altere em `admin.js`)
3. Adicione, edite ou delete produtos
4. Gere conteúdo e imagens automaticamente

## 🤖 Automação com IA

### Gerar Conteúdo

```bash
OPENAI_API_KEY=sua-chave python radar/scripts/generate_content.py
```

Gera automaticamente:
- Descrições dos produtos
- Prós e contras
- Análises

### Gerar Imagens

```bash
OPENAI_API_KEY=sua-chave python radar/scripts/generate_images.py
```

Gera ilustrações para cada produto usando DALL-E.

### Gerar Sitemap

```bash
python radar/scripts/generate_sitemap.py
```

Cria `sitemap.xml` para SEO.

## ⏰ Automação com GitHub Actions

O workflow `.github/workflows/update-radar.yml` executa automaticamente:

- **Diariamente** (00:00 UTC): Atualiza conteúdo e imagens
- **Manualmente**: Via botão "Run workflow" no GitHub

### Configurar Frequência

Edite `.github/workflows/update-radar.yml`:

```yaml
on:
  schedule:
    - cron: '0 0 * * *'  # Altere conforme necessário
```

Exemplos de cron:
- `0 0 * * *` - Diariamente às 00:00 UTC
- `0 */6 * * *` - A cada 6 horas
- `0 0 * * 0` - Semanalmente (domingo)

## 🔐 Segurança

### Painel Admin

- Senha protegida (altere `ADMIN_PASSWORD` em `admin.js`)
- Armazenamento local (localStorage)
- Sem exposição de dados sensíveis

### Links de Afiliados

- Armazenados em `products.json`
- Não expostos em HTML estático
- Redirecionados via atributo `href`

## 📱 Responsividade

Site totalmente responsivo para:
- 📱 Mobile (320px+)
- 📱 Tablet (768px+)
- 💻 Desktop (1200px+)

## 🎨 Customização

### Cores

Edite `styles.css`:

```css
:root {
  --primary: #10B981;        /* Verde-esmeralda */
  --secondary: #1E3A8A;      /* Azul-marinho */
  --bg-dark: #0F172A;        /* Fundo escuro */
  /* ... mais cores */
}
```

### Tipografia

Adicione fontes do Google em `index.html`:

```html
<link href="https://fonts.googleapis.com/css2?family=..." rel="stylesheet">
```

## 🚀 Deploy

### GitHub Pages

1. Commit e push para `main` branch
2. GitHub Pages publica automaticamente em `granahoje.github.io/radar/`

### Domínio Customizado

1. Adicione `CNAME` na raiz do repositório
2. Configure DNS no seu registrador

## 📊 SEO

- ✅ Meta tags dinâmicas
- ✅ Open Graph (OG)
- ✅ Sitemap.xml
- ✅ URLs amigáveis
- ✅ Schema.org (estruturado)

## 🐛 Troubleshooting

### Produtos não carregam

- Verifique se `products.json` está em `/radar/data/`
- Abra console do navegador (F12) para ver erros
- Verifique permissões do arquivo

### Imagens não aparecem

- Verifique se estão em `/radar/images/`
- Confirme nome do arquivo em `products.json`
- Teste em navegador diferente

### GitHub Actions falha

- Verifique se `OPENAI_API_KEY` está configurada
- Veja logs em **Actions → Workflow runs**
- Confirme sintaxe do Python

## 📞 Suporte

Para dúvidas ou problemas:
1. Verifique este README
2. Abra uma issue no GitHub
3. Consulte documentação da OpenAI

## 📄 Licença

MIT License - Veja LICENSE para detalhes

---

**Última atualização**: 2024
**Versão**: 1.0.0
**Status**: ✅ Ativo e em desenvolvimento
