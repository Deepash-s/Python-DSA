def prints(i ,n):
    if(i<1):
        return
    print(i)
    prints(i-1, n)
    

prints(5, 5)