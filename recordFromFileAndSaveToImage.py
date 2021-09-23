# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 21:33:52 2021

@author: hario
"""

# take input from video and capture its images and save to folder back

import cv2

# vidcap=cv2.VideoCapture("C:\\Users\\hario\\Desktop\\pythonCourse\\openCV11Hour\\projects\\ha.mp4")

'''
# import pafy
# to read the video from youtube
# url="https://www.youtube.com/watch?v=JiV8MLQjJsw&list=RDJiV8MLQjJsw&start_radio=1"

# data=pafy.new(url)
# data=data.getbest(preftype='mp4') 
# vidcap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
# vidcap.open(data.url)
# ret,image=vidcap.read()
'''

# reading from file
# vidPath="C:\\Users\\hario\\Desktop\\pythonCourse\\openCV11Hour\\videoFiles\\kanhaiya.mp4"
pathToSave="C:\\Users\\hario\\Desktop\\pythonCourse\\openCV11Hour\\projects\\framesCaptured\\"

vidcap=cv2.VideoCapture(0)
ret,image=vidcap.read() #read the video from file
image=cv2.resize(image,(640,480))
count=0
while True:
    if ret==True:
        cv2.imwrite(f"{pathToSave}img{count}.jpg",image)
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count**100))
        ret,image=vidcap.read()
        cv2.imshow("res",image)
        count+=1
        
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
        #     cv2.destroyAllWindows()
        # else:
        #     break
vidcap.release()
cv2.destroyAllWindows()
