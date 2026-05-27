#!/usr/bin/env python3
"""
Script para gerar conteúdo automático com IA (OpenAI)
Gera descrições, análises, prós e contras para cada produto
"""

import json
import os
import sys
from datetime import datetime

try:
    import openai
except ImportError:
    print("❌ Erro: openai não está instalado. Execute: pip install openai")
    sys.exit(1)

# Configurar API Key
openai.api_key = os.getenv('OPENAI_API_KEY')

if not openai.api_key:
    print("❌ Erro: OPENAI_API_KEY não configurada")
    sys.exit(1)

def load_products():
    """Carregar produtos do arquivo JSON"""
    try:
        with open('radar/data/products.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ Erro: arquivo products.json não encontrado")
        sys.exit(1)

def generate_description(product_name, product_type):
    """Gerar descrição do produto com IA"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "Você é um especialista em produtos financeiros. Gere descrições concisas e profissionais."
                },
                {
                    "role": "user",
                    "content": f"Gere uma descrição profissional de 1-2 linhas para o produto financeiro: {product_name} ({product_type}). Seja conciso e destacue o principal benefício."
                }
            ],
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"⚠️ Erro ao gerar descrição para {product_name}: {e}")
        return None

def generate_pros_cons(product_name, product_type):
    """Gerar prós e contras do produto"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "Você é um especialista em análise de produtos financeiros. Gere listas concisas de prós e contras."
                },
                {
                    "role": "user",
                    "content": f"""Para o produto financeiro: {product_name} ({product_type})
                    
Gere uma resposta em JSON com este formato:
{{
  "pros": ["pró 1", "pró 2", "pró 3"],
  "cons": ["contra 1", "contra 2"]
}}

Seja conciso e realista."""
                }
            ],
            max_tokens=300,
            temperature=0.7
        )
        
        try:
            content = response.choices[0].message.content.strip()
            # Extrair JSON da resposta
            start = content.find('{')
            end = content.rfind('}') + 1
            if start >= 0 and end > start:
                return json.loads(content[start:end])
        except:
            pass
        
        return {"pros": [], "cons": []}
    except Exception as e:
        print(f"⚠️ Erro ao gerar prós/contras para {product_name}: {e}")
        return {"pros": [], "cons": []}

def update_products():
    """Atualizar produtos com conteúdo gerado"""
    data = load_products()
    products = data['products']
    
    print(f"📝 Gerando conteúdo para {len(products)} produtos...")
    
    updated_count = 0
    for i, product in enumerate(products, 1):
        print(f"  [{i}/{len(products)}] {product['name']}...", end=" ", flush=True)
        
        # Gerar descrição se não existir ou estiver vazia
        if not product.get('description') or len(product.get('description', '')) < 20:
            desc = generate_description(product['name'], product['type'])
            if desc:
                product['description'] = desc
                print("✓", end="")
        
        # Gerar prós e contras se vazios
        if not product.get('pros') or len(product.get('pros', [])) == 0:
            analysis = generate_pros_cons(product['name'], product['type'])
            if analysis:
                product['pros'] = analysis.get('pros', [])
                product['cons'] = analysis.get('cons', [])
                print("✓", end="")
        
        print()
        updated_count += 1
    
    # Salvar produtos atualizados
    with open('radar/data/products.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ {updated_count} produtos atualizados com sucesso!")
    print(f"📅 Última atualização: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == '__main__':
    update_products()
