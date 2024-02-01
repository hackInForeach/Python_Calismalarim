import cv2
import numpy as np

# görüntü dosyası seçildi
img = cv2.imread("Pictures/Venom.png")
# ve gri olarak ta ele alındı
imgGri = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# ekranda zeytinin renkli fotosu gösterildi
cv2.imshow("Zeytin Fotosu",img)

size_y = img.shape[0] # yükseklik
size_x = img.shape[1] # genişlik
kanal = img.shape[2] # RGB renkleri olarak R=1,G=2,B=3

# resin en boy ve kullanılan renksayısına bakyık
print(
        "Yükseklik: " ,size_y,
        "\nGenişlik: ",size_x,
        "\nKanal: "   ,kanal
        )

print(img[(100,100)])   # resimdeki (x,y) kordinatlarındaki rengi bana göster
print(img[(100,100)]) # aynı işlemi imgGri için yapa

# sadece siyah-beyaz foro olarak gösterildi
cv2.imshow("Zeytin fotosu Gri",imgGri)

# resmi açmak için gerekli kod satırları
cv2.waitKey(0)
cv2.destroyAllWindows()

