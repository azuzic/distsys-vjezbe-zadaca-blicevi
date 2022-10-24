import asyncio

async def myFunc_1():
    for x in range(10):
        await asyncio.sleep(0.2)
        print("JEDAN: ", x)
    return ["JEDAN"]

async def myFunc_2():
    for x in range(20):
        await asyncio.sleep(0.1)
        print("DVA: ", x+10)
    return ["DVA"]

def myFunc_3():
    for x in range(10):
        print("TRI: ", x-987)
    return ["TRI"]

async def main():
    var1 = asyncio.create_task(myFunc_1())
    var2 = asyncio.create_task(myFunc_1())
    var3 = asyncio.create_task(myFunc_1())
    myFunc_3()
    await myFunc_2()
    res = await asyncio.gather(var1,var2,var3)
    print(res)

if __name__ == "__main__":
    asyncio.run(main())