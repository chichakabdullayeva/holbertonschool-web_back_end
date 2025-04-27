#!/usr/bin/env python3
"""Module for function that finds element length."""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Function that finds element length."""
    return [(i, len(i)) for i in lst]
