gizlisayi = 42
tahmin = 0

while tahmin != gizlisayi:
    tahmin = int(input("Sayıyı Tahmin Et"))
    if tahmin > gizlisayi:
        print("Doğru Sayıdan Büyük")
    elif tahmin < gizlisayi:
        print("Doğru Sayıdan Küçük")
    else:
        print("Doğru Bildin")

