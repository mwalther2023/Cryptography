def gcd(n: int,m: int)->int:
    return n if m==0 else gcd(m,n%m)
    # #First make sure n > m
    # if n < m:
    #     gcd(m,n)
    # #Base Case: Check if im done
    # if n % m == 0:
    #     return m
    # #Recursively call gcd() using reduction theorem
    # else:
    #     return gcd(m,n%m)
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
    print("GCD: "+str(a))

def inverse_gcd(a,b):
    arr = []
    n = a
    m = b
    while b > 0:
        q = int(a/b)
        r = a%b
        arr.append([r,a, -q, b]) # r = a-q*b
        a = b
        b = r
    arr.pop()
    # for i in range(len(arr)-1,-1,-1):
    #     print(arr[i])
    # inv = [arr[0]]
    inv = [arr[len(arr)-1]]
    # inv = []
    tally = 0
    print("Arr: "+str(arr))
    # for i in range(1,len(arr)):
    index = 0
    for i in range(len(arr)-1,0,-1):
        inv.append([arr[i][0], arr[i][1], arr[i][2], inv[index][1:]])
        index += 1
        print("Append: "+str(inv))
    for i in range(2,len(arr)):
        val = inv[i][1]
        for j in range(i):
            if val == inv[j][0]:
                inv[i][1] = [inv[j][1], inv[j][2], inv[j][3]]
                break
    inv[len(inv)-1][3][0] = [inv[0][1], inv[0][2], inv[0][3]]


    for i in range(len(arr)-1,-1,-1):
        print(inv[i])
    print("---------------------")
    val = []
    for i in range(len(arr)):
        val.append(arr[i][0])
        for j in range(1, len(arr[i])):
            # print(str(val)+" | "+str(arr[i][j]))
            if arr[i][j] in val or arr[i][j] == m:
                tally += 1
                # print("Found m")
    print("Mult Inverse of {} mod {} is {}".format(m,n,tally))

if __name__ == "__main__":
    a = input("Enter a number: ")
    b = input("Enter a number: ")
    inverse_gcd(int(a), int(b))
    # print(gcd(int(a), int(b)))