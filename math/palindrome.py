def palindrome(n):
    revNum = 0
    dup = n
    while(n>0):
        ld = n%10
        revNum = (revNum*10) + ld
        n //= 10
        
    if(dup == revNum):
        print(f'{dup} is PALINDROME')
    else:
        print(f'{dup} is not a PALINDROME')
        
    
palindrome(121)