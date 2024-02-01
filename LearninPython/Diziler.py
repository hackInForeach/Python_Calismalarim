# dizeler
# birden çok veriyi depolamamızı sağlar
# dizi tanımlarkern = diziAdi = [boyutu]



diziBoyutu = int(input("Dizinin boyutunu gir: "))
isciler = [None]*diziBoyutu # dinamik olarak dizi boyutu ayarlamak için
# burada None özel bir ifadedir bir birşey olmadığını belrtir
# çarpı işareti ile içerideki işlem çoğaltılır
# ve daha sonra dinamik olarak oluşturduğumuz olayda
# boş olarak açılan alanları doldururuz


for i in range(0, len(isciler)):
    isciIsimleri = input(str(i+1)+".İşcçi isimi: ")
    isciler[i]=isciIsimleri

for i in range(0,len(isciler)):
    print(isciler[i])


# kullanıcıdan n tane öğrencini vize ve final notlarını alıp
# ortalamasını bulan programı yazın

ogrenciSayisi = int(input("Öğrenci sayısını gir: "))

vize = [None] * ogrenciSayisi
final = [None] * ogrenciSayisi
ort = [None] * ogrenciSayisi

for i in range(0,ogrenciSayisi):
     ogrenciAd = input("Öğrenci adı: ")
     degerGir = int(input(str(i + 1) + ".Öğrenci vize notu: "))
     vize[i] = (degerGir * 0.4)
     degerGir = int(input(str(i + 1) + ".Öğrenci final notu: "))
     final[i] = (degerGir * 0.6)
     ort[i]=ogrenciAd+":",vize[i]+final[i]
for j in range(0,ogrenciSayisi):
    print(ort[j])

# diğer çalışma

isciler1 = ["Doğukan","Berk","Anıl","Emre","Sevim"]
print(isciler1[0:3])
