""""2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.
What is the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20?"""


# This function returns the smallest number that is divisible to
# 1 to num
def find_smallest_divisible(num):
    multi_list = []
    result_dict = {}
    result = 1
    multi_list.extend(range(2, num + 1))
    for num in multi_list:
        prime_list = find_prime_factors(num)
        for prime in prime_list:
            if not (prime in result_dict):
                result_dict[prime] = 0
            if result_dict[prime] < prime_list.count(prime):
                result_dict[prime] += 1
                result *= prime
    return result

# This functions returns the prime factors of num
def find_prime_factors(num):
    temp = num
    result = []
    while temp > 1:
        for number in range(2, temp + 1):
            if temp % number == 0:
                result.append(number)
                temp //= number
                break
    return result

if __name__ == '__main__':
    print(find_smallest_divisible(20))
