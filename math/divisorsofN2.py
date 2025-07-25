import math

def divisor(n):
    divisors = []
    sqrtN = int(math.sqrt(n))
    for i in range(1, sqrtN+1):
        if n%i == 0:
            divisors.append(i)
            if(i!=n//i):
                divisors.append(n//i)
                
    print(sorted(divisors))
    
    
divisor(12)

#optimal approach: Time complexity -> O(sqrt(n))