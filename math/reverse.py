def reverse(n):
    revNum = 0
    while(n>0):
        ld = n%10
        revNum = (revNum*10) + ld
        n //= 10
    print(revNum)
    
    
reverse(237)