import html
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

from Passw import generer_mot_de_passe

PAGE = """<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><title>Générateur de mot de passe</title><link rel="icon" href="data:,">
<style>
body{{font-family:system-ui,sans-serif;background:#f4f5f7;display:flex;justify-content:center;padding-top:80px}}
.card{{background:#fff;padding:32px;border-radius:12px;box-shadow:0 2px 12px #0001;width:420px}}
h1{{font-size:22px;margin-top:0}}
#pw{{font-family:monospace;font-size:18px;background:#eef;padding:12px;border-radius:8px;word-break:break-all}}
button{{padding:8px 16px;border:0;border-radius:6px;background:#3b5bdb;color:#fff;cursor:pointer}}
input{{width:60px;padding:6px}}
</style></head><body><div class="card">
<h1>Générateur de mot de passe</h1>
<form method="get">
<label>Longueur <input type="number" name="longueur" min="4" max="128" value="{longueur}"></label>
<button type="submit">Générer</button>
</form>
<p id="pw">{mot_de_passe}</p>
<button type="button" onclick="navigator.clipboard.writeText(document.getElementById('pw').textContent)">Copier</button>
</div></body></html>"""


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = urlparse(self.path)
        if url.path != "/":
            self.send_error(404)
            return
        try:
            longueur = max(4, min(128, int(parse_qs(url.query).get("longueur", ["16"])[0])))
        except ValueError:
            longueur = 16
        body = PAGE.format(longueur=longueur, mot_de_passe=html.escape(generer_mot_de_passe(longueur)))
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body.encode())


if __name__ == "__main__":
    ThreadingHTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
