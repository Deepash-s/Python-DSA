#optimal

arr = [2, 2, 1, 1, 1, 2, 2]
n = len(arr)
count = 0

for i in range(n):
    if count == 0:
        count = 1               
        element = arr[i]
    elif element == arr[i]:
        count += 1
    else:
        count -= 1
        
countN = 0   
for i in range(n):
    if arr[i] == element:
        countN += 1
        
if countN > n//2:
    print(element)
else:
    print("Not Found")