# generateVideo.py
# @epk-bder 09/03/2025

import numpy as np
import cv2
 
import frameGen

def generate(vid, dim=7, fcount=60, dfps=1):
    video = cv2.VideoCapture('bad_apple.mp4')
    fps = int(video.get(cv2.CAP_PROP_FPS))
    frameIndex = 0
    videoResult = "~E-AAgAf/f2ABAAAAAAA-AAgAgCgMACAAAAAAA-AAgAf8f2AsAAAAAAAABAA-" # beebo spawn point and ic or else game crashes + portal under beebo spawn with id 0
    while video.isOpened():
        success, frame = video.read()
        if not success:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        if frameIndex > fps * fcount: 
            break
        if frameIndex % (fps // dfps) == 0:
            videoResult += frameGen.createFrame(frame, dim, frameIndex // fps, dfps)
        frameIndex += 1
     
    video.release()
    print("\n"*3, videoResult, sep="")
    
if __name__ == "__main__":
    generate("bad_apple.mp4")