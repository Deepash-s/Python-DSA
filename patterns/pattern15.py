def reverseAlphabetTriangle(n):
    letter = 65
    for i in range(n,0,-1):
        for j in range(i):
            print(chr(letter), end=' ')
            letter += 1
        print()
        letter = 65
        
        
reverseAlphabetTriangle(5)