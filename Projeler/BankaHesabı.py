class BankaHesabi:
    def __init__(self):
        self.__bakiye = 0

    def para_yatir(self,para):
        if para < 0:
            print("Geçersiz Miktar")
        else:
            self.__bakiye += para 
            print(f"{para} Tl Yatırıldı")
    
    def para_cek(self,para):
        if para > self.__bakiye:
            print("Yetersiz Bakiye")
        else:
            self.__bakiye -= para 
            print(f"{para} Tl Çekildi")
        
    def get_bakiye(self):
        return self.__bakiye