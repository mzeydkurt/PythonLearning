"""import time

class Robot:
    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year

    def cagir(self):
        print(f"Robotumuzun İsmi: {self.name}, Yapım Tarihi: {self.build_year}")

    def yas(self):
        current_year = time.localtime().tm_year
        print("Şuanki yıl : ",current_year)
        return f"Robot Yaşı: {current_year - self.build_year} yıl"

robot1 = Robot("ZHR1", 2015)

robot1.cagir()
print(robot1.yas())
print(robot1.__dict__)"""


"""class A:
    def __init__(self, name = None):
        self.name = name
    def say_hi(self):
        if self.name:
            print("Hi I am " + self.name)
        else:
            print("Hi I am robot without name")
    def set_name(self):
        self.name = name
    def get_name(self):
        return self.name
    
x=A()
x.set_name('Henry')  
x.say_hi()
y=A()
y.set_name(x.get_name())
print(y.get_name())"""

"""class A:
    def __str__(self):
        return "42"
    def __repr__(self):
        return "42"
a=A()
print(a)
print(repr(a))
print(str(a))
"""


"""class P:
    def __init__(self,x):
        self.__x = x
    def get_x(self):
        return self.__x 
    def set_x(self, x):
        self.__x = x

p1 = P(42)
print(p1.get_x())
p1.set_x(32)
print(p1.get_x())"""



"""class P:

    def __init__(self, x):
        self.set_x(x)
    def get_x(self):
        return self.__x
    def set_x(self, x):
        if x < 0 :
            self.__x = 0
        elif x > 1000 :
            self.__x = 1000
        else:
            self.__x = x

p1 = P(5465465)
print(p1.get_x())"""


"""class Restorant():
    yiyecekler = {"Et":50,"Tavuk":35, "Çorba":20}
    icecekler = {"Kola":15, "Soda":5, "Su": 2}
    tatlilar = {"Sütlac":20, "Tramisu": 25, "Puding": 15}

    def __init__(self):
        self.hesap = 0

    def yiyeceksec(self,secim):
        if secim in self.yiyecekler:
            self.hesap += self.yiyecekler[secim]
        else:
            print("Seçiminiz Menüde Yoktur")

    def iceceksec(self,secim):
        if secim in self.icecekler:
            self.hesap += self.icecekler[secim]
        else:
            print("Seçiminiz Menüde Yoktur")

    def tatlisec(self,secim):
        if secim in self.tatlilar:
            self.hesap += self.tatlilar[secim]
        else:
            print("Seçiminiz Menüde Yoktur")
    def hesap_göster(self):
        print(f"Ödenecek Miktar : {self.hesap}")

deneme1 = Restorant()
deneme1.yiyeceksec(input("Yiyecek Seçiniz"))
deneme1.iceceksec(input("İçecek Seçiniz"))
deneme1.tatlisec(input("Tatli Seçiniz"))
deneme1.hesap_göster()"""

"""class Banka():
    def __init__(self):
        self.banka_hesap = 0

    def kalan_para(self):
        print(f"Kalan Bakşyeniz : {self.banka_hesap}")

    def para_yatir(self, tutar):
        if tutar > 0:
            self.bakiye += tutar
            print(f"{tutar} TL hesabınıza yatırıldı.")
        else:
            print("Geçersiz tutar!")
    def para_cek(self, tutar):
         if 0 < tutar <= self.bakiye:
            self.bakiye -= tutar
            print(f"{tutar} TL hesabınızdan çekildi.")
        else:
            print("Yetersiz bakiye veya geçersiz tutar!")

    def havale(self, tutar, kisi):
        if 0 < tutar <= self.bakiye:
            self.bakiye -= tutar
            print(f"{kisi} adlı kişiye {tutar} TL gönderildi.")
        else:
            print("Yetersiz bakiye veya geçersiz tutar!")
bnk1 = Banka()
bnk1.kalan_para()
bnk1.para_yatir(123456)
bnk1.para_cek(24323)
bnk1.kalan_para()
bnk1.havale(1234, "Zeyd")
bnk1.kalan_para()"""


# QUİZ DENEMSİ SORUSU 
class Calisan:
    calisan_listesi = []  # Tüm çalışanların isimlerini tutar
    sigorta_puani = 25    # Başlangıç sigorta puanı

    def __init__(self, isim, cinsiyet, maas):
        # Çalışanın temel bilgileri atanıyor
        self.isim = isim
        self._cinsiyet = cinsiyet
        self.maas = maas
        # Yeni çalışan ismi listeye ekleniyor
        Calisan.calisan_listesi.append(self.isim)

    @classmethod
    def personeli_goruntule(cls):
        # Tüm çalışanları listeler
        print("Personel listesi yazdırılıyor!")
        print(cls.calisan_listesi)

    def personel_ekle(self, ad):
        # Yeni bir isim manuel olarak çalışan listesine eklenir
        Calisan.calisan_listesi.append(ad)

    def sigorta_yatirim(self):
        # Sigorta puanı artırılır
        Calisan.sigorta_puani += 15
        print(f"Sigorta puanı: {Calisan.sigorta_puani}")

    @staticmethod
    def ifade_et(ozellik):
        # Statik metot: herhangi bir nesneye bağlı olmadan çalışır
        print(f"Personelin yeteneği: {ozellik}")

""" sonradan eklenen kısım kendim
    def zam_yap(self, oran):
        # Maaşa verilen oran kadar zam yapılır
        # Örn: oran = 0.10 ise %10 zam yapılır
        eski_maas = self.maas
        self.maas += self.maas * oran
        print(f"{self.isim} adlı çalışanın maaşı {eski_maas} TL'den {self.maas} TL'ye yükseltildi.")

    def cinsiyet_guncelle(self, yeni_cinsiyet):
        # Cinsiyet bilgisi güncellenir
        self._cinsiyet = yeni_cinsiyet
        print(f"{self.isim} adlı çalışanın cinsiyeti güncellendi: {self._cinsiyet}")

    def bilgi_goster(self):
        # Çalışanın tüm bilgileri yazdırılır
        print(f"İsim: {self.isim}")
        print(f"Cinsiyet: {self._cinsiyet}")
        print(f"Maaş: {self.maas} TL")"""


# Örnek kullanım:
calisan1 = Calisan("Ahmet", "Erkek", 5000)

calisan1.bilgi_goster()          # Tüm bilgileri yazdırır
calisan1.zam_yap(0.15)           # %15 zam yapar
calisan1.cinsiyet_guncelle("Diğer")  # Cinsiyet günceller
calisan1.bilgi_goster()          # Güncellenmiş bilgileri tekrar gösterir
