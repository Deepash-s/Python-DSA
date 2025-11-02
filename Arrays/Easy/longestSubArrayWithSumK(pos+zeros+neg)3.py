#Better

arr = [1, 2, 0, 0, 0, 3]
arr1 = [1, 2, 3, 1, 1, 1, 1, 4, 2, 3]
n = len(arr)
k = 3
preSumMap = {}
maxLen = 0
sums = 0

for i in range(n):
    sums += arr[i]
    
    if sums == k:
        maxLen = max(maxLen, i+1)
        
    rem = sums - k
    
    if rem in preSumMap:
        length = i - preSumMap[rem]
        maxLen = max(maxLen, length)
        
    if sums not in preSumMap:
        preSumMap[sums] = i


print(maxLen)