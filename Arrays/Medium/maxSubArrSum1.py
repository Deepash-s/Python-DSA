#brute

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(arr)

def maximumSubArrSum(arr, n):
    maximum = arr[0]
    for i in range(n):
        sums = 0
        for j in range(i, n):
            sums += arr[j]
            maximum = max(maximum, sums)
            
    return maximum

print(maximumSubArrSum(arr, n))