#!/usr/bin/env python3
"""
Orquestrador principal - executa todos os scripts de atualização
Busca dados reais, calcula scores e atualiza o site
"""

import subprocess
import sys
import os
from datetime import datetime

class RadarOrchestrator:
    def __init__(self):
        self.scripts = [
            ('fetch_bcb.py', 'Banco Central'),
            ('fetch_crypto.py', 'Criptomoedas'),
            ('fetch_currencies.py', 'Moedas'),
            ('fetch_rss.py', 'Notícias'),
            ('calculate_scores.py', 'Scores'),
            ('generate_content_eeat.py', 'Conteúdo EEAT 1200+ palavras'),
            ('generate_posts_index.py', 'Índice de Postagens'),
            ('generate_rss_fixed.py', 'RSS Feed'),
            ('generate_sitemap_fixed.py', 'Sitemap'),
        ]
        
    def run_script(self, script_name, description):
        """Executar um script individual"""
        print(f"\n{'='*60}")
        print(f"▶️  {description}")
        print(f"{'='*60}")
        
        max_retries = 3
        for attempt in range(1, max_retries + 1):
            try:
                print(f"   (Tentativa {attempt}/{max_retries})")
                script_path = os.path.join('radar/scripts', script_name)
                result = subprocess.run([sys.executable, script_path], capture_output=False)
                
                if result.returncode == 0:
                    print(f"✅ {description} concluído")
                    return True
                else:
                    print(f"⚠️ Erro em {description} (Retorno: {result.returncode})")
            except Exception as e:
                print(f"⚠️ Erro ao executar {description}: {e}")
            
            if attempt < max_retries:
                import time
                time.sleep(5) # Esperar antes de tentar novamente
        
        print(f"❌ {description} falhou após {max_retries} tentativas. Continuando com o próximo...")
        return False
    
    def run_all(self):
        """Executar todos os scripts"""
        print(f"\n{'='*60}")
        print(f"🤖 RADAR FINANCEIRO - ATUALIZAÇÃO AUTOMÁTICA")
        print(f"{'='*60}")
        print(f"📅 Início: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        results = {}
        
        for script, description in self.scripts:
            results[description] = self.run_script(script, description)
        
        # Resumo
        print(f"\n{'='*60}")
        print(f"📊 RESUMO DA ATUALIZAÇÃO")
        print(f"{'='*60}")
        
        success_count = sum(1 for v in results.values() if v)
        total_count = len(results)
        
        for description, success in results.items():
            status = "✅" if success else "❌"
            print(f"{status} {description}")
        
        print(f"\n📈 Resultado: {success_count}/{total_count} scripts executados com sucesso")
        print(f"📅 Fim: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        if success_count == total_count:
            print(f"\n🎉 ATUALIZAÇÃO COMPLETA COM SUCESSO!")
            return True
        else:
            print(f"\n⚠️  Alguns scripts falharam, mas o site foi parcialmente atualizado")
            return success_count > 0

def main():
    orchestrator = RadarOrchestrator()
    success = orchestrator.run_all()
    
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
