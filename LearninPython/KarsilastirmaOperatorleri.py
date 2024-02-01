# karşılaştırma operatörleri
# <, >, ==, <=, >= !=/=!
# hava 30 dereceden büyükse  çok sıcak
    # 0 dan küçükse çok soğuk,
    # bunların hiçbiri değilse çok güzel desin

derece = 23;

if derece >=30:
    print("Hava çok sıcak")
elif derece <0:
    print("Hava çok soğuk")
else:
    print("Hava çok güzel")


# çalışma: Soru:
    #   18 inden büyük ve okula gitmiyorsa askere gitme zamanı geldi
    #   18 inden buyuk ve okula gidiyorsa okul bittiğinde askere geleceksiniz
    #   eğer hiçbiri değilse askerlik daha gelmedi

yas = int(input("Yaşınızı girin: "));
okulDurumu = input("Okula gidiyorsan: Evet => e, Gitmiyorsan: Hayır =>h: ")

if yas>=18 and okulDurumu=="h":
    print("Askere Gelme Yaşınız Geldi!")
elif yas>=18 and okulDurumu=="e":
    print("Okul Bittiğinde Askere Geleceksiniz!")
else:
    print("Askerelik Yaşınız Daha Gelmedi!")