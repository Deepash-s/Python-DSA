def matrixPattern(n):
    size = n*2-1
    matrix = [[0]*size for i in range(size)]
    
    for i in range(size):
        for j in range(size):
            matrix[i][j] = n - min(i, j, size-i-1, size-j-1)
        
    for row in matrix:
        print(''.join(map(str,row)))
    
    
    
matrixPattern(4)