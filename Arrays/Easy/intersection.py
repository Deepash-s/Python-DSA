arr1 = [1, 2, 2, 3, 3, 4, 5, 6]
arr2 = [2, 3, 3, 5, 6, 6, 7]
n1 = len(arr1)
n2 =  len(arr2)
intersection  = []
visited = n2 * [0]

for i in range(n1):
    for j in range(n2):
        if arr1[i] == arr2[j] and visited[j]==0:
            intersection.append(arr1[i])
            visited[j] = 1
            break
        if arr2[j]>arr1[i]:
            break
        
        
print(intersection)