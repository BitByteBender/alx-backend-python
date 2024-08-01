#!/usr/bin/env python3
""" Complex types - functions """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        make_multiplier func - takes a float arg
        returns: a function that multiplies a float by given multiplier
    """
    def multiplier_func(val: float) -> float:
        return val * multiplier

    return multiplier_func
