# Coin Change Problem

## Description

This project tackles the classic coin change problem using dynamic programming. The objective is to find the fewest number of coins needed to meet a given total amount, given a list of coin denominations.

## Prototype

```python
def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Parameters:
    coins (list): A list of the values of the coins in your possession.
    total (int): The total amount to be met.

    Returns:
    int: The fewest number of coins needed to meet the total.
         If the total is 0 or less, return 0.
         If the total cannot be met by any number of coins, return -1.
    """
