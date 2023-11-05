from utils import Utils
from transformation import Transformation
from constants import rCon



def keyExpansion(key):
    keySchedule = [None for i in range(176)]
    rConIteration = 1
    for i in range(16):
      keySchedule[i] = key[i]
    byteGenerated = 16
    while(byteGenerated < 176):
      temp = [keySchedule[byteGenerated - 4], keySchedule[byteGenerated - 3], keySchedule[byteGenerated - 2], keySchedule[byteGenerated - 1]]
      if (byteGenerated % 16 == 0):
        temp =  Utils.xorLists(Transformation.substituteBytes( Utils.shift( temp ) ), [rCon[rConIteration], 0, 0, 0])
        rConIteration += 1
      keySchedule[byteGenerated] = keySchedule[byteGenerated - 16] ^ temp[0]
      keySchedule[byteGenerated + 1] = keySchedule[byteGenerated + 1 - 16] ^ temp[1]
      keySchedule[byteGenerated + 2] = keySchedule[byteGenerated + 2 - 16] ^ temp[2]
      keySchedule[byteGenerated + 3] = keySchedule[byteGenerated + 3 - 16] ^ temp[3]
      byteGenerated += 4
    return keySchedule