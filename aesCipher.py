from transformation import Transformation
from utils import Utils


class AesCipher:
  
  def encrypt(message, expandableKeys, rounds=10):
    states = [message[i:i+16] for i in range(0, len(message), 16)]
    cipherStates = []
    for x in range(len(states)):
      state = Transformation.addRoundKey(states[x], Utils.extractRoundKey(expandableKeys, 0))
      for i in range(rounds - 1):
        state = Transformation.substituteBytes(state)
        state = Transformation.shiftRows(state)
        state = Transformation.mixColumns(state)
        state = Transformation.addRoundKey(state, Utils.extractRoundKey(expandableKeys, i + 1))


      state = Transformation.substituteBytes(state)
      state = Transformation.shiftRows(state)
      state = Transformation.addRoundKey(state, Utils.extractRoundKey(expandableKeys, 10))

      for i in range(len(state)):
        cipherStates.append(state[i])

    return cipherStates

  def decrypt(state, key, rounds=10):
    print("todo")