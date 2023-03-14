import cv2
import random 
#put your file here
trained_face_data=cv2.CascadeClassifier('./haarcasecade_face.xml')
webcam=cv2.VideoCapture('lolo_meme.mp4')
while True:
    ## getting image out of video/ reading frame 
    successful_frame_read,frame=webcam.read()
    #for frame
    gray_image=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face_coordinate=trained_face_data.detectMultiScale(gray_image)
    #pop window for show image
    # #drawing rectangle around faces
    for(x,y,w,h) in face_coordinate:
      cv2.rectangle(frame,(x,y),(x+w,y+h),(random.randrange(256),random.randrange(256),random.randrange(256)))

    cv2.imshow('clever programmer face detector',frame)
    #to function put window on hold until any key is pressed down
    key =cv2.waitKey(1)
    #stop screen play
    if key==81 or key==113:
        break
    
#realease the videocapture objectws
webcam.release()
     
     
#some part of video is left 1.32.28 python AI tutorial-for begineer


