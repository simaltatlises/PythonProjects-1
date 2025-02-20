print("2.Dereceden Bir Denklemin Köklerini Bulma\nDenklem:ax^2+bx+c")
a=int(input("a değerini giriniz:"))
b=int(input("b değerini giriniz:"))
c=int(input("c değerini giriniz:"))
print("Kökler Hesaplanıyor....")
delta=b**2-4*a*c
kök1=(-b-delta**0.5)/2*a
kök2=(-b+delta**0.5)/2*a
print("Birinci Kök: {}\nİkinci Kök: {}".format(kök1,kök2))
