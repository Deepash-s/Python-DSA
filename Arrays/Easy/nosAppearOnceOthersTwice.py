arr = [1, 1, 2, 3, 3, 4, 4]

for i in range(len(arr)):
    num = arr[i]
    count = 0
    for j in range(len(arr)):
        if num == arr[j]:
            count += 1
    
    if count == 1:
        print(num)
        break