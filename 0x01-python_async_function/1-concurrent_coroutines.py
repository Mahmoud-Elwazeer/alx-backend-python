#!/usr/bin/env python3
"""import modules"""
import asyncio
from typing import List, Sequence

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """the list of all the delays (float values). T"""
    out: List[float] = []

    for i in range(n):
        out.append(await wait_random(max_delay))

    out = sorted(out)
    return out
