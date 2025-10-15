arr1 = [1, 1, 2, 3, 4, 5]
arr2 = [2, 3, 4, 4, 5, 6]
union = []

i = 0
j = 0
n1 =len(arr1)
n2 = len(arr2)

while i<n1 and j<n2:
    if arr1[i]<arr2[j]:
        if len(union) == 0 or union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1
        
    else:
        if len(union) == 0 or union[-1] !=  arr2[j]:
            union.append(arr2[j])
        j += 1
        
while i<n1:
    if union[-1] != arr1[i]:
        union.append(arr1[i])
    i += 1
        
while j<n2:
    if union[-1] != arr2[j]:
        union.append(arr2[j])
    j += 1
    
print(union)