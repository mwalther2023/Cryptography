import math
import numpy as np
factors = []
def primeFactors(n):
    factors.clear()
    while n % 2 == 0:
        if(2 not in factors):
            factors.append(2)
        n = n/2
         
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
            if(i not in factors):
                factors.append(i)
            n = n/i
             
    if n > 2:
        if(n not in factors):
            factors.append(n)
def exp_mod(b,e,m):
    b = b % m
    primeFactors(m)
    print(factors)
    phi = m
    for i in factors:
        phi *= (1-1/i)
    
    print(str(b)+"^"+str(e%int(phi))+" mod "+str(m))
    i = 2
    num = b
    power = [b]
    while i < int(phi):
        # print(i)
        num *= num
        num = num%m
        power.append(num)
        i *= 2
    print(power)
    powerList  = []
    ePhi = e%int(phi)
    i = 1
    while ePhi > 0:
        temp = ePhi - np.power(2,len(power)-i)
        if temp >= 0:
            ePhi -= np.power(2,len(power)-i)
            powerList.append(len(power)-i)
        i += 1
    print(powerList)
    ans = 1
    for i in powerList:
        ans *= power[i]

    print(ans % m)
if __name__ == "__main__":
    b = int(input("Enter the base number: "))
    e = int(input("Enter the exponent: "))
    m = int(input("Enter the mod number: "))
    # b = 983
    # e = 9698
    # m = 98
    exp_mod(b,e,m)
