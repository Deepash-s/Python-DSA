def symmetry(n):
    for i in range(n,0,-1):
        for j in range(i):
            print('*',end='')
        for j in range((n-i)*2):
            print('',end=' ')
        for j in range(i):
            print('*',end='')
        print()
    for i in range(1,n+1):
        for j in range(i):
            print('*',end='')
        for j in range((n-i)*2):
            print('',end=' ')
        for j in range(i):
            print('*',end='')
        print()
            
            
symmetry(5)