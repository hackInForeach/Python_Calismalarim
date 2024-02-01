# opencv kütüphanesi
import cv2
# kameradan görüntü almaj için kullanılan bir fonksiyon. 0= varsayılan kamera
video = cv2.VideoCapture(0)
# yüz tanıma için bir sınıflandırı, hazır bir xml dosyası
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while(True):
    #   ret okuma işleminini boolean değeri, frame: okunan çerçeveler
    ret, frame= video.read()
    # resmin griye dönüştürülmesi
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # renk,görüntü ölçeği, komşuluk sayısı(adayın yüz olup olmadığının anlaşılması)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
    
    #  x   y   w   h
    # 383  88  54  54
    
    # elde edilen kordinatlar dizisi
    # print(faces)
    
    # video kamerada yüzün bulunduğu kordinat verileri anlık olarak gösterilir
    for(x,y,width,height) in faces:
                      # hedef, başlangıç noktası,bitiş noktası,RGB, pixel kalınlığı
        cv2.rectangle(frame,(x,y),(width+x,height+y),(100,200,0),5)
    # pencere adı
    cv2.imshow('Face To Faces', frame)
    # klavyedeb q tuşuna basılması ile program kapatılır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# web kamerasını serbest bırakır. Bu fonksiyon, kaynakları boşaltır ve kamerayı kapatır.
video.release()
#açılan tüm pencereleri kapatır
cv2.destroyAllWindows()


