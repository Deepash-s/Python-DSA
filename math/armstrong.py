def armstrong(n):
    digit = len(str(n))
    dup = n
    sum = 0
    while(n>0):
        ld = n%10
        sum += ld**digit
        n //= 10
        
    if (sum == dup):
        print(f'{dup} is Armstrong')
    else:
        print(f'{dup} is not an Armstrong')
        
        
armstrong(153)