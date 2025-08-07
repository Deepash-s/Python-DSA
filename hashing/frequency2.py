def frequency(n, x):
    arr = []
    mp = {}
    for i in range(n):
        num = int(input('Enter element: '))
        arr.append(num)
        mp[num] = mp.get(num, 0) + 1
        
    print(f'Frequency of {x}: {mp.get(x, 0)}')
    

frequency(5, 2)