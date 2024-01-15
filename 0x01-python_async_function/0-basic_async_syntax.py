#!/usr/bin/env python3
"""import modules"""
import asyncio
import random


async def wait_random(max_delay=10):
    """random delay between 0 and max_delay"""
    val = 10 * random.random()

    await asyncio.sleep(val)

    return val
