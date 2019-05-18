"""What is the largest prime factor of the number 600851475143 ?"""


def largest_prime(num):
    prime = 2
    for i in range(2, num):
        if num % i == 0:
            prime = num
            num //= i
            if num == 1:
                break
    return prime


if __name__ == '__main__':
    print(largest_prime(600851475143))

