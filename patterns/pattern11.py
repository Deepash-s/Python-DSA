def rightMatrix(n):
    start = 1
    for i in range(n):
        if (i%2 == 0):
            start = 1
        else:
            start = 0
        for j in range(i+1):
            print(start, end=' ')
            start = 1 - start
            
        print()
        
        
rightMatrix(5)