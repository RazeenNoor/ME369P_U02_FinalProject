import cv2
import face_recognition as FR
font=cv2.FONT_HERSHEY_SIMPLEX
    #train
bface=FR.load_image_file('filepath as .jpg')
faceloc=FR.face_locations(bface)[0] 
bfaceencode=FR.face_encodings(bface)[0] 

knownencode=[bfaceencode]
names=['Name']
    #test
width= 640
height= 360
cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)   
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30) 
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
while True:
    ignore, frame=cam.read()
    unknownface=frame
    facelocs=FR.face_locations(unknownface)
    ukencodes=FR.face_encodings(unknownface,facelocs)
    
    for i,j in zip(facelocs,ukencodes):     #steps through arrays simultaneously
        t,r,b,l=i
        cv2.rectangle(unknownface,(l,t),(r,b),(255.0,0),2)
        name='unknown'
        matches=FR.compare_faces(knownencode,j) #check matching of known faces to faces in picture(j) -> outputs True/False
        if True in matches:
            mindex=matches.index(True) #returns index of matches in array
            print(mindex)
            name=(names[mindex])
            cv2.putText(unknownface,str(name),(l,t),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)

    cv2.imshow('window',unknownface)
    if cv2.waitKey(1) & 0xff ==ord('q'):   
        break   
cam.release()
































# import cv2
# print(cv2.__version__)
# width= 1280
# height= 720
# cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)   
# cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
# cam.set(cv2.CAP_PROP_FPS,30)
# cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
# while True: 
#     ignore, frame=cam.read()  
#     frame=cv2.resize(frame,(int(width),int(height)))  
#     grayFrame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) 
#     cv2.imshow('mycam',frame)      
#     cv2.moveWindow('mycam',0,0)
#     if cv2.waitKey(1) & 0xff ==ord('q'):  
#         break  
# cam.release()