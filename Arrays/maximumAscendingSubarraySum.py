arr1 = [10, 20, 30, 5, 10, 50]
arr = [12,17,15,13,10,11,12]

currentSum = arr[0]
result = arr[0]

for i in range(1, len(arr)):
    if arr[i]>arr[i-1]:
        currentSum += arr[i]
    else:
        currentSum = arr[i]
    result = max(result, currentSum)


print(result)