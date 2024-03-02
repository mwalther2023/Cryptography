import numpy as np

def encrypt(plain, key):
    index = 0
    cipher = ""
    for i in plain:
        keyShift = key[index % len(key)]
        cipher += str( chr(((ord(i)-ord('a')) + ord(keyShift)-ord('a'))%26+ord('a'))  )
        index += 1
    print("Encrypted: "+ cipher)
def decrypt(cipher, key):
    index = 0
    plain = ""
    for c in cipher:
        keyShift = key[index % len(key)]
        plain += str( chr((  (ord(c)-ord('a')) - (ord(keyShift)-ord('a')) )%26+ord('a'))  )
        index += 1
    print("Decrypted: "+ plain)


if __name__ == "__main__":
    # Vigenere cipher
    key = input("Key: ") # vizzini
    plain = input("Plaintext: ") # inconceivable
    encrypt(plain,key)
    # cipher = input("Ciphertext: ") # dvbnvpmddzatr
    # decrypt(cipher,key)


