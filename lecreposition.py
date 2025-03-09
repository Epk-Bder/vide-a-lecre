# lecreposition.py
# @epk-bder 24/01/2025

def toLCPos(x, y, z):
    base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    pos = [["", ""], ["", ""], ["", ""]]
    
    pos[0][0] = base64[x // 64]
    pos[0][1] = base64[x - ((x//64) * 64)]
    x = pos[0][0] + pos[0][1]
    
    pos[1][0] = base64[y // 64]
    pos[1][1] = base64[y - ((y//64) * 64)]
    y = pos[1][0] + pos[1][1]
    
    pos[2][0] = base64[z // 64]
    pos[2][1] = base64[z - ((z//64) * 64)]
    z = pos[2][0] + pos[2][1]
    return x + y + z
#print(toLCPos(2048, 3, 255))