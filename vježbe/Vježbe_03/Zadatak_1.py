import asyncio
import random

async def myFunc_1():
    return [{"artikl": v} for v in ["Kava", "Voda"] ] 

async def myFunc_2(ld):
    assert isinstance(ld, list) and all([isinstance(d, dict)] for d in ld)
    return [ dict(e, **{'Cijena': random.randrange(1, 11)}) for e in ld]

async def main():
    artikli  =  await myFunc_1()
    final = await myFunc_2(artikli)
    print(final)

if __name__ == "__main__":
    asyncio.run(main())