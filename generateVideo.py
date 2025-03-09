# generateVideo.py
# @briander 09/03/2025

import numpy as np
import cv2 as cv
 
import frameGen

video = cv.VideoCapture('bad_apple.mp4')
frames_per_second = int(video.get(cv2.CAP_PROP_FPS))

frameIndex = 0
while video.isOpened():
    success, frame = video.read()
    
    if not success:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    frameIndex += 1
    
    createFrame(frame, frameIndex)
    
    if frameIndex > 15:
        break
     
        
    
    #frameGen.createFrame:
 
cap.release()
cv.destroyAllWindows()