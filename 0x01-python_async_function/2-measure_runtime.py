#!/usr/bin/env python3
"""import modules"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ measure an approximate elapsed time."""
    s: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed: float = time.perf_counter() - s

    return elapsed / n
