#optimal 4

n = 5
arr = [1, 2, 4, 5]

xor1,xor2 = 0, 0

for i in range(n-1):
    xor1 = xor1 ^ (i+1)
    xor2 = xor2 ^ arr[i]
    
    
xor1 = xor1^n
print(xor1^xor2)