import cv2
frontf_cascade=cv2.CascadeClassifier("Haar Cascades\data\haarcascade_frontalface_default.xml")
eye_cascade=cv2.CascadeClassifier("Haar Cascades\data\haarcascade_eye_tree_eyeglasses.xml")
width=620 
height=480
xpos=0
ypos=0
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
    for x,y,w,h in faces:
        frameROI=frame[y:y+h,x:x+w]
        frameROIgray=cv2.cvtColor(frameROI,cv2.COLOR_BGR2GRAY)
        frameROIBGR=cv2.cvtColor(frameROIgray,cv2.COLOR_GRAY2BGR)
        cv2.rectangle(newframe,(x,y),(x+w,y+h),(0,85,204),4)
        xfrac=faces[0][0]/width 
        yfrac=faces[0][1]/width
        newframe[y:y+h,x:x+w]=frameROIBGR
        #xpos=int(1020*xfrac)
        #ypos=int(1080*yfrac)
        if len(faces) ==1:
            cv2.putText(newframe, "Person Detected", (0,height-10),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,255),2)
        else:
            cv2.putText(newframe, str(len(faces))  + " People Detected", (0,height-10),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,255),2)

    # for x,y,w,h in eyes:
    #     frameROI=frame[y:y+h,x:x+w]
    #     newframe[y:y+h,x:x+w]=frameROI
    #     cv2.rectangle(newframe,(x,y),(x+w,y+h),(0,255,255),4)
    cv2.imshow('Camera', newframe)   
    cv2.moveWindow('Camera',xpos,ypos) 
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows 

