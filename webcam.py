import cv2
cam=cv2.VideoCapture(0)
_,img=cam.read()

cv2.namedWindow("camera")
while True:
    cv2.imshow('camera', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break;