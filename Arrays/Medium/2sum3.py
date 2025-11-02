#optimal

arr = [2, 6, 5, 8, 11]
target = 14

def twoSum(arr, target):
    n = len(arr)
    arr.sort()
    left = 0
    right = n-1
    while left < right:
        sums = arr[left] + arr[right]
        if sums == target:
            return "YES"
        elif sums < target:
            left += 1
        else:
            right -= 1
            
    return "NO"


print(twoSum(arr, target))



#for returning indexes but not much optimal:

""" def twoSum(arr, target):
    indexed_arr = sorted([(num, i) for i, num in enumerate(arr)])
    left = 0
    right = len(indexed_arr) - 1

    while left < right:
        sums = indexed_arr[left][0] + indexed_arr[right][0]
        if sums == target:
            return indexed_arr[left][1], indexed_arr[right][1]
        elif sums < target:
            left += 1
        else:
            right -= 1

    return -1, -1 """
