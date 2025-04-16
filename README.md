
# Vide-a-Lecre
### by Epik

## What it is

Vide-a-Lecre is a tool that converts videos to Robot 64 level codes,

## Installation
1. Download the files from this repository
2. Install *python*
3. Install **opencv-python**
```
pip install opencv-python
```

## Usage

1. Run the file *run.py*
2. Follow the instructions given
### Example
```
 __  __          __                                     __
/\ \/\ \  __    /\ \                                   /\ \
\ \ \ \ \/\_\   \_\ \     __              __           \ \ \         __    ___   _ __    __
 \ \ \ \ \/\ \  /'_` \  /'__`\ _______  /'__`\   _______\ \ \  __  /'__`\ /'___\/\`'__\/'__`\
  \ \ \_/ \ \ \/\ \L\ \/\  __//\______\/\ \L\.\_/\______\\ \ \L\ \/\  __//\ \__/\ \ \//\  __/
   \ `\___/\ \_\ \___,_\ \____\/______/\ \__/.\_\/______/ \ \____/\ \____\ \____\\ \_\\ \____\
    `\/__/  \/_/\/__,_ /\/____/         \/__/\/_/          \/___/  \/____/\/____/ \/_/ \/____/


=== Video to Robot 64 level ===

Enter file location: C:\bad_apple.mp4
Enter video dimension (width and height) must be an odd number and greater than 3: 7
Enter the desired FPS for the video: 2
Enter the amount of frames you want to be generated: 30
```
*The inputs above result in the first 15 seconds of the video "bad_apple.mp4"*<br>
`30 frames / 2 fps = 15 seconds`

* Enter file location - pretty self explanatory
* Enter video dimension - Vide-a-lecre only makes square videos at this point in time, this is subject to change
* Enter the desired FPS for the video - the higher this number the faster the water current is in the level meaning higher fps
* Enter the amount of frames you want to be generated - 30 frames will be generated total
