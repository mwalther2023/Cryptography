            
def modMult(n):
    list = []
    n = int(n)
    header = "   |"
    for i in range(n):
        header += " " +str(i) + " "
    header += "\n---|"
    for i in range(n):
        header += "---"
    header += "\n"
    data = ""
    count = 0
    for i in range(n):
        data += " " + str(i) + " |"
        for j in range(n):
            data += " " +str((i*j)%n) + " "
            if (i*j)%n == 1:
                # print("Inverse: "+str(i)+" and "+str(j))
                count += 1
                list.append(i)
        data += "\n"
    print(count)
    print(header+data)
    print(list)

if __name__ == "__main__":
    n = input("Enter a number: ")
    modMult(n)