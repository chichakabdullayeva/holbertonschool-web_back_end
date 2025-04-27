#!/usr/bin/env python3
"""Module for function that multiplies"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function that returns a function that multiplies"""
    def func(x: float) -> float:
        return x * multiplier
    return func
