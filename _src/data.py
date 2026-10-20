# -*- coding: utf-8 -*-
"""
arslankayainsaat.com verisi. build.py bu dosyayı okur.

⛔ TEYİTSİZ İDDİA YAZMA. Kullanıcıdan gelen bilgiler (2026-10-20):
   iki yetkili + telefon, adres (Bartın Merkez), 13 hizmet, 5 çalışma alanı.
   Henüz VERİLMEDİ → sitede YOK: kuruluş yılı / deneyim süresi, çalışma saati,
   sigorta, belge, garanti süresi, fiyat, referans proje, "7/24".
   Bunlar teyit edilince ONAYLI_IDDIALAR'a eklenip build'e bağlanır.
⛔ Üstünlük iddiası yazılmaz ("en iyi", "lider", "1 numara") — Ticari Reklam
   Yönetmeliği ispat istiyor; denetim.py bunu HATA sayar.
"""

SITE = {
    "alan": "https://arslankayainsaat.com",
    "marka": "Arslankaya İnşaat",
    "sehir": "Bartın",
    # Birincil hat: kullanıcının ilk verdiği numara (Celal Arslankaya).
    "tel": "0539 437 14 44", "tel_link": "+905394371444", "tel_kisi": "Celal Arslankaya",
    "tel2": "0541 675 77 86", "tel2_link": "+905416757786", "tel2_kisi": "Kurtuluş Arslankaya",
    "wa": "905394371444",
    "adres": "Demirciler Mah. Kenar Sok. No:2, Merkez / Bartın",
    "adres_sokak": "Demirciler Mah. Kenar Sok. No:2",
    "adres_ilce": "Merkez",
    "adres_il": "Bartın",
    "adres_pk": "74100",
    "aciklama": ("Bartın'da temelden çatıya inşaat, kaba ve ince işler, tadilat, çatı, "
                 "mantolama ve anahtar teslim yenileme. Keşiften teslime aynı ekip."),
}

# Teyit edilen iddialar — şimdilik yalnız kullanıcının verdiği somut bilgiler.
ONAYLI_IDDIALAR = [
    "Bartın Merkez'de ofis (Demirciler Mah.)",
    "13 hizmet kalemi (kullanıcı listesi)",
    "Müteahhit, bireysel, kamu, ticari, toplu konut çalışma alanları",
]

# Bartın'ın ilçeleri — yalnız bilgi amaçlı listeleniyor.
# ⏳ Hizmet bölgesi teyit edilmedi; ilçe sayfası AÇILMADI.
ILCELER = ["Merkez", "Amasra", "Kurucaşile", "Ulus"]

HIZMETLER = [
    {
        "slug": "temelden-catiya-insaat", "ikon": "bina",
        "ad": "Temelden Çatıya İnşaat",
        "ozet": "Projesi hazır arsanızda zemin etüdünden çatı kaplamasına kadar binanın tamamı.",
        "giris": ("Elinizde ruhsatlı bir proje ve arsa varsa gerisini tek elden yürütüyoruz: "
                  "hafriyat, temel, betonarme karkas, duvar, çatı, tesisat altyapısı ve ince "
                  "işler. İşi parça parça farklı ustalara dağıtmadığınız için bir ekibin "
                  "bıraktığı hatayı bir sonrakinin kapatmaya çalıştığı durumlar yaşanmıyor."),
        "kapsam": ["Saha hazırlığı ve hafriyat", "Temel ve bodrum betonarmesi",
                   "Kolon, kiriş ve döşeme imalatı", "Duvar örümü ve sıva",
                   "Çatı konstrüksiyonu, kaplama ve yalıtım", "Elektrik ve sıhhi tesisat altyapısı",
                   "Cephe, mantolama ve dış boya", "İç mekân ince işleri ve teslim temizliği"],
        "surec": ("İşe proje ve zemin etüdü raporu üzerinden başlıyoruz. Metraj çıkıyor, iş "
                  "kalemleri ve sırası yazılı hale geliyor. Her kat betonu öncesi demir ve kalıp "
                  "kontrolü yapı denetim firmasıyla birlikte yapılıyor; kontrol tutanağı "
                  "imzalanmadan beton dökülmüyor."),
        "yerel": ("Bartın, yılın her mevsimi yağış alan Karadeniz ikliminde. Bu yüzden temelde "
                  "drenaj ve bohçalama yalıtımını, çatıda da su yalıtımını \"sonra bakarız\" "
                  "kalemi olarak görmüyoruz; kaba inşaat bitmeden yapılmaları gerekiyor."),
        "sss": [
            ("Temelden çatıya inşaata başlamak için ne gerekiyor?",
             "Onaylı mimari ve statik proje, yapı ruhsatı ve zemin etüdü raporu. Ruhsat "
             "süreci devam ediyorsa keşif ve metraj çalışmasına yine başlayabiliriz."),
            ("Malzemeyi kim alıyor?",
             "İki yolu da konuşabiliyoruz: malzeme dahil anahtar teslim ya da malzemesi "
             "sizden işçilik. Hangisinin size uygun olduğunu keşifte netleştiriyoruz."),
            ("Fiyatı nasıl belirliyorsunuz?",
             "Proje üzerinden metraj çıkarıp iş kalemi bazında teklif veriyoruz. Telefonda "
             "metrekare başı kesin fiyat vermiyoruz; zemin ve proje detayı rakamı değiştiriyor."),
        ],
    },
    {
        "slug": "kaba-insaat", "ikon": "kolon",
        "ad": "Kaba İnşaat İşleri",
        "ozet": "Temel, kolon, kiriş, döşeme ve duvar — binanın taşıyıcı iskeleti.",
        "giris": ("Kaba inşaat, binanın ayakta durmasını sağlayan her şey: temel, betonarme "
                  "karkas, döşemeler, merdivenler ve dış duvarlar. Bu aşamada yapılan bir "
                  "hata ince işte gizlenebilir ama düzelmez; o yüzden ölçü, demir ve beton "
                  "kalitesine ayrı özen gösteriyoruz."),
        "kapsam": ["Hafriyat ve tesviye", "Grobeton ve temel betonarmesi",
                   "Bohçalama ve perde duvar yalıtımı", "Kolon, kiriş, perde imalatı",
                   "Döşeme ve merdiven betonu", "Dış ve iç duvar örümü",
                   "Çatı karkası (betonarme ya da ahşap)"],
        "surec": ("Her kat için sıra aynı: aplikasyon, kalıp, demir, kontrol, beton, kür. "
                  "Beton döküldükten sonra kür süresine uyulmadan üst kata yük bindirilmiyor. "
                  "Yağışlı havada beton dökümü planlanmıyor ya da gerekli koruma alınıyor."),
        "yerel": ("Eğimli parsellerde istinat duvarı ve drenaj, kaba inşaatın parçası olarak "
                  "baştan planlanıyor. Sonradan eklenen istinat hem pahalıya geliyor hem de "
                  "bahçe düzenini bozuyor."),
        "sss": [
            ("Kaba inşaat ne kadar sürer?",
             "Kat sayısına, zemine ve mevsime göre değişiyor. Proje üzerinden iş programı "
             "çıkarıp size yazılı olarak veriyoruz."),
            ("Sadece kaba inşaatı yaptırabilir miyim?",
             "Evet. Kaba inşaatı biz bitirip ince işleri başka bir ekiple yürütebilirsiniz; "
             "ya da devamını da bize bırakabilirsiniz."),
            ("Yapı denetimle siz mi görüşüyorsunuz?",
             "Beton döküm ve kontrol tarihlerini yapı denetim firmasıyla doğrudan "
             "koordine ediyoruz, size yalnız sonuç bilgisi düşüyor."),
        ],
    },
    {
        "slug": "ince-insaat", "ikon": "mala",
        "ad": "İnce İnşaat İşleri",
        "ozet": "Sıva, şap, alçı, zemin ve duvar kaplamaları — binayı yaşanır hale getiren işler.",
        "giris": ("Kaba inşaatı biten bir bina hâlâ oturulacak durumda değildir. Sıva, şap, "
                  "alçı, boya, zemin kaplaması, seramik, kapı-pencere ve dolap montajı ince "
                  "işlerin kapsamına giriyor. Bu işlerin sırası önemli: tesisat bitmeden sıva, "
                  "şap kurumadan parke olmaz."),
        "kapsam": ["İç ve dış sıva", "Şap ve tesviye", "Alçı sıva ve saten alçı",
                   "Asma tavan ve alçıpan bölme", "Seramik, fayans ve granit",
                   "Laminat ve parke döşeme", "İç ve dış boya", "Kapı, pencere ve dolap montajı"],
        "surec": ("İnce işe başlamadan elektrik ve su tesisatının sıva altı kısmı tamamlanıyor "
                  "ve test ediliyor. Ardından sıva, şap, alçı ve kaplama aşamaları her birinin "
                  "kuruma süresine uyularak sırayla ilerliyor."),
        "yerel": ("Nemli iklimde sıva ve şapın kuruma süresi uzayabiliyor. Kurumadan üzerine "
                  "boya ya da parke uygulanırsa kabarma ve küf kaçınılmaz oluyor; takvimi buna "
                  "göre yapıyoruz."),
        "sss": [
            ("İnce işleri daire daire yaptırabilir miyim?",
             "Evet. Tek daire için de tüm bina için de çalışıyoruz."),
            ("Malzeme seçimine yardımcı oluyor musunuz?",
             "Seramik, parke, boya gibi kalemlerde bütçenize uygun seçenekleri birlikte "
             "değerlendiriyoruz; son karar sizin."),
            ("İnce işler ne kadar sürer?",
             "Dairenin büyüklüğüne ve seçilen malzemeye göre değişiyor. Keşiften sonra "
             "iş takvimini yazılı olarak veriyoruz."),
        ],
    },
    {
        "slug": "tadilat-tamirat", "ikon": "anahtar",
        "ad": "Tadilat ve Tamirat",
        "ozet": "Evde, iş yerinde ya da binada küçük-büyük onarım ve yenileme.",
        "giris": ("Akan bir tavan, kabaran boya, çatlayan sıva, değişmesi gereken bir banyo… "
                  "Tadilat ve tamirat işlerinde önce sorunun kaynağını buluyoruz, sonra "
                  "görüneni onarıyoruz. Kaynağı çözülmeyen nem lekesi boyanınca iki ay sonra "
                  "yeniden çıkıyor."),
        "kapsam": ["Nem, rutubet ve küf kaynaklı onarımlar", "Sıva ve duvar tamiri",
                   "Banyo ve mutfak yenileme", "Zemin kaplaması değişimi",
                   "Kapı, pencere ve doğrama onarımı", "Çatı aktarma ve oluk tamiri",
                   "Bina ortak alan onarımları"],
        "surec": ("Yerinde bakıp sorunu tespit ediyoruz, yapılacak işi ve malzemeyi yazılı "
                  "olarak çıkarıyoruz. Oturulan evde çalışırken toz ve gürültüyü sınırlı "
                  "tutmak için çalışılan alanı kapatıyor, gün sonunda temizliyoruz."),
        "yerel": ("Bartın'da tadilat taleplerinin önemli bir kısmı nem ve su kaçağıyla "
                  "ilgili. Bu yüzden onarım öncesi suyun nereden geldiğini — çatı, cephe, "
                  "tesisat ya da zemin — ayırt etmek işin yarısı."),
        "sss": [
            ("Küçük işlere de geliyor musunuz?",
             "Evet. Tek bir duvar ya da tek bir banyo için de arayabilirsiniz."),
            ("Evde oturuyorken tadilat yapılır mı?",
             "Çoğu işte evet. Çalışılan alanı kapatıp gün sonunda temizliyoruz; banyo gibi "
             "uzun süren işlerde takvimi sizinle birlikte planlıyoruz."),
            ("Fiyatı nasıl öğrenirim?",
             "Yerinde görmeden net fiyat vermiyoruz. Fotoğraf gönderirseniz kabaca fikir "
             "verebiliriz, kesin teklif keşiften sonra çıkıyor."),
        ],
    },
    {
        "slug": "cati-izolasyon", "ikon": "cati",
        "ad": "Çatı ve İzolasyon İşleri",
        "ozet": "Çatı yapımı, aktarma, kiremit, membran ve su yalıtımı.",
        "giris": ("Çatı binanın şemsiyesi; küçük bir açık bütün evi etkiler. Yeni çatı "
                  "yapımı, eski çatının aktarılması, kiremit değişimi, oluk-dere ve su "
                  "yalıtımı işlerini yapıyoruz. Teras ve düz çatılarda membran yalıtım da "
                  "kapsamımızda."),
        "kapsam": ["Ahşap ve çelik çatı konstrüksiyonu", "Kiremit ve shingle kaplama",
                   "Çatı aktarma ve kırık kiremit değişimi", "Su yalıtım örtüsü ve OSB",
                   "Teras ve düz çatıda membran yalıtım", "Oluk, dere ve iniş borusu",
                   "Çatı ısı yalıtımı"],
        "surec": ("Önce çatıya çıkıp mevcut durumu görüyoruz: kiremit, altındaki örtü, "
                  "konstrüksiyon ve oluklar. Aktarma mı yetiyor yoksa çatının yenilenmesi mi "
                  "gerekiyor, bunu fotoğraflarla birlikte size gösteriyoruz."),
        "yerel": ("Bartın'ın yağışlı iklimi çatıda en çok oluk, dere ve baca diplerini "
                  "zorluyor. Su yalıtımında bu birleşim noktalarını ayrıca ele alıyoruz; "
                  "sızıntıların büyük kısmı kiremitten değil buralardan geliyor."),
        "sss": [
            ("Çatı aktarma ne demek?",
             "Kiremitlerin sökülüp altındaki örtü ve çıtaların kontrol edilmesi, gerekenlerin "
             "yenilenmesi ve kiremitlerin yeniden dizilmesi. Kırık kiremitler değiştiriliyor."),
            ("Çatı işi hangi mevsimde yapılır?",
             "Kuru havalar tercih ediliyor. Acil bir akıntı varsa geçici önlem alıp asıl işi "
             "uygun havaya planlıyoruz."),
            ("Teras çatıda su alıyor, ne yapılır?",
             "Önce suyun girdiği nokta tespit ediliyor. Çoğu durumda eğim düzeltmesi ve "
             "membran yalıtımın yenilenmesi gerekiyor."),
        ],
    },
    {
        "slug": "boya-badana-alci", "ikon": "rulo",
        "ad": "Boya, Badana ve Alçı İşleri",
        "ozet": "İç-dış boya, saten alçı, kartonpiyer ve alçıpan uygulamaları.",
        "giris": ("İyi bir boyanın yarısı hazırlıktır. Çatlakları açıp doldurmak, zımparalamak, "
                  "astar atmak ve mobilyayı korumak boya kadar zaman alıyor. Saten alçı, "
                  "kartonpiyer ve alçıpan asma tavan uygulamalarını da aynı ekip yapıyor."),
        "kapsam": ["İç cephe boya ve badana", "Dış cephe boyası", "Saten alçı ve perdah",
                   "Alçıpan bölme duvar ve asma tavan", "Kartonpiyer ve stor kutusu",
                   "Rutubetli duvarda hazırlık ve özel astar"],
        "surec": ("Eşyaları örtüyor, prizleri ve süpürgelikleri bantlıyoruz. Çatlak ve "
                  "kabarmalar açılıp dolduruluyor, zımpara ve astardan sonra iki kat boya "
                  "uygulanıyor. İş bitince çalışılan alan temizlenip teslim ediliyor."),
        "yerel": ("Kuzey cephelerde ve banyo-mutfak duvarlarında küf sık görülüyor. Bu "
                  "yüzeylerde küf önleyici astar ve nefes alan boya öneriyoruz; ama asıl "
                  "çözüm nemin kaynağını kesmek."),
        "sss": [
            ("Bir daire boyası kaç gün sürer?",
             "Dairenin büyüklüğüne, alçı tamiri gerekip gerekmediğine ve renk sayısına göre "
             "değişiyor. Keşifte süreyi netleştiriyoruz."),
            ("Boyayı ben alabilir miyim?",
             "Evet. Malzemeyi siz alabilir ya da bize bırakabilirsiniz."),
            ("Küf yapan duvara boya yeter mi?",
             "Yetmez. Önce küf temizlenip nemin kaynağı bulunuyor; sonra uygun astar ve "
             "boyayla kapatılıyor."),
        ],
    },
    {
        "slug": "seramik-fayans", "ikon": "karo",
        "ad": "Seramik ve Fayans İşleri",
        "ozet": "Banyo, mutfak, balkon ve zeminlerde seramik, fayans ve granit döşeme.",
        "giris": ("Seramikte işin görünen kısmı derz çizgisi, görünmeyen kısmı ise altındaki "
                  "zemin. Eğri bir şap ya da su yalıtımı yapılmamış bir banyo zemini, en "
                  "pahalı seramiği de kısa sürede bozar. Döşemeden önce zemini ve yalıtımı "
                  "kontrol ediyoruz."),
        "kapsam": ["Banyo ve mutfak fayansı", "Zemin seramiği ve granit",
                   "Balkon ve teras kaplaması", "Islak hacimlerde su yalıtımı",
                   "Eski kaplama söküm ve yenileme", "Derz dolgu ve silikon yenileme"],
        "surec": ("Eski kaplama sökülüyorsa önce söküm ve moloz, ardından zemin tesviyesi ve "
                  "ıslak hacimlerde su yalıtımı yapılıyor. Seramik yerleşim planı (kesimlerin "
                  "nereye geleceği) döşemeye başlamadan sizinle konuşuluyor."),
        "yerel": ("Balkon ve teras zeminlerinde don etkisine dayanıklı seramik ve esnek "
                  "yapıştırıcı kullanılması gerekiyor; kış aylarında iç mekân seramiğinin "
                  "dış mekânda çatladığını sık görüyoruz."),
        "sss": [
            ("Eski fayansın üzerine yenisi döşenir mi?",
             "Bazı durumlarda mümkün ama önermediğimiz durumlar çok. Zemin sağlamsa ve kot "
             "farkı sorun olmayacaksa değerlendiriyoruz."),
            ("Banyo yenileme ne kadar sürer?",
             "Tesisat değişip değişmediğine göre değişiyor. Keşifte iş programını veriyoruz."),
            ("Seramiği siz mi alıyorsunuz?",
             "İsterseniz biz alıyoruz, isterseniz siz seçip alıyorsunuz; işçilik ayrıca "
             "fiyatlanıyor."),
        ],
    },
    {
        "slug": "ic-dis-cephe", "ikon": "cephe",
        "ad": "İç ve Dış Cephe Uygulamaları",
        "ozet": "Dış cephe yenileme, kaplama, sıva ve boya; iç cephede duvar uygulamaları.",
        "giris": ("Dış cephe binayı hem korur hem de tanıtır. Dökülen sıva, solmuş boya ve "
                  "çatlaklar yalnızca görüntü sorunu değil, suyun duvara girmesinin de "
                  "yolu. Cephe yenilemede sıva tamiri, boya, kaplama ve gerekiyorsa mantolama "
                  "işlerini birlikte ele alıyoruz."),
        "kapsam": ["Dış cephe sıva tamiri ve yenileme", "Dış cephe boyası",
                   "Kompozit, taş ve dekoratif kaplama", "Söve, denizlik ve parapet işleri",
                   "İç mekânda dekoratif duvar uygulamaları", "Cephe derz ve çatlak onarımı"],
        "surec": ("Cephe işleri iskele kurulumu gerektiriyor. Önce cephe yüzeyi kontrol "
                  "ediliyor, kabaran ve boşluk yapan sıva sökülüyor, onarımdan sonra seçilen "
                  "kaplama ya da boya uygulanıyor."),
        "yerel": ("Rüzgârla gelen yağmur en çok batı ve kuzey cepheleri yıpratıyor. Tüm "
                  "cephe yerine yalnız bu yüzlerin yenilenmesi bazen yeterli oluyor; keşifte "
                  "bunu ayrı ayrı değerlendiriyoruz."),
        "sss": [
            ("Dış cephe için kat malikleri kararı gerekir mi?",
             "Apartmanlarda ortak alan sayıldığı için genellikle kat malikleri kurulu kararı "
             "gerekiyor. Teklifi yönetime sunulacak şekilde hazırlıyoruz."),
            ("Cephe boyası kaç yılda bir yenilenir?",
             "Malzemeye, cephe yönüne ve bakıma göre değişiyor; sabit bir süre yok."),
            ("İskeleyi siz mi kuruyorsunuz?",
             "Cephe işinin gerektirdiği iskele organizasyonunu iş kapsamında planlıyoruz."),
        ],
    },
    {
        "slug": "mantolama-yalitim", "ikon": "katman",
        "ad": "Mantolama ve Yalıtım",
        "ozet": "Dış cephe ısı yalıtımı (mantolama), iç yalıtım ve ses yalıtımı.",
        "giris": ("Mantolama, binanın dış yüzünü ısı yalıtım levhalarıyla kaplayıp sıva ve "
                  "boyayla kapatma işidir. Kışın ısının dışarı, yazın sıcağın içeri geçmesini "
                  "azaltır; yoğuşma kaynaklı duvar terlemesini ve küfü de önemli ölçüde "
                  "keser."),
        "kapsam": ["EPS ve taşyünü levha ile mantolama", "Dübel, file ve file üstü sıva",
                   "Mantolama üstü dekoratif son kat", "İç cepheden ısı yalıtımı",
                   "Ara kat ve tesisat sesi yalıtımı", "Çatı arası ısı yalıtımı"],
        "surec": ("Yalıtım kalınlığı ve malzemesi binanın durumuna göre belirleniyor. Levha "
                  "yapıştırma, dübelleme, file ve sıva katları sırasıyla uygulanıyor; pencere "
                  "kenarları ve köşelerde ısı köprüsü kalmaması için özel profiller kullanılıyor."),
        "yerel": ("Bartın'ın nemli ve serin kışlarında mantolamasız eski binalarda duvar "
                  "terlemesi ve kuzey odalarda küf çok yaygın. Mantolama ısınma giderinin "
                  "yanında bu sorunu da çözüyor."),
        "sss": [
            ("EPS mi taşyünü mü?",
             "EPS daha ekonomik, taşyünü yanmazlık ve ses yalıtımında öne çıkıyor. Bina "
             "yüksekliği ve beklentiye göre birlikte karar veriyoruz."),
            ("Mantolama hangi mevsimde yapılır?",
             "Sıva ve yapıştırıcıların düzgün kuruması için yağışsız ve çok soğuk olmayan "
             "günler tercih ediliyor."),
            ("Tek daire mantolama yapılır mı?",
             "Teknik olarak mümkün ama bütün cephe yapıldığında daha verimli ve görünüş "
             "olarak daha düzgün oluyor. Apartmanda yönetim kararı gerekiyor."),
        ],
    },
    {
        "slug": "beton-kalip-demir", "ikon": "demir",
        "ad": "Beton, Kalıp ve Demir İşleri",
        "ozet": "Betonarme kalıp, demir donatı bağlama ve beton döküm işleri.",
        "giris": ("Betonarmenin dayanımı projede yazan demirin, doğru aralıkla ve doğru "
                  "pas payıyla yerine konmasına bağlı. Kalıp, demir ve beton işlerini "
                  "müteahhitlere ve yapı sahiplerine ayrı ayrı ya da birlikte veriyoruz."),
        "kapsam": ["Ahşap ve plywood kalıp", "Demir kesim, büküm ve bağlama",
                   "Pas payı ve paspayı takozları", "Beton döküm ve vibrasyon",
                   "Beton kürü", "İstinat duvarı ve perde betonları"],
        "surec": ("Kalıp ölçüsü ve demir yerleşimi projeyle karşılaştırılarak kontrol ediliyor. "
                  "Yapı denetim onayı alınmadan beton siparişi verilmiyor; döküm sırasında "
                  "vibratör kullanılıyor ve beton kür süresi boyunca sulanıyor."),
        "yerel": ("Sıcak ve rüzgârlı günlerde betonun yüzeyi hızlı kuruyup çatlayabiliyor, "
                  "soğuk günlerde ise donma riski var. Döküm gününü hava tahminine göre "
                  "belirliyoruz."),
        "sss": [
            ("Sadece demir ya da sadece kalıp işi veriyor musunuz?",
             "Evet, müteahhitlere taşeron olarak yalnız kalıp ya da yalnız demir işçiliği de "
             "veriyoruz."),
            ("Beton dökümünden sonra ne kadar beklenir?",
             "Kalıp alma ve yük bindirme süreleri betonun sınıfına ve havaya göre değişiyor; "
             "proje ve yapı denetim kurallarına uyuyoruz."),
            ("Küçük betonarme işler yapıyor musunuz?",
             "İstinat duvarı, merdiven, garaj döşemesi gibi işleri de yapıyoruz."),
        ],
    },
    {
        "slug": "duvar-siva", "ikon": "tugla",
        "ad": "Duvar ve Sıva İşleri",
        "ozet": "Tuğla, gazbeton ve bims duvar örümü; iç ve dış sıva.",
        "giris": ("Düz bir duvar, üzerine gelen her işi kolaylaştırır: seramik düzgün oturur, "
                  "dolap boşluk vermez, boya pürüzsüz çıkar. Duvar örümünde şakul ve teraziyi, "
                  "sıvada da mastar düzgünlüğünü işin temel ölçüsü sayıyoruz."),
        "kapsam": ["Tuğla, gazbeton ve bims duvar örümü", "Bölme duvar ve lento",
                   "Kaba ve ince iç sıva", "Dış cephe sıvası", "Makine sıvası",
                   "Sıva filesi ve köşe profili"],
        "surec": ("Duvarlar projeye göre aplike edilip örülüyor; kapı ve pencere boşluklarına "
                  "lento atılıyor. Sıva öncesi tesisat kanalları açılıp kapatılıyor, köşelere "
                  "profil, farklı malzeme birleşimlerine file konuyor."),
        "yerel": ("Dış duvarlarda nemi içeri taşımayan malzeme ve doğru sıva seçimi önemli; "
                  "yağışlı iklimde yanlış sıva kısa sürede kabarıp dökülüyor."),
        "sss": [
            ("Gazbeton mu tuğla mı?",
             "Gazbeton hafif ve ısı yalıtımı daha iyi; tuğla daha ekonomik olabiliyor. "
             "Projeye ve kullanım yerine göre öneriyoruz."),
            ("Sıva çatlaması neden olur?",
             "Farklı malzemelerin birleşim yerlerinde file kullanılmaması ve sıvanın hızlı "
             "kuruması en yaygın sebepler."),
            ("Sadece sıva işi alıyor musunuz?",
             "Evet, tek daire ya da tek kat sıva işi de yapıyoruz."),
        ],
    },
    {
        "slug": "yikim-yenileme", "ikon": "yikim",
        "ad": "Yıkım ve Yenileme İşleri",
        "ozet": "Bina, bölüm ya da iç mekân yıkımı; moloz kaldırma ve yeniden yapım.",
        "giris": ("Yenilemenin ilk adımı çoğu zaman yıkımdır: bir duvarın kaldırılması, eski "
                  "banyonun sökülmesi ya da binanın tamamen yıkılması. Taşıyıcı elemana "
                  "dokunulacaksa işe statik değerlendirme olmadan başlamıyoruz."),
        "kapsam": ["İç mekân söküm ve kırım", "Bölme duvar kaldırma", "Seramik, şap ve sıva sökümü",
                   "Komple bina yıkımı (izinli)", "Moloz toplama ve döküm", "Yıkım sonrası yeniden yapım"],
        "surec": ("Bina yıkımında belediyeden alınan yıkım izni ve elektrik-su-doğalgaz "
                  "aboneliklerinin kapatılması işin ön şartı. İç mekân yıkımlarında taşıyıcı "
                  "duvar ve kolonlara dokunulmuyor; gerekiyorsa statik proje isteniyor."),
        "yerel": ("Kentsel dönüşüm ve eski yapı yenilemelerinde yıkımla yeni yapımın aynı "
                  "ekipte olması, takvim ve moloz organizasyonunda zaman kazandırıyor."),
        "sss": [
            ("Duvar kaldırmak için izin gerekir mi?",
             "Taşıyıcı olmayan bölme duvarlar için genellikle gerekmiyor; taşıyıcı elemana "
             "dokunulacaksa statik değerlendirme ve izin şart."),
            ("Moloz kimin sorumluluğunda?",
             "Moloz toplama ve döküm işini iş kapsamına dahil ediyoruz."),
            ("Yıkımdan sonra yeniden yapımı da üstleniyor musunuz?",
             "Evet, yıkım ve yeni yapım aynı ekiple yürüyebiliyor."),
        ],
    },
    {
        "slug": "anahtar-teslim-yenileme", "ikon": "kapi",
        "ad": "Anahtar Teslim Daire ve İş Yeri Yenileme",
        "ozet": "Dairenizi ya da iş yerinizi boş teslim alıp kullanıma hazır geri veriyoruz.",
        "giris": ("Anahtar teslim yenilemede tek muhatabınız biziz. Söküm, tesisat, alçı, boya, "
                  "zemin, banyo, mutfak ve aydınlatmaya kadar bütün işler tek takvimde "
                  "yürüyor. Siz iş başında her gün ayrı bir ustayı beklemiyorsunuz."),
        "kapsam": ["Keşif, metraj ve yazılı iş programı", "Söküm ve moloz",
                   "Elektrik ve su tesisatı yenileme", "Alçı, boya ve asma tavan",
                   "Zemin kaplama, seramik ve parke", "Banyo ve mutfak yenileme",
                   "İş yerinde vitrin, bölme ve dekorasyon", "Teslim temizliği"],
        "surec": ("Keşifte yapılacak işler kalem kalem yazılıyor, malzeme seçimleri sizinle "
                  "yapılıyor ve iş programı çıkıyor. İş boyunca ilerlemeyi fotoğraflarla "
                  "paylaşıyoruz. Teslimde eksik listesi birlikte kontrol ediliyor."),
        "yerel": ("İş yerlerinde kapalı kalınan her gün kayıp olduğu için işleri gece ya da "
                  "parça parça yapma seçeneğini de konuşuyoruz."),
        "sss": [
            ("Anahtar teslim fiyatına neler dahil?",
             "Keşifte yazılı hale gelen her kalem dahil. Sonradan çıkan ek işler ayrıca "
             "konuşulup onayınızla yapılıyor."),
            ("İş yeri yenilemede dükkân kapalı kalmak zorunda mı?",
             "Her işte değil. Bazı işleri mesai dışına ya da bölüm bölüm planlayabiliyoruz."),
            ("Malzeme seçimini kim yapıyor?",
             "Seçimi siz yapıyorsunuz; biz bütçeye ve kullanım yerine uygun seçenekleri "
             "öneriyoruz."),
        ],
    },
]

ALANLAR = [
    {
        "slug": "muteahhitlere-ozel-insaat-hizmetleri", "ikon": "kolon",
        "ad": "Müteahhitlere Özel İnşaat Hizmetleri",
        "kisa": "Müteahhitler",
        "ozet": "Kaba, ince ya da tek kalem işlerde taşeron ve iş ortağı olarak çalışıyoruz.",
        "metin": [
            "Müteahhit firmalar için kaba inşaat, kalıp-demir, duvar-sıva, çatı, mantolama "
            "ve ince işlerde taşeron olarak çalışıyoruz. İşin tamamını ya da yalnız bir "
            "kalemini alabiliyoruz.",
            "Sizin için önemli olan takvim ve kalite: iş programına uyulması, yapı denetim "
            "kontrollerinin aksamaması ve bir sonraki ekibe temiz bir iş teslim edilmesi. "
            "İşe bu üç noktayı yazılı hale getirerek başlıyoruz.",
        ],
        "hizmet": ["kaba-insaat", "beton-kalip-demir", "duvar-siva", "mantolama-yalitim",
                   "cati-izolasyon", "ince-insaat"],
    },
    {
        "slug": "bireysel-musterilere-ozel-hizmetler", "ikon": "ev",
        "ad": "Bireysel Müşterilere Özel Hizmetler",
        "kisa": "Bireysel",
        "ozet": "Ev sahipleri için müstakil ev yapımından tek odalık tadilata kadar.",
        "metin": [
            "Kendi evini yaptırmak ya da yenilemek isteyenlerle çalışıyoruz: müstakil ev "
            "yapımı, kat ilavesi, banyo-mutfak yenileme, çatı aktarma, boya ve mantolama.",
            "Bireysel müşterinin inşaat dilini bilmesi gerekmiyor. Neyin neden yapılacağını "
            "sade bir dille anlatıyor, teklifi kalem kalem yazıyoruz; böylece neye ödeme "
            "yaptığınızı görüyorsunuz.",
        ],
        "hizmet": ["temelden-catiya-insaat", "tadilat-tamirat", "anahtar-teslim-yenileme",
                   "cati-izolasyon", "boya-badana-alci", "seramik-fayans"],
    },
    {
        "slug": "kamu-kurumlari-ve-devlet-projeleri", "ikon": "kamu",
        "ad": "Kamu Kurumları ve Devlet Projeleri",
        "kisa": "Kamu",
        "ozet": "Kamu yapılarında yapım, onarım ve bakım işleri.",
        "metin": [
            "Kamu kurumlarına ait yapılarda yapım, onarım, bakım ve yenileme işlerinde "
            "çalışıyoruz. Bu işlerde teknik şartnameye uygunluk, hakediş düzeni ve iş "
            "güvenliği belgelerinin eksiksiz tutulması işin kendisi kadar önemli.",
            "Okul, hizmet binası ve benzeri yapılarda kullanım devam ederken çalışmak "
            "gerekebiliyor; çalışma alanını ayırıp kullanıcıları etkilemeyecek bir takvim "
            "kuruyoruz.",
        ],
        "hizmet": ["tadilat-tamirat", "cati-izolasyon", "mantolama-yalitim", "ic-dis-cephe",
                   "boya-badana-alci", "kaba-insaat"],
    },
    {
        "slug": "ticari-isletmeler-ve-is-yeri-insaatlari", "ikon": "dukkan",
        "ad": "Ticari İşletmeler ve İş Yeri İnşaatları",
        "kisa": "Ticari",
        "ozet": "Dükkân, ofis, mağaza ve atölyelerde yapım ve yenileme.",
        "metin": [
            "Mağaza, ofis, restoran, atölye gibi iş yerlerinin yapım ve yenileme işlerini "
            "yapıyoruz. İş yerinde kapalı kalınan her gün gelir kaybı demek; bu yüzden "
            "takvimi işletmenin çalışma düzenine göre kuruyoruz.",
            "Gerekiyorsa işleri mesai dışına ya da bölüm bölüm planlıyor, işletmenin açık "
            "kalabileceği bir çalışma sırası öneriyoruz.",
        ],
        "hizmet": ["anahtar-teslim-yenileme", "ince-insaat", "boya-badana-alci",
                   "seramik-fayans", "yikim-yenileme", "ic-dis-cephe"],
    },
    {
        "slug": "toplu-konut-ve-buyuk-olcekli-projeler", "ikon": "site",
        "ad": "Toplu Konut ve Büyük Ölçekli Projeler",
        "kisa": "Toplu Konut",
        "ozet": "Çok bloklu konut ve büyük ölçekli projelerde kaba ve ince iş kalemleri.",
        "metin": [
            "Çok bloklu konut projelerinde ve büyük ölçekli yapılarda kaba inşaat, "
            "kalıp-demir, duvar, sıva, mantolama ve ince iş kalemlerinde çalışıyoruz.",
            "Büyük projede belirleyici olan tekrar eden işin her blokta aynı kalitede "
            "çıkması. Bunun için iş kalemlerini standart hale getirip blok blok kontrol "
            "listesiyle ilerliyoruz.",
        ],
        "hizmet": ["kaba-insaat", "beton-kalip-demir", "duvar-siva", "mantolama-yalitim",
                   "ince-insaat", "temelden-catiya-insaat"],
    },
]

ANA_SSS = [
    ("Arslankaya İnşaat nerede?",
     "Ofisimiz Bartın Merkez'de, Demirciler Mahallesi Kenar Sokak No:2 adresinde."),
    ("Hangi işleri yapıyorsunuz?",
     "Temelden çatıya inşaat, kaba ve ince inşaat, tadilat, çatı ve izolasyon, boya-alçı, "
     "seramik, cephe, mantolama, beton-kalıp-demir, duvar-sıva, yıkım ve anahtar teslim "
     "daire ve iş yeri yenileme."),
    ("Küçük tadilat işlerine de geliyor musunuz?",
     "Evet. Tek bir banyo, tek bir oda ya da çatıdaki bir akıntı için de arayabilirsiniz."),
    ("Telefonda fiyat veriyor musunuz?",
     "Fotoğraf ve ölçüyle kabaca fikir verebiliyoruz ama kesin teklifi yerinde görüp, iş "
     "kalemlerini yazılı hale getirdikten sonra veriyoruz."),
    ("Müteahhitlere taşeron olarak çalışıyor musunuz?",
     "Evet. Kaba inşaat, kalıp-demir, duvar-sıva, mantolama gibi kalemleri tek tek ya da "
     "birlikte alabiliyoruz."),
]

# ── Hizmet görselleri (kullanıcı 2026-10-20 img/'e yükledi) ─────────────────
# slug → (img/ kaynak adı, alt metin, kart kırpım odağı (x, y) 0..1)
# ⚠️ Alt metin görselin GÖSTERDİĞİNİ anlatır, dosya adını değil; kelime doldurma yok.
# ⚠️ Yayın adı `bartin-<slug>` (kaynak "montalama" yazım hatası yayına taşınmıyor).
HIZMET_GORSEL = {
    "temelden-catiya-insaat": ("temelden-catiya-insaat",
        "Gün batımında kule vinçli şantiyede yükselen betonarme konut inşaatı ve çalışan ekip", (.5, .5)),
    "kaba-insaat": ("kaba-insaat",
        "Kalıpları ve kolon filizleri duran, tuğla duvarları örülmüş üç katlı betonarme kaba inşaat", (.5, .5)),
    "ince-insaat": ("ince-insaat",
        "Duvara mala ile sıva çeken ustanın elleri", (.45, .5)),
    "tadilat-tamirat": ("tadilat-ve-tamirat",
        "Alet kemerli ustanın tezgâh üzerinde şerit metre ve aletlerle ölçü alması", (.5, .45)),
    "cati-izolasyon": ("cati-ve-izolasyon",
        "Çatı çıtaları üzerine kırmızı kiremit kaplama döşeyen iki usta", (.55, .45)),
    "boya-badana-alci": ("boya-badana",
        "Baretli ustanın rulo ile beyaz duvarı sarıya boyaması", (.42, .5)),
    "seramik-fayans": ("seramik-ve-fayans",
        "Gri büyük ebatlı zemin seramiği üzerinde üç farklı tonda seramik numunesi", (.5, .5)),
    "ic-dis-cephe": ("ic-ve-dis-cephe",
        "İskele üzerinde dış cepheye levha uygulayan reflektif yelekli, baretli usta", (.55, .45)),
    "mantolama-yalitim": ("montalama-ve-yalitim",
        "Dış cepheye dübelli ısı yalıtım levhası yerleştiren usta", (.62, .5)),
    "beton-kalip-demir": ("beton-kalip-demir",
        "Kolon demir donatısını bağlayan baretli ve yelekli işçi", (.4, .45)),
    "duvar-siva": ("duvar-ve-siva-isleri",
        "Duvarda mala ile perdah sıva yapan ustanın eli", (.45, .5)),
    "yikim-yenileme": ("yikim-ve-yenileme-isleri",
        "Ekskavatör kepçesiyle yıkılan eski betonarme bina", (.45, .5)),
    "anahtar-teslim-yenileme": ("anahtar-teslim-yenileme",
        "Anahtar demeti yanında duran iki katlı ev maketi", (.5, .5)),
}
