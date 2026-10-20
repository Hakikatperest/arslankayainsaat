# -*- coding: utf-8 -*-
"""Logo türevleri + favicon — kaynak: img/arslankaya-insaat-logo.png (kullanıcı 2026-10-20 yükledi).

⚠️ Kaynak PNG'de yarı saydam BEYAZ PARLAMA + arkada bulanık "hayalet" logo kopyası var.
   Doğrudan basılırsa koyu zeminde kirli beyaz bulut, açık zeminde gri leke çıkıyor.
   Yalnız koyu lacivert (#181820) ve turuncu (#F84000→#F89000) pikseller maskeyle ayıklanıyor.
⚠️ İKİ VARYANT: koyu alt bilgide "ARSLANKAYA" yazısı ve koyu bloklar kayboluyor →
   `-ak` varyantında koyu pikseller beyaza çekiliyor, turuncu korunuyor.
⚠️ Favicon logonun SOL BLOĞUNDAN (binalar + çatı) — tam logo 48px'te okunmuyor.
   WebP DEĞİL png/ico (Google WebP favicon'u göstermiyor)."""
import os
import numpy as np
from PIL import Image, ImageFilter

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KAYNAK = os.path.join(KOK, "img", "arslankaya-insaat-logo.png")
CIKTI = os.path.join(KOK, "images", "logo")

def temizle():
    im = np.asarray(Image.open(KAYNAK).convert("RGBA")).astype(float)
    r, g, b, a = (im[..., i] for i in range(4))
    koyu = np.clip((90 - np.maximum(np.maximum(r, g), b)) / 40, 0, 1)
    tur = (np.clip((r - 195) / 30, 0, 1) * np.clip((95 - b) / 40, 0, 1)
           * np.clip((r - g - 45) / 30, 0, 1))
    m = np.maximum(koyu, tur) * np.clip((a - 150) / 60, 0, 1)
    maske = Image.fromarray((m * 255).astype("uint8")).filter(ImageFilter.MedianFilter(3))
    out = Image.fromarray(im.astype("uint8")); out.putalpha(maske)
    ys, xs = np.where(np.asarray(maske) > 128)
    out = out.crop((xs.min() - 4, ys.min() - 4, xs.max() + 5, ys.max() + 5))
    return out, (koyu > tur)

def ak_varyant(im):
    a = np.asarray(im).copy()
    r, g, b = a[..., 0].astype(int), a[..., 1].astype(int), a[..., 2].astype(int)
    koyu = (np.maximum(np.maximum(r, g), b) < 110) & ~((r - b) > 90)
    a[koyu, 0:3] = 255
    return Image.fromarray(a)

def main():
    os.makedirs(CIKTI, exist_ok=True)
    logo, _ = temizle()
    for ad, im in (("arslankaya-logo", logo), ("arslankaya-logo-ak", ak_varyant(logo))):
        for w in (240, 360, 520, 720):
            h = round(im.height * w / im.width)
            im.resize((w, h), Image.LANCZOS).save(os.path.join(CIKTI, f"{ad}-{w}.webp"),
                                                  quality=90, method=4)
    # İşaret: sol blok (binalar + çatı), oranla kırpılıyor
    # ⚠️ Çatı sağa doğru "A" harfinin ve "İNŞAAT" çizgisinin altına uzanıyor; dik kırpım
    #    onları da alıyordu. x>470'te çatı üst kenarının (315,215)→(590,400) ÜSTÜNDE
    #    kalan pikseller siliniyor (koordinatlar temizlenmiş 1788×429 görsele göre).
    isaret = logo.crop((0, 0, 600, logo.height))
    a = np.asarray(isaret).copy()
    yy, xx = np.mgrid[0:a.shape[0], 0:a.shape[1]]
    a[(xx > 470) & (yy < 215 + (xx - 315) * 0.672 - 6), 3] = 0
    isaret = Image.fromarray(a)
    bb = isaret.getbbox(); isaret = isaret.crop(bb)
    n = 512; kare = Image.new("RGBA", (n, n), (255, 255, 255, 255))
    olc = (n * 0.84) / max(isaret.size)
    i2 = isaret.resize((round(isaret.width * olc), round(isaret.height * olc)), Image.LANCZOS)
    kare.alpha_composite(i2, ((n - i2.width) // 2, (n - i2.height) // 2))
    img = os.path.join(KOK, "images")
    for b in (48, 96, 192):
        kare.resize((b, b), Image.LANCZOS).save(os.path.join(img, f"favicon-{b}.png"), optimize=True)
    kare.resize((180, 180), Image.LANCZOS).save(os.path.join(img, "apple-touch-icon.png"), optimize=True)
    kare.convert("RGB").save(os.path.join(KOK, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)])
    print("logo:", logo.size, "· favicon üretildi")

if __name__ == "__main__":
    main()
