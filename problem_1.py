"""Find the sum of all the multiples of 3 or 5 below 1000."""
# sum of numbers from 1 to x is x * (x + 1) / 2


def sum_of_multiples(n, target):
    count = target // n
    return n * (count * (count + 1)) // 2


if __name__ == '__main__':
    x = (sum_of_multiples(5, 999))
    y = (sum_of_multiples(3, 999))
    z = (sum_of_multiples(15, 999))
    print(x + y - z)

