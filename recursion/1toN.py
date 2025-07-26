def prints(i, n):
    if(i>n):
        return
    print(i)
    prints(i+1, n)
    
    
prints(1, 5)