def backtrack(i, n):
    if(i<1):
        return
    backtrack(i-1, n)
    print(i)
    
    
backtrack(5, 5)