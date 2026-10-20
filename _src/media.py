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
# Paylaşım görseli: genel marka görseli (hizmet listeli afiş değil). JPEG (bazı uygulamalar WebP og:image'ı göstermiyor), 1200 genişlik
im = Image.open(os.path.join(KOK, "img", "arslankaya-insaat.webp")).convert("RGB")
im.resize((1200, round(im.height * 1200 / im.width)), Image.LANCZOS).save(
    os.path.join(KOK, "images", "og-arslankaya-insaat.jpg"), quality=84, optimize=True, progressive=True)
print("türevler üretildi")
