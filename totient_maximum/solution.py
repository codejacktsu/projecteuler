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
"""

from math import gcd
from util import timer


@timer
def totient_maximum(limit):
    cache = {}
    t_max = (0, 0)
    for n in range(2, limit+1):
        # find all prime
        phi = 0
        for j in range(1, n):
            if j in cache.keys():
                flag = cache[j]
            else:
                flag = prime(j)
                cache[n] = flag
            if flag and relative(j, n):
                phi += 1
        # print(n, n/phi)
        t_max = max(t_max, (n, n/phi), key=lambda i: i[1])
    return t_max[0]


def prime(num):
    if num == 1 or num == 2:
        return True
    for i in range(2, num):
        if (num % i) == 0:
            return False
        else:
            return True


def relative(num, n):
    if gcd(num, n) == 1:
        return True
    else:
        return False


limit = 1000000
print(totient_maximum(limit))
