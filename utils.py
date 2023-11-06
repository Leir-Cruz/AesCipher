from constants import mask8bits


class Utils:

  def galoisMulti(a, b):
    p = 0
    hiBitSet = 0
    for i in range(8):
        if b & 1 == 1:
            p ^= a
        hiBitSet = a & 0x80
        a <<= 1
        if hiBitSet == 0x80:
            a ^= 0x1b
        b >>= 1
    return p % 256

  
  def generatePadMessage(message):
    messageOriginalSize = len(message)
    padMessageSize = messageOriginalSize
    if(messageOriginalSize % 16 != 0):
      padMessageSize = (messageOriginalSize // 16 + 1)*16
    padMessage = [None for i in range(padMessageSize)]
    for i in range(padMessageSize):
      if(i >= messageOriginalSize):
        padMessage[i] = 0
      else:
        padMessage[i] = message[i]
    return padMessage
  

  def xorLists(list1, list2):
    newList = [None for i in range(len(list1))]
    for i in range(len(list1)):
      newList[i] = list1[i] ^ list2[i]
    return newList
  
  def extractRoundKey(expanded_key, round):
    return expanded_key[round*16:round*16+16]
    


