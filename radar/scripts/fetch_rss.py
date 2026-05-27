#!/usr/bin/env python3
"""
Buscar notícias financeiras de RSS feeds
InfoMoney, Exame, Valor Econômico
"""

import json
import requests
from datetime import datetime
from xml.etree import ElementTree as ET

class RSSFetcher:
    def __init__(self):
        self.cache_file = "radar/cache/rss_cache.json"
        self.feeds = {
            'infomoney': 'https://www.infomoney.com.br/feed/',
            'exame': 'https://exame.com/feed/',
            'valor': 'https://valor.globo.com/google/amp/rss.xml'
        }
        
    def fetch_feed(self, feed_url, source_name):
        """Buscar e parsear feed RSS"""
        try:
            response = requests.get(feed_url, timeout=10)
            
            if response.status_code == 200:
                root = ET.fromstring(response.content)
                items = []
                
                # Encontrar items do feed
                for item in root.findall('.//item')[:10]:  # Pegar top 10
                    title_elem = item.find('title')
                    link_elem = item.find('link')
                    pubdate_elem = item.find('pubDate')
                    desc_elem = item.find('description')
                    
                    if title_elem is not None:
                        items.append({
                            'titulo': title_elem.text or '',
                            'link': link_elem.text if link_elem is not None else '',
                            'data': pubdate_elem.text if pubdate_elem is not None else '',
                            'descricao': desc_elem.text[:200] if desc_elem is not None else '',
                            'fonte': source_name
                        })
                
                return items
        except Exception as e:
            print(f"⚠️ Erro ao buscar {source_name}: {e}")
        
        return []
    
    def categorize_news(self, title):
        """Categorizar notícia por tipo"""
        title_lower = title.lower()
        
        if any(word in title_lower for word in ['bitcoin', 'cripto', 'blockchain', 'ethereum']):
            return 'criptomoedas'
        elif any(word in title_lower for word in ['bolsa', 'ibovespa', 'ação', 'ações']):
            return 'bolsa'
        elif any(word in title_lower for word in ['dólar', 'moeda', 'câmbio']):
            return 'cambio'
        elif any(word in title_lower for word in ['selic', 'cdi', 'taxa', 'juros']):
            return 'taxas'
        elif any(word in title_lower for word in ['banco', 'financeiro', 'crédito']):
            return 'financeiro'
        else:
            return 'geral'
    
    def fetch_all(self):
        """Buscar notícias de todos os feeds"""
        print("📰 Buscando notícias financeiras...")
        
        all_news = {
            'timestamp': datetime.now().isoformat(),
            'feeds': {}
        }
        
        for source, url in self.feeds.items():
            print(f"  Buscando {source}...", end=" ", flush=True)
            news = self.fetch_feed(url, source)
            
            # Categorizar notícias
            for item in news:
                item['categoria'] = self.categorize_news(item['titulo'])
            
            all_news['feeds'][source] = news
            print(f"✓ ({len(news)} notícias)")
        
        return all_news
    
    def save_cache(self, data):
        """Salvar cache local"""
        import os
        os.makedirs('radar/cache', exist_ok=True)
        
        with open(self.cache_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Cache de notícias salvo")
    
    def generate_summary(self, data):
        """Gerar resumo das notícias"""
        summary = {
            'total_noticias': 0,
            'por_categoria': {},
            'ultimas_noticias': []
        }
        
        for source, news in data['feeds'].items():
            summary['total_noticias'] += len(news)
            
            for item in news:
                categoria = item.get('categoria', 'geral')
                if categoria not in summary['por_categoria']:
                    summary['por_categoria'][categoria] = 0
                summary['por_categoria'][categoria] += 1
                
                if len(summary['ultimas_noticias']) < 5:
                    summary['ultimas_noticias'].append({
                        'titulo': item['titulo'],
                        'categoria': categoria,
                        'fonte': source
                    })
        
        return summary

def main():
    fetcher = RSSFetcher()
    data = fetcher.fetch_all()
    fetcher.save_cache(data)
    
    # Gerar resumo
    summary = fetcher.generate_summary(data)
    
    print("\n📊 Resumo de Notícias:")
    print(f"  Total: {summary['total_noticias']} notícias")
    print(f"  Por categoria:")
    for cat, count in summary['por_categoria'].items():
        print(f"    - {cat}: {count}")
    
    print(f"\n  Últimas notícias:")
    for news in summary['ultimas_noticias']:
        print(f"    - {news['titulo'][:60]}... ({news['fonte']})")

if __name__ == '__main__':
    main()
