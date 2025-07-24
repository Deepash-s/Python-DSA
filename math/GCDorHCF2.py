def GCD(m, n):
    while n>0:
        m, n = n , m%n
    print(m)
    
    
GCD(9, 12)

#optimal approach: time complexity -> O(log(min(m,n)))