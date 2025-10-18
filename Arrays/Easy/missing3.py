#optimal 1

n = 5
arr = [1, 2, 4, 5]

total_sum = n*(n+1)//2
arr_sum = 0

for i in range(n-1):
    arr_sum += arr[i]
    
print(total_sum - arr_sum)