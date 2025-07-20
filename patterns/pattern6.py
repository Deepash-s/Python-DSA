def printTriangle(n):
        num = 1
        for i in range(n,0,-1):
            for j in range(i):
                print(num, end=' ')
                num += 1
            num = 1
            print()


printTriangle(5)