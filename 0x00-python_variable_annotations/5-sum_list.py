#!/usr/bin/env python3
""" Complex types - list of floats """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
        sum_list func - takes a list of floats as arg
        returns: sum of list of float values
    """
    result: float = 0.0

    for idx in input_list:
        result += idx

    return result
