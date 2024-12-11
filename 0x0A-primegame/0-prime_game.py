#!/usr/bin/python3

def isWinner(x, nums):
    """
    Determine the winner of each round of the prime game.

    :param x: Number of rounds
    :param nums: List of n values for each round
    :return: Name of the player with the most wins, or None for a tie
    """
    if not nums or x < 1:
        return None

    max_n = max(nums)
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False

    # Sieve of Eratosthenes to find all prime numbers up to max_n
    for i in range(2, int(max_n ** 0.5) + 1):
        if primes[i]:
            for multiple in range(i * i, max_n + 1, i):
                primes[multiple] = False

    # Precompute the number of primes up to each index
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0

    # Determine the winner for each round
    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

