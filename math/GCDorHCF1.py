def GCD(m, n):
    factors1 = [i for i in range(1,n+1) if n%i==0]
    factors2 = [i for i in range(1,m+1) if m%i==0]
    uniques = list(set(factors1) & set(factors2))
    print(max(uniques))
    
    
GCD(20, 15)

#brute force approach: time complexity -> 0(m+n)