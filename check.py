"""Check unico da vitrine estatica. Roda: python3 check.py."""
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
html = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()

assert "NUMERO_WHATSAPP =" in html, "constante NUMERO_WHATSAPP ausente"
assert html.count("NUMERO_WHATSAPP =") == 1, "constante NUMERO_WHATSAPP duplicada"
assert "encodeURIComponent" in html, "texto WhatsApp sem encodeURIComponent"
assert "wa.me" in html, "link wa.me ausente"
assert "fetch(" not in html, "fetch() quebra em file://"
for bad in ("TODO", "TBD", "lorem"):
    assert bad.lower() not in html.lower(), "placeholder " + bad + " no HTML"
for m in re.finditer(r"<a[^>]*>", html):
    tag = m.group(0)
    if "wa-link" in tag:
        assert "data-msg" in tag, "wa-link sem data-msg: " + tag
imgs = re.findall(r'<img[^>]+src="([^"]+)"', re.sub(r"<!--.*?-->", "", html, flags=re.S))
for src in imgs:
    assert src.startswith("fotos/"), "img fora de fotos/: " + src
    assert os.path.exists(os.path.join(ROOT, src)), "foto ausente: " + src
assert os.path.isdir(os.path.join(ROOT, "fotos")), "pasta fotos/ ausente"
print("OK: index.html integro; imgs checadas:", len(imgs))
