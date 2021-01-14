"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from util import timer


@timer
def largest_prime_factor(n):
    for i in range(1, n+1):
        if n % i == 0:
            n /= i
        if n <= i:
            return max(i, n)

print(largest_prime_factor(600851475143))
