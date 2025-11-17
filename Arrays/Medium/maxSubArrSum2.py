#brute

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(arr)

def maximumSubArrSum(arr, n):
    ansStart = -1
    ansEnd = -1
    maximum = arr[0]
    sums = 0
    start = 0
    
    for i in range(n):
        if sums == 0:
            start = i
        sums += arr[i]
        
        if sums > maximum:
            maximum = sums
            ansStart = start
            ansEnd = i
        
        if sums < 0:
            sums = 0 
            
            
    return maximum, ansStart, ansEnd

maximum, ansStart, ansEnd = maximumSubArrSum(arr, n)
print(arr[ansStart:ansEnd+1])
