def GCD(arr):
    gcd = arr[0]
    for num in arr[1:]:
        a, b = gcd, num
        while b>0:
            a, b = b, a%b
        gcd = a
    print(gcd)
    
    
GCD([2,4,6,8])