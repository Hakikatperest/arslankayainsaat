# -*- coding: utf-8 -*-
"""Panelden (panel.arslankayainsaat.com) gelen referans verisini depoya alır.
Kullanım: python3 _src/referans_al.py /home/panel.arslankayainsaat.com/veri
- veri/referanslar.json → _src/referanslar.json (alanlar süzülür, tipler zorlanır)
- veri/gorseller/<id>.webp → img/referans/<id>.webp ; artık kullanılmayanlar silinir
- data.HIZMETLER → veri/hizmetler.json (paneldeki "ilgili hizmet" listesi senkron kalsın)
⚠️ Panel verisi GÜVENİLMEZ girdi sayılır: id/görsel adı regex'le doğrulanır, metin build'de kaçışlanır."""
import json, os, re, shutil, sys
KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import data as D

veri = sys.argv[1]
ham = json.load(open(os.path.join(veri, "referanslar.json"), encoding="utf-8"))
hizmetler = {h["slug"] for h in D.HIZMETLER}
temiz, kullanilan = [], set()
for r in ham:
    rid = str(r.get("id", ""))
    gorsel = str(r.get("gorsel", ""))
    if not re.fullmatch(r"[a-f0-9]{12}", rid) or gorsel != rid + ".webp":
        continue
    kaynak = os.path.join(veri, "gorseller", gorsel)
    if not os.path.isfile(kaynak):
        continue
    temiz.append({
        "id": rid,
        "firma": str(r.get("firma", ""))[:80].strip(),
        "aciklama": str(r.get("aciklama", ""))[:700].strip(),
        "hizmet": r.get("hizmet") if r.get("hizmet") in hizmetler else "",
        "gorunur": bool(r.get("gorunur")),
        "sira": int(r.get("sira", 0)),
        "tarih": str(r.get("tarih", ""))[:25],
    })
    kullanilan.add(gorsel)
temiz.sort(key=lambda r: (r["sira"], r["tarih"]))
hedef = os.path.join(KOK, "img", "referans")
os.makedirs(hedef, exist_ok=True)
for g in kullanilan:
    shutil.copyfile(os.path.join(veri, "gorseller", g), os.path.join(hedef, g))
for f in os.listdir(hedef):
    if f not in kullanilan:
        os.remove(os.path.join(hedef, f))
with open(os.path.join(KOK, "_src", "referanslar.json"), "w", encoding="utf-8") as f:
    json.dump(temiz, f, ensure_ascii=False, indent=1)
with open(os.path.join(veri, "hizmetler.json"), "w", encoding="utf-8") as f:
    json.dump({h["slug"]: h["ad"] for h in D.HIZMETLER}, f, ensure_ascii=False, indent=1)
print(f"{len(temiz)} referans alındı ({sum(r['gorunur'] for r in temiz)} görünür)")
