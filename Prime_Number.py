import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if  n % i == 0:
            return False
       
    return True
        

result = is_prime(6)
print(result)

def rang_prime_number(n):
    primeList = []
    for i in range(2, n):
        if is_prime(i):
            primeList.append(i)
    return primeList
        

result2 = rang_prime_number(100)
print(result2)
