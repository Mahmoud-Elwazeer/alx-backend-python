#!/usr/bin/env python3
"""import modules"""
from typing import Union, Any, Mapping


def safely_get_value(dct: Mapping, key: Any, default = None):
    if key in dct:
        return dct[key]
    else:
        return default
