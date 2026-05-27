#!/usr/bin/env python3
"""
Script para gerar imagens automáticas com IA (DALL-E)
Gera ilustrações para cada produto financeiro
"""

import json
import os
import sys
import requests
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

def generate_image_prompt(product_name, product_type):
    """Gerar prompt para geração de imagem"""
    prompts = {
        "Conta Bancária": f"Professional financial banking app icon for {product_name}, modern design, green and blue colors, minimalist style",
        "Empréstimo": f"Money lending icon for {product_name}, professional design, financial theme, green accent",
        "Cartão de Crédito": f"Credit card illustration for {product_name}, modern design, elegant, financial theme",
        "Exchange de Criptomoedas": f"Cryptocurrency exchange icon for {product_name}, modern tech design, blockchain theme",
        "Plataforma de Investimentos": f"Investment platform icon for {product_name}, professional design, growth theme",
        "Máquina de Cartão": f"Payment terminal illustration for {product_name}, modern design, business theme",
        "Remessa Internacional": f"International money transfer icon for {product_name}, global theme, professional design",
        "Antecipação de FGTS": f"FGTS advance service icon for {product_name}, professional financial design",
        "Consultoria Fiscal": f"Tax consulting icon for {product_name}, professional design, financial theme",
        "Pagamento de Boletos": f"Bill payment service icon for {product_name}, professional design"
    }
    
    return prompts.get(product_type, f"Professional icon for {product_name}, financial theme, modern design")

def generate_image(product_name, product_type):
    """Gerar imagem com DALL-E"""
    try:
        prompt = generate_image_prompt(product_name, product_type)
        
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="256x256",
            quality="standard"
        )
        
        image_url = response['data'][0]['url']
        return image_url
    except Exception as e:
        print(f"⚠️ Erro ao gerar imagem para {product_name}: {e}")
        return None

def download_image(url, filename):
    """Baixar imagem de URL"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        with open(filename, 'wb') as f:
            f.write(response.content)
        
        return True
    except Exception as e:
        print(f"⚠️ Erro ao baixar imagem: {e}")
        return False

def update_product_images():
    """Atualizar imagens dos produtos"""
    data = load_products()
    products = data['products']
    
    # Criar diretório de imagens se não existir
    images_dir = 'radar/images'
    os.makedirs(images_dir, exist_ok=True)
    
    print(f"🖼️  Gerando imagens para {len(products)} produtos...")
    print("⚠️  Nota: Geração de imagens pode levar alguns minutos...")
    
    generated_count = 0
    for i, product in enumerate(products, 1):
        # Pular se já tem imagem
        if product.get('image'):
            print(f"  [{i}/{len(products)}] {product['name']}... ⏭️  (já existe)")
            continue
        
        print(f"  [{i}/{len(products)}] {product['name']}...", end=" ", flush=True)
        
        # Gerar imagem
        image_url = generate_image(product['name'], product['type'])
        if not image_url:
            print("❌")
            continue
        
        # Salvar imagem localmente
        image_filename = f"{product['id']}.png"
        image_path = os.path.join(images_dir, image_filename)
        
        if download_image(image_url, image_path):
            product['image'] = image_filename
            generated_count += 1
            print("✓")
        else:
            print("❌")
    
    # Salvar produtos atualizados
    with open('radar/data/products.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ {generated_count} imagens geradas com sucesso!")
    print(f"📅 Última atualização: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == '__main__':
    update_product_images()
