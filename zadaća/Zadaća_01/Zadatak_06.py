"""
Zadatak 6.
Funkciji se predaju dva parametra. Provjera se jesu li parametri istog tipa,
ako ne error. Provjeri se jesu li parametri liste ili dictionary, ako ne error.
Vraća se spojena lista ili dictionary.
Ispis : [1,2,1,2],[3,2] -> [1,2,1,2,3,2]
Ispis : {1:2,3:2},{5:2,4:1} -> {1: 2, 3: 2, 5: 2, 4: 1}
"""

def func(p1, p2):
    assert type(p1) == type(p2)
    assert isinstance(p1, list) or isinstance(p1, dict) and isinstance(p2, list) or isinstance(p2, dict)
    if isinstance(p1, list):
        return list(zip(p1,p2))
    else:
        return dict(zip(p1,p2))

print(func([1,2,1,2],[3,2])) 

print(func({1:2,3:2},{5:2,4:1})) 