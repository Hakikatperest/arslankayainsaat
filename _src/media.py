# -*- coding: utf-8 -*-
"""img/ altındaki kaynak görsellerden w500/w900/w1600 WebP türevi + og:image üretir.
⚠️ cwebp varsayılanı (-m 6 -pass 10) KULLANILMIYOR — yavaş ve dosyayı büyütebiliyor;
   Pillow quality=80 method=6 (tek görsel, süre sorun değil). Kaynaklar img/ altında kalır, silinmez.
⚠️ Logo burada değil, _src/logo.py'de (parlama temizliği gerekiyor)."""
import os
from PIL import Image
KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GORSELLER = ["arslankaya-insaat-hizmet", "arslankaya-insaat", "arslankaya-insaat-hero"]
for ad in GORSELLER:
    kaynak = next(os.path.join(KOK, "img", ad + u) for u in (".webp", ".jpg", ".png")
                  if os.path.exists(os.path.join(KOK, "img", ad + u)))
    im = Image.open(kaynak).convert("RGB")
    for w in (500, 900, 1200, 1600, 1920):   # kaynaktan geniş türev üretilmez
        if w > im.width: continue
        os.makedirs(os.path.join(KOK, "images", f"w{w}"), exist_ok=True)
        im.resize((w, round(im.height * w / im.width)), Image.LANCZOS).save(
            os.path.join(KOK, "images", f"w{w}", ad + ".webp"), quality=80, method=6)
# ── Hizmet görselleri ──────────────────────────────────────────────────────
# 1) Kart: yuvarlak çerçeveye KARE kırpım (odak noktası data.HIZMET_GORSEL'de), 240/480 px.
#    Kart dairesi ~200px; tam görseli indirip CSS ile kırptırmak gereksiz bayt.
# 2) Sayfa içi vitrin: KIRPMASIZ w500/w900 (kaynaktan geniş türev üretilmez).
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import data as D
os.makedirs(os.path.join(KOK, "images", "kart"), exist_ok=True)
for slug, (kaynak_ad, _alt, (ox, oy)) in D.HIZMET_GORSEL.items():
    im = Image.open(os.path.join(KOK, "img", kaynak_ad + ".webp")).convert("RGB")
    ad = "bartin-" + slug
    k = min(im.size)
    x = min(max(round(im.width * ox - k / 2), 0), im.width - k)
    y = min(max(round(im.height * oy - k / 2), 0), im.height - k)
    kare = im.crop((x, y, x + k, y + k))
    for b in (240, 480):
        kare.resize((b, b), Image.LANCZOS).save(
            os.path.join(KOK, "images", "kart", f"{ad}-{b}.webp"), quality=72, method=6)
    for w in (500, 900):
        if w > im.width and w != 500: continue
        hedef = im if im.width <= w else im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
        os.makedirs(os.path.join(KOK, "images", f"w{w}"), exist_ok=True)
        hedef.save(os.path.join(KOK, "images", f"w{w}", ad + ".webp"), quality=80, method=6)

# ── Referans görselleri (panelden gelir: img/referans/<id>.webp) ────────────
# Yayın adı firma adından + id: bartin-<firma>-<id>-{480,900,1600}.webp. Eskiler silinir.
import json
from build_ortak import referans_dosya_adi
REF = json.load(open(os.path.join(KOK, "_src", "referanslar.json"), encoding="utf-8"))
ref_dizin = os.path.join(KOK, "images", "referans")
os.makedirs(ref_dizin, exist_ok=True)
gecerli = set()
for r in REF:
    if not r.get("gorunur"): continue       # gizli referansın türevi üretilmez (herkese açık olurdu)
    kaynak = os.path.join(KOK, "img", "referans", r["id"] + ".webp")
    if not os.path.exists(kaynak): continue
    ad = referans_dosya_adi(r)
    im = None
    for w in (480, 900, 1600):
        hedef = os.path.join(ref_dizin, f"{ad}-{w}.webp")
        gecerli.add(os.path.basename(hedef))
        if os.path.exists(hedef) and os.path.getmtime(hedef) >= os.path.getmtime(kaynak): continue
        im = im or Image.open(kaynak).convert("RGB")
        t = im if im.width <= w else im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
        t.save(hedef, quality=80, method=6)
for f in os.listdir(ref_dizin):
    if f not in gecerli: os.remove(os.path.join(ref_dizin, f))

# ── Çalışma alanı stok görselleri (img/stok/*.jpg) → bartin-<ad>-{500,900,1600}.webp ──
for _slug, liste in D.ALAN_GORSEL.items():
    for kaynak_ad, _alt, _uid in liste:
        im = Image.open(os.path.join(KOK, "img", "stok", kaynak_ad + ".jpg")).convert("RGB")
        for w in (500, 900, 1600):
            if w > im.width: continue
            os.makedirs(os.path.join(KOK, "images", f"w{w}"), exist_ok=True)
            (im if im.width == w else im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)).save(
                os.path.join(KOK, "images", f"w{w}", f"bartin-{kaynak_ad}.webp"), quality=78, method=6)

# Paylaşım görseli: genel marka görseli (hizmet listeli afiş değil). JPEG (bazı uygulamalar WebP og:image'ı göstermiyor), 1200 genişlik
im = Image.open(os.path.join(KOK, "img", "arslankaya-insaat.webp")).convert("RGB")
im.resize((1200, round(im.height * 1200 / im.width)), Image.LANCZOS).save(
    os.path.join(KOK, "images", "og-arslankaya-insaat.jpg"), quality=84, optimize=True, progressive=True)
print("türevler üretildi")
