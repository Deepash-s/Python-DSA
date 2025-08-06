n = int(input('Enter array Size: '))
arr = []
mp = {}

for i in range(n):
    num = int(input(f'Enter element {i}: '))
    arr.append(num)
    mp[num] = mp.get(num, 0) + 1
    
q = int(input('Enter number of queries: '))

for j in range(q):
    number = int(input('Enter the number: '))
    print(mp.get(number, 0))