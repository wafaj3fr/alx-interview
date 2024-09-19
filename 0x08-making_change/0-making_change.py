#!/usr/bin/python3
"""
Function to determine the fewest number of coins needed to make the given total.
"""

def makeChange(coins, total):
    """
    Args:
    coins (list): A list of integers representing coin denominations.
    total (int): The total amount to achieve using the fewest coins.
    
    Returns:
    int: The fewest number of coins needed to make the total. If it's not possible, return -1.
    """
    if total <= 0:
        return 0
    

    dp = [float('inf')] * (total + 1)
    dp[0] = 0 
    

    for coin in coins:
    
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    
    return dp[total] if dp[total] != float('inf') else -1

