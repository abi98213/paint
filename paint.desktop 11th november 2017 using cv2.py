import cv2
import numpy as np

img = np.zeros((1400,1400,3),np.uint8)
cv2.namedWindow("image")
def nothing(x):
    pass

cv2.createTrackbar("R","image",0,255,nothing)
cv2.createTrackbar("G","image",0,255,nothing)
cv2.createTrackbar("B","image",0,255,nothing)
cv2.createTrackbar("RADIUS","image",0,50,nothing)


draw = False
def draw_shape(event,x,y,flag,param):
    global ix,iy,draw
    if event == cv2.EVENT_LBUTTONDOWN:
        draw = False
    if event == cv2.EVENT_RBUTTONDOWN:
        draw = True
    if event == cv2.EVENT_LBUTTONDOWN:
        draw = False
    elif event == cv2.EVENT_MOUSEMOVE:
        if draw:
            cv2.circle(img,(x,y),radius,(r,g,b),-1)
cv2.setMouseCallback("image",draw_shape)
while True:
    r = cv2.getTrackbarPos("R","image")
    b = cv2.getTrackbarPos("B","image")
    g= cv2.getTrackbarPos("G","image")
    radius = cv2.getTrackbarPos("RADIUS","image")
    cv2.imshow("image",img)
    if cv2.waitKey(1) & 0xFF == ord("c"):
        img [:] = 0
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()
