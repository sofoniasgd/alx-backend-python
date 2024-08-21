#!/usr/bin/env python3
"""7. Complex types - string and int/float to tuple"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """a type-annotated function to_kv that takes a
        Args:
            k: str
            v: int OR float
        Return: a tuple.
            The first element of the tuple is the string k.
            The second element is the square of the int/float v
            and should be annotated as a float.
    """
    return (k, (v ** 2))
