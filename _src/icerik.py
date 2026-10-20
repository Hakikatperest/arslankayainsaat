# -*- coding: utf-8 -*-
"""Hizmet sayfası gövde metinleri — kullanıcının "benim dilimle" isteğiyle (2026-10-20) yazıldı.

Ses: firmanın ağzından ("biz Arslankaya İnşaat olarak"), okuyucuya "siz"; samimi, dürüst,
yer yer :) ve "..", kademeli anlatım, kutucuklar (Tavsiyemiz / Dikkat / Önemli).
⛔ Teyitsiz iddia YOK: deneyim yılı, fiyat, garanti süresi, sigorta, "7/24", müşteri yorumu.
⛔ Uydurma vaka/proje anlatma — firma gerçek iş fotoğrafı/vakası verince buraya eklenir.

Biçim işaretleri (build.metin() çevirir):
  "son": [...]           → listeden SONRA gelen paragraflar ("p" listeden önce/sonra bölünür)
  **kalın**              → <strong>
  [[slug|bağlantı yazısı]] → iç bağlantı (slug data.HIZMETLER/ALANLAR'da olmalı; denetim kırık linki yakalar)
"""

ICERIK = {

# ───────────────────────────────────────────────────────────────────────────
"temelden-catiya-insaat": {
"giris": [
    "Elinizde bir arsa ve ruhsatlı bir proje var, ama işin içinden nasıl çıkacağınızı "
    "bilmiyorsunuz.. Hafriyatçı ayrı, kalıpçı ayrı, çatıcı ayrı, sıvacı ayrı derken bir bakmışsınız "
    "yedi sekiz farklı ekiple uğraşıyorsunuz ve her biri bir öncekinin işine laf ediyor :)",
    "Biz Arslankaya İnşaat olarak **temelden çatıya inşaatı tek elden** yürütüyoruz. Yani "
    "muhatabınız baştan sona aynı: zemin, temel, betonarme, duvar, çatı, cephe ve ince işler "
    "aynı programın parçası olarak ilerliyor.",
],
"bolumler": [
    {"h": "Temelden Çatıya İnşaatta Hangi Aşamalar Var?",
     "p": ["Bir binanın yapımını kabaca beş aşamada düşünebilirsiniz. Her aşamanın kendi "
           "kontrol noktası var ve bir sonrakine o kontrol bitmeden geçilmiyor:"],
     "liste": ["**Saha ve temel:** hafriyat, grobeton, temel betonarmesi ve temel yalıtımı.",
               "**Karkas:** kolon, kiriş, perde ve döşemeler — her katta kalıp, demir, kontrol, beton.",
               "**Duvar ve çatı:** dış ve iç duvarlar, çatı konstrüksiyonu ve kaplama. Bina bu noktada "
               "\"kapanır\", yağmur artık içeri girmez.",
               "**Tesisat ve cephe:** elektrik-su altyapısı, sıva, mantolama ve dış cephe.",
               "**İnce işler ve teslim:** alçı, boya, zemin, seramik, kapı-pencere, temizlik."]},
    {"h": "Bartın'da Bina Yaparken Neye Dikkat Ediyoruz?",
     "p": ["Bartın yılın neredeyse her ayı yağış alan bir Karadeniz şehri. Bu yüzden bizim için "
           "**su, binanın en büyük düşmanı.** Temelde drenaj ve perde duvar yalıtımını, çatıda "
           "da su yalıtımını \"sonra bakarız\" kalemi olarak görmüyoruz. Bunlar kaba inşaat "
           "bitmeden yapılmazsa sonradan yapmak hem çok pahalı hem de çoğu zaman yarım kalıyor.",
           "Bir tık ileri gidelim: eğimli arsalarda istinat duvarı ve yağmur suyunun nereye "
           "akacağı da baştan planlanmalı. Sonradan eklenen istinat bahçe düzenini bozar, "
           "bütçeyi de beklenmedik yerden deler."],
     "kutu": ("Tavsiyemiz", "Teklif karşılaştırırken sadece toplam rakama bakmayın. Temel "
              "yalıtımı, drenaj ve çatı altı su yalıtım örtüsü teklifte ayrı kalem olarak "
              "yazıyor mu, ona bakın. Ucuz görünen teklifin farkı çoğu zaman bu kalemlerdedir..")},
    {"h": "Yapı Denetim ve Kontroller",
     "p": ["Ruhsatlı her yapıda bir yapı denetim firması var ve her kat betonu öncesi demir ve "
           "kalıp kontrolü yapılıyor. Biz bu tarihleri yapı denetimle doğrudan koordine ediyoruz; "
           "**kontrol tutanağı imzalanmadan beton dökülmüyor.** Size düşen sadece sonucu takip "
           "etmek.",
           "Kaba inşaatın detaylarını [[kaba-insaat|kaba inşaat işleri]] sayfamızda, beton ve "
           "donatı tarafını da [[beton-kalip-demir|beton, kalıp ve demir işleri]] sayfamızda daha "
           "ayrıntılı anlattık."]},
    {"h": "Malzeme Dahil mi, Sadece İşçilik mi?",
     "p": ["İki modelle de çalışabiliyoruz. **Malzeme dahil anahtar teslimde** malzemenin "
           "alınması, sahaya gelmesi ve zamanında hazır olması bizim sorumluluğumuzda. "
           "**Malzemesi sizden işçilikte** ise malzemeyi siz alıyorsunuz, biz hangi malzemenin ne "
           "zaman sahada olması gerektiğini önceden söylüyoruz.",
           "Hangisinin size uygun olduğu bütçenize ve işe ne kadar zaman ayırabildiğinize bağlı. "
           "Bunu keşifte açık açık konuşuyoruz."]},
],
"sss": [
    ("Temelden çatıya inşaata başlamak için ne gerekiyor?",
     "Onaylı mimari ve statik proje, yapı ruhsatı ve zemin etüdü raporu. Ruhsat süreci devam "
     "ediyorsa keşif ve metraj çalışmasına yine başlayabiliyoruz."),
    ("Fiyatı nasıl belirliyorsunuz?",
     "Proje üzerinden metraj çıkarıp iş kalemi bazında teklif veriyoruz. Telefonda metrekare başı "
     "kesin fiyat vermiyoruz; zemin, kat sayısı ve proje detayı rakamı ciddi şekilde değiştiriyor."),
    ("Malzemeyi kim alıyor?",
     "İki yolu da konuşabiliyoruz: malzeme dahil anahtar teslim ya da malzemesi sizden işçilik."),
    ("İnşaat süresince nasıl haberdar olurum?",
     "İş programını yazılı veriyoruz, her aşama bittiğinde fotoğraflarla bilgi geçiyoruz. İki "
     "yetkiliye de doğrudan telefonla ulaşabiliyorsunuz."),
],
},

# ───────────────────────────────────────────────────────────────────────────
"kaba-insaat": {
"giris": [
    "Kaba inşaat, binanın ayakta durmasını sağlayan her şey demek: temel, kolonlar, kirişler, "
    "döşemeler, merdivenler ve dış duvarlar. Açık konuşalım; bu aşamada yapılan bir hata ince "
    "işte **gizlenebilir ama asla düzelmez.** Eğri bir kolonu sıvayla düzeltirsiniz, ama "
    "içindeki eksik demiri hiçbir şeyle tamamlayamazsınız.",
    "O yüzden biz Arslankaya İnşaat olarak kaba inşaatta en çok ölçüye, demire ve beton "
    "kalitesine kafa yoruyoruz.",
],
"bolumler": [
    {"h": "Kaba İnşaat Hangi İşleri Kapsar?",
     "p": ["Sahada iş sırası her katta aynı: aplikasyon, kalıp, demir, kontrol, beton ve kür. "
           "Kat bitince bir sonrakine geçiliyor. Kabaca şu kalemlerden oluşuyor:"],
     "liste": ["Hafriyat, tesviye ve grobeton",
               "Temel betonarmesi ve **bohçalama yalıtım** (temeli sudan koruyan kaplama)",
               "Kolon, kiriş, perde ve döşeme imalatı",
               "Merdiven ve sahanlıklar",
               "Dış ve iç duvar örümü — detayı [[duvar-siva|duvar ve sıva işleri]] sayfamızda",
               "Çatı karkası (betonarme ya da ahşap)"]},
    {"h": "Kaba İnşaatta En Sık Yapılan Hatalar",
     "p": ["Yıllar içinde sahada en çok gördüğümüz sorunları dürüstçe yazalım ki siz de "
           "kendi işinizde göz atabilin:"],
     "liste": ["**Pas payının unutulması:** demir kalıba yapışık kalırsa beton demiri korumaz, "
               "zamanla paslanma başlar. Demir ile kalıp arasına mutlaka pas payı takozu konmalı.",
               "**Vibratörsüz beton:** sıkıştırılmayan betonda boşluklar (çakıl yuvası) kalır.",
               "**Kürün atlanması:** beton döküldükten sonra günlerce nemli tutulmalı. Sıcak ve "
               "rüzgârlı havada sulanmayan beton yüzeyden çatlar.",
               "**Erken yük bindirme:** beton yeterli dayanıma gelmeden üstüne malzeme yığmak."]},
    {"h": "Yağışlı Havada Beton Dökülür mü?",
     "p": ["Bartın'da bu soruyu çok duyuyoruz :) Kısa cevap: sağanak altında beton dökmüyoruz. "
           "Hafif yağışta ise döküm gününü hava tahminine göre planlıyor, gerekirse yüzeyi "
           "örtüyoruz. Soğuk havada da donma riskine karşı önlem alınması gerekiyor.",
           "Takvimden bir iki gün kaybetmek, yanlış günde dökülmüş bir döşemeyle yıllarca "
           "uğraşmaktan her zaman daha ucuz.."],
     "kutu": ("Dikkat", "Eğimli parselde istinat duvarı ve drenaj, kaba inşaatın parçası olarak "
              "baştan planlanmalı. Bina bittikten sonra eklenen istinat hem pahalıya gelir hem de "
              "bahçe kotlarını bozar.")},
    {"h": "Sadece Kaba İnşaat Yaptırabilir miyim?",
     "p": ["Elbette. Kaba inşaatı biz bitirip ince işleri başka bir ekiple yürütebilirsiniz. "
           "Devamını da bize bırakmak isterseniz [[ince-insaat|ince inşaat işleri]] ve "
           "[[temelden-catiya-insaat|temelden çatıya inşaat]] sayfalarımıza göz atabilirsiniz. "
           "Müteahhitlere de bu kalemleri [[muteahhitlere-ozel-insaat-hizmetleri|taşeron olarak]] "
           "veriyoruz."]},
],
"sss": [
    ("Kaba inşaat ne kadar sürer?",
     "Kat sayısına, zemine ve mevsime göre değişiyor. Proje üzerinden iş programı çıkarıp size "
     "yazılı olarak veriyoruz; yağışlı günleri de bu programa pay olarak koyuyoruz."),
    ("Yapı denetimle siz mi görüşüyorsunuz?",
     "Evet. Beton döküm ve kontrol tarihlerini yapı denetim firmasıyla doğrudan koordine ediyoruz."),
    ("Kaba inşaat fiyatı neye göre değişir?",
     "İnşaat alanı, kat sayısı, temel tipi, zemin durumu ve malzemenin kimden olduğu belirleyici. "
     "Proje görmeden kesin rakam vermiyoruz."),
    ("Çatı kaba inşaata dahil mi?",
     "Çatı karkası genellikle kaba inşaatın son kalemi. Kaplama ve yalıtım tarafını "
     "çatı ve izolasyon işi olarak ayrıca planlıyoruz."),
],
},

# ───────────────────────────────────────────────────────────────────────────
"ince-insaat": {
"giris": [
    "Kaba inşaatı biten bir bina beton ve tuğladan ibaret; içinde oturulacak durumda değil. "
    "Sıva, şap, alçı, boya, zemin kaplaması, seramik, kapı-pencere ve dolap montajı.. Binayı "
    "**yaşanır hale getiren** bütün bu işlere ince inşaat diyoruz.",
    "İnce işin altın kuralı şu: **sıra önemli.** Tesisat bitmeden sıva, şap kurumadan parke, "
    "alçı kurumadan boya olmaz. Sırayı bozan her adım, birkaç ay sonra kabaran boya ya da "
    "kalkan parke olarak geri döner.",
],
"bolumler": [
    {"h": "İnce İnşaat İşleri Hangi Sırayla Yapılır?",
     "p": ["Bir daireyi kabadan teslime götürürken izlediğimiz sıra kabaca şöyle:"],
     "liste": ["Elektrik ve su tesisatının sıva altı kısmı ve testi",
               "İç sıva ve [[duvar-siva|duvar düzeltmeleri]]",
               "Şap ve zemin tesviyesi",
               "Alçı sıva, saten alçı ve gerekiyorsa asma tavan",
               "Islak hacimlerde su yalıtımı ve [[seramik-fayans|seramik-fayans]]",
               "Astar ve [[boya-badana-alci|boya]]",
               "Parke-laminat, kapı, dolap ve son montajlar",
               "Teslim temizliği"]},
    {"h": "Nemli İklimde Kuruma Süresi Neden Önemli?",
     "p": ["Bartın'ın nemli havasında sıva ve şap, kitapta yazan süreden daha geç kuruyabiliyor. "
           "Kurumadan üzerine boya ya da parke uygulanırsa kabarma, küf ve ses yapan zemin "
           "kaçınılmaz oluyor.",
           "O yüzden takvimi \"en hızlı\" değil, **\"en doğru\"** olacak şekilde kuruyoruz. Bu "
           "bazen birkaç gün kaybettirir ama sonradan yapılan tamirin yanında hiç kalır :)"],
     "kutu": ("Tavsiyemiz", "Parke döşetmeden önce şapın nemini mutlaka ölçtürün. Göz kararı "
              "\"kurumuş\" görünen şap içten hâlâ nemli olabilir.")},
    {"h": "Malzeme Seçiminde Nasıl Yardımcı Oluyoruz?",
     "p": ["Seramik, parke, boya, kapı gibi kalemlerde bütçenize ve kullanım yerine uygun "
           "seçenekleri birlikte değerlendiriyoruz. Son karar her zaman sizin; biz sadece "
           "\"bu ürün banyoda kayar\", \"bu boya kuzey odada küf tutar\" gibi sahada öğrendiğimiz "
           "şeyleri söylüyoruz.",
           "İnce işleri tek daire için de, tüm bina için de yapıyoruz. Komple yenileme "
           "düşünüyorsanız [[anahtar-teslim-yenileme|anahtar teslim daire ve iş yeri yenileme]] "
           "sayfamız da işinize yarayabilir."]},
],
"sss": [
    ("İnce işleri daire daire yaptırabilir miyim?",
     "Evet. Tek daire için de tüm bina için de çalışıyoruz."),
    ("İnce işler ne kadar sürer?",
     "Dairenin büyüklüğüne, seçilen malzemeye ve kuruma sürelerine göre değişiyor. Keşiften "
     "sonra iş takvimini yazılı olarak veriyoruz."),
    ("Tesisatı da siz mi yapıyorsunuz?",
     "Tesisatın sıva altı kısmının ince işten önce bitmesini ve test edilmesini biz organize "
     "ediyoruz; kapsamı keşifte netleştiriyoruz."),
    ("Malzemeyi ben alırsam ne değişir?",
     "Sadece işçilik fiyatlanır. Hangi malzemenin ne zaman sahada olması gerektiğini önceden "
     "söylüyoruz ki iş beklemesin."),
],
},

# ───────────────────────────────────────────────────────────────────────────
"tadilat-tamirat": {
"giris": [
    "Tavanda bir leke, banyoda kabaran fayans, duvarda bitmek bilmeyen bir küf.. Çoğu zaman "
    "insanlar bizi \"şurayı bir boyayalım\" diye arıyor. Biz de önce şunu soruyoruz: "
    "**bu leke nereden geliyor?**",
    "Çünkü dürüst olalım; kaynağı çözülmeyen bir nem lekesini boyarsanız iki ay sonra aynı "
    "yerde yeniden karşınıza çıkar. Biz Arslankaya İnşaat olarak tadilat ve tamiratta önce "
    "sorunun kaynağını buluyor, sonra görüneni onarıyoruz.",
],
"bolumler": [
    {"h": "Hangi Tadilat ve Tamirat İşlerini Yapıyoruz?",
     "p": ["Küçük ya da büyük ayırmadan şu işler için arayabilirsiniz:"],
     "liste": ["Nem, rutubet ve küf kaynaklı onarımlar",
               "Sıva çatlakları ve duvar tamiri",
               "Banyo ve mutfak yenileme",
               "Zemin kaplaması değişimi",
               "Kapı, pencere ve doğrama onarımı",
               "[[cati-izolasyon|Çatı aktarma]] ve oluk tamiri",
               "Apartman ortak alan onarımları"]},
    {"h": "Bartın'da Tadilatın Yarısı Neden Nemle İlgili?",
     "p": ["Bartın'da aldığımız tadilat taleplerinin önemli bir kısmı aslında su ile ilgili. "
           "Suyun nereden geldiğini ayırt etmek işin yarısı; dört olası kaynak var:"],
     "liste": ["**Çatı:** kırık kiremit, tıkalı oluk, baca dibi.",
               "**Cephe:** çatlak sıva, yalıtımsız duvar, pencere kenarları.",
               "**Tesisat:** duvar içindeki gizli bir kaçak.",
               "**Yoğuşma:** yalıtımsız soğuk duvarda içerideki nemin terlemesi — bu durumda "
               "çözüm çoğu zaman [[mantolama-yalitim|mantolama]]."],
     "kutu": ("Önemli", "Küf lekesi gördüğünüzde üstünü boyatmadan önce mutlaka kaynağını "
              "tespit ettirin. Yanlış teşhisle yapılan tadilat, paranızı iki kez harcatır.")},
    {"h": "Evde Otururken Tadilat Yapılır mı?",
     "p": ["Çoğu işte evet. Çalışılan alanı naylon perdeyle kapatıyor, eşyaları örtüyor ve gün "
           "sonunda temizleyip öyle çıkıyoruz. Banyo gibi birkaç gün süren işlerde ise takvimi "
           "sizinle birlikte planlıyoruz ki eviniz kullanılmaz hale gelmesin.",
           "Tadilat bütün evi kapsayacak kadar büyüdüyse [[anahtar-teslim-yenileme|anahtar teslim "
           "yenileme]] daha mantıklı olabilir; keşifte bunu da açık açık söylüyoruz."]},
],
"sss": [
    ("Küçük işlere de geliyor musunuz?",
     "Evet. Tek bir duvar, tek bir banyo ya da çatıdaki bir akıntı için de arayabilirsiniz."),
    ("Fiyatı nasıl öğrenirim?",
     "WhatsApp'tan fotoğraf gönderirseniz kabaca fikir verebiliriz. Kesin teklif yerinde gördükten "
     "sonra çıkıyor."),
    ("Nem lekesinin kaynağını nasıl buluyorsunuz?",
     "Lekenin yerine, mevsimine ve davranışına bakıyoruz: yağmurdan sonra mı artıyor, kışın mı "
     "çıkıyor, sürekli mi? Bu ipuçları çatı, cephe, tesisat ve yoğuşmayı birbirinden ayırıyor."),
    ("Kiracıyım, ev sahibine teklif sunabilir misiniz?",
     "Evet, yapılacak işi kalem kalem yazılı veriyoruz; ev sahibinize iletebilirsiniz."),
],
},

# ───────────────────────────────────────────────────────────────────────────
"cati-izolasyon": {
"giris": [
    "Çatı binanın şemsiyesi. Ve şemsiyedeki küçük bir delik, bütün evi ıslatır :) Bartın gibi "
    "bol yağış alan bir şehirde çatıyı ihmal etmenin bedelini genelde en üst kattaki komşu "
    "tavandaki lekeyle öder.",
    "Biz Arslankaya İnşaat olarak **yeni çatı yapımı, çatı aktarma, kiremit değişimi, oluk-dere "
    "ve su yalıtımı** işlerini yapıyoruz. Teras ve düz çatılarda membran yalıtım da "
    "kapsamımızda.",
],
"bolumler": [
    {"h": "Çatı Aktarma mı, Yeni Çatı mı?",
     "p": ["Çatı aktarma; kiremitlerin sökülüp altındaki su yalıtım örtüsünün ve çıtaların "
           "kontrol edilmesi, gerekenlerin yenilenip kiremitlerin yeniden dizilmesi demek. Kırık "
           "kiremitler bu sırada değiştiriliyor.",
           "Ama bazen ahşap konstrüksiyon çürümüş, örtü tamamen dağılmış oluyor. Bu durumda "
           "aktarma kurtarmaz, çatının yenilenmesi gerekir. Hangisinin gerektiğini çatıya çıkıp "
           "**fotoğraflarla size göstererek** anlatıyoruz; \"bize güvenin\" demiyoruz."],
     "kutu": ("Tavsiyemiz", "Çatı teklifi alırken kiremit altına hangi su yalıtım örtüsünün "
              "serileceğini sorun. Kiremit görünen kısım, ama asıl su yalıtımını altındaki örtü "
              "yapar.")},
    {"h": "Sızıntılar Aslında Nereden Geliyor?",
     "p": ["Sahada gördüğümüz şu: sızıntıların büyük kısmı kiremitin kendisinden değil, "
           "**birleşim noktalarından** geliyor:"],
     "liste": ["Baca dipleri ve çatıya oturan duvar birleşimleri",
               "Mahya ve dere (iki çatı yüzeyinin birleştiği oluk) hatları",
               "Tıkalı ya da ters eğimli oluklar",
               "Çatı pencereleri ve havalandırma çıkışları"]},
    {"h": "Teras ve Düz Çatılarda Su Yalıtımı",
     "p": ["Teras çatıda su alıyorsa önce suyun girdiği nokta tespit ediliyor. Çoğu durumda "
           "**eğim düzeltmesi ve membran yalıtımın yenilenmesi** gerekiyor. Su birikintisi "
           "yapan bir terasın üstüne ne kadar iyi malzeme koyarsanız koyun, eğim yanlışsa "
           "sorun geri gelir..",
           "Çatı ısı yalıtımını da bu işle birlikte düşünmenizi öneririz; detayını "
           "[[mantolama-yalitim|mantolama ve yalıtım]] sayfamızda anlattık."]},
    {"h": "Çatı İşi Hangi Mevsimde Yapılır?",
     "p": ["Kuru havalar tercih ediliyor. Ama tavanınızdan su damlıyorsa beklemenize gerek "
           "yok: geçici önlem alıp asıl işi uygun havaya planlıyoruz. Çatıdan kaynaklanan "
           "küçük onarımlar için [[tadilat-tamirat|tadilat ve tamirat]] sayfamıza da "
           "bakabilirsiniz."]},
],
"sss": [
    ("Çatı aktarma ne demek?",
     "Kiremitlerin sökülüp altındaki örtü ve çıtaların kontrol edilmesi, gerekenlerin yenilenmesi "
     "ve kiremitlerin yeniden dizilmesi. Kırık kiremitler değiştiriliyor."),
    ("Tavandan su damlıyor, hemen gelir misiniz?",
     "Arayın, durumu konuşalım. Acil durumda önce geçici önlemle suyu kesiyor, asıl işi uygun "
     "havaya planlıyoruz."),
    ("Teras çatıda su alıyor, ne yapılır?",
     "Önce suyun girdiği nokta tespit ediliyor. Çoğu durumda eğim düzeltmesi ve membran "
     "yalıtımın yenilenmesi gerekiyor."),
    ("Apartman çatısı için karar gerekir mi?",
     "Çatı ortak alan sayıldığı için genellikle kat malikleri kararı gerekiyor. Teklifi "
     "yönetime sunulacak şekilde yazılı hazırlıyoruz."),
],
},

# ───────────────────────────────────────────────────────────────────────────
"boya-badana-alci": {
"giris": [
    "Boya işini dışarıdan bakınca \"rulo al, sür\" gibi görürsünüz :) Ama iyi bir boyanın "
    "**yarısı hazırlıktır.** Çatlakları açıp doldurmak, zımparalamak, astar atmak, prizleri "
    "bantlamak, eşyaları korumak.. Bunlar en az boyanın kendisi kadar zaman alıyor.",
    "Biz Arslankaya İnşaat olarak iç-dış boya, saten alçı, kartonpiyer ve alçıpan "
    "uygulamalarını aynı ekiple yapıyoruz.",
],
"bolumler": [
    {"h": "Boya ve Alçı İşlerinde Neler Yapıyoruz?",
     "liste": ["İç cephe boya ve badana",
               "Dış cephe boyası — cephe yenilemesiyle birlikte [[ic-dis-cephe|iç ve dış cephe]] sayfamızda",
               "Saten alçı ve perdah",
               "Alçıpan bölme duvar ve asma tavan",
               "Kartonpiyer ve stor perde kutusu",
               "Rutubetli duvarda hazırlık ve özel astar"]},
    {"h": "Bir Odayı Nasıl Boyuyoruz?",
     "p": ["Eşyaları örtüyor, prizleri ve süpürgelikleri bantlıyoruz. Çatlak ve kabarmaları "
           "açıp dolduruyoruz, zımpara ve astardan sonra **iki kat boya** uyguluyoruz. İş bitince "
           "çalışılan alanı temizleyip öyle teslim ediyoruz.",
           "Tek kat boyayla \"idare eder\" diyenler oluyor; kısa vadede ucuz görünür ama renk "
           "eşit oturmaz, eski renk alttan gölge yapar."]},
    {"h": "Küf Yapan Duvara Boya Yeter mi?",
     "p": ["Yetmez.. Bunu bilerek söylüyoruz çünkü en sık aldığımız taleplerden biri "
           "\"küfün üstünü boyayalım\". Bartın'da özellikle kuzey cephelerde ve banyo-mutfak "
           "duvarlarında küf çok yaygın.",
           "Önce küf temizleniyor, sonra **nemin kaynağı** bulunuyor. Kaynak yoğuşmaysa "
           "[[mantolama-yalitim|mantolama]], sızıntıysa [[cati-izolasyon|çatı]] ya da tesisat "
           "onarımı gerekiyor. Ancak ondan sonra küf önleyici astar ve nefes alan boya işe yarar."],
     "kutu": ("Dikkat", "Küf önleyici boya, nem sorunu çözülmemiş bir duvarda küfü sadece "
              "erteler. Boyaya para vermeden önce kaynağı çözdürün.")},
],
"sss": [
    ("Bir daire boyası kaç gün sürer?",
     "Dairenin büyüklüğüne, alçı tamiri gerekip gerekmediğine ve renk sayısına göre değişiyor. "
     "Keşifte süreyi netleştiriyoruz."),
    ("Boyayı ben alabilir miyim?",
     "Evet. Malzemeyi siz alabilir ya da bize bırakabilirsiniz; hangi üründen ne kadar "
     "gerektiğini önceden söylüyoruz."),
    ("Saten alçı her duvara gerekir mi?",
     "Hayır. Duvar düzgünse astar ve boya yeterli olabilir. Bozuk, dalgalı duvarlarda saten alçı "
     "boyanın düzgün görünmesini sağlıyor."),
    ("Eşyalar ne olacak?",
     "Eşyaları odanın ortasına toplayıp örtüyoruz; boşaltmanız gerekmiyor."),
],
},

# ───────────────────────────────────────────────────────────────────────────
"seramik-fayans": {
"giris": [
    "Seramikte işin görünen kısmı derz çizgisi, görünmeyen kısmı ise **altındaki zemin.** "
    "Eğri bir şap ya da su yalıtımı yapılmamış bir banyo zemini, en pahalı seramiği de kısa "
    "sürede bozar.",
    "Biz Arslankaya İnşaat olarak banyo, mutfak, balkon ve zeminlerde seramik, fayans ve granit "
    "döşüyoruz. Ama döşemeden önce mutlaka zemini ve yalıtımı kontrol ediyoruz.",
],
"bolumler": [
    {"h": "Seramik ve Fayans İşlerinde Neler Yapıyoruz?",
     "liste": ["Banyo ve mutfak fayansı", "Zemin seramiği ve granit",
               "Balkon ve teras kaplaması", "Islak hacimlerde **su yalıtımı**",
               "Eski kaplama söküm ve yenileme", "Derz dolgu ve silikon yenileme"]},
    {"h": "Islak Hacimde Su Yalıtımı Neden Şart?",
     "p": ["Seramik su geçirmez ama derz geçirir. Banyoda yalıtım yapılmadıysa su derzden "
           "sızar, alt kattaki komşunun tavanına iner. O yüzden duş alanında ve banyo zemininde "
           "seramikten önce **su yalıtımı sürülüyor**, köşelere de yalıtım bandı konuyor.",
           "Bunu atlayan teklif ucuz görünür, ama alt kattan gelecek ilk şikâyette o fark "
           "fazlasıyla geri ödenir :)"]},
    {"h": "Balkon ve Terasta Hangi Seramik Kullanılmalı?",
     "p": ["Balkon ve teras zeminlerinde **dona dayanıklı ve kaymaz** seramik ile **esnek "
           "(yüksek performanslı) yapıştırıcı** kullanılması gerekiyor. Kışın iç mekân "
           "seramiğinin balkonda çatladığını, kabardığını sık görüyoruz.",
           "Islakken kayganlaşan parlak yüzeyli seramikleri ise banyo zemini ve balkonda "
           "önermiyoruz."],
     "kutu": ("Tavsiyemiz", "Seramik seçerken kutusundaki kaymazlık ve dış mekân bilgisine "
              "bakın; emin değilseniz fotoğrafını gönderin, kullanım yerine uygun mu söyleyelim.")},
    {"h": "Eski Fayansın Üzerine Yenisi Döşenir mi?",
     "p": ["Bazı durumlarda mümkün, ama önermediğimiz durumlar çok. Eski kaplama sağlam "
           "değilse, kot farkı kapı ve gider seviyesini bozacaksa sökmek gerekiyor. Keşifte "
           "eski kaplamaya vurup boşluk yapıp yapmadığına bakıyoruz.",
           "Banyo komple yenilenecekse [[tadilat-tamirat|tadilat ve tamirat]], bütün daire "
           "elden geçecekse [[anahtar-teslim-yenileme|anahtar teslim yenileme]] sayfamıza da "
           "göz atın."]},
],
"sss": [
    ("Banyo yenileme ne kadar sürer?",
     "Tesisat değişip değişmediğine ve kuruma sürelerine göre değişiyor. Keşifte iş programını "
     "veriyoruz."),
    ("Seramiği siz mi alıyorsunuz?",
     "İsterseniz biz alıyoruz, isterseniz siz seçip alıyorsunuz; işçilik ayrıca fiyatlanıyor."),
    ("Büyük ebat seramik döşüyor musunuz?",
     "Evet. Büyük ebatlı seramikte zemin düzgünlüğü daha da kritik; gerekiyorsa önce tesviye "
     "yapıyoruz."),
    ("Derzler kararmış, sadece derz yenilenir mi?",
     "Evet, seramik sağlamsa eski derz kazınıp yenilenebiliyor."),
],
},

# ───────────────────────────────────────────────────────────────────────────
"ic-dis-cephe": {
"giris": [
    "Dış cephe binanın hem kalkanı hem kartvizitidir. Dökülen sıva, solmuş boya, çatlaklar.. "
    "Bunlar sadece görüntü sorunu değil; **suyun duvarın içine girmesinin yolu.**",
    "Biz Arslankaya İnşaat olarak cephe yenilemede sıva tamiri, boya, kaplama ve gerekiyorsa "
    "mantolama işlerini birlikte ele alıyoruz. İç mekânda da dekoratif duvar uygulamaları "
    "yapıyoruz.",
],
"bolumler": [
    {"h": "Cephe İşlerinde Neler Yapıyoruz?",
     "liste": ["Dış cephe sıva tamiri ve yenileme", "Dış cephe boyası",
               "Kompozit, taş ve dekoratif kaplama", "Söve, denizlik ve parapet işleri",
               "Cephe çatlak ve derz onarımı", "İç mekânda dekoratif duvar uygulamaları"]},
    {"h": "Cephe Yenileme Nasıl Yapılır?",
     "p": ["Cephe işleri iskele gerektiriyor; iskele organizasyonunu iş kapsamında planlıyoruz. "
           "Sonra sırasıyla:"],
     "liste": ["Cephe yüzeyine vurularak **boşluk yapan, kabaran sıva** tespit ediliyor ve sökülüyor.",
               "Çatlaklar açılıp uygun malzemeyle dolduruluyor.",
               "Söve, denizlik ve pencere kenarlarındaki su yolları kontrol ediliyor.",
               "Astardan sonra seçilen dış cephe boyası ya da kaplama uygulanıyor."]},
    {"h": "Bütün Cephe mi, Sadece Yıpranan Yüzler mi?",
     "p": ["Bartın'da rüzgârla gelen yağmur en çok **batı ve kuzey cepheleri** yıpratıyor. "
           "Bazen bütün cephe yerine sadece bu yüzlerin yenilenmesi yeterli oluyor; keşifte her "
           "yüzü ayrı ayrı değerlendiriyoruz. Gereksiz iş yazmıyoruz.",
           "Cephe zaten elden geçecekse aynı iskeleyle **mantolamayı da yapmak** çok daha "
           "ekonomik. Bu konuyu [[mantolama-yalitim|mantolama ve yalıtım]] sayfamızda ayrıca "
           "anlattık."],
     "kutu": ("Tavsiyemiz", "Cephe boyası ile mantolamayı ayrı yıllarda yaptırmak iki kez iskele "
              "kurdurmak demek. İkisi de planınızdaysa aynı anda yaptırın.")},
    {"h": "Apartmanlarda Karar Süreci",
     "p": ["Dış cephe ortak alan sayıldığı için apartmanlarda genellikle kat malikleri kurulu "
           "kararı gerekiyor. Teklifimizi **yönetime sunulacak şekilde**, kalem kalem yazılı "
           "hazırlıyoruz ki toplantıda herkes neye onay verdiğini görsün.",
           "İç cephede boya ve alçı işleri için [[boya-badana-alci|boya, badana ve alçı]] "
           "sayfamıza bakabilirsiniz."]},
],
"sss": [
    ("Dış cephe için kat malikleri kararı gerekir mi?",
     "Apartmanlarda ortak alan sayıldığı için genellikle gerekiyor. Teklifi yönetime sunulacak "
     "şekilde hazırlıyoruz."),
    ("İskeleyi siz mi kuruyorsunuz?",
     "Cephe işinin gerektirdiği iskele organizasyonunu iş kapsamında planlıyoruz."),
    ("Cephe boyası kaç yılda bir yenilenir?",
     "Malzemeye, cephe yönüne ve bakıma göre değişiyor; sabit bir süre yok. Kuzey ve batı "
     "cepheleri daha çabuk yıpranıyor."),
    ("Müstakil evim için de geliyor musunuz?",
     "Evet, müstakil ev ve küçük binalar için de cephe işi yapıyoruz."),
],
},

# ───────────────────────────────────────────────────────────────────────────
"mantolama-yalitim": {
"giris": [
    "Kışın kalorifer yanıyor ama ev bir türlü ısınmıyor mu? Kuzey odanın köşesinde her yıl aynı "
    "küf çıkıyor mu? Bartın'da mantolamasız eski binalarda bu ikisini **neredeyse her evde** "
    "görüyoruz.",
    "Mantolama, binanın dış yüzünü ısı yalıtım levhalarıyla kaplayıp file, sıva ve son kat "
    "boyayla kapatma işi. Kışın ısının dışarı, yazın sıcağın içeri geçmesini azaltıyor; "
    "**duvar terlemesini ve yoğuşma küfünü de** büyük ölçüde kesiyor.",
],
"bolumler": [
    {"h": "Mantolama Hangi Aşamalardan Oluşur?",
     "liste": ["Cephe yüzeyinin temizlenmesi ve bozuk sıvanın onarılması",
               "Isı yalıtım levhalarının yapıştırılması",
               "Levhaların **dübelle** cepheye sabitlenmesi",
               "File gömülü ilk kat sıva",
               "İkinci kat sıva ve dekoratif son kat",
               "Pencere kenarı, köşe ve denizliklerde özel profiller"],
     "son": ["Pencere kenarları ve köşeler mantolamanın en hassas yerleri. Buralar düzgün "
           "çözülmezse **ısı köprüsü** kalır; yani o noktadan ısı kaçmaya, iç yüzeyde terleme "
           "olmaya devam eder."]},
    {"h": "EPS mi, Taşyünü mü?",
     "p": ["En çok sorulan soru bu :) Kısaca:"],
     "liste": ["**EPS (beyaz/gri strafor levha):** daha ekonomik, yaygın, uygulaması kolay.",
               "**Taşyünü:** yanmazlık ve ses yalıtımında öne çıkıyor, maliyeti daha yüksek."],
     "kutu": ("Tavsiyemiz", "Yalıtım kalınlığını \"komşu kaç santim yaptırdıysa\" diye değil, "
              "binanın durumuna ve ısı yalıtım hesabına göre belirleyin. İnce levha ucuza gelir "
              "ama beklediğiniz tasarrufu vermez.")},
    {"h": "Mantolama Hangi Mevsimde Yapılır?",
     "p": ["Yapıştırıcı ve sıvaların düzgün kuruması için **yağışsız ve çok soğuk olmayan** "
           "günler gerekiyor. Bartın'da bu, takvimi hava durumuna göre esnek tutmak demek. "
           "Yağmurlu bir haftada iş bekler; ama yağmur altında sıva atılmış bir cephe yıllarca "
           "sorun çıkarır.."]},
    {"h": "Apartmanda Mantolama İçin Karar Nasıl Alınır?",
     "p": ["Apartmanlarda mantolama için kat malikleri kurulu kararı gerekiyor; ısı yalıtımı "
           "işlerinde çoğunluk kararı yeterli olabiliyor. Bunu yönetiminizle teyit edin. Biz "
           "teklifi yönetime sunulacak şekilde kalem kalem hazırlıyoruz.",
           "Tek daire mantolama teknik olarak mümkün, ama bütün cephe yapıldığında hem daha "
           "verimli hem de görünüş olarak daha düzgün oluyor. Cephe zaten yenilenecekse "
           "[[ic-dis-cephe|iç ve dış cephe uygulamaları]] ile birlikte planlayın."]},
],
"sss": [
    ("EPS mi taşyünü mü?",
     "EPS daha ekonomik, taşyünü yanmazlık ve ses yalıtımında öne çıkıyor. Bina yüksekliği ve "
     "beklentiye göre birlikte karar veriyoruz."),
    ("Mantolama küfü keser mi?",
     "Küf yoğuşmadan kaynaklanıyorsa büyük ölçüde keser, çünkü duvarın iç yüzeyi artık soğumaz. "
     "Kaynak sızıntıysa önce o çözülmeli."),
    ("Tek daire mantolama yapılır mı?",
     "Teknik olarak mümkün ama bütün cephe yapıldığında daha verimli ve düzgün oluyor. "
     "Apartmanda yönetim kararı gerekiyor."),
    ("İçeriden yalıtım yapılabilir mi?",
     "Dış cepheye dokunulamayan durumlarda iç cepheden ısı yalıtımı da yapıyoruz; oda biraz "
     "küçülür, keşifte artı ve eksisini konuşuyoruz."),
],
},

# ───────────────────────────────────────────────────────────────────────────
"beton-kalip-demir": {
"giris": [
    "Betonarmenin dayanımı, projede yazan demirin **doğru çapta, doğru aralıkla ve doğru pas "
    "payıyla** yerine konmasına bağlı. Kâğıt üstünde mükemmel bir statik proje, sahada "
    "eksik bağlanmış bir etriyeyle boşa gidebilir.",
    "Biz Arslankaya İnşaat olarak kalıp, demir ve beton işlerini yapı sahiplerine ve "
    "müteahhitlere ayrı ayrı ya da birlikte veriyoruz.",
],
"bolumler": [
    {"h": "Beton, Kalıp ve Demir İşlerinde Neler Yapıyoruz?",
     "liste": ["Ahşap ve plywood kalıp", "Demir kesim, büküm ve bağlama",
               "Pas payı takozlarının yerleştirilmesi", "Beton döküm ve vibrasyon",
               "Beton kürü", "İstinat duvarı, perde, merdiven ve garaj döşemesi betonları"]},
    {"h": "Beton Dökülmeden Önce Neler Kontrol Edilir?",
     "p": ["Kalıp ölçüsü ve demir yerleşimi projeyle karşılaştırılıyor; kolon etriyeleri, "
           "kiriş-kolon birleşimleri ve pas payları tek tek kontrol ediliyor. **Yapı denetim "
           "onayı alınmadan beton siparişi verilmiyor.**",
           "Döküm sırasında vibratör kullanılıyor ki betonda boşluk (çakıl yuvası) kalmasın. "
           "Ardından beton günlerce nemli tutularak kür ediliyor."],
     "kutu": ("Önemli", "Kalıp söküm ve yük bindirme süreleri betonun sınıfına ve havaya göre "
              "değişir. Döşeme altındaki dikmeleri \"beton sertleşti\" diye erken sökmek, en "
              "sık yapılan ve en tehlikeli hatalardan biridir.")},
    {"h": "Bartın Havasında Beton Dökümü",
     "p": ["Sıcak ve rüzgârlı günlerde betonun yüzeyi hızlı kuruyup çatlayabiliyor; soğuk "
           "günlerde ise donma riski var. Yağmur da apayrı bir konu :) O yüzden **döküm gününü "
           "hava tahminine göre** belirliyoruz. Bir iki gün kaydırmak, yanlış günde dökülmüş "
           "bir döşemeyle uğraşmaktan her zaman daha ucuz."]},
    {"h": "Taşeron Olarak Çalışıyor musunuz?",
     "p": ["Evet. Müteahhitlere yalnız kalıp, yalnız demir ya da ikisini birlikte işçilik olarak "
           "veriyoruz. Detaylar için [[muteahhitlere-ozel-insaat-hizmetleri|müteahhitlere özel "
           "hizmetler]] sayfamıza bakabilirsiniz. Binanın tamamı için ise "
           "[[kaba-insaat|kaba inşaat işleri]] sayfamız daha uygun."]},
],
"sss": [
    ("Sadece demir ya da sadece kalıp işi veriyor musunuz?",
     "Evet, müteahhitlere taşeron olarak yalnız kalıp ya da yalnız demir işçiliği de veriyoruz."),
    ("Beton dökümünden sonra ne kadar beklenir?",
     "Kalıp alma ve yük bindirme süreleri betonun sınıfına ve havaya göre değişiyor; proje ve "
     "yapı denetim kurallarına uyuyoruz."),
    ("Küçük betonarme işler yapıyor musunuz?",
     "İstinat duvarı, merdiven, garaj döşemesi gibi işleri de yapıyoruz."),
    ("Beton kürü neden önemli?",
     "Beton suyla dayanım kazanır. İlk günlerde kuruyan beton hem yüzeyden çatlar hem de "
     "hedeflenen dayanıma ulaşamaz; o yüzden düzenli sulanır ya da örtülür."),
],
},

# ───────────────────────────────────────────────────────────────────────────
"duvar-siva": {
"giris": [
    "Düz bir duvar, üzerine gelen her işi kolaylaştırır: seramik düzgün oturur, dolap boşluk "
    "vermez, boya pürüzsüz çıkar. Eğri bir duvar ise kendinden sonra gelen her ustayı "
    "uğraştırır :)",
    "Biz Arslankaya İnşaat olarak duvar örümünde **şakul ve teraziyi**, sıvada da **mastar "
    "düzgünlüğünü** işin temel ölçüsü sayıyoruz.",
],
"bolumler": [
    {"h": "Duvar ve Sıva İşlerinde Neler Yapıyoruz?",
     "liste": ["Tuğla, gazbeton ve bims duvar örümü", "Bölme duvar ve lento",
               "Kaba ve ince iç sıva", "Dış cephe sıvası", "Makine sıvası",
               "Sıva filesi ve köşe profili uygulaması"]},
    {"h": "Gazbeton mu, Tuğla mı, Bims mi?",
     "liste": ["**Gazbeton:** hafif, ısı yalıtımı daha iyi, düzgün yüzeyli.",
               "**Tuğla:** yaygın ve çoğu zaman daha ekonomik.",
               "**Bims:** hafif ve yalıtımı iyi bir diğer seçenek."],
     "son": ["Hangisinin kullanılacağı projeye, duvarın dış duvar mı bölme mi olduğuna ve "
           "bütçeye göre belirleniyor. Keşifte artı ve eksilerini açıkça söylüyoruz."]},
    {"h": "Sıva Neden Çatlar?",
     "p": ["En sık iki sebep var: farklı malzemelerin (örneğin beton kolon ile tuğla duvar) "
           "birleştiği yerde **file kullanılmaması** ve sıvanın **çok hızlı kuruması.** Biz "
           "birleşim yerlerine file, köşelere profil koyuyoruz; sıcak ve rüzgârlı günlerde de "
           "sıvayı nemli tutuyoruz.",
           "Dış duvarlarda yağışlı iklim yüzünden doğru sıva seçimi ayrıca önemli. Yanlış "
           "sıva Bartın'ın yağmurunda kısa sürede kabarıp dökülüyor."],
     "kutu": ("Dikkat", "Sıvadan önce elektrik ve su tesisatı kanalları mutlaka açılıp "
              "kapatılmış olmalı. Sıva bittikten sonra açılan her kanal, yama izi olarak "
              "boyanın altından görünür.")},
    {"h": "Sıvadan Sonra Ne Geliyor?",
     "p": ["Sıva bittiğinde sırada alçı, boya ve kaplamalar var. Devamı için "
           "[[ince-insaat|ince inşaat işleri]] ve [[boya-badana-alci|boya, badana ve alçı]] "
           "sayfalarımıza göz atabilirsiniz."]},
],
"sss": [
    ("Gazbeton mu tuğla mı?",
     "Gazbeton hafif ve ısı yalıtımı daha iyi; tuğla daha ekonomik olabiliyor. Projeye ve "
     "kullanım yerine göre öneriyoruz."),
    ("Sıva çatlaması neden olur?",
     "Farklı malzemelerin birleşim yerlerinde file kullanılmaması ve sıvanın hızlı kuruması en "
     "yaygın sebepler."),
    ("Sadece sıva işi alıyor musunuz?",
     "Evet, tek daire ya da tek kat sıva işi de yapıyoruz."),
    ("Makine sıvası mı el sıvası mı?",
     "Geniş alanlarda makine sıvası hız kazandırıyor; küçük ve parçalı alanlarda el sıvası daha "
     "pratik. İşin büyüklüğüne göre öneriyoruz."),
],
},

# ───────────────────────────────────────────────────────────────────────────
"yikim-yenileme": {
"giris": [
    "Yenilemenin ilk adımı çoğu zaman yıkımdır: bir duvarın kaldırılması, eski banyonun "
    "sökülmesi ya da binanın tamamen yıkılıp yerine yenisinin yapılması.",
    "Bir konuda çok net söyleyelim: **taşıyıcı bir elemana dokunulacaksa** işe statik "
    "değerlendirme olmadan başlamıyoruz. \"Şu duvarı kaldırsak salon büyür\" dediğiniz duvar "
    "bazen binayı taşıyan duvar olabiliyor..",
],
"bolumler": [
    {"h": "Yıkım ve Yenilemede Neler Yapıyoruz?",
     "liste": ["İç mekân söküm ve kırım", "Taşıyıcı olmayan bölme duvar kaldırma",
               "Seramik, şap ve sıva sökümü", "İzinli komple bina yıkımı",
               "Moloz toplama ve döküm", "Yıkım sonrası yeniden yapım"]},
    {"h": "Bina Yıkımından Önce Neler Gerekir?",
     "liste": ["Belediyeden **yıkım izni**",
               "Elektrik, su ve doğalgaz aboneliklerinin kapatılması",
               "Çevre binalar, yol ve yayalar için güvenlik önlemleri",
               "Eski yapıda zararlı malzeme şüphesi varsa uzman tespiti"],
     "kutu": ("Önemli", "Eski binalarda çatı ya da tesisat elemanlarında asbest bulunabiliyor. "
              "Böyle bir şüphe varsa söküm, bu konuda yetkili ekiplerce yapılmalı. Bunu "
              "keşifte mutlaka konuşuyoruz.")},
    {"h": "Yıkımla Yeni Yapım Aynı Ekipte Olursa",
     "p": ["Kentsel dönüşüm ve eski yapı yenilemelerinde yıkımla yeni yapımın aynı ekipte "
           "olması **takvimde ve moloz organizasyonunda** ciddi zaman kazandırıyor. Bir ekip "
           "işi bitirip gidiyor, diğeri gelene kadar arsa haftalarca boş beklemiyor.",
           "Yeni bina için [[temelden-catiya-insaat|temelden çatıya inşaat]], iç mekân "
           "yenilemesi için de [[anahtar-teslim-yenileme|anahtar teslim yenileme]] sayfalarımıza "
           "bakabilirsiniz."]},
],
"sss": [
    ("Duvar kaldırmak için izin gerekir mi?",
     "Taşıyıcı olmayan bölme duvarlar için genellikle gerekmiyor; taşıyıcı elemana dokunulacaksa "
     "statik değerlendirme ve izin şart."),
    ("Bir duvarın taşıyıcı olup olmadığını nasıl anlarım?",
     "Göz kararıyla anlaşılmaz. Projeye bakılıyor, gerekirse statik mühendis görüşü alınıyor."),
    ("Moloz kimin sorumluluğunda?",
     "Moloz toplama ve döküm işini iş kapsamına dahil ediyoruz."),
    ("Yıkımdan sonra yeniden yapımı da üstleniyor musunuz?",
     "Evet, yıkım ve yeni yapım aynı ekiple yürüyebiliyor."),
],
},

# ───────────────────────────────────────────────────────────────────────────
"anahtar-teslim-yenileme": {
"giris": [
    "Bir daireyi ya da dükkânı baştan yenilemek isteyen herkesin en büyük korkusu aynı: "
    "\"Her gün ayrı bir ustayı mı bekleyeceğim?\" :)",
    "Anahtar teslim yenilemede **tek muhatabınız biziz.** Dairenizi ya da iş yerinizi boş "
    "teslim alıyor, söküm, tesisat, alçı, boya, zemin, banyo, mutfak ve aydınlatmaya kadar "
    "bütün işleri tek takvimde yürütüp kullanıma hazır geri veriyoruz.",
],
"bolumler": [
    {"h": "Anahtar Teslim Yenilemeye Neler Dahil?",
     "liste": ["Keşif, metraj ve yazılı iş programı",
               "Söküm ve moloz — bkz. [[yikim-yenileme|yıkım ve yenileme]]",
               "Elektrik ve su tesisatı yenileme",
               "Alçı, boya ve asma tavan",
               "Zemin kaplama, [[seramik-fayans|seramik]] ve parke",
               "Banyo ve mutfak yenileme",
               "İş yerinde vitrin, bölme ve dekorasyon",
               "Teslim temizliği"]},
    {"h": "Süreç Nasıl İşliyor?",
     "p": ["Keşifte yapılacak işler **kalem kalem yazılıyor**, malzeme seçimleri sizinle "
           "yapılıyor ve iş programı çıkıyor. İş boyunca ilerlemeyi fotoğraflarla paylaşıyoruz. "
           "Teslimde de bir **eksik listesini** birlikte dolaşıp kontrol ediyoruz; liste "
           "kapanmadan iş bitmiş sayılmıyor."],
     "kutu": ("Tavsiyemiz", "Teklifte \"daire yenileme — X TL\" gibi tek satırlık rakamlara "
              "dikkat edin. Neyin dahil neyin hariç olduğu yazmıyorsa, sonradan çıkan her iş "
              "\"ek iş\" olur.")},
    {"h": "İş Yerlerinde Kapalı Kalma Süresi",
     "p": ["İş yerinde kapalı kalınan her gün kayıp. O yüzden ticari mekânlarda işleri **mesai "
           "dışına ya da bölüm bölüm** planlama seçeneğini de konuşuyoruz. Bu konudaki "
           "yaklaşımımızı [[ticari-isletmeler-ve-is-yeri-insaatlari|ticari işletmeler ve iş yeri "
           "inşaatları]] sayfamızda anlattık."]},
    {"h": "Sonradan Çıkan İşler Ne Olacak?",
     "p": ["Dürüst olalım; eski bir dairede duvarı açınca beklenmedik bir şey çıkabiliyor :) "
           "Böyle durumlarda işi durdurup size gösteriyor, ek işi **ayrıca konuşup onayınızla** "
           "yapıyoruz. Habersiz ek iş faturası çıkarmıyoruz."]},
],
"sss": [
    ("Anahtar teslim fiyatına neler dahil?",
     "Keşifte yazılı hale gelen her kalem dahil. Sonradan çıkan ek işler ayrıca konuşulup "
     "onayınızla yapılıyor."),
    ("İş yeri yenilemede dükkân kapalı kalmak zorunda mı?",
     "Her işte değil. Bazı işleri mesai dışına ya da bölüm bölüm planlayabiliyoruz."),
    ("Malzeme seçimini kim yapıyor?",
     "Seçimi siz yapıyorsunuz; biz bütçeye ve kullanım yerine uygun seçenekleri öneriyoruz."),
    ("İş sürerken evde kalabilir miyim?",
     "Komple yenilemede genellikle önermiyoruz; toz, gürültü ve kullanılamayan banyo-mutfak "
     "yüzünden hem sizin hem işin rahatı için daire boş olmalı."),
],
},
}


# ═══════════════════════════════════════════════════════════════════════════
# Çalışma alanı sayfaları (2026-10-20: kullanıcı "çok kısa ve birbirine benziyor" dedi).
# ⚠️ Her sayfa KENDİ derdini anlatır; ortak cümle tekrarı yok. Aynı kurallar: teyitsiz iddia yok,
#    geçmiş ihale/proje UYDURMA yok (firma gerçek iş verince referans panelinden eklenir).
# Görseller: data.ALAN_GORSEL (Unsplash Lisansı, img/stok/).
# ═══════════════════════════════════════════════════════════════════════════
ALAN_ICERIK = {

"muteahhitlere-ozel-insaat-hizmetleri": {
"giris": [
    "Müteahhit olarak sizin derdiniz belli: bina zamanında bitsin, yapı denetim takılmasın, "
    "bir ekibin bıraktığı iş bir sonrakini uğraştırmasın.. Taşeron seçerken aslında fiyattan "
    "çok bu üçünü satın alıyorsunuz :)",
    "Biz Arslankaya İnşaat olarak müteahhitlere kaba inşaattan ince işe kadar **tek kalem ya da "
    "paket halinde** taşeron olarak çalışıyoruz.",
],
"bolumler": [
    {"h": "Hangi Kalemleri Taşeron Olarak Alıyoruz?",
     "liste": ["[[beton-kalip-demir|Kalıp, demir ve beton]] işçiliği",
               "[[kaba-insaat|Kaba inşaat]] (temelden çatı karkasına)",
               "[[duvar-siva|Duvar örümü ve sıva]]", "[[mantolama-yalitim|Mantolama ve yalıtım]]",
               "[[cati-izolasyon|Çatı konstrüksiyonu ve kaplama]]",
               "[[ince-insaat|İnce işler]]: şap, alçı, boya, seramik"],
     "son": ["İşin tamamını vermek zorunda değilsiniz. \"Kaba bizde, mantolama sizde\" gibi "
             "parçalı anlaşmalar da yapıyoruz."]},
    {"h": "Bir Müteahhidin Taşerondan Beklediği Üç Şey",
     "liste": ["**Takvime uymak.** İş programını baştan yazılı veriyoruz; Bartın'ın yağışlı "
               "günlerini de bu programa pay olarak koyuyoruz ki sürpriz olmasın.",
               "**Yapı denetimde takılmamak.** Demir ve kalıp kontrollerine sahayı hazır "
               "teslim ediyoruz; kontrol tutanağı imzalanmadan beton siparişi verilmiyor.",
               "**Bir sonraki ekibe temiz iş bırakmak.** Şakulünde duvar, mastarında sıva, "
               "temizlenmiş kat. Sıvacının duvarcıya, boyacının sıvacıya kızmadığı bir şantiye :)"]},
    {"h": "Ölçü ve Hakediş Nasıl Yapılıyor?",
     "p": ["Birim fiyatla mı (metrekare, metreküp, ton) yoksa götürü bedelle mi çalışılacağını "
           "işin başında konuşuyoruz. Hakedişler aşama ya da kat bazlı yapılabiliyor; ölçünün "
           "nasıl alınacağı (net mi, brüt mü, boşluklar düşülecek mi) sözleşmede yazılı oluyor."],
     "kutu": ("Tavsiyemiz", "Taşeron sözleşmesinde metraj yöntemini mutlaka yazın. Anlaşmazlıkların "
              "çoğu fiyattan değil, \"pencere boşluğu düşülecek miydi?\" gibi ölçü sorularından çıkar..")},
    {"h": "Sahada İş Güvenliği",
     "p": ["Baret, emniyet kemeri, korkuluk, iskele bağlantısı.. Bunlar bizim için pazarlık konusu "
           "değil. Şantiyenin genel iş güvenliği düzeni sizin iş güvenliği uzmanınızla birlikte "
           "yürüyor; biz kendi ekibimizin kurallara uymasından sorumluyuz."]},
],
"sss": [
    ("Sadece işçilik mi veriyorsunuz?",
     "Çoğunlukla malzemesi müteahhitten işçilik çalışıyoruz; malzeme dahil seçeneğini de işin "
     "kalemine göre konuşabiliyoruz."),
    ("Birden fazla bloğu aynı anda yürütebilir misiniz?",
     "Bu, iş kalemine ve takvime bağlı. Keşifte ekip planını açıkça konuşuyoruz; yetişmeyecek işi "
     "\"yetişir\" diye almıyoruz."),
    ("Hakediş nasıl yapılır?",
     "Aşama ya da kat bazlı hakediş yapılabiliyor; ölçü yöntemi sözleşmede yazılı oluyor."),
    ("Bartın dışındaki işlere geliyor musunuz?",
     "İşin büyüklüğüne ve yerine göre değişiyor; arayın, konuşalım."),
],
},

"bireysel-musterilere-ozel-hizmetler": {
"giris": [
    "Bir ev sahibi için tadilat ya da inşaat çoğu zaman hayatında bir iki kez yaptığı bir iş. "
    "Hangi usta ne yapar, teklif nasıl okunur, ne kadar sürer.. Bunları bilmemeniz çok normal.",
    "Biz Arslankaya İnşaat olarak bireysel müşterilerle çalışırken en çok **açık konuşmaya** "
    "özen gösteriyoruz: neyin neden yapılacağını inşaat jargonuna boğmadan anlatıyoruz.",
],
"bolumler": [
    {"h": "Ev Sahiplerinden En Sık Gelen İşler",
     "liste": ["[[temelden-catiya-insaat|Müstakil ev yapımı]] — arsadan anahtara",
               "[[tadilat-tamirat|Banyo ve mutfak yenileme]]",
               "[[cati-izolasyon|Çatı aktarma]] ve akıntı onarımı",
               "[[mantolama-yalitim|Mantolama]] — ısınmayan ev, küf yapan oda",
               "[[boya-badana-alci|Boya, badana ve alçı]]",
               "[[anahtar-teslim-yenileme|Daireyi komple yenileme]]"]},
    {"h": "Teklifi Nasıl Okumalısınız?",
     "p": ["İyi bir teklifte üç şey açık olmalı:"],
     "liste": ["**Kalemler:** \"Banyo yenileme — X TL\" değil; söküm, tesisat, yalıtım, seramik, "
               "vitrifiye ayrı ayrı.",
               "**Dahil ve hariçler:** malzeme kimden, moloz kimde, sonradan çıkacak işler nasıl "
               "konuşulacak.",
               "**Ödeme planı:** işin aşamalarına bağlı ödeme."],
     "kutu": ("Dikkat", "İşin tamamının parasını en başta peşin istenmesine onay vermeyin. "
              "Aşama bazlı ödeme hem sizi hem işi yapan ustayı korur.")},
    {"h": "Kat İlavesi Düşünüyorsanız",
     "p": ["En çok sorulan konulardan biri. Dürüst cevap: **her binaya kat çıkılmaz.** Mevcut "
           "binanın taşıyıcı sisteminin ek yükü kaldırıp kaldırmadığına statik mühendis karar "
           "verir, imar durumu da izin vermelidir. Ruhsatsız kat ilavesine girmiyoruz; hem "
           "sizin hem binadaki herkesin güvenliği için."]},
    {"h": "Apartmanda Tadilat Yaparken Komşular",
     "p": ["Gürültülü işleri (kırım, delme) apartman yönetiminin uygun gördüğü saatlere "
           "planlıyoruz, merdiven ve asansörü moloz taşırken koruyoruz. Cephe, çatı ya da "
           "mantolama gibi ortak alan işlerinde ise yönetim kararı gerekiyor; teklifi toplantıya "
           "sunulacak şekilde hazırlıyoruz."]},
],
"sss": [
    ("Küçük işlere de geliyor musunuz?",
     "Evet. Tek bir banyo, tek bir oda ya da çatıdaki bir akıntı için de arayabilirsiniz."),
    ("Önce fotoğraf göndersem fikir verir misiniz?",
     "Evet, WhatsApp'tan fotoğraf gönderirseniz kabaca fikir veriyoruz; kesin teklif yerinde "
     "gördükten sonra çıkıyor."),
    ("Malzemeyi ben seçebilir miyim?",
     "Elbette. Seçim sizin; biz kullanım yerine uygun mu, onu söylüyoruz."),
    ("Evde otururken iş yapılır mı?",
     "Çoğu tadilatta evet. Komple yenilemede ise evin boş olmasını öneriyoruz."),
],
},

"kamu-kurumlari-ve-devlet-projeleri": {
"giris": [
    "Kamu işinde inşaatın kendisi kadar **kağıt tarafı** da önemli: teknik şartname, birim "
    "fiyat pozları, metraj, ataşman, hakediş, iş güvenliği evrakı.. Sahada ne kadar iyi iş "
    "yaparsanız yapın, belgesi düzgün tutulmayan iş idareyle sorun yaşatır.",
    "Biz Arslankaya İnşaat olarak kamu kurumlarına ait yapılarda yapım, onarım, bakım ve "
    "yenileme işlerinde çalışıyoruz ve bu iki tarafı birlikte yürütmeye özen gösteriyoruz.",
],
"bolumler": [
    {"h": "Kamu Yapılarında Hangi İşleri Yapıyoruz?",
     "liste": ["Hizmet binalarında [[tadilat-tamirat|onarım ve tadilat]]",
               "[[cati-izolasyon|Çatı yenileme]] ve su yalıtımı",
               "[[mantolama-yalitim|Enerji verimliliği için mantolama]]",
               "[[ic-dis-cephe|Cephe yenileme]] ve boya",
               "[[kaba-insaat|Ek bina ve betonarme]] işler",
               "İç mekân [[boya-badana-alci|boya-alçı]] ve [[seramik-fayans|zemin]] yenileme"]},
    {"h": "Şartnameye Uygunluk ve Hakediş",
     "p": ["İşe teknik şartnameyi ve keşif özetini satır satır okuyarak başlıyoruz; "
           "şartnamede istenen malzeme ve uygulama dışına çıkılmıyor. Metraj ve ataşmanlar iş "
           "sırasında düzenli tutuluyor; hakediş günü \"o duvarın ölçüsü neydi\" diye "
           "aranmıyor :)",
           "Sonradan kapanacak işlerin (yalıtım, donatı, tesisat altyapısı gibi) **kapanmadan "
           "önce fotoğraflanması** bizim standart uygulamamız. Kontrol teşkilatı sorduğunda "
           "gösterecek bir şeyiniz olur."],
     "kutu": ("Önemli", "Kamu işlerinde iş artışı ya da değişiklik, idarenin yazılı onayı "
              "olmadan yapılmamalı. Sahada \"şunu da yapıverelim\" denen her iş, hakedişte sorun "
              "olarak geri döner.")},
    {"h": "Kullanım Devam Ederken Çalışmak",
     "p": ["Okul, sağlık tesisi ya da hizmet binası gibi yapılarda bina çoğu zaman tamamen "
           "boşaltılamıyor. Bu yüzden çalışma alanını fiziksel olarak ayırıyor, toz ve gürültü "
           "yapan işleri kullanımın en az olduğu saatlere ya da tatil dönemlerine planlıyoruz. "
           "Kullanıcıların güvenli geçiş yolları iş başlamadan belirleniyor."]},
],
"sss": [
    ("Kamu binalarında hangi işleri yapıyorsunuz?",
     "Onarım, tadilat, çatı, mantolama, cephe, boya-alçı, zemin yenileme ve betonarme işler."),
    ("Okul gibi binalarda iş ne zaman yapılır?",
     "Mümkünse tatil dönemlerine planlanır; değilse çalışma alanı ayrılıp gürültülü işler "
     "kullanımın az olduğu saatlere alınır."),
    ("Metraj ve ataşmanları kim tutuyor?",
     "İş sırasında düzenli olarak tutuyoruz; kapanacak imalatları kapanmadan fotoğraflıyoruz."),
    ("Şartnamede olmayan bir iş çıkarsa?",
     "İdareye bildiriliyor; yazılı onay gelmeden yapılmıyor."),
],
},

"ticari-isletmeler-ve-is-yeri-insaatlari": {
"giris": [
    "Bir ev tadilatı birkaç gün uzarsa canınız sıkılır; bir dükkân tadilatı birkaç gün uzarsa "
    "**kasanız** sıkılır.. Kira işliyor, personel bekliyor, müşteri kapıdan dönüyor.",
    "Biz Arslankaya İnşaat olarak mağaza, ofis, restoran-kafe, atölye ve depo gibi iş "
    "yerlerinde yapım ve yenileme yaparken takvimi **işletmenin çalışma düzenine göre** "
    "kuruyoruz.",
],
"bolumler": [
    {"h": "Hangi İş Yerlerinde Çalışıyoruz?",
     "liste": ["Mağaza ve dükkânlar — vitrin, zemin, duvar, aydınlatma altyapısı",
               "Ofisler — [[boya-badana-alci|alçıpan bölme]], asma tavan, zemin",
               "Restoran ve kafeler — ıslak zemin, [[seramik-fayans|kaymaz seramik]], mutfak alanı",
               "Atölye ve depolar — zemin betonu, duvar, [[cati-izolasyon|çatı]]",
               "Komple iş yeri yenileme — bkz. [[anahtar-teslim-yenileme|anahtar teslim yenileme]]"]},
    {"h": "Dükkânı Kapatmadan Tadilat Mümkün mü?",
     "p": ["Her işte değil ama çoğu işte kısmen evet. Kullandığımız yöntemler:"],
     "liste": ["**Mesai dışı çalışma:** gürültülü ve tozlu işler kapanıştan sonra ya da hafta sonu.",
               "**Bölüm bölüm ilerleme:** mağazanın yarısı açıkken diğer yarısında çalışmak.",
               "**Toz ayırma:** çalışılan alanı perdeyle kapatıp her gün temizleyip teslim etmek."],
     "son": ["Hangisinin uygun olduğu işin türüne ve mekânın düzenine bağlı; keşifte bunu açık "
             "açık konuşuyoruz. \"Hiç kapanmadan olur\" deyip sonra iki hafta kapattıran usta "
             "olmak istemiyoruz :)"]},
    {"h": "Açılış Tarihinden Geriye Planlama",
     "p": ["Yeni bir iş yeri açıyorsanız tarih genelde baştan belli: kira başlıyor, tabela "
           "sipariş edilmiş, açılış duyurulmuş. Biz de takvimi o tarihten geriye doğru kuruyoruz. "
           "Mobilya, tabela, mutfak ekipmanı gibi dış tedarikçilerin ne zaman sahaya gireceği de "
           "bu takvimin parçası."],
     "kutu": ("Tavsiyemiz", "İş yeri ruhsatı ve denetimlerde mekânda aranan şartlar (yangın, "
              "havalandırma, engelli erişimi gibi) işin türüne ve belediyeye göre değişir. "
              "Tadilata başlamadan bunları netleştirin; bittikten sonra duvar açmak her zaman "
              "daha pahalıdır.")},
],
"sss": [
    ("İş yeri yenilemede dükkân kapalı kalmak zorunda mı?",
     "Her işte değil. Bazı işleri mesai dışına ya da bölüm bölüm planlayabiliyoruz."),
    ("Gece ya da hafta sonu çalışıyor musunuz?",
     "İşin türüne ve binanın kurallarına göre mesai dışı çalışmayı planlayabiliyoruz."),
    ("Kiralık dükkânda tadilat yapılır mı?",
     "Evet; ama kalıcı değişiklikler için mülk sahibinin onayını almanızı öneririz."),
    ("Teklifi ne kadar sürede veriyorsunuz?",
     "Keşiften sonra iş kalemleri netleşince yazılı teklif hazırlıyoruz."),
],
},

"toplu-konut-ve-buyuk-olcekli-projeler": {
"giris": [
    "Tek bir binada iyi iş çıkarmak bir şey; on blokta, yüzlerce dairede **aynı kaliteyi** "
    "tutturmak bambaşka bir şey. Büyük projede asıl zorluk tekrar eden işin bir yerde "
    "gevşemesi.. Üçüncü blokta özenle yapılan köşe, yedinci blokta aceleye gelebiliyor.",
    "Biz Arslankaya İnşaat olarak toplu konut ve büyük ölçekli projelerde kaba ve ince iş "
    "kalemlerinde çalışırken bu gevşemeyi önleyecek bir düzenle ilerliyoruz.",
],
"bolumler": [
    {"h": "Hangi Kalemlerde Çalışıyoruz?",
     "liste": ["[[kaba-insaat|Kaba inşaat]] ve [[beton-kalip-demir|kalıp-demir-beton]]",
               "[[duvar-siva|Duvar ve sıva]]", "[[mantolama-yalitim|Mantolama]] ve [[ic-dis-cephe|cephe]]",
               "[[ince-insaat|İnce işler]]: şap, alçı, boya, seramik"]},
    {"h": "Önce Numune, Sonra Seri Uygulama",
     "p": ["Büyük projelerde işe **numune uygulamayla** başlamayı öneriyoruz: bir daire, bir "
           "cephe parçası ya da bir kat bütün detaylarıyla bitiriliyor, işveren ve kontrol "
           "ekibiyle birlikte onaylanıyor. Sonraki her uygulama o numuneye göre yapılıyor ve "
           "ona göre kontrol ediliyor.",
           "Böylece \"bu köşe nasıl dönülecekti\", \"süpürgelik nereye kadar\" gibi sorular "
           "her blokta yeniden tartışılmıyor."],
     "kutu": ("Önemli", "Numune onayını yazılı alın ve fotoğraflarıyla saklayın. Büyük projede "
              "en değerli belge, herkesin üzerinde anlaştığı o ilk örnektir.")},
    {"h": "Blok Blok Kontrol Listesi",
     "p": ["Her iş kalemi için kısa bir kontrol listesi kullanıyoruz: ölçü, şakul, yalıtım "
           "detayları, temizlik. Bir blok bu listeden geçmeden \"bitti\" sayılmıyor. Eksikler "
           "listede kalıyor, ekip bir sonraki bloğa geçmeden kapatılıyor."]},
    {"h": "Malzeme, Hava ve Takvim",
     "p": ["Bartın'ın yağışlı ikliminde büyük şantiyenin derdi sadece beton günü değil; "
           "sahada bekleyen malzeme de. Çimento, alçı, yalıtım levhası gibi malzemelerin "
           "**yağmurdan korunacağı stok alanı** ve sevkiyatların iş sırasına göre gelmesi "
           "takvimin bir parçası. Paralel bloklarda da ekipler, bir blok havaya takıldığında "
           "diğerinde çalışabilecek şekilde planlanıyor."]},
],
"sss": [
    ("Büyük projelerde hangi kalemleri alıyorsunuz?",
     "Kaba inşaat, kalıp-demir-beton, duvar-sıva, mantolama-cephe ve ince işler."),
    ("Numune uygulama neden önemli?",
     "Tekrar eden işte kaliteyi sabitlemenin en sağlam yolu; her blok aynı örneğe göre yapılıp "
     "kontrol ediliyor."),
    ("Kaç blok aynı anda yürütülebilir?",
     "İşin kalemine ve takvime göre değişiyor; keşifte ekip planını açıkça konuşuyoruz."),
    ("Hava koşulları takvimi nasıl etkiliyor?",
     "Yağışlı günleri programa pay olarak koyuyor, malzemeyi korunaklı stokluyor ve paralel "
     "bloklarda iş kaydırarak kaybı azaltıyoruz."),
],
},
}
