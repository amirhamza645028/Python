import asyncio
from asyncio import sleep

async def long_running(t):
    print("Starting .....")
    await sleep(t)
    print("Ending .....")

print("Hi")
# Task - 1
t1 = asyncio.create_task(long_running(5))
print("one")
print("two")
print("three")
# Task - 2
t2 = asyncio.create_task(long_running(5))

asyncio.gather([t1, t2])