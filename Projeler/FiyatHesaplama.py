# Ürün Fiyatlarına Kdv Ekle(%18) , İndirim Uygula(%20), Pahalı Ürünleri Filtrele(700 den fazla ise)
fiyatlar = [100, 250, 50, 800, 120, 1500, 75]

kdvli = list(map(lambda x: x * 1.18, fiyatlar))
print(kdvli)

indirimli = [f * 0.8 for f in fiyatlar]
print(indirimli)

pahali = [list(filter(lambda x: x > 700, fiyatlar))]
print(pahali)

son_fiyatlar = list(map(lambda x: x * 0.8 * 1.18, fiyatlar))
print(son_fiyatlar)