#!/usr/bin/env python3
"""9. Let's duck type an iterable object"""


from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ list of tuples, each tuple contains
        a sequence and its length.
    """
    print(reveal_type([(i, len(i)) for i in lst]))
    return [(i, len(i)) for i in lst]
