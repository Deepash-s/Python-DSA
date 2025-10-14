#brute

arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
n = len(arr)
temp = []

for i in range(n):
    if arr[i] != 0:
        temp.append(arr[i])
        
nz = len(temp)
    
for i in range(nz):
    arr[i] = temp[i]
    
for i in range(nz, n):
    arr[i] = 0
    
print(arr)