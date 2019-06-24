"""Find the sum of all the primes below two million."""

# TODO: implement a faster algorithm

from math import sqrt

def sum_of_primes(bound):
    sum = 5
    for number in range(3, bound + 1, 2):
        if is_prime(number):
            sum += number
    return sum

def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


print(sum_of_primes(2_000_000))

