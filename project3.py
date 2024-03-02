import numpy as np
from numpy import random as rand
import math
import random
import sys
import time

def it_jac(a,n):
    a %= n
    result = 1
    while a != 0:
        while a % 2 == 0:
            a /= 2
            n_mod_8 = n % 8
            if n_mod_8 in (3, 5):
                result = -result
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a %= n
    if n == 1:
        return result
    else:
        return 0
def exp_mod(x, y, p) :
    res = 1 
    x = x % p
    if (x == 0) :
        return 0
    while (y > 0) :
        if ((y & 1) == 1) :
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res
def iterative_gcd(a, b):
    if b > a:
        t = b
        b = a
        a = t
    while b > 0:
        q = int(a/b)
        r = a%b
        a = b
        b = r
    # print("GCD: "+str(a))
    return a
def gcdExtended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcdExtended(b % a, a)
    x = y1 - (b//a) * x1
    y = x1
    return gcd, x, y
# pub = (10235248904450273447, 1644052926450591421)
# priv = (10235248904450273447, 7816340532911148613)
pub = (16992811533205638443399234761866396091239925967673828336015551204769234877095007455590202950848594319049608092753082165516903943150424458674173979005786869628675016120463162540084768423405811041305821702587679888284749091825324739334374228519184498270334044159028495435473400271410009461988924722281049958554834241444584066507231624320449432192854891915114380285239725790763526680529576017623158555027533202141937148281054989377801086878408494785822265275549939388039351250053244223212643931474462637020733348343717784643408004321448855552773753586690915091565627453452984591139137293901295539509835167652837474009551,
       3270304030620914560906892734922597208266372985475447409208687782900547713781529528041533727039243228502307537604663923262229754474302718887934107557449580824423515342689287038539245688382641151505141476102197658737259036019044388533921316685926506198604047733242349666390275939041758817957911764809134462965986044306486509445606123233462981561667945008117647891931687629482342600812345041232509628431838730932879397073119913724407208436832499667300037497449461426890954285184098642180167921436801688704243061595648089002254125342528568826999049152672968093965309421771782407180477096482049679608703788694959569434423)
priv = (16992811533205638443399234761866396091239925967673828336015551204769234877095007455590202950848594319049608092753082165516903943150424458674173979005786869628675016120463162540084768423405811041305821702587679888284749091825324739334374228519184498270334044159028495435473400271410009461988924722281049958554834241444584066507231624320449432192854891915114380285239725790763526680529576017623158555027533202141937148281054989377801086878408494785822265275549939388039351250053244223212643931474462637020733348343717784643408004321448855552773753586690915091565627453452984591139137293901295539509835167652837474009551,
        10908797951378561839568622955917767214017991422325884283358409452233034982312282941404979120374199101029530721743803416729943995574478236819674739711277356996202290244946644459578738103239706195951320306069882976350930385875766006835119530003872691191100813171246012268038223178404972645862310234582063758185409261151998820863241203857153925473260681737790585007671631190093780434840165282447204041489130739003310770512618936242764210545082805105690922522858384377951850258123790199062994055891175715949561715452446644123176972069224869406220559590609955767477584606546737189138565891287162612092210043926895244799647)

# 2424957014399411631 #Cat msg encrypted 110001111000011110100 using 32 bit key
def RSA(option):
    print("RSA")
    global pub
    global priv
    if option == 1:
        p = option1()
        while p == 2:
            p = option1()
        q = option1()
        while q == 2 or q == p:
            if q == p:
                print("Duplicate prime, trying again...")
            q = option1()
        n = p * q
        print("\nPrime p:\t"+str(p))
        print("\nPrime q:\t"+str(q))
        print("\nn:\t"+str(n))
        phiN = (p-1)*(q-1)
        # phiN = phi(n)
        print("\nphi(n) = "+str(phiN))
 
        e = random.randrange(3,p-2)
        while iterative_gcd(phiN,e) != 1:
            # e = rand.randint(3,totient(phiN))
            e = random.randrange(3,p-2)
        print("\ne:\t"+str(e))
        CRT = gcdExtended(phiN,e)
        # print(CRT)
        d = CRT[2] % phiN
        print("\nd:\t"+str(d))
        pub = (n,e)
        priv = (n,d)
    elif option == 2:
        # pub = int(input("Enter a public key: "))
        msg = input("Enter the plaintext message: ")
        asciiMsg = ""
        blocking = []
        binary = ''
        blockNums = []
        if len(msg) > 214:
            for i in range(0,len(msg),214):
                bLet = ''
                # Adding the 1 led to issues when encoding using other's keys since they encoded a different way leading to different decryptions
                # binary = '1' # Adding 1 to start the binary string prevents loss of leading 0's if the char's binary is less than 8 bits
                binary = ''
                for x in msg[i:i+214]:
                    bLet = format(ord(x),'b')
                    newBin = "00000000"
                    bLet = newBin[:8-len(bLet)] + bLet
                    # print(bLet)
                    binary += bLet
                # binary = ''.join(format(ord(x), 'b') for x in msg[i:i+213])
                blocking.append(binary)
                # asciiMsg.append(str(ord(msg[i])))
                # asciiMsg += str(ord(msg[i]))
        # print("Ascii Msg: "+ asciiMsg)
        # binaryMsg = toBinary(msg)
        # print("Binary Msg: "+str(binaryMsg))
            print("Blocked Binary: "+str(blocking))
            for x in range(len(blocking)):
                blockNums.append(int(blocking[x],2))
                print("Block {}: Unencrypted Msg Number: {}".format(x,blockNums[x]))
        else:
            bLet = ''
            # Adding the 1 led to issues when encoding using other's keys since they encoded a different way leading to different decryptions
            # binary = '1' # Adding 1 to start the binary string prevents loss of leading 0's if the char's binary is less than 8 bits
            binary = ''
            for x in msg:
                bLet = format(ord(x),'b')
                newBin = "00000000"
                bLet = newBin[:8-len(bLet)] + bLet
                # print(bLet)
                binary += bLet
            # binary = ''.join(format(ord(x), 'b') for x in msg)
            print("Binary Msg: "+str(binary))
            msgNum = int(binary,2)
            print("Unencrypted Msg Number: "+str(msgNum))
        # n = pub[0]
        n = int(input("Enter the n of your public key: "))
        # e = pub[1]
        e = int(input("Enter the e of your public key: "))

        print("\nn:\t"+str(n))
        print("\ne:\t"+str(e))
        if len(blockNums) == 0:
            print("Encoded Msg: "+str(exp_mod(msgNum,e,n)))
        else:
            outMsg = ""
            for i in blockNums:
                outMsg += str(exp_mod(i,e,n)) + "|"
            print("Encoded Blocked Msg: "+str(outMsg))
    elif option == 3:
        # priv = int(input("Enter a private key: "))
        cipher = input("Enter a block of the ciphertext message: ")
        blockMsg = ""
        msgList = []
        for i in cipher:
            if i != "|":
                blockMsg += i
            else:
                msgList.append(blockMsg)
                blockMsg = ""
        if len(msgList) == 0:
            msgList.append(blockMsg)
            blockMsg = ""
        print(msgList)
        n = priv[0]
        # n = int(input("Enter the n of your private key: "))
        d = priv[1]
        # d = int(input("Enter the d of your private key: "))
        print("\nn:\t"+str(n))
        print("\nd:\t"+str(d))
        index = 1
        out = ""
        blocks = ""
        for i in msgList:
            msg = int(i)
            # print("Encrypted int for block {}: {}".format(index,msg))
            decInt = exp_mod(msg,d,n)
            decBin = format(decInt,'b')
            print("Decrypted Int for block {}: {}".format(index,decInt))
            print("Decrypted Binary: "+ str(decBin))
            # Without the leading 1 I have to now assume the first char will always be the first 7 bits in order to decode the messages sent to me. 
            # If there is a msg encrypted without the leading 1 and a char starts the binary with less than 7 bits it will mess up the decryption process
            out += chr(int(decBin[:7],2)) # "" 
            # out = ""
            for i in range(7,len(decBin),8):
            # for i in range(len(decBin),8,-8):
            # When I was adding a 1 to prevent loss of leading 0's I would start then skip the first bit which was that 1 and then count every 8 bits 
            # for i in range(1,len(decBin),8): 
                out += chr(int(decBin[i:i+8],2))
                # out = chr(int(decBin[i-8:i],2)) + out
                # print(decBin[i-8:i])
                # print(int(decBin[i:i+8],2))
                # print(chr(int(decBin[i:i+8],2)))
                # print(decBin[i:i+8])
            # print("Plaintext for your block {}: {}".format(index,out))
            # blocks += out
            index += 1
        print("Plaintext: "+str(out))
iterCount = 0
def nBitRandom(n):
    # return random.randrange(2**(n-1)+1, 2**n - 1)
    # return int(random.uniform(2**(n-1)+1, 2**n - 1))
    p = random.getrandbits(n)
    p |= (1 << n - 1) | 1
    return p
# nums = []
def option1():
    global iterCount
    count = 0
    # bits = 32
    bits = 1024
    n = nBitRandom(bits)
    
    while n % 5 == 0 or n % 3 == 0 or n % 7 == 0:
        n = nBitRandom(bits)
    iterCount += 1
    # print(n)
    e = (n-1)//2
    vals = []
    k = 20
    for i in range(k):
        b = random.randrange(2,nBitRandom(512))
        # print(b)
        g = iterative_gcd(b,n)
        # print(g)
        if(g == 1):
            exp = exp_mod(b,e,n)
            # jac = jacobi(b,n)
            jac = it_jac(b,n)
            vals.append(b)
            # print("\tExp Mod: "+str(exp))
            # print("\tJacobi: "+str(jac))
            if jac == 0 or exp != jac % n:
                count += 1
        else:
            count += 1
    
    if count == 0:
        print("Prime: "+str(n))
        # pub = n
        print("\tValues tested for {}: \n\t{}".format(n,vals))
        print("\tAttempts to generate prime number: "+str(iterCount))
        numerator = bits*math.log(2)-2
        denominator = bits*math.log(2)-2+2**(k+1)
        print("\tProbability of the number being prime: "+str(numerator/denominator))
        iterCount = 0
        # return n
        # private()
    else:
        return 2
    return n



if __name__ == "__main__":
    option = int(input("Enter an option number: "))
    # option = 3
    sys.setrecursionlimit(1500)
    RSA(option)


    