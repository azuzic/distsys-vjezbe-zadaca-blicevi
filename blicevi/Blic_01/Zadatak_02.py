"""
Zadatak 2.
{"valute":["GBP","USD","CZK","Error"],"cijena":[8.5,7.7,0.3,10.3]},
{"valute":["EUR","USD","CZK","Error"],"cijena":[7.5,7.7,0.3,5.5]}
-> [(7.7,'USD'),(0.3,'CZK')]
"""

def func(d1,d2):
    assert isinstance(d1, dict) and isinstance(d2, dict)
    assert isinstance(d1["valute"], list) and isinstance(d2["valute"], list)
    assert isinstance(d1["valute"], list) and isinstance(d2["valute"], list)
    assert "valute" in d1 and "cijena" in d1 and "valute" in d2 and "cijena" in d2
    return (e1 for e1,e2 in (d1,d2) if e1["valute"])

print(func({"valute":["GBP","USD","CZK","Error"],"cijena":[8.5,7.7,0.3,10.3]}, {"valute":["EUR","USD","CZK","Error"],"cijena":[7.5,7.7,0.3,5.5]}))