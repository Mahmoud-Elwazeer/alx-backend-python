#!/usr/bin/env python3
"""import modules"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """random delay between 0 and max_delay"""
    val = max_delay * random.random()

    await asyncio.sleep(val)

    return val
