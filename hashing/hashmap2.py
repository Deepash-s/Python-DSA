s = input('Enter a string: ')
mp = {}

for i in range(len(s)):
    mp[s[i]] = mp.get(s[i], 0) + 1
    

q = int(input('Enter number of queries: '))
for j in range(q):
    letter = input('Enter letter to find frequency: ')
    print(mp.get(letter, 0))