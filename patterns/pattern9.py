def printPyramid(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print('',end=' ')
        for j in range(i*2-1):
            print('*',end='')
        print()
    for i in range(n,0,-1):
        for j in range(n-i):
            print('',end=' ')
        for j in range(i*2-1):
            print('*', end='')
        print()
        
        
printPyramid(5)