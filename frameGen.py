# frameGen.py
# @epk-bder 24/01/2025
# fully reworked 08/03/2025

import cv2

import lecrecolour
import lecreposition
import frameTiming

def createFrame(img, imgDim, zOffset=0, dfps=1):
    pixelInfo = []
    finalcode = "" 
    blockcode = 'AM^AEAEAEAAA&AAAAAA-' # brightblock with position ^ and colour &
    img = cv2.resize(img, (imgDim, imgDim)) 
    for i, row in enumerate(img):
        for j, pixel in enumerate(row):
            x, y, z = 2048 + (j * -4), 2048 + (i * -4), zOffset * 32
            while True:
                if z >= 4096:
                    z -= 4096
                    x -= 64
                else: break
            if i == j and i == imgDim//2:
                finalcode += frameTiming.portal(x, y, z, dfps)
            else:
                position = lecreposition.toLCPos(x, y, z)
                colour = lecrecolour.new(*pixel)
                # pixelInfo.append((position, colour))
                newBlock = blockcode
                finalcode += newBlock.replace("^", position).replace("&", colour)

    #blockcode = 'AM^AEAEAEAAA&AAAAAA-' # Code for brightblock with position "^" and colour "&"
    #finalcode = "" # level code for just beebo and ic
    #for pixel in pixelInfo:
    #    newBlock = blockcode
    #    finalcode += newBlock.replace("^", pixel[0]).replace("&", pixel[1])
    return finalcode
    
if __name__ == "__main__":
    print(createFrame(cv2.imread("picture.png")))