#brute

n = 5
arr = [1, 2, 3, 4]

for i in range(1, n+1):
    flag = 0
    for j in range(len(arr)):
        if arr[j] == i:
            flag = 1
            break
    if flag == 0:
        print(i) 
        break
        
