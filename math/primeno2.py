import math

def prime(n):
    count = 0
    for i in range(1, int(math.sqrt(n))+1):
        if n%i == 0:
            count += 1
            
            if i!=n//i:
                count += 1
    
    if (count == 2):
        print(f'{n} is prime')
    else:
        print(f'{n} is not prime')
        

prime(13)