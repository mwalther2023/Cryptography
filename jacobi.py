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
if __name__ == '__main__':
    print(jacobi(8,21))
    print(jacobi(342,113))