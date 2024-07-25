#!/usr/bin/env python3
from typing import List


def pascal_triangle(n: int) -> List[list]:
    '''
    Pascal triangle
    '''
    if n <= 0:
        return []

    if n == 1:
        return [[1]]

    if n == 2:
        return [[1], [1, 1]]

    pt = [[1], [1, 1]]

    for i in range(2, n):
        temp = [1, 1]
        for j in range(0, len(pt[-1])-1):
            a = pt[-1][j]
            b = pt[-1][j+1]
            temp.insert(-1, a + b)
        pt.append(temp)

    return pt
