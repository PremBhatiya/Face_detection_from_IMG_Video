import cv2
import random 
#put your file here
trained_face_data=cv2.CascadeClassifier('./haarcasecade_face.xml')
#classifer word for cv in finding something

#chose image or video
img=cv2.imread('RDJ.jpg')

    


#turn image into grey
gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)




# #detect face
face_coordinate=trained_face_data.detectMultiScale(gray_image)
print(face_coordinate)


# #drawing rectangle around faces
for(x,y,w,h) in face_coordinate:
    cv2.rectangle(img,(x,y),(x+w,y+h),(random.randrange(256),random.randrange(256),random.randrange(256)))

  #pops up windows to show image
cv2.imshow('clever programmer face detector',img)
#to function put window on hold until any key is pressed down
cv2.waitKey()