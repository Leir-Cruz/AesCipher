from keyExpansion import keyExpansion

if __name__ == "__main__":
  print("Começar processo de cifração AES 128 bits\n")
  key = [0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07,0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0f, 0x10]
  print(f"chave usada para encriptar: {key}\n")

  expandableKeys = keyExpansion(key)
  print(f"chave após processo de expansão: {expandableKeys}\n")

