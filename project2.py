import math
import numpy as np
factors = []
def jacobi(a,n):
    if a == 0:
        return 0
    if a == 1:
        return 1
    if a == 2:
        m = n%8
        if m == 3 or m == 5:
            return -1
        else:
            return 1
    if a%2 == 0:
        return jacobi(2,n) * jacobi(a//2,n)
    if a >= n:
        return jacobi(a%n,n)
    if a%4 == 3 and n%4 == 3:
        return -jacobi(n,a)
    else:
        return jacobi(n,a)
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
    # print(factors)
    phi = m
    for i in factors:
        phi *= (1-1/i)
    # print("Phi: "+str(int(phi)))
    # print(str(b)+"^"+str(int(e%int(phi)))+" mod "+str(m))

    i = 2
    num = b
    power = [b]
    while i < int(phi):
        # print(i)
        num *= num
        num = num%m
        power.append(num)
        i *= 2
    # print(power)
    powerList  = []
    ePhi = e%int(phi)
    i = 1
    while ePhi > 0 and len(power)-i >= 0:
        temp = ePhi - np.power(2,len(power)-i)
        if temp >= 0:
            ePhi -= np.power(2,len(power)-i)
            powerList.append(len(power)-i)
        i += 1
    # print(powerList)
    ans = 1
    for i in powerList:
        ans *= power[i]

    # print("Exp Mod: "+str(ans % m))
    return ans % m
def gcd(n: int,m: int)->int:
    if n < m:
        gcd(m,n)
    #Base Case: Check if im done
    if n % m == 0:
        return m
    #Recursively call gcd() using reduction theorem
    else:
        return gcd(m,n%m)
if __name__ == "__main__":
    # n = int(input("Enter an odd number to test its compositeness: "))
    n = 221
    # b = np.random.randint(1,m)
    # b = 47
    b = 2
    e = (n-1)/2
    Zstarn = []
    for i in range(1,n):
        if gcd(n,i) == 1:
            Zstarn.append(i)
    print("Phi(n): "+str(len(Zstarn)))
    # print(Zstarn)

    # exp_mod(b,e,m)
    # print("Exp Mod: "+str(exp_mod(b,e,n)))
    # print("Jacobi: "+str(jacobi(b,n)))
    count = 0
    for i in Zstarn:
        # print(i)
        exp = exp_mod(i,e,n)
        jac = jacobi(i,n)
        # print("\tExp Mod: "+str(exp))
        # print("\tJacobi: "+str(jac))

        if jac == 0 or exp != jac % n:
            count += 1
            # print("\t\t"+str(count))

    print("Eulers Witnesses: "+str(count))