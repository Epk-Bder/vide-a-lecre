# run.py
# @epk-bder 13/04/2025

import os.path
import generateVideo

if __name__ == "__main__":
    
    print(
        r'''
 __  __          __                                     __                                    
/\ \/\ \  __    /\ \                                   /\ \                                   
\ \ \ \ \/\_\   \_\ \     __              __           \ \ \         __    ___   _ __    __   
 \ \ \ \ \/\ \  /'_` \  /'__`\ _______  /'__`\   _______\ \ \  __  /'__`\ /'___\/\`'__\/'__`\ 
  \ \ \_/ \ \ \/\ \L\ \/\  __//\______\/\ \L\.\_/\______\\ \ \L\ \/\  __//\ \__/\ \ \//\  __/ 
   \ `\___/\ \_\ \___,_\ \____\/______/\ \__/.\_\/______/ \ \____/\ \____\ \____\\ \_\\ \____\
    `\/__/  \/_/\/__,_ /\/____/         \/__/\/_/          \/___/  \/____/\/____/ \/_/ \/____/
                                                                                              
        '''
    )
    
    print("=== Video to Robot 64 level ===\n")
    while True:
        videoName = input("Enter file location: ")
        if  os.path.isfile(videoName):
            break
        else: print("\nInvalid file location, try again\n")
    while True:
        vidDim = map(int, input("Enter video width and height, 2 number seperated by a space must be an odd number and greater than 3: ").split(" "))
        vidDim = list(vidDim)
        if vidDim[0] % 2 == 1 and vidDim[0] > 3 and vidDim[1] % 2 == 1 and vidDim[1] > 3:
            break
        else: print("\nInvalid dimensions entered\n")
    while True:
        desFPS = int(input("Enter the desired FPS for the video: "))
        if desFPS >= 1:
            break
        else: print("\nInvalid FPS entered\n")
    frameCount = int(input("Enter the amount of frames you want to be generated: ")) - 1
    
    generateVideo.generate(videoName, vidDim, frameCount, desFPS)
    