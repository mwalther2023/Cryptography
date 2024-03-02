
def decode_shift_all(ciphertext):
    for shift in range(26):
        plaintext = ""
        for char in ciphertext:
            if char.isalpha():
                shifted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
                plaintext += shifted_char
            else:
                plaintext += char
        print("Shift {}: {}".format(shift, plaintext))
def encode_shift_all(ciphertext):
    for shift in range(26):
        plaintext = ""
        for char in ciphertext:
            if char.isalpha():
                shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
                plaintext += shifted_char
            else:
                plaintext += char
        print("Shift {}: {}".format(shift, plaintext))

def freq(cipher):
    arr = [0]*26
    dictionary = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    out = 0
    for i in cipher:
        arr[ord(i)-ord('a')] += 1
    print(str(len(cipher))+" / "+str(len(arr))+" / "+str(arr))
    for x in range(len(arr)):
        arr[x] = round(arr[x]/len(cipher),3)
        out += arr[x]*arr[x]
    for x in range(len(arr)):
        print("The frequency of {} is {}".format(dictionary[x], arr[x]))
    print(out)
if __name__ == "__main__":

    cipher = input("Ciphertext: ").lower()
    decode_shift_all(cipher)
    # encode_shift_all(cipher)

    freq(cipher)