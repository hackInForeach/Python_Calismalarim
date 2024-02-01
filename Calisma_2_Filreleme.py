import cv2
import numpy as np

# görüntü dosyası seçildi
img = cv2.imread("Pictures/Venom.png")


# ekranda zeytinin renkli fotosu gösterildi
cv2.imshow("Venom Fotosu",img)


# numpy kütüphanesini kullanarak bir çekirdek oluşturalım
# burada bir 3x3 lük matris oluşturduk ve içeriği ondalık değer ler ile doldurduk

#kernel= np.ones((3,3),np.float32)/9

# şim bunun nasıl göründüğüne bakalım:
# print(kernel)

# bu kernel bulanıklaştrıma işleminde mesala blur yapılmak istendiğinde:
# parametreleri:
# kaynak  : resim
# derinlik: -1 (-1: original resimle aynı demek derinlik demek)
# çekirdek: kernel
#imgBlur = cv2.filter2D(img,-1,kernel);

# şimdi bulanıklaştırmaya bakalım:
#cv2.imshow("Venom Fotosu Blanik",imgBlur)

# keskinlestirme
kernel = np.array([[-1,-1,-1],
                   [-1, 9,-1],
                   [-1,-1,-1]
                   ])

keskinlestirme = cv2.filter2D(img,-1,kernel)

cv2.imshow("Kardelen Fotosu Kesinlik: ",keskinlestirme)

# kenarları da bulanıklaştırmak için:
# kaynak
# çekirdek
# keneldeki standat sapma
#gaus = cv2.GaussianBlur(img,(5,5),0)
#cv2.imshow("Venom Gauss bulaniklaştirma: ",gaus)

# kenarların daha kesikin bırakılarak bulanıklaştırma yapılması için:
# kaynak
# renk uzayı
# bilatirel = cv2.bilateralFilter(img,9,75,75)
# cv2.imshow("Venom Bilatirel bulaniklaştirma: ",bilatirel)

# medan buluru ile gürültü azaltma: 
# çift sayılarda hata veriyor
# median = cv2.medianBlur(img,3)
# cv2.imshow("Venom Median bulaniklaştirma: ",median)

# resimde kenarları tespit etme:
# alt eşik
# üst eşik
canny = cv2.Canny(img,10,200)
cv2.imshow("Venom Canny ile Kenar  tespit etmek: ",canny)

# resmi açmak için gerekli kod satırları
cv2.waitKey(0)
cv2.destroyAllWindows()
