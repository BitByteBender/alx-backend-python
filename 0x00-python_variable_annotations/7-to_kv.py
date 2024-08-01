#!/usr/bin/env python3
""" Complex types - string and int/float to tuple """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        to_kv func - takes a string and a (integer or float)
        returns: a tuple
    """
    return (k, float(v**2))
