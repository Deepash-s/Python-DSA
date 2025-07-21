def alphabetTriangle(n):
    letter = 65
    for i in range(n):
        for j in range(i+1):
            print(chr(letter), end=' ')
            letter += 1
        print()
        letter = 65


alphabetTriangle(5)