#!/usr/bin/env python3
"""
Buscar dados reais de moedas da AwesomeAPI
Dólar, Euro, Bitcoin, moedas
"""

import json
import requests
from datetime import datetime

class CurrencyFetcher:
    def __init__(self):
        self.base_url = "https://economia.awesomeapi.com.br"
        self.cache_file = "radar/cache/currencies_cache.json"
        
    def fetch_dollar(self):
        """Buscar cotação do dólar"""
        try:
            url = f"{self.base_url}/json/last/USD-BRL"
            response = requests.get(url, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                usd = data['USDBRL']
                return {
                    'moeda': 'USD',
                    'nome': 'Dólar Americano',
                    'valor': float(usd['bid']),
                    'variacao': float(usd['pctChange']),
                    'timestamp': usd['timestamp'],
                    'data': datetime.now().isoformat()
                }
        except Exception as e:
            print(f"⚠️ Erro ao buscar dólar: {e}")
        
        return None
    
    def fetch_euro(self):
        """Buscar cotação do euro"""
        try:
            url = f"{self.base_url}/json/last/EUR-BRL"
            response = requests.get(url, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                eur = data['EURBRL']
                return {
                    'moeda': 'EUR',
                    'nome': 'Euro',
                    'valor': float(eur['bid']),
                    'variacao': float(eur['pctChange']),
                    'timestamp': eur['timestamp'],
                    'data': datetime.now().isoformat()
                }
        except Exception as e:
            print(f"⚠️ Erro ao buscar euro: {e}")
        
        return None
    
    def fetch_bitcoin_price(self):
        """Buscar preço do Bitcoin em BRL"""
        try:
            url = f"{self.base_url}/json/last/BTC-BRL"
            response = requests.get(url, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                btc = data['BTCBRL']
                return {
                    'moeda': 'BTC',
                    'nome': 'Bitcoin',
                    'valor': float(btc['bid']),
                    'variacao': float(btc['pctChange']),
                    'timestamp': btc['timestamp'],
                    'data': datetime.now().isoformat()
                }
        except Exception as e:
            print(f"⚠️ Erro ao buscar Bitcoin: {e}")
        
        return None
    
    def fetch_all_currencies(self):
        """Buscar múltiplas moedas"""
        try:
            url = f"{self.base_url}/json/all"
            response = requests.get(url, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                currencies = {}
                
                # Extrair principais moedas
                for key in ['USDBRL', 'EURBRL', 'GBPBRL', 'JPYBRL', 'AUDBRL']:
                    if key in data:
                        currency_data = data[key]
                        currencies[key] = {
                            'valor': float(currency_data['bid']),
                            'variacao': float(currency_data['pctChange']),
                            'timestamp': currency_data['timestamp']
                        }
                
                return currencies
        except Exception as e:
            print(f"⚠️ Erro ao buscar moedas: {e}")
        
        return {}
    
    def fetch_all(self):
        """Buscar todos os dados de moedas"""
        print("💱 Buscando dados de moedas...")
        
        data = {
            'timestamp': datetime.now().isoformat(),
            'dolar': self.fetch_dollar(),
            'euro': self.fetch_euro(),
            'bitcoin': self.fetch_bitcoin_price(),
            'todas': self.fetch_all_currencies()
        }
        
        return data
    
    def save_cache(self, data):
        """Salvar cache local"""
        import os
        os.makedirs('radar/cache', exist_ok=True)
        
        with open(self.cache_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Cache de moedas salvo")

def main():
    fetcher = CurrencyFetcher()
    data = fetcher.fetch_all()
    fetcher.save_cache(data)
    
    # Exibir dados
    print("\n💰 Cotações de Moedas:")
    if data['dolar']:
        print(f"  Dólar: R$ {data['dolar']['valor']:.2f}")
        print(f"  Variação: {data['dolar']['variacao']:.2f}%")
    
    if data['euro']:
        print(f"  Euro: R$ {data['euro']['valor']:.2f}")
        print(f"  Variação: {data['euro']['variacao']:.2f}%")
    
    if data['bitcoin']:
        print(f"  Bitcoin: R$ {data['bitcoin']['valor']:,.2f}")
        print(f"  Variação: {data['bitcoin']['variacao']:.2f}%")

if __name__ == '__main__':
    main()
