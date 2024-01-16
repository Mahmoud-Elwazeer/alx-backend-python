#!/usr/bin/env python3
import asyncio

async def async_countdown(n):
    while n > 0:
        yield n
        await asyncio.sleep(1)
        n -= 1

# Example usage
async def example():
    async for i in async_countdown(5):
        print(i)

# Run the event loop
asyncio.run(example())
