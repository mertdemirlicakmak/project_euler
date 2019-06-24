"""There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""

# a^2 + b^2 + c^2 + 2(ab + ac + bc) = 1000000
# a^2 + b^2 = c^2 => c^2 + ab + ac + bc = 500000

# TODO: implement a better algorithm
def find_pythagorean(n):
    for c in range(1, n):
        for a in range(c):
            for b in range(c):
                if pow(a, 2) + pow(b, 2) == pow(c, 2) and a + b + c == n:
                    return a * b * c


print(find_pythagorean(1000))
