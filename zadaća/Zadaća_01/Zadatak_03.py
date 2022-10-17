"""
Zadatak 3.
Funkcija uzima listu dictionary-a o artiklima. Provjerava je li parametar
lista, ak ne error. Provjerava jesu li svi elementi dictionary, ako ne error.
Provjerava imaju li svi dictionary odgovarajuća 3 ključeva, ako ne error.
("cijena","naziv","kolicina") (Moze i u dvije linije) Vraća novi nested
dictionary s ključem "ukupno" i dictionary sa ključem "artikli" i listom
svih odabranih artikala te "cijena" s ukupnom cijenom računa. (Ne treba
biti One-liner)
Ispis: 
[{"cijena":8,"naziv":"Kruh","kolicina":1}, 
{"cijena":13,"naziv":"Sok","kolicina":2}, 
{"cijena":7,"naziv":"Upaljac","kolicina":1}] 

-> {'ukupno': {'artikli': ['Kruh', 'Sok', 'Upaljac'], 'cijena': 41}}
"""
def func(ld):
    assert isinstance(ld, list)
    assert [e for e in ld if isinstance(e, dict)]
    assert len([e for e in ld if "cijena" in e and "naziv" in e and "kolicina" in e]) == len(ld)
    return {"ukupno" : {"artikli": [e["naziv"] for e in ld], "cijena": sum(e["kolicina"]*e["cijena"] for e in ld)}}

print(func( [{"cijena":8,"naziv":"Kruh","kolicina":1}, {"cijena":13,"naziv":"Sok","kolicina":2},
{"cijena":7,"naziv":"Upaljac","kolicina":1}]))
