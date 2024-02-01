x = 2
y = 5

# dört işlem
print(x+y)
print(x-y)
print(x*y)
print(x/y) # sonuç ondalıklı çıkar

# diğer işlemler
print(x//y) # sonuç tam sayılı çıkar
print(x ** y) # x sayısının y üssü

#-----------
# Çalışma: soru:
    #Kullanıcı iki sayı girsin ve bunlar çıktı olarak toplansın
#-----------

number1 = input("Birinci sayıyı gir: ")
number2 = input("İkinci sayıyı gir: ")
toplam = int(number1) + int(number2)
print("Sonuç: "+str(toplam))

# yuvarlama: round()
deger = input("ondalıklı bir değer gir: ")
print(round(float(deger)))

# mutlak değer: abs() 0 a olan uzaklık
print(abs(float(deger)))

# karke kök alma import math
    # math.sqrt()
import math
print(math.sqrt(float(deger)))

s1 = input("ilk değer: ")
s2 = input("İkinci değer: ")
s3 = input("Üçüncü değer: ")
# min()
print("Min değer: ",min(int(s1),float(s2),int(s3)))
# max()
print("Max değer: ",max(int(s1),float(s2),int(s3)))

