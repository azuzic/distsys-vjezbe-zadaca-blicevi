"""
Kreirajte jednu asinkronu (afun1) i jednu sinkronu (fun2) funkciju, te
funkciju main. Unutar funkcije main, kreiraju se tri datoteke u radnom
direktoriju te se nazivi spremaju u listu.

[“datoteka1”, “datoteka2”, “datoteka3”]

Nakon toga poziva se afun1 koja uzima parametar lista naziva datoteka.
Čeka 0.2 sekunde i vraća listu dictionary-a, gdje svaki dictonary sadrži
naziv datoteke te njenu veličinu u byte-ovima.

[{“naziv”:“datoteka1”, “velicina”:1212},{“naziv”:“datoteka2”, “velicina”:8912},{“naziv”:“datoteka3”, “velicina”:2212}]

Odmah nakon afun1, unutar main-a poziva se fun2 koja prima listu naziva
datoteka. Unutar nje, u svaku datoteku upisuje brojeve od 1 do 10 000.
Na kraju main-a čeka se rezultat iz afun1 koji se ispisuje u konzolu.

(Hint: os package)
"""

import asyncio
import os

async def afun1(list):
    await asyncio.sleep(0.2)
    return [{ "naziv":i, "velicina": os.path.getsize(i+".txt")} for i in list]

def fun2(list):
    for n in list:
        fd = open(n+".txt", "a")
        for i in range(1,10000+1):
            fd.write(str(i)+ "\n")

async def main():
    list = []
    for i in range(1,4):
        name = 'datoteka'+str(i)
        with open(name+'.txt', 'w') as fp:
            list.append(name)

    res = asyncio.create_task(afun1(list))
    fun2(list)
    await res
    print(res)



if __name__ == "__main__":
    asyncio.run(main())