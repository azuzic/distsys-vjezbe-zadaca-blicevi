"""
Zadatak 3.
Funkcija prima listu dictionary-a IP adresa, kreira set od vrijednosti.
(One-liner u return-u)
Ispis: [{“ip”:“192.168.3.1”}, {“ip”:“10.0.0.0”}, {“ip”:“127.0.0.0”},
{“ip”:“192.168.3.1”}] -> {‘10.0.0.0’, ‘192.168.3.1’, ‘127.0.0.0’}
"""

def func(list_of_distionaries):
     return{value for dictionary in list_of_distionaries for _,value in dictionary.items()}

print(func([{"ip":"192.168.3.1"}, {"ip":"10.0.0.0"}, {"ip":"127.0.0."}, {"ip":"192.168.3.1"}]))
