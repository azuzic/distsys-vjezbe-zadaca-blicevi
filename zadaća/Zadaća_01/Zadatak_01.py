"""
Zadatak 1.
Funkcija uzima listu string-ova. Provjeri dal su sve stringovi, ako ne error.
Vraća novu listu, gdje su string-ovi duži od 4 znaka. (Funkcija od dvije
linije)
Ispis: [“Pas”, “Macka”, “Stol”] -> [“Macka”]
"""
def func(list):
     for e in list: assert isinstance(e, str)
     return [e for e in list if len(e)>4]

print(func(["Pas", "Macka", "Stol"]))
