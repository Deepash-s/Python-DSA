n = int(input('Enter the size of array: '))
arr = []
for i in range(n):
    arr.append(int(input(f'Enter element {i}: ')))
print(f'Array before: {arr}')

def swap(m, arr, n):
    if(m>=n):
        print(f'Array after: {arr}')
        return
    temp = arr[m]
    arr[m] = arr[n-1]
    arr[n-1] =temp
    swap(m+1, arr, n-1)
    
swap(0, arr, n)

#my solution