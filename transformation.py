from constants import sBox, sBoxInv
from utils import Utils

class Transformation:

  def substituteByte(state):
     for i in range(len(state)):
      state[i] = sBox[state[i]]

  def shiftRows(state):
    for i in range(4):
      state[i*4:i*4+4] = Utils.rotate(state[i*4:i*4+4],i)


  def mixColumn(column):
    mixedColumn = [
        Utils.galouisMultiplicationX2(column[0]) ^ Utils.galouisMultiplicationX3(
            column[1]) ^ column[2] ^ column[3],
        Utils.galouisMultiplicationX2(column[1]) ^ Utils.galouisMultiplicationX3(
            column[2]) ^ column[3] ^ column[0],
        Utils.galouisMultiplicationX2(column[2]) ^ Utils.galouisMultiplicationX3(
            column[3]) ^ column[0] ^ column[1],
        Utils.galouisMultiplicationX2(column[3]) ^ Utils.galouisMultiplicationX3(
            column[0]) ^ column[1] ^ column[2],
    ]
    return mixedColumn

  def mixColumns(state):
    mixedColumns = [[], [], [], []]
    for i in range(4):
        column = [grid[j][i] for j in range(4)]
        column = Utils.mix_column(column)
        for i in range(4):
            mixedColumns[i].append(column[i])
    return mixedColumns

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
    
  def invMixColumns(mixedState):
    firstMixed = Transformation.mixColumns(mixedState)
    secondMixed = Transformation.mixColumns(firstMixed)
    unMixedState = Transformation.mixColumns(secondMixed)
    return unMixedState
