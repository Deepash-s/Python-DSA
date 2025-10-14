#optimal

arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
n = len(arr)

j = -1

for i in range(n):
    if arr[i] == 0:
        j = i
        break
    
if j == -1:
    print(arr)
    
for i in range(j+1, n):
    if arr[i] != 0:
        arr[i], arr[j] = arr[j], arr[i]
        j += 1
        
print(arr)