arr = [3, 2, 1, 5, 2, 7]
target = 5

def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            print(f'Target found at index: {i}.')
            break
        
    else:
        print('Target not found')
        

linearSearch(arr, target)