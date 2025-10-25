arr = [1, 1, 2, 3, 3, 4, 4]
largest = max(arr)
hash_arr = [0]*(largest+1)


for i in range(len(arr)):
    hash_arr[arr[i]] += 1
    
for num in hash_arr:
    if num == 1:
        print(hash_arr.index(num))
        break