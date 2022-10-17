"""
Zadatak 1.
Ispis ["Stol", "Stolica", "Krevet", "Fotelja"] -> {0: 'lotS', ,: 'acilotS', 2: 'teverK', 3:'ajletoF'}
"""

def func(l):
    assert isinstance(l, list) and len([e for e in l if isinstance(e, str)]) == len(l)
    return {l.index(key) : value[::-1] for key,value in zip(l,l)}

print(func(["Stol", "Stolica", "Krevet", "Fotelja"]))