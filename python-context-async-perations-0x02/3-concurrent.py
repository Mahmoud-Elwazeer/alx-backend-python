#!/usr/bin/python3

"""Run multiple database queries concurrently using asyncio.gather.
"""

import aiosqlite
import asyncio

# fetch users
async def async_fetch_users():
    async with aiosqlite.connect("users.db") as db:
        async with db.execute('SELECT * FROM users') as cursor:
            rows = await cursor.fetchall()
            for row in rows:
                print(row)
            return rows

# Async function to fetch users older than 40
async def async_fetch_older_users():
    async with aiosqlite.connect("users.db") as db:
        async with db.execute('SELECT * FROM users WHERE age > 40') as cursor:
            rows = await cursor.fetchall()
            print("Users older than 40:")
            for row in rows:
                print(row)
            return rows


async def fetch_concurrently():
    await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )

asyncio.run(fetch_concurrently())