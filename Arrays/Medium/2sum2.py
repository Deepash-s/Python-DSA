#better

arr = [2, 6, 5, 8, 11]
target = 14

def twoSum(arr, target):
    n = len(arr)
    hash_map = {}
    for i in range(n):
        num = arr[i]
        more = target - num
        if more in hash_map:
            return hash_map[more], i
        hash_map[num] = i
    return -1, -1

print(twoSum(arr, target))