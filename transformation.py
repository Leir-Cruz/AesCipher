from constants import sBox, sBoxInv
from copy import copy
from utils import Utils

class Transformation:

  def substituteBytes(state):
    for i in range(len(state)):
      state[i] = sBox[state[i]]
    return state

  def shiftRows(state):
    return [
        state[0], state[5], state[10], state[15],
        state[4], state[9], state[14], state[3],
        state[8], state[13], state[2], state[7],
        state[12], state[1], state[6], state[11]
    ]


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
      column = state[i * 4: i * 4 + 4]
      mixedColumn = Transformation.mixColumn(column)
      mixedColumns[i * 4: i * 4 + 4] = mixedColumn
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
    return [
        state[0], state[13], state[10], state[7],
        state[4], state[1], state[14], state[11],
        state[8], state[5], state[2], state[15],
        state[12], state[9], state[6], state[3]
    ]
    
  def invMixColumns(mixedState):
    firstMixed = Transformation.mixColumns(mixedState)
    secondMixed = Transformation.mixColumns(firstMixed)
    unMixedState = Transformation.mixColumns(secondMixed)
    return unMixedState
