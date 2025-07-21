def alphaTriangle(n):
    for i in range(n):
        for j in range(n-i-1, n):
            print(chr(65+j), end=' ')
        print()
        

alphaTriangle(5)