# -*- coding: utf-8 -*-
"""build.py ve media.py'nin ortak kullandığı küçük yardımcılar."""
import re

def kucuk(s):
    """⚠️ Python .lower() 'İ'yi 'i̇' yapıyor. Türkçe güvenli küçültme."""
    return s.replace("I", "ı").replace("İ", "i").lower()

def sluglastir(s):
    k = kucuk(s)
    for a, b in (("ç","c"),("ğ","g"),("ı","i"),("ö","o"),("ş","s"),("ü","u"),("â","a"),("î","i"),("û","u")):
        k = k.replace(a, b)
    return re.sub(r"[^a-z0-9]+", "-", k).strip("-")

def referans_dosya_adi(r):
    """SEO dostu yayın adı: bartin-<firma>-<id> (id çakışmayı önler, firma adı değişince ad da değişir)."""
    return f"bartin-{(sluglastir(r['firma'])[:50].strip('-') or 'referans')}-{r['id']}"
