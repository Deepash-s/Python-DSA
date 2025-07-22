def hollow(n):
    for i in range(1,n+1):
        if (i==1 or i==n):
            print('*'*n)
        else:
            print(f'*{' '*(n-2)}*')
        
        
hollow(8)