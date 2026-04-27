rehber = {
    'Ahmet': '0555-111-2233',
    'Mehmet': '0555-444-5566',
    'Ayşe': '0555-777-5434'
}
aranan = input("Aradığınız Kişi: ")
if aranan in rehber:
    print(f"{aranan} telefonu {rehber[aranan]}")
else:
    print("Kişi Bulunamadı")