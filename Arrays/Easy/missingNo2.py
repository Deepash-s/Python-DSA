n = 5
arr = [1, 2, 4, 5]

hash = [0] * (n+1)

for i in range(n-1):
    hash[arr[i]] += 1
    
print(hash)
    
    
for i in range(1, n+1):
    if hash[i] == 0:
        print(i)
        break