def factorial(n ,result=1):
    if n==0 or n==1:
        print(result)
        return
    factorial(n-1, result*n)
    
    
factorial(5)