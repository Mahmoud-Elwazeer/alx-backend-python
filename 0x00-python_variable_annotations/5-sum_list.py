#!/usr/bin/env python3
""" type-annotated function sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """sum list"""
    sum = 0
    for i in input_list:
        sum += i

    return sum
