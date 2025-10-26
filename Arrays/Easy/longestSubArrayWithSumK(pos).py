#brute

arr = [1, 2, 3, 1, 1, 1, 1, 4, 2, 3]
n = len(arr)
k = 3
length = 0

for i in range(n):
    for j in range(i, n):
        sums = 0
        for t in range(i, j+1):
            sums += arr[t]
    
        if sums == k:
            length = max(length, j-i+1)
        
print(length)