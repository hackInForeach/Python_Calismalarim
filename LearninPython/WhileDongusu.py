x = 1;

while x<= 10:
    print(x,"\t. NASIL GİDİYOR")
    x+=1


# daha sonra düzenlenecek
count =0
for num in range(int(5), int(10)+1):
    if  num > 1:
        for i in range(2,num):
            if num % i ==0:
                break
            else:
                count+=1
print("count prime: ",count)

for x in range(3):
    s = input("Kullanıcı Adını Belirle: ")
if not s:
    print("Kullanıcı Adı Boş Geçilemez")
elif s:
    print("Yeni Parola",s)
elif x == 2:
    print("3 Kere Yanlış Parola Girdiniz 60 Saniye Sonra Tekrar Deneyin")

#Bu kod dizimindeki print fonksiyonu neden çalışmıyor)
elif x == 2:
    print("3 Kere Yanlış Parola Girdiniz 60 Saniye Sonra Tekrar Deneyin")
