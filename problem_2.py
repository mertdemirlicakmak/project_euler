"""By considering the terms in the Fibonacci sequence whose values
do not exceed four million, find the sum of the even-valued terms.
1 1 2 3 5 8 13 21 34 55 89 144 ... (every third number is even)
"""


def fibonacci_even_sum(range_):
    first = 1
    second = 2
    total = 0
    fibonacci = []
    fibonacci.append(first)
    fibonacci.append(second)
    for i in range(1, range_ - 1):
        fibonacci.append(fibonacci[i-1] + fibonacci[i])
        if fibonacci[i] > range_:
            break
        if (i + 2) % 3 == 0:
            total += fibonacci[i]
    return total


if __name__ == '__main__':
    print(fibonacci_even_sum(4000000))

