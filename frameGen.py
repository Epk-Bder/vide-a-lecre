# frameGen.py
# @epk-bder 24/01/2025
# fully reworked 08/03/2025

import cv2

import lecrecolour
import lecreposition

def createFrame(img, zOffset=0):
    pixelInfo = []
    img = cv2.resize(img, (7, 7))
    for i, row in enumerate(img):
        for j, pixel in enumerate(row):
            if i == j and i == 3:
                continue
            
            position = lecreposition.toLCPos(2048 + (zOffset * 32), 2048 + (i * -4), 2048 + (j * 4))
            colour = lecrecolour.new(*pixel)
            pixelInfo.append((position, colour))

    blockcode = 'AM^AEAEAEAAA&AAAAAA-' # Code for brightblock with position "^" and colour "&"
    finalcode = "~B-AAgAf/f2ABAAAAAAA-AAgAgCgMACAAAAAAA-" # level code for just beebo and ic
    for pixel in pixelInfo:
        newBlock = blockcode
        finalcode += newBlock.replace("^", pixel[0]).replace("&", pixel[1])
    return finalcode
    
if __name__ == "__main__":
    print(createFrame(cv2.imread("picture.png")))