from constants import mask8bits, rCon
import random
import os


class Utils:

  def shift(word, n=1):
    return word[n:]+word[0:n]
  
  def apply8bitMask(hexNumber):
    return hexNumber & mask8bits

  def galouisMultiplicationX2(hexNumber):
    deslocated = hexNumber << 1
    masked = Utils.apply8bitMask(deslocated)
    if (hexNumber & 128) != 0:
        masked ^= 0x1b
    return masked

  def galouisMultiplicationX3(hexNumber):
    return Utils.galouisMultiplicationX2(hexNumber) ^ hexNumber

  def getRandomKey():
    random_key = os.urandom(16)
    return random_key
  
  def generatePadMessage(message):
    messageOriginalSize = len(message)
    padMessageSize = messageOriginalSize
    if(messageOriginalSize % 16 != 0):
      padMessageSize = ( padMessageSize / 16 + 1) * 16
    padMessage = [None for i in range(padMessageSize)]
    for i in range(padMessageSize):
      if(i > messageOriginalSize):
        padMessage[i] = 0
      else:
        padMessage[i] = message[i]

  def xorLists(list1, list2):
    newList = [None for i in range(len(list1))]
    for i in range(len(list1)):
      newList[i] = list1[i] ^ list2[i]
    return newList
    


