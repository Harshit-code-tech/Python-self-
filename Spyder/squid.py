import numpy as np
import cv2 as cv
img = cv.imread('Photos/tiger.jpg')

img = cv.resize(img, (800,1600), interpolation = cv.INTER_AREA)

#open the gui
cv.imshow('Tiger', img)

cv.waitKey(1000)
capture = cv.VideoCapture(0)


while True:
    frame = capture.read()
    cv.imshow('Video', frame)

    if(cv.waitKey(20) & 0xFF==ord('q')):
        break

capture.release()
cv.destroyAllWindows()
#reads the picture
img = cv.imread('Photos/tiger.jpg')

#open the gui
cv.imshow('Tiger', img)

#no of ms the gui waits
cv.waitKey(1000)
capture = cv.VideoCapture(0)

# to stop video/webcam
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if(cv.waitKey(20) & 0xFF==ord('q')):
        break

capture.release()
cv.destroyAllWindows()
import numpy as np

#zeroes((dimension x,dimension y, channels))
blank = np.zeros((500,500,3), dtype='uint8')
cv.rectangle(img, (0,0), (250,250), (0,255,0), thickness=2)
## iamge to draw on, source pts, destination pts, color(RGB), border

##thickness = -1 or cv.FILLED will fill entire box with color

cv.circle(img, (250,250), 50, (0,0,255), thickness=5)
## iamge to draw on, centre pts, radius, color(RGB), border

cv.line(img, (0,0), (300,400), (255,0,0), thickness=20)
cv.putText(img, "RRRAARRRGH TIGHERRR", (100, 100), cv.FONT_HERSHEY_COMPLEX, 2.0, (0,0,0), thickness=2)
## iamge to draw on, source pts, font face, font scale, color, thickness
# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur 
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

# Dilating the image
dilated = cv.dilate(img, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(img, (7,7), iterations=3)
cv.imshow('Eroded', eroded)
from cvzone import HandTrackingModule, overlayPNG

capture = cv.VideoCapture(0)
detector = HandTrackingModule.HandDetector(maxHands=2, detectionCon=0.77)
## max hands for no of hands we need to detect
## detectionCon for percentage of error we can allow. Range is from 0 to 1

while True:
    isTrue, frame = capture.read()
    hands, img = detector.findHands(frame, flipType=True)

    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmark points
        bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
        centerPoint1 = hand1['center']  # center of the hand cx,cy
        handType1 = hand1["type"]  # Handtype Left or Right

        fingers1 = detector.fingersUp(hand1)

        if len(hands) == 2:
            # Hand 2
            hand2 = hands[1]
            lmList2 = hand2["lmList"]  # List of 21 Landmark points
            bbox2 = hand2["bbox"]  # Bounding box info x,y,w,h
            centerPoint2 = hand2['center']  # center of the hand cx,cy
            handType2 = hand2["type"]  # Hand Type "Left" or "Right"

            fingers2 = detector.fingersUp(hand2)

    cv.imshow('Video', frame)


    if(cv.waitKey(20) & 0xFF==ord('q')):
        break

capture.release()
cv.destroyAllWindows() 
