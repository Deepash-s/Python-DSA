n = int(input('Enter Array size: '))
arr = []
max_element = 0

for i in range(n):
    element = int(input(f'Enter element {i}: '))
    arr.append(element)
    max_element = max(max_element, element)
    
hash_array = [0] * (max_element+1)

for num in arr:
    hash_array[num] += 1
   
   
q = int(input('Enter the number of elements you want to find frequency: ')) 
for j in range(q):
    number  = int(input('Enter number: '))
    if number < len(hash_array):
        print(hash_array[number])
    else:
        print(0)