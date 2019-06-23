"""Find the difference between the sum of the squares of the first
one hundred natural numbers and the square of the sum."""


sum_of_squares = 0
for i in range(1, 101):
    sum_of_squares += pow(i, 2)
squares_of_sum = pow(101 * 50, 2)

print(squares_of_sum - sum_of_squares)
