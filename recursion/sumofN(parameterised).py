def sumOfN(n, sum):
    if(n<1):
        print(f'sum of: {sum}')
        return
    sumOfN(n-1, sum+n)
    
    
sumOfN(5, 0)