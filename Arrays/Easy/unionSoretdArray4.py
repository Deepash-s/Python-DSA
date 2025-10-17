arr1 = [3, 6, 9, 0, 0]
arr2 = [4, 10]
m = 3
n = 2

for i in range(n):
    arr1[m+i] = arr2[i]
    
print(sorted(arr1))