#!/usr/bin/python3
"""
Lockboxes problem solved
"""

def canUnlockAll(boxes):
    """
    a method that determines if all the boxes can be opened.
    """
    if type(boxes) is not list:
        return False
    elif (len(boxes)) == 0:
        return False
    for j in range(1, len(boxes) - 1):
        checked = False
        for i in range(len(boxes)):
            checked = j in boxes[i] and j != i
            if checked:
                break
        if checked is False:
            return checked
    return True
