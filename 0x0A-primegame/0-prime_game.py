#!/usr/bin/python3
""" Prime Game
"""


def isWinner(x, nums):
    """ Maria and Ben are playing a game.
    Given a set of consecutive integers starting from 1 up to and including n,
    they take turns choosing a prime number from the set and removing that
    number and its multiples from the set. The player that cannot make a
    move loses the game.
    """
    if not nums or x < 1:
        return None

    max_num = max(nums)

    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(max_num**0.5) + 1):
        if sieve[i]:
            for multiple in range(i * i, max_num + 1, i):
                sieve[multiple] = False

    prime_counts = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if sieve[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
