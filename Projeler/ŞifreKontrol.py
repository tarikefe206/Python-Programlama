sifre = "python123"
deneme = 0

while deneme < 3:
    pwd = input("Şifre Gir: ")

    if pwd == sifre:
        print("Giriş Başarılı! ")
        break
    else:
        deneme += 1
        print(f"Yanlış! {3 - deneme} Hak Kaldı!")
    print("Hesap Kilitlendi!")
 