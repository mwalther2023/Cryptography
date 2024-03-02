            
def CRT(r1,m1,r2,m2):
    g, x, y = gcdExtended(m1, m2)
    n1 = x*m1*r2
    n2 = y*m2*r1
    print("CRT: "+str((n1+n2)%(m1*m2)))

def gcdExtended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcdExtended(b % a, a)
    x = y1 - (b//a) * x1
    y = x1
    return gcd, x, y

def order(n, m):
    list = []
    for i in range(m):
        c = n
        for j in range(i):
            c *= n
        list.append(c%m)
        if c%m == 1:
            break
    print(list)
    print(len(list))
    # for i in list:
    #     print(2**i)
if __name__ == "__main__":
    # r1 = int(input("Enter a remainder: "))
    # m1 = int(input("Enter a mod: "))
    # r2 = float(input("Enter a remainder: "))
    # m2 = int(input("Enter a mod: "))
    # CRT(r1,m1,r2,m2)
    order(2,83)
    order(2,96989)
    # print(gcdExtended(20128,513))
    # print(gcdExtended(20128,15969))
    # print(gcdExtended(4793,4792))
    # print(gcdExtended(12,5))
    