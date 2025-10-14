arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
k = 3
k = k % n

arr[:-k] = arr[:-k][::-1]
arr[-k:] = arr[-k:][::-1]
arr[:] = arr[::-1]

print(arr)