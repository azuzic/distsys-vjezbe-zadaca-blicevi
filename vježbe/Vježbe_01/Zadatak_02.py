"""
Zadatak 2.
Funckija uzima dvije liste, ako su liste iste duljine vraća dictionary gdje
su key vrijednost iz prve list, a value vrijednosti iz druge liste. Ako nisu
vraća prazan dictionary. (One-liner u return-u)
Ispis: [1,2,3], [4,3,2] -> {1: 4, 2: 3, 3: 2}
"""

def func(list_1, list_2):
    return {key : value for key,value in zip(list_1, list_2) if len(list_1)==len(list_2)}

print(func([1,2,3], [4,3,2]))