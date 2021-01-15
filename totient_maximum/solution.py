"""
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.

n	Relatively Prime	φ(n)	n/φ(n)
2	1	1	2
3	1,2	2	1.5
4	1,3	2	2
5	1,2,3,4	4	1.25
6	1,5	2	3
7	1,2,3,4,5,6	6	1.1666...
8	1,3,5,7	4	2
9	1,2,4,5,7,8	6	1.5
10	1,3,7,9	4	2.5
It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

Version Performance
limit = 10000
relative:       14 secs
cache:          7 secs
phi limit:      4 secs
check prime-1:  2.6 secs
"""

from math import gcd
from util import timer


@timer
def totient_maximum(limit):
    """ check num after prime """

    t_max = (2, 2)
    for n in range(3, limit+1):
        phi = 0
        phi_lim = n/t_max[1]
        breakflag = 0

        if prime(n-1):
            for j in range(1, n):
                if relative(n, j):
                    phi += 1
                    if phi >= phi_lim:
                        breakflag = 1
                        break
            if not breakflag:
                t_max = (n, n/phi)
        # print(n, phi, phi_lim, breakflag)
                # rel.append(j)
        # for r in rel:
        #     mn = n * r
        #     cache[mn] = phi * cache[r]
        # t_max = max(t_max, (n, n/phi), key=lambda i: i[1])

    return t_max[0]


def relative(num, n):
    if gcd(num, n) == 1:
        return True
    else:
        return False


def prime(num):
    if num <= 3:
        return True
    for i in range(4, num):
        if (num % i) == 0:
            return False
        else:
            return True


limit = 10000
print(totient_maximum(limit))


# deprecated versions
# @timer
# def totient_maximum(limit):
#     """ phi(m * n) = phi(m) * phi(n) if gcd(m, n) == 1 """
#
#     t_max = (0, 0)
#     cache = {1: 1}
#     for n in range(2, limit+1):
#         phi = 0
#         rel = []
#         if n in cache.keys():
#             phi = cache[n]
#         else:
#             for j in range(1, n):
#                 if relative(n, j):
#                     phi += 1
#                     rel.append(j)
#         for r in rel:
#             mn = n * r
#             cache[mn] = phi * cache[r]
#         t_max = max(t_max, (n, n/phi), key=lambda i: i[1])
#     return t_max[0]
#
#
# def relative(num, n):
#     if gcd(num, n) == 1:
#         return True
#     else:
#         return False
