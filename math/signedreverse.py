def signedReverse(n):
    sign = -1 if n<0 else 1
    n = abs(n)
    revNum = 0
    while(n>0):
        ld = n%10
        revNum = (revNum*10) + ld
        n //= 10
        
    revNum *= sign
    if revNum<-2**31 or revNum>2**31:
        return 0
    return revNum


print(signedReverse(-123))        