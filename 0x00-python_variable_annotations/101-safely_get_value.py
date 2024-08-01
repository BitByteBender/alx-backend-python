#!/usr/bin/env python3
""" More involved type annotations """
from typing import Union, Any, Mapping, TypeVar


typv = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[typv, None] = None) -> Union[Any, typv]:
    """
        Retrieves the value for a given key from the dict if key exists.
        Otherwise returns default value
    """
    if key in dct:
        return dct[key]
    else:
        return default
