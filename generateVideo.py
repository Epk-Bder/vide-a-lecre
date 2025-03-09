# generateVideo.py
# @briander 09/03/2025

import numpy as np
import cv2
 
import frameGen

video = cv2.VideoCapture('bad_apple.mp4')
fps = int(video.get(cv2.CAP_PROP_FPS))
frameIndex = 0
videoResult = "~E-AAgAf/f2ABAAAAAAA-AAgAgCgMACAAAAAAA-" # beebo spawn point and ic or else game crashes
while video.isOpened():
    success, frame = video.read()
    if not success:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    if frameIndex > 600:
        break
    if frameIndex % fps == 0:
        videoResult += frameGen.createFrame(frame, frameIndex // fps)
    frameIndex += 1
 
video.release()
print(videoResult)