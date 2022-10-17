"""
Zadatak 4.
. Funkcija prima dvije liste, provjerava dal su istih duljina, ako nisu raise-a
Error. Vraća novu listu uspoređujući elemente na istim indeksima. Ako
su vrijednosti iste, vraća taj element, ako nisu vraća -1 na toj poziciji.
(Funkcija mora imati dvije linije)
Ispis: [1,2,3,4,5],[2,2,4,4,5] -> [-1, 2, -1, 4, 5]
"""

def func(l1,l2):
    assert len(l1)==len(l2)
    return [e1 if e1==e2 else -1 for e1, e2 in zip(l1, l2)]

print(func([1,2,3,4,5],[2,2,4,4,5]))