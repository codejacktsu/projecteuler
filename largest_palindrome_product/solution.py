"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from util import timer


@timer
def largest_palindrome_product(n):
    """ largest palindrome of product of 2 x n-digit numbers
    :param n: num of digit"""

    a = int("9"*n)
    lst = []

    for i in range(1, a+1):
        for j in range(1, a+1):
            product = i * j

            palin = str(product)
            palin_rev = palin[::-1]

            if palin_rev == palin:
                lst.append(product)

    return max(lst)


n = 3
print(largest_palindrome_product(n))
