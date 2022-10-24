import asyncio
import random

async def myFunc_1():
    return [{"artikl":"Kava"},{"artikl":"Voda"}]

async def myFunc_2(ld):
    assert isinstance(ld, list)
    for e in ld:
        assert isinstance(e, dict)
    return [ dict(e, **{'Cijena': random.randrange(1, 11)}) for e in ld]

async def main():
    v =  await myFunc_1()
    print (await myFunc_2(v))

if __name__ == "__main__":
    asyncio.run(main())