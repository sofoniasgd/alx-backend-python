#!/usr/bin/env python3
"""10. Duck typing - first element of a sequence"""

from typing


# The types of the elements of the input are not know
def safe_first_element(lst: Iterable) -> :
    """ 
    """
    if lst:
        return lst[0]
        else:
    return None
