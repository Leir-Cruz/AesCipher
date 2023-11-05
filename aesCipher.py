from transformation import Transformation
from utils import Utils
from keyExpansion import keyExpansion


class AesCipher:
  
  def encrypt(plainText, key, rounds=10):
    state = plainText
    expandableKeys = keyExpansion(key)
    state = Transformation.addRoundKey(state)
    for i in range(rounds - 1):
      Transformation.substituteBytes(state)
      Transformation.shiftRows(state)
      Transformation.mixColumns(state)
      Transformation.addRoundKey(state, expandableKeys + (16 + (i+1)))

    Transformation.substituteBytes(state)
    Transformation.shiftRows(state)
    Transformation.addRoundKey(state, expandableKeys + (160))

  def decrypt(state, key, rounds=10):
    print("todo")