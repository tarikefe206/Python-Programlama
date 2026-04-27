print("\n" + "=" * 50)
print("Hastane Randevu Takibi")
print("=" * 50)

randevular = {
    "Dr. Ayşe Kaya": ["08.00","09.00"],
    "Dr. Mehmet Yılmaz" : ["08.00","09.00"],
    "Dr. Fatma Demir" : ["08.00","09.00"]
}
for doktor, saatler in randevular.items():
    toplam = len(saatler)
    benzersiz = set(saatler)
    tekrar_sayisi = toplam - len(benzersiz)

    print(f"\n{doktor}")
    print(f" Toplam Kayıt  : {toplam}")
    print(f" Benzersiz  :  {len(benzersiz)}")
    print(f" Çakışma  : {tekrar_sayisi} adet")
    print(f" Saatler  :  {sorted(benzersiz)}")