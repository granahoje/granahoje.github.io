import urllib.request, json, base64

token = "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"
repo = "granahoje/granahoje.github.io"

def upload(path, content):
    url = f"https://api.github.com/repos/{repo}/contents/{path}"
    data = json.dumps({"message": f"Add {path}", "content": base64.b64encode(content.encode()).decode()}).encode()
    req = urllib.request.Request(url, data=data, method="PUT")
    req.add_header("Authorization", f"token {token}")
    req.add_header("Content-Type", "application/json")
    try:
        urllib.request.urlopen(req)
        print(f"OK: {path}")
    except Exception as e:
        print(f"ERRO: {e}")

upload("novos_posts/mineracao-dados-mobile-etica.html", "<h1>teste</h1>")
upload("novos_posts/venda-digital-assets-ia.html", "<h1>teste</h1>")
