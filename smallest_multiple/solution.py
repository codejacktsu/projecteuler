"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from util import timer


@timer
def smallest_multiple():
    d = list(range(1,21))
    check = 20
    while True:
        for num in d:
            if check % num != 0:
                check += 1
                break
            if num == 20:
                return check


print(smallest_multiple())
