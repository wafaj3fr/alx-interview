#!/usr/bin/python3
""" Making changes """


def makeChange(coins, total):
    """ Generate changes needed to meet a given amount total

    Args:
        coins ([List]): [List of the values of the coins in your possession.]
        total ([int]): [total amount to be met]
    """
    if total <= 0:
        return 0
    check = 0
    temp = 0
    coins.sort(reverse=True)
    for coin in coins:
        while check < total:
            check += coin
            temp += 1
        if check == total:
            return temp
        check -= coin
        temp -= 1
    return -1
