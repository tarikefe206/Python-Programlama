isim = (input("İsmini Gir :"))
soyisim = (input("Soyadını Gir :"))
yaş = int(input("Yaşını Gir :"))
şehir = (input("Oturduğun Şehri Gir :"))
meslek = (input("Mesleğini Gir :"))
toplam_harf =len(isim)+len(soyisim)
print(f"İsim ve soydanızın toplam harf sayısı : {toplam_harf}")
print(f"Merhaba!\nBen {isim} {soyisim} \n{yaş} Yaşindayim \n{şehir} Şehrinde oturuyorum \nMesleğim : {meslek}")

ŞUANKİ_YIL = 2026
DOĞUM_YILI = int(input("Doğum Yılını Gir :"))
yaş = ŞUANKİ_YIL - DOĞUM_YILI 
yaşınızın_10_yıl_sonraki = yaş + 10

print(f"Yaşın : {yaş}")
print(f"10 Yıl sonra  {yaşınızın_10_yıl_sonraki} yaşında olacaksın")