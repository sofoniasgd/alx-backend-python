#!/usr/bin/env python3
""" 8. Complex types - functions"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ a type-annotated function make_multiplier that takes
        a float multiplier as argument and returns a function that
        multiplies a float by multiplier.
        Args:
            multiplier: float
        Return
            a function that multiples usng "multiplier"
    """
    def multiplier_fun(input_number: float) -> float:
        multiple: float = multiplier
        return input_number * multiple

    return multiplier_fun
