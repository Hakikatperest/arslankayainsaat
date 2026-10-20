# -*- coding: utf-8 -*-
"""Commit ÖNCESİ çalıştır: python3 _src/denetim.py  (hata varsa 1 döner)."""
import os, re, sys, json, glob, collections
KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
YASAK = ["en iyi", "lider", "bir numara", "1 numara", "en güvenilir", "en ucuz", "garantili",
         "7/24", "sigortalı", "yıllık tecrübe", "yılı aşkın"]   # teyitsiz iddialar
hata, uyari = [], []
sayfalar = {}
for f in glob.glob(os.path.join(KOK, "**", "*.html"), recursive=True):
    if "/_src/" in f or "/img/" in f: continue
    yol = "/" + os.path.relpath(f, KOK).replace("index.html", "")
    sayfalar[yol] = open(f, encoding="utf-8").read()
basliklar = collections.Counter(); aciklamalar = collections.Counter()
for yol, h in sayfalar.items():
    t = re.search(r"<title>(.*?)</title>", h).group(1)
    d = re.search(r'<meta name="description" content="(.*?)">', h).group(1)
    basliklar[t] += 1; aciklamalar[d] += 1
    if len(t) > 65: uyari.append(f"{yol}: title {len(t)} kr")
    if not 100 <= len(d) <= 170: uyari.append(f"{yol}: description {len(d)} kr")
    if h.count("<h1") != 1: hata.append(f"{yol}: {h.count('<h1')} adet H1")
    gorunur = re.sub(r"<script.*?</script>|<[^>]+>", " ", h, flags=re.S).lower()
    for y in YASAK:
        if y in gorunur: hata.append(f"{yol}: yasak/teyitsiz ifade '{y}'")
    for blok in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
        try: json.loads(blok)
        except Exception as ex: hata.append(f"{yol}: JSON-LD bozuk ({ex})")
    for u in set(re.findall(r'href="(/[^"#?]*)"', h)):
        if u.startswith("/assets") or u.startswith("/images") or u in ("/favicon.ico",): 
            if not os.path.exists(os.path.join(KOK, u.lstrip("/"))): hata.append(f"{yol}: eksik dosya {u}")
            continue
        if u not in sayfalar: hata.append(f"{yol}: kırık iç link {u}")
    for s in re.findall(r'src(?:set)?="([^"]+)"', h):
        for p in re.findall(r"(/(?:images|assets)/[^\s,?\"]+)", s):
            if not os.path.exists(os.path.join(KOK, p.lstrip("/"))): hata.append(f"{yol}: eksik görsel {p}")
for t, n in basliklar.items():
    if n > 1: hata.append(f"mükerrer title ({n}): {t}")
for d, n in aciklamalar.items():
    if n > 1: hata.append(f"mükerrer description ({n}): {d[:60]}…")
print(f"{len(sayfalar)} sayfa denetlendi · {len(hata)} hata · {len(uyari)} uyarı")
for x in sorted(set(hata)): print("  HATA ", x)
for x in sorted(set(uyari)): print("  uyarı", x)
sys.exit(1 if hata else 0)
