studenti = [
    {
        "name": "Marko",
        "kolegij": ["RS"]
    },
    {
        "name": "Ana",
        "kolegiji": ["WA","RS"]
    },
    {
        "name": "Hrvoje",
        "kolegiji": ["PI"]
    }
]

print("===============================NORMAL====================================")
#rez = ["Marko", "Ana", "Hrvoje"]
rez = []

for student in studenti:
    rez.append(student["name"])

print(rez)

print("===============================ONELINER==================================")

rez2 = [student["name"] for student in studenti ]

print(rez2)

print("===============================NORMAL====================================")

#rez3 = {
#    "Marko": True,
#    "Ana": True,
#    "Hrvoje": True
#}

rez3 = {}

for s in studenti:
    rez3[s["name"]] = True
print(rez3)

print("===============================ONELINER==================================")

rez3 = { s["name"]: True for s in studenti}

print(rez3)