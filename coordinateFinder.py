# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 13:05:47 2021

@author: hariom
"""

# create a function which help to find the coordinate of any pixel and its color

import cv2
import numpy as np

def mouse_event(event, x, y, flg, param):
    print("event==",event)
    print("x==",x)
    print("y==",y)
    print("flg==",flg)
    print("param==",param)
    font = cv2.FONT_HERSHEY_PLAIN 
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,', ' ,y)
           
        cord = ". "+str(x) + ', '+ str(y)
        cv2.putText(img, cord, (x, y), font, 1, (100,200 ,0), 2)
        cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        b= img[y, x, 0] #for blue channel is 0
        g = img[y, x, 1] #for green channel is 1
        r = img[y, x, 2] #for red channel is 2
        
        color_bgr = ". "+str(b) + ', '+ str(g)+ ', '+ str(r)
        cv2.putText(img, color_bgr, (x, y), font, 1, (100, 10, 200), 2)
        cv2.imshow('image', img)


# img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('C:\\Users\\hario\\Desktop\\pythonCourse\\openCV11Hour\\TestImages\\pic9.jpg')
cv2.imshow('image', img)


cv2.setMouseCallback('image', mouse_event)

cv2.waitKey(0)
cv2.destroyAllWindows()