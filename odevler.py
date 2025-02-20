print("Program-1: 3 Sayının Çarpımını Hesaplama")
a=int(input("1.sayıyı giriniz:"))
b=int(input("2.sayıyı giriniz:"))
c=int(input("3.sayıyı giriniz:"))
d=a*b*c
print("{} x {} x {} = {}".format(a,b,c,d))

print("Program-2: VKI Hesaplama")
a=int(input("Boyunuzu giriniz:"))
b=int(input("Kilonuzu giriniz:"))
c=b/(a*a)
print("Vücut Kitle İndeksiniz: {}".format(c))

print("Program-3")
a=int(input("Kilometre başına yakılan benzin miktarını giriniz:"))
b=int(input("Yapılan kilometre miktarını giriniz:"))
c=a*b
print("Toplam Ödemeniz Gereken Değer: {}".format(c))

print("Program-4")
a=input("Adınız:")
b=input("Soyadınız:")
c=input("Tel.Numaranız:")
print("Ad: {}\nSoyad: {}\nTel.: {}".format(a,b,c))

print("Program-5: Girilen Sayıların Yerlerini Değiştirme")
a=int(input("1.sayı:"))
b=int(input("2.sayı:"))
print("1.sayı: {}\n2.sayı: {}".format(a,b))
print("Karıştırılıyor....")
a,b=b,a
print("1.sayı: {}\n2.sayı: {}".format(a,b))

print("Program-6: Hipotenüs Hesaplama")
a=int(input("1.dik kenar:"))
b=int(input("2.dik kenar:"))
c =  (a ** 2 + b ** 2) ** 0.5
print("Hipotenüs: {}".format(c))
