#!/usr/bin/python3
""" Change comes from within.
"""


def makeChange(coins, total):
    """ Given a pile of coins of different values, determine the fewest
    number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0
    noc = 0
    coins.sort(reverse=True)
    for i in coins:
        q = total / i
        noc += q
        total %= i

    if total > 0:
        return -1
    return int(noc)
