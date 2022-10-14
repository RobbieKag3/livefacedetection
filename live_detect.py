import cv2
facecascade=cv2.CascadeClassifier("PRO-C106-Student-Boilerplate-main/haarcascade_frontalface_default.xml")
video=cv2.VideoCapture(0)
while True:
    ret,frame=video.read()
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=facecascade.detectMultiScale(grey,1.1,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow("face",frame)
    if cv2.waitKey(1)==32:
        break
video.release()
cv2.destroyAllWindows()