#brute 

arr = [2, 2, 1, 1, 1, 2, 2]
n = len(arr)

for i in range(n):
    cnt = 0
    for j in range(n):
        if arr[j] == arr[i]:
            cnt += 1

    if cnt > (n // 2):
        print(arr[i])
        break