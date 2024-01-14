#!/usr/bin/env python3
"""import modules"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """multiplies a float by multiplier"""
    def mul_func(x: float) -> float:
        return x * multiplier

    return mul_func
