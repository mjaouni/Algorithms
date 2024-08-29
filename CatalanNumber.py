import math


def bracket_combinations(num):
    # Calculate the Catalan number using the formula

    if num == 0:
        return 1  # There is 1 way to arrange 0 pairs of parentheses (an empty string)

    # Catalan number formula: C(n) = (2n)! / ((n+1)!*n!)
    catalan_number = math.comb(2 * num, num) // (num + 1)
    return catalan_number


# Usage
print(bracket_combinations(3))  # Output should be 5
