from constants import sBox, sBoxInv
from copy import copy
from utils import Utils

class Transformation:

  def substituteBytes(state):
    for i in range(len(state)):
      state[i] = sBox[state[i]]
    return state

  def shiftRows(state):
    for i in range(4):
      state[i*4:i*4+4] = Utils.shift(state[i*4:i*4+4],i)
    return state


  def mixColumn(column):
    temp = copy(column)
    mixedColumn = [
    Utils.galoisMulti(temp[0],2) ^ Utils.galoisMulti(temp[3],1) ^ \
                Utils.galoisMulti(temp[2],1) ^ Utils.galoisMulti(temp[1],3),
    Utils.galoisMulti(temp[1],2) ^ Utils.galoisMulti(temp[0],1) ^ \
                Utils.galoisMulti(temp[3],1) ^ Utils.galoisMulti(temp[2],3),
    Utils.galoisMulti(temp[2],2) ^ Utils.galoisMulti(temp[1],1) ^ \
                Utils.galoisMulti(temp[0],1) ^ Utils.galoisMulti(temp[3],3),
    Utils.galoisMulti(temp[3],2) ^ Utils.galoisMulti(temp[2],1) ^ \
		    Utils.galoisMulti(temp[1],1) ^ Utils.galoisMulti(temp[0],3)
    ]
    return mixedColumn

  def mixColumns(state):
    mixedColumns = [None for i in range(len(state))]
    for i in range(4):
      column = [state[j + i] for j in range(0, 16, 4)]
      mixedColumn = Transformation.mixColumn(column)
      h = 0
      for j in range(0, 16, 4):
        mixedColumns[j + i] = mixedColumn[h]
        h += 1
    return mixedColumns

  def addRoundKey(state, roundKey):
    for i in range(len(state)):
      state[i] = state[i] ^ roundKey[i]
    return state


  def invSubstituteBytes(state):
    for i in range(len(state)):
      state[i] = sBoxInv[state[i]]
    return state

  def invShiftRows(state):
    for i in range(4):
      state[i*4:i*4+4] = Utils.shift(state[i*4:i*4+4],-i)
    return state
    
  def invMixColumns(mixedState):
    firstMixed = Transformation.mixColumns(mixedState)
    secondMixed = Transformation.mixColumns(firstMixed)
    unMixedState = Transformation.mixColumns(secondMixed)
    return unMixedState
