#return duplicates in same order as they appeared

arr = [3, 2, 3, 1, 4, 1]
seen = set()
unique = []

for i in range(len(arr)):
    if arr[i] not in seen:
        unique.append(arr[i])
        seen.add(arr[i])
        
        
print(unique)