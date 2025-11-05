#better

arr = [2, 2, 1, 1, 1, 2, 2]
n = len(arr)
hash_map = {}

for num in arr:
    if num in hash_map:
        hash_map[num] += 1
        if hash_map[num] > n//2:
            print(num)
            break
    else:
        hash_map[num] = 1