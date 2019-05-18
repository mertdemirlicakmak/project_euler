"""Find the largest palindrome made from 
the product of two 3-digit numbers."""


def palindrome_finder(digit_number):
    range_max = pow(10, digit_number) - 1
    range_min = pow(10, digit_number - 1)
    palindrome_found = False
    palindromes = []
    for i in range(range_max, range_min, -1):
        for j in range(range_max, range_min, -1):
            temp_result = i * j
            length = len(str(temp_result))
            for k, digit in enumerate(str(temp_result)):
                if str(temp_result)[length - k - 1] != digit:
                    palindrome_found = False
                    break
                else:
                    palindrome_found = True
            if palindrome_found:
                print(i, j)
                palindromes.append(temp_result)
                break
    return max(palindromes)


if __name__ == '__main__':
    print(palindrome_finder(3))

