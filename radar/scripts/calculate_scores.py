#!/usr/bin/env python3
"""
Calcular scores reais baseados em dados concretos
Fórmula: Score = (Cashback + Rendimento + Popularidade + Atualização) - Taxas
"""

import json
import os
from datetime import datetime

class ScoreCalculator:
    def __init__(self):
        self.products_file = 'radar/data/products.json'
        self.cache_dir = 'radar/cache'
        
    def load_products(self):
        """Carregar produtos"""
        with open(self.products_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def load_cache_data(self):
        """Carregar dados do cache"""
        cache_data = {
            'bcb': {},
            'crypto': {},
            'currencies': {},
            'rss': {}
        }
        
        # Carregar BCB
        bcb_file = os.path.join(self.cache_dir, 'bcb_cache.json')
        if os.path.exists(bcb_file):
            with open(bcb_file, 'r') as f:
                cache_data['bcb'] = json.load(f)
        
        # Carregar Crypto
        crypto_file = os.path.join(self.cache_dir, 'crypto_cache.json')
        if os.path.exists(crypto_file):
            with open(crypto_file, 'r') as f:
                cache_data['crypto'] = json.load(f)
        
        # Carregar Currencies
        curr_file = os.path.join(self.cache_dir, 'currencies_cache.json')
        if os.path.exists(curr_file):
            with open(curr_file, 'r') as f:
                cache_data['currencies'] = json.load(f)
        
        # Carregar RSS
        rss_file = os.path.join(self.cache_dir, 'rss_cache.json')
        if os.path.exists(rss_file):
            with open(rss_file, 'r') as f:
                cache_data['rss'] = json.load(f)
        
        return cache_data
    
    def calculate_rendimento_score(self, product, cache_data):
        """Calcular score de rendimento"""
        score = 0
        
        # Contas de investimento
        if 'investimento' in product.get('category', '').lower():
            # Usar CDI como base
            if cache_data['bcb'].get('cdi'):
                cdi = cache_data['bcb']['cdi'].get('taxa', 0)
                score = min(100, cdi * 10)  # Normalizar
        
        # Criptomoedas
        elif 'cripto' in product.get('category', '').lower():
            if cache_data['crypto'].get('top_10'):
                # Calcular variação média
                variacoes = [c.get('variacao_24h', 0) for c in cache_data['crypto']['top_10']]
                media_variacao = sum(variacoes) / len(variacoes) if variacoes else 0
                score = max(0, min(100, 50 + media_variacao * 2))
        
        return score
    
    def calculate_popularidade_score(self, product, cache_data):
        """Calcular score de popularidade baseado em notícias"""
        score = 50  # Score base
        
        # Contar menções em notícias
        mentions = 0
        product_name = product.get('name', '').lower()
        
        if cache_data['rss'].get('feeds'):
            for source, news in cache_data['rss']['feeds'].items():
                for item in news:
                    if product_name in item.get('titulo', '').lower():
                        mentions += 1
        
        # Aumentar score com menções
        score = min(100, 50 + mentions * 10)
        
        return score
    
    def calculate_atualizacao_score(self, product):
        """Score de atualização recente"""
        # Produtos atualizados recentemente ganham mais pontos
        return 10
    
    def calculate_taxa_penalty(self, product):
        """Penalidade por taxas altas"""
        penalty = 0
        
        # Simular penalidade baseada em tipo de produto
        product_type = product.get('type', '').lower()
        
        if 'taxa' in product_type or 'juros' in product_type:
            penalty = 15
        elif 'empréstimo' in product_type:
            penalty = 10
        
        return penalty
    
    def calculate_score(self, product, cache_data):
        """Calcular score final"""
        rendimento = self.calculate_rendimento_score(product, cache_data)
        popularidade = self.calculate_popularidade_score(product, cache_data)
        atualizacao = self.calculate_atualizacao_score(product)
        taxa_penalty = self.calculate_taxa_penalty(product)
        
        # Fórmula: Score = (Rendimento + Popularidade + Atualização) - Taxas
        score = (rendimento + popularidade + atualizacao) / 3 - taxa_penalty
        
        # Normalizar entre 50 e 100
        score = max(50, min(100, score))
        
        return round(score, 1)
    
    def update_all_scores(self):
        """Atualizar scores de todos os produtos"""
        print("🔢 Calculando scores reais...")
        
        data = self.load_products()
        cache_data = self.load_cache_data()
        
        products = data['products']
        
        for product in products:
            old_score = product.get('score', 75)
            new_score = self.calculate_score(product, cache_data)
            
            product['score'] = new_score
            
            if abs(new_score - old_score) > 1:
                print(f"  {product['name']}: {old_score}% → {new_score}%")
        
        # Salvar produtos atualizados
        with open(self.products_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Scores atualizados com sucesso!")
        
        return data

def main():
    calculator = ScoreCalculator()
    calculator.update_all_scores()

if __name__ == '__main__':
    main()
