#brute

arr1 = [1, 1, 2, 4, 5]
arr2 = [2, 3, 4, 4, 6]

freq = {}
union = []

def sortedUnion(arr1, arr2):
    for num in arr1:
        freq[num] = freq.get(num, 0) + 1 
        
    for num in arr2:
        freq[num] = freq.get(num, 0) + 1
        
    for num in freq:
        union.append(num)
        
    print(sorted(union))
        

sortedUnion(arr1, arr2)