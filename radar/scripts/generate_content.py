#!/usr/bin/env python3
"""
Gerador avançado de conteúdo
Cria artigos únicos com 800-1000+ palavras, estilo humano, sem parecer IA
"""

import json
import os
import random
from datetime import datetime

class ContentGenerator:
    def __init__(self):
        self.products_file = 'radar/data/products.json'
        self.cache_dir = 'radar/cache'
        self.content_dir = 'radar/content'
        os.makedirs(self.content_dir, exist_ok=True)
        
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
        
        if os.path.exists(os.path.join(self.cache_dir, 'rss_cache.json')):
            with open(os.path.join(self.cache_dir, 'rss_cache.json')) as f:
                data['rss'] = json.load(f)
        
        return data
    
    def get_intro_section(self, product, data):
        """Gerar introdução com 100+ palavras"""
        intros = [
            f"Você está buscando {product['type'].lower()} com as melhores condições? {product['name']} pode ser exatamente o que você procura. Neste artigo detalhado, vamos explorar em profundidade como este produto se destaca no mercado financeiro brasileiro e por que tantas pessoas escolhem confiar nele para suas necessidades financeiras. Analisaremos cada aspecto importante para ajudá-lo a tomar a melhor decisão possível.",
            
            f"Se você acompanha o mercado financeiro, já deve ter ouvido falar em {product['name']}. Mas você realmente sabe como este {product['type'].lower()} funciona e se é a melhor opção para você? Neste guia completo, vamos desvendar todos os detalhes importantes, desde as características básicas até os aspectos mais técnicos, para que você possa fazer uma escolha informada e segura.",
            
            f"No cenário financeiro atual, encontrar um bom {product['type'].lower()} é fundamental para atingir seus objetivos. {product['name']} tem se destacado como uma opção confiável e inovadora. Mas será que é realmente a melhor escolha para você? Vamos analisar profundamente este produto, comparando com alternativas e identificando exatamente para quem ele é mais adequado.",
        ]
        return random.choice(intros)
    
    def get_what_is_section(self, product):
        """Seção 'O que é' com 150+ palavras"""
        what_is = f"""{product['description']} Este {product['type'].lower()} tem se posicionado como uma solução importante no mercado financeiro brasileiro, atraindo a atenção de milhares de usuários que buscam alternativas confiáveis e eficientes.

{product['name']} foi desenvolvido com o objetivo de atender às necessidades específicas de um público cada vez mais exigente e informado. A plataforma combina tecnologia moderna com uma abordagem focada no usuário, garantindo que cada aspecto da experiência seja pensado cuidadosamente.

Nos últimos anos, o produto tem evoluído constantemente, incorporando novas funcionalidades e melhorando seus serviços com base no feedback dos usuários. Esta dedicação à melhoria contínua é um dos fatores que o diferencia de seus concorrentes no mercado."""
        return what_is
    
    def get_features_section(self, product):
        """Seção de características com 150+ palavras"""
        features_text = f"As principais características de {product['name']} incluem:\n\n"
        
        if product.get('features'):
            for i, feature in enumerate(product['features'][:5], 1):
                variations = [
                    f"• {feature}",
                    f"{i}. {feature}",
                    f"✓ {feature}",
                ]
                features_text += random.choice(variations) + "\n"
        
        features_text += f"""
Cada uma destas características foi cuidadosamente desenvolvida para oferecer a melhor experiência possível. {product['name']} investe constantemente em pesquisa e desenvolvimento para garantir que seus usuários tenham acesso às melhores ferramentas disponíveis no mercado.

A combinação destas funcionalidades cria um ecossistema completo que atende às necessidades dos usuários de forma integrada e eficiente. Isso significa que você não precisa buscar múltiplas plataformas para resolver seus problemas financeiros."""
        
        return features_text
    
    def get_advantages_section(self, product):
        """Seção de vantagens com 200+ palavras"""
        advantages_intros = [
            "As vantagens de escolher este produto são notáveis e bem documentadas:",
            "O que torna este produto atraente para os usuários é uma combinação de fatores:",
            "Os pontos positivos que destacam este produto incluem:",
            "Por que muitos brasileiros optam por este produto:",
        ]
        
        advantages_text = f"\n{random.choice(advantages_intros)}\n\n"
        
        for pro in product.get('pros', [])[:5]:
            variations = [
                f"• {pro} - Uma vantagem significativa que faz diferença no dia a dia dos usuários.",
                f"✓ {pro} - Isso é particularmente importante para quem busca eficiência e praticidade.",
                f"→ {pro} - Este é um diferencial que muitos usuários valorizam e destacam.",
            ]
            advantages_text += random.choice(variations) + "\n"
        
        advantages_text += f"""
Estas vantagens não são apenas teóricas. Usuários reais relatam que experimentam benefícios tangíveis ao usar {product['name']}. A satisfação dos clientes é refletida nas avaliações positivas que o produto recebe regularmente.

Além disso, {product['name']} continua inovando para manter suas vantagens competitivas. A empresa está constantemente ouvindo feedback dos usuários e implementando melhorias que tornam o produto ainda mais atraente."""
        
        return advantages_text
    
    def get_disadvantages_section(self, product):
        """Seção de desvantagens com 150+ palavras"""
        disadvantages_intros = [
            "Porém, como todo produto, existem alguns pontos a considerar:",
            "É importante também conhecer os desafios e limitações:",
            "Antes de decidir, considere estes aspectos importantes:",
            "Nenhum produto é perfeito. Aqui estão alguns pontos de atenção:",
        ]
        
        disadvantages_text = f"\n{random.choice(disadvantages_intros)}\n\n"
        
        for con in product.get('cons', [])[:5]:
            variations = [
                f"• {con} - Algo que você deve levar em consideração antes de se comprometer.",
                f"⚠ {con} - Vale a pena avaliar se isso impacta significativamente você.",
                f"→ {con} - Este é um fator que pode influenciar sua decisão final.",
            ]
            disadvantages_text += random.choice(variations) + "\n"
        
        disadvantages_text += f"""
É importante notar que muitos destes pontos podem não ser relevantes para todos os usuários. Sua importância depende das suas necessidades específicas e do seu perfil como usuário.

A boa notícia é que {product['name']} está sempre trabalhando para minimizar estas limitações. A empresa tem demonstrado compromisso em resolver os problemas apontados pelos usuários."""
        
        return disadvantages_text
    
    def get_market_context(self, product, data):
        """Contexto de mercado com 150+ palavras"""
        contexts = []
        
        if 'cripto' in product.get('category', '').lower():
            if data['crypto'].get('bitcoin'):
                btc = data['crypto']['bitcoin']
                contexts.append(
                    f"No contexto atual do mercado de criptomoedas, com Bitcoin em R$ {btc['preco']:,.0f} e variação de {btc['variacao_24h']:.2f}% nas últimas 24 horas, plataformas como {product['name']} ganham ainda mais relevância para quem deseja investir com segurança. O mercado de criptomoedas é volátil e exigente, e ter uma plataforma confiável é essencial. {product['name']} oferece as ferramentas necessárias para navegar este mercado complexo com confiança."
                )
        
        if 'moeda' in product.get('category', '').lower() or 'câmbio' in product.get('type', '').lower():
            if data['currencies'].get('dolar'):
                dolar = data['currencies']['dolar']
                contexts.append(
                    f"Com o dólar cotado em R$ {dolar['valor']:.2f} e variação de {dolar['variacao']:.2f}%, serviços como {product['name']} se tornam essenciais para quem precisa fazer transferências internacionais ou acompanhar o câmbio. Em um mundo cada vez mais globalizado, ter acesso a cotações precisas e transferências rápidas é fundamental. {product['name']} oferece ambos, com taxas competitivas e segurança garantida."
                )
        
        if 'investimento' in product.get('category', '').lower():
            if data['bcb'].get('cdi'):
                cdi = data['bcb']['cdi']
                contexts.append(
                    f"Com a taxa CDI em {cdi['taxa']:.4f}% ao dia, investidores buscam plataformas como {product['name']} que ofereçam rentabilidade competitiva e segurança comprovada. O cenário de investimentos no Brasil é dinâmico, com oportunidades surgindo constantemente. Ter uma plataforma que oferece acesso a estas oportunidades é crucial para maximizar seus retornos."
                )
        
        if 'empréstimo' in product.get('category', '').lower():
            contexts.append(
                f"No mercado de crédito atual, {product['name']} se destaca por oferecer condições acessíveis e processo de aprovação rápido, atendendo a uma demanda crescente por soluções de crédito ágeis e transparentes. Muitas pessoas precisam de crédito, mas não querem lidar com burocracia desnecessária. {product['name']} resolve este problema oferecendo um processo simplificado e transparente."
            )
        
        return random.choice(contexts) if contexts else ""
    
    def get_comparison_section(self, product):
        """Seção de comparação com 150+ palavras"""
        comparison = f"""Quando comparado com outras opções no mercado, {product['name']} oferece um equilíbrio interessante entre custo-benefício e funcionalidades. Enquanto alguns concorrentes podem oferecer recursos mais avançados, {product['name']} se destaca pela simplicidade e eficiência.

A análise comparativa mostra que {product['name']} é particularmente competitivo em:
- Facilidade de uso
- Suporte ao cliente
- Segurança e confiabilidade
- Transparência de taxas
- Velocidade de processamento

Muitos usuários escolhem {product['name']} justamente porque oferece o melhor equilíbrio entre estas características. Não é necessariamente o mais barato, mas oferece o melhor custo-benefício."""
        
        return comparison
    
    def get_who_should_use(self, product):
        """Seção 'Quem deveria usar' com 100+ palavras"""
        who_section = f"""{product['name']} é ideal para:

- Pessoas que buscam um {product['type'].lower()} confiável e seguro
- Usuários que valorizam segurança, transparência e facilidade de uso
- Aqueles que desejam uma experiência sem complicações ou burocracia desnecessária
- Profissionais que precisam de soluções ágeis e eficientes
- Iniciantes que estão começando sua jornada financeira
- Usuários experientes que buscam melhor custo-benefício

Se você se encaixa em qualquer uma destas categorias, {product['name']} pode ser exatamente o que você está procurando. O produto foi desenvolvido pensando em diferentes perfis de usuários."""
        
        return who_section
    
    def get_conclusion(self, product):
        """Conclusão com 150+ palavras"""
        conclusions = [
            f"""Em resumo, {product['name']} apresenta-se como uma opção sólida no mercado de {product['type'].lower()}. Com suas características bem definidas, reputação estabelecida e compromisso contínuo com a melhoria, é uma escolha que merece consideração se você busca um {product['type'].lower()} confiável e eficiente.

A decisão de escolher {product['name']} deve levar em conta suas necessidades específicas, seu perfil como usuário e seus objetivos financeiros. Se os pontos positivos superam os negativos para sua situação particular, então é definitivamente uma opção a explorar.

Lembre-se de que a melhor escolha é aquela que se alinha perfeitamente com suas necessidades e expectativas. Não hesite em explorar todas as opções antes de tomar sua decisão final.""",
            
            f"""Concluindo, se você está em busca de um {product['type'].lower()} que combine segurança, eficiência e bom atendimento, {product['name']} é definitivamente uma opção a ser explorada. A decisão final dependerá de suas necessidades específicas e preferências pessoais.

O importante é que você tenha todas as informações necessárias para fazer uma escolha informada. Este artigo forneceu uma análise abrangente de {product['name']}, seus pontos fortes e seus desafios. Com estas informações em mãos, você está bem equipado para tomar a melhor decisão para sua situação.

Recomendamos que você visite o site oficial de {product['name']} para obter informações mais recentes e conhecer as condições atuais.""",
        ]
        return random.choice(conclusions)
    
    def generate_article(self, product, data):
        """Gerar artigo completo com 800+ palavras"""
        # Título
        title_variations = [
            f"{product['name']}: Análise Completa e Opinião Sincera",
            f"Vale a Pena {product['name']}? Descubra Agora",
            f"{product['name']}: O Que Você Precisa Saber",
            f"Guia Completo: {product['name']} em Detalhes",
            f"{product['name']}: Tudo o que Você Precisa Saber",
        ]
        title = random.choice(title_variations)
        
        # Montar artigo
        article = f"""# {title}

## Introdução

{self.get_intro_section(product, data)}

## O Que é {product['name']}?

{self.get_what_is_section(product)}

## Características Principais

{self.get_features_section(product)}

## Vantagens de {product['name']}

{self.get_advantages_section(product)}

## Pontos de Atenção

{self.get_disadvantages_section(product)}

## Contexto de Mercado

{self.get_market_context(product, data)}

## Avaliação e Reputação

Com uma avaliação de {product['rating']} estrelas e uma pontuação de {product['score']}% no nosso índice de confiabilidade, {product['name']} se destaca entre os concorrentes. Estes números refletem a satisfação de usuários reais que já utilizaram o serviço e compartilharam suas experiências.

A reputação de um produto é construída ao longo do tempo através de interações consistentes e positivas com os usuários. {product['name']} tem demonstrado consistência em entregar o que promete, o que explica suas avaliações positivas.

## Comparação com Concorrentes

{self.get_comparison_section(product)}

## Quem Deveria Usar?

{self.get_who_should_use(product)}

## Análise Detalhada

{product['name']} oferece uma proposta de valor clara e bem definida. Para usuários que buscam exatamente o que este produto oferece, ele representa uma excelente escolha. A combinação de funcionalidades, segurança e facilidade de uso o torna competitivo no mercado.

A empresa por trás de {product['name']} tem demonstrado compromisso com a inovação e a satisfação do cliente. Isso é evidente nas melhorias contínuas que o produto recebe e na forma como a empresa responde ao feedback dos usuários.

## Conclusão

{self.get_conclusion(product)}

## Próximos Passos

Se você se identificou com o que foi apresentado neste artigo, recomendamos que visite o site oficial de {product['name']} para obter mais informações e conhecer as condições atuais. Lembre-se de que a melhor escolha é aquela que se alinha com suas necessidades específicas e objetivos financeiros.

Não hesite em entrar em contato com o suporte de {product['name']} se tiver dúvidas. A equipe está disponível para ajudá-lo a tomar a melhor decisão.

---

**Publicado em**: {datetime.now().strftime('%d de %B de %Y')}
**Atualizado em**: {datetime.now().strftime('%H:%M:%S')}
**Avaliação**: {product['rating']}⭐ | Pontuação: {product['score']}%
**Categoria**: {product.get('category', 'Geral')}
"""
        
        return title, article
    
    def generate_all_articles(self):
        """Gerar artigos para todos os produtos"""
        print("📝 Gerando artigos únicos com 800+ palavras...")
        
        data = self.load_data()
        products = data['products']
        
        articles_generated = 0
        
        for product in products:
            title, article = self.generate_article(product, data)
            
            # Salvar artigo
            filename = f"{product['id']}.md"
            filepath = os.path.join(self.content_dir, filename)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(article)
            
            # Contar palavras
            word_count = len(article.split())
            
            print(f"  ✓ {product['name']}: {word_count} palavras")
            articles_generated += 1
        
        print(f"\n✅ {articles_generated} artigos gerados com sucesso!")
        print(f"📁 Localização: radar/content/")
        
        return articles_generated

def main():
    generator = ContentGenerator()
    generator.generate_all_articles()

if __name__ == '__main__':
    main()
