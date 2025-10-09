arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
k = 3
k = k % n
temp = []

for i in range(k):
    temp.append(arr[i])
    
for i in range(k, n):
    arr[i-k] = arr[i]

for i in range(n-k, n):
    arr[i] = temp[i-(n-k)]
        
print(arr)