#!/usr/bin/env python3
"""
Gerador avançado de conteúdo com foco em EEAT (Experience, Expertise, Authoritativeness, Trustworthiness)
Cria artigos únicos com 1200+ palavras, estilo humano, sem parecer IA
Gera páginas HTML estáticas para eliminar erros 404
"""

import json
import os
import random
from datetime import datetime
from pathlib import Path

class ContentGeneratorEEAT:
    def __init__(self):
        self.products_file = 'radar/data/products.json'
        self.cache_dir = 'radar/cache'
        self.content_dir = 'radar/content'
        self.produto_dir = 'radar/produto'
        os.makedirs(self.content_dir, exist_ok=True)
        os.makedirs(self.produto_dir, exist_ok=True)
        
    def load_data(self):
        """Carregar todos os dados"""
        data = {
            'products': [],
            'bcb': {},
            'crypto': {},
            'currencies': {},
            'rss': {}
        }
        
        # Carregar produtos
        with open(self.products_file, 'r', encoding='utf-8') as f:
            data['products'] = json.load(f)['products']
        
        # Carregar cache
        if os.path.exists(os.path.join(self.cache_dir, 'bcb_cache.json')):
            with open(os.path.join(self.cache_dir, 'bcb_cache.json')) as f:
                data['bcb'] = json.load(f)
        
        if os.path.exists(os.path.join(self.cache_dir, 'crypto_cache.json')):
            with open(os.path.join(self.cache_dir, 'crypto_cache.json')) as f:
                data['crypto'] = json.load(f)
        
        if os.path.exists(os.path.join(self.cache_dir, 'currencies_cache.json')):
            with open(os.path.join(self.cache_dir, 'currencies_cache.json')) as f:
                data['currencies'] = json.load(f)
        
        return data
    
    # ============ SEÇÕES COM FOCO EM EEAT ============
    
    def get_expertise_intro(self, product, data):
        """Introdução que demonstra expertise e autoridade (150+ palavras)"""
        intros = [
            f"""Você está buscando {product['type'].lower()} com as melhores condições? {product['name']} pode ser exatamente o que você procura. Como especialistas em análise de produtos financeiros, realizamos uma avaliação completa e detalhada de {product['name']}, considerando múltiplos aspectos técnicos, regulatórios e de experiência do usuário. Neste artigo, compartilhamos nossa análise profunda baseada em dados reais, feedback de usuários e pesquisa de mercado. Vamos explorar em profundidade como este produto se destaca no mercado financeiro brasileiro, por que tantas pessoas escolhem confiar nele e se ele é realmente a melhor opção para suas necessidades financeiras específicas.""",
            
            f"""Se você acompanha o mercado financeiro com atenção, já deve ter ouvido falar em {product['name']}. Mas você realmente sabe como este {product['type'].lower()} funciona, quais são suas vantagens reais e se é a melhor opção para você? Nossa equipe de especialistas financeiros realizou uma análise abrangente de {product['name']}, examinando cada detalhe desde as características básicas até os aspectos mais técnicos e regulatórios. Neste guia completo, compartilhamos nossas descobertas para que você possa fazer uma escolha informada e segura, baseada em informações verificadas e experiência prática.""",
            
            f"""No cenário financeiro atual, encontrar um bom {product['type'].lower()} é fundamental para atingir seus objetivos. {product['name']} tem se destacado como uma opção confiável e inovadora entre os profissionais financeiros. Mas será que é realmente a melhor escolha para você? Nossa análise profunda de {product['name']} examina não apenas as características superficiais, mas também a reputação da empresa, conformidade regulatória, segurança de dados e feedback real de usuários. Vamos desvendar todos os detalhes importantes para ajudá-lo a tomar a decisão mais acertada.""",
        ]
        return random.choice(intros)
    
    def get_trustworthiness_section(self, product):
        """Seção sobre confiabilidade e segurança (150+ palavras)"""
        trust_sections = [
            f"""## Confiabilidade e Segurança de {product['name']}

A confiabilidade é um fator crítico ao escolher um produto financeiro. {product['name']} demonstra seu compromisso com a segurança através de múltiplas camadas de proteção. A plataforma implementa criptografia de ponta a ponta, autenticação de dois fatores e conformidade com regulamentações financeiras brasileiras.

Segundo análises independentes e feedback de usuários, {product['name']} mantém um histórico consistente de proteção de dados e segurança das transações. A empresa investe continuamente em infraestrutura de segurança e realiza auditorias regulares para garantir que os dados dos usuários estejam protegidos.

A reputação de {product['name']} no mercado foi construída através de anos de operação confiável. Não há relatos significativos de violações de segurança ou problemas de confiabilidade que prejudiquem a experiência dos usuários. Esta consistência é um indicador forte de que você pode confiar seus dados e recursos financeiros à plataforma.""",
            
            f"""## Segurança e Conformidade Regulatória

{product['name']} opera em conformidade com as regulamentações do Banco Central do Brasil e outras autoridades financeiras relevantes. Esta conformidade regulatória é essencial para garantir que o produto funcione dentro dos padrões legais e éticos estabelecidos.

A empresa por trás de {product['name']} passa por auditorias regulares e mantém certificações de segurança internacionais. Estes fatores contribuem para a confiabilidade geral da plataforma e demonstram o compromisso da empresa com a proteção do usuário.

Usuários que escolhem {product['name']} podem ter confiança de que estão utilizando um serviço que atende aos mais altos padrões de segurança e conformidade regulatória. Esta é uma das razões pelas quais profissionais financeiros e investidores experientes confiam nesta plataforma.""",
        ]
        return random.choice(trust_sections)
    
    def get_experience_section(self, product):
        """Seção sobre experiência do usuário (150+ palavras)"""
        experience_sections = [
            f"""## Experiência do Usuário com {product['name']}

A experiência do usuário é fundamental para a satisfação com qualquer produto financeiro. {product['name']} foi desenvolvido com uma abordagem centrada no usuário, priorizando a facilidade de uso sem comprometer a funcionalidade.

Usuários relatam que a interface de {product['name']} é intuitiva e fácil de navegar, mesmo para iniciantes. O processo de onboarding é simplificado, permitindo que novos usuários começem rapidamente. A plataforma oferece suporte educacional através de tutoriais, webinários e documentação abrangente.

Além disso, o atendimento ao cliente de {product['name']} é responsivo e prestativo. Usuários que enfrentam dúvidas ou problemas podem contar com suporte rápido e eficiente. Esta combinação de interface amigável e suporte de qualidade cria uma experiência positiva que mantém os usuários satisfeitos e engajados.""",
            
            f"""## Como é Usar {product['name']} na Prática

Baseado em feedback de usuários reais, a experiência prática com {product['name']} é consistentemente positiva. A plataforma oferece funcionalidades que são fáceis de encontrar e usar, reduzindo a curva de aprendizado.

O design responsivo de {product['name']} funciona perfeitamente em dispositivos móveis e desktop, permitindo que os usuários acessem seus dados e realizem transações de qualquer lugar. A velocidade de carregamento é rápida, e as transações são processadas de forma eficiente.

Usuários experientes apreciam a profundidade de funcionalidades disponíveis, enquanto iniciantes encontram as ferramentas básicas acessíveis e fáceis de usar. Esta versatilidade é um dos pontos fortes de {product['name']} que contribui para sua reputação positiva no mercado.""",
        ]
        return random.choice(experience_sections)
    
    def get_expertise_features(self, product):
        """Seção de características com análise de expertise (200+ palavras)"""
        features_text = f"""## Análise Técnica das Características de {product['name']}

As principais características de {product['name']} foram desenvolvidas com base em pesquisa de mercado e feedback de usuários. Cada funcionalidade serve a um propósito específico e contribui para a proposta de valor geral:

"""
        
        if product.get('features'):
            for i, feature in enumerate(product['features'][:6], 1):
                # Limpar slug técnico
                display_feature = feature.replace('-', ' ').title()
                variations = [
                    f"**{i}. {display_feature}** - Esta funcionalidade foi implementada em resposta às necessidades identificadas no mercado.",
                    f"**{display_feature}** - Desenvolvida com base em melhores práticas da indústria financeira.",
                    f"**{display_feature}** - Uma característica que diferencia {product['name']} de seus concorrentes.",
                ]
                features_text += random.choice(variations) + "\n"
        
        features_text += f"""
Cada uma destas características foi cuidadosamente desenvolvida e testada para oferecer a melhor experiência possível. {product['name']} investe continuamente em pesquisa e desenvolvimento para garantir que seus usuários tenham acesso às melhores ferramentas disponíveis no mercado.

A combinação destas funcionalidades cria um ecossistema completo que atende às necessidades dos usuários de forma integrada e eficiente. Análises técnicas independentes confirmam que {product['name']} oferece um conjunto de ferramentas robusto e bem integrado.

Usuários que utilizam todas as funcionalidades de {product['name']} relatam maior eficiência em suas operações financeiras e melhor controle sobre seus investimentos ou créditos. A profundidade das funcionalidades permite que usuários avançados otimizem completamente sua experiência."""
        
        return features_text
    
    def get_authority_section(self, product, data):
        """Seção que demonstra autoridade (150+ palavras)"""
        authority_text = f"""## Posição de {product['name']} no Mercado

{product['name']} é reconhecido como um dos principais players no segmento de {product['type'].lower()} no Brasil. Esta posição foi conquistada através de anos de operação consistente, inovação contínua e satisfação do cliente.

Análises de mercado independentes reconhecem {product['name']} como uma solução confiável e inovadora. A empresa é frequentemente citada em publicações financeiras especializadas como um exemplo de boas práticas no setor.

A autoridade de {product['name']} é reforçada por parcerias estratégicas com instituições financeiras reconhecidas, certificações internacionais e conformidade com padrões regulatórios rigorosos. Estes fatores combinados estabelecem {product['name']} como uma autoridade confiável no seu segmento de mercado."""
        
        return authority_text
    
    def get_detailed_comparison(self, product):
        """Comparação detalhada com análise de expertise (200+ palavras)"""
        comparison = f"""## Análise Comparativa: {product['name']} vs Concorrentes

Quando comparado com outras opções no mercado, {product['name']} oferece um equilíbrio interessante entre custo-benefício, funcionalidades e segurança. Nossa análise comparativa examinou múltiplos critérios para fornecer uma avaliação abrangente.

**Critérios de Comparação:**

- **Facilidade de Uso**: {product['name']} se destaca pela interface intuitiva e processo de onboarding simplificado
- **Suporte ao Cliente**: Atendimento responsivo e prestativo em múltiplos canais
- **Segurança e Confiabilidade**: Implementação de padrões de segurança de classe empresarial
- **Transparência de Taxas**: Estrutura de preços clara sem cobranças ocultas
- **Velocidade de Processamento**: Transações processadas rapidamente com confirmação em tempo real
- **Funcionalidades Avançadas**: Conjunto robusto de ferramentas para usuários experientes
- **Conformidade Regulatória**: Total conformidade com regulamentações financeiras brasileiras

Enquanto alguns concorrentes podem oferecer recursos mais especializados, {product['name']} se destaca pelo equilíbrio geral. Muitos usuários escolhem {product['name']} justamente porque oferece o melhor custo-benefício considerando todos estes fatores."""
        
        return comparison
    
    def get_use_cases(self, product):
        """Casos de uso específicos (150+ palavras)"""
        use_cases = f"""## Casos de Uso Reais de {product['name']}

{product['name']} é ideal para diversos perfis de usuários e situações específicas:

**Para Iniciantes**: Usuários que estão começando sua jornada financeira encontram em {product['name']} uma plataforma acessível com ferramentas educacionais abrangentes. O suporte ao cliente ajuda a responder dúvidas iniciais.

**Para Profissionais**: Profissionais financeiros apreciam a profundidade de funcionalidades e ferramentas avançadas que {product['name']} oferece. A plataforma suporta operações complexas e análises detalhadas.

**Para Investidores**: Investidores que buscam diversificação encontram em {product['name']} acesso a múltiplas classes de ativos e ferramentas de análise sofisticadas.

**Para Pequenos Empresários**: Proprietários de negócios utilizam {product['name']} para gerenciar fluxo de caixa, acessar crédito e otimizar suas operações financeiras.

Cada um destes grupos encontra valor específico em {product['name']}, o que explica sua ampla base de usuários satisfeitos."""
        
        return use_cases
    
    def get_conclusion_eeat(self, product):
        """Conclusão com foco em EEAT (150+ palavras)"""
        conclusions = [
            f"""## Conclusão: {product['name']} é a Escolha Certa?

Baseado em nossa análise abrangente de expertise, experiência, autoridade e confiabilidade, {product['name']} apresenta-se como uma opção sólida no mercado de {product['type'].lower()}. Com suas características bem definidas, reputação estabelecida, conformidade regulatória e compromisso contínuo com a melhoria, é uma escolha que merece consideração se você busca um {product['type'].lower()} confiável e eficiente.

A decisão de escolher {product['name']} deve levar em conta suas necessidades específicas, seu perfil como usuário, seus objetivos financeiros e sua tolerância ao risco. Se os pontos positivos superam os negativos para sua situação particular, então é definitivamente uma opção a explorar seriamente.

Lembre-se de que a melhor escolha é aquela que se alinha perfeitamente com suas necessidades e expectativas. Recomendamos que você visite o site oficial de {product['name']} para obter informações mais recentes e conhecer as condições atuais antes de tomar sua decisão final.""",
            
            f"""## Recomendação Final

Nossa análise profunda de {product['name']} demonstra que é uma plataforma confiável, segura e bem posicionada no mercado. Com base em critérios de EEAT (Experience, Expertise, Authoritativeness, Trustworthiness), {product['name']} atende aos mais altos padrões.

Se você está em busca de um {product['type'].lower()} que combine segurança, eficiência, bom atendimento e conformidade regulatória, {product['name']} é definitivamente uma opção a ser explorada. A decisão final dependerá de suas necessidades específicas e preferências pessoais.

Não hesite em explorar todas as opções antes de tomar sua decisão final, mas considere {product['name']} como uma das principais alternativas em seu segmento.""",
        ]
        return random.choice(conclusions)
    
    def generate_article_eeat(self, product, data):
        """Gerar artigo completo com 1200+ palavras e foco em EEAT"""
        # Título otimizado para SEO
        title_variations = [
            f"{product['name']}: Análise Completa e Verificada por Especialistas",
            f"Vale a Pena {product['name']}? Análise Profunda e Honesta",
            f"{product['name']}: Guia Completo com Análise de Especialistas",
            f"{product['name']}: Tudo o que Você Precisa Saber (Análise Detalhada)",
            f"Análise Profissional: {product['name']} - Características, Vantagens e Desvantagens",
        ]
        title = random.choice(title_variations)
        
        # Montar artigo com foco em EEAT (Removido o # {title} para evitar duplicação no HTML)
        article = f"""**Última atualização**: {datetime.now().strftime('%d de %B de %Y')}

## Introdução

{self.get_expertise_intro(product, data)}

## O Que é {product['name']}?

{product['description']} 

{product['name']} é um {product['type'].lower()} que se posicionou como uma solução importante no mercado financeiro brasileiro. Nesta seção, explicaremos em detalhes o que é, como funciona e por que ganhou a confiança de milhares de usuários.

{product['name']} foi desenvolvido com o objetivo de atender às necessidades específicas de um público cada vez mais exigente e informado. A plataforma combina tecnologia moderna com uma abordagem focada no usuário, garantindo que cada aspecto da experiência seja pensado cuidadosamente.

Nos últimos anos, o produto tem evoluído constantemente, incorporando novas funcionalidades e melhorando seus serviços com base no feedback dos usuários. Esta dedicação à melhoria contínua é um dos fatores que o diferencia de seus concorrentes no mercado.

{self.get_expertise_features(product)}

## Vantagens de {product['name']}

As vantagens de escolher este produto são notáveis e bem documentadas:

"""
        
        for pro in product.get('pros', [])[:6]:
            variations = [
                f"✓ **{pro}** - Uma vantagem significativa que faz diferença real no dia a dia dos usuários.",
                f"✓ **{pro}** - Isso é particularmente importante para quem busca eficiência e praticidade.",
                f"✓ **{pro}** - Este é um diferencial que muitos usuários valorizam e destacam em suas avaliações.",
            ]
            article += random.choice(variations) + "\n"
        
        article += f"""
Estas vantagens não são apenas teóricas. Usuários reais relatam que experimentam benefícios tangíveis ao usar {product['name']}. A satisfação dos clientes é refletida nas avaliações positivas que o produto recebe regularmente em plataformas independentes.

Além disso, {product['name']} continua inovando para manter suas vantagens competitivas. A empresa está constantemente ouvindo feedback dos usuários e implementando melhorias que tornam o produto ainda mais atraente e funcional.

## Pontos de Atenção

Porém, como todo produto, existem alguns pontos que você deve considerar cuidadosamente:

"""
        
        for con in product.get('cons', [])[:5]:
            variations = [
                f"⚠ **{con}** - Algo que você deve levar em consideração antes de se comprometer.",
                f"⚠ **{con}** - Vale a pena avaliar se isso impacta significativamente você.",
                f"⚠ **{con}** - Este é um fator que pode influenciar sua decisão final.",
            ]
            article += random.choice(variations) + "\n"
        
        article += f"""
É importante notar que muitos destes pontos podem não ser relevantes para todos os usuários. Sua importância depende das suas necessidades específicas e do seu perfil como usuário.

A boa notícia é que {product['name']} está sempre trabalhando para minimizar estas limitações. A empresa tem demonstrado compromisso em resolver os problemas apontados pelos usuários através de atualizações regulares.

{self.get_trustworthiness_section(product)}

{self.get_experience_section(product)}

{self.get_authority_section(product, data)}

{self.get_detailed_comparison(product)}

{self.get_use_cases(product)}

## Análise de Avaliações e Reputação

Com uma avaliação de {product['rating']} estrelas e uma pontuação de {product['score']}% no nosso índice de confiabilidade, {product['name']} se destaca entre os concorrentes. Estes números refletem a satisfação de usuários reais que já utilizaram o serviço e compartilharam suas experiências honestas.

A reputação de um produto é construída ao longo do tempo através de interações consistentes e positivas com os usuários. {product['name']} tem demonstrado consistência em entregar o que promete, o que explica suas avaliações positivas em múltiplas plataformas independentes.

Análises independentes e revisões de especialistas confirmam que {product['name']} é uma escolha confiável para seus objetivos financeiros.

{self.get_conclusion_eeat(product)}

## Próximos Passos Recomendados

Se você se identificou com o que foi apresentado neste artigo e acredita que {product['name']} pode atender suas necessidades, recomendamos os seguintes passos:

1. **Visite o site oficial** de {product['name']} para obter informações mais recentes e conhecer as condições atuais
2. **Leia as avaliações** de usuários em plataformas independentes para confirmar nossa análise
3. **Entre em contato com o suporte** de {product['name']} para esclarecer dúvidas específicas sobre sua situação
4. **Compare com alternativas** para garantir que está fazendo a melhor escolha possível
5. **Consulte um especialista financeiro** se necessário para sua situação específica

Lembre-se de que a melhor escolha é aquela que se alinha perfeitamente com suas necessidades, objetivos financeiros e tolerância ao risco. Não hesite em explorar todas as opções antes de tomar sua decisão final.

---

**Informações do Produto:**
- **Avaliação**: {product['rating']}⭐ 
- **Pontuação de Confiabilidade**: {product['score']}%
- **Categoria**: {product.get('category', 'Geral')}
- **Tipo**: {product['type']}
- **Última Atualização**: {datetime.now().strftime('%d/%m/%Y às %H:%M')}

**Aviso Importante**: Este artigo foi preparado com base em pesquisa profissional e análise de dados. Sempre consulte um especialista financeiro antes de tomar decisões financeiras importantes. Os produtos mencionados podem incluir links de afiliados."""
        
        return title, article
    
    def generate_html_page(self, product, title, article):
        """Gerar página HTML estática para eliminar erros 404"""
        html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Análise completa de {product['name']} - {product['description']}">
    <meta name="keywords" content="{product['name']}, {product['type']}, {product.get('category', 'Financeiro')}, análise, comparação">
    <meta name="author" content="Radar Financeiro">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="Análise profissional e verificada de {product['name']}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://granahoje.github.io/radar/produto/{product['id']}/">
    <title>{title} | Radar Financeiro</title>
    <link rel="stylesheet" href="/radar/styles.css">
    <link rel="canonical" href="https://granahoje.github.io/radar/produto/{product['id']}/">
</head>
<body>
    <!-- HEADER -->
    <header>
        <div class="container">
            <div class="header-content">
                <div class="logo">📊 Radar Financeiro</div>
                <nav>
                    <a href="/radar/">Catálogo</a>
                    <a href="/radar/comparacao/">Comparar</a>
                    <a href="/radar/postagens.html">Postagens</a>
                </nav>
            </div>
        </div>
    </header>

    <!-- ARTICLE SECTION -->
    <article class="article-container">
        <div class="container">
            <div class="article-header">
                <h1>{title}</h1>
                <div class="article-meta">
                    <span class="category">{product.get('category', 'Geral')}</span>
                    <span class="rating">⭐ {product['rating']} ({product['score']}%)</span>
                    <span class="date">{self._get_pt_date()}</span>
                </div>
            </div>

            <div class="article-content">
                {self._markdown_to_html(article)}
            </div>

            <div class="article-cta" style="margin: 3rem 0; padding: 2rem; background: rgba(16, 185, 129, 0.1); border-radius: 1rem; border: 2px dashed var(--primary); text-align: center;">
                <h3 style="color: var(--primary); margin-bottom: 1rem;">🚀 Pronto para começar com {product['name']}?</h3>
                <p style="margin-bottom: 1.5rem;">Aproveite as condições especiais que encontramos para você através do nosso link oficial.</p>
                <a href="{product['affiliateLink']}" class="btn btn-primary btn-large" target="_blank" rel="noopener noreferrer" style="font-size: 1.25rem; padding: 1rem 2.5rem; animation: pulse 2s infinite;">
                    👉 ACESSAR SITE OFICIAL AGORA
                </a>
                <p style="font-size: 0.8rem; margin-top: 1rem; color: var(--text-tertiary);">* Você será redirecionado para a página oficial do produto em segurança.</p>
            </div>

            <div class="article-footer">
                <p><strong>Aviso Importante:</strong> Este artigo foi preparado com base em pesquisa profissional. Sempre consulte um especialista financeiro antes de tomar decisões financeiras.</p>
            </div>
        </div>
    </article>

    <!-- FOOTER -->
    <footer>
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>Sobre</h3>
                    <p>Radar Financeiro é uma plataforma de comparação e análise de produtos financeiros com conteúdo verificado por especialistas.</p>
                </div>
                <div class="footer-section">
                    <h3>Links Úteis</h3>
                    <ul>
                        <li><a href="/radar/">Catálogo</a></li>
                        <li><a href="/radar/comparacao/">Comparar</a></li>
                        <li><a href="/radar/postagens.html">Postagens</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 Radar Financeiro. Todos os direitos reservados.</p>
            </div>
        </div>
    </footer>

    <script src="/radar/app.js"></script>
</body>
</html>"""
        return html
    
    def _markdown_to_html(self, markdown_text):
        """Converter markdown simples para HTML de forma robusta"""
        import re
        
        # Substituir meses para português
        months = {
            'January': 'Janeiro', 'February': 'Fevereiro', 'March': 'Março',
            'April': 'Abril', 'May': 'Maio', 'June': 'Junho',
            'July': 'Julho', 'August': 'Agosto', 'September': 'Setembro',
            'October': 'Outubro', 'November': 'Novembro', 'December': 'Dezembro'
        }
        for eng, pt in months.items():
            markdown_text = markdown_text.replace(eng, pt)
            
        lines = markdown_text.split('\n')
        html_lines = []
        in_list = False
        
        for line in lines:
            line = line.strip()
            if not line:
                if in_list:
                    html_lines.append('</ul>')
                    in_list = False
                continue
            
            # Títulos
            if line.startswith('## '):
                if in_list:
                    html_lines.append('</ul>')
                    in_list = False
                html_lines.append(f'<h2>{line[3:]}</h2>')
            elif line.startswith('# '):
                if in_list:
                    html_lines.append('</ul>')
                    in_list = False
                # Ignorar H1 no corpo do artigo para evitar duplicação com o H1 do header da página
                continue
            
            # Listas
            elif line.startswith('- ') or line.startswith('✓ ') or line.startswith('⚠ ') or line.startswith('* '):
                if not in_list:
                    html_lines.append('<ul>')
                    in_list = True
                content = line[2:]
                # Negrito dentro da lista
                content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', content)
                html_lines.append(f'<li>{content}</li>')
            
            # Parágrafos normais
            else:
                if in_list:
                    html_lines.append('</ul>')
                    in_list = False
                # Negrito no parágrafo
                content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', line)
                html_lines.append(f'<p>{content}</p>')
        
        if in_list:
            html_lines.append('</ul>')
            
        return '\n'.join(html_lines)
    
    def _get_pt_date(self):
        """Obter data atual formatada em português"""
        now = datetime.now()
        months = {
            1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril',
            5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
            9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'
        }
        return f"{now.day} de {months[now.month]} de {now.year}"

    def generate_all_articles(self):
        """Gerar artigos para todos os produtos"""
        print("📝 Gerando artigos únicos com 1200+ palavras e foco em EEAT...")
        
        data = self.load_data()
        products = data['products']
        
        articles_generated = 0
        
        for product in products:
            title, article = self.generate_article_eeat(product, data)
            
            # Salvar artigo em Markdown
            filename = f"{product['id']}.md"
            filepath = os.path.join(self.content_dir, filename)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(article)
            
            # Adicionar link de afiliado no meio do conteúdo (após a seção "O Que é")
            affiliate_cta = f'\n\n<div class="inline-cta" style="margin: 2rem 0; padding: 1.5rem; background: rgba(16, 185, 129, 0.05); border-left: 5px solid var(--primary); border-radius: 0.5rem; border: 1px solid rgba(16, 185, 129, 0.1);">\n<h4 style="color: var(--primary); margin: 0 0 0.5rem 0;">🔥 Destaque: {product["name"]}</h4>\n<p style="margin: 0 0 1rem 0; font-size: 0.95rem;">{product["description"]}</p>\n<a href="{product["affiliateLink"]}" target="_blank" rel="noopener noreferrer" style="display: inline-block; font-weight: bold; color: var(--primary); text-decoration: none; border-bottom: 2px solid var(--primary);">Clique aqui para acessar o site oficial e conferir os detalhes &rarr;</a>\n</div>\n\n'
            
            # Inserir após a descrição do produto para melhor fluxo de leitura
            search_term = f"## O Que é {product['name']}?"
            if search_term in article:
                parts = article.split(search_term, 1)
                # Tentar inserir após o primeiro parágrafo da descrição
                article_with_cta = parts[0] + search_term + parts[1].replace("\n\n", "\n\n" + affiliate_cta, 1)
            else:
                article_with_cta = article + affiliate_cta

            # Gerar página HTML estática
            html = self.generate_html_page(product, title, article_with_cta)
            html_filepath = os.path.join(self.produto_dir, product['id'], 'index.html')
            os.makedirs(os.path.dirname(html_filepath), exist_ok=True)
            
            with open(html_filepath, 'w', encoding='utf-8') as f:
                f.write(html)
            
            # Contar palavras
            word_count = len(article.split())
            
            print(f"  ✓ {product['name']}: {word_count} palavras (HTML + Markdown)")
            articles_generated += 1
        
        print(f"\n✅ {articles_generated} artigos gerados com sucesso!")
        print(f"📁 Markdown: radar/content/")
        print(f"📁 HTML: radar/produto/[id]/index.html")
        
        return articles_generated

def main():
    generator = ContentGeneratorEEAT()
    generator.generate_all_articles()

if __name__ == '__main__':
    main()
