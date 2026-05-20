import requests, json

links = [
    "https://apretailer.com.br/click/6a0bab802bfa817b4557a492/188471/358980/subaccount",
    "https://apretailer.com.br/click/6a0bab802bfa817b6c7f4032/188459/358980/subaccount",
    "https://apretailer.com.br/click/6a0bab802bfa817b723762f2/188414/358980/subaccount",
    "https://apretailer.com.br/click/6a0bab802bfa817b650fa492/188415/358980/subaccount",
    "https://apretailer.com.br/click/6a0bab802bfa817b57502472/188413/358980/subaccount",
    "https://apretailer.com.br/click/6a0bab802bfa817b517e54d2/188400/358980/subaccount",
    "https://apretailer.com.br/click/6a0bab802bfa817b5e071672/186226/358980/subaccount",
    "https://apretailer.com.br/click/6a0bab802bfa817b7f1a79b2/188286/358980/subaccount",
    "https://apretailer.com.br/click/6a0bab802bfa817b783708b2/188130/358980/subaccount",
    "https://apretailer.com.br/click/6a0bab802bfa817b8555f8d2/188136/358980/subaccount",
    "https://apretailer.com.br/click/6a0bab802bfa817b8c14a912/182687/358980/subaccount",
    "https://apretailer.com.br/click/6a0bab802bfa817b9272f8a2/187944/358980/subaccount",
    "https://apretailer.com.br/click/6a0bab802bfa817b98549fd2/187799/358980/subaccount",
    "https://apretailer.com.br/click/6a0bab802bfa817b9e6d0122/188544/358980/subaccount",
    "https://apretailer.com.br/click/6a0bab802bfa817bb6494802/188543/358980/subaccount",
    "https://apretailer.com.br/click/6a0bab802bfa817bc8530a72/187745/358980/subaccount",
    "https://apretailer.com.br/click/6a0bab802bfa817bb04d2b72/188352/358980/subaccount",
    "https://apretailer.com.br/click/6a0bab802bfa81398f1142c2/182268/358980/subaccount",
    "https://apretailer.com.br/click/6a0bab802bfa8139414ad4b3/184731/358980/subaccount",
    "https://apretailer.com.br/click/6a0bab802bfa81394d4c4542/184515/358980/subaccount",
    "https://apretailer.com.br/click/6a0bab802bfa8139047c0493/184363/358980/subaccount",
    "https://apretailer.com.br/click/6a0bab802bfa8139047c0492/177702/358980/subaccount",
    "https://apretailer.com.br/click/6a0bab802bfa8139352802e2/179925/358980/subaccount"
]

results = []
for url in links:
    try:
        r = requests.get(url, allow_redirects=True, timeout=10)
        results.append({"aff_url": url, "final_url": r.url})
        print(f"Resolved: {url} -> {r.url}")
    except Exception as e:
        print(f"Error resolving {url}: {e}")

with open('resolved_links.json', 'w') as f:
    json.dump(results, f, indent=2)
