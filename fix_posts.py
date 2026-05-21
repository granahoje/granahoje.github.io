import urllib.request, json, base64

token = "TOKEN_REMOVIDO"
repo = "granahoje/granahoje.github.io"

def get_sha(path):
    url = f"https://api.github.com/repos/{repo}/contents/{path}"
    req = urllib.request.Request(url)
    req.add_header("Authorization", f"token {token}")
    return json.loads(urllib.request.urlopen(req).read())["sha"]

def upload(path, content):
    sha = get_sha(path)
    url = f"https://api.github.com/repos/{repo}/contents/{path}"
    data = json.dumps({"message": f"Update {path}", "content": base64.b64encode(content.encode("utf-8")).decode(), "sha": sha}).encode()
    req = urllib.request.Request(url, data=data, method="PUT")
    req.add_header("Authorization", f"token {token}")
    req.add_header("Content-Type", "application/json")
    urllib.request.urlopen(req)
    print(f"OK: {path}")

h = open("/data/data/com.termux/files/home/granahoje.github.io/artigos/mineracao-dados-mobile-etica.html").read()
upload("artigos/mineracao-dados-mobile-etica.html", h)
upload("artigos/venda-digital-assets-ia.html", h)
