# lecre_colour.py
# @epk-bder 23/12/2024
# adapted 24/01/2025

def hexCToLCC(channel):
    digit1Key = {0 : "A", 1 : "B", 2 : "C", 3 : "D"}
    digit1num = channel // 64
    digit1 = digit1Key[digit1num]
    
    digit2num = channel - (64 * digit1num)
    base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    digit2 = base64[digit2num]
    return(digit1 + digit2)

def new(r, g, b, a=0):
    lcColour = hexCToLCC(r) + hexCToLCC(g) + hexCToLCC(b)
    return lcColour