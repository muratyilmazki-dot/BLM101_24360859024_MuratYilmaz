# Kullanıcıdan bilgileri alıyoruz
ad = input("Adınız nedir? ")
biyografi = input("Kısa bir biyografi yazın: ")
dersler = input("Aldığınız dersleri virgülle ayırarak yazın: ")

# Dersleri bir liste haline getiriyoruz (HTML için)
ders_listesi = ""
for ders in dersler.split(","):
    ders_listesi += f"<li>{ders.strip()}</li>"

# HTML İçeriği ve CSS (F-String kullanarak bilgileri gömüyoruz)
html_icerik = f"""
<!DOCTYPE html>
<html>
<head>
    <title>{ad} - Profil Sayfası</title>
    <style>
        body {{ font-family: Arial, sans-serif; background-color: #f4f4f4; text-align: center; }}
        .card {{ background: white; width: 50%; margin: 50px auto; padding: 20px; border-radius: 10px; shadow: 0 0 10px rgba(0,0,0,0.1); }}
        h1 {{ color: #2c3e50; }}
        ul {{ list-style-type: none; padding: 0; }}
        li {{ background: #ecf0f1; margin: 5px; padding: 8px; border-radius: 5px; }}
    </style>
</head>
<body>
    <div class="card">
        <h1>{ad}</h1>
        <p><strong>Biyografi:</strong> {biyografi}</p>
        <h3>Aldığım Dersler</h3>
        <ul>
            {ders_listesi}
        </ul>
    </div>
</body>
</html>
"""

# Dosyayı oluşturma ve yazma
with open("index.html", "w", encoding="utf-8") as dosya:
    dosya.write(html_icerik)

print("index.html başarıyla oluşturuldu! Klasörünüzü kontrol edin.")
