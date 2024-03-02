#!/usr/bin/python
import numpy as np
arr = [0]*26
englishFreq = [0.082, 0.015, 0.028, 0.042, 0.127, 0.022, 0.020, 0.061, 0.070, 0.002, 0.008, 0.040, 0.024, 0.067,
                0.075, 0.019, 0.001, 0.060, 0.063, 0.091, 0.028, 0.010, 0.023, 0.001, 0.020, 0.001]
dictionary = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
keys = []
def vigenere(cipher):
    print("Decrypting...")
    # l = 1
    ICs = []
    subtextFreq = []
    possibleBins = []
    for l in range(1,int(len(cipher)/2)):
        subtext = [""]*l
        for i in range(0, len(cipher)):
            subtext[i%l] += cipher[i]
        # print("KeyLength: "+str(l) +" | Subtext: "+str(subtext))
        possibleBins.append(subtext)
        for i in range(len(subtext)):
            subtextFreq.append(freq(subtext[i]))

        ICs.append(subtextFreq)
        subtextFreq = []
    avg = []
    for i in range(0, len(ICs)):
        for j in range(0,len(ICs[i])):
            ICs[i][j] = round(ICs[i][j],5)

    # print(possibleBins)
    
    # print("ICs: "+str(ICs))
    # print(len(ICs))
    for i in range(len(ICs)):
        # avg.append(round(0.065/sum(ICs[i]),5))
        avg.append(round(sum(ICs[i])/len(ICs[i]),5))
    # print(avg)
    # print(len(avg))
    maxIndex = 2
    max = avg[maxIndex]
    
    # for i in range(3, len(avg)):
    for i in range(3,6):
        if avg[i] > max:
            if (i+1) % (maxIndex+1) == 0:
                # print("Breaking at: "+str(i) + " | "+ str((i+1) % (maxIndex+1)))
                break
            max = avg[i]
            maxIndex = i


    print("Cipher IC: "+str(freq(cipher)))
    print("Cipher Letter Freq: "+str(arr))
    print("Key Length: "+str(maxIndex+1))#+" | Max Avg: "+str(max))

    decryptMIC = []
    letterMIC = []
    for i in range(len(possibleBins[maxIndex])):
        for k in dictionary:
            letterMIC.append(round(MIC(decrypt_vigenere(possibleBins[maxIndex][i],k)),5))
        decryptMIC.append(letterMIC)
        letterMIC = []

    # for x in range(len(decryptMIC)):
    #     print("Decrypted MICs of Bin {}".format(x))
    #     for i in range(len(decryptMIC[x])):
    #         print("\tThe Decrypted MIC of {} is {}".format(dictionary[i], decryptMIC[x][i]))

    # print("Decrypted MIC Freq for each text bin made from key size: "+str(decryptMIC))

    bestLetter = []
    for i in range(len(decryptMIC)):
        bestLetter.append(decryptMIC[i].index(np.max(decryptMIC[i])))
    # print("Best Letters: "+str(bestLetter))

    key = ""
    for l in bestLetter:
        key += dictionary[l]
    print("Best Key: "+key)
    plaintext = decrypt_vigenere(cipher,key)
    print("Plaintext: "+ str(plaintext))
    # print("The process coded for decrypting a ciphertext works best with keys of length 3-6, therefore if the key is larger or smaller than that it has the chance to be partially incorrect.")
    plainMIC = MIC(plaintext)
    print("Plaintext MIC: " +str(plainMIC))
    if abs(plainMIC - 0.065) < 0.01:
        print("The plaintext has an MIC similar to english so the key is probably correct")
    else:
        print("The plaintext's MIC has a noticable difference from enlgish and is proabably incorrect")
def freq(cipher):
    IC = 0
    for i in cipher:
        arr[ord(i)-ord('a')] += 1
    # print(str(len(cipher))+" / "+str(len(arr))+" / "+str(arr))
    for x in range(len(arr)):
        arr[x] = round(arr[x]/len(cipher),3)
        IC += arr[x]*arr[x]
    return IC
def MIC(cipher):
    MIC = 0
    for i in cipher:
        arr[ord(i)-ord('a')] += 1
    # print(str(len(cipher))+" / "+str(len(arr))+" / "+str(arr))
    for x in range(len(arr)):
        arr[x] = round(arr[x]/len(cipher),3)
        MIC += arr[x]*englishFreq[x]

    return MIC
def decrypt_vigenere(ciphertext, key):
    key = key.lower()
    plaintext = ""
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            key_char = key[key_index % len(key)]
            key_shift = ord(key_char) - ord('a')
            shifted_char = chr((ord(char) - ord('a') - key_shift) % 26 + ord('a'))
            plaintext += shifted_char
            key_index += 1
        else:
            plaintext += char
    return plaintext
if __name__ == "__main__":
    cipher = input("Ciphertext: ").lower()
    # vigenere(cipher)
    print(freq(cipher))
    print(MIC(cipher))
