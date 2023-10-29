from constants import mask8bits

class Utils:

  def encrypt(plainText, key, rounds):
    print("todo")

  def decrypt(state, key, rounds):
    print("todo")

  def rotate(row, n):
    return row[n:]+row[0:n]
  
  def apply8bitMask(hexNumber):
    return hexNumber & 0xff

  def galouisMultiplicationX2(hexNumber):
    deslocated = hexNumber << 1
    masked = Utils.apply8bitMask(deslocated)
    if (hexNumber & 128) != 0:
        masked ^= 0x1b
    return masked

  def galouisMultiplicationX3(hexNumber):
    return Utils.galouisMultiplicationX2(hexNumber) ^ hexNumber
