import math

def fibonacci(x):
    if x == 1:
        return 0
    elif x==2:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)

def is_prime(x):
    n = 2
    while n < math.sqrt(x):
        if x < 2:
            return False
        elif x % n == 0:
            return False
        else:
            n += 1


def print_prime_factors(x):
    n = 1
    parameter = 1
    while n != x:
        try:
            if x % n == 0:
                return parameter * n
            else:
                return x * 1
        except ValueError:
            return False
        n += 1