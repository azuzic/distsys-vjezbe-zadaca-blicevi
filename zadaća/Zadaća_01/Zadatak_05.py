"""
Zadatak 5.
Funkcija prima listu tuple-a o studentima (id, ime, prezime). Vraća novu
sortiranu po id-u (manji->veci) listu dictionary-a o studentima kojima ime
i prezime počinje istim slovom. (One-liner u return-u)
Ispis : [(121,"Ivan","Ivic"),(431,"Pero","Horvat"),(31,"Marija","Maric")]
-> [{'id': 31, 'ime': 'Marija', 'prezime': 'Maric'}, {'id': 121, 'ime':
'Ivan', 'prezime': 'Ivic'}]
"""

def func(t):
    return sorted([{"id": e[0], "ime": e[1], "prezime": e[2]} for e in t if e[1][0] == e[2][0]], key=lambda d: d['id'])

print(func([(121,"Ivan","Ivic"),(431,"Pero","Horvat"),(31,"Marija","Maric")]))