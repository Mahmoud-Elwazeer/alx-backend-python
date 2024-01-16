#!/usr/bin/env python3
"""import modules"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    task: asyncio.Task = [async_comprehension() for i in range(4)]
    s: float = time.perf_counter()
    result: asyncio.Task = await asyncio.gather(*task)
    elapsed: float = time.perf_counter() - s

    return elapsed


