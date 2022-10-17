"""
Zadatak 2.
Funkcija uzima listu i dictionary. Provjeri jesu li lista i dictionary, ako ne
error. Provjeri imaju li isti broj elemenata. Provjeri jesu li svi elementi
liste tipa integer. Vraća novi dictionary, gdje je value element iz liste na
tom indexu ako se nalazi unutar [5,10] ako ne upisuje -1.
Ispis : [8,7,1], {1:2,2:1,3:2} -> {1: 8, 2: 7, 3: -1}
"""

from re import L


def func(l, d):
    assert isinstance(l, list)
    assert isinstance(d, dict)
    assert len(l) == len(d)
    for e in l:
        assert isinstance(e, int)
    return {key : value for key,value in zip(d.keys(), [ e if e >=5 and e <=10 else e*0-1 for e in l ])}

print(func([8,7,1], {1:2,2:1,3:2}))