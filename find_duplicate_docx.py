import os
from collections import defaultdict

# Çalışma klasörünü otomatik al
base_path = os.getcwd()

# Dosya adlarını ve yollarını saklamak için dict
dosya_yollari = defaultdict(list)

# Tüm alt klasörleri tara
for root, dirs, files in os.walk(base_path):
    for file in files:
        if file.lower().endswith('.docx'):
            full_path = os.path.join(root, file)
            dosya_yollari[file].append(full_path)

# Tekrarlayan dosyaları bul
tekrarlayanlar = {dosya: yollar for dosya, yollar in dosya_yollari.items() if len(yollar) > 1}

# Sonuçları yazdır
if tekrarlayanlar:
    print("Tekrarlayan .docx dosyaları ve bulundukları klasörler:\n")
    for dosya, yollar in tekrarlayanlar.items():
        print(f"{dosya} ({len(yollar)} kez bulundu):")
        for yol in yollar:
            print(f"   - {yol}")
        print("-" * 60)
else:
    print("Tekrarlayan .docx dosyası bulunamadı.")
