# -*- coding: utf-8 -*-
"""
arslankayainsaat.com üreticisi (desen: /root/dehaiskele/_src/build.py).

⛔ Üretilen HTML'i ELLE DÜZENLEME — bu betik her çalıştığında üzerine yazar.
   Metin ve veri değişikliği `data.py`'ye yapılır.

Çalıştırma:  python3 _src/build.py
Denetim:     python3 _src/denetim.py   (commit ÖNCESİ, hatada 1 döner)
"""
import os, re, sys, html, hashlib, json
from urllib.parse import quote

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import data as D

S = D.SITE
ALAN = S["alan"]
HIZ = {h["slug"]: h for h in D.HIZMETLER}

# GitHub Pages CSS/JS'i max-age=600 ile servis ediyor; ?v=md5 damgası şart.
_surum = {}
def surum(yol):
    if yol not in _surum:
        try:
            h = hashlib.md5(open(os.path.join(KOK, yol.lstrip("/")), "rb").read()).hexdigest()[:8]
        except FileNotFoundError:
            h = "0"
        _surum[yol] = f"{yol}?v={h}"
    return _surum[yol]

def e(t):
    return html.escape(str(t), quote=True)

def kirp(metin, en_az=110, en_cok=165):
    m = " ".join(metin.split())
    if len(m) > en_cok:
        kes = m[:en_cok]
        kes = kes[:kes.rfind(" ")] if " " in kes else kes
        m = kes.rstrip(" ,;:.") + "."
    return m

def kucuk(s):
    """⚠️ Python .lower() 'İ'yi 'i̇' yapıyor (birleşen nokta). Türkçe güvenli küçültme."""
    return s.replace("I", "ı").replace("İ", "i").lower()

# ── İkonlar ─────────────────────────────────────────────────────────────────
# ⚠️ Satır içi SVG'lere HER ZAMAN width/height ver: CSS gelmezse 300×150 olur.
def svg(yol, boy=18, dolu=False):
    if dolu:
        return (f'<svg viewBox="0 0 24 24" width="{boy}" height="{boy}" aria-hidden="true" '
                f'fill="currentColor">{yol}</svg>')
    return (f'<svg viewBox="0 0 24 24" width="{boy}" height="{boy}" aria-hidden="true" fill="none" '
            f'stroke="currentColor" stroke-width="1.7" stroke-linecap="round" '
            f'stroke-linejoin="round">{yol}</svg>')

def svg_tel():
    return svg('<path d="M6.6 10.8a15.1 15.1 0 006.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.2.4 2.4.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1C10.8 21 3 13.2 3 3.6c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.4 0 .8-.2 1l-2.3 2.6z"/>', dolu=True)

def svg_wa():
    return svg('<path d="M12 2a10 10 0 00-8.6 15L2 22l5.2-1.4A10 10 0 1012 2zm0 18a8 8 0 01-4.1-1.1l-.3-.2-3 .8.8-2.9-.2-.3A8 8 0 1112 20zm4.4-5.8c-.2-.1-1.4-.7-1.6-.8-.2-.1-.4-.1-.5.1l-.7.9c-.1.2-.3.2-.5.1a6.5 6.5 0 01-3.2-2.8c-.1-.2 0-.4.1-.5l.4-.5c.1-.2.1-.3 0-.5l-.7-1.6c-.2-.4-.4-.4-.5-.4h-.5c-.2 0-.5.1-.7.3a3 3 0 00-.9 2.2c0 1.3.9 2.5 1.1 2.7 1.3 2 2.8 2.9 4.6 3.4 1.1.3 1.7.3 2.2.2.6-.1 1.4-.6 1.6-1.2.2-.6.2-1.1.1-1.2 0-.1-.2-.2-.4-.3z"/>', dolu=True)

def svg_konum():
    return svg('<path d="M12 21s-7-6.2-7-11.5A7 7 0 0119 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>', 16)

IKON = {
    "bina":   '<path d="M4 21V8l8-5 8 5v13"/><path d="M9 21v-6h6v6"/><path d="M8 10h2M14 10h2"/><path d="M2 21h20"/>',
    "kolon":  '<path d="M3 21h18"/><path d="M5 21V5M12 21V5M19 21V5"/><path d="M3 5h18"/><path d="M3 12h18"/>',
    "mala":   '<path d="M14 4l6 6-8.5 8.5H5.5v-6z"/><path d="M5.5 18.5L3 21"/><path d="M11 7l6 6"/>',
    "anahtar":'<path d="M14.7 6.3a4 4 0 00-5.4 5.4L3 18v3h3l6.3-6.3a4 4 0 005.4-5.4l-2.5 2.5-2.5-.5-.5-2.5z"/>',
    "cati":   '<path d="M2 12L12 4l10 8"/><path d="M5 10v10h14V10"/><path d="M8 20v-5h8v5"/>',
    "rulo":   '<rect x="3" y="3" width="15" height="6" rx="1.5"/><path d="M18 6h3v5h-9v3"/><rect x="10.5" y="14" width="3" height="7" rx="1"/>',
    "karo":   '<rect x="3" y="3" width="8" height="8" rx="1"/><rect x="13" y="3" width="8" height="8" rx="1"/><rect x="3" y="13" width="8" height="8" rx="1"/><rect x="13" y="13" width="8" height="8" rx="1"/>',
    "cephe":  '<rect x="4" y="3" width="16" height="18" rx="1"/><path d="M8 7h2M14 7h2M8 11h2M14 11h2M8 15h2M14 15h2"/>',
    "katman": '<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/><path d="M3 17.5l9 4.5 9-4.5" opacity=".6"/>',
    "demir":  '<path d="M3 7h18M3 12h18M3 17h18"/><path d="M7 4v16M17 4v16"/>',
    "tugla":  '<rect x="3" y="4" width="18" height="16" rx="1"/><path d="M3 9.3h18M3 14.6h18"/><path d="M12 4v5.3M7.5 9.3v5.3M16.5 9.3v5.3M12 14.6V20"/>',
    "yikim":  '<path d="M14 3l7 7-3 3-7-7z"/><path d="M11 6L3 14l3 3 8-8"/><path d="M4 21h8"/><path d="M15 17l2 2M18 15l2 2"/>',
    "kapi":   '<path d="M5 21V4a1 1 0 011-1h12a1 1 0 011 1v17"/><path d="M3 21h18"/><circle cx="15" cy="12" r="1"/>',
    "ev":     '<path d="M3 11l9-7 9 7"/><path d="M5 9.5V20h14V9.5"/><path d="M10 20v-6h4v6"/>',
    "kamu":   '<path d="M3 9l9-5 9 5"/><path d="M5 10v8M9.5 10v8M14.5 10v8M19 10v8"/><path d="M3 20h18"/>',
    "dukkan": '<path d="M4 9l1.5-5h13L20 9"/><path d="M4 9a2.7 2.7 0 005.3 0 2.7 2.7 0 005.4 0A2.7 2.7 0 0020 9"/><path d="M5 11v9h14v-9"/><path d="M10 20v-5h4v5"/>',
    "site":   '<rect x="2.5" y="8" width="7" height="13" rx="1"/><rect x="9.5" y="3" width="7" height="18" rx="1"/><rect x="16.5" y="11" width="5" height="10" rx="1"/>',
}
def ikon(ad, boy=36):
    return svg(IKON[ad], boy)

# ── Görseller ───────────────────────────────────────────────────────────────
GENISLIKLER = (500, 900, 1200, 1600)
def gorsel(taban, alt, boy="100vw", oncelik=False):
    """_src/media.py türevlerinden srcset'li <picture>. Türev yoksa BOŞ döner."""
    kaynak = [(g, f"/images/w{g}/{taban}.webp") for g in GENISLIKLER
              if os.path.exists(os.path.join(KOK, "images", f"w{g}", taban + ".webp"))]
    if not kaynak:
        return ""
    from PIL import Image
    with Image.open(os.path.join(KOK, kaynak[-1][1].lstrip("/"))) as im:
        w, h = im.size
    yukle = ' loading="eager" fetchpriority="high"' if oncelik else ' loading="lazy" decoding="async"'
    yedek = next((y for g, y in kaynak if g == 900), kaynak[-1][1])
    return (f'<picture><img src="{yedek}" srcset="{", ".join(f"{y} {g}w" for g, y in kaynak)}" '
            f'sizes="{boy}" alt="{e(alt)}" width="{w}" height="{h}"{yukle}></picture>')

# ⚠️ Alt metin görselin GÖSTERDİĞİNİ anlatır (dosya adını değil); anahtar kelime doldurma yok.
AFIS_ALT = ("Arslankaya İnşaat tanıtım afişi: Bartın'da anahtar teslim inşaat hizmetleri "
            "listesi, çalışma alanları, modern iki katlı villa ve baret görseli, Celal ve "
            "Kurtuluş Arslankaya'nın telefonları ile Bartın Merkez adresi")

def afis_bolum(baslik="Hizmetlerimiz Bir Bakışta", giris=None):
    """Kullanıcının 2026-10-20'de verdiği tanıtım afişi (img/arslankaya-insaat-hizmet.webp).
    ⚠️ KIRPMA YOK ve üstüne yazı/perde BİNMEZ: afişin alt şeridinde telefon ve adres var,
       dehaiskele'deki .vitrin-ara bindirmesi onu örtüyordu → arama düğmesi görselin ALTINDA.
    ⚠️ Afişteki metin görselde; aynı bilgiler sayfada HTML olarak da var (SEO değeri orada)."""
    g = gorsel("arslankaya-insaat-hizmet", AFIS_ALT, boy="(min-width:1220px) 1180px, 100vw")
    if not g:
        return ""
    gr = f'<p class="giris">{e(giris)}</p>' if giris else ""
    return f"""<section class="bol afis"><div class="kap">
  <div class="bol-bas"><h2>{e(baslik)}</h2>{gr}</div>
  <a class="afis-kutu" href="tel:{S['tel_link']}" aria-label="{e(S['marka'])} — hemen ara: {e(S['tel'])}">{g}</a>
  <div class="dg-grup afis-dg">{tel_btn()}{tel2_btn("dg dg-hat2")}{wa_btn()}</div>
</div></section>"""

# ── Marka ───────────────────────────────────────────────────────────────────
def logo(koyu_zemin=False, buyuk=False):
    """Gerçek logo (img/arslankaya-insaat-logo.png → _src/logo.py türevleri).
    ⚠️ Alt bilgi AÇIK zeminli (dehaiskele CSS'i) → orada da normal logo. `-ak` varyantı
       (koyu harfler beyaza çekilmiş) yalnız koyu zemine konacak yerler için hazır."""
    ad = "arslankaya-logo-ak" if koyu_zemin else "arslankaya-logo"
    kaynak = ", ".join(f"/images/logo/{ad}-{w}.webp {w}w" for w in (240, 360, 520, 720))
    # Üstteki logo ilk ekranda → yüksek öncelik; alt bilgideki lazy.
    yukle = 'loading="lazy" decoding="async"' if buyuk else 'fetchpriority="high"'
    olcu = "300px" if buyuk else "(min-width:860px) 226px, 184px"
    return (f'<span class="logo"><img src="/images/logo/{ad}-360.webp" srcset="{kaynak}" '
            f'sizes="{olcu}" width="360" height="86" alt="{e(S["marka"])} logosu — Bartın inşaat firması" '
            f'class="logo-im" {yukle}></span>')

MENU = [
    ("/", "Ana Sayfa"),
    ("/hakkimizda/", "Hakkımızda"),
    ("/hizmetlerimiz/", "Hizmetlerimiz"),
    ("/calisma-alanlari/", "Çalışma Alanları"),
    ("/iletisim/", "İletişim"),
]

def head(baslik, aciklama, yol, schema=""):
    kanonik = ALAN + yol
    ac = kirp(aciklama)
    return f"""<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(baslik)}</title>
<meta name="description" content="{e(ac)}">
<link rel="canonical" href="{e(kanonik)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{e(S['marka'])}">
<meta property="og:title" content="{e(baslik)}">
<meta property="og:description" content="{e(ac)}">
<meta property="og:url" content="{e(kanonik)}">
<meta property="og:locale" content="tr_TR">
<meta property="og:image" content="{ALAN}/images/og-arslankaya-insaat.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="675">
<meta property="og:image:alt" content="{e(S['marka'])} tanıtım görseli">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#171a22">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" href="/images/favicon-48.png" sizes="48x48">
<link rel="apple-touch-icon" href="/images/apple-touch-icon.png">
<link rel="preload" href="/assets/fonts/pjs-var-tr.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{surum('/assets/style.css')}">
<script>document.documentElement.classList.add('js')</script>
{schema}
</head>
<body>
<a class="atla" href="#ana">İçeriğe geç</a>
"""

def wa_link(mesaj="Merhaba, inşaat işi için bilgi almak istiyorum."):
    return f'https://wa.me/{S["wa"]}?text={quote(mesaj)}'

def tel_btn(sinif="dg dg-sari", metin=None):
    return (f'<a class="{sinif}" href="tel:{S["tel_link"]}">{svg_tel()}'
            f'<span>{e(metin or S["tel"])}</span></a>')

def tel2_btn(sinif="dg dg-hat2", metin=None):
    return (f'<a class="{sinif}" href="tel:{S["tel2_link"]}">{svg_tel()}'
            f'<span>{e(metin or S["tel2"])}</span></a>')

def wa_btn(mesaj="Merhaba, inşaat işi için bilgi almak istiyorum.", sinif="dg dg-wa"):
    return (f'<a class="{sinif}" href="{wa_link(mesaj)}" target="_blank" rel="noopener">'
            f'{svg_wa()}<span>WhatsApp</span></a>')

def teklif_btn(sinif="dg dg-teklif", konu="inşaat işi"):
    """Statik site, form yok — WhatsApp'a hazır mesajla gidiyor."""
    return (f'<a class="{sinif}" href="{wa_link(f"Merhaba, {konu} için teklif almak istiyorum.")}" '
            f'target="_blank" rel="noopener"><span>Teklif Al</span>'
            f'<svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true" fill="none" '
            f'stroke="currentColor" stroke-width="2.4" stroke-linecap="round">'
            f'<path d="M7 17L17 7M8 7h9v9"/></svg></a>')

def ust_serit():
    return f"""<div class="ust-serit">
  <div class="kap ust-serit-ic">
    <div class="us-sol">
      <a href="tel:{S['tel_link']}">{svg_tel()}<span>{e(S['tel'])}</span></a>
      <a href="tel:{S['tel2_link']}">{svg_tel()}<span>{e(S['tel2'])}</span></a>
      <a href="{wa_link()}" target="_blank" rel="noopener">{svg_wa()}<span>WhatsApp</span></a>
    </div>
    <div class="us-sag">
      <span class="us-saat">{svg_konum()}<span>Merkez / Bartın</span></span>
    </div>
  </div>
</div>"""

def ust_header(aktif=""):
    ln = "".join('<a href="%s"%s>%s</a>' % (u, ' class="aktif"' if u == aktif else "", e(m))
                 for u, m in MENU)
    return f"""<div class="ust-kap">
{ust_serit()}
<header class="ust">
  <div class="kap ust-ic">
    <a class="logo-bag" href="/" aria-label="{e(S['marka'])} ana sayfa">{logo()}</a>
    <nav class="menu" id="menu" aria-label="Ana menü">{ln}</nav>
    <div class="ust-ara">
      <a class="ust-tel" href="tel:{S['tel_link']}">
        <span class="ust-tel-ik">{svg_tel()}</span>
        <span class="ust-tel-ic"><small>Hemen arayın</small><strong>{e(S['tel'])}</strong></span>
      </a>
      {teklif_btn("dg dg-teklif")}
      <button class="hamburger" id="hamburger" aria-label="Menüyü aç" aria-expanded="false" aria-controls="menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>
</div>
"""

def kirinti(parcalar):
    ic, ld = [], []
    for n, (ad, u) in enumerate(parcalar, 1):
        ic.append(f'<a href="{u}">{e(ad)}</a>' if u else f'<span aria-current="page">{e(ad)}</span>')
        ld.append({"@type": "ListItem", "position": n, "name": ad, **({"item": ALAN + u} if u else {})})
    return (f'<nav class="kirinti" aria-label="Site haritası"><div class="kap">{"".join(ic)}</div></nav>'
            + ldj({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": ld}))

def w4_kredi():
    """Web4Medya imzası — bağlantı YALNIZ marka adını sarar (bkz. dehaiskele kararı)."""
    return ('<div class="w4"><span class="w4-bag">'
            '<span class="w4-etiket">Web Tasarım:</span> '
            '<a class="w4-ad" href="https://www.web4medya.com/" target="_blank" rel="noopener">'
            'Web<span class="w4-d">4</span>Medya</a></span></div>')

def alt_bilgi():
    hiz = "".join(f'<li><a href="/{h["slug"]}/">{e(h["ad"])}</a></li>' for h in D.HIZMETLER[:8])
    hiz += '<li class="alt-tumu"><a href="/hizmetlerimiz/">Tüm hizmetler →</a></li>'
    alan = "".join(f'<li><a href="/{a["slug"]}/">{e(a["ad"])}</a></li>' for a in D.ALANLAR)
    harita = "https://www.google.com/maps/search/?api=1&amp;query=" + quote(S["adres"])
    return f"""<footer class="alt">
  <div class="kap">
    <div class="alt-ust">
      <div class="alt-marka">
        <a class="logo-bag" href="/">{logo(buyuk=True)}</a>
        <p>{e(S['aciklama'])}</p>
        {tel_btn("dg dg-sari")}
      </div>
      <div class="alt-sut"><h3>Hizmetlerimiz</h3><ul>{hiz}</ul></div>
      <div class="alt-sut"><h3>Çalışma Alanları</h3><ul>{alan}</ul></div>
      <div class="alt-sut alt-iletisim"><h3>İletişim</h3>
        <p class="adres">{e(S['adres'])}</p>
        <p><span class="alt-kisi">{e(S['tel_kisi'])}</span><br><a href="tel:{S['tel_link']}">{e(S['tel'])}</a></p>
        <p><span class="alt-kisi">{e(S['tel2_kisi'])}</span><br><a href="tel:{S['tel2_link']}">{e(S['tel2'])}</a></p>
        <p><a href="{harita}" target="_blank" rel="noopener">Yol tarifi al</a></p>
      </div>
    </div>
    <div class="alt-son">
      <p>&copy; 2026 {e(S['marka'])} · Tüm hakları saklıdır.</p>
      {w4_kredi()}
    </div>
  </div>
</footer>
<nav class="sabit-ara" aria-label="Hızlı iletişim">
  <a class="sa sa-tel" href="tel:{S['tel_link']}"><span class="sa-ik">{svg_tel()}</span><span class="sa-yz">Celal</span></a>
  <a class="sa sa-tel" href="tel:{S['tel2_link']}"><span class="sa-ik">{svg_tel()}</span><span class="sa-yz">Kurtuluş</span></a>
  <a class="sa sa-wa" href="{wa_link()}" target="_blank" rel="noopener"><span class="sa-ik">{svg_wa()}</span><span class="sa-yz">WhatsApp</span></a>
</nav>
<script src="{surum('/assets/app.js')}" defer></script>
</body>
</html>
"""

# ── JSON-LD ─────────────────────────────────────────────────────────────────
def ldj(n):
    return ('<script type="application/ld+json">' +
            json.dumps(n, ensure_ascii=False, separators=(",", ":")) + '</script>')

def isletme_semasi():
    """⚠️ aggregateRating ve openingHours BİLİNÇLİ YOK — veri teyit edilmedi."""
    return ldj({
        "@context": "https://schema.org",
        "@type": "GeneralContractor",
        "@id": ALAN + "/#isletme",
        "name": S["marka"],
        "url": ALAN + "/",
        "telephone": [S["tel_link"], S["tel2_link"]],
        "description": S["aciklama"],
        "image": ALAN + "/images/og-arslankaya-insaat.jpg",
        "logo": ALAN + "/images/logo/arslankaya-logo-720.webp",
        "slogan": "Güvenle İnşa Ediyoruz",
        "address": {"@type": "PostalAddress", "streetAddress": S["adres_sokak"],
                    "addressLocality": S["adres_ilce"], "addressRegion": S["adres_il"],
                    "postalCode": S["adres_pk"], "addressCountry": "TR"},
        "areaServed": {"@type": "AdministrativeArea", "name": "Bartın"},
        "employee": [{"@type": "Person", "name": S["tel_kisi"], "telephone": S["tel_link"]},
                     {"@type": "Person", "name": S["tel2_kisi"], "telephone": S["tel2_link"]}],
        "hasOfferCatalog": {"@type": "OfferCatalog", "name": "İnşaat hizmetleri",
                            "itemListElement": [{"@type": "Offer", "itemOffered": {
                                "@type": "Service", "name": h["ad"], "url": f'{ALAN}/{h["slug"]}/'}}
                                for h in D.HIZMETLER]},
    })

def hizmet_semasi(h):
    return ldj({"@context": "https://schema.org", "@type": "Service",
                "name": h["ad"], "serviceType": h["ad"], "description": h["ozet"],
                "url": f'{ALAN}/{h["slug"]}/',
                "provider": {"@id": ALAN + "/#isletme"},
                "areaServed": {"@type": "AdministrativeArea", "name": "Bartın"}})

def sss_semasi(sorular):
    return ldj({"@context": "https://schema.org", "@type": "FAQPage",
                "mainEntity": [{"@type": "Question", "name": s,
                                "acceptedAnswer": {"@type": "Answer", "text": c}}
                               for s, c in sorular]})

# ── Bileşenler ──────────────────────────────────────────────────────────────
def dalga():
    return ('<div class="dalga" aria-hidden="true">'
            '<svg viewBox="0 0 1440 90" width="1440" height="90" preserveAspectRatio="none">'
            '<path d="M0,54 C240,90 480,10 720,32 C960,54 1200,86 1440,58 L1440,90 L0,90 Z"/>'
            '</svg></div>')

def hero_h1(satirlar):
    # ⚠️ Satırlar arasında boşluk şart — metin çıkarımında bitişiyordu (dehaiskele).
    return ('<h1 class="hb">' +
            " ".join(f'<span class="l"><span>{e(s)}</span></span>' for s in satirlar) + '</h1>')

def guven_seridi():
    """⚠️ Yalnız teyitli bilgiler. Yıl/sigorta/7-24 EKLEME (bkz. data.py başlığı)."""
    ogeler = [
        ("Bartın Merkez'deyiz", "Demirciler Mahallesi'ndeki ofisimizden sahaya çıkıyoruz"),
        ("Temelden çatıya", "Kaba inşaattan anahtar teslime 13 iş kalemi"),
        ("Yerinde keşif, yazılı teklif", "İş kalemleri ve sırası baştan kâğıda dökülüyor"),
        ("İki yetkili, doğrudan hat", "Celal ve Kurtuluş Arslankaya'ya doğrudan ulaşın"),
    ]
    ic = "".join(f'<li><strong>{e(a)}</strong><span>{e(b)}</span></li>' for a, b in ogeler)
    return f'<section class="serit"><div class="kap"><ul>{ic}</ul></div>{dalga()}</section>'

def hizmet_kartlari(baslik="Hizmetlerimiz", haric=None, giris=None, liste=None):
    kart = []
    for h in (liste or D.HIZMETLER):
        if h["slug"] == haric:
            continue
        kart.append(
            f'<a class="kart gel" href="/{h["slug"]}/">'
            f'<span class="kart-daire kart-ikon">{ikon(h["ikon"], 46)}</span>'
            f'<span class="kart-ic"><h3>{e(h["ad"])}</h3><p>{e(h["ozet"])}</p>'
            f'<span class="kart-ok">Detaylı Bilgi</span></span></a>')
    gr = f'<p class="giris">{e(giris)}</p>' if giris else ""
    return (f'<section class="bol turler"><div class="kap"><div class="bol-bas">'
            f'<h2>{e(baslik)}</h2>{gr}</div>'
            f'<div class="izgara izgara-kart">{"".join(kart)}</div></div></section>')

def bolunmus_bolum():
    alan = "".join(
        f'<a class="urun urun-ikon" href="/{a["slug"]}/"><span class="urun-ik">{ikon(a["ikon"], 30)}</span>'
        f'<span class="urun-ic"><h3>{e(a["ad"])}</h3><span class="urun-ok">Detaylı Bilgi</span></span></a>'
        for a in D.ALANLAR)
    return f"""<section class="bolunmus">
  <div class="kap bolunmus-ic">
    <div class="bl-sol">
      <h2>Çalışma Alanlarımız</h2>
      <p>Ev sahibinden müteahhide, iş yerinden kamu yapısına kadar aynı özenle.</p>
      <div class="urunler">{alan}</div>
    </div>
    <div class="bl-sag">
      <h2>Bartın'da Temelden Çatıya</h2>
      <p><strong>Arslankaya İnşaat</strong>, Celal Arslankaya ve Kurtuluş Arslankaya'nın
         yürüttüğü, Bartın Merkez'de bulunan bir inşaat firması. Kaba inşaattan ince işe,
         çatıdan mantolamaya, küçük tadilattan anahtar teslim yenilemeye kadar işleri
         kendi ekibimizle yapıyoruz.</p>
      <p>Çalışma şeklimiz basit: önce yerinde görüyoruz, yapılacak işleri kalem kalem
         yazıyoruz, sonra fiyat konuşuyoruz. Telefonda kesin rakam vermek yerine işi
         görmeyi tercih ediyoruz; çünkü aynı görünen iki işin altından bambaşka şeyler
         çıkabiliyor.</p>
      <div class="dg-grup">
        <a class="dg dg-cerceve-ak" href="/hakkimizda/"><span>Bizi Tanıyın</span></a>
        {teklif_btn("dg dg-sari")}
      </div>
    </div>
  </div>
</section>"""

def surec_bolum():
    adim = [
        ("Arayın ya da yazın", "İşi kısaca anlatın; fotoğraf gönderebiliyorsanız WhatsApp'tan iletin."),
        ("Yerinde keşif", "Gelip görüyor, ölçü alıyor, işin kapsamını birlikte netleştiriyoruz."),
        ("Yazılı teklif", "İş kalemleri, malzeme ve süre kâğıda dökülüyor; neye ödeme yaptığınızı görüyorsunuz."),
        ("Uygulama ve teslim", "İş programına göre ilerliyor, teslimde eksik listesini birlikte kontrol ediyoruz."),
    ]
    ic = "".join(f'<div class="donem adim"><span class="adim-no">{n}</span><h3>{e(a)}</h3><p>{e(b)}</p></div>'
                 for n, (a, b) in enumerate(adim, 1))
    return f"""<section class="bol donemler"><div class="kap">
  <div class="bol-bas"><h2>Nasıl Çalışıyoruz?</h2>
  <p class="giris">Her işte aynı dört adım — küçük bir tadilatta da, bir binada da.</p></div>
  <div class="izgara-4">{ic}</div>
</div></section>"""

def sss_bolum(sorular, baslik="Sık Sorulan Sorular"):
    ic = "".join(f'<details class="sss-o"><summary>{e(s)}</summary><div class="sss-c"><p>{e(c)}</p></div></details>'
                 for s, c in sorular)
    return f'<section class="bol sss"><div class="kap dar"><h2>{e(baslik)}</h2>{ic}</div></section>'

def cta_band(baslik, metin, konu="inşaat işi"):
    return f"""<section class="cta"><div class="kap dar">
  <h2>{e(baslik)}</h2><p>{e(metin)}</p>
  <div class="dg-grup">{tel_btn()}{tel2_btn()}{wa_btn(f"Merhaba, {konu} için bilgi almak istiyorum.")}</div>
</div></section>"""

def hero_ic(ust, satirlar, alt, konu="inşaat işi", cipler=None):
    cip = "".join(f"<li>{e(c)}</li>" for c in (cipler or []))
    cip = f'<ul class="hero-cip">{cip}</ul>' if cip else ""
    return f"""<section class="hero hero-ic hero-desen">
  <div class="kap hero-metin">
    <p class="hero-ust">{e(ust)}</p>
    {hero_h1(satirlar)}
    <p class="hero-alt">{e(alt)}</p>
    <div class="dg-grup">{tel_btn()}{teklif_btn("dg dg-cerceve", konu)}</div>
    {cip}
  </div>
</section>"""

# ── Sayfalar ────────────────────────────────────────────────────────────────
def anasayfa():
    baslik = "Bartın İnşaat Firması - Arslankaya İnşaat"
    aciklama = ("Bartın'da temelden çatıya inşaat, kaba ve ince işler, tadilat, çatı, mantolama "
                "ve anahtar teslim yenileme. Yerinde keşif, yazılı teklif: " + S["tel"])
    sema = (isletme_semasi() + sss_semasi(D.ANA_SSS) +
            ldj({"@context": "https://schema.org", "@type": "WebSite", "name": S["marka"],
                 "url": ALAN + "/", "inLanguage": "tr-TR"}))
    return head(baslik, aciklama, "/", sema) + ust_header("/") + f"""
<main id="ana">
<section class="hero hero-ana hero-tam hero-desen">
  <div class="kap hero-metin">
    <p class="hero-ust">Bartın İnşaat Firması</p>
    {hero_h1(["Bartın İnşaat Firması - Arslankaya İnşaat"])}
    <p class="hero-slogan">“Güvenle İnşa Ediyoruz.”</p>
    <p class="hero-alt">Kaba ve ince inşaat, tadilat, çatı, mantolama ve anahtar teslim
       yenileme. Önce yerinde görüyoruz, işi kalem kalem yazıyoruz, sonra fiyat konuşuyoruz.</p>
    <div class="dg-grup">{tel_btn()}{teklif_btn("dg dg-cerceve")}</div>
    <ul class="hero-cip"><li>Bartın Merkez</li><li>13 hizmet kalemi</li>
      <li>Yerinde keşif</li><li>Yazılı teklif</li></ul>
  </div>
</section>
{guven_seridi()}
{hizmet_kartlari("Hizmetlerimiz", giris="Anahtar teslim inşaatın her aşamasını kendi ekibimizle yapıyoruz.")}
{afis_bolum(giris="Temelden çatıya bütün hizmetlerimiz ve çalışma alanlarımız tek görselde.")}
{bolunmus_bolum()}
{surec_bolum()}
{sss_bolum(D.ANA_SSS)}
{cta_band("İşinizi yerinde görelim", "Ne yaptırmak istediğinizi anlatın; keşif gününü birlikte belirleyelim.")}
</main>
{alt_bilgi()}"""

def hizmet_sayfasi(h):
    yol = f'/{h["slug"]}/'
    baslik = f'Bartın {h["ad"]} | {S["marka"]}'
    aciklama = f'Bartın\'da {kucuk(h["ad"])}: {h["ozet"]} Yerinde keşif ve yazılı teklif: {S["tel"]}'
    kapsam = "".join(f"<li>{e(k)}</li>" for k in h["kapsam"])
    # İlgili hizmetler: bu hizmeti içeren çalışma alanlarındaki diğer hizmetler
    ilgili = []
    for a in D.ALANLAR:
        if h["slug"] in a["hizmet"]:
            ilgili += [s for s in a["hizmet"] if s != h["slug"] and s not in ilgili]
    ilgili = [HIZ[s] for s in ilgili][:6] or [x for x in D.HIZMETLER if x is not h][:6]
    alanlar = [a for a in D.ALANLAR if h["slug"] in a["hizmet"]]
    alan_ln = ", ".join(f'<a href="/{a["slug"]}/">{e(kucuk(a["kisa"]))}</a>' for a in alanlar)
    alan_p = (f"<p>Bu hizmeti {alan_ln} müşterilerimize veriyoruz.</p>" if alanlar else "")
    sema = isletme_semasi() + hizmet_semasi(h) + sss_semasi(h["sss"])
    return head(baslik, aciklama, yol, sema) + ust_header("/hizmetlerimiz/") + f"""
<main id="ana">
{kirinti([("Ana Sayfa", "/"), ("Hizmetlerimiz", "/hizmetlerimiz/"), (h["ad"], None)])}
{hero_ic("Bartın · " + S["marka"], ["Bartın " + h["ad"]], h["ozet"], kucuk(h["ad"]))}
<section class="bol"><div class="kap dar metin">
  <h2>{e(h["ad"])} Nedir, Neleri Kapsar?</h2>
  <p>{e(h["giris"])}</p>
  <ul class="ok-liste">{kapsam}</ul>
  <h2>İşi Nasıl Yürütüyoruz?</h2>
  <p>{e(h["surec"])}</p>
  <h2>Bartın'da Dikkat Ettiğimiz Nokta</h2>
  <p>{e(h["yerel"])}</p>
  {alan_p}
</div></section>
{hizmet_kartlari("İlgili Hizmetler", liste=ilgili)}
{sss_bolum(h["sss"], h["ad"] + " Hakkında Sık Sorulanlar")}
{cta_band(h["ad"] + " için yerinde keşif", "İşi anlatın, uygun günü birlikte belirleyelim. Teklifi kalem kalem yazılı veriyoruz.", kucuk(h["ad"]))}
</main>
{alt_bilgi()}"""

def hizmetler_sayfasi():
    yol = "/hizmetlerimiz/"
    baslik = f'Bartın İnşaat Hizmetleri | {S["marka"]}'
    aciklama = ("Arslankaya İnşaat'ın Bartın'da verdiği 13 hizmet: temelden çatıya inşaat, kaba ve "
                "ince işler, tadilat, çatı, boya, seramik, cephe, mantolama ve daha fazlası.")
    sema = isletme_semasi()
    return head(baslik, aciklama, yol, sema) + ust_header(yol) + f"""
<main id="ana">
{kirinti([("Ana Sayfa", "/"), ("Hizmetlerimiz", None)])}
{hero_ic("Anahtar Teslim İnşaat", ["Hizmetlerimiz"], "Temelden çatıya bir binanın bütün aşamaları — ister tamamını, ister tek bir kalemini verin.")}
{hizmet_kartlari("13 Hizmet Kalemi")}
{afis_bolum("Tüm Hizmetlerimiz Tek Görselde")}
{cta_band("Hangi hizmet size uygun?", "Emin değilseniz işi anlatmanız yeterli; doğru kalemi birlikte belirleyelim.")}
</main>
{alt_bilgi()}"""

def alan_sayfasi(a):
    yol = f'/{a["slug"]}/'
    baslik = f'{a["ad"]} | {S["marka"]} Bartın'
    aciklama = f'{a["ozet"]} Arslankaya İnşaat, Bartın Merkez. Yerinde keşif ve yazılı teklif: {S["tel"]}'
    metin = "".join(f"<p>{e(p)}</p>" for p in a["metin"])
    diger = "".join(f'<li><a href="/{x["slug"]}/">{e(x["ad"])}</a></li>' for x in D.ALANLAR if x is not a)
    return head(baslik, aciklama, yol, isletme_semasi()) + ust_header("/calisma-alanlari/") + f"""
<main id="ana">
{kirinti([("Ana Sayfa", "/"), ("Çalışma Alanları", "/calisma-alanlari/"), (a["ad"], None)])}
{hero_ic("Çalışma Alanlarımız", [a["ad"]], a["ozet"])}
<section class="bol"><div class="kap dar metin">
  <h2>Bu Alanda Neler Yapıyoruz?</h2>
  {metin}
  <h2>Diğer Çalışma Alanlarımız</h2>
  <ul class="ok-liste">{diger}</ul>
</div></section>
{hizmet_kartlari("Bu Alanda Sık Verdiğimiz Hizmetler", liste=[HIZ[s] for s in a["hizmet"]])}
{cta_band("Projenizi konuşalım", "Kapsamı anlatın; keşif ve yazılı teklif için gün belirleyelim.")}
</main>
{alt_bilgi()}"""

def alanlar_sayfasi():
    yol = "/calisma-alanlari/"
    baslik = f'Çalışma Alanlarımız | {S["marka"]} Bartın'
    aciklama = ("Arslankaya İnşaat müteahhitler, bireysel müşteriler, kamu kurumları, ticari "
                "işletmeler ve toplu konut projeleri için Bartın'da inşaat hizmeti veriyor.")
    kart = "".join(
        f'<a class="donem alan-kart gel" href="/{a["slug"]}/"><span class="alan-ik">{ikon(a["ikon"], 34)}</span>'
        f'<h3>{e(a["ad"])}</h3><p>{e(a["ozet"])}</p><span class="kart-ok">Detaylı Bilgi</span></a>'
        for a in D.ALANLAR)
    return head(baslik, aciklama, yol, isletme_semasi()) + ust_header(yol) + f"""
<main id="ana">
{kirinti([("Ana Sayfa", "/"), ("Çalışma Alanları", None)])}
{hero_ic("Kimlerle Çalışıyoruz", ["Çalışma Alanlarımız"], "Ev sahibinden müteahhide, iş yerinden kamu yapısına kadar.")}
<section class="bol"><div class="kap"><div class="izgara-3">{kart}</div></div></section>
{cta_band("Projenizi konuşalım", "Kapsamı anlatın; keşif ve yazılı teklif için gün belirleyelim.")}
</main>
{alt_bilgi()}"""

def hakkimizda_sayfasi():
    yol = "/hakkimizda/"
    baslik = f'Hakkımızda | {S["marka"]} Bartın'
    aciklama = ("Arslankaya İnşaat, Celal Arslankaya ve Kurtuluş Arslankaya'nın yürüttüğü, Bartın "
                "Merkez'de bulunan inşaat firması. Temelden çatıya, keşiften teslime aynı ekip.")
    sema = ldj({"@context": "https://schema.org", "@type": "AboutPage", "url": ALAN + yol,
                "about": {"@id": ALAN + "/#isletme"}}) + isletme_semasi()
    # ⏳ Firma geçmişi / kuruluş yılı / tamamlanan işler kullanıcıdan bekleniyor.
    return head(baslik, aciklama, yol, sema) + ust_header(yol) + f"""
<main id="ana">
{kirinti([("Ana Sayfa", "/"), ("Hakkımızda", None)])}
{hero_ic("Arslankaya İnşaat", ["Hakkımızda"], "Bartın Merkez'de, temelden çatıya inşaat ve yenileme işleri yapan bir aile firması.")}
<section class="bol"><div class="kap dar metin">
  <h2>Biz Kimiz?</h2>
  <p><strong>Arslankaya İnşaat</strong>, Celal Arslankaya ve Kurtuluş Arslankaya'nın yürüttüğü,
     ofisi Bartın Merkez Demirciler Mahallesi'nde bulunan bir inşaat firması. Kaba inşaattan
     ince işlere, çatıdan mantolamaya, küçük tadilattan anahtar teslim daire ve iş yeri
     yenilemeye kadar geniş bir alanda çalışıyoruz.</p>
  <h2>Nasıl Çalışırız?</h2>
  <p>İşe her zaman yerinde bakarak başlıyoruz. Yapılacak işleri kalem kalem yazıyor, malzeme
     ve süreyi netleştiriyor, ardından fiyat konuşuyoruz. İş boyunca muhatabınız değişmiyor:
     iki yetkiliye de doğrudan telefonla ulaşabiliyorsunuz.</p>
  <h2>Kimlerle Çalışıyoruz?</h2>
  <ul class="ok-liste">{"".join(f'<li><a href="/{a["slug"]}/">{e(a["ad"])}</a></li>' for a in D.ALANLAR)}</ul>
</div></section>
{afis_bolum("Arslankaya İnşaat Tanıtım")}
{iletisim_kartlari()}
{cta_band("Tanışalım", "İşinizi anlatın; yerinde keşif için uygun günü birlikte belirleyelim.")}
</main>
{alt_bilgi()}"""

def iletisim_kartlari():
    kisi = "".join(f"""<div class="donem kisi-kart">
      <h3>{e(ad)}</h3><p class="kisi-rol">{e(S['marka'])}</p>
      <a class="dg dg-sari" href="tel:{lnk}">{svg_tel()}<span>{e(tel)}</span></a></div>"""
        for ad, tel, lnk in ((S["tel_kisi"], S["tel"], S["tel_link"]),
                             (S["tel2_kisi"], S["tel2"], S["tel2_link"])))
    harita = "https://www.google.com/maps/search/?api=1&amp;query=" + quote(S["adres"])
    return f"""<section class="bol iletisim"><div class="kap">
  <div class="bol-bas"><h2>Bize Ulaşın</h2></div>
  <div class="izgara-3">{kisi}
    <div class="donem kisi-kart"><h3>Ofis Adresimiz</h3><p>{e(S['adres'])}</p>
      <a class="dg dg-hat2" href="{harita}" target="_blank" rel="noopener">{svg_konum()}<span>Yol tarifi al</span></a>
      {wa_btn()}</div>
  </div>
</div></section>"""

def iletisim_sayfasi():
    yol = "/iletisim/"
    baslik = f'İletişim | {S["marka"]} Bartın'
    aciklama = (f'Arslankaya İnşaat iletişim: {S["tel_kisi"]} {S["tel"]}, {S["tel2_kisi"]} '
                f'{S["tel2"]}. Adres: Demirciler Mah. Kenar Sok. No:2, Merkez / Bartın.')
    sema = ldj({"@context": "https://schema.org", "@type": "ContactPage", "url": ALAN + yol,
                "about": {"@id": ALAN + "/#isletme"}}) + isletme_semasi()
    return head(baslik, aciklama, yol, sema) + ust_header(yol) + f"""
<main id="ana">
{kirinti([("Ana Sayfa", "/"), ("İletişim", None)])}
{hero_ic("Arslankaya İnşaat", ["İletişim"], "Arayın, WhatsApp'tan yazın ya da ofisimize uğrayın.")}
{iletisim_kartlari()}
</main>
{alt_bilgi()}"""

def hata404():
    ilk = "".join(f'<li><a href="/{h["slug"]}/">{e(h["ad"])}</a></li>' for h in D.HIZMETLER[:6])
    return head("Sayfa bulunamadı | " + S["marka"],
                "Aradığınız sayfa taşınmış ya da hiç var olmamış olabilir. Hizmetlerimize ana "
                "sayfadan ulaşabilir veya doğrudan bizi arayabilirsiniz.", "/404.html") + ust_header() + f"""
<main id="ana">
{hero_ic("404", ["Sayfa bulunamadı"], "Aradığınız sayfa taşınmış olabilir. Aşağıdan devam edebilir ya da doğrudan arayabilirsiniz.")}
<section class="bol"><div class="kap dar metin">
  <h2>Sık kullanılan sayfalar</h2>
  <ul class="ok-liste">{ilk}<li><a href="/hizmetlerimiz/">Tüm hizmetler</a></li></ul>
</div></section>
</main>
{alt_bilgi()}"""

# ── Yazım ───────────────────────────────────────────────────────────────────
def ritim_uygula(sayfa):
    """Bölüm zeminlerini sıraya göre beyaz/gri dönüşümlü yapar (dehaiskele'den)."""
    sayac = [0]
    def degis(m):
        sinif = m.group(1)
        if sinif.startswith("bolunmus"):
            sayac[0] += 1
            return m.group(0)
        sayac[0] += 1
        return '<section class="%s %s"' % (sinif, "bol-gri" if sayac[0] % 2 else "bol-ak")
    return re.sub(r'<section class="((?:bol|bolunmus)\b[^"]*)"', degis, sayfa)

def yaz(yol, ic):
    ic = ritim_uygula(ic)
    if yol == "/":
        hedef = os.path.join(KOK, "index.html")
    elif yol.endswith("/"):
        hedef = os.path.join(KOK, yol.strip("/"), "index.html")
    else:
        hedef = os.path.join(KOK, yol.lstrip("/"))
    os.makedirs(os.path.dirname(hedef), exist_ok=True)
    with open(hedef, "w", encoding="utf-8") as f:
        f.write(ic)

AFIS_SAYFALARI = {"/", "/hizmetlerimiz/", "/hakkimizda/"}

def main():
    yollar = []
    yaz("/", anasayfa()); yollar.append(("/", "1.0"))
    for h in D.HIZMETLER:
        yaz(f'/{h["slug"]}/', hizmet_sayfasi(h)); yollar.append((f'/{h["slug"]}/', "0.9"))
    for a in D.ALANLAR:
        yaz(f'/{a["slug"]}/', alan_sayfasi(a)); yollar.append((f'/{a["slug"]}/', "0.7"))
    for yol, f, p in (("/hizmetlerimiz/", hizmetler_sayfasi, "0.9"),
                      ("/calisma-alanlari/", alanlar_sayfasi, "0.7"),
                      ("/hakkimizda/", hakkimizda_sayfasi, "0.6"),
                      ("/iletisim/", iletisim_sayfasi, "0.6")):
        yaz(yol, f()); yollar.append((yol, p))
    yaz("/404.html", hata404())

    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
          'xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">']
    for y, p in yollar:
        gor = ""
        if y in AFIS_SAYFALARI:
            gor = (f"<image:image><image:loc>{ALAN}/images/w1600/arslankaya-insaat-hizmet.webp"
                   f"</image:loc></image:image>")
        sm.append(f"  <url><loc>{ALAN}{y}</loc><priority>{p}</priority>{gor}</url>")
    sm.append("</urlset>")
    open(os.path.join(KOK, "sitemap.xml"), "w", encoding="utf-8").write("\n".join(sm) + "\n")
    open(os.path.join(KOK, "robots.txt"), "w", encoding="utf-8").write(
        "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % ALAN)
    open(os.path.join(KOK, "CNAME"), "w", encoding="utf-8").write(ALAN.split("//")[1] + "\n")
    print(f"{len(yollar)} sayfa yazıldı (1 ana + {len(D.HIZMETLER)} hizmet + "
          f"{len(D.ALANLAR)} alan + 4 sabit) + 404")

if __name__ == "__main__":
    main()
