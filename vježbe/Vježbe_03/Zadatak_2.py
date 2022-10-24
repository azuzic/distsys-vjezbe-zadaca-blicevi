import asyncio

async def myFunc_1(l):
    assert isinstance(l, list)
    return [ {"korisnik": value , "id" : index} for index,value in enumerate(l)]

async def myFunc_2():
    for n in range(1,10):
        print(n)
        await asyncio.sleep(0.01)

async def myFunc_3(ld):
    assert isinstance(ld, list) and all([isinstance(d, dict)] for d in ld) and all("korisnik" in d and "id" in d for d in ld)
    await asyncio.sleep(0.05)
    return [ (v["korisnik"],v["id"], len(v["korisnik"]) ) for v in ld]

async def main():
    imena = ["Ivan", "Pero"]
    korisnici = await myFunc_1(imena)
    asyncio.create_task(myFunc_2())
    korisnici2 = await myFunc_3(korisnici)
    print(korisnici2)

if __name__ == "__main__":
    asyncio.run(main())