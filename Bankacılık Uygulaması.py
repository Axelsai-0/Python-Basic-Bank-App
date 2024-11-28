import random
from datetime import datetime
import hashlib
class BankaHesabı():
    Hesap_Listesi={}
    def __init__(self, İsim="", Soyisim="",Parola="", Banka_Iban_No="", Bakiye=0):
        self.İsim = İsim
        self.Soyisim = Soyisim
        self.Banka_Iban_No = Banka_Iban_No
        self.Bakiye = Bakiye
        self.İşlem_Listesi= []
        self.Parola = Parola
        self.kredi_borcu = 0
        
    def Hesap_Açma(self):
        
        while True:
            try:
                # Kullanıcıdan isim al
                self.İsim = input("Lütfen İsminizi Giriniz (Çıkmak için 'q'ya basınız): ")
                if self.İsim.lower() == "q":
                    print("Hesap açma işlemi iptal edildi.")
                    break

                # İsmin geçerli olup olmadığını kontrol et
                if not all(char.isalpha() or char.isspace() for char in self.İsim):
                    raise ValueError("İsim yalnızca harflerden oluşmalıdır.")
    
                # Kullanıcıdan soyisim al
                self.Soyisim = input("Lütfen Soyisminizi Giriniz (Çıkmak için 'q'ya basınız): ")
                if self.Soyisim.lower() == "q":
                    print("Hesap açma işlemi iptal edildi.")
                    break

                # Soyismin geçerli olup olmadığını kontrol et
                if not all(char.isalpha() or char.isspace() for char in self.Soyisim):
                    raise ValueError("Soyisim yalnızca harflerden oluşmalıdır.")

                # IBAN Üretimi
                self.Banka_Iban_No = "TR" + "".join([str(random.randint(0, 9)) for _ in range(11)])
                
                # Sözlüğe Ekleme 
                BankaHesabı.Hesap_Listesi[self.Banka_Iban_No] = self

                print(f"Hesabınız başarıyla oluşturuldu. IBAN Numaranız: {self.Banka_Iban_No}")
                print("Sayın {} {} \nHesabınızın Iban Numarası{}".format(self.İsim,self.Soyisim,self.Banka_Iban_No))
                break
                       
            except ValueError as hata:
                print(f"Hata: {hata}")


    def Hesapları_Listele():
        print("\n--- Kayıtlı Hesaplar ---")
        for iban, hesap in BankaHesabı.Hesap_Listesi.items():
            print(f"IBAN: {iban}, İsim: {hesap.İsim}, Soyisim: {hesap.Soyisim}, Bakiye: {hesap.Bakiye} TL")


    def Bakiye_Yönetimi(self):
        try:
            while True:

                self.Bakiye=(input("Lütfen bakiyenizi giriniz: /İptal etmek için q ya basınız..."))
                if self.Bakiye.lower()=="q":
                    print("İptal ediliyor...")
                    break
                
                elif not self.Bakiye.isdigit():
                    raise ValueError("Geçersiz hesap bilgisi//Harf girmeyiniz...")
                else:
                    self.Bakiye=int(self.Bakiye)
                    self.İşlem_Listesi.append(f"Güncel bakiye: {self.Bakiye}")
                    return
        except ValueError as hata:
            print(f"Hata: {hata}")
    def Bakiye_yatırma(self):
        try:
            while True:
                Yatırım_Miktarı=input("Lütfen yatırmak istediğiniz tutarı giriniz.../İptal etmek için q tuşuna basınız.")
                if Yatırım_Miktarı.lower()=="q":
                    print("İptal ediliyor...")
                    break
                elif not Yatırım_Miktarı.isdigit():
                    raise ValueError("Geçersiz miktar//Harf girmeyiniz...")
                else:
                    Yatırım_Miktarı=int(Yatırım_Miktarı)
                    self.Bakiye +=Yatırım_Miktarı
                    self.İşlem_Listesi.append(f"{datetime.now()} - {Yatırım_Miktarı} TL yatırıldı. Güncel bakiye: {self.Bakiye}")
                    print(f"{Yatırım_Miktarı} TL yatırıldı. Güncel bakiye: {self.Bakiye}")
                    
                    return
        except ValueError as hata:
            print(f"Hata: {hata}") 
    
    def Bakiye_çekme(self):
        try:
            while True:
                Çekim_Miktarı=input("Lütfen çekmek istediğiniz tutarı giriniz.../İptal etmek için q tuşuna basınız.")
                if Çekim_Miktarı.lower()=="q":
                    print("İptal ediliyor...")
                    break
                elif not Çekim_Miktarı.isdigit():
                    raise ValueError("Geçersiz miktar! Lütfen sadece sayı giriniz.")
                
                else:
                    Çekim_Miktarı=int(Çekim_Miktarı)
                    if Çekim_Miktarı > self.Bakiye:
                        print("Bakiyeniz yetersiz, işlem gerçekleştirilemiyor.")
                        break
                    self.Bakiye-=Çekim_Miktarı
                    self.İşlem_Listesi.append(f"{datetime.now()} - {Çekim_Miktarı} TL çekildi. Güncel bakiye: {self.Bakiye}")
                    print(f"{Çekim_Miktarı} TL çekildi. Güncel bakiye: {self.Bakiye}")
                    return
                
        except ValueError as hata:
            print(f"Hata: {hata}") 
    
    def çıkış(self):
        print("\n--- İşlem Özeti ---")
        print("Sayın {} {} /nHesabınızın Iban Numarası{}".format(self.İsim,self.Soyisim,self.Banka_Iban_No))
        for işlem in self.İşlem_Listesi:
            
            print(işlem)
            
        print(f"Son bakiye: {self.Bakiye} TL")
        print("Çıkış yapılıyor. İyi günler!")
    
    def Havale_işlemleri(self):
        try:
            while True:
                Havale_Tutarı = input("Lütfen tutarı giriniz/İptal etmek için q tuşuna basınız: ")
                Havale_edilecek_Hesap_İsmi = input("Lütfen havale edilecek hesap ismini giriniz/İptal etmek için q tuşuna basınız: ")

                if Havale_Tutarı.lower() == "q" or Havale_edilecek_Hesap_İsmi.lower() == "q":
                    print("İşlem iptal edildi.")
                    break

                if not Havale_Tutarı.isdigit():
                    raise ValueError("Geçersiz tutar. Lütfen bir sayı giriniz.")

                if not all(char.isalpha() or char.isspace() for char in Havale_edilecek_Hesap_İsmi):
                    raise ValueError("Hesap ismi yalnızca harflerden oluşmalıdır.")

                if Havale_edilecek_Hesap_İsmi not in BankaHesabı.Hesap_Listesi:
                    raise ValueError("Hesap bilgileri bulunamadı.")

                Havale_Tutarı = int(Havale_Tutarı)
                if self.Bakiye < Havale_Tutarı:
                    raise ValueError("Yetersiz bakiye.")

                # İşlemi gerçekleştir
                self.Bakiye -= Havale_Tutarı
                hedef_hesap = BankaHesabı.Hesap_Listesi[Havale_edilecek_Hesap_İsmi]
                hedef_hesap.Bakiye += Havale_Tutarı

                # İşlem bilgisi ekle
                self.İşlem_Listesi.append(f"{Havale_Tutarı} TL, {Havale_edilecek_Hesap_İsmi} hesabına havale edildi.")
                hedef_hesap.İşlem_Listesi.append(f"{Havale_Tutarı} TL, {self.İsim} tarafından havale alındı.")

                print(f"{Havale_Tutarı} TL, {Havale_edilecek_Hesap_İsmi} hesabına başarıyla gönderildi.")
                break

        except ValueError as hata:
            print("Hatalı işlem yapıldı.", hata)
            return None


    def kredi_basvurusu(self):
        try:
            # Kullanıcıdan bilgileri al
            yaş = int(input("Yaşınızı giriniz: "))
            aylık_gelir = int(input("Aylık gelirinizi giriniz (TL): "))
            mevcut_borç = int(input("Mevcut borç durumunuzu giriniz (TL): "))
            kredi_talebi = int(input("Talep ettiğiniz kredi miktarını giriniz (TL): "))
            
            # Kredi uygunluk kriterlerini kontrol et
            if yaş < 18:
                raise ValueError("18 yaşından küçükler kredi başvurusu yapamaz.")
            if kredi_talebi > (aylık_gelir * 10) - mevcut_borç:
                raise ValueError("Gelirinize göre talep edilen kredi çok yüksek.")
            
            # Kredi onaylanırsa işlem yap
            self.kredi_borcu += kredi_talebi
            self.Bakiye += kredi_talebi
            print(f"Kredi başvurunuz onaylandı! Hesabınıza {kredi_talebi} TL yatırıldı.")
            print(f"Güncel bakiyeniz: {self.Bakiye} TL")
            print(f"Toplam kredi borcunuz: {self.kredi_borcu} TL")
        
        except ValueError as hata:
            print(f"Kredi başvurusu reddedildi: {hata}")
        except Exception as hata:
            print(f"Beklenmedik bir hata oluştu: {hata}")


    def parola_gir(self):
        hak = 3
        while hak > 0:
            try:
                parola = input("Parolanızı girin: ")
                if len(parola) < 8:
                    raise ValueError("Parola en az 8 karakter uzunluğunda olmalıdır.")
                if not any(char.isupper() for char in parola):
                    raise ValueError("Parola en az bir büyük harf içermelidir.")
                if not any(char.isdigit() for char in parola):
                    raise ValueError("Parola en az bir rakam içermelidir.")
            
                print("Parola başarıyla doğrulandı.")
                return parola
        
            except ValueError as hata:
                hak -= 1
                print(f"Hata: {hata}. Kalan giriş hakkı: {hak}")
                if hak == 0:
                    print("Giriş hakkınız bitti. İşlem sonlandırılıyor.")
                    return None

    
Müşteri_1=BankaHesabı()
Müşteri_1.Hesap_Açma()
Müşteri_1.Bakiye_Yönetimi()
Müşteri_1.Bakiye_yatırma()
Müşteri_1.Bakiye_çekme()
Müşteri_1.Bakiye_çekme()
Müşteri_1.Bakiye_yatırma()
Müşteri_1.Bakiye_çekme()
Müşteri_1.Bakiye_çekme()
Müşteri_1.çıkış()