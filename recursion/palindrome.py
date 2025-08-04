s = input('Enter a string: ')
n = len(s)

def palindrome(left, right):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return palindrome(left + 1, right - 1)

if palindrome(0, n - 1):
    print(f'{s} is a palindrome')
else:
    print(f'{s} is not a palindrome')
