import cv2 as cv
import cv2.aruco as aruco

VideoCap = False
cap = cv.VideoCapture(0)

def findAruco(img):
    arucodict = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_4X4_250)
    arucoparam =  cv.aruco.DetectorParameters()
    detector = cv.aruco.ArucoDetector(arucodict, arucoparam)
    markerCorners, markerIds, rejectedCandidates = detector.detectMarkers(img)
    newimg = aruco.drawDetectedMarkers(img.copy(), markerCorners, markerIds)
    # print(markerIds)
    return newimg
 
while True:
    ret, img = cap.read()
    if not ret:
        break

    newimg = findAruco(img)
    cv.imshow('ArUco Marker Detection', newimg)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()