arr = [1, 1, 2, 3, 3, 4, 4]

n = len(arr)

hash_map = {}
for num in arr:
    hash_map[num] = hash_map.get(num, 0) + 1
    
for num, count in hash_map.items():
    if count == 1:
        print(num)
        break