arr1 = [1, 1, 2, 3, 4, 5]
arr2 = [2, 3, 4, 4, 6]

union = []

for num in arr1:
    if num not in union:
        union.append(num)

for num in arr2:
    if num not in union:
        union.append(num)

print(sorted(union))
