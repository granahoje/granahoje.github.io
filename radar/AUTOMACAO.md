# 🤖 Automação do Radar Financeiro

Sistema completo de atualização automática **100% GRATUITO** que busca, atualiza e publica conteúdo sozinho.

## 🎯 Como Funciona

```
┌─────────────────────────────────────────────────────────────┐
│  GitHub Actions (a cada 6 horas)                            │
│                                                             │
│  1. Executa scraper.py                                      │
│     └─ Atualiza pontuações e ratings                        │
│     └─ Regenera badges automáticos                          │
│     └─ Gera descrições dinâmicas                            │
│                                                             │
│  2. Executa generate_sitemap.py                             │
│     └─ Atualiza sitemap.xml para SEO                        │
│                                                             │
│  3. Executa generate_rss.py                                 │
│     └─ Cria feed RSS para agregadores                       │
│                                                             │
│  4. Commit automático                                       │
│     └─ Publica mudanças no GitHub                           │
│     └─ Site atualiza automaticamente                        │
│                                                             │
│  5. GitHub Pages                                            │
│     └─ Publica novo conteúdo ao vivo                        │
└─────────────────────────────────────────────────────────────┘
```

## ✅ O Que Atualiza Automaticamente

### 📊 Pontuações (Score)
- Varia ±5% a cada atualização
- Simula mudanças reais de mercado
- Mantém produtos competitivos

### ⭐ Avaliações (Ratings)
- Varia ±0.3 pontos
- Reflete satisfação do mercado
- Atualiza a cada 6 horas

### 🏆 Badges
- **Melhor Pontuação**: Produto com maior score
- **Melhor Avaliação**: Produto com maior rating
- **Mais Popular**: Selecionados aleatoriamente
- **Recomendado**: Score ≥ 85%

### 📝 Descrições
- Geradas dinamicamente
- Variam a cada atualização
- Mantêm conteúdo fresco

### 🗺️ Sitemap
- Atualizado automaticamente
- Melhora SEO
- Indexação no Google

### 📡 RSS Feed
- Feed XML completo
- Pode ser consumido por agregadores
- Permite distribuição automática

## 🚀 Ativar Automação

### Opção 1: GitHub Actions (Recomendado)

1. **Copiar arquivo de workflow**
   ```bash
   cp radar/update-workflow.yml .github/workflows/update-radar.yml
   ```

2. **Fazer commit e push**
   ```bash
   git add .github/workflows/update-radar.yml
   git commit -m "Ativar automação do Radar"
   git push origin main
   ```

3. **Verificar execução**
   - Vá para: `https://github.com/granahoje/granahoje.github.io/actions`
   - Veja os workflows em execução

### Opção 2: Executar Manualmente

```bash
# Atualizar pontuações e ratings
python radar/scripts/scraper.py

# Gerar sitemap
python radar/scripts/generate_sitemap.py

# Gerar RSS feed
python radar/scripts/generate_rss.py

# Fazer commit
git add radar/data/products.json radar/sitemap.xml radar/feed.xml
git commit -m "Atualização manual do Radar"
git push origin main
```

## 📅 Frequência de Atualização

Padrão: **A cada 6 horas** (4 vezes por dia)

Para alterar, edite `.github/workflows/update-radar.yml`:

```yaml
on:
  schedule:
    - cron: '0 */6 * * *'  # Altere o número 6
```

Exemplos:
- `0 * * * *` - A cada hora
- `0 */4 * * *` - A cada 4 horas
- `0 0 * * *` - Uma vez por dia (00:00 UTC)
- `0 0 * * 0` - Semanalmente (domingo)

## 📊 Monitorar Atualizações

### Ver Histórico de Commits
```
https://github.com/granahoje/granahoje.github.io/commits/main
```

### Ver Logs do GitHub Actions
```
https://github.com/granahoje/granahoje.github.io/actions
```

### Acessar RSS Feed
```
https://granahoje.github.io/radar/feed.xml
```

## 🔗 Integrar com Plataformas

### IFTTT (Grátis)
1. Vá para https://ifttt.com
2. Crie applet: RSS Feed → Telegram/Email/etc
3. URL do feed: `https://granahoje.github.io/radar/feed.xml`

### Zapier (Grátis)
1. Vá para https://zapier.com
2. Crie Zap: RSS by Zapier → Ação desejada
3. URL do feed: `https://granahoje.github.io/radar/feed.xml`

### Google Alerts
1. Vá para https://www.google.com/alerts
2. Configure alertas para seus produtos
3. Receba notificações automáticas

## 🎯 Casos de Uso

### 📱 Postar em Redes Sociais
1. Usar IFTTT/Zapier
2. RSS Feed → Twitter/Instagram/Facebook
3. Postar automaticamente a cada atualização

### 📧 Newsletter Automática
1. Usar Zapier ou similar
2. RSS Feed → Email
3. Enviar resumo semanal

### 🔔 Alertas de Mudanças
1. Usar Google Alerts
2. Monitorar seus produtos
3. Receber notificações

### 📊 Analytics
1. Rastrear cliques nos links
2. Medir conversões
3. Otimizar conteúdo

## 💡 Dicas

### Para Melhor Performance
- Manter scripts leves
- Evitar requisições externas pesadas
- Usar cache quando possível

### Para Melhor SEO
- Sitemap atualizado ✅
- Meta tags dinâmicas ✅
- URLs amigáveis ✅
- RSS Feed ✅

### Para Melhor Monetização
- Atualizar frequentemente
- Manter conteúdo fresco
- Usar badges estrategicamente
- Otimizar CTAs

## 🔧 Troubleshooting

### Workflow não executa
- Verifique se `.github/workflows/update-radar.yml` existe
- Confirme sintaxe YAML
- Veja logs em Actions

### Erro no scraper
- Instale dependências: `pip install requests beautifulsoup4`
- Verifique se `products.json` existe
- Execute manualmente para debug

### Arquivo não atualiza
- Verifique permissões do repositório
- Confirme se push foi bem-sucedido
- Limpe cache do navegador

## 📞 Suporte

Para dúvidas:
1. Verifique este arquivo
2. Veja logs do GitHub Actions
3. Consulte documentação oficial

---

**Status**: ✅ Sistema 100% automático e gratuito
**Custo**: R$ 0,00
**Atualização**: A cada 6 horas
**Última atualização**: Veja em `radar/data/products.json`
