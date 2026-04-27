shopping_list = ["ekmek", "süt", "yumurta", "peynir","domates"]
print(f"İlk : {shopping_list[0]},Son ; {shopping_list[-1]}")

shopping_list.append("meyve") #Yeni Ürün Ekleme
shopping_list.append("salata")

shopping_list.remove("domates") #Ürün Silme

shopping_list.sort() #Alfabetik Sıralama

print(shopping_list)
print(f"{len(shopping_list)} Adet Ürün Var")



