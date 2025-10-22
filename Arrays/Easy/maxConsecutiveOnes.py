arr = [1, 1, 1, 1, 0, 1, 1, 1]
arr1 = [1, 0, 1, 1, 0, 1]

count = 0
result = 0

for i in range(len(arr)):
    if arr[i] == 1:
        count += 1
        result = max(result, count)
    else:
        count = 0
        
        
print(result)