#brute

arr = [2, 6, 5, 8, 11]
target = 14

""" for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == target:
                print("YES")
                break """
   
def twoSum(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i):
            if arr[i] + arr[j] == target:
                return j, i
    return -1, -1
             
print(twoSum(arr, target))