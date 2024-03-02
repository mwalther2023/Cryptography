import numpy as np


def affine(cipher):
    y = 0
    x = 0
    out = ""
    for a in range(1,26):
        for b in range(1,26):
            for i in range(0,len(cipher)):
                y = (ord(cipher[i])-ord('a')) % 26
                # x = ((x*a) + (b) )% 26
                x = ((y-b)*(26-a)) %26
                # out += chr( (x+ord('a')) )
                out += " "+str(x)
            if(a == 409%26 and b == 3):
                print("A="+str(a)+",B="+str(b)+": "+str(out))
            out = ""
        
if __name__ == "__main__":
    print("HW4")
    cipher = input("Ciphertext: ")
    affine(cipher.lower())
