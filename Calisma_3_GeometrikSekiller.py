import cv2

img = cv2.imread("Pictures/Venom.png")

#bu .imwirte() komutu dosyanın üzerinde işlem yapılmak için kaydedilmesi sağlar 
# cv2.imwrite("VenomGri.png",img)


# resim üzerine bir çizgi çizmek için:
# hedef resim
# başlangıç noktası
# bitişş noktası
# RBG renk kodları
# çizginin pixel kalınlığı
cv2.line(img,(0,0),(841,1019),(100,200,100),50)

# şimdi kare/dikdörtgen çizdirelim:
# hedef resim
# başlangıç noktası
# bitişş noktası
# RBG renk kodları
# çizginin pixel kalınlığı
cv2.rectangle(img,(100,100),(600,300),(100,0,50),25)
# için doldurmak için: -1
cv2.rectangle(img,(300,200),(400,300),(100,0,50),-1)

# çember çizmek için:
# hedef resim
# başlangıç noktası
# yarı çap (pixel)
# RBG renk kodları
# çizginin pixel kalınlığı
cv2.circle(img,(200,200),150,(100,200,250),5)

# şimdi elipse çizdirelim:
# hedef resim
# başlangıç noktası
# elipsin genişliği ve yüksekliği
# lipsin gözükeceği açısal değer
# başlangıç açısı 
# bitiş açısı (çeyrek=90/yarım=180/tam=360)
# renk skalası (RGB)
# kalınlık, -1 verilirse içini boş olan çizgimizin içi doldurulur
cv2.ellipse(img,(400,400),(100,200),45,50,270,(0,100,255),5)

# resime yazı ekleneceği zaman:
# hedef resim
# resime yazılacak şey = 'yazı'
# başlangıç noktası
# yazı fontu
# yazı büyüklüğü
# yazı rengi (RGB)
# yazı kalınlığı
# çizgi silili = düz,kesikli vb.
# yazı ters mi düz mü yazılsın evet/hayır
cv2.putText(img,'DOGUKANOZTURK',(50,200),cv2.FONT_HERSHEY_SIMPLEX,2.5,(100,100,100),10,cv2.LINE_8,False)

cv2.imshow("Venom Fotosu",img)
cv2.waitKey(0)
# pencre kapatılmasını sağlar
# istenirse isim verilebirlir
cv2.destroyAllWindows("Venom")