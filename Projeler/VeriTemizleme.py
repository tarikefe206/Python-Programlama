kullanicilar = [" ALi ", "ayŞE", " Mehmet ", "", "  ", "CAN"]

temiz = [k.strip() for k in kullanicilar]    # Boşlukları Temizleme
print(temiz)

dolu = [k for k in temiz if k]        # İçi Boş Olanları Filtreleme
print(dolu)

standart = [k.capitalize() for k in dolu] # İlk Harfi Büyük Diğerlerini Küçük Yapma
print(standart)

temiz_kullanicilar = [k.strip().capitalize() for k in kullanicilar if k.strip()]  # Hepsini Temiz Şekilde Yazdırma
print(temiz_kullanicilar)