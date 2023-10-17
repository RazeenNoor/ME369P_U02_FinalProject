import cv2
frontf_cascade=cv2.CascadeClassifier("Haar Cascades/data/haarcascade_frontalface_alt2.xml")
eye_cascade=cv2.CascadeClassifier("Haar Cascades\data\haarcascade_eye_tree_eyeglasses.xml")
width=480
height=560
xpos=0
ypos=0
counter=1
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS,30) 
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    rec,frame=cam.read()
    #Cascades works on gray scale so the colored camera feed must be converted
    newframe=frame.copy()
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=frontf_cascade.detectMultiScale(gray_frame,1.5,5)
    eyes=eye_cascade.detectMultiScale(gray_frame,1.5,5)
    for x,y,w,h in eyes:
        frameROI=frame[y:y+h,x:x+w]
        newframe[y:y+h,x:x+w]=frameROI
        cv2.rectangle(newframe,(x,y),(x+w,y+h),(0,255,255),4)
    for x,y,w,h in faces:
        counter+=1
        frameROI=frame[y:y+h,x:x+w]
        frameROIgray=cv2.cvtColor(frameROI,cv2.COLOR_BGR2GRAY)
        frameROIBGR=cv2.cvtColor(frameROIgray,cv2.COLOR_GRAY2BGR)
        cv2.rectangle(newframe,(x,y),(x+w,y+h),(0,255,255),4)
        xfrac=faces[0][0]/width #1st person in frame controls position
        yfrac=faces[0][1]/width
        # xpos=int(1020*xfrac)
        # ypos=int(1080*yfrac)
    cv2.imshow('Camera', newframe)   
    cv2.moveWindow('Camera',xpos,ypos) 
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows
        

