def divisor(n):
    divisors = []
    for i in range(1, n+1):
        if n%i==0:
            divisors.append(i)
    print(divisors)


divisor(12)

#Brute force approach: Time complexity -> O(n)