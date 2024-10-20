import asyncio
from packages import greet

print(greet('pavel'))
async def joke():
    for i in range(100):
        print(i, " hello")
    await asyncio.sleep(3)

async def a():
    for i in range(100):
        print(i)
    print("Timing!")

async def main():
    await asyncio.gather(joke(),a())

asyncio.run(main())
