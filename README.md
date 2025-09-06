🗂️ Find Duplicate Files

Bu proje, bir dizin ve alt dizinlerinde bulunan **tekrarlayan dosyaları** bulmanızı sağlar.  
Varsayılan olarak `.docx` dosyaları tarar ancak **tüm dosya uzantılarında kullanılabilir**.  
Yapmanız gereken tek şey, kodun içindeki **dosya uzantısını** değiştirmektir. 🔧  

Büyük projelerde, yedekleme dosyalarında veya karmaşık klasör yapılarında aynı isimdeki dosyaları tespit etmek için **pratik ve hızlı bir çözüm** sunar. 🚀

Örnek:  
- `.pdf` dosyaları için `"if file.lower().endswith('.pdf'):"` olarak düzenleyin.  
- `.jpg` dosyaları için `"if file.lower().endswith('.jpg'):"` şeklinde kullanın.  
- **Tüm uzantıları kontrol etmek için** `if` kısmını kaldırabilirsiniz. 🌍  

------------------------------------------------------------
🔹 Neden Bu Araca İhtiyacınız Var?

📚 Düzen ve Temizlik: Belgelerinizin düzenini sağlamak için tekrarlayan dosyaları tespit eder.  
💾 Depolama Alanı Tasarrufu: Gereksiz kopyaları silerek disk alanınızı boşaltır.  
⏳ Zaman Kazandırır: Manuel olarak klasörleri kontrol etmek yerine tek komutla tarama yapar.  
🔍 Hızlı Tespit: Karmaşık klasör yapılarında kaybolmadan dosyalarınızı kontrol etmenizi sağlar.  
🖥️ Kullanıcı Dostu: Basit bir Python scripti ile zahmetsizce çalışır.  
🌐 Esnek Kullanım: İstediğiniz dosya türüyle çalışabilirsiniz.

------------------------------------------------------------
🌟 Avantajları

⚡ Otomatik Tarama: Alt klasörleri tek tek gezmenize gerek kalmaz.  
🎯 Sade Kullanım: Belirttiğiniz dosya türünü arayarak gereksiz sonuçları filtreler.  
📂 Çoklu Dosya Kontrolü: Bir dosya birden fazla klasörde varsa hepsini listeler.  
💻 Platform Bağımsız: Windows, MacOS ve Linux üzerinde çalışır.  
🛠️ Açık Kaynak: İhtiyacınıza göre özelleştirebilirsiniz.

------------------------------------------------------------
⚙️ Kurulum

🐍 Python 3 kurulu olduğundan emin olun.  
💻 Ardından proje dizinine gidin ve depoyu klonlayın:

git clone https://github.com/ebubekirbastama/find-duplicate-docx.git  
cd find-duplicate-docx

------------------------------------------------------------
🚀 Nasıl Kullanılır?

1️⃣ Terminal veya Komut İstemi açın.  
2️⃣ `find_duplicate_docx.py` dosyasını çalıştırın:

python find_duplicate_docx.py

3️⃣ Program, çalıştığı klasör ve alt klasörlerdeki dosyaları tarar.  
4️⃣ Eğer aynı isimde birden fazla dosya varsa sonuçları listeler.

💡 Dosya uzantısını değiştirmek için kod içindeki şu satırı düzenleyin:
if file.lower().endswith('.docx'):

Bunu istediğiniz uzantıyla değiştirin. Örneğin `.pdf`, `.jpg`, `.txt` vb.

------------------------------------------------------------
📝 Örnek Çıktı

Tekrarlayan dosyalar ve bulundukları klasörler:

📄 Rapor.docx (2 kez bulundu):  
   - C:\\Projeler\\Rapor.docx  
   - C:\\Yedekler\\Rapor.docx  
------------------------------------------------------------
📄 Toplanti.pdf (3 kez bulundu):  
   - C:\\Belgeler\\Toplanti.pdf  
   - C:\\Yedekler\\Toplanti.pdf  
   - D:\\Eski\\Toplanti.pdf  
------------------------------------------------------------

------------------------------------------------------------
💡 İpuçları

📁 Klasör Düzeni: Scripti çalıştırmadan önce belgelerinizi tek bir ana klasörde toplayın.  
🗑️ Gereksiz Dosyalar: Tespit edilen kopyaları silmeden önce mutlaka yedek alın.  
⚡ Hızlı Tarama: Çok fazla dosya varsa SSD diskte çalıştırarak taramayı hızlandırabilirsiniz.  
🔐 Dikkat: Benzer isimli ama farklı içerikli dosyalara dikkat edin.  
🌍 Esneklik: `.docx` dışında istediğiniz dosya türüyle kullanabilirsiniz.

------------------------------------------------------------
🧾 Lisans

📜 Bu proje **MIT Lisansı** ile lisanslanmıştır.  
Detaylar için `LICENSE` dosyasına göz atabilirsiniz.

------------------------------------------------------------
👨‍💻 Katkıda Bulunun

💡 Fikirlerinizi paylaşmak için **Issue** açabilirsiniz.  
🔧 Geliştirme yapmak için **Pull Request** gönderebilirsiniz.  
🤝 Projeyi geliştirmemize destek olun!

------------------------------------------------------------
🔍 Etiketler

🐍 Python, 📄 DOCX, 🔁 Duplicate Files, 🗂️ File Management, 🌐 Multi Extension
