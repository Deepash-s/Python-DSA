arr = [1,2,1,3,5]
n = len(arr)
hash_arr = [0]*n

for num in arr:
    hash_arr[num-1] += 1
    
print([1, 2, 3, 4, 5])
print(hash_arr)