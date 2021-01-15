"""
Euler's Totient function, φ(n) [sometimes called the phi function],
is used to determine the number of numbers less than n which are relatively prime to n.
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.

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
check prime-1:  0.6 secs
check prime-1 + prime phi cache + factor:
"""

from math import gcd, sqrt, floor
from functools import reduce
from util import timer


@timer
def totient_maximum(lmt):
    """ check num after prime """

    t_max = (1, 1)
    cache = {0: 0, 1: 1}
    for n in range(2, lmt+1):
        if prime(n):
            # if n = prime, phi = n - 1
            cache[n] = n - 1
            continue
        if prime(n-1):
            phi = 1
            factli = factors(n)[2::]
            while factli:
                # print(factli, n, cache, phi)
                f = factli.pop()
                if prime(f):
                    phi *= cache[f]
                else:
                    factli += factors(f)[2:3]
            t_max = max(t_max, (n, n/phi), key=lambda i: i[1])
    print(cache)
    return t_max[0]


def relative(num, n):
    if gcd(num, n) == 1:
        return True
    else:
        return False


def prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num > 2 and num % 2 == 0:
        return False

    for i in range(3, floor(sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


def factors(num):
    return reduce(list.__add__,
                  ([i, num//i] for i in range(1, int(num**0.5) + 1) if num % i == 0))


def phi_1_to_n(n):
    phi = {0: 0, 1: 1}
    for i in range(2, n + 1):
        phi[i] = i
    for i in range(2, n + 1):
        if phi[i] == i:
            for j in range(i, n + 1, i):
                phi[j] -= phi[j] // i
    return phi


limit = 10000
# print(totient_maximum(limit))
print(phi_1_to_n(limit))

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
