from constants import sBox, sBoxInv
from utils import Utils

class Transformation:

  def substituteByte(state):
     for i in range(len(state)):
      state[i] = sBox[state[i]]

  def shiftRows(state):
    for i in range(4):
      state[i*4:i*4+4] = Utils.rotate(state[i*4:i*4+4],i)

  def mixColumns(state):
    print("mixColumns")

  def addRoundKey(word, roundKey):
    for i in range(4):
      word[i] = word[i] ^ roundKey[i]
    return word


  def invSubstituteByte(state):
    for i in range(len(state)):
      state[i] = sBoxInv[state[i]]
    return state

  def invShiftRows(state):
    for i in range(4):
      state[i*4:i*4+4] = Utils.rotate(state[i*4:i*4+4],-i)
    return state
    

  def invMixColumns(state):
    print("mixColumns")
