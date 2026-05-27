#!/usr/bin/env python3
"""
Buscar dados reais de criptomoedas da CoinGecko
Bitcoin, Ethereum, top criptos, market cap
"""

import json
import requests
from datetime import datetime

class CryptoFetcher:
    def __init__(self):
        self.base_url = "https://api.coingecko.com/api/v3"
        self.cache_file = "radar/cache/crypto_cache.json"
        
    def fetch_top_cryptos(self, limit=10):
        """Buscar top criptomoedas por market cap"""
        try:
            url = f"{self.base_url}/coins/markets"
            params = {
                'vs_currency': 'brl',
                'order': 'market_cap_desc',
                'per_page': limit,
                'page': 1,
                'sparkline': False
            }
            
            response = requests.get(url, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                cryptos = []
                
                for coin in data:
                    cryptos.append({
                        'nome': coin['name'],
                        'simbolo': coin['symbol'].upper(),
                        'preco': coin['current_price'],
                        'market_cap': coin['market_cap'],
                        'variacao_24h': coin['price_change_percentage_24h'],
                        'volume_24h': coin['total_volume'],
                        'data': datetime.now().isoformat()
                    })
                
                return cryptos
        except Exception as e:
            print(f"⚠️ Erro ao buscar criptos: {e}")
        
        return []
    
    def fetch_bitcoin_data(self):
        """Buscar dados específicos do Bitcoin"""
        try:
            url = f"{self.base_url}/coins/bitcoin"
            params = {
                'vs_currency': 'brl',
                'include_market_data': True
            }
            
            response = requests.get(url, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                return {
                    'nome': 'Bitcoin',
                    'simbolo': 'BTC',
                    'preco': data['market_data']['current_price']['brl'],
                    'market_cap': data['market_data']['market_cap']['brl'],
                    'volume_24h': data['market_data']['total_volume']['brl'],
                    'variacao_24h': data['market_data']['price_change_percentage_24h'],
                    'ath': data['market_data']['ath']['brl'],
                    'atl': data['market_data']['atl']['brl'],
                    'data': datetime.now().isoformat()
                }
        except Exception as e:
            print(f"⚠️ Erro ao buscar Bitcoin: {e}")
        
        return None
    
    def fetch_ethereum_data(self):
        """Buscar dados específicos do Ethereum"""
        try:
            url = f"{self.base_url}/coins/ethereum"
            params = {
                'vs_currency': 'brl',
                'include_market_data': True
            }
            
            response = requests.get(url, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                return {
                    'nome': 'Ethereum',
                    'simbolo': 'ETH',
                    'preco': data['market_data']['current_price']['brl'],
                    'market_cap': data['market_data']['market_cap']['brl'],
                    'volume_24h': data['market_data']['total_volume']['brl'],
                    'variacao_24h': data['market_data']['price_change_percentage_24h'],
                    'ath': data['market_data']['ath']['brl'],
                    'atl': data['market_data']['atl']['brl'],
                    'data': datetime.now().isoformat()
                }
        except Exception as e:
            print(f"⚠️ Erro ao buscar Ethereum: {e}")
        
        return None
    
    def fetch_all(self):
        """Buscar todos os dados de cripto"""
        print("₿ Buscando dados de criptomoedas...")
        
        data = {
            'timestamp': datetime.now().isoformat(),
            'bitcoin': self.fetch_bitcoin_data(),
            'ethereum': self.fetch_ethereum_data(),
            'top_10': self.fetch_top_cryptos(10)
        }
        
        return data
    
    def save_cache(self, data):
        """Salvar cache local"""
        import os
        os.makedirs('radar/cache', exist_ok=True)
        
        with open(self.cache_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Cache de criptos salvo")

def main():
    fetcher = CryptoFetcher()
    data = fetcher.fetch_all()
    fetcher.save_cache(data)
    
    # Exibir dados
    print("\n💰 Dados de Criptomoedas:")
    if data['bitcoin']:
        print(f"  Bitcoin: R$ {data['bitcoin']['preco']:,.2f}")
        print(f"  Variação 24h: {data['bitcoin']['variacao_24h']:.2f}%")
    
    if data['ethereum']:
        print(f"  Ethereum: R$ {data['ethereum']['preco']:,.2f}")
        print(f"  Variação 24h: {data['ethereum']['variacao_24h']:.2f}%")
    
    print(f"\n  Top 10 criptos: {len(data['top_10'])} encontradas")

if __name__ == '__main__':
    main()
