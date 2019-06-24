"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
 we can see that the 6th prime is 13.

What is the 10 001st prime number?"""

from math import sqrt

def find_prime(n):
    prime_candidate = 2
    counter = 2
    is_prime = False
    while counter <= n:
        prime_candidate += 1
        for i in range(2, sqrt(prime_candidate)):
            if prime_candidate % i == 0:
                is_prime = False
                break
            else:
                is_prime = True
        if is_prime:
            counter += 1
    return prime_candidate


print(find_prime(10001))
