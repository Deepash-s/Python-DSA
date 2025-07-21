def alphabetTriangle(n):
    letter = 65
    for i in range(n):
        for j in range(i+1):
            print(chr(letter), end=' ')
        print()
        letter += 1
        

alphabetTriangle(5)