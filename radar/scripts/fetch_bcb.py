#!/usr/bin/env python3
"""
Buscar dados reais do Banco Central do Brasil
CDI, SELIC, inflação, taxas oficiais
"""

import json
import requests
from datetime import datetime, timedelta

class BCBFetcher:
    def __init__(self):
        self.base_url = "https://www.bcb.gov.br/api/dados/v1"
        self.cache_file = "radar/cache/bcb_cache.json"
        
    def fetch_selic(self):
        """Buscar taxa SELIC atual"""
        try:
            # API do Banco Central para SELIC
            url = f"{self.base_url}/ultimasTaxas/selic"
            response = requests.get(url, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                return {
                    'taxa': data.get('taxa', 0),
                    'data': datetime.now().isoformat(),
                    'fonte': 'Banco Central'
                }
        except Exception as e:
            print(f"⚠️ Erro ao buscar SELIC: {e}")
        
        return None
    
    def fetch_cdi(self):
        """Buscar taxa CDI atual"""
        try:
            # CDI é calculado a partir da SELIC
            # Usar API alternativa
            url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.12/dados/ultimos/1?formato=json"
            response = requests.get(url, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                if data:
                    return {
                        'taxa': float(data[0]['valor']),
                        'data': data[0]['data'],
                        'fonte': 'Banco Central'
                    }
        except Exception as e:
            print(f"⚠️ Erro ao buscar CDI: {e}")
        
        return None
    
    def fetch_inflacao(self):
        """Buscar inflação (IPCA)"""
        try:
            # IPCA - Índice de Preços ao Consumidor Amplo
            url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados/ultimos/1?formato=json"
            response = requests.get(url, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                if data:
                    return {
                        'taxa': float(data[0]['valor']),
                        'data': data[0]['data'],
                        'fonte': 'Banco Central'
                    }
        except Exception as e:
            print(f"⚠️ Erro ao buscar inflação: {e}")
        
        return None
    
    def fetch_taxa_media_poupanca(self):
        """Buscar taxa média de poupança"""
        try:
            url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.196/dados/ultimos/1?formato=json"
            response = requests.get(url, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                if data:
                    return {
                        'taxa': float(data[0]['valor']),
                        'data': data[0]['data'],
                        'fonte': 'Banco Central'
                    }
        except Exception as e:
            print(f"⚠️ Erro ao buscar taxa poupança: {e}")
        
        return None
    
    def fetch_all(self):
        """Buscar todos os dados"""
        print("📊 Buscando dados do Banco Central...")
        
        data = {
            'timestamp': datetime.now().isoformat(),
            'selic': self.fetch_selic(),
            'cdi': self.fetch_cdi(),
            'inflacao': self.fetch_inflacao(),
            'poupanca': self.fetch_taxa_media_poupanca()
        }
        
        return data
    
    def save_cache(self, data):
        """Salvar cache local"""
        import os
        os.makedirs('radar/cache', exist_ok=True)
        
        with open(self.cache_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Cache do Banco Central salvo")

def main():
    fetcher = BCBFetcher()
    data = fetcher.fetch_all()
    fetcher.save_cache(data)
    
    # Exibir dados
    print("\n📈 Dados do Banco Central:")
    print(f"  SELIC: {data['selic']['taxa'] if data['selic'] else 'N/A'}%")
    print(f"  CDI: {data['cdi']['taxa'] if data['cdi'] else 'N/A'}%")
    print(f"  Inflação (IPCA): {data['inflacao']['taxa'] if data['inflacao'] else 'N/A'}%")
    print(f"  Poupança: {data['poupanca']['taxa'] if data['poupanca'] else 'N/A'}%")

if __name__ == '__main__':
    main()
