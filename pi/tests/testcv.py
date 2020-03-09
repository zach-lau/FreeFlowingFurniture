import cv2 as cv
import numpy 

vid = cv.VideoCapture(0)
while 1: 
	ret, frame = vid.read()
	cv.imshow("Bots", frame)
	cv.waitKey(0)
