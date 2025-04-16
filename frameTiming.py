# frameTiming.py

import lecreposition
import lecrecolour

startPortalCode = "AA*AsAAAAAAAAA_-"
endPortalCode = "AA*AsAAAAAAAAB_-"
waterCode =  "AE*AEAEAEAAAAAAA_AA-" # AE*AEAEAEAAAAAAAABAA-
def portal(x, y, z, fps=1):
    newStartPortal = startPortalCode.replace("*", lecreposition.toLCPos(x, y, z)).replace("_", lecrecolour.hexCToLCC(int(z/32)))
    newEndPortal = endPortalCode.replace("*", lecreposition.toLCPos(x, y, z+6)).replace("_", lecrecolour.hexCToLCC(int((z/32))+1))
    newWater = waterCode.replace("*", lecreposition.toLCPos(x, y, z)).replace("_", lecrecolour.hexCToLCC(int(fps)))
    return newStartPortal + newEndPortal + newWater