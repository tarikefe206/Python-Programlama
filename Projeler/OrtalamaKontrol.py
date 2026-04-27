not_ortalama = int(input("Notunu Gir"))

while not_ortalama > 100:
    print("Hatalı Sayı Girildi")
    not_ortalama = int(input("Notu Tekrar Gir"))    
if not_ortalama >= 90 :
    print("AA") 
elif not_ortalama >= 80:
    print("BA")
elif not_ortalama >= 70:
    print("BB")
elif not_ortalama >= 60:
    print("CC")
elif not_ortalama >= 50:
   print("DD")
else: print("FF")