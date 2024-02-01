# stringlerde "" veya '' kullanılarbilir tanımlama  yapılırken
isim = "\'Doğukan\'"
print(isim)
# or
ismi = '\"Doğukan\"'
print(ismi)

# koca bir metni tek bi değişkene kaydetmek istediğimiz: """ """"
# nasıl yazıldıysa öyle çıktı alınır
mektup = """ 
  Merhab Doğukan. Nasılsın?
  Umarım yisindir. Sana kötü bir haberim var ya da... Sen akşam bana uğra.
  Hmmm... 
  Tamam o halde.
  Saat 20:40 da ...Cafe de ol.
  Görüşürüz...
  DıDıDııı"""
print(mektup)

#------------
# bir metnin ilk ifadesi için: örn 0-1-2-3-4-5 ... gibi devam eder
isim = 'doğukan'
print(ismi[4]) # 5 inci ifadeyi göster
print(ismi[4:7]) # belli bir kısımı almak için ama 7 hariç
print(ismi[-4:-1]) # sondan başlayarak almak için '-' ifadesi kullanılır
print(len(ismi)) # metin uzunluğu len()

print(ismi[1:4]+ismi[3:6].upper()+ismi[6:8])
# şimdi buna benzer işlemi fonk ile yapalım..
print(ismi.title()) # ilk harfi büyültmek için
print(ismi.upper()) # harfleri büyült
print(ismi.lower()) # harfleri küçült
print(ismi.find("e")) # hassas tır


metin = "Merhaba Doğukan nasılsın ?"
print(metin.replace("nasılsın","EveT")) # birşeyleri değiştirmek için: replace("değişecek","yeni")

#----------------
# Çalışma: soru: kulanıcıdan ismini iste, ilk harf her şartta büyütülsün
#----------------

ad = input("İsmini gir: ").title();
print(ad)









