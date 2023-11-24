import Pdf
import cv2 as cv
import cv2.aruco as aruco


VideoCap = False
# cap = cv.VideoCapture(0)
width=1080 
height=720
cap=cv.VideoCapture(0,cv.CAP_DSHOW)
cap.set(cv.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, height)
cap.set(cv.CAP_PROP_FPS,30) 
cap.set(cv.CAP_PROP_FOURCC,cv.VideoWriter_fourcc(*'MJPG'))

def findAruco(img):
    arucodict = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_4X4_250)
    arucoparam =  cv.aruco.DetectorParameters()
    detector = cv.aruco.ArucoDetector(arucodict, arucoparam)
    markerCorners, markerIds, rejectedCandidates = detector.detectMarkers(img)
    newimg = aruco.drawDetectedMarkers(img.copy(), markerCorners, markerIds)
    # print(markerIds)
    aruco_id=''
    if str(markerIds)!= "None":
        aruco_id=markerIds.flatten().tolist()
    return newimg,aruco_id
 
while True:
    ret, img = cap.read()
    if not ret:
        break
    newimg = findAruco(img)[0]
    aruco_ids=findAruco(img)[1]
    for id in aruco_ids:
        match id:
            case 0:
                Pdf.BuildPDF("Austin")
            case 1:
                Pdf.BuildPDF("Boston")
            case 2:
                Pdf.BuildPDF("Chicago")
        cv.putText(newimg, "ArUco Marker Detected", (0,30),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    cv.imshow('ArUco Marker Detection', newimg)
    cv.resizeWindow('ArUco Marker Detection',(width,height))
    cv.moveWindow('ArUco Marker Detection',0,0)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()