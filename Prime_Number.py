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
