"""
Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
steps at a time. Implement a method to count how many possible ways the child can run up the
stairs.

"""


def countWays(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return countWays(n-1)+countWays(n-2)+countWays(n-3)


print(countWays(8))


"""

Recursive Multiply: Write a recursive function to multiply two positive integers without using
the * operator (or / operator). You can use addition, subtraction, and bit shifting, but you should
minimize the number of those operations.


"""


def min_product(a, b):
    bigger = a if a > b else b
    smaller = b if a > b else a
    return min_product_helper(smaller, bigger)


def min_product_helper(smaller, bigger):
    if smaller == 0:
        return 0
    elif smaller == 1:
        return bigger

    s = smaller >> 1
    half_prod = min_product_helper(s, bigger)
    if smaller % 2 == 0:
        return half_prod + half_prod
    else:
        return half_prod + half_prod + bigger


print(min_product(7, 8))


