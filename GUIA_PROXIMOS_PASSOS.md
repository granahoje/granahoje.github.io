# 📋 Guia Passo a Passo - Recuperação SEO

## ✅ O QUE JÁ FOI FEITO

### 1. Otimizações Técnicas Implementadas
- ✅ **JSON-LD Structured Data** adicionado (schema.org)
  - Organization
  - WebSite  
  - WebPage
  - BreadcrumbList
  
- ✅ **Meta Tags Sociais** implementadas
  - Open Graph (Facebook, LinkedIn)
  - Twitter Cards
  - Imagem featured para compartilhamento

- ✅ **Performance** otimizada
  - Preconnect para Google Fonts
  - Preconnect para Google Analytics  
  - DNS-prefetch para melhor carregamento
  
- ✅ **Canonical URL** corrigido
  - De: https://granahoje.github.io/index.html
  - Para: https://granahoje.github.io/

- ✅ **Sitemap.xml** atualizado
  - Data modificada para 2026-05-24
  - Sinalizando freshness ao Google

- ✅ **Git Push** realizado
  - Mudanças publicadas no GitHub
  - GitHub Pages irá fazer deploy automaticamente (1-5 minutos)

---

## 🎯 O QUE VOCÊ PRECISA FAZER AGORA

### PASSO 1: Aguardar Deploy (5-10 minutos)
Aguarde o GitHub Pages fazer o deploy das mudanças.

**Como verificar:**
1. Acesse: https://github.com/granahoje/granahoje.github.io/actions
2. Verifique se o workflow "pages build and deployment" está concluído ✅
3. Quando aparecer ✅ verde, o site está atualizado

### PASSO 2: Verificar as Mudanças (após deploy)
Acesse: https://granahoje.github.io/

**Validar:**
1. Abra o DevTools do navegador (F12)
2. Vá em "Elements" ou "Inspetor"
3. Procure por `<script type="application/ld+json">` no `<head>`
4. Procure por `<meta property="og:` no `<head>`
5. Se encontrar, significa que está tudo OK! ✅

### PASSO 3: Google Search Console - CRÍTICO! 🔥

#### A) Remover e Re-adicionar Sitemap
1. Acesse: https://search.google.com/search-console
2. Selecione a propriedade: **granahoje.github.io**
3. Menu lateral → **Sitemaps**
4. Se houver sitemap antigo, clique em "..." → **Excluir**
5. No campo "Adicionar sitemap" digite: **sitemap.xml**
6. Clique em **ENVIAR**
7. Aguarde confirmação ✅

#### B) Solicitar Indexação das Páginas Principais
Para CADA URL abaixo, faça:

**URLs para solicitar indexação:**
1. `https://granahoje.github.io/`
2. `https://granahoje.github.io/blog.html`
3. `https://granahoje.github.io/ferramentas.html`
4. `https://granahoje.github.io/about.html`
5. `https://granahoje.github.io/calculadora-juros-compostos.html`
6. `https://granahoje.github.io/calculadora-salario-liquido.html`
7. `https://granahoje.github.io/calculadora-investimento-mensal.html`
8. `https://granahoje.github.io/conversor-moedas.html`
9. `https://granahoje.github.io/calculadora-reserva-emergencia.html`
10. `https://granahoje.github.io/calculadora-financiamento.html`

**Como fazer:**
1. No Search Console, clique em **"Inspeção de URL"** (topo)
2. Cole a URL completa
3. Aguarde a análise (10-30 segundos)
4. Se aparecer "URL não está no Google":
   - Clique em **"SOLICITAR INDEXAÇÃO"**
   - Aguarde confirmação (pode levar 1-2 minutos)
5. Repita para todas as URLs da lista

#### C) Verificar Cobertura
1. Menu lateral → **Páginas** (ou "Indexação" → "Páginas")
2. Verifique se não há erros críticos
3. Procure por:
   - ❌ "Bloqueado por robots.txt" → Não deve ter
   - ❌ "Soft 404" → Não deve ter
   - ❌ "Redirecionado" → Não deve ter
   - ✅ "Descoberto" ou "Rastreado" → OK

---

## 📊 MONITORAMENTO (Próximos 7-14 dias)

### Dia 1-2: Aguardar Re-crawl
- Google precisa visitar o site novamente
- Pode levar 24-48h para começar a indexar
- **Ação:** Verificar Search Console 1x por dia

### Dia 3-5: Primeiros Sinais
- Impressões devem começar a subir
- Cliques podem ainda estar baixos
- **Ação:** Monitorar métricas no painel "Desempenho"

### Dia 7-14: Recuperação
- Esperado: Impressões voltando aos níveis normais
- Cliques devem aumentar gradualmente
- **Ação:** Continuar monitorando

### Se NÃO melhorar em 14 dias:
1. Voltar ao Search Console
2. Verificar se há **Ações Manuais** (penalizações)
3. Verificar se há **Problemas de Segurança**
4. Chamar o troubleshoot_agent para análise mais profunda

---

## 🎓 COMO USAR O SEARCH CONSOLE

### Dashboard Principal
1. Acesse: https://search.google.com/search-console
2. Selecione: granahoje.github.io
3. Você verá 4 cards principais:
   - **Desempenho** (cliques, impressões)
   - **Cobertura/Páginas** (páginas indexadas)
   - **Melhorias** (problemas de usabilidade)
   - **Segurança** (malware, hacks)

### Onde Ver os Números
**Gráfico de Desempenho:**
- Menu → **Desempenho**
- Filtre por **"Últimos 7 dias"** ou **"Últimos 28 dias"**
- Compare com **período anterior**
- Observe:
  - **Cliques totais** (linha azul)
  - **Impressões totais** (linha roxa)
  - **CTR médio** (linha verde)
  - **Posição média** (linha laranja)

**Páginas Indexadas:**
- Menu → **Indexação** → **Páginas**
- Veja quantas páginas estão indexadas
- Veja se há erros

---

## ⚠️ PROBLEMAS COMUNS

### Problema 1: Site não mudou após 10 minutos
**Solução:**
- Limpe o cache do navegador (Ctrl+Shift+Delete)
- Abra em modo anônimo
- Adicione `?v=2` no final da URL: `https://granahoje.github.io/?v=2`

### Problema 2: Search Console diz "URL não está no Google"
**Normal!** 
- Isso significa que o Google ainda não indexou
- Por isso você precisa clicar em "Solicitar indexação"
- Pode levar 1-7 dias para aparecer

### Problema 3: Erros no Search Console
- **4xx (404, 403):** URL não existe, verifique o link
- **5xx (500, 503):** Problema no servidor GitHub (raro)
- **Redirecionado:** Verificar configuração de redirect
- **Bloqueado:** Verificar robots.txt

---

## 📱 CONTATO SE PRECISAR DE AJUDA

Se após 14 dias as métricas NÃO melhorarem, ou se tiver dúvidas:

**Me chame novamente e compartilhe:**
1. Screenshot do Search Console (gráfico de Desempenho)
2. Screenshot da seção "Páginas"
3. Qualquer erro que aparecer
4. Eu vou analisar mais profundamente

---

## 🎯 EXPECTATIVAS REALISTAS

### O que é NORMAL:
- ✅ Recuperação levar 7-14 dias
- ✅ Oscilações nos primeiros dias
- ✅ Impressões subirem antes dos cliques
- ✅ Algumas páginas demorarem mais para indexar

### O que NÃO é normal:
- ❌ Nenhuma mudança após 30 dias
- ❌ Quedas contínuas mesmo após correções
- ❌ Erros persistentes no Search Console
- ❌ Penalizações manuais

---

## 🚀 RESUMO DO QUE FAZER AGORA

1. ⏱️ **Aguardar 5-10 minutos** (deploy do GitHub Pages)
2. 🔍 **Verificar se mudanças estão online** (ver PASSO 2)
3. 🗺️ **Re-adicionar sitemap** no Search Console (ver PASSO 3A)
4. 📍 **Solicitar indexação** das 10 URLs principais (ver PASSO 3B)
5. 📊 **Monitorar diariamente** por 7-14 dias
6. 🎉 **Comemorar quando as métricas subirem!**

---

**BOA SORTE! 🍀**

O trabalho pesado já está feito. Agora é só aguardar o Google fazer a mágica dele! 🚀

---

**Data:** 24/05/2026
**Próxima revisão:** 31/05/2026 (7 dias)
