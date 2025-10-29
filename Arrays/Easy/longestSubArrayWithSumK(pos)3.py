arr = [1, 2, 3, 1, 1, 1, 1, 3, 3]
n = len(arr)
k = 6
left = 0
curr_sum = 0
maxLen = 0

for right in range(n):
    curr_sum += arr[right]

    while curr_sum > k:
        curr_sum -= arr[left]
        left += 1

    if curr_sum == k:
        maxLen = max(maxLen, right - left + 1)
        
        
print(maxLen)        