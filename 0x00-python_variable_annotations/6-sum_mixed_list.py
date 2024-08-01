#!/usr/bin/env python3
""" Complex types - mixed list """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
        sum_mixed_list func - takes a list of integers and floats
        returns: sum of the list in float
    """
    result: float = 0.0

    for val in mxd_lst:
        result += val

    return result
