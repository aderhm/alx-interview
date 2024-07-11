#!/usr/bin/python3
"""Module: Minimum Operations"""


def minOperations(n):
    """Calculates the fewest number of operations needed to
       result in exactly n H characters in the file.
    """
    if n == 1:
        return 0

    operations = 0
    prime_factor = 2
    while n > 1:
        if n % prime_factor == 0:
            operations += prime_factor
            n //= prime_factor
        else:
            prime_factor += 1
    return operations
