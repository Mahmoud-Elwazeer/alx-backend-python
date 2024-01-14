#!/usr/bin/env python3
"""import modules"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """multiplies a float by multiplier"""
    out: Callable[[float], float] = multiplier**2

    return out
