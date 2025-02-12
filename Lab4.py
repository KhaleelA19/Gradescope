import math

def fibonacci(x):
    if x == 1:
        return 0
    elif x==2:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)

def is_prime(x):
    if x < 2:
        return False
    for n in range(2, int(math.sqrt(x))+1):
        if x % n == 0:
            return False
    return True


def print_prime_factors(x):
    factor_list = []
    divisor = 2
    original = x
    while x > 1:
        while x % divisor == 0:
            factor_list.append(divisor)
            x //= divisor
        divisor += 1

    print(f"{original} =  {'*' .join(map(str, factor_list))} ")
