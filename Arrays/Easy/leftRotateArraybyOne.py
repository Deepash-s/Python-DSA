#brute force

arr = [1, 2, 3, 4, 5]
n = len(arr)
temp = [0] * n

for i in range(1, n):
    temp[i - 1] = arr[i]
temp[n - 1] = arr[0] 

print(temp)