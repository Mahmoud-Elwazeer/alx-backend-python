#!/usr/bin/env python3
""" type-annotated function to_kv"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """out-> 1st: string, 2nd: square of int or float"""
    return (k, v**2)
