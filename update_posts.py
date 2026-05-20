import urllib.request, json, base64

token = "TOKEN_REMOVIDO"
repo = "granahoje/granahoje.github.io"

sha1 = "d03c93ae30e1a0155d50cd772bb2cc474e100cc8"
sha2 = "d03c93ae30e1a0155d50cd772bb2cc474e100cc8"

def upload(path, sha, content):
    url = f"https://api.github.com/repos/{repo}/contents/{path}"
    data = json.dumps({"message": f"Update {path}", "content": base64.b64encode(content.encode()).decode(), "sha": sha}).encode()
    req = urllib.request.Request(url, data=data, method="PUT")
    req.add_header("Authorization", f"token {token}")
    req.add_header("Content-Type", "application/json")
    urllib.request.urlopen(req)
    print(f"OK: {path}")

html1 = open("novos_posts/mineracao-dados-mobile-etica.html").read()
html2 = open("novos_posts/venda-digital-assets-ia.html").read()

upload("novos_posts/mineracao-dados-mobile-etica.html", sha1, html1)
upload("novos_posts/venda-digital-assets-ia.html", sha2, html2)
