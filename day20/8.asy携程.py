import asyncio
async def test1():
    print('hello')
    await asyncio.sleep(1)
    print('world')
    await asyncio.sleep(1)
async def test2():
    print('bye')

asyncio.run(test1())
asyncio.run(test2())

