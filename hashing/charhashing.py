s = input('Enter a string: ')
hash = [0] * 26 

for i in range(len(s)):
    hash[ord(s[i]) - ord('a')] += 1;    
    
q = int(input('Enter number of queries: '))
for i in range(q):
    c = input('Enter character to find frequency: ')
    print(hash[ord(c) - ord('a')])