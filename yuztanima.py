#OpenCV'yi projemize ekliyoruz.
import cv2
#Yüz tanıması için classımızı ekliyoruz.
face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')
#Kullanacağımız fotoğraf.
image = cv2.imread('./persons.jpg',0)
while(True):
    #Yüz tanıma classımız yüzleri arıyor.
    faces = face_cascade.detectMultiScale(image, 1.1, 5)
    #Bulunan yüzlerin etrafını çiziyoruz.
    for (x,y,w,h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    #Bulunan yüzlerle beraber fotoğrafın çıktısını gösteriyoruz.
    cv2.imshow('frame',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
