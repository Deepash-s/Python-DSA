n = int(input(f'Enter the array size: '))
arr = []
for i in range(n):
    arr.append(int(input(f'Enter element {i}:')))
print(f'Array before: {arr}')

def reverseArray(start, arr, end):
    if start >= end :
        print(f'Reverse array: {arr}')
        return
    arr[start], arr[end] = arr[end],  arr[start]
    reverseArray(start+1, arr, end-1)\
        

reverseArray(0, arr, n-1)